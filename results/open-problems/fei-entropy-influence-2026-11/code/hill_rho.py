"""Local search for Boolean functions whose BEST coordinate is still bad (FLOW.md section 7).

For Boolean f (+-1) on n variables, coordinate i, a = fhat(T), b = fhat(T+i) (T without i):
  D_i = H(f) - H(f|x_i=+1)/2 - H(f|x_i=-1)/2      (restrictions have spectra (a+b)^2 and (a-b)^2)
  E_i = sum_T (a^2+b^2) h(b^2/(a^2+b^2))            (= H(1[i in U] | U - i))
  Inf_i = sum_T b^2
  rhoD(f) = min over i with Inf_i > 0 of D_i/Inf_i,   rhoE likewise with E_i.
R := sup_f rhoD(f) is an upper bound for the FEI constant (induction along a decision tree), and FEI <=> R < infinity.
The search maximises one of: rhoD, rhoE, HI (= H/I), HmI (= sum_i E_i / I), PsiI (= sum_i D_i / I).

Moves: flip one truth-table bit (all 2^n neighbours evaluated in one batch), steepest ascent, random restarts,
with a few random double flips to leave plateaus. Functions are required to depend on every variable.

Usage: python hill_rho.py n objective seconds seed outdir [start]
   start: random (default) | sparse | tribes | file:PATH (hex truth tables, one per line, bit x set when f(x) = -1)
Writes outdir/best_n{n}_{objective}_s{seed}.txt (rewritten at every improvement) and a progress line per restart.
Stop file: outdir/STOP.
"""
import sys
import os
import time
import math
import numpy as np


def wht(f, n):
    """rows are functions; returns Fourier coefficients (normalised)."""
    a = f.astype(np.float64).copy()
    N = 1 << n
    h = 1
    while h < N:
        a = a.reshape(a.shape[0], -1, 2, h)
        x = a[:, :, 0, :] + a[:, :, 1, :]
        y = a[:, :, 0, :] - a[:, :, 1, :]
        a = np.stack([x, y], axis=2).reshape(a.shape[0], N)
        h *= 2
    return a / N


def eta(x):
    return np.where(x > 1e-300, -x * np.log2(np.maximum(x, 1e-300)), 0.0)


def measures(f, n):
    """f: (batch, 2^n) of +-1. Returns dict of arrays (batch,) and per-coordinate arrays (batch, n)."""
    N = 1 << n
    fh = wht(f, n)
    mu = fh * fh
    H = eta(mu).sum(axis=1)
    idx = np.arange(N)
    D = np.zeros((f.shape[0], n))
    E = np.zeros((f.shape[0], n))
    Inf = np.zeros((f.shape[0], n))
    for i in range(n):
        lo = idx[(idx >> i) & 1 == 0]
        a = fh[:, lo]
        b = fh[:, lo | (1 << i)]
        a2 = a * a
        b2 = b * b
        Inf[:, i] = b2.sum(axis=1)
        E[:, i] = (eta(a2) + eta(b2) - eta(a2 + b2)).sum(axis=1)
        Hu = eta((a + b) ** 2).sum(axis=1)
        Hv = eta((a - b) ** 2).sum(axis=1)
        D[:, i] = H - 0.5 * Hu - 0.5 * Hv
    I = Inf.sum(axis=1)
    live = Inf > 1e-12
    alldep = live.all(axis=1)
    big = 1e9
    rD = np.where(live, D / np.maximum(Inf, 1e-300), big).min(axis=1)
    rE = np.where(live, E / np.maximum(Inf, 1e-300), big).min(axis=1)
    safeI = np.maximum(I, 1e-300)
    out = {"H": H, "I": I, "rhoD": rD, "rhoE": rE, "HI": H / safeI, "HmI": E.sum(axis=1) / safeI,
           "PsiI": D.sum(axis=1) / safeI, "alldep": alldep, "Inf": Inf, "D": D, "E": E}
    for k in ("rhoD", "rhoE", "HI", "HmI", "PsiI"):
        out[k] = np.where(alldep, out[k], -1.0)
    return out


def tohex(f):
    bits = (f < 0)
    v = 0
    for x in np.nonzero(bits)[0]:
        v |= 1 << int(x)
    return "%x" % v


def fromhex(s, n):
    v = int(s, 16)
    N = 1 << n
    return np.array([-1.0 if (v >> x) & 1 else 1.0 for x in range(N)])


