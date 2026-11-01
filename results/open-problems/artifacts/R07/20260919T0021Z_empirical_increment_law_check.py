#!/usr/bin/env python3
"""
R07 run 56 exact self-check.
Standard library only. Every assertion is exact over Q(sqrt(2)).
"""
from fractions import Fraction as F
from dataclasses import dataclass

@dataclass(frozen=True)
class Q2:
    a: F = F(0)  # a + b*sqrt(2)
    b: F = F(0)
    def __add__(self,o):
        o=toQ2(o); return Q2(self.a+o.a,self.b+o.b)
    __radd__=__add__
    def __neg__(self): return Q2(-self.a,-self.b)
    def __sub__(self,o): return self+(-toQ2(o))
    def __rsub__(self,o): return toQ2(o)-self
    def __mul__(self,o):
        o=toQ2(o)
        return Q2(self.a*o.a+2*self.b*o.b,self.a*o.b+self.b*o.a)
    __rmul__=__mul__
    def __truediv__(self,o):
        o=toQ2(o)
        den=o.a*o.a-2*o.b*o.b
        assert den != 0
        return Q2((self.a*o.a-2*self.b*o.b)/den,
                  (self.b*o.a-self.a*o.b)/den)
    def sign(self):
        a,b=self.a,self.b
        if b==0: return (a>0)-(a<0)
        if a==0: return (b>0)-(b<0)
        if a>0 and b>0: return 1
        if a<0 and b<0: return -1
        # Compare |a| with |b|*sqrt(2) exactly by squaring.
        cmp = a*a - 2*b*b
        if cmp==0: return 0
        if a>0 and b<0:
            return 1 if cmp>0 else -1
        # a<0,b>0
        return 1 if cmp<0 else -1
    def __str__(self):
        return f"({self.a}) + ({self.b})*sqrt(2)"

def toQ2(x):
    if isinstance(x,Q2): return x
    return Q2(F(x),F(0))

SQ2=Q2(F(0),F(1))
ZERO=Q2()

# polynomials low-to-high in q
def trim(p):
    p=list(p)
    while len(p)>1 and p[-1]==ZERO: p.pop()
    return p
def padd(p,r):
    n=max(len(p),len(r)); out=[ZERO]*n
    for i in range(n):
        out[i]=(p[i] if i<len(p) else ZERO)+(r[i] if i<len(r) else ZERO)
    return trim(out)
def pneg(p): return [-c for c in p]
def psub(p,r): return padd(p,pneg(r))
def pmul(p,r):
    out=[ZERO]*(len(p)+len(r)-1)
    for i,a in enumerate(p):
        for j,b in enumerate(r):
            out[i+j]=out[i+j]+a*b
    return trim(out)
def pscale(p,c): return [x*c for x in p]
def peval(p,x):
    x=toQ2(x); y=ZERO
    for c in reversed(p): y=y*x+c
    return y
def pder(p):
    return [p[i]*i for i in range(1,len(p))] or [ZERO]

q=[ZERO,toQ2(1)]
one=[toQ2(1)]

# E(q)=0 is exactly the fourth-moment matching equation.
E=[
    -6 + 3*SQ2,
    45 - 6*SQ2,
    -74 - 2*SQ2,
    toQ2(18),
]

q0=F(12,25)
q1=F(49,100)
assert peval(E,q0).sign() > 0
assert peval(E,q1).sign() < 0

# Strict decrease on bracket. E' is quadratic; E''=108q-148-4sqrt(2)<0
# there, so E' decreases. It is already negative at q0.
Ep=pder(E)
Epp=pder(Ep)
assert peval(Ep,q0).sign() < 0
assert peval(Epp,q0).sign() < 0
assert peval(Epp,q1).sign() < 0

# Build the fourth-moment equation from the stationary affine-IFS recursion.
# a+b=sqrt(2), ab=q, c^2=q.
# A = 1-E[A^4] = -1+4q-q^2.
A=psub(padd(pscale(q,4),[-toQ2(1)]),pmul(q,q))
# D = 1-E[A^3] = 1-sqrt(2)+(3sqrt(2)/2)q.
D=[toQ2(1)-SQ2, F(3,2)*SQ2]
# term1 = 6q(2-4q)(2-q)
term1=pscale(pmul(pmul(q,[toQ2(2),toQ2(-4)]),[toQ2(2),toQ2(-1)]),6)
# bracket = (6q-5q^2)-3A
bracket=psub(padd(pscale(q,6),pscale(pmul(q,q),-5)),pscale(A,3))
# fourth-moment condition after multiplying by sqrt(2)D:
# term1 + sqrt(2)D*bracket = 0.
derived=padd(term1,pmul(pscale(D,SQ2),bracket))
assert trim(derived)==trim(E)

# Variance recursion: m2=(1-q)m2+q => m2=1 exactly.
# Check the identity algebraically as polynomials.
lhs_var=psub(one,padd([toQ2(1)],pscale(q,-1)))  # 1-(1-q)=q
assert trim(lhs_var)==trim(q)

# Denominators are nonzero/positive on bracket:
# A=-1+4q-q^2 is increasing for q<2 and A(q0)>0.
assert peval(A,q0).sign() > 0
# D is increasing, D(q0)>0.
assert peval(D,q0).sign() > 0

# Contraction. q0 > sqrt(2)-1; for roots of z^2-sqrt(2)z+q,
# this implies the larger root b<1. q>0 gives both roots positive.
assert (toQ2(q0) - (SQ2-1)).sign() > 0

print("R07 RUN 56 EXACT SELF-CHECK")
print("E(12/25) =", peval(E,q0), "> 0")
print("E(49/100) =", peval(E,q1), "< 0")
print("E'(12/25) =", peval(Ep,q0), "< 0")
print("E''(49/100) =", peval(Epp,q1), "< 0")
print("derived fourth-moment polynomial equals E(q): PASS")
print("stationary variance identity m2=1: PASS")
print("root bracket unique by IVT + strict decrease: PASS")
print("stationary recursion denominators positive on bracket: PASS")
print("affine branches contract on root bracket: PASS")
print("ALL_EXACT_CHECKS_PASS")
