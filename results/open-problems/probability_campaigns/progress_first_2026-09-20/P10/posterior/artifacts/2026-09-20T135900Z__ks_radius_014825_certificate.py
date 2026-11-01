#!/usr/bin/env python3
"""Outward-rounded certificate for P10/F0119: arbitrary-orbit KS ball rho=593/4000.

At lambda_*=1/sqrt(2), prior exact work gives
  H_4 >= (r^4+s^4)/18,
  |H_5| <= C5*rho*(r^4+s^4),
  H_6 >= (13/405)*rho^2*(r^4+s^4),
with C5=-1/12+31*sqrt(2)/144 and rho=max(r,s).

This certificate improves the degree>=7 remainder bound by preserving the exact
radial ratio t=min(r,s)/max(r,s) instead of replacing r^4+s^4 by rho^4.
By p<->q symmetry take r>=s, put s=t r, 0<=t<=1, and normalize the tail by
r^3(r^4+s^4)=r^7(1+t^4). All formulas below are direct absolute bounds for
the endpoint entropy tail, KL fusion interaction tail, and the cubic/quartic
polynomial fusion denominator tails.
"""
import mpmath as mp
mp.mp.dps = 80
iv = mp.iv

RHO = iv.mpf(593)/4000  # 0.14825 exactly as a rational input
SQ2 = iv.sqrt(2)
C5 = -iv.mpf(1)/12 + 31*SQ2/144
C6 = iv.mpf(13)/405

# If B7(v)=(2v)^7/[42(1-2v)], then
# (1/2)B7(v)+B7(v/sqrt(2)) = endpoint_coeff(v)*v^7.
def endpoint_coeff(v):
    return ((iv.mpf(32)/21)/(1-2*v)
            +(iv.mpf(64)/21)*(iv.mpf(2)**(-iv.mpf(7)/2))/(1-SQ2*v))

def tail_coeff(t):
    """Upper interval for |R_{>=7}|/[r^3(r^4+s^4)] at r<=RHO,s=tr."""
    one = iv.mpf(1)
    z = RHO**2 * t            # |c_g| <= r s <= RHO^2 t
    den4 = one + t**4

    # Endpoint Psi tails for p and q.
    Ce = (endpoint_coeff(RHO) + t**7*endpoint_coeff(t*RHO))/den4

    # J_D tail after c^2 and c^3: (rs)^4/[12(1-rs)].
    Cjd = RHO*t**4/(12*(1-z)*den4)

    # For one relative orbit, L=(m+gn)/sqrt(2), Q=conj(m)conj(gn)/2.
    # Hence |L|<=r*l and |Q|<=r^2*q.
    ell = (one+t)/SQ2
    q = t/2

    # Tails of (1+c)^(-2):
    # sum_{k>=2}(k+1)z^(k-2) and sum_{k>=1}(k+1)z^(k-1).
    C21 = (3-2*z)/(1-z)**2
    C20 = (2-z)/(1-z)**2
    Ccub = (iv.mpf(1)/3)/den4 * (
        ell**3*t**2*C21
        + 3*RHO*ell**2*q*t**2*C21
        + 3*ell*q**2*t*C20
        + RHO*q**3*t*C20
    )

    # Tails of (1+c)^(-3):
    # sum_{k>=2} binom(k+2,2) z^(k-2), sum_{k>=1} ... z^(k-1), and full sum.
    C31 = (6-8*z+3*z**2)/(1-z)**3
    C30 = (3-3*z+z**2)/(1-z)**3
    inv3 = 1/(1-z)**3
    Cquart = (iv.mpf(2)/9)/den4 * (
        RHO*ell**4*t**2*C31
        + 4*ell**3*q*t*C30
        + 6*RHO*ell**2*q**2*t*C30
        + 4*ell*q**3*inv3
        + RHO*q**4*inv3
    )
    return Ce + Cjd + Ccub + Cquart

# Rigorous 1D cover of t in [0,1]. The interval overestimate is harmless;
# 6000 rational boxes leave a comfortable positive final margin.
N = 6000
sup_hi = mp.mpf('0')
sup_box = None
for j in range(N):
    t = iv.mpf([mp.mpf(j)/N, mp.mpf(j+1)/N])
    val = tail_coeff(t)
    hi = mp.mpf(val.b)
    if hi > sup_hi:
        sup_hi = hi
        sup_box = (j, val)

# f(r)=1/18-C5*r+C6*r^2 is decreasing on [0,RHO], since C5-2*C6*RHO>0.
# Every positive tail coefficient above is nondecreasing in r, so
# r^3*Ctail(r,t) <= RHO^3*Ctail(RHO,t). Thus the endpoint r=RHO controls
# the full ball, not merely the outer sphere.
monotone = C5 - 2*C6*RHO
lower_degree = iv.mpf(1)/18 - C5*RHO + C6*RHO**2
margin = lower_degree - iv.mpf([sup_hi,sup_hi])*RHO**3

print('rho', RHO)
print('C5_sharp', C5)
print('C6_rho2_coefficient', C6)
print('monotone_check_C5_minus_2C6rho', monotone)
print('tail_sup_upper', sup_hi)
print('tail_sup_box', sup_box)
print('lower_degree', lower_degree)
print('normalized_margin', margin)
assert monotone.a > 0
assert margin.a > mp.mpf('0.00003')
print('OVERALL_PASS')
