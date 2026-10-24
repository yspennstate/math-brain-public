#!/usr/bin/env python3
from fractions import Fraction as F

# HARD7-05 exact self-check.
# This certifies only the finite algebra used in the new source-side comparison:
#   (i) direct source-covariance domination at lags 1 and 2 for q=r=4/5;
#   (ii) inherited-envelope domination at every k>=3;
#   (iii) the exact n=8 Gaussian-loop covariance algebra for the trace route.
# It does NOT certify a new numerical upper bound on the Volterra/operator norm.

q = F(4, 5)
r = q
r0 = F(287831, 500000)
C1 = (1 + r) / 2
C2 = C1 * r


def strict_source_cov_bound(u, cap):
    # Inherited exact H=1/4 source covariance formula:
    # R(u)-u=(1-u^2)/(6u^5)[-P(z)+2(1+z)(1-z^2)^(3/2)], z=u^2,
    # P(z)=2+2z-3z^2-2z^3-2z^4.
    # To prove R(u)<cap, move cap-u to the rational side and square after
    # checking positivity of that side.
    z = u * u
    P = 2 + 2*z - 3*z*z - 2*z**3 - 2*z**4
    D = 6*u**5*(cap-u)/(1-u*u)
    T = P + D
    lhs_sq = 4*(1+z)**2*(1-z*z)**3
    assert T > 0
    assert lhs_sq < T*T
    return T*T - lhs_sq


lag1_margin = strict_source_cov_bound(q, C1)
lag2_margin = strict_source_cov_bound(q*q, C2)

assert C1 == F(9, 10)
assert C2 == F(18, 25)
assert q**3 == F(64, 125)
assert q**3 < r0
assert C1 / q == F(9, 8)

# For k>=3 the inherited source envelope gives R(q^k)<=q^k because q^k<=q^3<r0.
# The edge-smoothed comparator has C_k=C1*r^(k-1), and q=r, so C_k/q^k=9/8.
for k in range(3, 40):
    Ck = C1 * r**(k-1)
    assert q**k < Ck

# Exact n=8 Gaussian-loop covariance for the even-trace route.
# Normalized loop covariance: C_d=(r^d+r^(n-d))/(1-r^n).
# Its inverse is the cyclic AR precision with diagonal (1+r^2)/(1-r^2)
# and nearest-neighbor entries -r/(1-r^2).
n = 8
s2 = 1 - r*r
loop_cov = [(r**d + r**(n-d))/(1-r**n) for d in range(n)]
Q = [[F(0) for _ in range(n)] for __ in range(n)]
for i in range(n):
    Q[i][i] = (1+r*r)/s2
    Q[i][(i-1) % n] = -r/s2
    Q[i][(i+1) % n] = -r/s2

for i in range(n):
    for j in range(n):
        val = sum(Q[i][k] * loop_cov[(k-j) % n] for k in range(n))
        assert val == (1 if i == j else 0)

trace_P8 = 1/(1-r**8)
assert trace_P8 == F(390625, 325089)

print('q =', q, 'r =', r)
print('C1 =', C1, 'C2 =', C2)
print('q^3 =', q**3, '< r0 =', r0)
print('lag1 squared-margin =', lag1_margin)
print('lag2 squared-margin =', lag2_margin)
print('C_k/q^k for k>=1 =', C1/q)
print('loop n =', n)
print('loop covariance first row =', loop_cov)
print('tr(P_r^8) =', trace_P8)
print('ALL_EXACT_CHECKS_PASS = True')
