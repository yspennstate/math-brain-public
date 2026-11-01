"""A004 independent finite-law projections and actual Boolean certificates."""
from fractions import Fraction as F
from functools import lru_cache
from pathlib import Path
import json, time, sys, hashlib

RUN=Path(__file__).resolve().parents[1]
COUNT=0
def ck(x):
    global COUNT
    COUNT+=1
    assert x
@lru_cache(None)
def factors(n):
    out={};d=2
    while d*d<=n:
        while n%d==0:out[d]=out.get(d,0)+1;n//=d
        d+=1
    if n>1:out[n]=out.get(n,0)+1
    return out
def add(*terms):
    out={}
    for a,v in terms:
        for p,b in v.items():out[p]=out.get(p,F(0))+a*b
    return {p:a for p,a in out.items() if a}
def logq(q):
    q=F(q);assert q>0
    return add((1,factors(q.numerator)),(-1,factors(q.denominator)))
def CE(p,q):
    return add(*[(-a,logq(b)) for a,b in zip(p,q) if a])
def KL(p,q):return add((1,CE(p,q)),(-1,CE(p,p)))
def lnunit(x):
    z=(x-1)/(x+1);v=sum((2*z**(2*j+1)/F(2*j+1) for j in range(36)),F(0))
    return v,v+2*z**73/(73*(1-z*z))
LN2=lnunit(F(2))
@lru_cache(None)
def lb(p):
    k=p.bit_length()-1;a,b=lnunit(F(p,1<<k))
    return k+a/LN2[1],k+b/LN2[0]
def bounds(v):
    lo=hi=F(0)
    for p,a in v.items():
        l,h=lb(p);lo+=a*(l if a>=0 else h);hi+=a*(h if a>=0 else l)
    return lo,hi
def record(v):
    lo,hi=bounds(v)
    return {'prime_logs':{str(p):str(a) for p,a in sorted(v.items())},'lower':str(lo),'upper':str(hi),'display_only':float((lo+hi)/2)}
def spectrum(v):
    w=list(v);h=1
    while h<len(w):
        for i in range(0,len(w),2*h):
            for j in range(i,i+h):a,b=w[j],w[j+h];w[j],w[j+h]=a+b,a-b
        h*=2
    return tuple(F(a*a,len(v)**2) for a in w)
def direct(v):
    return tuple(F(sum(a*(-1)**((s&t).bit_count()) for t,a in enumerate(v))**2,len(v)**2) for s in range(len(v)))
def projection(pi,l):
    # Remove floor-active atoms until the rational free scale stabilizes.
    active={j for j,p in enumerate(pi) if not p}
    while True:
        mass=sum((p for j,p in enumerate(pi) if j not in active),F(0))
        k=(1-sum((l[j] for j in active),F(0)))/mass
        more={j for j,p in enumerate(pi) if l[j]>k*p}
        if more<=active:break
        active|=more
    return tuple(max(x,k*p) for x,p in zip(l,pi)),k
def enumerate_projection(pi,l):
    # Independent finite active-set representation, used on <=3 tail atoms.
    out=set();n=len(pi)
    for mask in range(1<<n):
        a=[j for j in range(n) if mask>>j&1];c=[j for j in range(n) if not mask>>j&1]
        p=sum((pi[j] for j in c),F(0))
        if not p:continue
        k=(1-sum((l[j] for j in a),F(0)))/p
        if k<=0:continue
        if all(l[j]>=k*pi[j] for j in a) and all(l[j]<=k*pi[j] for j in c):
            out.add(tuple(l[j] if j in a else k*pi[j] for j in range(n)))
    return out
