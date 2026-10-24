from fractions import Fraction as F

# Exact checker for the depth-six T_8-fibre Galton--Watson comparison
# and the degree-28 nonbacktracking root test used in the accompanying report.

p0 = F(277, 5000)
s = 1 - p0
h = s
# h_0=s and h_j=s(s+p h_{j-1})^7.  Five updates produce h_5;
# C_6=s(s+p h_5)^8 is the pgf E[s^{Z_6}] for the radius-six T_8 cluster.
for _ in range(5):
    h = s * (s + p0 * h) ** 7
C6 = s * (s + p0 * h) ** 8
m6 = 11 * (1 - C6)
assert m6 > 1 + F(1, 1000)

# Rational square-root upper bounds.
sqrt11 = F(199, 60)
sqrt7 = F(127, 48)
sqrt3 = F(26, 15)
assert sqrt11 * sqrt11 > 11
assert sqrt7 * sqrt7 > 7
assert sqrt3 * sqrt3 > 3

base_bound = 2 * sqrt11 + 2 * sqrt7
freepair_bound = 2 * sqrt3
a_bound = base_bound + freepair_bound + 4
assert a_bound == F(2327, 120)

# Degree D=28, hence Q=D-1=27.  Test p_u > 559/10000 by z=1/p.
p1 = F(559, 10000)
z = 1 / p1
Q = 27
assert z * z > Q
root_margin = z + F(Q, 1) / z - a_bound
assert root_margin > 0

gap = p1 - p0
assert gap == F(1, 2000)

# Abstract weakening: it suffices that one symmetric two-pair block has
# operator norm <= 347/100; the remaining two pairs are charged crudely by 2 each.
kappa_allow = z + F(Q, 1) / z - base_bound - 4
assert kappa_allow > F(347, 100)
assert freepair_bound < F(347, 100)

print("PC_TEST_P =", p0, float(p0))
print("DEPTH6_MEAN =", format(float(m6), ".15f"))
print("DEPTH6_MEAN_MINUS_1_GT_1_1000 =", m6 - 1 > F(1, 1000))
print("DEPTH6_MARGIN_NUM_BITS =", (m6 - 1).numerator.bit_length())
print("DEPTH6_MARGIN_DEN_BITS =", (m6 - 1).denominator.bit_length())
print("BASE_NORM_RATIONAL_UPPER =", base_bound, float(base_bound))
print("FREEPAIR_NORM_RATIONAL_UPPER =", freepair_bound, float(freepair_bound))
print("TOTAL_NORM_RATIONAL_UPPER =", a_bound, float(a_bound))
print("PU_TEST_P =", p1, float(p1))
print("Z =", z, float(z))
print("Z2_MINUS_27 =", z * z - Q)
print("ROOT_MARGIN =", root_margin, float(root_margin))
print("CERTIFIED_GAP =", gap, float(gap))
print("KAPPA_ALLOW =", kappa_allow, float(kappa_allow))
print("KAPPA_ALLOW_MINUS_347_100 =", kappa_allow - F(347, 100))
print("FREEPAIR_BOUND_LT_347_100 =", freepair_bound < F(347, 100))
print("SQRT11_MARGIN =", sqrt11 * sqrt11 - 11)
print("SQRT7_MARGIN =", sqrt7 * sqrt7 - 7)
print("SQRT3_MARGIN =", sqrt3 * sqrt3 - 3)
print("ALL_EXACT_CHECKS_PASS")
