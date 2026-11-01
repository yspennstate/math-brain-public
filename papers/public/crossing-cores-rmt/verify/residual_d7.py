"""The residual cases of the three-slab conjecture at d = 7.

Lemma (private pairs may be deleted) removes any configuration in which
some form carries two private coordinates of opposite sign.  Together
with the exhaustive scans at d <= 6, the cases left open are those in
dimension at least seven in which, for every form, all of its private
coordinates carry the same sign.

This script enumerates exactly those configurations at d = 7 with
L = X_1 + X_2 - X_3 fixed, and computes their slab probabilities
exactly.  It first prints how many survive the filter, so the cost is
known before the volumes are computed.

Run:  python -u residual_d7.py [--count-only]
"""
import sys, os, time
from fractions import Fraction as Fr
from itertools import combinations

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "engine"))
from exact_volume import volume_from_halfspaces

D = 7

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

def residual(rows):
    """True if no form has two private coordinates of opposite sign."""
    d = len(rows[0])
    for i, r in enumerate(rows):
        signs = set()
        for c in range(d):
            if r[c] == 0:
                continue
            if all(rows[k][c] == 0 for k in range(len(rows)) if k != i):
                signs.add(r[c])
        if len(signs) > 1:
            return False
    return True

def vol(rows, d):
    hs = []
    for M in rows:
        hs.append((tuple(M), 1))
        hs.append((tuple(-x for x in M), 1))
    return volume_from_halfspaces(hs, [(-1, 1)] * d) / 2 ** d

def main():
    count_only = "--count-only" in sys.argv
    L = tuple([1, 1, -1] + [0] * (D - 3))
    coords = {tuple(1 if i == j else 0 for i in range(D)) for j in range(D)}
    F = [f for f in forms(D)
         if f != L and tuple(-x for x in L) != f and f not in coords]
    print(f"d={D}: {len(F)} admissible forms, {len(F)*(len(F)-1)//2} pairs",
          flush=True)
    todo = []
    for M, N in combinations(F, 2):
        if residual([L, M, N]):
            todo.append((M, N))
    print(f"residual (irreducible by the private-pair lemma): {len(todo)}",
          flush=True)
    if count_only:
        return
    # checkpoint: index of the last completed pair, plus the running max
    import json
    ck = os.path.join(HERE, "residual_d7_checkpoint.json")
    start = 0
    best = Fr(0)
    arg = None
    if os.path.exists(ck):
        with open(ck, encoding="utf-8") as f:
            st = json.load(f)
        start = st["done"]
        best = Fr(st["best"])
        arg = st.get("arg")
        print(f"resuming from checkpoint at {start}/{len(todo)}, "
              f"running max {best}", flush=True)
    t0 = time.time()
    for i in range(start, len(todo)):
        M, N = todo[i]
        v = vol([L, M, N], D)
        if v > best:
            best, arg = v, [list(M), list(N)]
        if (i + 1) % 200 == 0 or i + 1 == len(todo):
            tmp = ck + ".tmp"
            with open(tmp, "w", encoding="utf-8") as f:
                json.dump({"done": i + 1, "best": str(best), "arg": arg}, f)
            os.replace(tmp, ck)
            rate = (i + 1 - start) / (time.time() - t0)
            print(f"   {i+1}/{len(todo)}, max {best} = {float(best):.6f}, "
                  f"eta {(len(todo)-i-1)/rate/60:.1f} min", flush=True)
    print(f"\nd=7 residual MAXIMUM = {best} = {float(best):.6f}")
    print(f"conjectured bound 2/5 = 0.400000   "
          f"{'HOLDS' if best <= Fr(2,5) else '*** EXCEEDED ***'}")
    if arg:
        print(f"attained by M={arg[0]} N={arg[1]}")

if __name__ == "__main__":
    main()
