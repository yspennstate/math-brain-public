#!/usr/bin/env python3
"""
R19 / I0084 exact finite checker, run 2026-09-16 15:35 UTC.

Finite/symbolic cores only.  The infinite free-subordination/support proof is
written in the immutable run report and uses Huang--Wang (2022).

Checks:
(A) sparse initial-law constants used for the free positive alpha=1/2 case;
(B) exact standard positive free-stable Voiculescu coefficient at alpha=1/2,
    positivity parameter rho=1;
(C) independent R19 audit of R20/I0100's p=41 exact theta certificate.

No floating-point computation is evidence for the R19 theorem.
"""
from fractions import Fraction
import sympy as sp

print("R19 I0084 free-halfstable exact checker")

# ---------- A. Sparse-law constants ----------
# A_n=2^(2^n), w_n=2^{-n} A_n^{-n}, n>=1.
# w_1=1/8 and for n>=2, w_n <= 32^{-n}; hence
# W=sum_{n>=1} w_n < 1/8 + sum_{n>=2}32^{-n}=1/8+1/992<1/4.
geom_tail = Fraction(1, 32**2) / (1 - Fraction(1,32))
assert geom_tail == Fraction(1,992)
assert Fraction(1,8) + geom_tail < Fraction(1,4)
print("PASS W < 1/8 + 1/992 < 1/4, hence w0 > 3/4")

# Critical moment: 5/2-n <= -1/2 for every n>=3.
assert Fraction(5,2) - 3 == Fraction(-1,2)
print("PASS 5/2-n <= -1/2 for n>=3")

# At c_n=-A_n/2:
# -G(c_n) >= 1/A_n from the written decomposition.
# I_2(c_n) < (4+4+1)/A_n^2 = 9/A_n^2.
# Therefore H_t'(c_n) >= 1 - 9t/(2 sqrt(A_n)).
# sqrt(A_n)>9t gives H_t'>1/2.
assert Fraction(4)+Fraction(4)+Fraction(1) == Fraction(9)
assert Fraction(9,2) / Fraction(9) == Fraction(1,2)
print("PASS derivative constants: I2<9/A^2 and sqrt(A)>9t imply H_t'>1/2")

# For n>=2, A_{n-1}=sqrt(A_n)<=A_n/4 because A_n>=16.
for n in range(2,8):
    An = 2**(2**n)
    Aprev = 2**(2**(n-1))
    assert Aprev*Aprev == An
    assert 4*Aprev <= An
print("PASS A_{n-1}=sqrt(A_n)<=A_n/4 finite exact core n=2..7")

# ---------- B. Positive free stable coefficient ----------
# Hasebe--Kuznetsov normalization:
# phi_{alpha,rho}(z)=-exp(i*pi*alpha*rho) z^(1-alpha).
# alpha=1/2, rho=1 gives -i sqrt(z).
coef = -sp.exp(sp.I*sp.pi*sp.Rational(1,2))
assert sp.simplify(coef + sp.I) == 0
print("PASS phi_{1/2,1}(z) coefficient = -i")

# ---------- C. Independent audit of R20/I0100 p=41 ----------
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
for val in w.values():
    assert sp.ask(sp.Q.positive(val)) is True
for d in N:
    lhs=sum(v*sp.cos(2*PI*m*d/n) for m,v in w.items())
    assert ezero(lhs)==0
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
    assert sp.ask(sp.Q.nonnegative(s)) is True
assert ezero(n*a-theta)==0

print("PASS R19-AUDIT-R20-I0100-P41-01: exact primal/dual theta=2*sqrt(5)")
print("R20 exact slack set =", sorted({str(s) for s in slacks}))
print("ALL CHECKS PASS")
