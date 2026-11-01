from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
import json, sys, time
RUN=Path(__file__).resolve().parents[1]
start=time.perf_counter(); assertions=0
def check(a,b):
    global assertions
    assertions+=1
    assert a==b,(a,b)
@lru_cache(None)
def factors(n):
    out={}; d=2
    while d*d<=n:
        while n%d==0: out[d]=out.get(d,0)+1; n//=d
        d+=1
    if n>1:out[n]=out.get(n,0)+1
    return out
def logadd(v,c,r):
    if not c:return
    assert r>0
    for n,sgn in [(r.numerator,1),(r.denominator,-1)]:
        for p,e in factors(n).items():v[p]=v.get(p,F(0))+c*sgn*e
    for p in list(v):
        if not v[p]:del v[p]
def plus(*vs):
    out={}
    for v in vs:
        for p,c in v.items():out[p]=out.get(p,F(0))+c
    return {p:c for p,c in out.items() if c}
def scale(v,c):return {p:x*c for p,x in v.items() if x*c}
def phi(a,b):
    v={}
    if a:logadd(v,a,(a+b)/a)
    if b:logadd(v,b,(a+b)/b)
    return v
def spectrum(truth):
    N=len(truth)
    return [F(sum(y*(-1 if (x&s).bit_count()%2 else 1) for x,y in enumerate(truth)),N)**2 for s in range(N)]
def truth(n,mask):return [-1 if mask>>x&1 else 1 for x in range(1<<n)]
def stats(t):
    n=(len(t)).bit_length()-1; p=spectrum(t)
    e=[F(sum(t[x]!=t[x^(1<<i)] for x in range(len(t))),len(t)) for i in range(n)]
    check(sum(p),1)
    for i in range(n):check(e[i],sum(v for s,v in enumerate(p) if s>>i&1))
    B={}; M={}; Bt={}; Mt={}; Ds=[]
    for i in range(n):
        dv={}
        for s in range(len(p)):
            if s>>i&1:continue
            a,b=p[s],p[s|1<<i]; edge=phi(a,b); B=plus(B,edge)
            if s.bit_count()>=2:Bt=plus(Bt,edge)
            if b:
                v={};logadd(v,b,(a+b)/b);M=plus(M,v)
                if s.bit_count()>=2:Mt=plus(Mt,v)
                logadd(dv,b/e[i],b/(e[i]*(a+b)))
        Ds.append(dv)
    weighted=plus(*(scale(v,e[i]) for i,v in enumerate(Ds)))
    rarity={}
    for d in e:
        if d:logadd(rarity,d,1/d)
    check(M,plus(rarity,scale(weighted,-1)))
    return p,e,B,M,Bt,Mt,Ds,weighted
def run(n,mask,m,ell,k):
    seed=truth(n,mask); sp,se,sB,sM,*_=stats(seed)
    sD=stats(seed)[-1]; J=m*sum(se)+ell; N=n*m+ell+k; q=F(1,1<<k)
    def core(x):
        v=(-1 if ((x>>(n*m))&((1<<ell)-1)).bit_count()%2 else 1)
        for b in range(m):v*=seed[(x>>(b*n))&((1<<n)-1)]
        return v
    t=[core(x) if x>>(n*m+ell)==0 else 1 for x in range(1<<N)]
    p,e,B,M,Bt,Mt,Ds,D=stats(t)
    check(sum(e),q*(J+k))
    check(Bt,plus(scale(sB,q*m),{2:2*k*q*(1-k*q)}))
    check(Mt,plus(scale(sM,q*m),{2:k*q*(1-k*q)}))
    d=(1-q)**2+q*q; dc={2:(1-q)*(k-1)};logadd(dc,q,q/d)
    mc={2:q*(1-q)};logadd(mc,q*q,d/(q*q))
    check(M,plus(scale(sM,q*m),scale(mc,k)))
    check(D,scale(plus(scale(sD,m),{2:k*J},scale(dc,k)),q))
    for i in range(n*m+ell):
        expected=stats(seed)[6][i%n] if i<n*m and se[i%n] else {}
        if i<n*m and not se[i%n]:check(e[i],0);continue
        check(Ds[i],plus(expected,{2:F(k)}))
        if i>=n*m:
            check(e[i],q)
            check(plus(*(phi(p[s],p[s|1<<i]) for s in range(len(p)) if not s>>i&1)),{})
    for i in range(n*m+ell,N):check(Ds[i],dc)
    assert time.perf_counter()-start<60
pilot='--pilot' in sys.argv
cases=[(n,mask,m,ell,k) for n in (1,2) for mask in range(1<<(1<<n)) for m in ([1,2] if n==1 else [1]) for ell in (2,3) for k in (1,2)]
if pilot:cases=[(1,mask,1,2,1) for mask in range(4)]
for case in cases:run(*case)
out={'status':'PASS','helper_version':'A099-direct-character-refund-v1','cases':len(cases),'assertions':assertions,'runtime_seconds':time.perf_counter()-start,'max_dimension':max(n*m+ell+k for n,mask,m,ell,k in cases),'arithmetic':'Direct character sums; physical edges; Fraction/prime-log identities','scope':'Exact finite checks accompany complete analytic reconstruction, no finite-to-infinite extrapolation'}
(RUN/'out').mkdir(exist_ok=True)
(RUN/'out'/('PILOT.json' if pilot else 'EXACT_AUDIT.json')).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out))
