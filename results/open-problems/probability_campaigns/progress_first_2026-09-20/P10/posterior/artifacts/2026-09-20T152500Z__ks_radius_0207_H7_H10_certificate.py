#!/usr/bin/env python3
"""P10/F0119 certificate: exact H7--H10 and arbitrary-orbit KS ball rho=207/1000.

At lambda_*=1/sqrt(2), write A=|m|^2, B=|n|^2,
C=Re(m^3), D=Re(n^3). The path-scoped exact D3 expansion gives

H7 = a(A^2 C+B^2 D)+b AB(C+D)+g(C B^2+A^2 D),
 a=-1/2+sqrt(2)/16, b=-7sqrt(2)/24, g=-19sqrt(2)/48.

H8 = 27/64(A^4+B^4)+1/4(A C^2+B D^2)
     +1/6(A B^3+A^3 B)+1/16 C D(A+B)-59/288 A^2 B^2.

H9 = c1(A^3 C+B^3 D)+c2(C^3+D^3)
     +c4(C B^3+A^3 D)+c5(C D^2+C^2 D)
     +c6(A^2 B D+A B^2 C),
 c1=-9/8+9sqrt(2)/128, c2=-1/18+sqrt(2)/288,
 c4=sqrt(2)/6, c5=sqrt(2)/12, c6=83sqrt(2)/96.

H10 = 27/32(A^5+B^5)+15/16(A^2 C^2+B^2 D^2)
      -5/36 C D(A^2+B^2)-5/24 A^2 B^2(A+B)
      +1/6(A^2 D^2+C^2 B^2)+67/576 A B C D.

The report derives these coefficients from D3 invariant theory and exact formal
series. This certificate verifies the analytic inequalities after those exact
identities: angular minimization of H7+...+H10, degree>=11 tail control, and
an outward-rounded t-cover at rho=0.207.
"""
import mpmath as mp
mp.mp.dps = 80
iv = mp.iv
R = iv.mpf(207)/1000
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

# Crude global derivative magnitudes for H9,H10 angular parts:
# M9 = c4+3*c5+c6 = 41*sqrt(2)/32.
# M10 = 15/8+5/18+1/3+67/576 = 1499/576.
M9 = 41*SQ2/32
M10 = iv.mpf(1499)/576

# The H7+...+H10 angular polynomial, after factoring r^7, has
# d/dx <= a + r*(5/8) + r^2*M9 + r^3*M10,
# and for t>0, (d/dy)/t^3 <= g + same positive remainder.
dx_upper = a + R*(iv.mpf(5)/8) + R**2*M9 + R**3*M10
dy_over_t3_upper = g + R*(iv.mpf(5)/8) + R**2*M9 + R**3*M10

def h7_11(t):
    den=1+t**4
    return (a*(1+t**7)+b*(t**2+t**5)+g*(t**3+t**4))/den

def h8_11(t):
    den=1+t**4
    return ((iv.mpf(27)/64)*(1+t**8)
            +(iv.mpf(1)/6)*(t**2+t**6)
            -(iv.mpf(59)/288)*t**4
            +(iv.mpf(1)/4)*(1+t**8)
            +(iv.mpf(1)/16)*t**3*(1+t**2))/den

def h9_11(t):
    den=1+t**4
    return ((c1+c2)*(1+t**9)
            +(c4+c5)*(t**6+t**3)
            +c6*(t**5+t**4))/den

def h10_11(t):
    den=1+t**4
    return (((iv.mpf(27)/32+iv.mpf(15)/16)*(1+t**10))
            -(iv.mpf(5)/36)*t**3*(1+t**4)
            -(iv.mpf(5)/24)*t**4*(1+t**2)
            +(iv.mpf(1)/6)*(t**6+t**4)
            +(iv.mpf(67)/576)*t**5)/den

