from pathlib import Path
from fractions import Fraction as R
from functools import lru_cache
import importlib.util,json,time,sys
sys.dont_write_bytecode=True

BASE=Path(__file__).resolve().parents[1]
HELPER=BASE.parent/'20261014T021008Z-account05-A097-cross-route-transfer'/'code'/'check.py'
spec=importlib.util.spec_from_file_location('a097_own_arithmetic',HELPER)
ar=importlib.util.module_from_spec(spec); spec.loader.exec_module(ar)
checks=0
def req(x):
    global checks
    assert x
    checks+=1
def guard(start):
    if time.perf_counter()-start>55: raise RuntimeError('Frozen cutoff reached; no full result credited')
@lru_cache(None)
def factors(n):
    out={}; d=2
    while d*d<=n:
        while n%d==0: out[d]=out.get(d,0)+1; n//=d
        d+=1
    if n>1: out[n]=out.get(n,0)+1
    return out
def logadd(out,q,w):
    if not w: return
    req(q>0)
    for n,sgn in ((q.numerator,1),(q.denominator,-1)):
        for p,e in factors(n).items():
            out[p]=out.get(p,R(0))+sgn*w*e
            if not out[p]: del out[p]
def kl_expr(p,q):
    expr={}
    for x,y in zip(p,q):
        if x: logadd(expr,x/y,x)
    return expr
def sum_expr(*terms):
    out={}
    for w,expr in terms:
        for p,c in expr.items():
            out[p]=out.get(p,R(0))+w*c
            if not out[p]: del out[p]
    return out

def reference_checks(a,b,r,pg,actual,raw):
    N=len(pg); p=R(1,1<<r); s=R(1,1<<a); t=R(1,N); mu=1-2*s
    rho=4*p*t; lam=2*p/(1<<b); weights=[1-lam,lam*mu,rho]
    if mu:
        r0=[mu*mu]+[(1-mu*mu)*x/(1-raw[0]) for x in raw[1:]]
    else:
        r0=[R(0)]+[x/(1-raw[0]) for x in raw[1:]]
    req(sum(r0)==1)
    c=ar.ce(pg,raw); c0=ar.ce(pg,r0)
    req(raw==r0 or c0[1]<=c[0])
    q=[weights[0]*pg[T]+(weights[1] if T==0 else 0)+rho*t for T in range(N)]
    ref=[weights[0]*r0[T]+(weights[1] if T==0 else 0)+rho*t for T in range(N)]
    req(sum(q)==sum(ref)==1)
    qp=[ref[j%N]*actual[j]/q[j%N] for j in range(len(actual))]
    req(sum(qp)==1)
    kap={}
    for T in range(N):
        jt=[weights[0]*pg[T],weights[1] if not T else R(0),rho*t]
        jr=[weights[0]*r0[T],weights[1] if not T else R(0),rho*t]
        for x,y in zip(jt,jr):
            if x: logadd(kap,(x/q[T])/(y/ref[T]),x)
    req(not sum_expr((1,kl_expr(q,ref)),(1,kap),(-weights[0],kl_expr(pg,r0))))
    # Lifting keeps the full data likelihood ratio, including every control choice.
    req(all(not x or qp[j]/x==ref[j%N]/q[j%N] for j,x in enumerate(actual)))
    cf=ar.ce(actual,qp)
    C=2*p*t*b; E=2*p*t*a; J=2*r*p*t; ig=2*a*s; rootI=ig+C-E+J
    req(cf[1]<=c[0]+10*(C+E+J))
    price=((c[1]/ig).__ceil__())
    K=2*price+10
    req(c[1]<=price*ig and E<=ig/2)
    req(cf[1]<=K*rootI)
    if raw==pg: req(cf[1]<18*rootI)
    if a>=2:
        A=(1-lam)*(1-mu*mu); B=rho*(1-t); M=A+B
        req(M<=1-mu*mu and ref[0]==q[0])
        req(q[0]-mu*mu<=rho)
        req(M/B<=R(4,3)*(1<<(b+r)))
    return qp,cf

