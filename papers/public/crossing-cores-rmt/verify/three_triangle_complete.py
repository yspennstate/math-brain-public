"""COMPLETE enumeration of three-triangle slab systems, up to symmetry.

A slot form of minimal support is a "triangle": three nonzero entries in
{0,+-1} with coefficient sum one, i.e. two entries +1 and one entry -1.
For three such forms the whole configuration is a 3 x d sign matrix whose
rows each carry exactly two +1 and one -1, with no zero column.  Two
configurations related by a permutation of coordinates give the same
slab probability, so a configuration is determined by the MULTISET of its
columns, each column being a nonzero vector in {-1,0,1}^3.

This script enumerates every such multiset exactly (a small integer
program: for each row, the multiplicities of columns with +1 in that row
sum to 2, and with -1 sum to 1), discards degenerate cases where two
forms coincide or one is +-another, and computes each slab probability
Pr{|M_i(X)| <= 1/2, i = 1,2,3} exactly as a rational polytope volume.

The maximum over the complete list is a THEOREM for the all-triangle
case of the three-slab bound, not a sample.

Run:  python -u three_triangle_complete.py
"""
import sys, os, time
from fractions import Fraction as Fr
from itertools import product

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "engine"))
from exact_volume import volume_from_halfspaces

COLS = [c for c in product((-1, 0, 1), repeat=3) if any(c)]

def enumerate_configs():
    """All multisets of columns with, per row, exactly two +1 and one -1."""
    out = []
    n = len(COLS)

    def rec(i, mult, need_plus, need_minus):
        if all(p == 0 for p in need_plus) and all(m == 0 for m in need_minus):
            cols = []
            for t, m in enumerate(mult):
                cols.extend([COLS[t]] * m)
            out.append(tuple(cols))
            return
        if i == n:
            return
        c = COLS[i]
        # max multiplicity of this column type given remaining needs
        cap = 3
        for r in range(3):
            if c[r] == 1:
                cap = min(cap, need_plus[r])
            elif c[r] == -1:
                cap = min(cap, need_minus[r])
        for m in range(cap, -1, -1):
            np_ = list(need_plus)
            nm = list(need_minus)
            ok = True
            for r in range(3):
                if c[r] == 1:
                    np_[r] -= m
                    if np_[r] < 0:
                        ok = False
                elif c[r] == -1:
                    nm[r] -= m
                    if nm[r] < 0:
                        ok = False
            if not ok:
                continue
            mult[i] = m
            rec(i + 1, mult, np_, nm)
            mult[i] = 0

    rec(0, [0] * n, [2, 2, 2], [1, 1, 1])
    return out

def rows_of(cols):
    d = len(cols)
    return [tuple(cols[j][r] for j in range(d)) for r in range(3)]

def degenerate(rows):
    for a in range(3):
        for b in range(a + 1, 3):
            if rows[a] == rows[b]:
                return True
            if rows[a] == tuple(-x for x in rows[b]):
                return True
    return False

def vol(rows, d):
    hs = []
    for M in rows:
        hs.append((tuple(M), 1))
        hs.append((tuple(-x for x in M), 1))
    return volume_from_halfspaces(hs, [(-1, 1)] * d) / 2 ** d

def main():
    t0 = time.time()
    configs = enumerate_configs()
    # canonicalise by sorted column multiset (already a multiset; sort it)
    seen = set()
    canon = []
    for cols in configs:
        key = tuple(sorted(cols))
        if key in seen:
            continue
        seen.add(key)
        canon.append(key)
    print(f"complete list: {len(canon)} configurations up to coordinate "
          f"permutation ({time.time()-t0:.1f}s)", flush=True)

    best = Fr(0)
    arg = None
    ndeg = 0
    dist = {}
    for i, cols in enumerate(canon):
        d = len(cols)
        rows = rows_of(cols)
        if degenerate(rows):
            ndeg += 1
            continue
        v = vol(rows, d)
        dist[v] = dist.get(v, 0) + 1
        if v > best:
            best, arg = v, (rows, d)
        if (i + 1) % 100 == 0:
            print(f"   {i+1}/{len(canon)} evaluated, running max {best} "
                  f"({time.time()-t0:.0f}s)", flush=True)
    print(f"\ndegenerate (repeated or opposite forms) skipped: {ndeg}")
    print(f"MAXIMUM over all three-triangle systems: {best} = {float(best):.6f}")
    print(f"conjectured bound 2/5 = 0.400000   "
          f"{'HOLDS' if best <= Fr(2,5) else '*** EXCEEDED ***'}")
    if arg:
        print(f"attained by d={arg[1]}, rows {arg[0]}")
    top = sorted(dist.items(), reverse=True)[:6]
    print("top of the value distribution:")
    for v, m in top:
        print(f"   {v} = {float(v):.6f}  x{m}")

if __name__ == "__main__":
    main()
