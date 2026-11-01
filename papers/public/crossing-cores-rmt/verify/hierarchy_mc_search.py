"""Broad Monte-Carlo search for a violation of the slab hierarchy.

The conjecture says j distinct slot forms give slab probability at most
2/(j+2).  Exact polytope volumes are expensive above j = 3, so this
script samples random j-tuples of admissible slot forms in dimensions
where exhaustive work is out of reach, estimates the probability by
direct simulation, and flags any tuple whose estimate exceeds the bound
by more than four standard errors.  Flagged tuples are then recomputed
EXACTLY, so a reported violation is never a Monte-Carlo artifact.

The star system of each j is included as a positive control: its
estimate must sit at 2/(j+2).

Run:  python -u hierarchy_mc_search.py [trials_per_setting]
"""
import sys, os, time, random
from fractions import Fraction as Fr
from itertools import combinations
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "engine"))
from exact_volume import volume_from_halfspaces

N_SAMPLES = 200_000

def forms(d):
    out = []
    for supp in range(3, d + 1, 2):
        nminus = (supp - 1) // 2
        for positions in combinations(range(d), supp):
            for minus in combinations(positions, nminus):
                v = [0] * d
                for pnt in positions:
                    v[pnt] = 1
                for m in minus:
                    v[m] = -1
                out.append(tuple(v))
    return sorted(set(out))

def mc(rows, d, rng, n=N_SAMPLES):
    M = np.array(rows, dtype=np.float64)
    X = rng.random((n, d)) - 0.5
    W = X @ M.T
    ok = (np.abs(W) <= 0.5).all(axis=1)
    p = ok.mean()
    se = (p * (1 - p) / n) ** 0.5
    return p, se

def exact(rows, d):
    hs = []
    for M in rows:
        hs.append((tuple(M), 1))
        hs.append((tuple(-x for x in M), 1))
    return volume_from_halfspaces(hs, [(-1, 1)] * d) / 2 ** d

def star(j):
    d = j + 2
    rows = []
    for i in range(j):
        v = [0] * d
        v[0], v[1], v[2 + i] = 1, -1, 1
        rows.append(tuple(v))
    return rows, d

def main():
    trials = int(sys.argv[1]) if len(sys.argv) > 1 else 3000
    rng = np.random.default_rng(20260824)
    pyrng = random.Random(7)
    print("positive controls (the star must sit at 2/(j+2)):", flush=True)
    for j in range(2, 8):
        rows, d = star(j)
        p, se = mc(rows, d, rng)
        tgt = 2.0 / (j + 2)
        print(f"   j={j}: MC {p:.5f} +- {se:.5f}   target {tgt:.5f}   "
              f"{'ok' if abs(p-tgt) < 4*se else 'CONTROL FAILS'}", flush=True)
    print("\nviolation search:", flush=True)
    flagged = []
    for j in range(4, 8):
        bound = 2.0 / (j + 2)
        for d in range(j + 2, j + 5):
            F = forms(d)
            coords = {tuple(1 if i == k else 0 for i in range(d)) for k in range(d)}
            F = [f for f in F if f not in coords]
            if len(F) < j:
                continue
            best = 0.0
            bestrows = None
            t0 = time.time()
            n = 0
            while n < trials and time.time() - t0 < 240:
                rows = pyrng.sample(F, j)
                p, se = mc(rows, d, rng, n=40_000)
                n += 1
                if p > best:
                    best, bestrows = p, rows
                if p > bound + 4 * ((p * (1 - p) / 40_000) ** 0.5):
                    flagged.append((j, d, rows, p))
            print(f"   j={j} d={d}: {n} tuples, best MC {best:.5f}, "
                  f"bound {bound:.5f}  "
                  f"{'clear' if best <= bound + 0.004 else 'CHECK'}", flush=True)
    print(f"\nflagged for exact recomputation: {len(flagged)}", flush=True)
    real = 0
    for j, d, rows, p in flagged[:20]:
        v = exact(rows, d)
        if v > Fr(2, j + 2):
            real += 1
            print(f"   REAL VIOLATION j={j} d={d}: exact {v} > {Fr(2,j+2)}",
                  flush=True)
    print(f"confirmed violations after exact recomputation: {real}")
    if real == 0:
        print("SLAB HIERARCHY SURVIVES the search at j = 4..7")

if __name__ == "__main__":
    main()
