from fractions import Fraction
from decimal import Decimal, getcontext

getcontext().prec = 50

# p_c side: radius-2 fibre Galton--Watson lower comparison
# Base factor: T_12, hence 11 forward child fibres after rooting.
# Fibre factor: T_8.  Expose only the open cluster of the entry seed
# inside the radius-2 ball of the fibre.
p = Fraction(3, 50)
s = 1 - p
q = 11       # forward base children
r = 7        # forward branching in a rooted T_8 branch

# For one rooted outward branch of T_8, h_j is E[s^{# open vertices in
# that branch truncated at depth j}], including the branch root if reached.
# Radius two around the fibre seed gives:
h0 = s
h1 = s * (s + p * h0) ** r
C2 = s * (s + p * h1) ** (r + 1)  # E[s^{Z_2}]
activation = 1 - C2
mean = Fraction(q, 1) * activation
fib_margin = mean - 1

# p_u side: adjacency norm and nonbacktracking recurrence for degree D=22.
# Standard T_12 x T_8 adjacency norm = 2 sqrt(11) + 2 sqrt(7).
# Adding c,c^{-1} costs at most 2 in operator norm.
u11 = Fraction(331663, 100000)  # > sqrt(11)
u7 = Fraction(264576, 100000)   # > sqrt(7)
Aup = 2 * u11 + 2 * u7 + 2
D = 22
Q = D - 1

# Test z0 above the larger characteristic root via z + Q/z > Aup.
z0 = Fraction(10000, 819)
nb_margin = z0 + Fraction(Q, 1) / z0 - Aup

gap = Fraction(819, 10000) - Fraction(3, 50)


def dec(x):
    return Decimal(x.numerator) / Decimal(x.denominator)


checks = {
    "FIBRE_MEAN_GT_1": mean > 1,
    "FIBRE_MARGIN_GT_1_15": fib_margin > Fraction(1, 15),
    "SQRT11_UPPER_CERT": u11 * u11 > 11,
    "SQRT7_UPPER_CERT": u7 * u7 > 7,
    "Z_ABOVE_SQRT_Q": z0 * z0 > Q,
    "NB_TEST_MARGIN_GT_1_200": nb_margin > Fraction(1, 200),
    "GAP_EQ_219_10000": gap == Fraction(219, 10000),
}

print("p0 =", dec(p))
print("truncated_fibre_activation =", dec(activation))
print("GW_mean =", dec(mean))
print("GW_mean_minus_1 =", dec(fib_margin))
print("A_upper =", dec(Aup))
print("z0 =", dec(z0))
print("z0_plus_21_over_z0_minus_A_upper =", dec(nb_margin))
print("pc < 3/50 =", dec(Fraction(3, 50)))
print("pu > 819/10000 =", dec(Fraction(819, 10000)))
print("gap > 219/10000 =", dec(gap))
for k, v in checks.items():
    print(k, "=", v)
assert all(checks.values())
print("ALL_EXACT_CHECKS_PASS")
