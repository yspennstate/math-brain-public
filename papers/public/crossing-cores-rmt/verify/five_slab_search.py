"""Direct search against the open rank-five 2/7 slab bound.

The slab-hierarchy conjecture says j distinct exceptional slot forms give
at most 2/(j+2); for j = 5 that is 2/7, the extension's open rank-five
bound.  The conjectured extremal is the "star" system of the fully
crossing word w_6,

    M_i = X_0 + X_6 - X_i,   i = 1..5,

whose value is exactly int_{-1}^{1} (1-|s|)^6 ds = 2/7: conditioning on
S = X_0 + X_6 (density (1-|s|)_+), each constraint puts X_i in an
interval of length (1-|S|)_+, independently.

This script (a) confirms the star value exactly, and (b) searches for any
5-subset of admissible slot forms exceeding 2/7, both exhaustively at
small d and by random sampling at d = 6, 7.  A single counterexample
would refute the bound; none refutes nothing but accumulates evidence.

Run:  python -u five_slab_search.py [trials]
"""
import sys, os, time, random
from fractions import Fraction as Fr
from itertools import combinations

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "engine"))
from exact_volume import volume_from_halfspaces

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

def vol(rows, d):
    hs = []
    for M in rows:
        hs.append((tuple(M), 1))
        hs.append((tuple(-x for x in M), 1))
    return volume_from_halfspaces(hs, [(-1, 1)] * d) / 2 ** d

TARGET = Fr(2, 7)

# (a) the star system of w_6: variables X_0..X_6 (d = 7), M_i = X_0 + X_6 - X_i
d = 7
star = []
for i in range(1, 6):
    v = [0] * d
    v[0] = 1
    v[6] = 1
    v[i] = -1
    star.append(tuple(v))
sv = vol(star, d)
print(f"star system of w_6: volume {sv} = {float(sv):.8f}, target 2/7 = "
      f"{float(TARGET):.8f}  {'MATCH' if sv == TARGET else 'DIFFERS'}", flush=True)

# (b) exhaustive at d = 5 (few forms), then random at d = 6, 7
trials = int(sys.argv[1]) if len(sys.argv) > 1 else 400
for d in (5, 6, 7):
    F = forms(d)
    coords = {tuple(1 if i == j else 0 for i in range(d)) for j in range(d)}
    F = [f for f in F if f not in coords]
    total = 1
    for i in range(5):
        total = total * (len(F) - i) // (i + 1)
    print(f"\nd={d}: {len(F)} admissible forms, {total} five-subsets", flush=True)
    best = Fr(0)
    arg = None
    t0 = time.time()
    if total <= 3000:
        it = combinations(F, 5)
        n = 0
        for sub in it:
            v = vol(list(sub), d)
            n += 1
            if v > best:
                best, arg = v, sub
        print(f"   exhaustive over {n} subsets: max {best} = {float(best):.6f}",
              flush=True)
    else:
        rng = random.Random(20260824 + d)
        n = 0
        while n < trials and time.time() - t0 < 900:
            sub = rng.sample(F, 5)
            v = vol(sub, d)
            n += 1
            if v > best:
                best, arg = v, tuple(sub)
            if n % 100 == 0:
                print(f"   {n} random subsets, max {best} = {float(best):.6f} "
                      f"({time.time()-t0:.0f}s)", flush=True)
        print(f"   random search over {n} subsets: max {best} = {float(best):.6f}",
              flush=True)
    over = best > TARGET
    print(f"   2/7 = {float(TARGET):.6f}  ->  "
          f"{'*** EXCEEDS 2/7, BOUND REFUTED ***' if over else 'no violation found'}",
          flush=True)
    if over:
        print(f"   witness: {arg}", flush=True)
print("\nFIVE-SLAB SEARCH COMPLETE", flush=True)
