from fractions import Fraction as Q
from math import comb

# P01 T06 exact checker: full D=246, p<=19/50, lambda<=2/3 rectangle.
# Every theorem-critical comparison is exact rational arithmetic.

D = 246
PMIN = Q(3, 8)
P0 = Q(19, 50)
LAM0 = Q(1661, 2500)   # 0.6644
L = Q(2, 3)
U = Q(34783, 50000)    # 0.69566
TARGET = Q(1, 250000)


def bmin(n, lam):
    return Q(n) * (1-lam) / (Q(n) - Q(n-1)*lam)


def chord_coeff(n, lam):
    c = 1-lam
    blo = bmin(n, lam)
    bhi = Q(n)/(Q(n)+lam)
    slope = (bhi-blo)/lam
    intercept = blo - slope*c
    return intercept, slope


def lower_mean_and_high(D, p, lam):
    a1, s1 = chord_coeff(1, lam)
    aD, sD = chord_coeff(D, lam)
    A = (1-p)*a1 + p*aD
    B = (1-p)*s1 + p*sD
    assert 0 <= B < 1
    mu_lower = A/(1-B)
    high_lower = aD+sD*mu_lower
    return mu_lower, high_lower


def qpoly(D, p, lam, u):
    return (Q(D)*u*u + (lam*(D+1)-D)*u
            + lam*lam - lam*(1+p*(D-1)))


def theta_bound(D, p, lam):
    t = (1+lam)/(Q(D)+lam)
    return p*t/(1-p+p*t), t


def jstar(D, pmin, p0, lam0, L, u):
    mu_lower, M = lower_mean_and_high(D, pmin, L)

    # Uniform upper conditional sibling means from E B <= u.
    U1 = u/(lam0+u)
    UD = Q(D)*u/(lam0+Q(D)*u)
    assert UD > U1

    c0 = 1-lam0
    cL = 1-L

    # Exact distinguished-branch lower factor from Z >= B(B-c)/lambda.
    # M(M-c)/lambda increases with lambda for M<1, so lambda0 is worst.
    pref = Q(D)*M*(M-c0)/lam0

    # K~Bin(D,p); denominator worsens with K and hence with p. Use p0.
    s = Q(0)
    for k in range(D+1):
        prob = Q(comb(D, k))*p0**k*(1-p0)**(D-k)
        den = M + Q(D-k)*U1 + Q(k)*UD - cL
        s += prob/(den*den)

    return pref*s, mu_lower, M, U1, UD


def endpoint_certificate(D, p, L, J):
    h = D-1
    theta, t = theta_bound(D, p, L)
    C = L/(1-L) - p*L*J
    delta = 1 + Q(h)*theta - Q(h)*C*theta*(1-theta)
    margin = 2*delta/(1+Q(h)*theta+L)**2

    H = L*J
    Cbase = L/(1-L)
    N = (1-Cbase
         + p*(Cbase*(1+t)+t-1+2*H)
         - 3*H*p*p
         + H*(1-t)*p**3)
    Np = (Cbase*(1+t)+t-1+2*H
          - 6*H*p
          + 3*H*(1-t)*p*p)
    return delta, margin, theta, C, N, Np


def support_free_margin(p, L):
    # P01 support-free minimum-one theorem.
    return 2*(1-p)*(1-L-2*p*L*L)/((1-L)*(1+L)**2)


def static_margin(D, p0):
    # P01 exact static theorem at L=2/3.
    theta = Q(5)*p0/(Q(3*D+2)-Q(3*(D-1))*p0)
    delta = 1-Q(D-1)*theta+Q(2*(D-1))*theta*theta
    return 2*delta/(Q(5,3)+Q(D-1)*theta)**2


# A. Low-p part: latest static theorem covers p<=3/8 on all [0,2/3].
low_p_margin = static_margin(D, PMIN)
assert low_p_margin > TARGET

# B. Upper-p lower strip: support-free theorem covers p<=19/50 on [0,LAM0].
support_slack = 1-(2*P0*LAM0*LAM0+LAM0)
assert support_slack > 0
lower_strip_margin = support_free_margin(P0, LAM0)
assert lower_strip_margin > TARGET

# C. Upper-p new strip [LAM0,2/3]. Uniform E B <= U.
qcap = qpoly(D, P0, LAM0, U)
assert qcap > 0
q_lam_slope = (D+1)*U + 2*LAM0 - (1+P0*(D-1))
assert q_lam_slope > 0

# Same-law static ratio hypothesis.
ratio_slack = Q(D)*(1-L) - (1+L)
assert ratio_slack > 0

# New type-conditioned/binomial high-degree derivative score.
J, mu_lower, M, U1, UD = jstar(D, PMIN, P0, LAM0, L, U)
assert J > 0 and M < 1
amin = Q(D)*U1 - (1-LAM0)
assert amin > 3   # sufficient for monotonicity/convexity of x(x-c)/(x+a)^2 on [c,1]

# Lambda/tilt/p endpoint reductions.
delta, new_band_margin, thetaL, CL, N, Np = endpoint_certificate(D, P0, L, J)
Cprime_slack = 1/(1-LAM0)**2 - P0*J
assert Cprime_slack > 0
C_lam0 = LAM0/(1-LAM0) - P0*LAM0*J
theta_direction_slack = C_lam0*(1-2*thetaL) - 1
assert theta_direction_slack > 0
assert N < 0
assert Np > 0
assert delta > 0
assert new_band_margin > TARGET

# D. Complete rectangle gets the minimum of the three exact patch margins.
full_margin = min(low_p_margin, lower_strip_margin, new_band_margin)
assert full_margin > TARGET

# E. Immediate extension attempt: same certificate at D=247 fails.
D2 = 247
U2 = Q(34784, 50000)
assert qpoly(D2, P0, LAM0, U2) > 0
J2, mu2, M2, U12, UD2 = jstar(D2, PMIN, P0, LAM0, L, U2)
delta2, margin2, theta2, C2, N2, Np2 = endpoint_certificate(D2, P0, L, J2)
assert delta2 < 0

print('ALL_EXACT_CHECKS_PASS')
print('FULL_RECTANGLE: D=246, 0<p<=19/50, 0<=lambda<=2/3')
print('claimed_uniform_margin_gt_1/250000 =', full_margin > TARGET)
print('low-p static margin =', float(low_p_margin))
print('upper-p support-free lower-strip margin =', float(lower_strip_margin))
print('new-band margin =', float(new_band_margin))
print('support_free_slack =', support_slack)
print('mean_cap_Q =', qcap)
print('mean_cap_lambda_slope =', q_lam_slope)
print('static_ratio_slack =', ratio_slack)
print('mu_lower =', mu_lower, float(mu_lower))
print('high_type_mean_lower_M =', M, float(M))
print('U1 =', U1, float(U1))
print('UD =', UD, float(UD))
print('amin =', amin, float(amin))
print('Jstar approx =', float(J))
print('thetaL =', thetaL, float(thetaL))
print('Cprime_slack approx =', float(Cprime_slack))
print('theta_direction_slack approx =', float(theta_direction_slack))
print('N(P0) approx =', float(N))
print('Nprime(P0) approx =', float(Np))
print('new-band delta approx =', float(delta))
print('D=247 same-certificate delta approx =', float(delta2))
print('D=247 same-certificate margin approx =', float(margin2))
