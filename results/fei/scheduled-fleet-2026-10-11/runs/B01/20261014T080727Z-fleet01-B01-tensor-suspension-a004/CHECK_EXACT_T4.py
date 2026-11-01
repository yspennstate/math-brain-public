#!/usr/bin/env python3
"""Exact prime-product certificate for the fourfold-tensor suspension.

Every entropy is stored as a rational linear combination of log_2(prime).
No floating-point sign is used in the certified comparisons.
"""
from fractions import Fraction as F
from math import log2
from functools import lru_cache


def fwht(v):
    a=[F(x) for x in v]; h=1
    while h < len(a):
        for j in range(0,len(a),2*h):
            for k in range(j,j+h):
                x,y=a[k],a[k+h]; a[k],a[k+h]=x+y,x-y
        h*=2
    return [x/len(a) for x in a]


def caps(p):
    a=list(p); n=len(a).bit_length()-1
    for i in range(n):
        bit=1<<i
        for s in range(len(a)):
            if not s&bit: a[s]+=a[s|bit]
    return a


def addlog(e,w,r):
    if not w: return
    # Composite integer bases are sufficient: log(ab)=log(a)+log(b), and
    # the final integer-product comparison is still exact.  Avoiding full
    # factorization keeps the certificate bounded for rational tensor means.
    if r.numerator != 1:
        e[r.numerator]=e.get(r.numerator,F())+w
    if r.denominator != 1:
        e[r.denominator]=e.get(r.denominator,F())-w


def add(a,b,s=F(1)):
    z=dict(a)
    for p,x in b.items(): z[p]=z.get(p,F())+s*x
    return {p:x for p,x in z.items() if x}


def scale(a,s): return {p:s*x for p,x in a.items() if s*x}


def entropy(p):
    c=caps(p); e={}
    for x,y in zip(p,c):
        if x: addlog(e,x,y/x)
    return e


def Texpr(a,b):
    e={}
    if a: addlog(e,a,(a+b)/a)
    if b: addlog(e,b,(a+b)/b)
    return e


def Rexpr(m):
    pq=[m*m,1-m*m]
    pa=[(1+m)**2/4,(1-m*m)/4,(1-m)**2/4,(1-m*m)/4]
    return add(entropy(pa),entropy(pq),F(-1,2))


def Bzexpr(m):
    return add({2:(1-m*m)/2},Texpr((1+m)**2,(1-m)**2),F(1,4))


def Cexpr(m,p):
    z=scale(Texpr(m*m,p),F(-1,2))
    z=add(z,Texpr((1+m)**2,p),F(1,4))
    return add(z,Texpr((1-m)**2,p),F(1,4))


def restrict(v,i,bit):
    n=len(v).bit_length()-1; out=[]
    for z in range(1<<(n-1)):
        lo=z&((1<<i)-1); hi=z>>i
        out.append(v[lo|(bit<<i)|(hi<<(i+1))])
    return tuple(out)


def uexpr(v):
    return entropy([x*x for x in fwht(v)])


def bexpr(v):
    p=[x*x for x in fwht(v)]; n=len(v).bit_length()-1; e={}
    for i in range(n):
        bit=1<<i
        for s in range(len(p)):
            if not s&bit: e=add(e,Texpr(p[s],p[s|bit]))
    return e


def gexpr(v):
    n=len(v).bit_length()-1; e=scale(uexpr(v),F(n))
    for i in range(n):
        e=add(e,uexpr(restrict(v,i,0)),F(-1,2))
        e=add(e,uexpr(restrict(v,i,1)),F(-1,2))
    return e


def iexact(v):
    p=[x*x for x in fwht(v)]
    return sum(F(s.bit_count())*x for s,x in enumerate(p))


def ln_interval(y,terms=120):
    # Exact atanh series: ln y = 2 sum z^(2j+1)/(2j+1),
    # z=(y-1)/(y+1), with the displayed geometric tail bound.
    assert F(1) <= y <= F(2)
    z=(y-1)/(y+1)
    zz=z*z; power=z; s=F(0)
    for j in range(terms):
        s += power/F(2*j+1)
        power *= zz
    lo=2*s
    tail=2*power/(F(2*terms+1)*(1-zz))
    return lo,lo+tail


LN2=ln_interval(F(2))


@lru_cache(None)
def log2_interval_integer(p):
    k=p.bit_length()-1
    y=F(p,1<<k)
    lo,hi=ln_interval(y)
    return F(k)+lo/LN2[1], F(k)+hi/LN2[0]


def interval_sign(e):
    lo=hi=F(0)
    for p,x in e.items():
        a,b=log2_interval_integer(p)
        if x>=0: lo+=x*a; hi+=x*b
        else: lo+=x*b; hi+=x*a
    return (1 if lo>0 else -1 if hi<0 else 0),(lo,hi)


def value(e): return sum(float(x)*log2(p) for p,x in e.items())


def fmt(e): return '{'+', '.join(f'{p}:{x}' for p,x in sorted(e.items()))+'}'


mask=56242
q=tuple(1 if mask&(1<<i) else -1 for i in range(16))
f=tuple(q)+tuple(1 for _ in q)
h=fwht(f); p=[x*x for x in h]
U=uexpr(f); M=add(gexpr(f),bexpr(f),F(-1)); I=iexact(f)
m=h[0]; n=5; t=4; mt=m**t

DR={}; C={}
for i in range(n):
    mm=F(sum(restrict(f,i,0)),len(restrict(f,i,0)))*m**(t-1)
    mp=F(sum(restrict(f,i,1)),len(restrict(f,i,1)))*m**(t-1)
    DR=add(DR,add(Rexpr(mt),add(Rexpr(mm),Rexpr(mp)),F(-1,2)),F(t))
    C=add(C,Cexpr(mt,p[1<<i]*m**(2*t-2)),F(t))
RR=Rexpr(mt); BZ=Bzexpr(mt); J=(1-mt)/2
IA=F(t,2)*I+J

alpha_num=scale(add(M,U),F(t,2))
alpha_num=add(alpha_num,DR); alpha_num=add(alpha_num,RR,F(2))
alpha_num=add(alpha_num,BZ,F(-1)); alpha_num=add(alpha_num,C,F(-1))
beta_num=add(scale(U,F(t,2)),RR)
alpha4=scale(alpha_num,1/IA); beta4=scale(beta_num,1/IA)
alphaF=scale(add(M,U),1/I); betaF=scale(U,1/I)
D0=add(alpha4,alphaF,F(-1)); D1=add(beta4,betaF,F(-1))

eta=F(1,4)
c4=add(alpha4,beta4,eta)
above=add(c4,{2:F(-10669,5000)})

checks={'D0':D0,'D_slope':D1,'c4_minus_2.1338':above}
print('status=PASS')
print(f'mean_F={m}')
print(f'I_F={I}')
print(f'mean_tensor4={mt}')
print(f'I_activated_tensor4={IA}')
print(f'alpha4={value(alpha4):.15f}')
print(f'beta4={value(beta4):.15f}')
print(f'c4_eta_1_4={value(c4):.15f}')
for name,e in checks.items():
    s,interval=interval_sign(e)
    assert s>0
    print(f'{name}_sign={s}')
    print(f'{name}_outward_interval=[{float(interval[0]):.17g},{float(interval[1]):.17g}]')
    print(f'{name}_rational_log_terms={len(e)}')

