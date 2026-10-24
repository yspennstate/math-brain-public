"""No import of main checker/helper. Direct characters and independent KL expansion."""
from fractions import Fraction as Q
from pathlib import Path
from functools import lru_cache
from collections import defaultdict
import json,time
ROOT=Path(__file__).resolve().parents[1]; START=time.monotonic(); checks=nodes=leaves=0

def ck(v):
    global checks
    assert v;checks+=1

def add(*terms):
    z=defaultdict(Q)
    for term in terms:
        for k,v in term.items(): z[k]+=v
    return {k:v for k,v in z.items() if v}

def mul(term,c): return {k:v*c for k,v in term.items() if v*c}
def difference(a,b): return add(a,mul(b,-1))
def mean(a,b): return mul(add(a,b),Q(1,2))

@lru_cache(None)
def log(q):
    result=defaultdict(Q)
    for N,sgn in [(q.numerator,1),(q.denominator,-1)]:
        d=2
        while d*d<=N:
            while N%d==0:result[d]+=sgn;N//=d
            d+=1
        if N>1:result[N]+=sgn
    return dict(result)

def D(p,r):
    ck(sum(p)==sum(r)==1)
    return add(*(mul(log(x/y),x) for x,y in zip(p,r) if x))

def H(p): return add(*(mul(log(x),-x) for x in p if x))

@lru_cache(None)
def coefficients(t):
    return tuple(sum(((-1)**((s&x).bit_count())*v for x,v in enumerate(t)),Q())/len(t) for s in range(len(t)))

def law(t):return tuple(x*x for x in coefficients(t))

def ids(n,i,b):
    return [x for x in range(n) if ((x>>i)&1)==b]

def child(t,i,b): return tuple(t[x] for x in ids(len(t),i,b))

def joint(t,r,i):
    aa=coefficients(t); js=[[],[]]
    lo=ids(len(t),i,0)
    for s in lo:
        u,v=aa[s],aa[s|(1<<i)]
        mass=r[s]+r[s|(1<<i)]
        for b in [0,1]:
            prob=(u+(-1)**b*v)**2/(2*(u*u+v*v)) if u or v else Q(1,2)
            js[b].append(mass*prob)
    branch=[sum(row) for row in js]
    ck(sum(branch)==1 and min(branch)>0)
    rr=[tuple(x/branch[b] for x in js[b]) for b in [0,1]]
    Er={}
    # Independent conditional decomposition of the erasure KL.
    pp=law(t)
    for s in lo:
        sp=pp[s]+pp[s|(1<<i)];sr=r[s]+r[s|(1<<i)]
        if sp:
            Er=add(Er,mul(D((pp[s]/sp,pp[s|(1<<i)]/sp),(r[s]/sr,r[s|(1<<i)]/sr)),sp))
    O=D((Q(1,2),Q(1,2)),tuple(branch))
    ck(not difference(D(pp,r),add(Er,O,mean(*(D(law(child(t,i,b)),rr[b]) for b in [0,1])))))
    return rr,Er,O

def state(a,g,h,rg,rh):
    p=Q(a.count(-1),len(a))
    f=tuple((g if y==1 else h)[x] for x in range(len(g)) for y in a)
    pf=law(f);pg=law(g);ph=law(h);q=[];r=[];rf=[]
    for t in range(len(g)):
        qt=(1-p)*pg[t]+p*ph[t];rt=(1-p)*rg[t]+p*rh[t]
        q.append(qt);r.append(rt)
        row=pf[t*len(a):(t+1)*len(a)];ck(sum(row)==qt)
        rf.extend(rt*x/qt if qt else (rt if u==0 else Q()) for u,x in enumerate(row))
    debt=D(pf,tuple(rf));ck(not difference(debt,D(tuple(q),tuple(r))))
    w=add(mul(D(pg,rg),1-p),mul(D(ph,rh),p));z=difference(w,debt)
    return dict(p=p,f=f,rf=tuple(rf),debt=debt,w=w,z=z,h=H(pf))

def walk(a,g,h,rg,rh,labels,order,history,policy):
    global nodes,leaves
    nodes+=1;s=state(a,g,h,rg,rh)
    if not labels or (policy==1 and len(history)>=3 and (sum(history)%2==0)):
        leaves+=1
        return dict(sig={},A={},zl=s['z'],path={},ce=add(s['h'],s['debt']),debt=s['debt'])
    # Second policy chooses next priority according to the observed history.
    priorities=order if policy==0 or sum(history)%2==0 else tuple(reversed(order))
    label=next(x for x in priorities if x in labels);i=labels.index(label)
    na=len(a).bit_length()-1
    rs,Ef,Of=joint(s['f'],s['rf'],i)
    if i<na:
        args=[(child(a,i,b),g,h,rg,rh) for b in [0,1]]
    else:
        j=i-na
        rgg,Eg,Og=joint(g,rg,j);rhh,Eh,Oh=joint(h,rh,j)
        args=[(a,child(g,j,b),child(h,j,b),rgg[b],rhh[b]) for b in [0,1]]
    kids=[state(*ar) for ar in args]
    A=difference(s['w'],mean(*(v['w'] for v in kids)))
    sigma=difference(mean(*(v['debt'] for v in kids)),s['debt'])
    ck(not difference(sigma,add(s['z'],mul(mean(*(v['z'] for v in kids)),-1),mul(A,-1))))
    raw=difference(mean(*(v['debt'] for v in kids)),mean(*(D(law(child(s['f'],i,b)),rs[b]) for b in [0,1])))
    ck(not difference(raw,add(sigma,Ef,Of)))
    if i<na: ck(not A)
    else: ck(not difference(A,add(mul(add(Eg,Og),1-s['p']),mul(add(Eh,Oh),s['p']))))
    remaining=labels[:i]+labels[i+1:]
    ret=[walk(*args[b],remaining,order,history+(b,),policy) for b in [0,1]]
    out={k:mean(*(v[k] for v in ret)) for k in ret[0]}
    out['sig']=add(sigma,out['sig']);out['A']=add(A,out['A'])
    out['path']=add(difference(s['h'],mean(*(v['h'] for v in kids))),out['path'])
    ck(not difference(add(out['sig'],out['A'],out['zl']),s['z']))
    ck(not difference(add(out['path'],out['ce'],out['A'],out['zl']),add(s['h'],s['w'])))
    return out

a=tuple(-1 if x<3 else 1 for x in range(8))
g=tuple((-1 if x&3==0 else 1)*(-1 if x&4 else 1) for x in range(8))
h=tuple(-1 if x.bit_count()>=2 else 1 for x in range(8))
pg=law(g);ph=law(h);rg=tuple((x+Q(1,8))/2 for x in pg);rh=tuple(Q(1,8) for x in ph)
labels=('c0','c1','c2','d0','d1','d2')
order=('c0','d0','c1','d1','c2','d2')
reports=[]
for policy in [0,1]:
    before=(nodes,leaves,checks)
    answer=walk(a,g,h,rg,rh,labels,order,(),policy)
    reports.append(dict(policy=policy,nodes=nodes-before[0],leaves=leaves-before[1],assertions=checks-before[2],ledger={k:{str(x):str(y) for x,y in v.items()} for k,v in answer.items()}))
out=dict(status='PASS',representation='direct characters; conditional-label erasure; independent prime-log algebra',nodes=nodes,leaves=leaves,assertions=checks,seconds=time.monotonic()-START,policies=reports)
(ROOT/'out/independent.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k!='policies'}))
