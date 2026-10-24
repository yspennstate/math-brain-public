from fractions import Fraction as F
from itertools import permutations

U = [
    [F(0),        F(3,5),       F(16,25),     F(-12,25)],
    [F(-69,325), F(-192,325),  F(48,65),     F(16,65)],
    [F(48,65),   F(16,65),     F(69,325),    F(192,325)],
    [F(16,25),   F(-12,25),    F(0),         F(-3,5)],
]

# Exact orthogonality.
for i in range(4):
    for j in range(4):
        dot = sum(U[i][k] * U[j][k] for k in range(4))
        assert dot == (F(1) if i == j else F(0))


def minor2(rows, cols):
    i, j = rows
    a, b = cols
    return U[i][a] * U[j][b] - U[i][b] * U[j][a]


def R(rows, cols):
    d = minor2(rows, cols)
    return d * d

# Any probability law on S_4 whose two-subset image marginals equal R must
# obey this pointwise indicator cut, because every individual permutation does.
terms = [
    ((0, 1), (0, 2)),
    ((0, 1), (0, 3)),
    ((0, 1), (1, 3)),
    ((0, 3), (0, 2)),
]


def hit(p, rows, cols):
    return {p[i] for i in rows} == set(cols)

for p in permutations(range(4)):
    lhs = int(hit(p, (0, 2), (2, 3)))
    rhs = sum(int(hit(p, rows, cols)) for rows, cols in terms)
    assert lhs <= rhs

lhs = R((0, 2), (2, 3))
rhs_terms = [R(rows, cols) for rows, cols in terms]
gap = lhs - sum(rhs_terms)

assert lhs == F(144, 625)
assert rhs_terms == [
    F(1218816, 66015625),
    F(685584, 66015625),
    F(1218816, 66015625),
    F(65536, 390625),
]
assert gap == F(40448, 2640625)
assert gap > 0

# Exact zero-entry corner factorization useful for the surviving direct route.
# With u_00=0, for i,j in {1,2,3}, |det U[{0,i},{0,j}]|^2
# equals |u_0j|^2 |u_i0|^2.
for i in (1, 2, 3):
    for j in (1, 2, 3):
        assert R((0, i), (0, j)) == (U[0][j] ** 2) * (U[i][0] ** 2)

print("orthogonal_exact=True")
print("pointwise_cut_all_24=True")
print("R_02_23=", lhs)
for (rows, cols), value in zip(terms, rhs_terms):
    print(f"R_{rows}_{cols}=", value)
print("gap=", gap)
print("corner_factorization_exact=True")
print("status=PASS")
