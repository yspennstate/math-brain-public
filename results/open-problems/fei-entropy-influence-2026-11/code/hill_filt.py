"""Local search for Boolean functions whose best filtration witness is large (FLOW section 12).

rhoF(f) = min over coordinates i and orderings pi of the other coordinates of  L^pi_i / Inf_i,
L^pi_i = sum_k Phi(A_k, B_k) with A_k, B_k the weights of fhat(T)^2, fhat(T + i)^2 on the sets T whose last element
in the ordering is the k-th (see filt_cs.py).  E_i <= L^pi_i, so FEI holds with constant sup_f rhoF + 2/ln 2 if the
supremum is finite.  The search maximises rhoF (objective rhoF) or rhoF - rhoE (objective gap).

Usage: python hill_filt.py n objective seconds seed outdir [start]
   start: random | sparse | tribes | file:PATH   (as in hill_rho.py)
Writes outdir/bestF_n{n}_{objective}_s{seed}.txt and logF_...txt.  Stop file: outdir/STOP.
"""
import sys
import os
import time
import numpy as np
from hill_rho import wht, eta, start_fn, tohex, fromhex

_PLAN = {}


def plan(m):
    """index lists for the subset DP on m coordinates."""
    if m not in _PLAN:
        size = 1 << m
        idx = np.arange(size)
        pc = np.zeros(size, dtype=np.int64)
        for j in range(m):
            pc += (idx >> j) & 1
        steps = []
        for layer in range(1, m + 1):
            R = idx[pc == layer]
            for j in range(m):
                sel = R[(R >> j) & 1 == 1]
                steps.append((sel, sel ^ (1 << j)))
        _PLAN[m] = steps
    return _PLAN[m]


def zeta(v, m):
    a = v.copy()
    B = a.shape[0]
    for j in range(m):
        a = a.reshape(B, -1, 2, 1 << j)
        a[:, :, 1, :] += a[:, :, 0, :]
        a = a.reshape(B, -1)
    return a


def phi(p, q):
    return eta(p) + eta(q) - eta(p + q)


def rho(fb, n):
    """fb: (batch, 2^n) of +-1.  Returns rhoF, rhoE (batch,), -1 where f does not depend on every variable."""
    B = fb.shape[0]
    mu = wht(fb, n) ** 2
    idx = np.arange(1 << n)
    m = n - 1
    steps = plan(m)
    rF = np.full(B, 1e9)
    rE = np.full(B, 1e9)
    alldep = np.ones(B, dtype=bool)
    for i in range(n):
        lo = idx[(idx >> i) & 1 == 0]
        p = mu[:, lo]
        q = mu[:, lo | (1 << i)]
        inf = q.sum(axis=1)
        live = inf > 1e-12
        alldep &= live
        E = phi(p, q).sum(axis=1)
        a = zeta(p, m)
        b = zeta(q, m)
        best = np.full((B, 1 << m), np.inf)
        best[:, 0] = phi(a[:, 0], b[:, 0])
        for sel, prev in steps:
            da = np.maximum(a[:, sel] - a[:, prev], 0.0)
            db = np.maximum(b[:, sel] - b[:, prev], 0.0)
            cand = best[:, prev] + phi(da, db)
            best[:, sel] = np.minimum(best[:, sel], cand)
        safe = np.maximum(inf, 1e-300)
        rF = np.minimum(rF, np.where(live, best[:, -1] / safe, 1e9))
        rE = np.minimum(rE, np.where(live, E / safe, 1e9))
    rF = np.where(alldep, rF, -1.0)
    rE = np.where(alldep, rE, -1.0)
    return rF, rE


def score(fb, n, obj):
    rF, rE = rho(fb, n)
    if obj == "gap":
        return np.where(rF >= 0, rF - rE, -1.0), rF, rE
    return rF, rF, rE


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
            pool = [fromhex(l.split()[-1], n) for l in fh if l.strip()]
    t0 = time.time()
    best = -1.0
    restarts = 0
    outpath = os.path.join(outdir, "bestF_n%d_%s_s%d.txt" % (n, obj, seed))
    logpath = os.path.join(outdir, "logF_n%d_%s_s%d.txt" % (n, obj, seed))
    eye = np.eye(N)
    chunk = max(1, min(N, (1 << 22) // (1 << (n - 1))))      # keep the DP arrays under about 32 MB each

    def batch_score(fb):
        outs = [score(fb[s:s + chunk], n, obj) for s in range(0, fb.shape[0], chunk)]
        return tuple(np.concatenate([o[k] for o in outs]) for k in range(3))

    while time.time() - t0 < seconds and not os.path.exists(os.path.join(outdir, "STOP")):
        if pool is not None:
            f = pool[restarts % len(pool)].copy()
            for x in rng.integers(0, N, size=int(rng.integers(0, 3))):
                f[x] = -f[x]
        else:
            f = start_fn(start, n, rng)
        cur = float(batch_score(f[None, :])[0][0])
        stall = 0
        while time.time() - t0 < seconds:
            nb = f[None, :] * (1.0 - 2.0 * eye)
            v = batch_score(nb)[0]
            j = int(np.argmax(v))
            if float(v[j]) > cur + 1e-12:
                f = nb[j].copy()
                cur = float(v[j])
                stall = 0
                continue
            stall += 1
            if stall > 3:
                break
            k = min(2048, N * 4)
            xs = rng.integers(0, N, size=(k, 2))
            nb2 = np.repeat(f[None, :], k, axis=0)
            nb2[np.arange(k), xs[:, 0]] *= -1.0
            nb2[np.arange(k), xs[:, 1]] *= -1.0
            v2 = batch_score(nb2)[0]
            j2 = int(np.argmax(v2))
            if float(v2[j2]) > cur + 1e-12:
                f = nb2[j2].copy()
                cur = float(v2[j2])
                stall = 0
        restarts += 1
        s, rF, rE = batch_score(f[None, :])
        line = "restart %d  t=%.0fs  %s=%.6f  rhoF=%.4f rhoE=%.4f  tt=%s" % (
            restarts, time.time() - t0, obj, cur, float(rF[0]), float(rE[0]), tohex(f))
        with open(logpath, "a", encoding="utf-8") as fh:
            fh.write(line + "\n")
        if cur > best:
            best = cur
            with open(outpath, "w", encoding="utf-8") as fh:
                fh.write(line + "\n")
    print("done n=%d obj=%s seed=%d restarts=%d best=%.6f" % (n, obj, seed, restarts, best))


if __name__ == "__main__":
    main()
