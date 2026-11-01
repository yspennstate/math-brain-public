from fractions import Fraction
from math import gcd

# Exact finite-core checker for R16 / I0036.
# It certifies three algebraic obstruction facts used in the accompanying report.
# No floating-point comparison is used.

N = 48
k = 5

# Parafermionic phase lambda = exp(-i*5*pi/24) is a primitive 48th root.
# Multiplication by 5 therefore permutes Z/48, so the uniform phase profile
# has zero k=5 Fourier coefficient.
assert gcd(k, N) == 1
residues = sorted((k * r) % N for r in range(N))
assert residues == list(range(N))

# Formal cyclotomic cancellation:
# (X-1)(1+X+...+X^47) = X^48 - 1.
S = [1] * N
prod = [0] * (N + 1)
for i, c in enumerate(S):
    prod[i] -= c
    prod[i + 1] += c
target = [-1] + [0] * (N - 1) + [1]
assert prod == target

# Local three-direction positivity obstruction.
# After an invertible real-linear normalization, the three 120-degree
# honeycomb direction vectors may be represented by these integer vectors.
# They sum to zero and the first two span R^2. Hence if a real linear
# functional is nonnegative on all three, all three values sum to zero and
# must vanish; spanning then forces the functional itself to be zero.
v1 = (2, 0)
v2 = (-1, 1)
v3 = (-1, -1)
dir_sum = (v1[0] + v2[0] + v3[0], v1[1] + v2[1] + v3[1])
assert dir_sum == (0, 0)
det12 = v1[0] * v2[1] - v1[1] * v2[0]
assert det12 != 0

# Abstract strip-gap obstruction, normalized so the critical point is y=1.
# For any eta>0 and B>0,
#     F(y)=a/(1-y/(1+eta)),  a=B*eta/(1+eta),
# has nonnegative coefficients, radius 1+eta, and F(1)=B.
# Thus a fixed critical value alone cannot force a positive radius gap.
# The report proves the identity symbolically; these exact rational instances
# exercise the template over six decades.
for Neta in [2, 3, 5, 10, 100, 1000, 1_000_000]:
    eta = Fraction(1, Neta)
    B = Fraction(7, 13)
    a = B * eta / (1 + eta)
    F1 = a / (1 - Fraction(1, 1) / (1 + eta))
    assert F1 == B

print("R16 I0036 exact parafermionic / strip-gap obstruction checker")
print(f"gcd({k},{N}) = {gcd(k, N)}")
print("multiplication by 5 permutes Z/48 =", residues == list(range(N)))
print("(X-1)(1+...+X^47)=X^48-1 =", prod == target)
print("normalized 3-direction sum =", dir_sum)
print("det(v1,v2) =", det12)
print("fixed-value rational-series template exact for eta=1/N, N up to 10^6 = PASS")
print("CONCLUSION 1: uniform nonnegative 48-phase profile has total mass 48 but zero k=5 parafermionic Fourier mode.")
print("CONCLUSION 2: no nonzero real linear functional is nonnegative on all three local direction vectors.")
print("CONCLUSION 3: a fixed critical generating-function value alone gives no positive lower bound on radius gap.")
print("ALL_EXACT_CHECKS_PASS")
