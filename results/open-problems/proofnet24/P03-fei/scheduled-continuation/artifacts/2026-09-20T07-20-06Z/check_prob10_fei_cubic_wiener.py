#!/usr/bin/env python3
from __future__ import annotations
from fractions import Fraction as F
from itertools import combinations
import math, random, json

SEED=20260920
rng=random.Random(SEED)

def walsh(vals):
    a=list(vals); h=1
    while h<len(a):
        for s in range(0,len(a),2*h):
            for j in range(s,s+h):
                u,v=a[j],a[j+h]; a[j]=u+v; a[j+h]=u-v
        h*=2
    return tuple(a)

def lam(vals):
    W=walsh(vals); N=len(vals)
    return F(sum(abs(x) for x in W),N)

def entropy(vals):
    W=walsh(vals); N=len(vals); N2=N*N
    ans=0.0
    for w in W:
        if w:
            p=(w*w)/N2
            ans-=p*math.log2(p)
    return ans

def influences(vals):
    N=len(vals); n=N.bit_length()-1
    out=[]
    for i in range(n):
        c=sum(vals[x]!=vals[x^(1<<i)] for x in range(N))
        out.append(F(c,N))
    return tuple(out)

def folded(vals):
    return tuple(min(a,1-a) for a in influences(vals))

def J(vals): return sum(folded(vals),F(0))

def multiply(a,b): return tuple(x*y for x,y in zip(a,b))

def restrict(vals,i,b):
    n=len(vals).bit_length()-1
    idx=[j for j in range(n) if j!=i]
    out=[]
    for y in range(1<<(n-1)):
        x=(b<<i)
        for k,j in enumerate(idx): x|=((y>>k)&1)<<j
        out.append(vals[x])
    return tuple(out)

def d_wiener(vals,i):
    W=walsh(vals); N=len(vals)
    tot=0
    for s in range(N):
        if not ((s>>i)&1):
            tot+=min(abs(W[s]),abs(W[s|(1<<i)]))
    return F(tot,N)

def mean_derivative(vals,i):
    N=len(vals)
    return F(sum(vals[x]*vals[x^(1<<i)] for x in range(N)),N)

def gf2_rank(rows,n):
    rows=list(rows); r=0
    for c in range(n):
        p=next((k for k in range(r,len(rows)) if (rows[k]>>c)&1),None)
        if p is None: continue
        rows[r],rows[p]=rows[p],rows[r]
        for k in range(len(rows)):
            if k!=r and ((rows[k]>>c)&1): rows[k]^=rows[r]
        r+=1
    return r

def phase_from_monomials(n, monomials):
    vals=[]
    for x in range(1<<n):
        q=0
        for m in monomials:
            if all((x>>i)&1 for i in m): q^=1
        vals.append(1-2*q)
    return tuple(vals)

def link_rank(n,cubic_edges,i):
    rows=[0]*n
    for e in cubic_edges:
        if i not in e: continue
        a,b=[j for j in e if j!=i]
        rows[a]^=1<<b; rows[b]^=1<<a
    return gf2_rank(rows,n)

def derivative(vals,i):
    return tuple(vals[x]*vals[x^(1<<i)] for x in range(len(vals)))

def c_qw(L):
    return max(15.0, 2*math.log2(math.e)+12*math.log2(float(L)))

def table_key(v):
    return sum((1 if x<0 else 0)<<i for i,x in enumerate(v))

def all_bool(n):
    N=1<<n
    for key in range(1<<N):
        yield tuple(-1 if (key>>x)&1 else 1 for x in range(N))

def quadratic_phases(n):
    mons=[(i,) for i in range(n)]+list(combinations(range(n),2))
    for mask in range(1<<len(mons)):
        sel=[mons[k] for k in range(len(mons)) if (mask>>k)&1]
        yield phase_from_monomials(n,sel)