# Degree>=11 endpoint entropy tail: B11(v)=(2v)^11/[110(1-2v)].
def endpoint11_coeff(v):
    return ((iv.mpf(512)/55)/(1-2*v)
            +(iv.mpf(1024)/55)*(iv.mpf(2)**(-iv.mpf(11)/2))/(1-SQ2*v))

def tail11_coeff(t):
    """Upper interval for |R_{>=11}|/[r^7(r^4+s^4)] at r<=R,s=tr."""
    one=iv.mpf(1)
    den=one+t**4
    z=R**2*t
    Ce=(endpoint11_coeff(R)+t**11*endpoint11_coeff(t*R))/den

    # KL interaction: c^2,c^3,c^4,c^5 are retained; tail starts c^6.
    Cjd=R*t**6/(30*(1-z)*den)

    ell=(one+t)/SQ2
    q=t/2

    # (1+c)^(-2): k>=4 and k>=3.
    C23=(5-4*z)/(1-z)**2
    C22=(4-3*z)/(1-z)**2
    Ccub=(iv.mpf(1)/3)/den*(
        ell**3*t**4*C23
        +3*R*ell**2*q*t**4*C23
        +3*ell*q**2*t**3*C22
        +R*q**3*t**3*C22)

    # (1+c)^(-3): k>=4, k>=3, k>=2.
    C33=(15-24*z+10*z**2)/(1-z)**3
    C32=(10-15*z+6*z**2)/(1-z)**3
    C31=(6-8*z+3*z**2)/(1-z)**3
    Cquart=(iv.mpf(2)/9)/den*(
        R*ell**4*t**4*C33
        +4*ell**3*q*t**3*C32
        +6*R*ell**2*q**2*t**3*C32
        +4*ell*q**3*t**2*C31
        +R*q**4*t**2*C31)
    return Ce+Cjd+Ccub+Cquart

def margin_box(t):
    return (iv.mpf(1)/18-C5*R+C6*R**2
            +h7_11(t)*R**3+h8_11(t)*R**4
            +h9_11(t)*R**5+h10_11(t)*R**6
            -tail11_coeff(t)*R**7)

N=10000
minimum_lower=mp.inf
worst=None
h8_sup=mp.mpf('-inf')
h9_sup=mp.mpf('-inf')
h10_sup=mp.mpf('-inf')
for j in range(N):
    t=iv.mpf([mp.mpf(j)/N,mp.mpf(j+1)/N])
    m=margin_box(t)
    lo=mp.mpf(m.a)
    if lo<minimum_lower:
        minimum_lower=lo
        worst=(j,m)
    h8_sup=max(h8_sup,mp.mpf(h8_11(t).b))
    h9_sup=max(h9_sup,mp.mpf(h9_11(t).b))
    h10_sup=max(h10_sup,mp.mpf(h10_11(t).b))

# All tail coefficients increase with r. h7<=0. For an upper bound on the
# radial derivative, discard the negative h7 and tail derivatives and use
# the certified suprema of h8,h9,h10.
radial_derivative_upper = (-C5+2*C6*R
                           +4*iv.mpf([h8_sup,h8_sup])*R**3
                           +5*iv.mpf([max(h9_sup,mp.mpf('0')),max(h9_sup,mp.mpf('0'))])*R**4
                           +6*iv.mpf([max(h10_sup,mp.mpf('0')),max(h10_sup,mp.mpf('0'))])*R**5)

print("rho",R)
print("dx_upper",dx_upper)
print("dy_over_t3_upper",dy_over_t3_upper)
print("h8_sup",h8_sup)
print("h9_sup",h9_sup)
print("h10_sup",h10_sup)
print("radial_derivative_upper",radial_derivative_upper)
print("minimum_margin_lower",minimum_lower)
print("worst_box",worst)
assert dx_upper.b<0
assert dy_over_t3_upper.b<0
assert radial_derivative_upper.b<0
assert minimum_lower>mp.mpf("0.00017")
print("OVERALL_PASS")