def start_fn(kind, n, rng):
    N = 1 << n
    if kind == "sparse":
        d = rng.choice([0.03, 0.06, 0.12, 0.25])
        return np.where(rng.random(N) < d, -1.0, 1.0)
    if kind == "tribes":
        w = int(rng.integers(2, 4))
        pts = (np.arange(N)[:, None] >> np.arange(n)[None, :]) & 1
        perm = rng.permutation(n)
        s = n // w
        val = np.zeros(N, dtype=bool)
        for t in range(s):
            val |= pts[:, perm[t * w:(t + 1) * w]].all(axis=1)
        f = np.where(val, -1.0, 1.0)
        k = int(rng.integers(0, 4))
        for x in rng.integers(0, N, size=k):
            f[x] = -f[x]
        return f
    d = rng.choice([0.5, 0.35, 0.2])
    return np.where(rng.random(N) < d, -1.0, 1.0)


def main():
    n = int(sys.argv[1])
    obj = sys.argv[2]
    seconds = float(sys.argv[3])
    seed = int(sys.argv[4])
    outdir = sys.argv[5]
    start = sys.argv[6] if len(sys.argv) > 6 else "random"
    os.makedirs(outdir, exist_ok=True)
    N = 1 << n
    rng = np.random.default_rng(seed)
    pool = None
    if start.startswith("file:"):
        with open(start[5:], encoding="utf-8") as fh:
            pool = [fromhex(l.split()[0], n) for l in fh if l.strip()]
    t0 = time.time()
    best = -1.0
    bestf = None
    restarts = 0
    outpath = os.path.join(outdir, "best_n%d_%s_s%d.txt" % (n, obj, seed))
    logpath = os.path.join(outdir, "log_n%d_%s_s%d.txt" % (n, obj, seed))
    eye = np.eye(N)
    while time.time() - t0 < seconds and not os.path.exists(os.path.join(outdir, "STOP")):
        if pool is not None:
            f = pool[restarts % len(pool)].copy()
            for x in rng.integers(0, N, size=int(rng.integers(0, 3))):
                f[x] = -f[x]
        else:
            f = start_fn(start, n, rng)
        cur = float(measures(f[None, :], n)[obj][0])
        stall = 0
        while time.time() - t0 < seconds:
            nb = f[None, :] * (1.0 - 2.0 * eye)          # all single flips
            m = measures(nb, n)
            j = int(np.argmax(m[obj]))
            v = float(m[obj][j])
            if v > cur + 1e-12:
                f = nb[j].copy()
                cur = v
                stall = 0
                continue
            # plateau: try random double flips
            stall += 1
            if stall > 3:
                break
            k = min(4096, N * 4)
            xs = rng.integers(0, N, size=(k, 2))
            nb2 = np.repeat(f[None, :], k, axis=0)
            nb2[np.arange(k), xs[:, 0]] *= -1.0
            nb2[np.arange(k), xs[:, 1]] *= -1.0
            m2 = measures(nb2, n)
            j2 = int(np.argmax(m2[obj]))
            if float(m2[obj][j2]) > cur + 1e-12:
                f = nb2[j2].copy()
                cur = float(m2[obj][j2])
                stall = 0
        restarts += 1
        m = measures(f[None, :], n)
        line = "restart %d  t=%.0fs  %s=%.6f  H/I=%.4f rhoD=%.4f rhoE=%.4f HmI=%.4f PsiI=%.4f I=%.4f  tt=%s" % (
            restarts, time.time() - t0, obj, cur, float(m["HI"][0]), float(m["rhoD"][0]), float(m["rhoE"][0]),
            float(m["HmI"][0]), float(m["PsiI"][0]), float(m["I"][0]), tohex(f))
        with open(logpath, "a", encoding="utf-8") as fh:
            fh.write(line + "\n")
        if cur > best:
            best = cur
            bestf = f.copy()
            with open(outpath, "w", encoding="utf-8") as fh:
                fh.write(line + "\n")
                fh.write("Inf: " + " ".join("%.6f" % x for x in m["Inf"][0]) + "\n")
                fh.write("D/Inf: " + " ".join("%.4f" % (x / max(y, 1e-300)) for x, y in zip(m["D"][0], m["Inf"][0])) + "\n")
                fh.write("E/Inf: " + " ".join("%.4f" % (x / max(y, 1e-300)) for x, y in zip(m["E"][0], m["Inf"][0])) + "\n")
    print("done n=%d obj=%s seed=%d restarts=%d best=%.6f" % (n, obj, seed, restarts, best))


if __name__ == "__main__":
    main()
