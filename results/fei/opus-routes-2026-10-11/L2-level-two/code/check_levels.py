"""Numerical checks for route L2 (level two and above of the B functional).

Exact Fourier spectra by fast Walsh-Hadamard transform; logs base 2.
Checks, for every function examined:
  A096   d1_i <= 2 eps_i^2 ln(2/eps_i),  H2 <= K2 I (K2 = 3.0484),  B_1 <= 7.540 I
  HC     d_{k-1,i} <= eps^(2-2/q) (q-1)^(k-1) for q = max(2, ln(1/eps)) (k = 2, 3)
  L3     H3 <= 7.985 I,  B_2 <= 25.40 I (candidate level 2->3 bound)
  B13    J_i <= B_i,  G <= B <= G + (log2 e) I  (G = sum_S p(S) sum_{i in S} log(1 + p(S-i)/p(S)))
and records the extreme ratios.  Usage: python check_levels.py OUTDIR [--quick]
"""
import os, sys, json, math, time
os.environ.setdefault("OMP_NUM_THREADS", "2")
import numpy as np

try:  # BelowNormal priority, proper handle types
    import ctypes
    from ctypes import wintypes
    _k32 = ctypes.WinDLL("kernel32", use_last_error=True)
    _k32.GetCurrentProcess.restype = wintypes.HANDLE
    _k32.SetPriorityClass.argtypes = [wintypes.HANDLE, wintypes.DWORD]
    _k32.SetPriorityClass.restype = wintypes.BOOL
    _k32.SetPriorityClass(_k32.GetCurrentProcess(), 0x4000)
except Exception:
    pass

LN2 = math.log(2.0)
LOG2E = 1.0 / LN2
K2 = 8 / (math.e ** 2 * LN2) + 2 / math.e + math.sqrt(2) / (math.e * LN2)
T12C = 2 * K2 + LOG2E
H3C = 7.985
T23C = 25.40


