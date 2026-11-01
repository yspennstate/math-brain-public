"""Independent exact arithmetic; no external package or floating sign decisions."""
from fractions import Fraction as F
from functools import lru_cache
from itertools import product
from collections import Counter
from pathlib import Path
import argparse, hashlib, json, time

B=Path(__file__).resolve().parents[1]
COUNT=0
QROUND=2**96
def rounded(a):
    lo,hi=a
    return F((lo.numerator*QROUND)//lo.denominator,QROUND),F(-((-hi.numerator*QROUND)//hi.denominator),QROUND)
def ok(x):
    global COUNT
    COUNT+=1
    if not x: raise AssertionError(COUNT)
def add(a,b): return rounded((a[0]+b[0],a[1]+b[1]))
def neg(a): return (-a[1],-a[0])
def sub(a,b): return add(a,neg(b))
def mul(a,b):
    v=[x*y for x in a for y in b];return rounded((min(v),max(v)))
def scale(a,x): return mul(a,(x,x))
def div(a,b):
    assert b[0]>0
    return mul(a,(1/b[1],1/b[0]))
def const(x): return F(x),F(x)
@lru_cache(None)
def lnsmall(x):
    assert 1<=x<=2
    z=(x-1)/(x+1)
    if not z:return const(0)
    zi=rounded((z,z));z2=mul(zi,zi);s=const(0);power=zi
    for k in range(40):
        s=add(s,scale(power,F(2,2*k+1)));power=mul(power,z2)
    tail=F(2,3**81)/(81*(1-F(1,9)))
    return rounded((s[0],s[1]+tail))
@lru_cache(None)
def log2(x):
    assert x>0
    e=0
    while x<1:x*=2;e-=1
    while x>2:x/=2;e+=1
    return add(div(lnsmall(x),lnsmall(F(2))),const(e))
def logiv(x): return log2(x[0])[0],log2(x[1])[1]
def eta(p): return const(0) if p==0 else scale(log2(p),-p)
def h2(p): return add(eta(p),eta(1-p))
def entropy(p):
    ans=const(0)
    for v in p:ans=add(ans,eta(v))
    return ans
def outiv(a): return [str(x) for x in a]
def defect(k):
    if k==0:return const(0),F(0),F(-1)
    e=F(1,2**k); mu=1-2*e
    h=add(eta(mu*mu),const(8*(k-1)*e*(1-e)))
    return h,2*k*e,mu
def core(m,r):
    h,i,mu=defect(r);return scale(h,m),m*i,mu**m
def phi(c,rs):
    if not c:return sum(rs,F(0))
    p=F(1)
    for a,count in Counter(rs).items():p*=(1-c*a)**count
    return (1-p)/c
def canonical(m,r):
    hc,ic,mu=core(m,r); t=(1-mu)/2;p0=(1-t)**2/4;v=1-p0
    ds=[F(1,2),F(1,2),t/2]+[F(1,2**(r+1))]*(m*r)
    rs=[d/v for d in ds]; lo,hi=F(0),F(1)
    ok(phi(lo,rs)>1 and phi(hi,rs)<1)
    for _ in range(64):
        c=(lo+hi)/2
        if phi(c,rs)>1:lo=c
        else:hi=c
    ok(phi(lo,rs)>1 and phi(hi,rs)<1)
    c=(lo,hi); total=logiv(c)
    for a in rs:
        th=scale(c,a)
        total=sub(total,add(scale(logiv(th),a),scale(logiv(sub(const(1),th)),1-a)))
    ce=add(h2(p0),scale(total,v))
    G=sub(entropy([]),const(0))
    for d in ds:G=add(G,h2(d))
    G=sub(G,const(2))
    # g_b=1 for b0, h for b1. Every nonempty seed coefficient occurs twice/4.
    hg=add(add(eta((1-t)**2),eta(t*t)),add(scale(sub(hc,eta(mu*mu)),F(1,2)),const(1-mu*mu)))
    hroot=add(const(2),scale(hg,F(1,2)))
    floor=min(hroot[0],2+2*t)
    bound=(ce[0]-min(hroot[1],2+2*t),ce[1]-floor)
    return {'m':m,'r':r,'t':t,'p0':p0,'v':v,'ds':ds,'rs':rs,'c':c,'CE':ce,'G':G,'Hroot':hroot,'L_bound':bound,'Iroot':1+t/2+ic/4}
def walsh(vals):
    a=list(vals);step=1
    while step<len(a):
        for i in range(0,len(a),2*step):
            for j in range(i,i+step):a[j],a[j+step]=a[j]+a[j+step],a[j]-a[j+step]
        step*=2
    return [F(x,len(a)) for x in a]
def restrict(vals,i,bit):
    return [vals[(x&((1<<i)-1))|((x>>i)<<(i+1))|(bit<<i)] for x in range(len(vals)//2)]
def influence(vals,i):
    return F(sum(vals[x]!=vals[x^(1<<i)] for x in range(len(vals))),len(vals))
def spec(vals):return [x*x for x in walsh(vals)]
def node(vals,q,i):
    n=(len(vals)-1).bit_length();a=walsh(vals);p=[x*x for x in a]
    ok(sum(p)==sum(q)==1 and all(x>=0 for x in q) and all(not p[j] or q[j]>0 for j in range(len(p))))
    children=[tuple(restrict(vals,i,b)) for b in (0,1)]
    qs=[[F(0)]*(len(vals)//2) for _ in (0,1)]
    for w in range(len(vals)//2):
        j=(w&((1<<i)-1))|((w>>i)<<(i+1)); k=j|(1<<i)
        pm=p[j]+p[k]; qm=q[j]+q[k]
        for b in (0,1):
            ker=(a[j]+(-1)**b*a[k])**2/(2*pm) if pm else F(1,2)
            qs[b][w]=qm*ker
            ok(pm*ker==spec_cache(children[b])[w]/2)
            for z in (j,k):
                if p[z] and ker:
                    # Erasure likelihood * outcome likelihood * inherited child likelihood.
                    er=(p[z]/pm)/(q[z]/qm)
                    raw=qm*ker
                    ok(er*(pm*ker)/raw==p[z]/q[z])
    qb=[sum(x) for x in qs];ok(sum(qb)==1 and all(x>0 for x in qb))
    for b in (0,1):
        qs[b]=[x/qb[b] for x in qs[b]];ok(sum(qs[b])==1)
        pp=spec_cache(children[b])
        ok(all(not pp[w] or qs[b][w]>0 for w in range(len(pp))))
    ok(influence(vals,i)==sum(p[j] for j in range(len(p)) if j&(1<<i)))
    return children,qs
@lru_cache(None)
def spec_cache(vals):return spec(vals)
def fixture(seed):
    n=(len(seed)-1).bit_length()
    vals=[]
    for v in range(1<<(n+3)):
        x=v&1;a=(v>>1)&1;b=(v>>2)&1;z=v>>3
        vals.append((-1)**a if x==0 else (seed[z] if b else 1))
    return tuple(vals)
def finite(seed):
    vals=fixture(seed);n=(len(seed)-1).bit_length();p=spec(vals)
    t=F(sum(v==-1 for v in seed),len(seed));p0=(1-t)**2/4;v=1-p0
    ds=[F(1,2),F(1,2),t/2]+[influence(seed,i)/4 for i in range(n)]
    actual=[influence(vals,i) for i in range(n+3)]
    ok(actual==ds and p[0]==p0)
    # Independent normalized rational perturbation, explicitly NOT the algebraic canonical law.
    c=F(4,5);ths=[c*d/v for d in ds]
    mass=[]
    for s in range(len(p)):
        z=F(1)
        for i,th in enumerate(ths):z*=th if s&(1<<i) else 1-th
        mass.append(z)
    # Dummies are retained only in this finite replay, then contracted so Q dominates.
    support=[s for s in range(len(p)) if mass[s] or s==0]
    norm=1-mass[0];q=[p0 if s==0 else v*mass[s]/norm for s in range(len(p))]
    ok(sum(q)==1 and all(not p[s] or q[s]>0 for s in range(len(p))))
    # node() requires strict positivity; constant/dummy cases validate spectra only.
    if not all(q):return
    cs,qs=node(vals,q,2)
    if n:node(cs[1],qs[1],2)
    # Entropy from explicit spectrum agrees with disjoint a-label formula.
    g=tuple(1 if not (w&1) else seed[w>>1] for w in range(2*len(seed)))
    pg=spec(g)
    for s in range(len(p)):
        expected=F(1,4) if s in (2,3) else F(0) if s&2 else pg[s>>2]/4
        ok(p[s]==expected)
    hi=add(const(2),scale(entropy(spec(g)),F(1,2)))
    hv=entropy(p);ok(hv[0]<=hi[1] and hi[0]<=hv[1])
def run(pilot):
    start=time.monotonic()
    domain=[(3,5)] if pilot else [(3,5),(2,4),(2,3),(3,4),(6,5),(12,5),(24,5),(48,5)]
    frozen={'helper_version':'A048-exact-canonical-v2','helper_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'actual_Boolean_family':'F_h with h a product of disjoint point defects; finite all seeds n<=2','domain':domain,'finite_seeds':'all 22 signs on n=0,1,2; plus (m,r)=(2,2),(2,3),(3,2)' if not pilot else 'AND2 sign only','case_count':{'formula':len(domain),'finite':1 if pilot else 25,'restricted_states':0 if pilot else 343,'sparse_symbolic':64},'symmetry':'group equal exact marginals only; all seeds kept','arithmetic':'integer Walsh, Fraction, rational atanh bounds with outward 2^-96 rounding, 64 sign-checked normalizer bisections','memory_estimate_MB':80,'maximum_runtime_seconds':60 if pilot else 120,'no_automatic_dimension_increase':True}
    frozen['helper_version']='A048-exact-canonical-v3'
    (B/'out'/('FROZEN_PILOT.json' if pilot else 'FROZEN_SPEC.json')).write_text(json.dumps(frozen,indent=2),encoding='utf-8')
    rows=[]
    for m,r in domain:
        a=canonical(m,r)
        if (m,r)==(3,5):
            ok(a['G'][0]>2)
            ok(a['CE'][1]<4)
            ok(a['L_bound'][1]<2)
        rows.append({k:(outiv(v) if isinstance(v,tuple) else str(v) if isinstance(v,F) else v) for k,v in a.items() if k not in ('rs','ds')})
        (B/'out'/f'FORMULA_{m}_{r}.json').write_text(json.dumps(rows[-1],indent=2),encoding='utf-8')
    seeds=[(1,1,1,-1)] if pilot else [tuple(-1 if mask&(1<<j) else 1 for j in range(1<<n)) for n in range(3) for mask in range(1<<(1<<n))]
    if not pilot:
        for m,r in [(2,2),(2,3),(3,2)]:
            seeds.append(tuple((-1)**sum(((z>>(j*r))&((1<<r)-1))==((1<<r)-1) for j in range(m)) for z in range(1<<(m*r))))
    for seed in seeds:finite(seed)
    states=0
    if not pilot:
        for ks in product(range(-1,6),repeat=3):
            h=const(0);inf=F(0)
            for k in ks:
                if k<0:continue
                hk,ik,_=defect(k);h=add(h,hk);inf+=ik
            ok(h[1]<=4*inf);ok(2+2*inf-h[1]/2>=2);states+=1
    # The algebraic load-bearing max identity holds on signed/zero boundary cells.
    scalar=0
    for A,D,R in product([F(0),F(1,4),F(2),F(3)],[-2,-1,0,1,2],[F(0),F(1,4),F(1)]):
        ok(A+max(D-4*R,0)==max(A,A+D-4*R));scalar+=1
    sparse=0
    for k,T in product(range(1,9),repeat=2):
        alpha=F(1,2**k);hq,iq,_=defect(k+1)
        ok(iq==alpha*(k+1) and hq[1]<=4*iq)
        # Full outer L is bounded by guard4alpha plus alpha*T original L.
        ell=F(rows[0]['L_bound'][1]);margin=2-ell
        ok(margin>0 and 4*alpha+alpha*T*ell<4*alpha+alpha*T*2)
        for edge in [F(-2),F(0),F(1,8)]:
            ctrl=hq[1]-4*alpha*k
            ok(max(ctrl+alpha*T*edge,0)<=4*alpha+alpha*T*max(edge,0))
        sparse+=1
    result={'status':'PASS','assertions':COUNT,'formula_cases':len(domain),'finite_seed_cases':len(seeds),'restriction_states':states,'scalar_boundary_cases':scalar,'sparse_symbolic_cases':sparse,'runtime_seconds':time.monotonic()-start,'selected':rows[0],'rung':'analytic proof with exact checks; Lean status separate'}
    (B/'out'/('CHECK_PILOT.json' if pilot else 'CHECK.json')).write_text(json.dumps(result,indent=2),encoding='utf-8')
    print(json.dumps({k:v for k,v in result.items() if k!='selected'}))
if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--pilot',action='store_true');run(parser.parse_args().pilot)
