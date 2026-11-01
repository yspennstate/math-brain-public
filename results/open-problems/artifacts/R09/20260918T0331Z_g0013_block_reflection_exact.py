#!/usr/bin/env python3
"""
R09 / G0013 exact symbolic self-check for the one-interface mixed-orientation
block-reflection copula

    g_c(s) = s                    for 0 <= s <= c,
             1 + c - s            for c < s <= 1.

This script checks only the exact algebra/integrals in the explicit transport
constructed in the accompanying analytic report. It does not certify the
continuous optimal-transport theorem by itself.
"""
import sympy as sp

z,d,a,b = sp.symbols("z d a b", nonnegative=True, real=True)

# Regime I: 0 <= c <= 1/2, c=2a^2, 0<=a<=1/2.
c1 = 2*a**2
m1 = (1+c1)/2

A1 = sp.integrate(
    2*((z-2*z**2)**2 + z**2/sp.Integer(3))*4*z,
    (z,0,a)
)

Bperp1 = (
    sp.integrate(2*(z-m1)**2*4*z, (z,a,sp.Rational(1,2)))
    + sp.integrate(2*(z-m1)**2*4*(1-z), (z,sp.Rational(1,2),1))
)

w1a = 2*(1-a-d)
dp1a = 2*(1-a)*d - d**2
w1b = 2*(1-2*d)
dp1b = 2*d - 2*d**2 - a**2

Balong1 = 4*(
    sp.integrate((d-dp1a)**2*w1a, (d,0,a))
    + sp.integrate((d-dp1b)**2*w1b, (d,a,sp.Rational(1,2)))
)

C1 = sp.factor(sp.simplify(A1+Bperp1+Balong1))
gap1 = sp.factor(sp.Rational(1,10)-C1)
expected_gap1 = sp.factor(
    sp.Rational(4,15)*a**2*(13*a**3 - 5*a**2 - 10*a + 5)
)
assert sp.simplify(gap1-expected_gap1) == 0

P = 13*a**3 - 5*a**2 - 10*a + 5
assert sp.simplify(P.subs(a, sp.Rational(1,2)) - sp.Rational(3,8)) == 0
Pprime = sp.diff(P,a)
# On 0<=a<=1/2:
# 39 a^2 <= (39/2)a, hence
# P'(a)=39a^2-10a-10 <= (19/2)a-10 <= -21/4 <0.
assert sp.simplify(Pprime - (39*a**2 - 10*a - 10)) == 0
assert sp.Rational(19,2)*sp.Rational(1,2) - 10 == -sp.Rational(21,4)

# Regime II: 1/2 <= c <= 1, c=1-2b^2, 0<=b<=1/2.
c2 = 1-2*b**2
m2 = (1+c2)/2

Fleft = 2*z**2
Fright = 1-2*(1-z)**2

A2 = (
    sp.integrate(
        2*((z-Fleft)**2 + z**2/sp.Integer(3))*4*z,
        (z,0,sp.Rational(1,2))
    )
    + sp.integrate(
        2*((z-Fright)**2 + (1-z)**2/sp.Integer(3))*4*(1-z),
        (z,sp.Rational(1,2),1-b)
    )
)

Bperp2 = sp.integrate(
    2*(z-m2)**2*4*(1-z),
    (z,1-b,1)
)

w2 = 2*(b-d)
dp2 = 2*b*d-d**2
Balong2 = 4*sp.integrate((d-dp2)**2*w2, (d,0,b))

C2 = sp.factor(sp.simplify(A2+Bperp2+Balong2))
gap2 = sp.factor(sp.Rational(1,10)-C2)
assert sp.simplify(gap2 - sp.Rational(4,5)*b**5) == 0

# Matching at c=1/2 means a=b=1/2.
assert sp.simplify(C1.subs(a,sp.Rational(1,2)) - sp.Rational(3,40)) == 0
assert sp.simplify(C2.subs(b,sp.Rational(1,2)) - sp.Rational(3,40)) == 0

print("REGIME_I_A_COST =", sp.factor(A1))
print("REGIME_I_B_PERP =", sp.factor(Bperp1))
print("REGIME_I_B_ALONG =", sp.factor(Balong1))
print("REGIME_I_TOTAL =", C1)
print("REGIME_I_GAP =", gap1)
print("REGIME_I_P_HALF =", sp.factor(P.subs(a,sp.Rational(1,2))))
print("REGIME_I_DERIVATIVE_UPPER_ENDPOINT_BOUND =", -sp.Rational(21,4))
print("REGIME_II_A_COST =", sp.factor(A2))
print("REGIME_II_B_PERP =", sp.factor(Bperp2))
print("REGIME_II_B_ALONG =", sp.factor(Balong2))
print("REGIME_II_TOTAL =", C2)
print("REGIME_II_GAP =", gap2)
print("MIDPOINT_COST =", sp.Rational(3,40))
print("SELF_CHECK_ONLY / PASS")