def run(active=None,pilot=False):
    start=time.perf_counter(); cases=refs=0
    domain=[1,2] if pilot else [active]
    for a in domain:
        for b in (range(2) if pilot else range(4)):
            n=a+b; N=1<<n; gt=[-1 if not j&((1<<a)-1) else 1 for j in range(N)]
            coeff=ar.walsh(gt); pg=[x*x for x in coeff]
            req(sum(ar.infl(gt))==R(2*a,1<<a))
            for r in (range(1,3) if pilot else range(1,4)):
                p=R(1,1<<r); t=R(1,N); rho=4*p*t; lam=2*p/(1<<b); mu=1-R(2,1<<a)
                cached=None
                for point in range(1<<b):
                    guard(start); edit=point<<a
                    ft=[(1 if j//N==0 and j%N==edit else gt[j%N]) for j in range(N*(1<<r))]
                    fhat=ar.walsh(ft); pf=[x*x for x in fhat]
                    edges=ar.infl(ft)
                    C=2*p*t*b; E=2*p*t*a; J=2*r*p*t; ig=R(2*a,1<<a)
                    req(sum(edges)==ig+C-E+J)
                    req(sum(edges[n:])==J)
                    req(sum(edges[:n])==ig+C-E)
                    req(all(fhat[j]==(coeff[j%N] if not j//N else 0)+2*p*t*((-1)**((j%N&edit).bit_count())) for j in range(len(fhat))))
                    q=[sum(pf[T+U*N] for U in range(1<<r)) for T in range(N)]
                    req(all(q[T]==(1-lam)*pg[T]+(lam*mu if not T else 0)+rho*t for T in range(N)))
                    if cached is None:
                        raws=[pg,[R(1,N)]*N,[R(j+1,N*(N+1)//2) for j in range(N)]]
                        cached=[reference_checks(a,b,r,pg,pf,raw) for raw in raws]
                    else:
                        for qp,cf in cached:
                            req(sum(qp)==1)
                            req(all(not x or qp[j]>0 for j,x in enumerate(pf)))
                        # Dummy translations preserve every squared atom; reuse the same exact reference signs.
                        req(pf==first_pf)
                    first_pf=pf; refs+=3; cases+=1
    name='PILOT.json' if pilot else f'ACTIVE_{active}_RESULTS.json'
    out=dict(status='PASS',cases=cases,reference_cases=refs,assertions=checks+ar.COUNT,seconds=time.perf_counter()-start,helper_source=str(HELPER),active_width=active,pilot_not_added_to_full_total=pilot)
    (BASE/'out'/name).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8'); print(json.dumps(out))

def tensor():
    start=time.perf_counter(); a,b,r=2,1,1; n=3; N=8; p=R(1,2); t=R(1,8); s=R(1,4); mu=R(1,2); rho=R(1,4); lam=R(1,2)
    gt=[-1 if not j&3 else 1 for j in range(N)]
    ft=[1 if j==0 else gt[j%N] for j in range(16)]
    pg=[x*x for x in ar.walsh(gt)]; pf=[x*x for x in ar.walsh(ft)]
    refs=[]
    for raw in (pg,[R(1,8)]*8,[R(j+1,36) for j in range(8)]):
        r0=[mu*mu]+[(1-mu*mu)*x/(1-raw[0]) for x in raw[1:]]
        q=[(1-lam)*pg[T]+(lam*mu if not T else 0)+rho*t for T in range(N)]
        rf=[(1-lam)*r0[T]+(lam*mu if not T else 0)+rho*t for T in range(N)]
        refs.append([rf[j%N]*pf[j]/q[j%N] for j in range(16)])
    total=0
    for label in range(16):
        guard(start); ht=[1 if label>>j&1 else -1 for j in range(4)]
        ph=[x*x for x in ar.walsh(ht)]
        actual=[ht[j&3]*ft[j>>2] for j in range(64)]
        product=[x*x for x in ar.walsh(actual)]
        req(all(product[j]==ph[j&3]*pf[j>>2] for j in range(64)))
        req(sum(ar.infl(actual))==sum(ar.infl(ht))+sum(ar.infl(ft)))
        for rh in (ph,[R(1,4)]*4,[R(j+1,10) for j in range(4)]):
            for rf in refs:
                qr=[rh[j&3]*rf[j>>2] for j in range(64)]
                req(sum(qr)==1)
                for j,x in enumerate(product):
                    if x: req(qr[j]/x==(rh[j&3]/ph[j&3])*(rf[j>>2]/pf[j>>2]))
                total+=1
    req(total==144)
    out=dict(status='PASS',reference_cases=total,terminal_signs=16,assertions=checks+ar.COUNT,seconds=time.perf_counter()-start)
    (BASE/'out'/'TENSOR_RESULTS.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8'); print(json.dumps(out))

if __name__=='__main__':
    arg=sys.argv[1]
    if arg=='pilot': run(pilot=True)
    elif arg=='tensor': tensor()
    else: run(active=int(arg))
