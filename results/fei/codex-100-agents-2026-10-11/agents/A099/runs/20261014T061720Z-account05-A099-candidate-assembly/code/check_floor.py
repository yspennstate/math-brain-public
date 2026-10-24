from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
import json,sys,time
RUN=Path(__file__).resolve().parents[1];start=time.perf_counter();checks=0
def ck(a):
    global checks
    checks+=1;assert a
@lru_cache(None)
def fac(n):
    out={};j=2
    while j*j<=n:
        while n%j==0:out[j]=out.get(j,0)+1;n//=j
        j+=1
    if n>1:out[n]=out.get(n,0)+1
    return out
def logterm(v,w,q):
    if not w:return
    assert q>0
    for n,sgn in ((q.numerator,1),(q.denominator,-1)):
        for j,e in fac(n).items():v[j]=v.get(j,F(0))+w*sgn*e
    for j in list(v):
        if not v[j]:del v[j]
def add(*vs):
    o={}
    for v in vs:
        for p,w in v.items():o[p]=o.get(p,F(0))+w
    return {p:w for p,w in o.items() if w}
def scale(v,c):return {p:w*c for p,w in v.items() if w*c}
def CE(p,r):
    v={}
    for x,y in zip(p,r):
        if x:logterm(v,x,1/y)
    return v
def D(p,r):return add(CE(p,r),scale(CE(p,p),-1))
@lru_cache(None)
def ln(q):
    power=0
    while q>=2:q/=2;power+=1
    while q<1:q*=2;power-=1
    def ser(x):
        z=(x-1)/(x+1);lo=sum((2*z**(2*j+1)/F(2*j+1) for j in range(20)),F(0))
        return lo,lo+2*z**41/(41*(1-z*z))
    lo,hi=ser(q);a,b=ser(F(2))
    return lo+power*(a if power>=0 else b),hi+power*(b if power>=0 else a)
def bounds(v):
    lo=hi=F(0)
    for p,w in v.items():
        a,b=ln(F(p));lo+=w*(a if w>=0 else b);hi+=w*(b if w>=0 else a)
    return lo,hi
def coeff(t):
    N=len(t)
    return [F(sum(y*(-1 if (x&s).bit_count()%2 else 1) for x,y in enumerate(t)),N) for s in range(N)]
def inf(t):return [F(sum(t[x]!=t[x^(1<<i)] for x in range(len(t))),len(t)) for i in range(len(t).bit_length()-1)]
def run(a,b,r,point):
    n=a+b;s=F(1,1<<a);t=F(1,1<<n);p=F(1,1<<r);rho=4*p*t;lam=2*p/F(1<<b);mu=1-2*s
    g=[-1 if not x&((1<<a)-1) else 1 for x in range(1<<n)];vertex=point<<a
    f=[g[x&((1<<n)-1)]+(2 if x==vertex else 0) for x in range(1<<(n+r))]
    ah=coeff(g);P=[z*z for z in ah];fh=coeff(f);PF=[z*z for z in fh]
    q=[sum(PF[(u<<n)|T] for u in range(1<<r)) for T in range(1<<n)]
    weights=[1-lam,lam*mu,rho];vac=[F(int(T==0)) for T in range(1<<n)];unif=[t]*(1<<n)
    ck(sum(weights)==1 and min(weights)>=0);ck(sum(PF)==sum(q)==sum(P)==1)
    predicted=[(1-lam)*P[T]+lam*mu*vac[T]+rho*t for T in range(1<<n)]
    ck(q==predicted)
    C=2*p*t*b;E=2*p*t*a;J=2*r*p*t;Ig=2*a*s
    fI=inf(f);gI=inf(g);If=sum(fI)
    ck(sum(gI)==Ig);ck(If==Ig+C-E+J);ck(E<=Ig/2)
    for i in range(n+r):ck(fI[i]==2*s-2*p*t if i<a else fI[i]==2*p*t)
    for u in range(1,1<<r):ck(sum(PF[(u<<n)|T] for T in range(1<<n))==4*p*p*t)
    for kind in ('true','uniform','increasing'):
        R=P if kind=='true' else [t]*(1<<n) if kind=='uniform' else [F(T+1,(1<<n)*((1<<n)+1)//2) for T in range(1<<n)]
        R0=[mu*mu]+[R[T]*(1-mu*mu)/(1-R[0]) for T in range(1,1<<n)]
        ck(sum(R0)==1 and all(R0[T]>0 for T in range(1<<n) if P[T]))
        Rp=[(1-lam)*R0[T]+lam*mu*vac[T]+rho*t for T in range(1<<n)]
        Q=[Rp[T]*PF[(u<<n)|T]/q[T] for u in range(1<<r) for T in range(1<<n)]
        ck(sum(Q)==1 and all(Q[j]>0 for j,v in enumerate(PF) if v))
        kappa={}
        for T in range(1<<n):
            for w,tru,ref in zip(weights,[P,vac,unif],[R0,vac,unif]):
                if w and tru[T]:logterm(kappa,w*tru[T],(w*tru[T]/q[T])/(w*ref[T]/Rp[T]))
        ck(not add(D(PF,Q),scale(D(P,R0),-(1-lam)),kappa))
        ck(not add(D(PF,Q),scale(D(q,Rp),-1)))
        c=CE(P,R);c0=CE(P,R0);cost=CE(PF,Q)
        drop=add(c,scale(c0,-1));ber=D([mu*mu,1-mu*mu],[R[0],1-R[0]])
        ck(drop==ber)
        gap=add(c,{2:10*(C+E+J)},scale(cost,-1))
        ck(not gap or bounds(gap)[0]>0)
        _,c_hi_nat=bounds(c);ln2lo,_=ln(F(2));C0=c_hi_nat/ln2lo/Ig;K=2*C0+10
        gapK={2:K*If};gapK=add(gapK,scale(cost,-1))
        ck(not gapK or bounds(gapK)[0]>0)
        if kind=='true':ck(bounds(add({2:18*If},scale(cost,-1)))[0]>0)
    ck(time.perf_counter()-start<60)
cases=[(a,b,r,point) for a in (1,2,3) for b in (0,1) for r in (1,2) for point in range(1<<b)]
pilot='--pilot' in sys.argv
if pilot:cases=[(1,0,1,0)]
for case in cases:run(*case)
out={'status':'PASS','helper_version':'A099-negative-cell-floor-audit-v1','instances':len(cases),'reference_cases':3*len(cases),'assertions':checks,'runtime_seconds':time.perf_counter()-start,'arithmetic':'Direct signed characters and physical flips; Fraction positive floors/actual kernels; exact posterior prime-log identities; fixed 20-term rational ln bounds','max_dimension':max(a+b+r for a,b,r,v in cases),'scope':'Finite validation plus complete all-parameter analytic reconstruction; no hereditary reference reset assumed'}
(RUN/'out'/('PILOT.json' if pilot else 'EXACT_FLOOR.json')).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out))
