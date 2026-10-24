"""Numerical test of the FEI compute package's induction step.

The package (math-open-problems, operations/COMPUTE_STRATEGY_2026-09-20.md,
Section 3) proposes: find a potential Psi with 0 <= Psi <= K I and, for
every nonconstant Boolean f, a coordinate i with

    Delta_i H(f) := H(f) - (H(f_0) + H(f_1)) / 2  <=  C Inf_i(f) + Psi(f) - (Psi(f_0) + Psi(f_1)) / 2 .

With Psi = 0 the step needs, for every f, a coordinate with
Delta_i H / Inf_i <= C.  So the basic quantity is

    rho0(f) = min over relevant coordinates i of  Delta_i H(f) / Inf_i(f),

and max_f rho0(f) over n-variable functions is the smallest C that works
with no potential in dimension n.  Irrelevant coordinates have Inf_i = 0 and
Delta_i H = 0 exactly (both children equal f), so they are skipped.

Entropy is in bits, on the squared normalised Walsh coefficients.

Subcommands
  control                exact known values (one-point flips) against the code
  exhaustive --n N       every N-variable function (N<=5; N=5 takes core-hours),
                         optionally sharded with --shard k --nshards m
  search --n N --seconds T   structured seeds + hill climb at N variables
"""
import argparse, json, math, os, sys, time
import numpy as np

LOG2 = math.log(2.0)


def set_idle_priority():
    if os.name == "nt":
        try:
            import ctypes
            k = ctypes.windll.kernel32
            k.SetPriorityClass(k.GetCurrentProcess(), 0x40)  # IDLE_PRIORITY_CLASS
        except Exception:
            pass


class Cube:
    """Precomputed tables for n variables."""

    def __init__(self, n):
        self.n = n
        N = 1 << n
        self.N = N
        idx = np.arange(N)
        pop = np.array([bin(x).count("1") for x in range(N)], dtype=np.float64)
        self.pop = pop
        # H[x, S] = (-1)^{popcount(x & S)}
        self.H = np.array([[1.0 - 2.0 * (bin(x & S).count("1") & 1) for S in range(N)] for x in range(N)])
        self.bit = np.array([[(S >> i) & 1 for S in range(N)] for i in range(n)], dtype=np.float64)  # (n, N)
        # children index maps: for coordinate i, inputs with x_i = b, in the natural order of the remaining bits
        self.idx0 = []
        self.idx1 = []
        for i in range(n):
            lo, hi = [], []
            for y in range(N >> 1):
                low = y & ((1 << i) - 1)
                high = y >> i
                x0 = low | (high << (i + 1))
                lo.append(x0)
                hi.append(x0 | (1 << i))
            self.idx0.append(np.array(lo))
            self.idx1.append(np.array(hi))
        self.child = Cube(n - 1) if n >= 2 else None

    def spectrum(self, F):
        """F: (B, N) array of +-1 values. Returns p (B, N) squared normalised coefficients."""
        fhat = F @ self.H / self.N
        return fhat * fhat

    def entropy(self, p):
        with np.errstate(divide="ignore", invalid="ignore"):
            t = np.where(p > 0, p * np.log2(np.where(p > 0, p, 1.0)), 0.0)
        return -t.sum(axis=1)

    def stats(self, F):
        """Return dict of per-function arrays: H, I, Inf (B,n), rho0, best coordinate, child stats."""
        B = F.shape[0]
        p = self.spectrum(F)
        H = self.entropy(p)
        I = p @ self.pop
        Inf = p @ self.bit.T  # (B, n)
        pmax = p.max(axis=1)
        w1 = (p * (self.pop <= 1)).sum(axis=1)
        dH = np.zeros((B, self.n))
        H0 = np.zeros((B, self.n)); H1 = np.zeros((B, self.n))
        I0 = np.zeros((B, self.n)); I1 = np.zeros((B, self.n))
        pm0 = np.zeros((B, self.n)); pm1 = np.zeros((B, self.n))
        c = self.child
        for i in range(self.n):
            for b, (idx, Hb, Ib, pmb) in enumerate(((self.idx0[i], H0, I0, pm0), (self.idx1[i], H1, I1, pm1))):
                G = F[:, idx]
                pc = c.spectrum(G)
                Hb[:, i] = c.entropy(pc)
                Ib[:, i] = pc @ c.pop
                pmb[:, i] = pc.max(axis=1)
            dH[:, i] = H - 0.5 * (H0[:, i] + H1[:, i])
        relevant = Inf > 1e-12
        ratio = np.where(relevant, dH / np.where(relevant, Inf, 1.0), np.inf)
        rho0 = ratio.min(axis=1)
        best = ratio.argmin(axis=1)
        return dict(H=H, I=I, Inf=Inf, dH=dH, H0=H0, H1=H1, I0=I0, I1=I1, pmax=pmax, pm0=pm0, pm1=pm1,
                    w1=w1, rho0=rho0, best=best, relevant=relevant)


