#!/usr/bin/env python3
"""
PROB20-19 reproducibility checker:
exact balanced p=4,d=2 negative-spike score, Hessian, and first bifurcation bracket.

This script is a self-review aid. It uses exact SymPy algebra where possible and
mpmath interval arithmetic for the two transcendental sign enclosures.
"""
import sympy as sp
import mpmath as mp

s = sp.symbols("s", positive=True)
pi = sp.pi
r = sp.sqrt(1 + 2*s**2)
A = sp.atan(s/r)
B = sp.atan(1/(sp.sqrt(3)*s))

g = sp.Rational(12,1)/pi**2 * (B/sp.sqrt(3) + r*A)
g1_claim = sp.Rational(24,1)*s/(pi**2*r)*A
g2_claim = sp.Rational(24,1)/pi**2 * (
    A/r**3 + s/(r**2*(1+3*s**2))
)

print("g' identity residual:", sp.simplify(sp.diff(g,s)-g1_claim))
print("g'' identity residual:", sp.simplify(sp.diff(g,s,2)-g2_claim))

Q = sp.simplify(-g + 2*sp.diff(g,s)/s - (1-s**2)*sp.diff(g,s,2)/2)
qhat = sp.simplify(pi**2*Q/12)
qhat_claim = sp.simplify(
    (-4*s**4+5*s**2+2)*A/r**3
    - B/sp.sqrt(3)
    - (1-s**2)*s/(r**2*(1+3*s**2))
)
print("qhat identity residual:", sp.simplify(qhat-qhat_claim))

T = sp.simplify(
    s*(36*s**8+141*s**6+91*s**4+19*s**2+1)*A
    + r*(3*s**6-25*s**4-13*s**2-1)
)
qhat_prime_claim = sp.simplify(
    -2*T/(r**5*(1+3*s**2)**2)
)
print("qhat' identity residual:", sp.simplify(sp.diff(qhat,s)-qhat_prime_claim))

P0 = 36*s**10+147*s**8+44*s**6-32*s**4-14*s**2-1
u = sp.Rational(13,50)  # 0.26
bound = sp.simplify(u*(36*u**2+147*u+44))
print("exact positive-part coefficient bound:", bound, "< 32 =", bool(bound < 32))

q0 = sp.simplify(sp.limit(qhat, s, 0, dir="+"))
R1 = sp.simplify(sp.limit(qhat/(1-s**2), s, 1, dir="-"))
Delta42 = sp.simplify(32*R1/pi**2)
print("qhat(0+):", q0)
print("lim qhat/(1-s^2) at 1-:", R1)
print("Delta_4,2 exact:", Delta42)
print("Delta_4,2 numeric:", sp.N(Delta42, 30))

mp.iv.dps = 80
iv = mp.iv

def iatan(x):
    return iv.atan2(x, iv.mpf([1,1]))

def qhat_iv(txt):
    x = iv.mpf([txt,txt])
    rr = iv.sqrt(1+2*x*x)
    AA = iatan(x/rr)
    BB = iatan(1/(iv.sqrt(3)*x))
    return ((-4*x**4+5*x**2+2)*AA/rr**3
            - BB/iv.sqrt(3)
            - (1-x**2)*x/(rr**2*(1+3*x**2)))

lo = qhat_iv("0.50461")
hi = qhat_iv("0.50462")
print("qhat(0.50461) interval:", lo)
print("qhat(0.50462) interval:", hi)

mp.mp.dps = 60
def qhat_num(x):
    rr = mp.sqrt(1+2*x*x)
    AA = mp.atan(x/rr)
    BB = mp.atan(1/(mp.sqrt(3)*x))
    return ((-4*x**4+5*x**2+2)*AA/rr**3
            - BB/mp.sqrt(3)
            - (1-x**2)*x/(rr**2*(1+3*x**2)))

root = mp.findroot(qhat_num, (mp.mpf("0.50461"), mp.mpf("0.50462")))
print("locator s*:", root)
print("locator lambda*:", root**2)
print("lambda bracket lower:", mp.mpf("0.50461")**2)
print("lambda bracket upper:", mp.mpf("0.50462")**2)
