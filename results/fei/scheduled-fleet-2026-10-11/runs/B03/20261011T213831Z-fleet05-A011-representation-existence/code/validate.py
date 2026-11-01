"""Frozen exact representation check; no entropy floating point is used."""
from fractions import Fraction as Q
from functools import lru_cache
from collections import defaultdict
import json, time, pathlib

START=time.perf_counter()
ASSERTIONS=0
def check(p):
    global ASSERTIONS
    ASSERTIONS+=1
    assert p

@lru_cache(None)
def trees(j,n):
    if j==n: return (0,1)
    lower=trees(j+1,n)
    return (0,1)+tuple((j,a,b) for a in lower for b in lower)

def label(t,x):
    while isinstance(t,tuple):
        j,a,b=t
        t=b if (x>>j)&1 else a
    return t

def coefficients(t,n):
    # Characters use (-1)^input-bit; selector child0 is +1.
    vals=[1-2*((x>>(n+label(t,x)))&1) for x in range(1<<(n+2))]
    w=vals[:]
    h=1
    while h<len(w):
        for k in range(0,len(w),2*h):
            for i in range(k,k+h):
                a,b=w[i],w[i+h]; w[i],w[i+h]=a+b,a-b
        h*=2
    return {s:Q(a,len(w)) for s,a in enumerate(w) if a}

@lru_cache(None)
def build(t,n):
    if isinstance(t,int):
        return {1<<(n+t):Q(1)}, {((),0,1<<(n+t)):Q(1)}, Q(0)
    j,a,b=t
    fa,wa,da=build(a,n); fb,wb,db=build(b,n)
    out={}; witness=defaultdict(Q)
    tails=set(fa)|set(fb)
    theta={}
    for s in tails:
        aa,bb=fa.get(s,Q(0)),fb.get(s,Q(0))
        q=(aa*aa+bb*bb)/2
        theta[s]=(aa-bb)**2/(4*q)
        for z,c in ((0,(aa+bb)/2),(1,(aa-bb)/2)):
            if c: out[s|(z<<j)]=c
    for physical,ww in ((0,wa),(1,wb)):
        for (path,zmask,s),p in ww.items():
            for z,prob in ((0,1-theta[s]),(1,theta[s])):
                if prob:
                    key=(((j,physical),)+path,zmask|(z<<j),s|(z<<j))
                    witness[key]+=p*prob/2
    return out,dict(witness),1+(da+db)/2

def leaf_partition(t,n,path=(),fixed=0):
    if isinstance(t,int): return [(path,fixed,t)]
    j,a,b=t
    return leaf_partition(a,n,path+((j,0),),fixed|(1<<j))+leaf_partition(b,n,path+((j,1),),fixed|(1<<j))

def validate(t,n):
    f,w,D=build(t,n)
    check(f==coefficients(t,n))
    check(sum(w.values())==1)
    marginal=defaultdict(Q); paths=defaultdict(Q)
    expected_depth=Q(0)
    for (path,zmask,s),p in w.items():
        marginal[s]+=p; paths[path]+=p; expected_depth+=p*len(path)
        check(all((zmask>>j)&1==0 for j in range(n) if j not in [i for i,b in path]))
    check(dict(marginal)=={s:a*a for s,a in f.items()})
    check(expected_depth==D)
    leaves=leaf_partition(t,n)
    check(paths=={path:Q(1,1<<len(path)) for path,_,_ in leaves})
    B=Q(0)
    for x in range(1<<n):
        ell=label(t,x)
        B+=sum(ell!=label(t,x^(1<<j)) for j in range(n))*Q(1,1<<n)
    Isel=sum(a*a*(s&((1<<n)-1)).bit_count() for s,a in f.items())
    Idata=sum(a*a*(s>>n).bit_count() for s,a in f.items())
    check(2*Isel==B); check(Idata==1); check(B<=D)
    return D,B,len(w)

def comb(a,j=0):
    return (a%2) if j==a else (j,j%2,comb(a,j+1))

alltrees=trees(0,3)
check(len(alltrees)==1446)
admitted=0; max_witnesses=0
for t in alltrees:
    D,B,c=validate(t,3)
    admitted+=bool(D and B>=D/2)
    max_witnesses=max(max_witnesses,c)
    check(time.perf_counter()-START<60)

combs=[]
for a in range(1,65):
    # r_j=P(continuation label differs from leaf j); r_a=1,
    # r_j=1-r_(j+1)/2 working backwards.
    rs=[Q(0)]*a; rs[-1]=Q(1)
    for j in range(a-2,-1,-1): rs[j]=1-rs[j+1]/2
    D=sum(Q(1,1<<j) for j in range(a))
    B=sum(Q(1,1<<j)*rs[j] for j in range(a))
    check(D==2*(1-Q(1,1<<a)))
    check(all(Q(1,2)<=r<=1 for r in rs))
    check(B>=D/2)
    if a<=6:
        d,b,_=validate(comb(a),a); check((d,b)==(D,B))
    combs.append({'a':a,'D':str(D),'B':str(B),'I_selector':str(B/2)})

result={'helper_version':'a011-selector-transcript-v1','exact_tree_cases':len(alltrees),
        'beta_half_admitted_nontrivial_representations':admitted,'comb_recurrence_cases':64,
        'comb_truth_table_cases':6,'assertions':ASSERTIONS,'max_tree_witnesses':max_witnesses,
        'runtime_seconds':time.perf_counter()-START,'arithmetic':'integer FWHT and Fraction',
        'entropy_certification':'analytic chain rule and h2(theta)<=1; no floating logarithms',
        'combs':combs}
root=pathlib.Path(__file__).resolve().parents[1]
(root/'out'/'EXACT_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in result.items() if k!='combs'},indent=2))
