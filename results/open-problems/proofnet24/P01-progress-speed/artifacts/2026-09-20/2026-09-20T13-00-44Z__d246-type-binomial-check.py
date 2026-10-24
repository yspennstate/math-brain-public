from fractions import Fraction as Q
from math import comb

# Exact checker for the P01 T06 {1,246}, p<=19/50 theorem.
# All theorem-critical comparisons use Fraction, not floating point.

D = 246
PMIN = Q(3, 8)
P0 = Q(19, 50)
LAM0 = Q(1661, 2500)   # 0.6644
L = Q(2, 3)
U = Q(34783, 50000)    # 0.69566


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
    # Lower high-type escape mean at the hardest lower-mixture/right-bias corner.
    mu_lower, M = lower_mean_and_high(D, pmin, L)

    # Uniform upper conditional sibling means from the self-consistent mean cap.
    U1 = u/(lam0+u)
    UD = Q(D)*u/(lam0+Q(D)*u)
    assert UD > U1

    c0 = 1-lam0
    cL = 1-L

    # Safe separation of the lambda-dependent numerator and denominator:
    # M(M-c)/lambda is increasing in lambda (M<1), while the reciprocal-square
    # denominator is worst at lambda=L.
    pref = Q(D)*M*(M-c0)/lam0

    # The sibling type count K is Bin(D,p); the summand decreases in K, hence
    # p=p0 is the worst mixture in the band pmin<=p<=p0.
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

    # Exact p-uniformity cubic from differentiating F(Theta(p),C(p)).
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


# 1. Support-free predecessor covers [0,LAM0] at the full p cap.
support_slack = 1-(2*P0*LAM0*LAM0+LAM0)
assert support_slack > 0

# 2. Uniform same-law escape-mean upper cap mu<=U on [LAM0,L], p<=P0.
qcap = qpoly(D, P0, LAM0, U)
assert qcap > 0
q_lam_slope = (D+1)*U + 2*LAM0 - (1+P0*(D-1))
assert q_lam_slope > 0

# 3. Static Aidekon ratio hypothesis throughout the strip.
ratio_slack = Q(D)*(1-L) - (1+L)
assert ratio_slack > 0

# 4. New type-conditioned/binomial high-degree derivative score.
J, mu_lower, M, U1, UD = jstar(D, PMIN, P0, LAM0, L, U)
assert J > 0
assert M < 1
# Sufficient convexity for x(x-c)/(lambda(x+a)^2) on x in [c,1].
amin = Q(D)*U1 - (1-LAM0)
assert amin > 3

# 5. Uniform lambda and theta monotonicity reduction.
delta, margin, thetaL, CL, N, Np = endpoint_certificate(D, P0, L, J)
Cprime_slack = 1/(1-LAM0)**2 - P0*J
assert Cprime_slack > 0
C_lam0 = LAM0/(1-LAM0) - P0*LAM0*J
theta_direction_slack = C_lam0*(1-2*thetaL) - 1
assert theta_direction_slack > 0

# 6. Uniformity in p. Here N''(p)=6H((1-t)p-1)<0 on [0,1].
# N(P0)<0<N'(P0) therefore forces N(p)<0 for all p<=P0.
assert N < 0
assert Np > 0

# 7. Positive endpoint numerator and the clean quantitative derivative margin.
assert delta > 0
assert margin > Q(1, 250000)

# 8. The inherited exact-static theorem covers p<=p2(D), in particular p<=3/8.
p2 = Q(3, 8) + Q(35, 32*D) + Q(435, 128*D*D)
assert p2 > PMIN

# 9. Immediate breadth extension attempt: same certificate at D=247 is negative.
D2 = 247
U2 = Q(34784, 50000)
assert qpoly(D2, P0, LAM0, U2) > 0
J2, mu2, M2, U12, UD2 = jstar(D2, PMIN, P0, LAM0, L, U2)
delta2, margin2, theta2, C2, N2, Np2 = endpoint_certificate(D2, P0, L, J2)
assert delta2 < 0

print('ALL_EXACT_CHECKS_PASS')
print('D=246 p<=19/50 lambda<=2/3')
print('support_free_slack_at_lambda0 =', support_slack)
print('mean_cap_Q =', qcap)
print('mean_cap_lambda_slope =', q_lam_slope)
print('static_ratio_slack =', ratio_slack)
print('mu_lower_at_(p=3/8,L=2/3) =', mu_lower, float(mu_lower))
print('high_type_mean_lower_M =', M, float(M))
print('U1 =', U1, float(U1))
print('UD =', UD, float(UD))
print('amin =', amin, float(amin))
print('Jstar approx =', float(J))
print('Cprime_slack approx =', float(Cprime_slack))
print('theta_direction_slack approx =', float(theta_direction_slack))
print('p_uniform_N(P0) approx =', float(N))
print('p_uniform_Nprime(P0) approx =', float(Np))
print('delta approx =', float(delta))
print('derivative_margin approx =', float(margin))
print('margin_gt_1/250000 =', margin > Q(1,250000))
print('static_p2_minus_3/8 =', p2-PMIN, float(p2-PMIN))
print('D=247 boundary delta approx =', float(delta2))
print('D=247 boundary margin approx =', float(margin2))
