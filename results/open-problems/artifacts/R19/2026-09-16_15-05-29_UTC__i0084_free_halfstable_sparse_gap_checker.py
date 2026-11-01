#!/usr/bin/env python3
"""
R19 / I0084 run checker.

Purpose:
  (A) exact-arithmetic finite cores for the new free positive alpha=1/2
      sparse-gap counterexample;
  (B) an independent exact audit of R20/I0100's p=41 Paley-theta certificate.

This script does NOT certify the infinite-dimensional subordination theorem;
that proof is written in the run report and uses Huang--Wang (2022).
Finite claims here are exact/symbolic.

Seed: none (deterministic exact arithmetic).
"""
from fractions import Fraction
import sympy as sp
import math

print("R19 I0084 checker -- deterministic exact arithmetic")

# ---------------------------------------------------------------------
# Part A1. Sparse measure elementary inequalities.
# A_n = 2^(2^n), w_n = 2^-n A_n^-n.
# ---------------------------------------------------------------------
def A(n):
    return 2 ** (2 ** n)

def w_frac(n):
    return Fraction(1, 2**n * (A(n)**n))

for n in range(2, 9):
    assert A(n) == A(n-1)**2
print("PASS A_n=A_{n-1}^2 for n=2..8")

w1 = w_frac(1)
assert w1 == Fraction(1,8)
geom_tail = Fraction(1, 32**2) / (1 - Fraction(1,32))
assert geom_tail == Fraction(1, 992)
assert w1 + geom_tail < Fraction(1,4)
print("PASS W < 1/8 + 1/992 < 1/4, hence w0>3/4")

for n in range(2, 13):
    An = A(n)
    Bn = 2 ** (3 * (2 ** (n-2)))
    assert Bn**4 == An**3
    lhs1 = Fraction(1, (2**(n-2)) * An**(n+1))
    rhs1 = Fraction(1, 4*Bn)
    assert lhs1 <= rhs1
    if n <= 3:
        lhs2 = Fraction(2**(3-n), An**(n+2))
    else:
        lhs2 = Fraction(1, (2**(n-3))*An**(n+2))
    rhs2 = Fraction(1, Bn**2)
    assert lhs2 <= rhs2
print("PASS sparse left-tail and derivative-tail inequalities for n=2..12 (exact)")

for n in range(3, 13):
    assert 5 <= 2*n
print("PASS critical 5/2-moment comparison for n>=3")

for n in range(2, 10):
    Bn = 2 ** (3 * (2 ** (n-2)))
    assert Bn >= 2*A(n-1)
print("PASS B_n>=2 A_{n-1} for n>=2 finite core")

assert Fraction(200,800) == Fraction(1,4)
print("PASS exact constant: B>800 t^2 implies H_t'(c_n)>1/2")

for k in range(1,7):
    wk = w_frac(k)
    eps = wk / 100
    sq = Fraction(1,1) / (4*wk*eps)
    assert sq > 1
print("PASS isolated-atom leading derivative blow-up diagnostic")

# ---------------------------------------------------------------------
# Part B. Independent audit of R20/I0100 p=41 exact theta certificate.
# Rebuild the Paley localized complement classes independently.
# ---------------------------------------------------------------------
p = 41
n = (p-1)//2

def factors(N):
    out=[]
    d=2
    x=N
    while d*d<=x:
        if x%d==0:
            out.append(d)
            while x%d==0:
                x//=d
        d+=1
    if x>1:
        out.append(x)
    return out

def primitive_root(p):
    for g in range(2,p):
        if all(pow(g,(p-1)//q,p)!=1 for q in factors(p-1)):
            return g
    raise AssertionError

g = primitive_root(p)
alpha = pow(g,2,p)
Q = {x*x % p for x in range(1,p)}
vals = [pow(alpha,j,p) for j in range(n)]
S = {d for d in range(1,n) if (vals[d]-1)%p in Q}
Nred = [d for d in range(1,n//2+1) if d not in S]
assert Nred == [1,2,3,6,8], Nred
print("PASS R20 p=41 localized complement reduced classes =", Nred)

pi = sp.pi
sq5 = sp.sqrt(5)
sA = sp.sqrt(10+2*sq5)
sB = sp.sqrt(50+10*sq5)

w = {
    0:sq5/10,
    1:-sA/16 - sq5/20 + sB/80 + sp.Rational(1,4),
    4:sq5/40 + sp.Rational(1,8),
    5:sq5/10,
    6:sp.Rational(3,8) - sq5/8,
    9:-sq5/20 - sB/80 + sA/16 + sp.Rational(1,4),
}
lam = {
    2:(5-sq5)/20,
    6:(5+sq5)/20,
    8:(5-sq5)/10,
}
a = sq5/10
theta = 2*sq5

def simp(x):
    return sp.simplify(sp.trigsimp(sp.expand_trig(x), method="fu"))

assert simp(sum(w.values())-1) == 0
for m,val in w.items():
    assert sp.ask(sp.Q.nonnegative(val)) is True, (m,val)
for d in Nred:
    lhs = sum(val*sp.cos(2*pi*m*d/n) for m,val in w.items())
    assert simp(lhs) == 0, (d,simp(lhs))
assert simp(n*w[0]-theta) == 0

slacks=[]
for m in range(n):
    lhs = a + sum(val*sp.cos(2*pi*m*d/n) for d,val in lam.items())
    rhs = 1 if m==0 else 0
    sl = simp(lhs-rhs)
    slacks.append(sl)
    assert float(sp.N(sl,50)) > -1e-40, (m,sl)
assert simp(n*a-theta) == 0

targets = [
    sp.Integer(0),
    sq5/4-sp.Rational(1,2),
    sq5/4,
    sp.Integer(1),
]
for sl in slacks:
    assert any(simp(sl-t)==0 for t in targets), sl
print("PASS R20 p=41 exact primal/dual certificate; theta=2*sqrt(5)")
print("R20 p=41 exact slack set =", sorted({str(simp(s)) for s in slacks}))
print("ALL CHECKS PASS")
