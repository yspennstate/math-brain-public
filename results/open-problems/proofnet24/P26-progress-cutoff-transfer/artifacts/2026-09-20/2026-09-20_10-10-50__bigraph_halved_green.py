from fractions import Fraction

# Exact sanity check for the p=2 Eisenstein Cayley-bigraph application.
# Bigraph degrees are (K+1,k+1)=(9,3); the left halved graph joins
# two left vertices when they have a common right neighbor.
K = 8
k = 2
left_degree = K + 1
right_degree = k + 1
halved_degree = left_degree * k

# Interior radial increments in two-edge units on the biregular tree.
# -1: choose the parent right vertex, then the unique grandparent left vertex.
#  0: choose the parent right vertex, then one of the other k-1 left vertices.
# +1: choose one of K child right vertices, then any of its k new left vertices.
counts = {-1: 1, 0: k - 1, 1: K * k}
assert sum(counts.values()) == halved_degree

v = sum(Fraction(delta * multiplicity, halved_degree)
        for delta, multiplicity in counts.items())
M2 = sum(Fraction(delta * delta * multiplicity, halved_degree)
         for delta, multiplicity in counts.items())
tau2 = M2 / (v ** 3)
center_log16 = 1 / v
center_log2 = center_log16 / 4

assert v == Fraction(5, 6)
assert M2 == Fraction(17, 18)
assert tau2 == Fraction(204, 125)
assert center_log16 == Fraction(6, 5)
assert center_log2 == Fraction(3, 10)

# Spectral transfer.  For an adj-Ramanujan (K+1,k+1)-bigraph,
# every nontrivial squared adjacency singular value is either 0 or in
# [K+k-2 sqrt(Kk), K+k+2 sqrt(Kk)].  Here sqrt(Kk)=4 exactly.
sqrt_Kk = 4
s2_lo = K + k - 2 * sqrt_Kk
s2_hi = K + k + 2 * sqrt_Kk
q_lo = Fraction(s2_lo - left_degree, halved_degree)
q_hi = Fraction(s2_hi - left_degree, halved_degree)
q_zero = Fraction(-left_degree, halved_degree)

assert (s2_lo, s2_hi) == (2, 18)
assert q_lo == Fraction(-7, 18)
assert q_hi == Fraction(1, 2)
assert q_zero == Fraction(-1, 2)

# Green-function specialization of Evra--Feigon--Maurischat--Parzanchevski.
# Choose their exceptional-multiplicity exponent 3/8+eps with eps=1/16.
# At r=log_16 N, the exceptional term E/4^r is O(N^{-1/16}).
eps_exp = Fraction(1, 16)
exception_exp = Fraction(3, 8) + eps_exp
residual_exp = Fraction(1, 2) - exception_exp
assert exception_exp == Fraction(7, 16)
assert residual_exp == Fraction(1, 16)

# Long-range-expansion obstruction: the halved universal cover grows by Kk=16
# per radial layer, whereas an 18-regular tree grows by 17.
branching = K * k
assert halved_degree == 18
assert branching == 16
assert branching < halved_degree - 1

print("K,k =", K, k)
print("left_degree,right_degree =", left_degree, right_degree)
print("halved_degree =", halved_degree)
print("radial_counts =", counts)
print("v =", v)
print("M2 =", M2)
print("tau^2 =", tau2)
print("center coefficient vs log_16 n =", center_log16)
print("center coefficient vs log_2 n =", center_log2)
print("adj-Ramanujan s^2 interval =", (s2_lo, s2_hi))
print("output bulk eigenvalue interval =", (q_lo, q_hi))
print("zero singular-value output eigenvalue =", q_zero)
print("spectral gap >=", 1 - q_hi)
print("Green exceptional exponent chosen =", exception_exp)
print("Green residual exponent at entropic shell =", residual_exp)
print("branching =", branching, "< regular-tree branching =", halved_degree - 1)
print("P26_T08_BIGRAPH_HALVED_GREEN_EXACT_PASS")
