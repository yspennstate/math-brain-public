#!/usr/bin/env python3
from fractions import Fraction as F
from math import factorial

# PROB10-05 exact self-check for the multimode Hermite-compression improvement.
# Inherited, separately archived repository inputs:
#   tr(K^4) < 54959/50000 from the corrected M=500 four-cycle certificate;
#   degree-48 Perron quasimode bounds
#       91219830/1e8 < mu < 91219831/1e8,
#       eps^2 < 25851/1e9.
# This checker proves the new finite-dimensional min-max lower bounds on
# lambda_3,...,lambda_6, the infinite even-Hermite tail, and the resulting
# Kato-Temple synthesis theta_{2,1/4} > 85887/500000.

r = F(7, 8)
s = F(24861, 25000)
c = s * F(1 + r, 2)
trace4 = F(54959, 50000)
mu_lo = F(91219830, 100000000)
mu_hi = F(91219831, 100000000)
eps2_hi = F(25851, 1000000000)

# Rationalized columns selected before certification from the first six
# numerical Ritz vectors of the degree-10 Hermite compression. Coordinates
# are in the unnormalized probabilists' Hermite basis He_0,...,He_10.
Q = [
    [100000000, -51111650, 100000000, -100000000, 100000000, -100000000],
    [-97698347, -34302382, 51205642, -45364478, 41170732, -28604368],
    [22584157, 100000000, -78315567, 64148896, -59457646, 59447237],
    [5911776, -56075583, -56995273, 34121522, -26987709, 17006750],
    [-1844271, 8116046, 89282967, -25935037, 19711163, -18662113],
    [-734902, 2386411, -36959980, -19457525, 10203560, -5235881],
    [157537, -478825, 3938761, 22142716, -5566803, 4272518],
    [77694, -204497, 1218570, -7598957, -3861278, 1136002],
    [-11838, 32505, -190798, 696268, 3744935, -873242],
    [-6841, 16441, -79745, 199632, -1186425, -204403],
    [871, -2377, 13057, -35395, 133938, 245510],
]

# The exact opposite-parity Hermite entries contain the single scalar
# tau=sqrt(c/(2*pi)).  Classical rational pi bounds suffice for a robust
# outward enclosure.
pi_lo = F(333, 106)
pi_hi = F(355, 113)
tau_lo = F(38519, 100000)
tau_hi = F(38521, 100000)
assert pi_lo < pi_hi
assert tau_lo * tau_lo < c / (2 * pi_hi)
assert tau_hi * tau_hi > c / (2 * pi_lo)


def mhe(i, j, tau):
    """<He_i,K He_j> evaluated at an endpoint tau."""
    if (i + j) % 2 == 0:
        return F(factorial(i)) * r**i / 2 if i == j else F(0)
    out = F(0)
    for k in range(min(i, j) + 1):
        n = i + j - 2 * k
        m = (n - 1) // 2
        # E[He_n(W)1_{W<0}] / phi(0), n=2m+1.
        half_over_phi0 = -F(((-1) ** m) * factorial(2 * m), 2**m * factorial(m))
        coeff = F(
            factorial(i) * factorial(j),
            factorial(k) * factorial(i - k) * factorial(j - k),
        )
        out += coeff * r**k * c**m * half_over_phi0
    return tau * out


def full_BG(tau):
    M = [[mhe(i, j, tau) for j in range(11)] for i in range(11)]
    B = [[F(0) for _ in range(6)] for __ in range(6)]
    G = [[F(0) for _ in range(6)] for __ in range(6)]
    for a in range(6):
        for b in range(6):
            G[a][b] = sum(F(Q[i][a] * Q[i][b] * factorial(i)) for i in range(11))
            B[a][b] = sum(
                F(Q[i][a] * Q[j][b]) * M[i][j]
                for i in range(11)
                for j in range(11)
            )
    return B, G


def ldlt_pivots(A):
    """Exact no-pivot LDL^T; positive pivots certify positive definiteness."""
    n = len(A)
    L = [[F(0)] * n for _ in range(n)]
    D = [F(0)] * n
    for i in range(n):
        L[i][i] = F(1)
        z = A[i][i] - sum(L[i][k] * L[i][k] * D[k] for k in range(i))
        D[i] = z
        assert z > 0
        for j in range(i + 1, n):
            z = A[j][i] - sum(L[j][k] * L[i][k] * D[k] for k in range(i))
            L[j][i] = z / D[i]
    return D


# If B-aG is positive definite on a k-dimensional trial subspace then, by
# min-max, the kth largest positive eigenvalue of K is > a.  Since B-aG is
# affine in tau and the positive-definite cone is convex, endpoint checks
# cover the whole tau interval.
targets = [
    (3, F(11, 20)),
    (4, F(53, 125)),
    (5, F(323, 1000)),
    (6, F(4, 25)),
]
min_pivots = []
for tau in (tau_lo, tau_hi):
    B, G = full_BG(tau)
    for k, a in targets:
        C = [[B[i][j] - a * G[i][j] for j in range(k)] for i in range(k)]
        piv = ldlt_pivots(C)
        min_pivots.append((tau, k, min(piv)))

# The even-Hermite compression is diagonal with entries r^(2m)/2.
# Interlacing therefore gives lambda_j >= r^(2(j-1))/2 for every j>=1.
# After using stronger finite-dimensional bounds for j=3,4,5,6, retain the
# geometric even-Hermite lower tail from j=7 onward.
positive_tail = sum(a**4 for _, a in targets) + r**48 / (F(16) * (1 - r**8))

# New source-level threshold.
theta = F(85887, 500000)  # 0.171774
x = F(456167, 500000)     # 0.912334
beta = F(36071, 50000)    # 0.72142

# x < r^(4 theta), since 4 theta = 85887/125000.
assert x**125000 < r**85887

# Under lambda_1 >= r^(4 theta) > x, trace(K^4) and the certified positive
# modes force lambda_2 < beta.
trace_margin = beta**4 - (trace4 - x**4 - positive_tail)
assert trace_margin > 0
assert mu_lo > beta
assert x > mu_hi

# Kato-Temple contradiction with the inherited degree-48 residual.
temple_margin = (x - mu_hi) * (mu_lo - beta) - eps2_hi
assert temple_margin > 0

old_theta = F(171587, 1000000)
old_width = F(1, 4) - old_theta
new_width = F(1, 4) - theta
assert theta > old_theta
assert old_width - new_width == theta - old_theta

print('tau interval =', float(tau_lo), float(tau_hi))
for tau, k, p in min_pivots:
    print('positive LDL min pivot', float(tau), 'k', k, '=', float(p))
print('certified positive-mode fourth tail L =', positive_tail, float(positive_tail))
print('inherited trace4 cap =', trace4, float(trace4))
print('theta old/new =', old_theta, theta, float(old_theta), float(theta))
print('x,beta =', x, beta, float(x), float(beta))
print('trace-budget margin =', trace_margin, float(trace_margin))
print('Temple margin =', temple_margin, float(temple_margin))
print('old/new width =', old_width, new_width, float(old_width), float(new_width))
print('source gain =', theta - old_theta, float(theta - old_theta))
print('ALL_EXACT_CHECKS_PASS = True')
