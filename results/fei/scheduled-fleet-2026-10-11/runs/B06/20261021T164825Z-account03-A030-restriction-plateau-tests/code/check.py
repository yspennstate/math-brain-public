"""Frozen exact tests for equal-mean controller collapse; no floating sign tests."""
from pathlib import Path
from fractions import Fraction as F
from itertools import product
from collections import Counter
from functools import lru_cache
import json, time, hashlib, sys
ROOT=Path(__file__).resolve().parents[1]
OLD=ROOT.parents[1]/'runs/20261013T212321Z-account05-A030-restriction-plateau-tests/code/check.py'
ns={'__file__':str(OLD)}
exec(OLD.read_text(encoding='utf-8').split('for n in (1,2,3):')[0],ns)
expr,add,const,child,reserve,positive,walsh=[ns[k] for k in ('expr','add','const','child','reserve','positive','walsh')]
ZERO=(); start=time.perf_counter(); pilot='--pilot' in sys.argv; limit=55 if pilot else 300
checks=0
def ck(v):
    global checks
    checks+=1
    assert v,checks
    assert time.perf_counter()-start<limit,'frozen runtime guard'
@lru_cache(None)
def phi(s):
    if not s:return ZERO
    d={}
    for p,e in ns['factors'](s.denominator).items():d[p]=s*e
    for p,e in ns['factors'](s.numerator).items():d[p]=d.get(p,F(0))-s*e
    return expr(d)
@lru_cache(None)
def L(q):return add((1,phi(q*q)),(-F(1,4),phi((1-2*q)**2)),(1,const(2*q*(1-q))))
@lru_cache(None)
def entropy(t):
    den=len(t)**2
    return add(*((count,phi(F(v*v,den))) for v,count in Counter(abs(x) for x in walsh(t) if x).items()))
def mean(t):return F(sum(t),len(t))
def cuts(labels):return tuple(tuple(-1 if x==j else 1 for x in labels) for j in range(3))
def qs(labels):return tuple(F(labels.count(j),len(labels)) for j in range(3))
def mix(labels,cores):
    n=len(labels).bit_length()-1; dims=[len(t).bit_length()-1 for t in cores]
    offsets=[n,n+dims[0],n+dims[0]+dims[1]]
    return tuple(cores[labels[x&(len(labels)-1)]][(x>>offsets[labels[x&(len(labels)-1)]])&(len(cores[labels[x&(len(labels)-1)]])-1)] for x in range(1<<(n+sum(dims))))
def rhs(labels,cores):
    m=mean(cores[0]);V=1-m*m;q=qs(labels);h=cuts(labels)
    return add(*[(q[j],entropy(cores[j])) for j in range(3)],*[(V/4,entropy(t)) for t in h],*[(V,L(x)) for x in q])
def rarity(labels,m):return add(*((1-m*m,phi(q)) for q in qs(labels)))
def dec(t,i):return add((1,entropy(t)),(-F(1,2),entropy(child(t,i,0))),(-F(1,2),entropy(child(t,i,1))))
def edge(labels,i):
    a,b=child(labels,i,0),child(labels,i,1)
    return F(sum(x!=y for x,y in zip(a,b)),len(a))
