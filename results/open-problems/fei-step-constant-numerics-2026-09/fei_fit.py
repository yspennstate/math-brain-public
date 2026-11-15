"""Job B of the FEI compute package, in its simplest form: does a potential
Psi = K * I * psi(f), with psi an inspectable spectral statistic in [0,1],
lower the constant the induction step needs?

For each function f and each relevant coordinate i:
    a_i = Delta_i H,  b_i = Inf_i,
    g_i = I(f) psi(f) - ( I(f_0) psi(f_0) + I(f_1) psi(f_1) ) / 2     (potential drop per unit K)
The step holds with (C, K) iff some i has a_i <= C b_i + K g_i.  For a grid of K,
    C_needed(K) = max_f min_i (a_i - K g_i) / b_i,
and the FEI constant delivered is C_needed(K) + K.  K = 0 is the no-potential baseline.

Statistics tried (all in [0,1], so 0 <= Psi <= K I holds automatically):
    spread   = 1 - max_S p_S
    highdeg  = 1 - W^{<=1}(f)          (weight above degree one)
    unbiased = 1 - p_empty             (= 1 - E[f]^2)
    dense    = I(f) / n                (influence density; children use I/(n-1))
Usage: fei_fit.py --n N [--all | --ints a,b,c | --json search_or_exhaustive.json]
"""
import argparse, json, math
import numpy as np
import fei_p2

STATS = ("spread", "highdeg", "unbiased", "dense")


def psi_of(cube, F):
    p = cube.spectrum(F)
    pop = cube.pop
    I = p @ pop
    out = {
        "spread": 1.0 - p.max(axis=1),
        "highdeg": 1.0 - (p * (pop <= 1)).sum(axis=1),
        "unbiased": 1.0 - p[:, 0],
        "dense": I / cube.n,
    }
    return out, I


def rows_for(cube, F):
    """Return arrays a (B,n), b (B,n), g[stat] (B,n), relevant (B,n)."""
    s = cube.stats(F)
    psi, I = psi_of(cube, F)
    c = cube.child
    g = {k: np.zeros_like(s["dH"]) for k in STATS}
    for i in range(cube.n):
        G0 = F[:, cube.idx0[i]]; G1 = F[:, cube.idx1[i]]
        p0, I0 = psi_of(c, G0); p1, I1 = psi_of(c, G1)
        for k in STATS:
            g[k][:, i] = I * psi[k] - 0.5 * (I0 * p0[k] + I1 * p1[k])
    return s["dH"], s["Inf"], g, s["relevant"], s


def c_needed(a, b, g, rel, Ks):
    """C_needed(K) over the functions given; returns dict K -> (C, C+K)."""
    out = {}
    for K in Ks:
        val = np.where(rel, (a - K * g) / np.where(rel, b, 1.0), np.inf)
        per_f = val.min(axis=1)
        per_f = per_f[np.isfinite(per_f)]
        C = float(per_f.max()) if per_f.size else float("nan")
        out[float(K)] = (C, C + K)
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--n", type=int, required=True)
    ap.add_argument("--all", action="store_true", help="every n-variable function with f(0)=+1 (n<=4)")
    ap.add_argument("--ints", help="comma-separated truth-table integers")
    ap.add_argument("--json", help="fei_p2 output json: uses best[] tables or results[].climbed_table")
    ap.add_argument("--Ks", default="0,0.25,0.5,0.75,1,1.5,2,3,4,6,8")
    a = ap.parse_args()
    n = a.n
    cube = fei_p2.Cube(n)
    Ks = [float(x) for x in a.Ks.split(",")]
    if a.all:
        assert n <= 4
        ints = np.arange(0, 1 << ((1 << n) - 1), dtype=np.uint64) * np.uint64(2)
    elif a.ints:
        ints = [int(x) for x in a.ints.split(",")]
    else:
        d = json.load(open(a.json, encoding="utf-8"))
        if "best" in d:
            ints = sorted({int(v) for _, v in d["best"]})
        else:
            ints = sorted({int(v["climbed_table"]) for v in d["results"].values()})
    F = fei_p2.tables_from_ints(ints, n)
    A = []; Bm = []; G = {k: [] for k in STATS}; R = []
    step = 4096
    for j in range(0, len(F), step):
        aa, bb, gg, rr, _ = rows_for(cube, F[j:j + step])
        A.append(aa); Bm.append(bb); R.append(rr)
        for k in STATS: G[k].append(gg[k])
    A = np.vstack(A); Bm = np.vstack(Bm); R = np.vstack(R)
    print(f"n={n} functions={len(F)}")
    base = c_needed(A, Bm, np.zeros_like(A), R, [0.0])[0.0][0]
    print(f"baseline (no potential): C_needed = {base:.6f}")
    for k in STATS:
        res = c_needed(A, Bm, np.vstack(G[k]), R, Ks)
        bestK = min(res, key=lambda K: res[K][1])
        line = "  ".join(f"K={K:g}: C={res[K][0]:.3f} (C+K={res[K][1]:.3f})" for K in Ks)
        print(f"psi={k:9s} best C+K = {res[bestK][1]:.4f} at K={bestK:g}   | {line}")


if __name__ == "__main__":
    main()