def tables_from_ints(ints, n):
    """ints: array of truth-table integers; bit x of the integer is f(x) in {0,1}; returns +-1 array (B, 2^n)."""
    N = 1 << n
    if N > 64:
        # Python integers: truth tables longer than 64 bits do not fit uint64
        rows = [[(int(v) >> x) & 1 for x in range(N)] for v in ints]
        return 1.0 - 2.0 * np.array(rows, dtype=np.float64)
    ints = np.asarray(ints, dtype=np.uint64)
    bits = ((ints[:, None] >> np.arange(N, dtype=np.uint64)[None, :]) & np.uint64(1)).astype(np.float64)
    return 1.0 - 2.0 * bits


def one_point_flip(n):
    F = np.ones((1, 1 << n))
    F[0, 0] = -1.0
    return F


def control():
    """Exact one-point-flip values against the code, plus the influence identity."""
    out = {}
    for n in range(2, 8):
        cube = Cube(n)
        s = cube.stats(one_point_flip(n))
        N = 1 << n
        p0 = (1 - 2.0 ** (1 - n)) ** 2
        q = 2.0 ** (2 - 2 * n)
        H_exact = -p0 * math.log2(p0) - (N - 1) * q * math.log2(q)
        I_exact = q * n * 2 ** (n - 1)
        out[n] = dict(H=float(s["H"][0]), H_exact=H_exact, I=float(s["I"][0]), I_exact=I_exact,
                      ratio=float(s["H"][0] / s["I"][0]), rho0=float(s["rho0"][0]))
    # published exact constants from the repo (P03): C_5, C_6 are attained by one-point flips
    C5 = 128 / 5 - (45 / 8) * math.log2(15)
    C6 = 160 / 3 - (961 / 96) * math.log2(31)
    out["C5_repo"] = C5; out["C6_repo"] = C6
    # influence identity on random functions
    rng = np.random.default_rng(1)
    cube = Cube(6)
    F = 1.0 - 2.0 * rng.integers(0, 2, size=(50, 64)).astype(np.float64)
    s = cube.stats(F)
    lhs = s["I"][:, None]
    rhs = s["Inf"] + 0.5 * (s["I0"] + s["I1"])
    out["influence_identity_max_abs_err"] = float(np.abs(lhs - rhs).max())
    return out


def exhaustive(n, shard=0, nshards=1, block_bits=14, report_every=200, top=20, outpath=None):
    """Sweep every n-variable function with f(0)=+1 (complement symmetry halves the work)."""
    set_idle_priority()
    cube = Cube(n)
    N = 1 << n
    total = 1 << (N - 1)  # functions with f(0) = +1  (bit 0 of the integer = 0)
    B = 1 << block_bits
    nblocks = (total + B - 1) // B
    t0 = time.time()
    best = []  # (rho0, table_int)
    hist = {}
    maxratio = 0.0; argratio = None
    done = 0
    for blk in range(shard, nblocks, nshards):
        start = blk * B
        ints = np.arange(start, min(start + B, total), dtype=np.uint64) * np.uint64(2)  # bit0 = 0 -> f(0)=+1
        F = tables_from_ints(ints, n)
        s = cube.stats(F)
        rho = s["rho0"]
        nonconst = np.isfinite(rho)
        # histogram of rho0 in 0.25 bins
        bins = np.floor(rho[nonconst] * 4).astype(int)
        for k, c in zip(*np.unique(bins, return_counts=True)):
            hist[int(k)] = hist.get(int(k), 0) + int(c)
        r = s["H"] / np.where(s["I"] > 0, s["I"], np.inf)
        j = int(np.argmax(r))
        if r[j] > maxratio:
            maxratio = float(r[j]); argratio = int(ints[j])
        order = np.argsort(-np.where(nonconst, rho, -np.inf))[:top]
        for j in order:
            if nonconst[j]:
                best.append((float(rho[j]), int(ints[j])))
        best.sort(reverse=True); best = best[:top]
        done += 1
        if done % report_every == 0:
            el = time.time() - t0
            print(f"shard {shard}/{nshards} blocks {done}/{(nblocks - shard + nshards - 1)//nshards} elapsed {el:.0f}s best rho0 {best[0][0]:.6f} maxH/I {maxratio:.6f}", flush=True)
    res = dict(n=n, shard=shard, nshards=nshards, blocks=done, elapsed=time.time() - t0,
               best=best, hist=hist, max_H_over_I=maxratio, argmax_H_over_I=argratio)
    if outpath:
        with open(outpath, "w", encoding="utf-8") as fh:
            json.dump(res, fh, indent=1)
    return res


