from fractions import Fraction
from math import comb

# R14 / H0008 exact finite-core checker.
# Source-specialized 2-type example for the constant-q-row-average
# lumpability theorem in the finite-type failed Galton--Watson reduction.

q = [Fraction(1, 2), Fraction(1, 2)]
P = [
    [Fraction(1, 1), Fraction(1, 2)],
    [Fraction(3, 4), Fraction(3, 4)],
]
m_star = Fraction(2, 1)

row_averages = [sum(q[j] * P[i][j] for j in range(2)) for i in range(2)]
assert row_averages == [Fraction(3, 4), Fraction(3, 4)]

# Source mean matrix M_ij = m_* q_j p_ij.
M = [[m_star * q[j] * P[i][j] for j in range(2)] for i in range(2)]
row_sums = [sum(row) for row in M]
assert row_sums == [Fraction(3, 2), Fraction(3, 2)]

# Verify lambda=3/2 is an eigenvalue exactly and recover the second eigenvalue.
lam = Fraction(3, 2)
char_at_lam = (M[0][0] - lam) * (M[1][1] - lam) - M[0][1] * M[1][0]
assert char_at_lam == 0
trace = M[0][0] + M[1][1]
other_eigenvalue = trace - lam
assert other_eigenvalue == Fraction(1, 4)

# Under type erasure, K | nu=2 ~ Bin(2, 3/4).
c = Fraction(3, 4)
K_probs = [Fraction(comb(2, k), 1) * c**k * (1 - c)**(2-k) for k in range(3)]
assert K_probs == [Fraction(1, 16), Fraction(3, 8), Fraction(9, 16)]
assert sum(K_probs) == 1
mean_K = sum(Fraction(k, 1) * K_probs[k] for k in range(3))
assert mean_K == Fraction(3, 2)
assert sum(1 for x in K_probs if x > 0) > 1  # nondegenerate offspring law

print("row_averages", row_averages)
print("M", M)
print("M_row_sums", row_sums)
print("char_at_3/2", char_at_lam, "other_eigenvalue", other_eigenvalue)
print("K_probs", K_probs, "sum", sum(K_probs), "mean", mean_K)
print("ALL_EXACT_CHECKS_PASS")