def fwht(a):
    a = np.array(a, dtype=np.float64, copy=True)
    M, N = a.shape
    h = 1
    while h < N:
        a = a.reshape(M, N // (2 * h), 2, h)
        x = a[:, :, 0, :].copy()
        a[:, :, 0, :] = x + a[:, :, 1, :]
        a[:, :, 1, :] = x - a[:, :, 1, :]
        a = a.reshape(M, N)
        h *= 2
    return a / N


def eta(x):
    """-x log2 x, 0 at 0 (vectorised)."""
    out = np.zeros_like(x)
    m = x > 1e-300
    out[m] = -x[m] * np.log2(x[m])
    return out


_cache = {}


def tables(n):
    if n not in _cache:
        N = 1 << n
        pc = np.array([bin(s).count("1") for s in range(N)])
        idx0 = []
        for i in range(n):
            z = np.array([s for s in range(N) if not (s >> i) & 1])
            idx0.append(z)
        _cache[n] = (pc, idx0)
    return _cache[n]


def analyse(tt):
    """tt: (M, N) array of +-1.  Returns dict of per-function arrays."""
    tt = np.atleast_2d(tt)
    M, N = tt.shape
    n = N.bit_length() - 1
    pc, idx0 = tables(n)
    fh = fwht(tt)
    p = fh * fh
    p[p < 1e-28] = 0.0
    H = eta(p).sum(1)
    I = (p * pc).sum(1)
    eps = np.zeros((M, n))
    for i in range(n):
        eps[:, i] = p[:, idx0[i] | (1 << i)].sum(1)
    Wk = np.zeros((M, n + 1))
    Hk = np.zeros((M, n + 1))
    ep = eta(p)
    for k in range(n + 1):
        Wk[:, k] = p[:, pc == k].sum(1)
        Hk[:, k] = ep[:, pc == k].sum(1)
    Bk = np.zeros((M, n))          # edges (U, U+i) with |U| = k
    Bi = np.zeros((M, n))
    Ji = np.zeros((M, n))
    Gi = np.zeros((M, n))
    d1 = np.zeros((M, n))          # level-1 weight of D_i f
    d2 = np.zeros((M, n))          # level-2 weight of D_i f
    for i in range(n):
        z0 = idx0[i]
        z1 = z0 | (1 << i)
        a, b = p[:, z0], p[:, z1]
        ph = eta(a) + eta(b) - eta(a + b)
        ph[ph < 0] = 0.0
        Bi[:, i] = ph.sum(1)
        lev = pc[z0]
        for k in range(n):
            sel = lev == k
            if sel.any():
                Bk[:, k] += ph[:, sel].sum(1)
        fa, fb = fh[:, z0], fh[:, z1]
        pp, pm = (fa + fb) ** 2, (fa - fb) ** 2
        Ji[:, i] = (eta(a + b) - 0.5 * (eta(pp) + eta(pm))).sum(1)
        g = np.zeros_like(b)
        m = b > 0
        g[m] = b[m] * np.log2((a[m] + b[m]) / b[m])
        Gi[:, i] = g.sum(1)
        d1[:, i] = b[:, lev == 1].sum(1)
        d2[:, i] = b[:, lev == 2].sum(1)
    B = Bi.sum(1)
    return dict(n=n, p=p, H=H, I=I, eps=eps, Wk=Wk, Hk=Hk, Bk=Bk, Bi=Bi, Ji=Ji,
                Gi=Gi, G=Gi.sum(1), B=B, d1=d1, d2=d2)


def hc_bound(eps, k):
    """eps^(2-2/q) (q-1)^(k-1) with q = max(2, ln(1/eps)); bound on the level-(k-1) weight of D_i f."""
    out = np.full_like(eps, np.inf)
    m = eps > 0
    e = eps[m]
    L = np.log(1.0 / e)
    q = np.maximum(2.0, L)
    out[m] = e ** (2 - 2 / q) * (q - 1) ** (k - 1)
    return out


def a096_bound(eps):
    out = np.full_like(eps, np.inf)
    m = eps > 0
    out[m] = 2 * eps[m] ** 2 * np.log(2 / eps[m])
    return out


class Tracker:
    """Keeps the worst ratio per quantity with the function that attains it, plus violation counts."""

    def __init__(self):
        self.best = {}
        self.viol = {}
        self.count = 0

    def ratio(self, name, num, den, tt, tag):
        m = den > 1e-12
        if not m.any():
            return
        r = np.where(m, num / np.where(m, den, 1), -np.inf)
        j = int(np.argmax(r))
        if name not in self.best or r[j] > self.best[name][0]:
            self.best[name] = (float(r[j]), tag, "".join("1" if v < 0 else "0" for v in tt[j]))

    def check(self, name, lhs, rhs, tol=1e-9):
        bad = int(np.sum(lhs > rhs + tol))
        self.viol[name] = self.viol.get(name, 0) + bad

    def feed(self, tt, tag):
        tt = np.atleast_2d(tt)
        R = analyse(tt)
        self.count += tt.shape[0]
        I, n = R["I"], R["n"]
        self.check("A096_d1", R["d1"], a096_bound(R["eps"]))
        self.check("HC_d1", R["d1"], hc_bound(R["eps"], 2))
        self.check("HC_d2", R["d2"], hc_bound(R["eps"], 3))
        self.check("H<=", R["B"], R["H"])          # B <= H
        self.check("J<=B", R["Ji"], R["Bi"])
        self.check("G<=B", R["G"], R["B"])
        self.check("B<=G+log2e*I", R["B"], R["G"] + LOG2E * I)
        if n >= 2:
            self.check("H2<=K2*I", R["Hk"][:, 2], K2 * I)
            self.check("B1<=7.540*I", R["Bk"][:, 1], T12C * I)
        if n >= 3:
            self.check("H3<=7.985*I", R["Hk"][:, 3], H3C * I)
            self.check("B2<=25.40*I", R["Bk"][:, 2], T23C * I)
        self.ratio("B/I", R["B"], I, tt, tag)
        self.ratio("H/I", R["H"], I, tt, tag)
        self.ratio("B0/I", R["Bk"][:, 0], I, tt, tag)
        if n >= 2:
            self.ratio("H2/I", R["Hk"][:, 2], I, tt, tag)
            self.ratio("B1/I", R["Bk"][:, 1], I, tt, tag)
            self.ratio("B>=1/I", R["B"] - R["Bk"][:, 0], I, tt, tag)
        if n >= 3:
            self.ratio("H3/I", R["Hk"][:, 3], I, tt, tag)
            self.ratio("B2/I", R["Bk"][:, 2], I, tt, tag)
        if n >= 4:
            self.ratio("B3/I", R["Bk"][:, 3], I, tt, tag)
        var = 1 - R["p"][:, 0]
        self.ratio("B0/Var", R["Bk"][:, 0], var, tt, tag)
        e = R["eps"]
        with np.errstate(divide="ignore", invalid="ignore"):
            self.ratio("d1/A096bound", np.nanmax(np.where(e > 0, R["d1"] / a096_bound(e), 0), axis=1), np.ones(len(I)), tt, tag)
            self.ratio("d2/HCbound", np.nanmax(np.where(e > 0, R["d2"] / hc_bound(e, 3), 0), axis=1), np.ones(len(I)), tt, tag)
            self.ratio("J/B max coord", np.nanmax(np.where(R["Bi"] > 1e-12, R["Ji"] / np.where(R["Bi"] > 1e-12, R["Bi"], 1), 0), axis=1), np.ones(len(I)), tt, tag)
        return R


def all_functions(n):
    N = 1 << n
    k = np.arange(1 << N, dtype=np.int64)
    bits = (k[:, None] >> np.arange(N)[None, :]) & 1
    return (1 - 2 * bits).astype(np.int8)


def bits_of(n):
    N = 1 << n
    return (np.arange(N)[:, None] >> np.arange(n)[None, :]) & 1   # (N, n) 0/1; 1 means x_j = -1


def fam_bent_times_x0(m):
    n = m + 1
    u = bits_of(n)
    ip = np.zeros(1 << n, dtype=np.int64)
    for j in range(m // 2):
        ip += u[:, 2 * j] * u[:, 2 * j + 1]
    return ((1 - 2 * (ip % 2)) * (1 - 2 * u[:, m])).astype(np.int8)[None, :]


def fam_threshold(n, t):
    u = bits_of(n).sum(1)
    return np.where(u <= t, -1, 1).astype(np.int8)[None, :]


def fam_and(n):
    u = bits_of(n).sum(1)
    return np.where(u == n, -1, 1).astype(np.int8)[None, :]


def fam_tribes(w, s):
    n = w * s
    u = bits_of(n)
    anyt = np.zeros(1 << n, dtype=bool)
    for j in range(s):
        anyt |= u[:, j * w:(j + 1) * w].all(1)
    return np.where(anyt, -1, 1).astype(np.int8)[None, :]


def random_dt(n, depth, rng, M):
    out = np.empty((M, 1 << n), dtype=np.int8)
    u = bits_of(n)
    for r in range(M):
        def build(d, avail):
            if d == 0 or not avail or rng.random() < 0.15:
                return ("leaf", rng.choice([-1, 1]))
            v = rng.choice(avail)
            rest = [a for a in avail if a != v]
            return ("node", v, build(d - 1, rest), build(d - 1, rest))
        tree = build(depth, list(range(n)))
        vals = np.empty(1 << n, dtype=np.int8)
        for x in range(1 << n):
            t = tree
            while t[0] == "node":
                t = t[2] if u[x, t[1]] == 0 else t[3]
            vals[x] = t[1]
        out[r] = vals
    return out


def random_dnf(n, width, terms, rng, M):
    out = np.empty((M, 1 << n), dtype=np.int8)
    u = bits_of(n)
    for r in range(M):
        val = np.zeros(1 << n, dtype=bool)
        for _ in range(terms):
            vs = rng.choice(n, size=width, replace=False)
            sg = rng.integers(0, 2, size=width)
            val |= (u[:, vs] == sg).all(1)
        out[r] = np.where(val, -1, 1)
    return out


def random_ltf(n, rng, M):
    u = 1 - 2 * bits_of(n)
    out = np.empty((M, 1 << n), dtype=np.int8)
    for r in range(M):
        w = rng.standard_normal(n) * rng.exponential(1.0, n)
        th = rng.normal(0, np.abs(w).sum() * 0.3)
        s = u @ w - th
        out[r] = np.where(s >= 0, 1, -1)
    return out


def hill_climb(n, objective, rng, starts, steps, tracker, tag):
    """Greedy single-bit flips maximising objective(R) (vector over a batch). All N flips are scored per step."""
    N = 1 << n
    best_overall = -1.0
    for s in range(starts):
        dens = [0.5, 0.25, 0.125, 0.0625][s % 4]
        f = np.where(rng.random(N) < dens, -1, 1).astype(np.int8)
        if np.all(f == 1):
            f[rng.integers(0, N)] = -1
        cur = float(objective(analyse(f[None, :]))[0])
        for _ in range(steps):
            cand = np.repeat(f[None, :], N, axis=0)
            cand[np.arange(N), np.arange(N)] *= -1
            vals = objective(analyse(cand))
            j = int(np.argmax(vals))
            if vals[j] <= cur + 1e-12:
                break
            f, cur = cand[j].copy(), float(vals[j])
        tracker.feed(f[None, :], f"{tag}:climb")
        best_overall = max(best_overall, cur)
    return best_overall


def obj_ratio(key, k=None):
    def f(R):
        I = np.maximum(R["I"], 1e-12)
        if key == "B":
            v = R["B"]
        elif key == "Bge1":
            v = R["B"] - R["Bk"][:, 0]
        elif key == "Bk":
            v = R["Bk"][:, k]
        elif key == "Hk":
            v = R["Hk"][:, k]
        return np.where(R["I"] > 1e-9, v / I, 0)
    return f


def main():
    outdir = sys.argv[1]
    quick = "--quick" in sys.argv
    os.makedirs(outdir, exist_ok=True)
    rng = np.random.default_rng(20261012)
    T = Tracker()
    t0 = time.time()
    log = []
    for n in range(1, 5):
        T.feed(all_functions(n), f"all_n{n}")
    log.append(f"exhaustive n<=4 done, {T.count} functions, {time.time()-t0:.1f}s")
    fam = {}
    for m in (2, 4, 6, 8, 10, 12):
        R = T.feed(fam_bent_times_x0(m), f"x0*bent_{m}")
        fam[f"x0*bent_{m}"] = dict(B=float(R["B"][0]), I=float(R["I"][0]), H=float(R["H"][0]),
                                   Bk_over_I=[float(v) for v in R["Bk"][0] / R["I"][0]])
    for n in (6, 8, 10, 12):
        for t in range(0, n // 2 + 1):
            T.feed(fam_threshold(n, t), f"ball_n{n}_t{t}")
        T.feed(fam_and(n), f"and_{n}")
    for (w, s) in ((2, 2), (2, 3), (3, 2), (2, 4), (3, 3), (4, 2), (2, 5), (3, 4), (4, 3)):
        T.feed(fam_tribes(w, s), f"tribes_{w}x{s}")
    log.append(f"families done, {time.time()-t0:.1f}s")
    reps = 40 if quick else 300
    for n in range(5, 11):
        T.feed((1 - 2 * rng.integers(0, 2, (reps, 1 << n))).astype(np.int8), f"rand_n{n}")
        T.feed(random_dt(n, min(n, 5), rng, reps // 3), f"dt_n{n}")
        T.feed(random_dnf(n, 2, 3, rng, reps // 3), f"dnf2_n{n}")
        T.feed(random_dnf(n, 3, 4, rng, reps // 3), f"dnf3_n{n}")
        T.feed(random_ltf(n, rng, reps // 3), f"ltf_n{n}")
    log.append(f"random classes done, {T.count} functions, {time.time()-t0:.1f}s")
    climbs = {}
    targets = [("H2", obj_ratio("Hk", 2)), ("B1", obj_ratio("Bk", 1)), ("H3", obj_ratio("Hk", 3)),
               ("B2", obj_ratio("Bk", 2)), ("B3", obj_ratio("Bk", 3)), ("Bge1", obj_ratio("Bge1")), ("B", obj_ratio("B"))]
    for n in ((5, 6) if quick else (5, 6, 7, 8)):
        for name, obj in targets:
            climbs[f"{name}_n{n}"] = hill_climb(n, obj, rng, 2 if quick else 6, 60 if quick else 200, T, f"{name}_n{n}")
        log.append(f"climbs n={n} done, {time.time()-t0:.1f}s")
    if not quick:
        for n in (9, 10):
            for name, obj in targets[:4]:
                climbs[f"{name}_n{n}"] = hill_climb(n, obj, rng, 4, 120, T, f"{name}_n{n}")
            log.append(f"climbs n={n} done, {time.time()-t0:.1f}s")
    res = dict(constants=dict(K2=K2, T12=T12C, H3=H3C, T23=T23C), count=T.count, violations=T.viol,
               worst={k: dict(ratio=v[0], where=v[1], tt=v[2]) for k, v in sorted(T.best.items())},
               families=fam, climbs=climbs, log=log, seconds=time.time() - t0)
    stamp = time.strftime("%Y%m%dT%H%M%S")
    path = os.path.join(outdir, f"check_levels_{stamp}{'_quick' if quick else ''}.json")
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(res, fh, indent=1)
    print(path)
    print("count", T.count, "seconds", round(time.time() - t0, 1))
    print("violations", json.dumps(T.viol))
    for k, v in sorted(T.best.items()):
        print(f"  {k:16s} {v[0]:.4f}  at {v[1]}  tt={v[2][:64]}")
    print("climbs", json.dumps({k: round(v, 4) for k, v in climbs.items()}))


if __name__ == "__main__":
    main()