def encode(x):return [[p,str(c)] for p,c in x]
def positive_bound(x):return [str(q) for q in ns['bounds'](x)]
PD=(1,1,1,-1)
fixtures=[(PD,PD,PD),((1,1,-1,1),PD,(1,-1,1,1)),((-1,-1,-1,1),(-1,1,-1,-1),(1,-1,-1,-1))]
tables=[(0,0,0,1,1,2,2,2),(0,0,1,2,0,1,2,2),(0,1,2,0,1,2,0,1),(0,0,0,0,1,1,2,2),(0,1,1,2,2,2,2,2),(0,0,0,0,0,0,1,2)]
domain=tables if pilot else (t for t in product(range(3),repeat=8) if len(set(t))==3)
best=ZERO;best_record=None;roots=faces=direct=0;witness=None
for labels in domain:
    cs=fixtures if pilot else [(PD,PD,PD)]
    for cores in cs:
        m=mean(cores[0]);V=1-m*m;h=cuts(labels);f=None
        ck(all(mean(t)==m for t in cores))
        # Actual raw full-cube spectrum is checked on every pilot root, the first
        # six main roots, and the six explicit fixtures. Main rest uses the
        # independently derived exact Fourier-sector formula below.
        if pilot or roots<6 or labels in tables:
            f=mix(labels,cores);ck(entropy(f)==rhs(labels,cores));direct+=1
        # Independent sector reconstruction includes empty and nonempty S,T.
        sector=phi(m*m)
        for j in range(3):
            ch=walsh(tuple(int(x==j) for x in labels))
            uh=walsh(cores[j]);dd=F(len(labels)**2*len(cores[j])**2)
            masses=Counter(F(a*a*b*b,dd) for a in ch if a for b in uh[1:] if b)
            sector=add((1,sector),*((count,phi(p)) for p,count in masses.items()))
        ck(sector==rhs(labels,cores))
        for i in range(3):
            lc=[child(labels,i,s) for s in (0,1)];q=qs(labels)
            d=V*edge(labels,i)/2
            release=add((1,rarity(labels,m)),(-F(1,2),rarity(lc[0],m)),(-F(1,2),rarity(lc[1],m)))
            ck(positive(add((-1,release)))==ZERO)
            correction=add(*[(V,L(x)) for x in q],*[(-V/2,L(x)) for t in lc for x in qs(t)],(-1,release))
            actual=add((1,rhs(labels,cores)),(-F(1,2),rhs(lc[0],cores)),(-F(1,2),rhs(lc[1],cores)),*[(-V/4,dec(t,i)) for t in h],(-1,release))
            ck(actual==correction)
            ck(positive(add((1,correction),(-1,const(14*d))))==ZERO)
            ck(sum(abs(qs(lc[0])[j]-q[j]) for j in range(3))<=edge(labels,i))
            if f is not None:
                rawd=F(sum(f[x]!=f[x^(1<<i)] for x in range(len(f))),len(f))
                ck(rawd==d)
                ck(dec(f,i)==add((1,actual),*[(V/4,dec(t,i)) for t in h],(1,release)))
            if d:
                ratio=add((1/d,correction))
                if positive(add((1,ratio),(-1,best))):
                    best=ratio;best_record=dict(labels=labels,query=i,mean=str(m),influence=str(d),E=encode(correction),ratio=encode(ratio),ratio_bounds=positive_bound(ratio))
            # Fixed original cut reserve at C=1, query i then others in order.
            order=(i,)+tuple(j for j in range(3) if j!=i)
            rr=[reserve(t,order,1) for t in h]
            rest=(0,1)
            pc=[add(*((V/4,reserve(t,rest,1)) for t in cuts(lc[s]))) for s in (0,1)]
            P=add(*((V/4,r) for r in rr))
            seedD=add(*((V/4,dec(t,i)) for t in h))
            slack=add((1,const(d)),(1,P),(-F(1,2),pc[0]),(-F(1,2),pc[1]),(-1,seedD))
            ck(positive(add((-1,slack)))==ZERO)
            if positive(correction) and positive(slack) and witness is None:
                witness=dict(labels=labels,query=i,mean=str(m),influence=str(d),E=encode(correction),unused_same_cut_slack=encode(slack),P=encode(P),P_children=[encode(x) for x in pc],R=encode(rarity(labels,m)),R_children=[encode(rarity(t,m)) for t in lc],seed_reserves=[encode(r) for r in rr],actual_terminal_entropies=[encode(entropy(t)) for t in cores])
            faces+=1
        roots+=1
    entropy.cache_clear();ns['stats'].cache_clear();reserve.cache_clear()
# Explicit endpoint/assumption attacks, including unequal means.
boundaries=[]
for mcore in [(1,),(-1,),(1,-1),PD]:
    labels=tables[1];cores=(mcore,)*3;f=mix(labels,cores)
    ck(entropy(f)==rhs(labels,cores));boundaries.append(str(mean(mcore)))
unequal=(PD,(1,-1),(1,));bad=mix(tables[1],unequal)
ck(entropy(bad)!=rhs(tables[1],unequal))
# Rational constants in derivative estimate: ln2>=2/3, e>=8/3 imply
# (6/e+1)/ln2+2 <=55/8 <7; no numerical approximation used.
ck((6*F(3,8)+1)*F(3,2)+2==F(55,8));ck(F(55,8)<7)
out=dict(status='PASS',pilot=pilot,helper_version='A030-equal-mean-controller-v1',roots=roots,faces=faces,direct_full_walsh_roots=direct,checks=checks,maximum=best_record,positive_slack_witness=witness,boundary_means=boundaries,unequal_mean_identity_countercontrol=True,certified_sign_decisions=ns['signs'],exact_zero_decisions=ns['zeros'],elapsed_seconds=time.perf_counter()-start,source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),helper_sha256=hashlib.sha256(OLD.read_bytes()).hexdigest())
(ROOT/'out'/('PILOT.json' if pilot else 'VALIDATION.json')).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k not in ['positive_slack_witness','maximum']},indent=2))
