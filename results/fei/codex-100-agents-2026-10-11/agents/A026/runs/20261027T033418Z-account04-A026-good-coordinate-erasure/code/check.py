"""Frozen finite audit. Exact rational spectra and prime-log expressions only."""
from pathlib import Path
from fractions import Fraction as F
from collections import defaultdict
import json, time, sys, hashlib
from functools import lru_cache

ROOT=Path(__file__).resolve().parents[1]
start=time.monotonic(); COUNT=0
def ck(p):
    global COUNT
    COUNT+=1
    if not p: raise AssertionError(COUNT)
    if time.monotonic()-start>55: raise TimeoutError('55-second frozen cap')
@lru_cache(None)
def factor(n):
    out={}; d=2
    while d*d<=n:
        while n%d==0: out[d]=out.get(d,0)+1; n//=d
        d+=1
    if n>1: out[n]=out.get(n,0)+1
    return out
class Log:
    def __init__(self): self.d=defaultdict(F)
    def add(self,c,x):
        if c==0:return self
        assert x>0
        for p,k in factor(x.numerator).items(): self.d[p]+=c*k
        for p,k in factor(x.denominator).items(): self.d[p]-=c*k
        return self
    def __add__(self,o):
        r=Log(); r.d.update(self.d)
        for p,c in o.d.items():r.d[p]+=c
        return r
    def __sub__(self,o):return self+o.scale(-1)
    def scale(self,c):
        r=Log();r.d.update({p:v*c for p,v in self.d.items()});return r
    def __eq__(self,o):return all(v==o.d.get(p,0) for p,v in self.d.items()) and all(v==self.d.get(p,0) for p,v in o.d.items())
    def dump(self):return {str(p):str(c) for p,c in sorted(self.d.items()) if c}
def entropy(p):
    z=Log()
    for v in p:
        if v:z.add(-v,v)
    return z
def kl(p,q):
    z=Log()
    for a,b in zip(p,q):
        if a:z.add(a,a/b)
    return z
def lnunit(x):
    t=(x-1)/(x+1);s=F(0)
    for j in range(24):s+=2*t**(2*j+1)/(2*j+1)
    return s,s+2*t**49/(49*(1-t*t))
@lru_cache(None)
def lgprime(p):
    k=p.bit_length()-1;a,b=lnunit(F(p,1<<k));c,d=lnunit(F(2))
    return k+a/d,k+b/c
def bounds(z):
    lo=hi=F(0)
    for p,v in z.d.items():
        if not v:continue
        a,b=lgprime(p)
        lo+=v*(a if v>0 else b);hi+=v*(b if v>0 else a)
    return lo,hi
@lru_cache(None)
def _walsh(f):
    a=list(map(F,f)); n=len(a)
    h=1
    while h<n:
        for j in range(0,n,2*h):
            for k in range(j,j+h):u,v=a[k],a[k+h];a[k],a[k+h]=u+v,u-v
        h*=2
    return tuple(v/n for v in a)
