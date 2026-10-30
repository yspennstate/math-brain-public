from fractions import Fraction
from collections import defaultdict
import math


def v2(a):
    a=abs(int(a))
    assert a
    k=0
    while a%2==0:
        a//=2; k+=1
    return k


def KL(P,Q):
    out=0.0
    for s,p in P.items():
        if p:
            q=Q.get(s,0.0)
            assert q>0
            out += p*math.log2(p/q)
    return out


def sparse(m):
    # F(y,x)=y(1-2 1_{x=0}); statistic is (sign,v2,old-layer).
    a=2.0**(-m); n=m+1
    A={0:2**n-4}
    for s in range(1,2**m): A[s]=-4
    P={s:(A[s]/2**n)**2 for s in A}
    j=2*a
    Q={}
    for s in range(2**m):
        k=s.bit_count()
        Q[s]=j**k*(1-j)**(m-k)
    Pz=defaultdict(float); Qz=defaultdict(float)
    for s,q in Q.items():
        aa=A.get(s,0)
        z=(0,None,s.bit_count()) if aa==0 else ((1 if aa>0 else -1),v2(aa),s.bit_count())
        Pz[z]+=P.get(s,0.0); Qz[z]+=q
    return KL(P,Q),KL(Pz,Qz)


def maj3_coeffs():
    return {1:Fraction(1,2),2:Fraction(1,2),4:Fraction(1,2),7:Fraction(-1,2)}


def recmaj(depth):
    C=maj3_coeffs(); n=3
    for _ in range(2,depth+1):
        old=C; oldn=n; C={}
        for j in range(3):
            for s,c in old.items(): C[s << (j*oldn)] = c*Fraction(1,2)
        for s1,c1 in old.items():
            for s2,c2 in old.items():
                for s3,c3 in old.items():
                    s=s1 | (s2<<oldn) | (s3<<(2*oldn))
                    C[s]=-Fraction(1,2)*c1*c2*c3
        n*=3
    return n,C


def positive_c(n,r):
    lo=1e-14; hi=1.0
    def h(c): return 1-c-(1-c*r)**n
    for _ in range(200):
        mid=(lo+hi)/2
        if h(mid)>0: lo=mid
        else: hi=mid
    return (lo+hi)/2


def majority(depth):
    n,C=recmaj(depth)
    P={s:float(c*c) for s,c in C.items()}
    r=2.0**(-depth); cpar=positive_c(n,r); t=cpar*r
    Q={}
    for s in range(1,1<<n):
        k=s.bit_count(); Q[s]=t**k*(1-t)**(n-k)/cpar
    Pz=defaultdict(float); Qz=defaultdict(float)
    for s,q in Q.items():
        cc=C.get(s,Fraction(0,1))
        if cc:
            A=cc*(2**n); assert A.denominator==1
            aa=A.numerator; z=(1 if aa>0 else -1,v2(aa),s.bit_count())
            # Pure-power Walsh integer: odd part must be one.
            assert abs(aa)//(2**v2(aa))==1
        else:
            z=(0,None,s.bit_count())
        Pz[z]+=P.get(s,0.0); Qz[z]+=q
    return KL(P,Q),KL(Pz,Qz)


for m in range(2,9):
    a,b=sparse(m); assert abs(a-b)<1e-12
for d in (1,2):
    a,b=majority(d); assert abs(a-b)<1e-12
print('PASS sparse m=2..8 and recursive majority depths 1..2: coarse signed-valuation/class-count KL equals K_occ')