def tail_reference(vac,w,x):return (vac,)+tuple(w*z for z in x)
def run(pilot):
    start=time.perf_counter();cases=0;ghost=0;source_reviews={}
    # A090: reconstruct the producer's actual AND3 child; no producer code.
    v=(1,)+(-1,)*7;p=spectrum(v);ck(p==direct(v))
    kids=[tuple(v[t] for t in range(8) if t&1==b) for b in (0,1)]
    pp=[spectrum(x) for x in kids];ck(pp[0]==(F(1,4),)*4);ck(pp[1]==(F(1),F(0),F(0),F(0)))
    q0=tuple(F(x,256) for x in (144,1,1,1,106,1,1,1))
    q1=tuple(F(x,256) for x in (144,80,15,13,1,1,1,1))
    q=tuple((3*x+y)/4 for x,y in zip(q0,q1))
    m=tuple(p[2*t]+p[2*t+1] for t in range(4))
    inherited=[]
    for pb in pp:
        raw=tuple((q[2*t]+q[2*t+1])*(pb[t]/m[t] if m[t] else 1) for t in range(4))
        inherited.append(tuple(z/sum(raw) for z in raw))
    current=inherited[0];ck(current==tuple(F(x) for x in (F(659,2484),F(85,1242),F(1615,2484),F(10,621))))
    pi=(F(1,3),)*3;M=tuple(x/(1-current[0]) for x in current[1:]);T=(F(7,8),F(1,16),F(1,16))
    repaired=tail_reference(current[0],1-current[0],pi)
    target=(F(7,12),F(35,96),F(5,192),F(5,192))
    ck(min(x/y for x,y in zip(pi,T))==F(8,21));ck(all(x>=y/4 for x,y in zip(repaired,target)))
    oldbill=add(*[(F(1,2),CE(pb,r)) for pb,r in zip(pp,inherited)])
    newbill=add((F(1,2),CE(pp[0],repaired)),(F(1,2),CE(pp[1],inherited[1])))
    release=add((1,oldbill),(-1,newbill));ck(release==add((F(3,8),KL(pi,M))));ck(bounds(release)[0]>F(1,4))
    source_reviews['A090_release']=record(release)
    # Sign reversal for exactly the same actual Boolean source and floor.
    p2=spectrum((1,-1,-1,-1));ck(p2==direct((1,-1,-1,-1)));ck(p2==(F(1,4),)*4)
    M=(F(1,4),F(5,8),F(1,8));l=(F(1,2),F(0),F(0));pi=(F(1,3),)*3
    x,k=projection(pi,l);ck(x==(F(1,2),F(1,4),F(1,4)))
    prof=(F(1,2),F(5,12),F(1,12));r=tail_reference(F(1,4),F(3,4),M)
    flex=add((1,CE(p2,tail_reference(F(1,4),F(3,4),x))),(-1,CE(p2,r)))
    fixed=add((1,CE(p2,tail_reference(F(1,4),F(3,4),prof))),(-1,CE(p2,r)))
    ck(flex==add((F(1,4),logq(F(5,8)))));ck(fixed==add((F(1,4),logq(F(9,8)))))
    ck(bounds(flex)[1]<0<bounds(fixed)[0]);source_reviews['flexible_price']=record(flex);source_reviews['fixed_profile_price']=record(fixed)
    # A097 exact price/sign and omitted positive derivative factor.
    for t in (F(1,4),F(3,4),F(1)):
        for aa,bb,ll in ((F(1,3),F(1,4),F(1,2)),(F(3,4),F(1,4),F(1,2))):
            a,b,ell=t*aa,t*bb,t*ll;z=max(a,ell)
            d=add((a,logq(b/z)),(t-a,logq((t-b)/(t-z))))
            ck(d==add((t,KL((a/t,1-a/t),(z/t,1-z/t))),(-t,KL((a/t,1-a/t),(b/t,1-b/t)))))
            test=(ell+t)/2
            deriv=-a/test+(t-a)/(t-test)
            ck(deriv==t*(test-a)/(test*(t-test)))
            if t!=1 and test!=a:ck(deriv!=(test-a)/(test*(t-test)))
    # All Boolean functions on n<=3: constants, dictators, parity, near constants,
    # bent signs, and majority are included, without symmetry reduction.
    for n in range(0,2 if pilot else 4):
        for mask in range(1<<(1<<n)):
            v=tuple(1 if mask>>t&1 else -1 for t in range(1<<n));p=spectrum(v);ck(sum(p)==1)
            if n<=2:ck(p==direct(v))
            a=1-p[0]
            if not a:
                ck(CE(p,p)=={});continue
            pi=tuple(z/a for z in p[1:]);N=len(pi)
            targets=[tuple(F(1,N) for _ in pi),tuple(F(int(j==min(range(N),key=lambda i:pi[i]))) for j in range(N))]
            for T in targets:
                for c in (F(1,4),F(1,2),F(3,4)):
                    l=tuple(c*z for z in T);x,k=projection(pi,l)
                    ck(k>0 and sum(x)==1);ck(all(xx>=ll and (not pp or xx>0) for xx,ll,pp in zip(x,l,pi)))
                    if n<=2:ck(enumerate_projection(pi,l)=={x})
                    g=tuple(pp/xx if pp else F(0) for pp,xx in zip(pi,x))
                    ck(all(gg<=1/k and (xx==ll or gg==1/k) for gg,xx,ll in zip(g,x,l)))
                    # All vertices of the translated simplex certify the exact
                    # first-order objective comparison over EVERY feasible law.
                    for j in range(N):
                        vertex=tuple(ll+(1-c if i==j else 0) for i,ll in enumerate(l))
                        ck(sum(gg*(yy-xx) for gg,yy,xx in zip(g,vertex,x))<=0)
                    for s in (F(1),F(1,2)):
                        M=tuple(pp/2+F(1,2*N) for pp in pi)
                        r=tail_reference(s*p[0],s*a,M);new=tail_reference(s*p[0],s*a,x)
                        delta=add((1,CE(p,new)),(-1,CE(p,r)))
                        ck(sum(r)==sum(new)==s and new[0]==r[0])
                        ck(delta==add((a,KL(pi,x)),(-a,KL(pi,M))))
                        # Explicit SAME-owner algebra, both sibling bills and old U.
                        sibling=CE(p,r);U=logq(F(3,2));B=add((1,CE(p,r)),(1,sibling),(1,U),(1,logq(F(2))))
                        before=add((1,B),(-1,CE(p,r)),(-1,sibling),(-1,U))
                        after=add((1,B),(-1,CE(p,new)),(-1,sibling),(-1,U))
                        ck(after==add((1,before),(-1,delta)))
                    ghost+=sum(pp==0 and ll>0 for pp,ll in zip(pi,l));cases+=1
            ck(time.perf_counter()-start<55)
    out={'status':'PASS','pilot':pilot,'exact_assertions':COUNT,'projection_cases':cases,'required_ghost_floors':ghost,'seconds':time.perf_counter()-start,'reviews_and_witness':source_reviews,'arithmetic':'Fraction/integer FWHT, independent direct characters, prime-log identities, exact KKT vertex signs, rational atanh intervals','scope':'Finite certificates plus written all-finite-law proof; full FEI OPEN'}
    (RUN/'out'/('PILOT.json' if pilot else 'CHECK.json')).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:out[k] for k in ['status','pilot','exact_assertions','projection_cases','required_ghost_floors','seconds']}))
if __name__=='__main__':run('--pilot' in sys.argv)