def walsh(f):return _walsh(tuple(f))
@lru_cache(None)
def _spec(f):return tuple(v*v for v in walsh(f))
def spec(f):return _spec(tuple(f))
def table(n,label):return [1-2*((label>>x)&1) for x in range(1<<n)]
def delete(t,i):return (t&((1<<i)-1))|((t>>(i+1))<<i)
def insert(t,i,b):return (t&((1<<i)-1))|((t>>i)<<(i+1))|(b<<i)
def child(f,i,b):return [f[insert(t,i,b)] for t in range(len(f)//2)]
def inf(f,i):return F(sum(f[x]!=f[x^(1<<i)] for x in range(len(f))),len(f))
def I(f):return sum((inf(f,i) for i in range(len(f).bit_length()-1)),F(0))
def B(f,i):
    p=spec(f);q=[F(0)]*(len(f)//2)
    for t,v in enumerate(p):q[delete(t,i)]+=v
    return entropy(p)-entropy(q)
def mux(a,g,h):return [g[t] if a[u]==1 else h[t] for u in range(len(a)) for t in range(len(g))]
def target(a,g,h,eps):
    f=mux(a,g,h);p=spec(f);na=len(a);nd=len(g);pa=spec(a);V=1-pa[0]
    gamma=F(sum(x!=y for x,y in zip(g,h)),nd);eta=V*gamma
    q=[sum(p[u*nd+t] for u in range(na)) for t in range(nd)]
    out=[F(0)]*len(f);C=Log()
    for t,mass in enumerate(q):
        if not mass:continue
        k=sum(p[u*nd+t] for u in range(1,na))/mass
        ell=(1-eps)*k+eps*eta
        out[t]=mass*(1-ell)
        for u in range(1,na):out[u*nd+t]=mass*ell*pa[u]/V if V else F(0)
        C=C+kl([1-k,k],[1-ell,ell]).scale(mass)
    ck(sum(out)==1);ck(kl(p,out)==C)
    return f,out,eta,C
def physical(f,q,i):
    a=walsh(f);nn=len(f)//2; raw=[[F(0)]*nn for _ in range(2)]
    for t in range(nn):
        x,y=insert(t,i,0),insert(t,i,1);den=a[x]**2+a[y]**2;r=q[x]+q[y]
        for s in range(2):raw[s][t]=r*(a[x]+(-1)**s*a[y])**2/(2*den) if den else r/2
    z=[sum(v) for v in raw];ck(sum(z)==1)
    kids=[child(f,i,s) for s in range(2)];r=[ [v/z[s] for v in raw[s]] for s in range(2)]
    for s in range(2):ck(sum(r[s])==1)
    dp=kl(spec(f),q);dc=(kl(spec(kids[0]),r[0])+kl(spec(kids[1]),r[1])).scale(F(1,2));loss=dp-dc
    H=entropy(spec(f));hc=(entropy(spec(kids[0]))+entropy(spec(kids[1]))).scale(F(1,2))
    ce=H+dp;cec=hc+dc
    ck(ce-cec==H-hc+loss)
    return loss,dp,dc,kids,r,z
def run(mode):
    labels=range(4) if mode=='pilot' else range(16)
    rows=0;splits=0
    for al in range(16):
        a=table(2,al)
        for gl in labels:
            g=table(2,gl)
            for hl in labels:
                h=table(2,hl)
                f,q,eta,C=target(a,g,h,F(1,16));rows+=1
                ck(eta<=I(f));ck(I(f)==sum((inf(f,i) for i in range(4)),F(0)))
                ck(bounds(C)[1]<=F(31,160)*eta)
                for i in range(4):physical(f,q,i);splits+=1
    # Exact admissible A026 relative-odds AND2 witness. Controller is high bit.
    f=[-1,1,1,1];q=[F(1,6),F(1,4),F(1,3),F(1,4)]
    L,dp,dc,kids,r,z=physical(f,q,1)
    want=Log().add(F(1,4),F(9,8))
    ck(dp==want);ck(L==want);ck(dc==Log());ck(z==[F(1,2),F(1,2)])
    ck(entropy(spec(f))==Log().add(2,F(2)));ck(all(entropy(spec(k))==Log() for k in kids))
    # Calibrated A029 admissible witness: a=y, G=1, H=AND2.
    f,q,eta,C=target([1,-1],[1]*4,[-1,1,1,1],F(1,16))
    L,dp,dc,kids,r,z=physical(f,q,2)
    ck(dp==C);ck(L==C);ck(dc==Log());ck(z==[F(1,2),F(1,2)])
    ck(2**80*3**6>5**10*7*11**3*19**9*31**3)
    result={'status':'PASS','mode':mode,'representations':rows,'physical_splits':splits,'assertions':COUNT,'seconds':time.monotonic()-start,
      'AND2_query_loss':want.dump(),'calibrated_query_loss':L.dump(),'calibrated_eta':str(eta),
      'scope':'Exact identities; universal nonnegativity by data processing, not finite sampling. No raw-budget failure claimed.'}
    (ROOT/'out'/f'{mode}.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8');print(json.dumps(result))
if __name__=='__main__':run(sys.argv[1])
