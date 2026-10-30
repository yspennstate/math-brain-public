#!/usr/bin/env python3
"""Exact rational-log intervals for the finite B05 sign obligations."""
from fractions import Fraction
from functools import lru_cache


class E:
    def __init__(self, c=0, logs=None):
        self.c = Fraction(c); self.logs = {} if logs is None else dict(logs)
    def __add__(self, o):
        if not isinstance(o, E): o = E(o)
        z = E(self.c+o.c, self.logs)
        for x, a in o.logs.items(): z.logs[x] = z.logs.get(x, Fraction(0))+a
        z.logs = {x:a for x,a in z.logs.items() if a}; return z
    __radd__ = __add__
    def __neg__(self): return self*Fraction(-1)
    def __sub__(self, o): return self+(-o)
    def __mul__(self, a): return E(self.c*a, {x:b*a for x,b in self.logs.items()})
    __rmul__ = __mul__


def ln(x): return E(0, {Fraction(x):Fraction(1)})
def xlog(x, y): return E() if x == 0 else x*ln(y/x)
def q(t): return E() if t == 0 else t*ln(1/t)+2*t


def wht(v):
    a = [Fraction(x) for x in v]; h = 1
    while h < len(a):
        for j in range(0, len(a), 2*h):
            for k in range(j, j+h):
                x, y = a[k], a[k+h]; a[k], a[k+h] = x+y, x-y
        h *= 2
    return tuple(x/len(a) for x in a)


def caps(p):
    a = list(p); n = len(a).bit_length()-1
    for i in range(n):
        for s in range(len(a)):
            if not s >> i & 1: a[s] += a[s | 1 << i]
    return a


def restrict(v, i, b):
    n = len(v).bit_length()-1; out = []
    for z in range(1 << (n-1)):
        lo = z & ((1 << i)-1); hi = z >> i
        out.append(v[lo | (b << i) | (hi << (i+1))])
    return tuple(out)


@lru_cache(None)
def stats(v):
    h = wht(v); p = tuple(x*x for x in h); pi = caps(p); n = len(v).bit_length()-1
    U = sum((xlog(x,y) for x,y in zip(p,pi)), E())
    I = sum((Fraction(s.bit_count())*x for s,x in enumerate(p)), Fraction(0))
    B = E(); inf = []
    for i in range(n):
        inf.append(sum((p[s] for s in range(len(p)) if s >> i & 1), Fraction(0)))
        for s in range(len(p)):
            if not s >> i & 1:
                a,b = p[s],p[s | 1 << i]; B += xlog(a,a+b)+xlog(b,a+b)
    G = n*U
    for i in range(n): G -= Fraction(1,2)*(stats(restrict(v,i,0))[0]+stats(restrict(v,i,1))[0])
    return U,I,B,G-B,p,tuple(inf)


def theta(v, X):
    p=stats(v)[4]; inf=stats(v)[5]; n=len(v).bit_length()-1; ans=E()
    for i in range(n):
        if X >> i & 1: ans += q(inf[i])
        else:
            e=Fraction(0); sub=X
            while True:
                e += p[(1 << i) | sub]
                if sub == 0: break
                sub = (sub-1) & X
            ans += q(e)
    return ans


def L(v, a):
    U,I,B,M,_,_=stats(v)
    return M+2*U-4*I-a*I*ln(2)  # c=a+4/ln(2)


def remap(mask,d): return (mask & ((1 << d)-1)) | ((mask >> (d+1)) << d)
def drift(v,Y,x,Z,a):
    ch0,ch1=restrict(v,x,0),restrict(v,x,1); z=remap(Z,x)
    return L(v,a)-Fraction(1,2)*(L(ch0,a)+L(ch1,a))+2*theta(v,Y)-theta(ch0,z)-theta(ch1,z)


def ln_interval(x,N=110):
    k=0; y=Fraction(x)
    while y<1: y*=2; k-=1
    while y>2: y/=2; k+=1
    z=(y-1)/(y+1); s=Fraction(0)
    for j in range(N): s += z**(2*j+1)/Fraction(2*j+1)
    lo=2*s; hi=lo+2*z**(2*N+1)/Fraction((2*N+1)*(1-z*z))
    if y==1: lo=hi=Fraction(0)
    if k==0: return lo,hi
    l2,h2=ln_interval(Fraction(2),N)
    return (lo+k*l2,hi+k*h2) if k>=0 else (lo+k*h2,hi+k*l2)


def bound(e):
    lo=hi=e.c
    for x,a in e.logs.items():
        l,h=ln_interval(x)
        if a>=0: lo+=a*l; hi+=a*h
        else: lo+=a*h; hi+=a*l
    return lo,hi


rows=[]
for r in range(1,7):
    v=tuple([-1]+[1]*((1 << r)-1))
    if r==1: Y,Z=1,0
    elif r==2: Y,Z=3,2
    else: Y,Z=3,6
    rows.append((r,*bound(drift(v,Y,0,Z,Fraction(14)))))
v5=tuple([-1]+[1]*31)
full=bound(drift(v5,31,0,30,Fraction(29,2)))
print('quantity=ln(2)*signed_node_charge')
for r,lo,hi in rows:
    print(f'width_two_or_endpoint_rank_{r}_lower={float(lo)}')
    print(f'width_two_or_endpoint_rank_{r}_upper={float(hi)}')
print(f'full_block_rank_5_at_cstar_lower={float(full[0])}')
print(f'full_block_rank_5_at_cstar_upper={float(full[1])}')
print('status=' + ('CERTIFIED' if all(hi<0 for _,_,hi in rows) and full[0]>0 else 'FAIL'))
