import sys,json,time,itertools
from pathlib import Path
from fractions import Fraction as Q
from functools import lru_cache
ROOT=Path(__file__).resolve().parents[2]
START=time.monotonic(); counts={}; pilot='--pilot' in sys.argv
def check(ok,label):
    assert ok,label
    counts[label]=counts.get(label,0)+1
    if time.monotonic()-START>60: raise RuntimeError('frozen runtime reached')
def add(*parts):
    out={}
    for c,f in parts:
        for k,v in f.items(): out[k]=out.get(k,Q(0))+c*v
    return {k:v for k,v in out.items() if v}
@lru_cache(None)
def factor(n):
    out={}; d=2
    while d*d<=n:
        while n%d==0: out[d]=out.get(d,0)+1; n//=d
        d+=1
    if n>1: out[n]=out.get(n,0)+1
    return out
def eta(q):
    if not q: return {}
    return add((q,factor(q.denominator)),(-q,factor(q.numerator)))
def E(a): return eta(a*a)
def phi(d): return E(1-2*d)
@lru_cache(None)
def spectrum(f):
    a=list(f); h=1
    while h<len(a):
        for j in range(0,len(a),2*h):
            for k in range(j,j+h): a[k],a[k+h]=a[k]+a[k+h],a[k]-a[k+h]
        h*=2
    return tuple(Q(x,len(a)) for x in a)
@lru_cache(None)
def H(f): return add(*[(1,eta(x*x)) for x in spectrum(f)])
def Hplus(f): return add((1,H(f)),(-1,E(spectrum(f)[0])))
def neg(f): return Q(f.count(-1),len(f))
@lru_cache(None)
def inf(f,i): return Q(sum(f[x]!=f[x^(1<<i)] for x in range(len(f))),len(f))
@lru_cache(None)
def I(f): return sum((inf(f,i) for i in range(len(f).bit_length()-1)),Q(0))
@lru_cache(None)
def restrict(f,fixed):
    fixed=dict(fixed); free=[i for i in range(len(f).bit_length()-1) if i not in fixed]
    base=sum(b<<i for i,b in fixed.items())
    return tuple(f[base+sum(((x>>j)&1)<<i for j,i in enumerate(free))] for x in range(1<<len(free)))
@lru_cache(None)
def activate(u,a): return tuple(u[x] if v==-1 else 1 for v in a for x in range(len(u)))
@lru_cache(None)
def R(p,d):
    v=4*p*(1-p)
    return add((4*d*(1-d),eta(p*p)),(2*d*(1-d)*v,{2:Q(1)}),(v,E(d)),(1,phi(p*d)),(-p,phi(d)))
def ln_bounds(y):
    z=(y-1)/(y+1); power=z; lo=Q(0)
    for j in range(24): lo+=2*power/(2*j+1); power*=z*z
    return lo,lo+2*power/(49*(1-z*z))
LN2=ln_bounds(Q(2)); DEN=1<<52
@lru_cache(None)
def log_bounds(k):
    if k==2: return Q(1),Q(1)
    q=Q(k); exponent=0
    while q>=2: q/=2; exponent+=1
    lo,hi=ln_bounds(q); lo=exponent+lo/LN2[1]; hi=exponent+hi/LN2[0]
    return Q((lo*DEN).__floor__(),DEN),Q((hi*DEN).__ceil__(),DEN)
def bounds(f):
    lo=hi=Q(0)
    for k,c in f.items():
        a,b=log_bounds(k)
        lo+=c*(a if c>=0 else b); hi+=c*(b if c>=0 else a)
    return lo,hi
@lru_cache(None)
def identity(u,a):
    f=activate(u,a); p=neg(a); d=neg(u)
    check(not add((1,H(f)),(-p,H(u)),(-d,Hplus(a)),(-1,R(p,d))),'exact prime-log entropy identity')
    check(I(f)==p*I(u)+d*I(a),'independent physical full influence')
    check(sum(x*x for x in spectrum(f))==1,'exact Parseval')
    return f
def evaluate(u,a,leaves,cost):
    f=identity(u,a); p=neg(a); d=neg(u); coreH={}; actH={}; remainder=R(p,d)
    leafI=actI=mean=variation=Q(0)
    for fixed,w in leaves:
        v=restrict(u,fixed); g=identity(v,a); e=neg(v)
        check(restrict(f,fixed)==g,'actual lifted restriction')
        coreH=add((1,coreH),(w,H(v))); actH=add((1,actH),(w,H(g)))
        remainder=add((1,remainder),(-w,R(p,e)))
        leafI+=w*I(v); actI+=w*I(g); mean+=w*e; variation+=w*abs(e-d)
    check(mean==d,'core bias martingale')
    check(I(u)-leafI==cost,'core physical query budget')
    check(I(f)-actI==p*cost,'scaled physical query budget')
    check(actI==p*leafI+d*I(a),'unspent controller terminal reserve')
    check(variation<=cost/2,'nonreusing martingale variation payment')
    error=add((1,H(f)),(-1,actH),(-p,H(u)),(p,coreH))
    check(error==remainder,'exact controller entropy cancellation')
    lo,hi=bounds(error)
    check(max(abs(lo),abs(hi))<=22*p*cost,'rigorous full signed transport rate 22')
    # Independent check of the consumed A028 scalar estimate, without its code.
    check(bounds(R(p,d))[1]<=6*d*4*p*(1-p),'A028 scalar controller correction at rational 6')
    counts['partitions']=counts.get('partitions',0)+1
