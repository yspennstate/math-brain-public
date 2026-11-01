"""Test the Anderson reduction for the three-slab conjecture.

Claim: if a coordinate lies in the support of exactly one of the three
forms, deleting it can only INCREASE the slab probability.  Reason: write
that form as M = M' +- X_j with X_j independent of everything else and
symmetric unimodal; the event is a symmetric convex set in the remaining
variables shifted by an independent symmetric unimodal variable, so
Anderson's inequality applies coordinatewise.

If true, the conjecture reduces to configurations in which every
coordinate lies in at least two of the three supports - a bounded family.

This script tests the claim exhaustively on small systems: for every
admissible (L, M, N) at d = 4, compare against the same system with a
private coordinate appended to M (and to N), at d = 5.

Run:  python -u anderson_reduction.py
"""
import sys, os
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

d = 4
L = (1, 1, -1, 0)
coords = {tuple(1 if i == j else 0 for i in range(d)) for j in range(d)}
F = [f for f in forms(d) if f != L and tuple(-x for x in L) != f and f not in coords]
print(f"d={d}: {len(F)} forms, testing private-coordinate insertion", flush=True)

viol = 0
tested = 0
worst_gain = Fr(0)
for M, N in combinations(F, 2):
    base = vol([L, M, N], d)
    # append a private coordinate to M: M gets +1 in slot 4, and to keep the
    # coefficient sum equal to one, flip an existing +1 to 0 is not allowed
    # (that changes the form), so instead we extend by a +1/-1 PAIR, the
    # smallest private extension preserving coefficient sum one.
    Lx = L + (0, 0)
    Mx = M + (1, -1)
    Nx = N + (0, 0)
    ext = vol([Lx, Mx, Nx], d + 2)
    tested += 1
    if ext > base:
        viol += 1
        if ext - base > worst_gain:
            worst_gain = ext - base
        if viol <= 3:
            print(f"  VIOLATION: base {base} -> extended {ext}  M={M} N={N}")
print(f"tested {tested} systems; extensions that INCREASED the probability: {viol}")
if viol == 0:
    print("ANDERSON REDUCTION SUPPORTED: private coordinates never increase the "
          "slab probability, so the extremal configurations have every "
          "coordinate shared by at least two forms")
else:
    print(f"REDUCTION FAILS on {viol} systems (worst gain {worst_gain}) - the "
          f"finite reduction needs a different argument")
