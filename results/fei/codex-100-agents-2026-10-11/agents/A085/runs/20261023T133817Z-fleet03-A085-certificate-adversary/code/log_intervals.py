from pathlib import Path
from fractions import Fraction as F
import argparse, json, time, hashlib

RUN=Path(__file__).resolve().parents[1]
S=1<<100
checks=0
def ck(b):
    global checks
    checks+=1
    assert b

def fw(v):
    v=list(v); h=1
    while h<len(v):
        for i in range(0,len(v),2*h):
            for j in range(i,i+h):
                a,b=v[j],v[j+h];v[j],v[j+h]=a+b,a-b
        h*=2
    return v
def chars(v):
    return [sum(a*(-1 if (s&x).bit_count()%2 else 1) for x,a in enumerate(v)) for s in range(len(v))]
def law(v):
    w=fw(v);ck(w==chars(v))
    p=[F(a*a,len(v)**2) for a in w];ck(sum(p)==1)
    return p
def influence(v,j):
    return F(sum(a!=v[x^(1<<j)] for x,a in enumerate(v)),len(v))
def restrict(v,j,b):
    return [v[(x&((1<<j)-1))|((x>>j)<<(j+1))|(b<<j)] for x in range(len(v)//2)]
def marginal(p,j):
    return [p[(x&((1<<j)-1))|((x>>j)<<(j+1))]+p[(x&((1<<j)-1))|((x>>j)<<(j+1))|(1<<j)] for x in range(len(p)//2)]

# Outward dyadic interval arithmetic. All interval endpoints below are integer/S.
def add(a,b):return a[0]+b[0],a[1]+b[1]
def neg(a):return -a[1],-a[0]
def mul(a,b):
    z=[x*y for x in a for y in b];return min(z)//S,-(-max(z)//S)
def divpos(a,b):
    assert b[0]>0
    z=[F(x*S,y) for x in a for y in b]
    return min(z).__floor__(),max(z).__ceil__()
def exact(x):return (x*S).__floor__(),(x*S).__ceil__()
def ln_r(r):
    assert 1<=r<=2
    z=exact((r-1)/(r+1));z2=mul(z,z);pw=z;acc=(0,0)
    N=40
    for k in range(N):
        acc=add(acc,(pw[0]//(2*k+1),-(-pw[1]//(2*k+1))))
        pw=mul(pw,z2)
    # 2 sum_{k>=N} z^(2k+1)/(2k+1) <= 9/[4(2N+1)3^(2N+1)].
    tail=F(9,4*(2*N+1)*3**(2*N+1))
    return 2*acc[0],2*acc[1]+(tail*S).__ceil__()
LN2=ln_r(F(2))
def lg(x):
    assert x>0
    k=x.numerator.bit_length()-x.denominator.bit_length()
    r=x/F(2)**k
    if r<1:k-=1;r*=2
    assert 1<=r<2
    a=divpos(ln_r(r),LN2)
    return a[0]+k*S,a[1]+k*S
def ce(p,q):
    v=(0,0)
    for a,b in zip(p,q):
        if a:
            assert b>0
            v=add(v,mul(exact(a),neg(lg(b))))
    return v
def diff(a,b):return add(a,neg(b))
def serial(iv):return [str(F(iv[0],S)),str(F(iv[1],S))]
