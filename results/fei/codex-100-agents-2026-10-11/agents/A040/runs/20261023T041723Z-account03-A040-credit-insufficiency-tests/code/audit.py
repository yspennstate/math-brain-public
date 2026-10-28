"""Independent representation: direct Walsh sums, prime-log identities, density transport.
Imports no check.py or arithmetic.py. Fixed audit domain recorded before execution.
"""
from fractions import Fraction as Q
from functools import lru_cache
from pathlib import Path
import json,time,itertools,hashlib
ROOT=Path(__file__).resolve().parents[1]
started=time.perf_counter();checks=0;prime_equalities=0
def assertq(test):
    global checks
    assert test
    checks+=1
    assert time.perf_counter()-started<55
@lru_cache(None)
def probabilities(truth):
    size=len(truth)
    return tuple(Q(sum(truth[x]*(-1 if (x&t).bit_count()%2 else 1) for x in range(size)),size)**2 for t in range(size))
def pt(k):return tuple(1-2*(x==(1<<k)-1) for x in range(1<<k))
def product(tables):
    result=(1,)
    for tab in tables:result=tuple(a*b for b in tab for a in result)
    return result
def restrict(truth,j,y):return tuple(v for x,v in enumerate(truth) if x>>j&1==y)
def G(v,u,eps):return tuple(eps if x%2==0 else v[(x//2)%len(v)]*u[x//(2*len(v))] for x in range(2*len(v)*len(u)))
def tilted(v,beta):
    p=probabilities(v)
    if len(v)<=2 or p[0]==1:return p
    return tuple(p[0] if t==0 else beta*p[t]+(1-beta)*(1-p[0])*(t==len(p)-1) for t in range(len(p)))
def step(truth,ref,j):
    p=probabilities(truth);out=[];normalizers=[]
    for y in (0,1):
        child=restrict(truth,j,y);pc=probabilities(child);unnorm=[]
        for t in range(len(pc)):
            lowbits=t%2**j; highbits=t//2**j
            i0=lowbits+highbits*2**(j+1);i1=i0+2**j
            pbar=p[i0]+p[i1]
            unnorm.append((ref[i0]+ref[i1])*(pc[t]/(2*pbar) if pbar else Q(1,2)))
        norm=sum(unnorm);assertq(norm>0)
        out.append((child,tuple(q/norm for q in unnorm)));normalizers.append(norm)
    assertq(sum(normalizers)==1)
    return out,normalizers
@lru_cache(None)
def factors(n):
    out={};d=2
    while d*d<=n:
        while n%d==0:out[d]=out.get(d,0)+1;n//=d
        d+=1 if d==2 else 2
    if n>1:out[n]=out.get(n,0)+1
    return out
def logsum_add(out,coefficient,value):
    for prime,exp in factors(value.numerator).items():out[prime]=out.get(prime,Q(0))+coefficient*exp
    for prime,exp in factors(value.denominator).items():out[prime]=out.get(prime,Q(0))-coefficient*exp
def divergence_vector(p,q):
    out={}
    for x,y in zip(p,q):
        if x:assertq(y>0);logsum_add(out,x,x/y)
    return out
def combine(*terms):
    out={}
    for coefficient,vec in terms:
        for prime,value in vec.items():out[prime]=out.get(prime,Q(0))+coefficient*value
    return {p:c for p,c in out.items() if c}

records=[];discarded_witnesses=[]
for width,uw,eps,sign in itertools.product((2,3),(0,1,2),(-1,1),(-1,1)):
    u=pt(uw) if uw else (1,);pu=probabilities(u);qu=tilted(u,Q(5,6));su=tuple(q/p if p else Q(1) for p,q in zip(pu,qu))
    v=tuple(sign*x for x in pt(width));pv=probabilities(v);qv=tilted(v,Q(5,6));lv=tuple(q/p if p else Q(1) for p,q in zip(pv,qv))
    truth=G(v,u,eps);p=probabilities(truth)
    B=tuple(x*lv[(t//2)%len(v)] for t,x in enumerate(p));R=tuple(b*su[t//(2*len(v))] for t,b in enumerate(B))
    nrows=0
    def visit(v,B,R,path):
        global prime_equalities
        nonlocal_dummy=None
        truth=G(v,u,eps);p=probabilities(truth);w=len(v).bit_length()-1
        assertq(sum(B)==sum(R)==1)
        ss=tuple(su[t//(2*len(v))] for t in range(len(p)))
        assertq(R==tuple(b*s for b,s in zip(B,ss)))
        for uu in range(1,len(pu)):
            assertq(sum(x for t,x in enumerate(p) if t//(2*len(v))==uu)==pu[uu]/2)
        pv=probabilities(v);qn=tilted(v,Q(4,5));ln=tuple(q/x if x else Q(1) for x,q in zip(pv,qn))
        N=tuple(x*ss[t]*ln[(t//2)%len(v)] for t,x in enumerate(p));assertq(sum(N)==1)
        # Exact independent logarithm-vector identity at root and depth one.
        if len(path)<=1:
            diff=combine((1,divergence_vector(p,N)),(-1,divergence_vector(p,R)),(-Q(1,2),divergence_vector(pv,qn)),(1,divergence_vector(p,B)))
            assertq(not diff);prime_equalities+=1
        count=1
        for j in range(w):
            bs,zb=step(truth,B,j+1);rs,zr=step(truth,R,j+1);assertq(zb==zr)
            for y in (0,1):count+=visit(restrict(v,j,y),bs[y][1],rs[y][1],path+[(j,y)])
        return count
    nrows=visit(v,B,R,[]);records.append({'width':width,'spectator_width':uw,'epsilon':eps,'sign':sign,'nodes':nrows})

# Reconstruct every persisted full terminal P independently, including constants.
main=json.loads((ROOT/'out/CHECK.json').read_text(encoding='utf-8'))
terminal_count=0;constant_count=0
for policy in main['root_policies']:
    reach=Q(0)
    for term in policy['terminals']:
        p=probabilities(tuple(term['truth']));q=tuple(Q(x) for x in term['Q']);reach+=Q(term['reach'])
        assertq(p==tuple(Q(x) for x in term['P']))
        assertq(sum(q)==1 and all(not x or y>0 for x,y in zip(p,q)))
        terminal_count+=1;constant_count+=len(set(term['truth']))==1
    assertq(reach==1)
assertq(5**3<2*4**3);assertq(6**40<2**11*5**40);assertq(8**5<2*7**5)
out={'status':'PASS','checks':checks,'runtime_seconds':time.perf_counter()-started,'local_nodes':sum(x['nodes'] for x in records),'prime_log_equalities':prime_equalities,'root_terminal_laws_reconstructed':terminal_count,'constant_terminal_laws_retained':constant_count,'local_domains':records,'imported_author_or_foreign_helpers':False,'scope':'Exact local spectator identity and saved terminal-law reconstruction; not external peer acceptance or formal verification.'}
(ROOT/'out/AUDIT.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8',newline='\n')
print(json.dumps({k:v for k,v in out.items() if k!='local_domains'}))
