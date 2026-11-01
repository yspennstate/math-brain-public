from fractions import Fraction as Q

# Exact finite algebra for the P0033 two-color Galton--Watson construction.
# This is a self-check of the arithmetic core only; the measure-theoretic proof
# is written in the immutable R02 report.

p = Q(1, 2)
F_half = Q(3, 5) * p * p + Q(2, 5) * (1 - (1 - p) ** 3)
assert F_half == Q(1, 2)

# R(r) = 3/10 + (3/5) r^2 + (2/5) r^3.
def R(r):
    return Q(3, 10) + Q(3, 5) * r * r + Q(2, 5) * r * r * r

# Verify coefficientwise:
# 10(R(r)-r) = (2r-1)(2r^2+4r-3).
lhs = [Q(3), Q(-10), Q(6), Q(4)]  # low degree -> high degree
f1 = [Q(-1), Q(2)]
f2 = [Q(-3), Q(4), Q(2)]
rhs = [Q(0)] * 4
for i, x in enumerate(f1):
    for j, y in enumerate(f2):
        rhs[i + j] += x * y
assert lhs == rhs

# Endpoint/invariance arithmetic used in the proof.
assert R(Q(1, 4)) == Q(11, 32)
assert R(Q(1, 2)) == Q(1, 2)
# 2r^2+4r-3 is increasing on [1/4,1/2] and is still negative at 1/2.
assert 2 * Q(1, 2) ** 2 + 4 * Q(1, 2) - 3 == Q(-1, 2)
# The other positive fixed point is (sqrt(10)-2)/2 > 1/2 because 10 > 9.
assert 10 > 9

# Independent tree-automaton diagnostic: expected number of pivotal children
# at the Bernoulli(1/2) fixed point is 3/5*1 + 2/5*(3/4) = 9/10.
pivot_mean = Q(3, 5) * 1 + Q(2, 5) * Q(3, 4)
assert pivot_mean == Q(9, 10)

print("F(1/2) =", F_half)
print("factorization coefficients =", lhs)
print("R(1/4) =", R(Q(1, 4)))
print("R(1/2) =", R(Q(1, 2)))
print("pivot mean =", pivot_mean)
print("ALL_EXACT_CHECKS_PASS")