# ---------------- structured families ----------------

def f_from_rule(n, rule):
    N = 1 << n
    x = [[(v >> i) & 1 for i in range(n)] for v in range(N)]
    return np.array([[1.0 - 2.0 * rule(x[v]) for v in range(N)]])


def tribes(w, s):
    n = w * s
    def rule(x):
        for t in range(s):
            if all(x[t * w + j] for j in range(w)):
                return 1
        return 0
    return n, f_from_rule(n, rule)


def majority(n):
    return n, f_from_rule(n, lambda x: 1 if sum(x) * 2 > n else 0)


def address(k):
    n = k + (1 << k)
    def rule(x):
        a = sum(x[i] << i for i in range(k))
        return x[k + a]
    return n, f_from_rule(n, rule)


def inner_product(m):
    n = 2 * m
    return n, f_from_rule(n, lambda x: sum(x[i] * x[m + i] for i in range(m)) & 1)


def and_of_ors(w, s):
    n = w * s
    def rule(x):
        return 1 if all(any(x[t * w + j] for j in range(w)) for t in range(s)) else 0
    return n, f_from_rule(n, rule)


def iterated_majority3(depth):
    n = 3 ** depth
    def rule(x):
        v = list(x)
        while len(v) > 1:
            v = [1 if v[3 * i] + v[3 * i + 1] + v[3 * i + 2] >= 2 else 0 for i in range(len(v) // 3)]
        return v[0]
    return n, f_from_rule(n, rule)


def sortedness(n):
    # 1 if the bits are monotone (non-decreasing or non-increasing)
    def rule(x):
        nd = all(x[i] <= x[i + 1] for i in range(n - 1))
        ni = all(x[i] >= x[i + 1] for i in range(n - 1))
        return 1 if (nd or ni) else 0
    return n, f_from_rule(n, rule)


def parity_xor_and(n):
    # parity of the first n-2 bits XOR AND of the last two
    return n, f_from_rule(n, lambda x: (sum(x[:n - 2]) + (x[n - 2] & x[n - 1])) & 1)


def seeds_for(n):
    out = []
    out.append(("one_point_flip", one_point_flip(n)))
    m, F = majority(n); out.append(("majority", F))
    if n % 2 == 0:
        m, F = inner_product(n // 2); out.append(("inner_product(bent)", F))
    for w in range(2, n):
        if n % w == 0:
            m, F = tribes(w, n // w); out.append((f"tribes({w}x{n//w})", F))
            m, F = and_of_ors(w, n // w); out.append((f"and_of_ors({w}x{n//w})", F))
    for k in range(1, 4):
        if k + (1 << k) == n:
            m, F = address(k); out.append((f"address({k})", F))
    if n == 9:
        m, F = iterated_majority3(2); out.append(("maj3_of_maj3", F))
    m, F = sortedness(n); out.append(("sortedness", F))
    m, F = parity_xor_and(n); out.append(("parity_xor_and", F))
    return out


def hill_climb(cube, F, seconds, rng, seed_name=""):
    """Maximise rho0 by single-output flips (batch-evaluate all 2^n neighbours), with random restarts on stall."""
    n, N = cube.n, cube.N
    cur = F.copy()
    s = cube.stats(cur)
    cur_val = float(s["rho0"][0]) if np.isfinite(s["rho0"][0]) else -1.0
    best_val, best_tab = cur_val, cur.copy()
    t0 = time.time(); it = 0; stalls = 0
    eye = np.eye(N)
    while time.time() - t0 < seconds:
        it += 1
        neigh = cur - 2.0 * cur * eye  # flip output x in row x
        s = cube.stats(neigh)
        vals = np.where(np.isfinite(s["rho0"]), s["rho0"], -1.0)
        j = int(np.argmax(vals))
        if vals[j] > cur_val + 1e-12:
            cur = neigh[j:j + 1].copy(); cur_val = float(vals[j]); stalls = 0
            if cur_val > best_val:
                best_val, best_tab = cur_val, cur.copy()
        else:
            stalls += 1
            # random kick: flip a few random outputs
            k = rng.integers(1, 4)
            cur = cur.copy()
            for x in rng.integers(0, N, size=k):
                cur[0, x] *= -1
            s2 = cube.stats(cur); v = s2["rho0"][0]
            cur_val = float(v) if np.isfinite(v) else -1.0
    return best_val, best_tab, it


def table_to_int(F):
    bits = ((1 - F[0]) / 2).astype(int)
    return int(sum(int(b) << x for x, b in enumerate(bits)))


def search(n, seconds, outpath=None, seed=0):
    set_idle_priority()
    cube = Cube(n)
    rng = np.random.default_rng(seed)
    results = {}
    t_all = time.time()
    seeds = seeds_for(n)
    per = max(5.0, seconds / (len(seeds) + 3))
    for name, F in seeds:
        s = cube.stats(F)
        base = dict(rho0=float(s["rho0"][0]), H=float(s["H"][0]), I=float(s["I"][0]), H_over_I=float(s["H"][0] / s["I"][0]),
                    best_coord=int(s["best"][0]))
        bv, bt, it = hill_climb(cube, F, per, rng, name)
        results[name] = dict(seed=base, climbed_rho0=bv, climbed_table=table_to_int(bt), iterations=it)
        print(f"n={n} {name:22s} seed rho0 {base['rho0']:.4f} H/I {base['H_over_I']:.4f} -> climbed {bv:.4f} ({it} it)", flush=True)
    # random restarts
    for r in range(3):
        F = 1.0 - 2.0 * rng.integers(0, 2, size=(1, 1 << n)).astype(np.float64)
        bv, bt, it = hill_climb(cube, F, per, rng, "random")
        results[f"random_{r}"] = dict(climbed_rho0=bv, climbed_table=table_to_int(bt), iterations=it)
        print(f"n={n} random_{r:<16d} -> climbed {bv:.4f} ({it} it)", flush=True)
    res = dict(n=n, seconds=time.time() - t_all, results=results,
               overall_best=max(v["climbed_rho0"] for v in results.values()))
    if outpath:
        with open(outpath, "w", encoding="utf-8") as fh:
            json.dump(res, fh, indent=1)
    return res


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("control")
    e = sub.add_parser("exhaustive"); e.add_argument("--n", type=int, required=True); e.add_argument("--shard", type=int, default=0)
    e.add_argument("--nshards", type=int, default=1); e.add_argument("--block-bits", type=int, default=14); e.add_argument("--out")
    s = sub.add_parser("search"); s.add_argument("--n", type=int, required=True); s.add_argument("--seconds", type=float, default=600)
    s.add_argument("--out"); s.add_argument("--seed", type=int, default=0)
    a = ap.parse_args()
    if a.cmd == "control":
        print(json.dumps(control(), indent=1))
    elif a.cmd == "exhaustive":
        r = exhaustive(a.n, a.shard, a.nshards, a.block_bits, outpath=a.out)
        print(json.dumps({k: v for k, v in r.items() if k != "hist"}, indent=1))
        print("hist(rho0 quarter-bins):", json.dumps(dict(sorted(r["hist"].items()))))
    elif a.cmd == "search":
        r = search(a.n, a.seconds, outpath=a.out, seed=a.seed)
        print("overall best rho0:", r["overall_best"])


if __name__ == "__main__":
    main()
