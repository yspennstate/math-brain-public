#!/usr/bin/env python3
"""Compressed recurrence for F_{k+1}=A(F_k^{tensor t})."""
from fractions import Fraction
from math import log2


def fwht(v):
    a=[Fraction(x) for x in v]; h=1
    while h<len(a):
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


def xr(x,y): return 0.0 if x==0 else float(x)*log2(float(y/x))
def T(a,b): return xr(a,a+b)+xr(b,a+b)


def restrict(v,i,bit):
    n=len(v).bit_length()-1; out=[]
    for z in range(1<<(n-1)):
        lo=z&((1<<i)-1); hi=z>>i
        out.append(v[lo|(bit<<i)|(hi<<(i+1))])
    return tuple(out)


def basic(v):
    h=fwht(v); p=[x*x for x in h]; c=caps(p)
    U=sum(xr(x,y) for x,y in zip(p,c))
    I=sum(s.bit_count()*float(x) for s,x in enumerate(p))
    n=len(v).bit_length()-1; B=0.0
    for i in range(n):
        bit=1<<i
        for s in range(len(p)):
            if not s&bit: B+=T(p[s],p[s|bit])
    return U,I,B,h,p


def stats(v):
    U,I,B,h,p=basic(v); n=len(v).bit_length()-1; G=n*U
    for i in range(n):
        G-=.5*basic(restrict(v,i,0))[0]
        G-=.5*basic(restrict(v,i,1))[0]
    types=[]
    for i in range(n):
        vm=restrict(v,i,0); vp=restrict(v,i,1)
        types.append([1.0, sum(vm)/len(vm), sum(vp)/len(vp), float(p[1<<i])])
    return dict(U=U,I=I,M=G-B,m=float(h[0]),types=types,n=n)


def activate(v): return tuple(v)+tuple(1 for _ in v)


def R(m):
    p=[m*m,1-m*m]
    uq=sum(xr(x,y) for x,y in zip(p,caps(p)))
    pa=[(1+m)**2/4,(1-m*m)/4,(1-m)**2/4,(1-m*m)/4]
    ua=sum(xr(x,y) for x,y in zip(pa,caps(pa)))
    return ua-.5*uq


def Bz(m): return (1-m*m)/2+.25*T((1+m)**2,(1-m)**2)


def C(m,p):
    return -.5*T(m*m,p)+.25*T((1+m)**2,p)+.25*T((1-m)**2,p)


def step(s,t):
    m=s['m']; mt=m**t; scale=m**(t-1); pscale=m**(2*t-2)
    dr=0.0; corr=0.0; newtypes=[]
    for mult,mm,mp,p in s['types']:
        w=t*mult
        qmm=mm*scale; qmp=mp*scale; qp=p*pscale
        dr += w*(R(mt)-.5*(R(qmm)+R(qmp)))
        corr += w*C(mt,qp)
        newtypes.append([w,(1+qmm)/2,(1+qmp)/2,qp/4])
    newtypes.append([1.0,mt,1.0,(1-mt)**2/4])
    return dict(
        U=.5*t*s['U']+R(mt),
        I=.5*t*s['I']+(1-mt)/2,
        M=.5*t*s['M']+dr+R(mt)-Bz(mt)-corr,
        m=(1+mt)/2,
        types=newtypes,
        n=t*s['n']+1,
        dr=dr,corr=corr,
    )


def threshold(s,eta): return (s['M']+(1+eta)*s['U'])/s['I']


mask=56242
q=tuple(1 if mask&(1<<i) else -1 for i in range(16))
s=stats(activate(q))
eta=.25; t=4
print('status=PASS')
print('tower=F_0=A(mask56242); F_(k+1)=A(F_k^tensor4)')
print('k n mean alpha beta c_eta_1_4 increment')
prev=None
selected=set(range(0,11))|{15,20,25,30,35,40}
for k in range(41):
    c=threshold(s,eta)
    inc=float('nan') if prev is None else c-prev
    alpha=(s['M']+s['U'])/s['I']; beta=s['U']/s['I']
    if k in selected:
        print(k,s['n'],f'{s["m"]:.15f}',f'{alpha:.15f}',f'{beta:.15f}',f'{c:.15f}',f'{inc:.3e}')
    if k==0:
        assert abs(c-2.067158948727794)<2e-12
    if k==1:
        assert abs(c-2.133840018016030)<2e-12
    prev=c
    s=step(s,t)

