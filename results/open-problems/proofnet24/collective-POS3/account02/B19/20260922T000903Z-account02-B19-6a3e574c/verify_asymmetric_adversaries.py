from fractions import Fraction
from math import comb, factorial
from functools import lru_cache
from itertools import combinations


def qprob(r, s, i, j):
    """Probability R_i precedes S_j in a uniform shuffle of chains C_r || C_s."""
    t = i + j - 1
    den = comb(r + s, r)
    num = 0
    for k in range(i, min(r, t) + 1):
        rem = r - k
        if 0 <= rem <= r + s - t:
            num += comb(t, k) * comb(r + s - t, rem)
    return Fraction(num, den)


def frac(x):
    return f"{x.numerator}/{x.denominator}" if x.denominator != 1 else str(x.numerator)


# Asymmetric parallel-chain core Q = C_1 || C_4 || C_16.
lens = {"A": 1, "B": 4, "C": 16}
E_q = factorial(21) // (factorial(1) * factorial(4) * factorial(16))
assert E_q == 101745
rows = []
for X, Y in (("A", "B"), ("A", "C"), ("B", "C")):
    r, s = lens[X], lens[Y]
    for i in range(1, r + 1):
        for j in range(1, s + 1):
            p = qprob(r, s, i, j)
            b = min(p, 1 - p)
            rows.append((f"{X}{i}", f"{Y}{j}", p, b, Fraction(1, 3) <= p <= Fraction(2, 3)))
assert len(rows) == 84
balanced = [r for r in rows if r[4]]
assert len(balanced) == 22
equal_depth = [
    ("A1", "B1", qprob(1, 4, 1, 1)),
    ("A1", "C1", qprob(1, 16, 1, 1)),
] + [(f"B{i}", f"C{i}", qprob(4, 16, i, i)) for i in range(1, 5)]
assert [p for _, _, p in equal_depth] == [
    Fraction(1, 5), Fraction(1, 17), Fraction(1, 5),
    Fraction(5, 57), Fraction(31, 969), Fraction(7, 969),
]
assert all(min(p, 1 - p) < Fraction(1, 3) for _, _, p in equal_depth)
assert qprob(1, 4, 1, 2) == Fraction(2, 5)
assert qprob(4, 16, 1, 3) == Fraction(29, 57)

print("Q_ASYMMETRIC_CHAIN_CORE")
print("E", E_q)
print("incomparable_pairs", len(rows))
print("balanced_pairs", len(balanced))
print("equal_depth_selector")
for x, y, p in equal_depth:
    print(x, y, frac(p), "balance", frac(min(p, 1 - p)))
print("balanced_witnesses")
for x, y, p, b, ok in balanced:
    print(x, y, frac(p))
print("all_Q_pair_probabilities")
for x, y, p, b, ok in rows:
    print(x, y, frac(p), "balance", frac(b), "BAL" if ok else "OUT")

# Only genuinely 3D nontrivial chain box with width <=3 is C2 x C2 x C2.
# Verify exact probabilities in the Boolean lattice B3.
elts = list(range(8))
lt = [[False] * 8 for _ in elts]
for x in elts:
    for y in elts:
        if x != y and (x & y) == x:
            lt[x][y] = True
pred = [0] * 8
for j in elts:
    for i in elts:
        if lt[i][j]:
            pred[j] |= 1 << i
full = (1 << 8) - 1


@lru_cache(None)
def ecount(mask, pred_tuple=tuple(pred)):
    if mask == full:
        return 1
    total = 0
    for z in elts:
        if not (mask >> z) & 1 and not (pred_tuple[z] & ~mask):
            total += ecount(mask | (1 << z), pred_tuple)
    return total


E_b3 = ecount(0)
assert E_b3 == 48


def augmented_count_before(x, y):
    rel = [row[:] for row in lt]
    rel[x][y] = True
    for k in elts:
        for i in elts:
            if rel[i][k]:
                for j in elts:
                    if rel[k][j]:
                        rel[i][j] = True
    assert not any(rel[i][i] for i in elts)
    pr = [0] * 8
    for j in elts:
        for i in elts:
            if rel[i][j]:
                pr[j] |= 1 << i
    pt = tuple(pr)

    @lru_cache(None)
    def dp(mask):
        if mask == full:
            return 1
        return sum(
            dp(mask | (1 << z))
            for z in elts
            if not (mask >> z) & 1 and not (pt[z] & ~mask)
        )

    return dp(0)


b3 = []
for x, y in combinations(elts, 2):
    if not lt[x][y] and not lt[y][x]:
        p = Fraction(augmented_count_before(x, y), E_b3)
        b3.append((x, y, p, min(p, 1 - p)))
assert len(b3) == 9
assert sorted(set(p for _, _, p, _ in b3)) == [Fraction(1, 12), Fraction(1, 2), Fraction(11, 12)]
assert sum(1 for _, _, _, b in b3 if b == Fraction(1, 2)) == 6
assert sum(1 for _, _, _, b in b3 if b == Fraction(1, 12)) == 3

print("B3_CARTESIAN_PRODUCT")
print("E", E_b3)
print("incomparable_pairs", len(b3))
for x, y, p, b in b3:
    print(f"{x:03b}", f"{y:03b}", frac(p), "balance", frac(b))

# Explicit width-4 antichain in C2 x C2 x C3 (zero-based coordinates),
# proving any 3D box with one side >=3 contains a width-4 subposet.
ant = [(1, 1, 0), (1, 0, 1), (0, 1, 1), (0, 0, 2)]


def leq(u, v):
    return all(a <= b for a, b in zip(u, v))


for u, v in combinations(ant, 2):
    assert not leq(u, v) and not leq(v, u)
print("C2xC2xC3_width4_antichain", ant)
print("ORDINAL_SUM_INVARIANCE", "C_r + Q + C_s has same 84 incomparable-pair probabilities for all r,s>=0")
print("POS3_ASYMMETRIC_ADVERSARY_CHECK_PASS")
