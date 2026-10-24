#!/usr/bin/env python3
"""Independent closed-form certificate for B05 width-two point defects."""
from fractions import Fraction as F


class E:
    def __init__(self,c=0,logs=None): self.c=F(c); self.logs={} if logs is None else dict(logs)
    def __add__(self,o):
        if not isinstance(o,E): o=E(o)
        z=E(self.c+o.c,self.logs)
        for x,a in o.logs.items(): z.logs[x]=z.logs.get(x,F(0))+a
        z.logs={x:a for x,a in z.logs.items() if a}; return z
    __radd__=__add__
    def __neg__(self): return self*F(-1)
    def __sub__(self,o): return self+(-o)
    def __mul__(self,a): return E(self.c*a,{x:b*a for x,b in self.logs.items()})
    __rmul__=__mul__


def ln(x): return E(0,{F(x):F(1)})
L=ln(2)
def xlog(x,y): return E() if x==0 else x*ln(y/x)
def T(a,b): return xlog(a,a+b)+xlog(b,a+b)
def qn(t): return E() if t==0 else t*ln(1/t)+2*t  # ln(2)*q_bits


def U(r):
    t=F(1,2**(r-1))
    first=E() if t==1 else -2*(1-t)**2*ln(1-t)
    return first+r*t*(1-t)*L
def B(r):
    t=F(1,2**(r-1))
    return r*(T((1-t)**2,t*t)+2*t*(1-t)*L)
def D(r): return U(r)-(F(1,2)*U(r-1) if r>1 else E())
def M(r): return r*D(r)-B(r)
def theta(r,k):
    t=F(1,2**(r-1))
    return k*qn(t)+(r-k)*qn((2**k)*t*t)


def charge(r,kp,kc,a):
    # c=a+4/ln(2), so (ln2)*c*t = a*t*ln2+4t.
    t=F(1,2**(r-1))
    cm=M(r)-(F(1,2)*M(r-1) if r>1 else E())+2*D(r)
    orbit=2*theta(r,kp)-(theta(r-1,kc) if r>1 else E())
    return cm+orbit-a*t*L-4*t


def ln_interval(x,N=120):
    y=F(x); k=0
    while y<1: y*=2; k-=1
    while y>2: y/=2; k+=1
    z=(y-1)/(y+1); s=F(0)
    for j in range(N): s+=z**(2*j+1)/F(2*j+1)
    lo=2*s; hi=lo+2*z**(2*N+1)/F((2*N+1)*(1-z*z))
    if y==1: lo=hi=F(0)
    if k==0:return lo,hi
    l2,h2=ln_interval(F(2),N)
    return (lo+k*l2,hi+k*h2) if k>=0 else (lo+k*h2,hi+k*l2)
def bound(e):
    lo=hi=e.c
    for x,a in e.logs.items():
        l,h=ln_interval(x)
        if a>=0:lo+=a*l;hi+=a*h
        else:lo+=a*h;hi+=a*l
    return lo,hi


rows=[]
for r in range(1,7):
    kp,kc=(1,0) if r==1 else ((2,1) if r==2 else (2,2))
    rows.append((r,*bound(charge(r,kp,kc,F(14)))))
full=bound(charge(5,5,4,F(29,2)))
print('quantity=natural_log_scaled_signed_node_charge')
for r,lo,hi in rows:
    print(f'c0_rank_{r}_lower={float(lo)}')
    print(f'c0_rank_{r}_upper={float(hi)}')
print(f'cstar_full_rank_5_lower={float(full[0])}')
print(f'cstar_full_rank_5_upper={float(full[1])}')
print('status='+('CERTIFIED' if all(hi<0 for _,_,hi in rows) and full[0]>0 else 'FAIL'))
