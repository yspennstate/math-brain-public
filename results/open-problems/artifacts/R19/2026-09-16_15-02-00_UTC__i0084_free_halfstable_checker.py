#!/usr/bin/env python3
"""
R19 / I0084 run 2 exact finite checker.
Finite arithmetic only. The theorem proof is in the immutable run report.

Checks:
(1) constants used in the free positive half-stable disconnected-support proof;
(2) exact moment/tail arithmetic templates at the smallest A=256;
(3) independent exact audit of R20 I0100 p=41 certificate.

No numerical experiment is used as evidence for the universal theorem.
"""
from fractions import Fraction
import sympy as sp

# ---------- R19 finite constants ----------
A = 256

# w0 >= 3/4: sum_{k>=0} A^{-3(k+1)} = A^-3/(1-A^-3) < 1/4.
geom = Fraction(1, A**3) / (1 - Fraction(1, A**3))
assert geom < Fraction(1,4)

# Gap point r=-A_n/2:
# negative core 3/(10A), positive left-tail <= 1/(20A), net >=1/(4A).
assert Fraction(3,10) - Fraction(1,20) == Fraction(1,4)
assert 80 <= A**3  # 4 A^-4 <= (20 A)^-1

# For y>=A: core imaginary Cauchy part >=3/(5y).
assert Fraction(3,4)*Fraction(4,5) == Fraction(3,5)

# Remote atom r=-A_n:
# core real magnitude >=3/(8A), farther-left positive part <=1/(24A).
assert Fraction(3,8) - Fraction(1,24) == Fraction(1,3)
assert 48 <= A**7  # 2 A^-8 <= (24 A)^-1

# I0 <=6/A^2 and a>=1/(3A) yield
# v <= 9 sqrt(3)/A < 16/A; exact square comparison.
assert 243 < 256  # (9 sqrt 3)^2 < 16^2

# sqrt(A)>64t implies 2t sqrt(A)<A/32 and 16t/A<A^-1/2/4.
assert Fraction(2,64) == Fraction(1,32)
assert Fraction(16,64) == Fraction(1,4)

# Moment summability template at p=5/2.
assert Fraction(5,2) - 3 == Fraction(-1,2)

print("R19-C002/C003 finite constant checks: PASS")
print("geom_tail_bound_at_A256 =", geom)
print("gap_net_constant =", Fraction(1,4))
print("remote_net_constant =", Fraction(1,3))
print("9sqrt3<16 certified by 243<256")

# ---------- R20 independent p=41 audit ----------
PI=sp.pi
SQ5=sp.sqrt(5)
sA=sp.sqrt(10+2*SQ5)
sB=sp.sqrt(50+10*SQ5)
w1= -sA/16 - SQ5/20 + sB/80 + sp.Rational(1,4)
w9= -SQ5/20 - sB/80 + sA/16 + sp.Rational(1,4)
w={
    0:SQ5/10,
    1:w1,
    4:SQ5/40+sp.Rational(1,8),
    5:SQ5/10,
    6:sp.Rational(3,8)-SQ5/8,
    9:w9,
}
N=[1,2,3,6,8]
n=20

def ezero(expr):
    return sp.simplify(sp.radsimp(sp.expand_trig(sp.trigsimp(expr, method='fu'))))

assert ezero(sum(w.values())-1)==0
assert sp.ask(sp.Q.positive(SQ5/10))
assert sp.ask(sp.Q.positive(SQ5/40+sp.Rational(1,8)))
assert sp.ask(sp.Q.positive(sp.Rational(3,8)-SQ5/8))
assert sp.ask(sp.Q.positive(w1)) is True
assert sp.ask(sp.Q.positive(w9)) is True

for d in N:
    lhs=sum(v*sp.cos(2*PI*m*d/n) for m,v in w.items())
    assert ezero(lhs)==0, (d, ezero(lhs))

theta=2*SQ5
assert ezero(n*w[0]-theta)==0

a=SQ5/10
lam={2:(5-SQ5)/20, 6:(5+SQ5)/20, 8:(5-SQ5)/10}
slacks=[]
for m in range(n):
    lhs=a+sum(v*sp.cos(2*PI*m*d/n) for d,v in lam.items())
    rhs=1 if m==0 else 0
    s=ezero(lhs-rhs)
    slacks.append(s)
    assert sp.ask(sp.Q.nonnegative(s)) is True, (m,s)
assert ezero(n*a-theta)==0

print("R19-AUDIT-R20-I0100-C02-P41: PASS")
print("R20 p=41 reduced complement classes =",N)
print("R20 p=41 theta_exact =",theta)
print("R20 p=41 unique exact dual slacks =",sorted({str(s) for s in slacks}))
print("PASS")
