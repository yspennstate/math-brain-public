"""Independent explicit FWHT, physical flips and prime-log erasure vectors."""
from pathlib import Path
from fractions import Fraction as Q
from functools import lru_cache
import itertools,json,time,runpy
ROOT=Path(__file__).resolve().parents[1]
hh=runpy.run_path(str(ROOT.parent/'20261014T012528Z-fleet05-A046-current-candidate-intake'/'code'/'layers.py'))
@lru_cache(None)
def factor(n):
    out={};d=2
    while d*d<=n:
        while n%d==0:out[d]=out.get(d,0)+1;n//=d
        d+=1
    if n>1:out[n]=out.get(n,0)+1
    return out
def xlogx(x):
    out={}
    if not x:return out
    for n,sign in ((x.numerator,1),(x.denominator,-1)):
        for p,v in factor(n).items():out[p]=out.get(p,Q(0))+sign*x*v
    return out
def plus(*terms):
    out={}
    for c,term in terms:
        for p,v in term.items():out[p]=out.get(p,Q(0))+c*v
    return {p:v for p,v in out.items() if v}
def psi(a,b):return plus((1,xlogx(a+b)),(-1,xlogx(a)),(-1,xlogx(b)))
def interval(v):
    out=hh['ZERO']
    for p,c in v.items():out=hh['add'](out,hh['mul'](c,hh['log'](Q(p))))
    return out
start=time.perf_counter();results=[];checks=0
for j,(R,T),core in itertools.product((1,2),((1,1),(1,2),(2,2),(4,4)),('dictator','majority3')):
    L=1;k=1 if core=='dictator' else 3;n=j+R+T+L+k
    f=[]
    for x in range(2**n):
        off=0;ind=[]
        for w in (j,R,T,L):ind.append(((x>>off)&(2**w-1))==0);off+=w
        S,U,V,W=ind;A=(W and U and V)or(S and(U or V))
        g=1 if core=='dictator' and not(x>>off&1) else (-1 if core=='dictator' else (1 if sum((x>>(off+i))&1 for i in range(3))>=2 else -1))
        f.append(g if A else 1)
    arr=f[:];h=1
    while h<len(arr):
        for base in range(0,len(arr),2*h):
            for a in range(base,base+h):u,v=arr[a],arr[a+h];arr[a],arr[a+h]=u+v,u-v
        h*=2
    d=Q(sum(f[x]!=f[x^1] for x in range(len(f))),len(f));vec={}
    paircounts={}
    for t in range(len(f)//2):
        a=Q(arr[2*t],len(f))**2;b=Q(arr[2*t+1],len(f))**2
        paircounts[a,b]=paircounts.get((a,b),0)+1
    for (a,b),count in paircounts.items():vec=plus((1,vec),(count,psi(a,b)))
    # Independent grouping formula: paired control rows, arbitrary normalized core law.
    expected={}
    for mask,count in hh['rows']((j-1,R,T,L)):
        child0=hh['coeff']((None,R,T,L),mask);child1=hh['coeff']((j-1,R,T,L),mask)
        for corelabel in (0,1):
            g=child0 if corelabel else Q(mask==0)-child0
            h=child1 if corelabel else Q(mask==0)-child1
            expected=plus((1,expected),(count,psi(((g+h)/2)**2,((g-h)/2)**2)))
    assert vec==expected;checks+=1
    q,r=Q(1,2**R),Q(1,2**T);eta=Q(1,2**(L+R+T));e=q+r-q*r-eta
    assert d==e/Q(2**j);checks+=1
    bound=interval(vec)
    if min(R,T)>=4:assert bound[1]<Q(1781,480)*d;checks+=1
    results.append({'j':j,'L':L,'R':R,'T':T,'core':core,'dimension':n,'d':str(d),'B_over_d':hh['fmt'](hh['mul'](1/d,bound)),'exact_erasure_vector':{str(p):str(v) for p,v in vec.items()},'grouping_exactly_matches':True})
out={'status':'PASS','explicit_boolean_roots':len(results),'recorded_assertions':checks,'max_dimension':max(x['dimension'] for x in results),'runtime_seconds':time.perf_counter()-start,'results':results}
(ROOT/'out'/'DIRECT_CHECK.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8');print(json.dumps({k:v for k,v in out.items() if k!='results'}))
