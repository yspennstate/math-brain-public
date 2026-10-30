"""Independent direct DFT and actual assignment enumeration; no production imports."""
from fractions import Fraction as F
from pathlib import Path
from functools import lru_cache
from itertools import product
from collections import Counter
import json,time
R=Path(__file__).resolve().parents[1]; start=time.perf_counter(); tests=0
def ck(v):
    global tests
    tests+=1
    assert v,tests
def plus(*es):
    out={}
    for e in es:
        for p,c in e.items():out[p]=out.get(p,F(0))+c
    return {p:c for p,c in out.items() if c}
def times(e,c):return {p:c*v for p,v in e.items() if c*v}
def const(c):return {2:F(c)} if c else {}
def factor(n):
    out={}; p=2
    while n>1:
        while n%p==0:out[p]=out.get(p,0)+1;n//=p
        p+=1
    return out
@lru_cache(None)
def fourier(f):
    return tuple(sum(v*(-1 if (j&s).bit_count()%2 else 1) for j,v in enumerate(f)) for s in range(len(f)))
@lru_cache(None)
def entropy(f):
    n=len(f).bit_length()-1; out={}
    for a,c in Counter(abs(v) for v in fourier(f)).items():
        if a:
            w=F(c*a*a,len(f)**2)
            out=plus(out,const(2*n*w),times(factor(a),-2*w))
    return out
@lru_cache(None)
def influences(f):
    return tuple(F(sum(v!=f[j^(1<<i)] for j,v in enumerate(f)),len(f)) for i in range(len(f).bit_length()-1))
def influence(f):return sum(influences(f),F(0))
@lru_cache(None)
def bounds_log(p):
    x=F(p); k=0
    while x>=2:x/=2;k+=1
    while x<1:x*=2;k-=1
    def s(z):
        q=sum((2*z**(2*j+1)/F(2*j+1) for j in range(48)),F(0)); return q,q+2*z**97/(97*(1-z*z))
    a,b=s((x-1)/(x+1)); c,d=s(F(1,3)); return k+a/d,k+b/c
def lower(e):return sum((v*bounds_log(p)[0 if v>0 else 1] for p,v in e.items()),F(0))
def truth(fix,label=None):
    names=['y0','y1','y2','y3','z']+([] if label is not None else ['A','B'])
    free=[x for x in names if x not in fix]; table=[]
    for row in range(1<<len(free)):
        v=dict(fix);v.update({s:(row>>j)&1 for j,s in enumerate(free)})
        g=(-1)**(v['z']+v['y0']*v['y1']+v['y2']*v['y3'])
        k=label if label is not None else (0 if v['A'] else (1 if v['B'] else 2))
        y=sum(v['y'+str(i)]*(1<<i) for i in range(4))
        if not v['x'] and k and y==k-1:g=-g
        table.append(g)
    return tuple(table),free
def node(fix):
    ctrl=[x for x in ['A','B'] if x not in fix]; pi=[F(0)]*3
    for row in range(1<<len(ctrl)):
        a=dict(fix);a.update({s:(row>>j)&1 for j,s in enumerate(ctrl)})
        k=0 if a['A'] else (1 if a['B'] else 2);pi[k]+=F(1,1<<len(ctrl))
    cores=[truth(fix,k)[0] for k in range(3)]; f,free=truth(fix)
    it=sum(p*influence(g) for p,g in zip(pi,cores));ht={}
    for p,g in zip(pi,cores):ht=plus(ht,times(entropy(g),p))
    hh=entropy(f);ll=plus(hh,times(ht,-1));ss=plus(const(8*it),times(ht,-1))
    rr=sum((2*pi[j]*pi[k]*influence(tuple(a*b for a,b in zip(cores[j],cores[k]))) for j in range(3) for k in range(j+1,3)),F(0))
    return {'H':hh,'L':ll,'S':ss,'R':rr,'IT':it,'f':f,'free':free}
roots=[node({'x':x}) for x in (0,1)]
S0=times(plus(*(v['S'] for v in roots)),F(1,2));L0=times(plus(*(v['L'] for v in roots)),F(1,2));H0=times(plus(*(v['H'] for v in roots)),F(1,2));delta=F(1,16);U=2*delta
orders=[['y0','y1','y2','y3','A','B'],['B','y3','A','y0','y2','y1']];results=[]
for order in orders:
    for depth in range(7):
        pd=pc=F(0)
        for k in range(depth):
            for x in (0,1):
                for values in product((0,1),repeat=k):
                    fix={'x':x};fix.update(dict(zip(order[:k],values)));v=node(fix)
                    d=influences(v['f'])[v['free'].index(order[k])]*F(1,2**(k+1))
                    if order[k].startswith('y'):pd+=d
                    else:pc+=d
        ss=hh=ll={};rr=F(0)
        for x in (0,1):
            for values in product((0,1),repeat=depth):
                fix={'x':x};fix.update(dict(zip(order[:depth],values)));v=node(fix);w=F(1,2**(depth+1))
                ss=plus(ss,times(v['S'],w));hh=plus(hh,times(v['H'],w));ll=plus(ll,times(v['L'],w));rr+=w*v['R']
        ee=plus(const(10*(pd+pc)),times(H0,-1),hh);a=plus(ss,ee)
        rhs=plus(S0,const(2*pd+10*pc),times(L0,-1),ll)
        ck(not plus(a,times(rhs,-1)))
        ck(lower(plus(a,const(-rr-U),times(S0,-F(71,78)),const(-2*pd-10*pc)))>=0)
        if order[0]=='y0' and depth==4:
            ck(not plus(ss,const(-8)))
            ck(lower(plus(ee,L0,const(-16)))>=0)
        results.append({'order':order,'depth':depth,'Pi_D':str(pd),'Pi_C':str(pc),'bank':str(rr),'remaining_capacity_lower':str(lower(plus(a,const(-rr-U))))})
for m in (44,46):
    diff=F(m,16)-F(17,8)-F(2,3)
    ck((diff>0)==(m==46))
out={'status':'PASS','assertions':tests,'cut_cases':len(results),'rows':results,'seconds':time.perf_counter()-start,'arithmetic':'independent direct DFT, rational prime-log identities,48-term intervals'}
(R/'out/REPLAY.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8',newline='')
print(json.dumps({k:out[k] for k in ['status','assertions','cut_cases','seconds']}))
