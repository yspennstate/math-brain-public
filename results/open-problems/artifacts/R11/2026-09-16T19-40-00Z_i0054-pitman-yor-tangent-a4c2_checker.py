#!/usr/bin/env python3
from fractions import Fraction
from dataclasses import dataclass
from math import factorial, comb

print("R11 I0054 positive-discount Pitman-Yor tangent exact self-check")
print("FINITE CLAIMS ONLY; asymptotic convergence is proved in the written report, not by this checker.")

def rising(x,n):
    out=Fraction(1)
    for j in range(n):
        out*=x+j
    return out

def eppf(alpha,theta,sizes):
    m=sum(sizes); r=len(sizes)
    num=Fraction(1)
    for j in range(1,r):
        num*=theta+j*alpha
    den=rising(theta+1,m-1)
    prod=Fraction(1)
    for n in sizes:
        prod*=rising(1-alpha,n-1)
    return num*prod/den

def set_partitions(seq):
    if not seq:
        yield ()
        return
    first=seq[0]
    for rest in set_partitions(seq[1:]):
        yield ((first,),)+rest
        for i in range(len(rest)):
            nr=list(rest)
            nr[i]=(first,)+nr[i]
            yield tuple(nr)

def sizes(part):
    return tuple(len(b) for b in part)

params=[
    (Fraction(1,8),Fraction(1,8)),
    (Fraction(1,10),Fraction(1,5)),
    (Fraction(1,7),Fraction(0)),
    (Fraction(0),Fraction(1,4)),
]
norm_instances=0
for n in range(1,8):
    parts=list(set_partitions(tuple(range(n))))
    for alpha,theta in params:
        total=sum((eppf(alpha,theta,sizes(p)) for p in parts), Fraction(0))
        assert total==1, (n,alpha,theta,total)
        norm_instances += len(parts)
print("EPPF_normalization: PASS", norm_instances, "exact labelled-partition instances")

@dataclass(frozen=True)
class Dual:
    a: Fraction
    b: Fraction
    def _d(self,o):
        return o if isinstance(o,Dual) else Dual(Fraction(o),Fraction(0))
    def __add__(self,o):
        o=self._d(o); return Dual(self.a+o.a,self.b+o.b)
    __radd__=__add__
    def __neg__(self): return Dual(-self.a,-self.b)
    def __sub__(self,o): return self+(-self._d(o))
    def __rsub__(self,o): return self._d(o)-self
    def __mul__(self,o):
        o=self._d(o)
        return Dual(self.a*o.a,self.a*o.b+self.b*o.a)
    __rmul__=__mul__
    def __truediv__(self,o):
        o=self._d(o)
        assert o.a != 0
        return Dual(self.a/o.a,(self.b*o.a-self.a*o.b)/(o.a*o.a))
    def __rtruediv__(self,o): return self._d(o)/self

def rising_dual(x,n):
    out=Dual(Fraction(1),Fraction(0))
    for j in range(n):
        out*=x+j
    return out

def eppf_direction(c,sizes_):
    # alpha=c*t, theta=(1-c)*t, so delta=alpha+theta=t.
    t=Dual(Fraction(0),Fraction(1))
    alpha=c*t
    theta=(1-c)*t
    m=sum(sizes_); r=len(sizes_)
    num=Dual(Fraction(1),Fraction(0))
    for j in range(1,r):
        num*=theta+j*alpha
    den=rising_dual(theta+1,m-1)
    prod=Dual(Fraction(1),Fraction(0))
    for n in sizes_:
        prod*=rising_dual(1-alpha,n-1)
    return num*prod/den

def H(n):
    return sum((Fraction(1,j) for j in range(1,n+1)),Fraction(0))

def BetaInt(i,j):
    return Fraction(factorial(i-1)*factorial(j-1),factorial(i+j-1))

tangent_instances=0
for c in [Fraction(0),Fraction(1,4),Fraction(1,2),Fraction(3,4),Fraction(1)]:
    for m in range(2,13):
        d=eppf_direction(c,(m,))
        assert d.a==1 and d.b==-H(m-1), (c,m,d)
        tangent_instances+=1
        for i in range(1,m):
            d=eppf_direction(c,(i,m-i))
            assert d.a==0 and d.b==BetaInt(i,m-i), (c,m,i,d)
            tangent_instances+=1
        for i in range(1,m-1):
            for j in range(1,m-i):
                k=m-i-j
                if k>=1:
                    d=eppf_direction(c,(i,j,k))
                    assert d.a==0 and d.b==0, (c,m,i,j,k,d)
                    tangent_instances+=1
print("universal_first_order_CTCS_tangent: PASS", tangent_instances, "exact directional identities")

harmonic_instances=0
for m in range(2,31):
    total=sum(Fraction(comb(m,i),2)*BetaInt(i,m-i) for i in range(1,m))
    assert total==H(m-1),(m,total,H(m-1))
    harmonic_instances+=1
print("CTCS_total_rate_identity: PASS", harmonic_instances, "values")

# Concrete positive-discount model alpha_N=theta_N=1/(2N), at N=4.
a=t=Fraction(1,8)
p_four=eppf(a,t,(1,1,1,1))
assert p_four==Fraction(8,1275)
ratio_py=eppf(a,t,(1,3))/eppf(a,t,(2,2))
assert ratio_py==Fraction(15,7)

# SC-nCRP comparison at N=4: alpha=0, theta=1/4.
ratio_ewens=eppf(Fraction(0),Fraction(1,4),(1,3))/eppf(Fraction(0),Fraction(1,4),(2,2))
assert ratio_ewens==2

print("finite_non_equivalence_witnesses: PASS")
print("  PY_N4_four_singletons =", p_four)
print("  PY_N4_particular_rate_ratio_1|3_over_2|2 =", ratio_py)
print("  Ewens_N4_particular_rate_ratio_1|3_over_2|2 =", ratio_ewens)
print("  q=3_Dirichlet_model_four_way_probability = 0 (structural: at most 3 children)")

print("ALL_EXACT_CHECKS_PASS")
