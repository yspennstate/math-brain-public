#!/usr/bin/env python3
"""P10/F0119 certificate: exact H11/H12 continuation and arbitrary-orbit KS ball rho=0.2085.

At lambda_*=1/sqrt(2), use the independent D3 invariants
A=|m|^2, B=|n|^2, C=Re(m^3), D=Re(n^3).
The path-scoped exact formal-series computation gives

H11 = alpha(A C^3+B D^3)+beta(A^4 C+B^4 D)
      +delta(C^2 B D+A C D^2)
      +eps(A C B^3+A^3 B D)+zeta A^2 B^2(C+D),
 alpha=(-32+sqrt(2))/80,
 beta=27(-32+sqrt(2))/320,
 delta=-125 sqrt(2)/288,
 eps=-51 sqrt(2)/64,
 zeta=-55 sqrt(2)/96.

H12 = 31/528(C^4+D^4)+279/88(A^3 C^2+B^3 D^2)
      +2511/1408(A^6+B^6)+101/240 C^2 D^2
      -643/1440(C^2 B^3+A^3 D^2)
      +95/576 A B C D(A+B)
      +5/16(A^2 B^4+A^4 B^2)+833/2880 A^3 B^3.

This script certifies the analytic inequalities after those exact identities:
small-radius angular minimization through degree 12, degree>=13 remainder
control, radial monotonicity of the resulting lower bound, and an
outward-rounded t-cover at rho=417/2000=0.2085.
"""
import mpmath as mp
mp.mp.dps = 80
iv = mp.iv

R = iv.mpf(417)/2000
SQ2 = iv.sqrt(2)
C5 = -iv.mpf(1)/12 + 31*SQ2/144
C6 = iv.mpf(13)/405

a = -iv.mpf(1)/2 + SQ2/16
b = -7*SQ2/24
g = -19*SQ2/48
c1 = -iv.mpf(9)/8 + 9*SQ2/128
c2 = -iv.mpf(1)/18 + SQ2/288
c4 = SQ2/6
c5 = SQ2/12
c6 = 83*SQ2/96

alpha = -iv.mpf(2)/5 + SQ2/80
beta = -iv.mpf(27)/10 + 27*SQ2/320
delta = -125*SQ2/288
eps = -51*SQ2/64
zeta = -55*SQ2/96

u0 = iv.mpf(31)/528
u1 = iv.mpf(279)/88
u2 = iv.mpf(2511)/1408
u5 = iv.mpf(101)/240
u6 = -iv.mpf(643)/1440
u9 = iv.mpf(95)/576
u11 = iv.mpf(5)/16
u12 = iv.mpf(833)/2880

# Crude but global angular derivative envelopes.  H11 has only one
# sign-indefinite x/y derivative term, from delta*C^2 B D (or its swap).
M9 = 41*SQ2/32
M10 = iv.mpf(1499)/576
M11 = -2*delta
M12 = iv.mpf(15207)/1760

dx_upper = (a + R*(iv.mpf(5)/8) + R**2*M9 + R**3*M10
            + R**4*M11 + R**5*M12)
dy_over_t3_upper = (g + R*(iv.mpf(5)/8) + R**2*M9 + R**3*M10
                     + R**4*M11 + R**5*M12)

def h7(t):
    den = 1+t**4
    return (a*(1+t**7)+b*(t**2+t**5)+g*(t**3+t**4))/den

def h8(t):
    den = 1+t**4
    return ((iv.mpf(27)/64)*(1+t**8)
            +(iv.mpf(1)/6)*(t**2+t**6)
            -(iv.mpf(59)/288)*t**4
            +(iv.mpf(1)/4)*(1+t**8)
            +(iv.mpf(1)/16)*t**3*(1+t**2))/den

def h9(t):
    den = 1+t**4
    return ((c1+c2)*(1+t**9)
            +(c4+c5)*(t**6+t**3)
            +c6*(t**5+t**4))/den

def h10(t):
    den = 1+t**4
    return (((iv.mpf(27)/32+iv.mpf(15)/16)*(1+t**10))
            -(iv.mpf(5)/36)*t**3*(1+t**4)
            -(iv.mpf(5)/24)*t**4*(1+t**2)
            +(iv.mpf(1)/6)*(t**6+t**4)
            +(iv.mpf(67)/576)*t**5)/den

def h11(t):
    den = 1+t**4
    return (((alpha+beta)*(1+t**11)
             +(delta+eps)*(t**5+t**6)
             +zeta*(t**4+t**7))/den)

