"""Frozen A097-reference-lift-v1. Exact identities, not floating signs."""
from fractions import Fraction as F
from collections import defaultdict
from pathlib import Path
import json, time

ROOT=Path(__file__).resolve().parents[1]
checks=0
def check(a,b):
    global checks
    checks+=1
    assert a==b,(a,b)

def add(*vs):
    d=defaultdict(F)
    for v in vs:
        for k,a in v.items(): d[k]+=a
    return {k:a for k,a in d.items() if a}
def scale(v,t): return {k:a*t for k,a in v.items() if a*t}
def log(q):
    assert q>0
    d={}
    for x,sgn in [(q.numerator,1),(q.denominator,-1)]:
        p=2
        while p*p<=x:
            while x%p==0:
                d[p]=d.get(p,0)+sgn;x//=p
            p+=1
        if x>1:d[x]=d.get(x,0)+sgn
    return {k:F(a) for k,a in d.items() if a}
def ce(p,q): return add(*(scale(log(q[k]),-a) for k,a in p.items() if a))
def ent(p):return ce(p,p)
def kl(p,q):return add(ce(p,q),scale(ent(p),-1))
def spec(values,coords):
    ans={}
    for s in range(1<<len(coords)):
        m=sum(1<<coords[j] for j in range(len(coords)) if s>>j&1)
        a=F(sum(v*(-1 if (s&x).bit_count()%2 else 1) for x,v in enumerate(values)),len(values))
        ans[m]=a
    return ans
def influence(p):return sum((m.bit_count()*a for m,a in p.items()),F(0))

def rec(values,coords,cut,mode,path=()):
    a=spec(values,coords);p={s:v*v for s,v in a.items()}
    check(sum(p.values()),F(1))
    infl={i:sum((v for s,v in p.items() if s>>i&1),F(0)) for i in coords}
    if len(coords)<=cut or not any(infl.values()):
        if mode==0: q={s:F(1,1<<len(coords)) for s in p}
        else:
            rho=F(2+(sum(y for _,y in path)%2),5)
            mass=F(1,2+len(path)%3)
            q={s:mass*rho**s.bit_count()*(1-rho)**(len(coords)-s.bit_count()) for s in p}
        pp={(s,path):v for s,v in p.items()}
        qq={(s,path):v for s,v in q.items()}
        return dict(p=p,q=q,pp=pp,qq=qq,B={},J={},K={},leafH=ent(p),leafCE=ce(p,q),leafKL=kl(p,q),removed=F(0),leafI=influence(p),depth=F(0))
    i=min((i for i in coords if infl[i]>0),key=lambda i:(infl[i],i))
    j=coords.index(i);childcoords=tuple(x for x in coords if x!=i)
    ch=[]
    for y in range(2):
        vals=[]
        for x in range(1<<len(childcoords)):
            old=(x&((1<<j)-1)) | (y<<j) | ((x>>j)<<(j+1))
            vals.append(values[old])
        ch.append(rec(vals,childcoords,cut,mode,path+((i,y),)))
    mix={t:(ch[0]['p'][t]+ch[1]['p'][t])/2 for t in ch[0]['p']}
    refmix={t:(ch[0]['q'][t]+ch[1]['q'][t])/2 for t in ch[0]['p']}
    q={};pp=defaultdict(F);qq=defaultdict(F)
    B={};K={}
    for t,w in mix.items():
        check(w,p[t]+p[t|(1<<i)])
        theta=[p[t]/w,p[t|(1<<i)]/w] if w else [F(1,2),F(1,2)]
        if w:
            B=add(B,scale(ent(dict(enumerate(theta))),w))
            kp={y:ch[y]['p'][t]/(2*w) for y in range(2)}
            kq={y:ch[y]['q'][t]/(2*refmix[t]) for y in range(2)}
            K=add(K,scale(kl(kp,kq),w))
        for z in range(2):
            s=t|(z<<i);q[s]=refmix[t]*theta[z]
            for y in range(2):
                for (tc,l),v in ch[y]['pp'].items():
                    if tc==t:pp[s,l]+=v*theta[z]/2
                for (tc,l),v in ch[y]['qq'].items():
                    if tc==t:qq[s,l]+=v*theta[z]/2
    J=add(ent(mix),scale(add(ent(ch[0]['p']),ent(ch[1]['p'])),-F(1,2)))
    check(ce(p,q),add(B,J,scale(add(ce(ch[0]['p'],ch[0]['q']),ce(ch[1]['p'],ch[1]['q'])),F(1,2)),scale(K,-1)))
    out=dict(p=p,q=q,pp=dict(pp),qq=dict(qq))
    for k,v in [('B',B),('J',J),('K',K)]:out[k]=add(v,scale(add(ch[0][k],ch[1][k]),F(1,2)))
    for k in ['leafH','leafCE','leafKL']:out[k]=scale(add(ch[0][k],ch[1][k]),F(1,2))
    out['removed']=infl[i]+(ch[0]['removed']+ch[1]['removed'])/2
    out['leafI']=(ch[0]['leafI']+ch[1]['leafI'])/2
    out['depth']=1+(ch[0]['depth']+ch[1]['depth'])/2
    return out

start=time.perf_counter();cases=0;positive_K=0;positive_terminal_H=0
for n in range(4):
    for mask in range(1<<(1<<n)):
        values=[1 if mask>>x&1 else -1 for x in range(1<<n)]
        for cut in range(3):
            for mode in range(2):
                r=rec(values,tuple(range(n)),cut,mode);cases+=1
                p,q,pp,qq=(r[k] for k in ['p','q','pp','qq'])
                for s in p:
                    check(sum((v for (t,l),v in pp.items() if t==s),F(0)),p[s])
                    check(sum((v for (t,l),v in qq.items() if t==s),F(0)),q[s])
                for l in set(l for s,l in pp):
                    check(sum((v for (s,ll),v in pp.items() if ll==l),F(0)),F(1,1<<len(l)))
                assert sum(q.values())<=1
                check(ent(p),add(r['B'],r['J'],r['leafH']))
                check(ce(p,q),add(r['B'],r['J'],r['leafCE'],scale(r['K'],-1)))
                check(kl(p,q),add(r['leafKL'],scale(r['K'],-1)))
                check(kl(pp,qq),r['leafKL'])
                post={}
                for s,v in p.items():
                    if not v:continue
                    pl={l:x/v for (t,l),x in pp.items() if t==s}
                    ql={l:x/q[s] for (t,l),x in qq.items() if t==s}
                    post=add(post,scale(kl(pl,ql),v))
                check(post,r['K'])
                check(ent(pp),add({2:r['depth']} if r['depth'] else {},r['B'],r['leafH']))
                check(influence(p),r['removed']+r['leafI'])
                positive_K+=bool(r['K']);positive_terminal_H+=bool(r['leafH'])
elapsed=time.perf_counter()-start
assert elapsed<60
result=dict(helper_version='A097-reference-lift-v1',cases=cases,exact_assertions=checks,failures=0,nonzero_posterior_KL_cases=positive_K,nonzero_terminal_entropy_cases=positive_terminal_H,runtime_seconds=elapsed,arithmetic='Fraction plus symbolic log2-prime coefficient vectors',all_dimensional_proof='REPORT.md and CROSS_ROUTE_SUBSTITUTION.tex')
(ROOT/'out').mkdir(exist_ok=True)
(ROOT/'out'/'EXACT_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
