#!/usr/bin/env python3
"""
R19 2026-09-16 I0110 exact self-check + independent R20 algebraic audit.

SELF-CHECK SCOPE ONLY.
Part A checks, with exact Fraction arithmetic on a finite rational atlas, the
algebra behind R19-I0110-C004:
  * likelihood-ratio lower/upper TV inequalities;
  * weighted-collision = 1 + chi^2 identity;
  * 4 TV^2 <= chi^2.
The report contains the general proof; finite enumeration is not that proof.

Part B independently re-derives the finite arithmetic underlying the new R20
Jacobi/autocorrelation route for every prime p == 1 mod 4 up to 421:
  * C(0)=p-2, C(r)=0 for odd r and -2 for nonzero even r;
  * even/odd decimation sums -1 and 0;
  * the algebraic minimizer u=1+sqrt(p) solves u^2-2u-2n=0;
  * B_n(1+sqrt(p))=sqrt(p)-1 exactly in Q(sqrt(p)).
This does not audit R20's asymptotic conjecture or floating-point probes.
"""

from fractions import Fraction
from itertools import product

def tv(p, pi):
    return sum(abs(x-y) for x,y in zip(p,pi)) / 2

def chi2(p, pi):
    return sum((x-y)*(x-y)/y for x,y in zip(p,pi))

def atlas_distributions(den=8, k=3):
    out=[]
    for a in range(1, den):
        for b in range(1, den-a):
            c=den-a-b
            if c >= 1:
                out.append(tuple(Fraction(x,den) for x in (a,b,c)))
    return out

def check_information_ratio_atlas():
    ds=atlas_distributions()
    thresholds=[Fraction(3,2), Fraction(2,1), Fraction(3,1)]
    deltas=[Fraction(1,8), Fraction(1,4), Fraction(1,2)]
    count=0
    for p in ds:
        for pi in ds:
            ratios=[x/y for x,y in zip(p,pi)]
            T=tv(p,pi)
            X=chi2(p,pi)
            collision=sum(x*x/y for x,y in zip(p,pi))
            assert collision == 1 + X
            assert 4*T*T <= X
            for A in thresholds:
                heavy=sum(x for x,r in zip(p,ratios) if r >= A)
                assert T >= heavy - Fraction(1,1)/A
                count += 1
            for d in deltas:
                bad=sum(x for x,r in zip(p,ratios) if r > 1+d)
                assert T <= bad + d
                count += 1
    return len(ds), count

def is_prime(n):
    if n < 2: return False
    if n % 2 == 0: return n == 2
    d=3
    while d*d <= n:
        if n%d==0: return False
        d += 2
    return True

def legendre(a,p):
    a %= p
    if a == 0: return 0
    z=pow(a,(p-1)//2,p)
    return 1 if z==1 else -1

def factorize(n):
    fs=[]
    d=2
    while d*d<=n:
        if n%d==0:
            fs.append(d)
            while n%d==0: n//=d
        d+=1
    if n>1: fs.append(n)
    return fs

def primitive_root(p):
    fs=factorize(p-1)
    for g in range(2,p):
        if all(pow(g,(p-1)//q,p)!=1 for q in fs):
            return g
    raise RuntimeError("no primitive root")

class Qsqrt:
    def __init__(self,a,b,p):
        self.a=Fraction(a); self.b=Fraction(b); self.p=p
    def __add__(self,o): return Qsqrt(self.a+o.a,self.b+o.b,self.p)
    def __sub__(self,o): return Qsqrt(self.a-o.a,self.b-o.b,self.p)
    def __mul__(self,o):
        return Qsqrt(self.a*o.a+self.b*o.b*self.p,
                     self.a*o.b+self.b*o.a,self.p)
    def scale(self,c): return Qsqrt(self.a*c,self.b*c,self.p)
    def __eq__(self,o): return self.p==o.p and self.a==o.a and self.b==o.b
    def __repr__(self): return f"{self.a}+({self.b})sqrt({self.p})"

def check_r20_jacobi():
    primes=[]
    shifts=0
    for p in range(5,422):
        if p%4!=1 or not is_prime(p):
            continue
        primes.append(p)
        g=primitive_root(p)
        L=p-1
        a=[legendre(1-pow(g,j,p),p) for j in range(L)]
        assert sum(x*x for x in a)==p-2
        for r in range(L):
            C=sum(a[j]*a[(j+r)%L] for j in range(L))
            target=p-2 if r==0 else (0 if r%2 else -2)
            assert C==target, (p,r,C,target)
            shifts += 1
        n=L//2
        assert sum(a[2*d] for d in range(n)) == -1
        assert sum(a[2*d+1] for d in range(n)) == 0
        one=Qsqrt(1,0,p)
        s=Qsqrt(0,1,p)
        u=one+s
        nn=Fraction(p-1,2)
        assert u*u - u.scale(2) - Qsqrt(2*nn,0,p) == Qsqrt(0,0,p)
        lhs=(Qsqrt(2*nn,0,p)+u*u).scale(nn)
        rhs=(s-one)*u*(Qsqrt(2*nn,0,p)+u)
        assert lhs==rhs, (p,lhs,rhs)
    return primes, shifts

def group_elements(moduli):
    return list(product(*[range(m) for m in moduli]))

def add_scaled(acc, d, z, moduli):
    return tuple((a + d*b) % m for a,b,m in zip(acc,z,moduli))

def elem_order(x, moduli):
    from math import gcd
    o=1
    for a,m in zip(x,moduli):
        oi=1 if a==0 else m//gcd(a,m)
        o=o*oi//gcd(o,oi)
    return o

def check_abelian_random_homomorphism_collision():
    """Exact finite check of R19-I0110-C005."""
    tests=[((2,),2),((3,),2),((4,),3),((2,2),2),((2,4),2)]
    oneD={-1:Fraction(1,4),0:Fraction(1,2),1:Fraction(1,4)}
    count=0
    for moduli,k in tests:
        G=group_elements(moduli)
        N=len(G)
        zero=tuple(0 for _ in moduli)
        lhs=Fraction(0)
        for Zs in product(G, repeat=k):
            for ds in product(oneD.keys(), repeat=k):
                pd=Fraction(1)
                acc=zero
                for d,z in zip(ds,Zs):
                    pd *= oneD[d]
                    acc=add_scaled(acc,d,z,moduli)
                if acc==zero:
                    lhs += Fraction(N, len(G)**k) * pd
        rhs=Fraction(0)
        for x in G:
            m=elem_order(x,moduli)
            rm=sum(prob for d,prob in oneD.items() if d % m == 0)
            rhs += rm**k
        assert lhs==rhs, (moduli,k,lhs,rhs)
        count += 1
    return count

if __name__=="__main__":
    nd, nchecks=check_information_ratio_atlas()
    abtests=check_abelian_random_homomorphism_collision()
    primes, shifts=check_r20_jacobi()
    print(f"I0110 exact rational atlas: distributions={nd}, inequality_checks={nchecks}, PASS")
    print(f"I0110 Abelian random-homomorphism collision tests={abtests}, PASS")
    print(f"R20 independent Jacobi audit: primes={primes}")
    print(f"R20 cyclic shifts checked={shifts}, PASS")
    print("ALL_EXACT_CHECKS_PASS")