def lambda2_cache(n):
    phases=list(quadratic_phases(n))
    cache={}; minimizer={}
    for f in all_bool(n):
        k=table_key(f); best=None; bestu=None
        for q in phases:
            u=multiply(f,q); L=lam(u)
            if best is None or L<best:
                best=L; bestu=u
        cache[k]=best; minimizer[k]=bestu
    return cache,minimizer

def one_point(n):
    return tuple(-1 if x==0 else 1 for x in range(1<<n))

def majority(n):
    assert n%2==1
    return tuple(1 if x.bit_count()<=n//2 else -1 for x in range(1<<n))

def maj3_comp():
    n=9; vals=[]
    for x in range(1<<n):
        inner=[]
        for b in range(3):
            ones=sum((x>>(3*b+j))&1 for j in range(3))
            inner.append(1 if ones<=1 else -1)
        vals.append(1 if sum(1 for z in inner if z==-1)<=1 else -1)
    return tuple(vals)

def addressing6():
    vals=[]
    for x in range(64):
        a=((x>>0)&1)+2*((x>>1)&1)
        bit=(x>>(2+a))&1
        vals.append(1-2*bit)
    return tuple(vals)

def bent4():
    return phase_from_monomials(4,[(0,1),(2,3)])

def tensor(a,b):
    na=len(a).bit_length()-1; nb=len(b).bit_length()-1
    return tuple(a[x & ((1<<na)-1)]*b[x>>na] for x in range(1<<(na+nb)))

def gamma_controls(seed,c=3):
    ns=len(seed).bit_length()-1; n=ns+c; vals=[]
    for x in range(1<<n):
        old=x & ((1<<ns)-1); ctrl=x>>ns
        vals.append(seed[old] if ctrl==0 else 1)
    return tuple(vals)

out={"status":"PASS","seed":SEED,"exact":{},"numerical":{},"named":{}}

cnt=0
for n in range(1,4):
    for f in all_bool(n):
        L=lam(f)
        for i in range(n):
            lhs=(lam(restrict(f,i,0))+lam(restrict(f,i,1)))/2
            rhs=L-d_wiener(f,i)
            assert lhs==rhs
            cnt+=1
out["exact"]["raw_wiener_branch_drop_checks"]=cnt

l2={}; mins={}
for n in range(0,4):
    if n==0:
        l2[0]={0:F(1),1:F(1)}; mins[0]={0:(1,),1:(-1,)}
    else:
        l2[n],mins[n]=lambda2_cache(n)
cnt=0; min_slack=None
for n in range(1,4):
    for f in all_bool(n):
        k=table_key(f); L=l2[n][k]; u=mins[n][k]
        for i in range(n):
            c0=restrict(f,i,0); c1=restrict(f,i,1)
            lhs=(l2[n-1][table_key(c0)]+l2[n-1][table_key(c1)])/2
            rhs=L-d_wiener(u,i)
            assert lhs<=rhs
            slack=rhs-lhs
            min_slack=slack if min_slack is None or slack<min_slack else min_slack
            cnt+=1
out["exact"]["quadratic_normalized_branch_drop_checks"]=cnt
out["exact"]["quadratic_normalized_min_slack"]=str(min_slack)

named={
    "one_point_6":one_point(6),
    "majority_5":majority(5),
    "majority_substitution_9":maj3_comp(),
    "addressing_6":addressing6(),
    "bent_quadratic_4":bent4(),
    "tensor_w3_w3":tensor(one_point(3),one_point(3)),
    "fresh_control_gamma3_majority3":gamma_controls(majority(3),3),
}
anti_cnt=0; min_anti=None; closure_cnt=0; min_closure=1e99

def random_cubic_edges(n,p=0.45):
    edges=[e for e in combinations(range(n),3) if rng.random()<p]
    if not edges and n>=3: edges=[tuple(range(3))]
    return edges

def test_anti(u,edges,lower=()):
    global anti_cnt,min_anti,closure_cnt,min_closure
    n=len(u).bit_length()-1
    P=phase_from_monomials(n,list(edges)+list(lower))
    Fv=multiply(P,u); L=lam(u); C=c_qw(L)
    active=sorted(set(i for e in edges for i in e))
    qualifies=True
    detail=[]
    for i in active:
        r=link_rank(n,edges,i); assert r%2==0
        Li=lam(derivative(u,i))
        amp=Li/F(2**(r//2),1)
        bound=(1-min(F(1),amp))/2
        ji=(1-abs(mean_derivative(Fv,i)))/2
        assert ji>=bound
        sl=ji-bound
        if min_anti is None or sl<min_anti: min_anti=sl
        anti_cnt+=1
        qualifies=qualifies and (float(amp)<=1-4/C+1e-15)
        detail.append((i,r,str(Li),str(ji),str(bound),float(amp)))
    if active and qualifies:
        h=entropy(Fv); rhs=C*float(J(Fv))
        assert h<=rhs+1e-10
        closure_cnt+=1; min_closure=min(min_closure,rhs-h)
    return {"n":n,"Lambda":str(L),"C_QW":C,"active":len(active),"qualifies_all_active":qualifies,"H":entropy(Fv),"J":float(J(Fv)),"coordinates":detail[:12]}

for n in range(3,9):
    for _ in range(80):
        u=tuple(rng.choice((-1,1)) for _ in range(1<<n))
        edges=random_cubic_edges(n,0.35)
        lower=[]
        for e in combinations(range(n),2):
            if rng.random()<0.12: lower.append(e)
        test_anti(u,edges,lower)
for name,u in named.items():
    n=len(u).bit_length()-1
    edges=random_cubic_edges(n,0.55 if n<=6 else 0.25)
    out["named"][name]=test_anti(u,edges)
out["exact"]["high_link_anticancellation_coordinate_checks"]=anti_cnt
out["exact"]["high_link_min_slack"]=str(min_anti)
out["numerical"]["qualified_cubic_transfer_instances"]=closure_cnt
out["numerical"]["min_cubic_transfer_entropy_slack"]=None if closure_cnt==0 else min_closure

pair_cnt=0; min_slack=1e99; worst=None
for n in range(1,4):
    funcs=list(all_bool(n)); H=[entropy(f) for f in funcs]; L=[float(lam(f)) for f in funcs]
    for a,f in enumerate(funcs):
        for b,g in enumerate(funcs):
            fg=multiply(f,g); diff=abs(entropy(fg)-H[a]); rhs=2*math.log2(L[b])
            slack=rhs-diff
            if slack<min_slack:
                min_slack=slack; worst=(n,a,b,diff,rhs,L[b])
            assert slack>=-1e-10
            pair_cnt+=1
out["numerical"]["entropy_perturbation_pair_checks"]=pair_cnt
out["numerical"]["entropy_perturbation_min_slack"]=min_slack
out["numerical"]["entropy_perturbation_worst"]=worst

for name,f in named.items():
    n=len(f).bit_length()-1; L=lam(f)
    ds=[d_wiener(f,i) for i in range(n)]
    out["named"][name].update({
        "raw_Lambda":str(L),"raw_wiener_overlap": [str(x) for x in ds],
        "raw_overlap_zero_count":sum(x==0 for x in ds),
        "entropy":entropy(f),"I":float(sum(influences(f),F(0))),"J":float(J(f))
    })

out["limitations"]=(
    "Structural branch-drop and cubic anti-cancellation checks are exact rational/integer checks. "
    "Entropy comparisons use Python floating point only as deterministic stress tests; the report supplies the all-dimensional proofs. "
    "The archived coded F_8 obstruction has 2040 physical inputs and was not truth-table executed here. "
    "No independent audit or formal proof assistant run is claimed."
)
print(json.dumps(out,indent=2))
