from fractions import Fraction
from itertools import combinations
import math

# Exact repeated-axis Parseval frame: four copies of e1,e2,e3, each scaled by 1/2.
rows = []
for axis in range(3):
    for copy in range(4):
        v = [Fraction(0), Fraction(0), Fraction(0)]
        v[axis] = Fraction(1, 2)
        rows.append(tuple(v))


def det3(m):
    return (
        m[0][0] * (m[1][1] * m[2][2] - m[1][2] * m[2][1])
        - m[0][1] * (m[1][0] * m[2][2] - m[1][2] * m[2][0])
        + m[0][2] * (m[1][0] * m[2][1] - m[1][1] * m[2][0])
    )


triples = list(combinations(range(len(rows)), 3))
d = {}
for I in triples:
    M = [rows[i] for i in I]
    x = det3(M)
    d[I] = x * x

sum_d = sum(d.values(), Fraction(0))
assert sum_d == 1

ell = []
for i in range(len(rows)):
    ell_i = sum(d[I] for I in triples if i in I)
    ell.append(ell_i)
assert all(x == Fraction(1, 4) for x in ell)
alpha = max(ell)

disjoint_mass = Fraction(0)
for I in triples:
    for J in triples:
        if set(I).isdisjoint(J):
            disjoint_mass += d[I] * d[J]

assert disjoint_mass == Fraction(27, 64)
expectation = disjoint_mass / 64
lower_bound = (1 - 3 * alpha) / 64
assert lower_bound == Fraction(1, 256)
assert expectation >= lower_bound

density_alpha_quarter = 3 * math.e * (2048 / 3) ** (1 / 3)
pair_bound = 4 * math.sqrt(20) * (8 ** 0.25) * (((7 / 144) * (1 / 64)) ** (-0.25))
a0j = math.sqrt(5) / 128

assert density_alpha_quarter < 71.805
assert pair_bound < 181.222
assert a0j < 0.017470

print("sum_d =", sum_d)
print("alpha =", alpha)
print("disjoint_mass =", disjoint_mass)
print("expectation =", expectation)
print("theorem_lower_bound =", lower_bound)
print("alpha_1_4_density_bound =", f"{density_alpha_quarter:.12f}")
print("transverse_mu_lower =", "7/144")
print("partner_pair_bound =", f"{pair_bound:.12f}")
print("unpaid_Ajj_bound =", "1/256")
print("unpaid_A0j_bound =", f"{a0j:.12f}")
print("QFORM_B19_R21_DISJOINT_BASIS_CHECK_PASS")
