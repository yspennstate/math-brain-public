#!/usr/bin/env python3
"""Exact central-slice adversary check for the 5-input FEI gate reformulation.

At uniform input biases and balanced output, the gate margin is
    c_G = 4*(H/(I-1) - C0).
This checker proves, by exact integer enumeration for low edge boundary and an
analytic Gibbs bound for the complement, that every balanced 5-bit Boolean
gate satisfies H <= 6*(I-1). Equality in the enumerated low-boundary sector is
always degenerate (some coordinate has zero influence).

No benchmark gold, external service, random seed, or floating comparison is
used for the exact inequality. Floating entropy is printed only as a
diagnostic after the exact checks.
"""
from collections import defaultdict, Counter
from math import log2, comb

N4 = 16
N5 = 32

EDGES4 = [(x, x ^ (1 << i)) for x in range(N4) for i in range(4)
          if x < (x ^ (1 << i))]
EDGES5_BY_I = [
    [(x, x ^ (1 << i)) for x in range(N5) if x < (x ^ (1 << i))]
    for i in range(5)
]

def boundary4(mask):
    return sum(((mask >> x) ^ (mask >> y)) & 1 for x, y in EDGES4)

def fwht(vals):
    a = list(vals)
    h = 1
    while h < len(a):
        for i in range(0, len(a), 2*h):
            for j in range(i, i+h):
                x, y = a[j], a[j+h]
                a[j], a[j+h] = x+y, x-y
        h *= 2
    return a

def spectral_data(a0, a1):
    # A = {-1 output}; a0/a1 are its two 4-cube slices.
    vals = [1] * 32
    for x in range(16):
        if (a0 >> x) & 1:
            vals[x] = -1
        if (a1 >> x) & 1:
            vals[16+x] = -1
    W = fwht(vals)
    # Balanced 5-bit truth tables have every Walsh integer divisible by four.
    assert W[0] == 0
    assert all(w % 4 == 0 for w in W)
    aa = [0 if w == 0 else (abs(w)//4)**2 for w in W]
    assert sum(aa) == 64
    L = sum(s.bit_count() * aa[s] for s in range(32))
    return vals, W, aa, L

def exact_H_le_6Iminus1(aa, L):
    # H = (1/64) sum a log2(64/a), I=L/64.
    # H <= 6(I-1) iff product a^a >= 2^(768-6L).
    P = 1
    for a in aa:
        if a:
            P *= a ** a
    e = 768 - 6*L
    if e >= 0:
        return P >= (1 << e), P == (1 << e)
    return True, False

def active_coordinates(vals):
    active = []
    for i, edges in enumerate(EDGES5_BY_I):
        cuts = sum(vals[x] != vals[y] for x, y in edges)
        active.append(cuts > 0)
    return active

def entropy_diag(aa):
    H = 0.0
    for a in aa:
        if a:
            p = a / 64.0
            H -= p * log2(p)
    return H

# Group all 4-cube slices by cardinality and internal boundary.
groups = defaultdict(list)
for m in range(1 << 16):
    groups[(m.bit_count(), boundary4(m))].append(m)

qualified = 0
by_boundary = Counter()
exact_equal = 0
equal_genuine = 0
max_diag = {}
boundary16_nondegenerate = 0

for s in range(17):
    t = 16 - s
    left = [(b, g) for (ss, b), g in groups.items() if ss == s]
    right = [(b, g) for (tt, b), g in groups.items() if tt == t]
    for b0, g0 in left:
        for b1, g1 in right:
            # Cross-slice disagreement >= |s-t|; prune impossible pairs.
            if b0 + b1 + abs(s-t) > 26:
                continue
            rem = 26 - b0 - b1
            for a0 in g0:
                for a1 in g1:
                    cross = (a0 ^ a1).bit_count()
                    if cross > rem:
                        continue
                    B = b0 + b1 + cross
                    qualified += 1
                    by_boundary[B] += 1
                    vals, W, aa, L = spectral_data(a0, a1)
                    assert L == 4*B  # I = B/16 = L/64
                    if B == 16:
                        # Balanced edge-isoperimetric equality cases in the
                        # enumerated sector must be dictators/negations.
                        act = active_coordinates(vals)
                        if sum(act) != 1:
                            boundary16_nondegenerate += 1
                        continue
                    ok, eq = exact_H_le_6Iminus1(aa, L)
                    assert ok
                    act = active_coordinates(vals)
                    if eq:
                        exact_equal += 1
                        if all(act):
                            equal_genuine += 1
                    H = entropy_diag(aa)
                    I = L / 64.0
                    ratio = H / (I-1.0)
                    old = max_diag.get(B)
                    if old is None or ratio > old[0]:
                        max_diag[B] = (ratio, H, I,
                                       Counter(abs(w) for w in W if w))

assert qualified == 142410
assert by_boundary == Counter({26:130560, 24:9440, 22:2400, 16:10})
assert boundary16_nondegenerate == 0
assert exact_equal == 960
assert equal_genuine == 0

# High-boundary analytic closure. For any spectral law on nonempty subsets,
# KL against r(S) proportional to (1/3)^|S| gives
# H <= log2(781/243) + I log2 3.
# At I=7/4 this is strictly < 9/2 = 6(I-1), exactly because:
assert 781**4 < (2**18) * (3**13)
# The RHS 6(I-1) has slope 6, larger than log2(3), so the inequality
# remains strict for every I >= 7/4.

print("PASS low-boundary balanced gates", qualified, dict(sorted(by_boundary.items())))
print("PASS exact H<=6(I-1) on B<=26; equality_cases", exact_equal,
      "equality_genuine", equal_genuine)
print("PASS boundary-16 cases are 10 dictators/negations")
print("PASS high-boundary Gibbs closure integer check",
      781**4, "<", (2**18)*(3**13))
for B in sorted(max_diag):
    ratio, H, I, patt = max_diag[B]
    print("DIAG boundary", B, "I", I, "max H/(I-1)", ratio,
          "H", H, "Walsh_abs_counts", dict(sorted(patt.items())))
print("THEOREM-SLICE: every balanced 5-input gate at p_i=1/2 has",
      "H<=6(I-1); equality is degenerate in the low-boundary equality sector.")