def h12(t):
    den = 1+t**4
    return (((u0+u1+u2)*(1+t**12)
             +(u5+2*u6+u12)*t**6
             +u9*t**5*(1+t**2)
             +u11*(t**4+t**8))/den)

# Degree >=13 endpoint entropy tail.
def endpoint13_coeff(v):
    return ((iv.mpf(1024)/39)/(1-2*v)
            +(iv.mpf(2048)/39)*(iv.mpf(2)**(-iv.mpf(13)/2))/(1-SQ2*v))

def tail13_coeff(t):
    """Upper interval for |R_{>=13}|/[r^9(r^4+s^4)] at r<=R,s=t r."""
    one = iv.mpf(1)
    den = one+t**4
    z = R**2*t

    Ce = (endpoint13_coeff(R)+t**13*endpoint13_coeff(t*R))/den

    # KL interaction: c^2,...,c^6 are retained; tail starts at c^7.
    Cjd = R*t**7/(42*(1-z)*den)

    ell = (one+t)/SQ2
    q = t/2

    # (1+c)^(-2): tail starts k>=5 for L^3,L^2Q and
    # k>=4 for LQ^2,Q^3.
    C25 = (6-5*z)/(1-z)**2
    C24 = (5-4*z)/(1-z)**2
    Ccub = (iv.mpf(1)/3)/den*(
        ell**3*t**5*C25
        +3*R*ell**2*q*t**5*C25
        +3*ell*q**2*t**4*C24
        +R*q**3*t**4*C24)

    # (1+c)^(-3): starts k>=5,k>=4,k>=4,k>=3,k>=3.
    C35 = (21-35*z+15*z**2)/(1-z)**3
    C34 = (15-24*z+10*z**2)/(1-z)**3
    C33 = (10-15*z+6*z**2)/(1-z)**3
    Cquart = (iv.mpf(2)/9)/den*(
        R*ell**4*t**5*C35
        +4*ell**3*q*t**4*C34
        +6*R*ell**2*q**2*t**4*C34
        +4*ell*q**3*t**3*C33
        +R*q**4*t**3*C33)

    return Ce+Cjd+Ccub+Cquart

def margin_box(t):
    return (iv.mpf(1)/18-C5*R+C6*R**2
            +h7(t)*R**3+h8(t)*R**4
            +h9(t)*R**5+h10(t)*R**6
            +h11(t)*R**7+h12(t)*R**8
            -tail13_coeff(t)*R**9)

N = 10000
minimum_lower = mp.inf
worst = None
h8_sup = mp.mpf('-inf')
h9_sup = mp.mpf('-inf')
h10_sup = mp.mpf('-inf')
h12_sup = mp.mpf('-inf')
for j in range(N):
    t = iv.mpf([mp.mpf(j)/N, mp.mpf(j+1)/N])
    m = margin_box(t)
    lo = mp.mpf(m.a)
    if lo < minimum_lower:
        minimum_lower = lo
        worst = (j,m)
    h8_sup = max(h8_sup,mp.mpf(h8(t).b))
    h9_sup = max(h9_sup,mp.mpf(h9(t).b))
    h10_sup = max(h10_sup,mp.mpf(h10(t).b))
    h12_sup = max(h12_sup,mp.mpf(h12(t).b))

# h7<0 and h11<0 for t in [0,1].  All tail coefficients increase with r.
# Hence these terms can be discarded in an upper bound on the radial
# derivative of the normalized lower bound.
radial_derivative_upper = (
    -C5 + 2*C6*R
    +4*iv.mpf([h8_sup,h8_sup])*R**3
    +5*iv.mpf([max(h9_sup,mp.mpf('0')),max(h9_sup,mp.mpf('0'))])*R**4
    +6*iv.mpf([h10_sup,h10_sup])*R**5
    +8*iv.mpf([h12_sup,h12_sup])*R**7)

print('rho',R)
print('dx_upper',dx_upper)
print('dy_over_t3_upper',dy_over_t3_upper)
print('h8_sup',h8_sup)
print('h9_sup',h9_sup)
print('h10_sup',h10_sup)
print('h12_sup',h12_sup)
print('radial_derivative_upper',radial_derivative_upper)
print('minimum_margin_lower',minimum_lower)
print('worst_box',worst)
assert dx_upper.b < 0
assert dy_over_t3_upper.b < 0
assert radial_derivative_upper.b < 0
assert minimum_lower > mp.mpf('0.00002')
print('OVERALL_PASS')
