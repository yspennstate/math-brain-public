from fractions import Fraction
from itertools import product

# Exact finite certificate for R13-C33:
# any level-one projective 5-cube row cover whose maximum column energy
# is strictly below c0 = 1 / ((4+sqrt(142))/9)^2 uses at most five rows.

# Projective representatives s_1 = +1.
S = [(1,) + tail for tail in product((-1, 1), repeat=4)]

# For k chosen distinct projective classes, each may be oriented independently.
# states[k] is the exact set of possible coordinate sums of k oriented classes.
states = [set() for _ in range(17)]
states[0].add((0, 0, 0, 0, 0))
for s in S:
    nxt = [set(x) for x in states]
    for k in range(15, -1, -1):
        for v in states[k]:
            for sig in (-1, 1):
                w = tuple(v[j] + sig * s[j] for j in range(5))
                nxt[k + 1].add(w)
    states = nxt

M = {}
for k in range(1, 17):
    M[k] = max(sum(x*x for x in v) for v in states[k])

expected_M = {
    1:5, 2:16, 3:29, 4:48, 5:61, 6:80, 7:101, 8:128,
    9:133, 10:144, 11:157, 12:176, 13:189, 14:208, 15:229, 16:256
}
assert M == expected_M, (M, expected_M)

# If a row r covers k projective classes at level one, orient each covered
# class t so that r.t >= 1. Then
#   k <= r . sum(t) <= ||r||_2 ||sum(t)||_2,
# hence ||r||_2^2 >= q[k] := k^2 / M[k].
q = {k: Fraction(k*k, M[k]) for k in range(1, 17)}
assert all(q[k] <= q[k+1] for k in range(1,16))

# For a pruned cover there are at most 16 nonempty rows.
# For each row count m, minimize sum q[k_i] subject to k_i >= 1 and
# sum k_i >= 16. Dynamic programming is exact rational arithmetic.
min_cost = {}
argmin = {}
for m in range(1, 17):
    arr = {0: (Fraction(0), ())}
    for _ in range(m):
        narr = {}
        for total, (cost, ks) in arr.items():
            for k in range(1, 17):
                nt = total + k
                nc = cost + q[k]
                if nt not in narr or nc < narr[nt][0]:
                    narr[nt] = (nc, ks + (k,))
        arr = narr
    candidates = [(cost, ks, total)
                  for total, (cost, ks) in arr.items() if total >= 16]
    best = min(candidates, key=lambda z: z[0])
    min_cost[m], argmin[m] = best[0], (best[1], best[2])

assert min_cost[6] == Fraction(49, 30), (min_cost[6], argmin[6])
assert argmin[6][0] == (1, 1, 1, 1, 4, 8), argmin[6]
assert min(min_cost[m] for m in range(6,17)) == Fraction(49,30)
assert all(min_cost[m] >= Fraction(49,30) for m in range(6,17))

# c0 = 79/98 - (2/49)*sqrt(142).
# Check exactly that 49/30 > 5*c0.
# Difference = 2*(-881 + 75*sqrt(142))/735.
assert 75*75*142 - 881*881 == 22589 > 0

print("PROJECTIVE_CLASSES", len(S))
print("M_TABLE", " ".join(f"{k}:{M[k]}" for k in range(1,17)))
print("Q_TABLE", " ".join(f"{k}:{q[k]}" for k in range(1,17)))
for m in range(1,17):
    print("MIN_COST", m, min_cost[m], "PROFILE", argmin[m][0],
          "TOTAL_COVER_COUNT", argmin[m][1])
print("SIX_ROW_LOWER", Fraction(49,30))
print("COMPARE_49_OVER_30_MINUS_5C0",
      "2*(-881+75*sqrt(142))/735 > 0",
      "SQUARE_GAP", 22589)
print("CONCLUSION any cover with max_j column_energy < c0 has at most 5 nonzero witness rows")
print("R13_C33_EXACT_PASS")
