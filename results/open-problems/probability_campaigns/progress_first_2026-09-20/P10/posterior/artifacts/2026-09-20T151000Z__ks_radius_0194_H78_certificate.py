#!/usr/bin/env python3
"""P10/F0119 outward-rounded certificate: arbitrary-orbit KS ball rho=97/500=0.194.

Inputs proved in the path-scoped P10 history:
  H4 >= (r^4+s^4)/18,
  H5 >= -C5*rho*(r^4+s^4), C5=-1/12+31*sqrt(2)/144,
  H6 >= (13/405)*rho^2*(r^4+s^4).

New exact homogeneous terms (derived in the report from D3 invariant theory) are
  H7 = a(A^2 C+B^2 D)+b AB(C+D)+g(C B^2+A^2 D),
  a=-1/2+sqrt(2)/16, b=-7sqrt(2)/24, g=-19sqrt(2)/48,
and
  H8 = 27/64(A^4+B^4)+1/4(A C^2+B D^2)
       +1/6(A B^3+A^3 B)+1/16 C D(A+B)-59/288 A^2 B^2.
Here A=r^2, B=s^2, C=r^3 x, D=s^3 y, x,y in [-1,1].

For r>=s=tr and rho<=97/500, H7+H8 is minimized over x,y on the
box at x=y=1. The report gives the elementary derivative proof. We retain these
two exact degrees and bound only degree >=9 absolutely.
"""
import mpmath as mp
mp.mp.dps = 80
iv = mp.iv

R = iv.mpf(97)/500
SQ2 = iv.sqrt(2)
C5 = -iv.mpf(1)/12 + 31*SQ2/144
C6 = iv.mpf(13)/405
a = -iv.mpf(1)/2 + SQ2/16
b = -7*SQ2/24
g = -19*SQ2/48

# Derivative tests proving that, for every t in [0,1] and every r<=R,
# the exact H7+r*H8 angular polynomial is minimized at x=y=1.
# d/dx <= a + R*(1/2+1/8), because b,g<0 and t^3(1+t^2)/16<=1/8.
dx_upper = a + R*(iv.mpf(5)/8)
# For t>0 divide d/dy by t^3:
# <= g + R*(1/2+1/8), since a,b<0.
dy_over_t3_upper = g + R*(iv.mpf(5)/8)

def h7_at_11(t):
    den = 1+t**4
    return (a*(1+t**7)+b*(t**2+t**5)+g*(t**3+t**4))/den

def h8_at_11(t):
    den = 1+t**4
    return ((iv.mpf(27)/64)*(1+t**8)
            +(iv.mpf(1)/6)*(t**2+t**6)
            -(iv.mpf(59)/288)*t**4
            +(iv.mpf(1)/4)*(1+t**8)
            +(iv.mpf(1)/16)*t**3*(1+t**2))/den

# Degree >=9 endpoint entropy tail.
# B9(v)=(2v)^9/[72(1-2v)].
def endpoint9_coeff(v):
    return ((iv.mpf(32)/9)/(1-2*v)
            +(iv.mpf(64)/9)*(iv.mpf(2)**(-iv.mpf(9)/2))/(1-SQ2*v))

def tail9_coeff(t):
    """Upper interval for |R_{>=9}|/[r^5(r^4+s^4)] at r<=R,s=tr."""
    one = iv.mpf(1)
    den = one+t**4
    z = R**2*t

    Ce = (endpoint9_coeff(R)+t**9*endpoint9_coeff(t*R))/den

    # KL interaction after retaining c^4: tail starts at c^5.
    Cjd = R*t**5/(20*(1-z)*den)

    ell = (one+t)/SQ2
    q = t/2

    # (1+c)^(-2) tails.
    # k>=3: sum (k+1)z^(k-3) = (4-3z)/(1-z)^2.
    # k>=2: sum (k+1)z^(k-2) = (3-2z)/(1-z)^2.
    C22 = (4-3*z)/(1-z)**2
    C21 = (3-2*z)/(1-z)**2
    Ccub = (iv.mpf(1)/3)/den * (
        ell**3*t**3*C22
        +3*R*ell**2*q*t**3*C22
        +3*ell*q**2*t**2*C21
        +R*q**3*t**2*C21
    )

    # (1+c)^(-3) tails.
    # k>=3, k>=2, k>=1 respectively.
    C32 = (10-15*z+6*z**2)/(1-z)**3
    C31 = (6-8*z+3*z**2)/(1-z)**3
    C30 = (3-3*z+z**2)/(1-z)**3
    Cquart = (iv.mpf(2)/9)/den * (
        R*ell**4*t**3*C32
        +4*ell**3*q*t**2*C31
        +6*R*ell**2*q**2*t**2*C31
        +4*ell*q**3*t*C30
        +R*q**4*t*C30
    )
    return Ce+Cjd+Ccub+Cquart

def margin_box(t):
    h7 = h7_at_11(t)
    h8 = h8_at_11(t)
    tail = tail9_coeff(t)
    return (iv.mpf(1)/18-C5*R+C6*R**2
            +h7*R**3+h8*R**4-tail*R**5)

# Endpoint r=R controls the whole ball. Indeed h7<=0, tail coefficients increase
# with r, and h8(t)<=115/144 on [0,1]. Hence
# d/dr lower_bound <= -C5+2*C6*R+4*(115/144)*R^3 <0.
radial_derivative_upper = -C5+2*C6*R+4*(iv.mpf(115)/144)*R**3

N = 8000
minimum_lower = mp.inf
worst = None
for j in range(N):
    t = iv.mpf([mp.mpf(j)/N, mp.mpf(j+1)/N])
    m = margin_box(t)
    lo = mp.mpf(m.a)
    if lo < minimum_lower:
        minimum_lower = lo
        worst = (j,m)

print("rho", R)
print("dx_upper", dx_upper)
print("dy_over_t3_upper", dy_over_t3_upper)
print("radial_derivative_upper", radial_derivative_upper)
print("minimum_margin_lower", minimum_lower)
print("worst_box", worst)
assert dx_upper.b < 0
assert dy_over_t3_upper.b < 0
assert radial_derivative_upper.b < 0
assert minimum_lower > mp.mpf("0.0008")
print("OVERALL_PASS")
