#!/usr/bin/env python3
import itertools, json, math, random

def fwht(a):
    a=list(a); h=1
    while h<len(a):
        for i in range(0,len(a),2*h):
            for j in range(i,i+h):
                x,y=a[j],a[j+h]
                a[j],a[j+h]=x+y,x-y
        h*=2
    return a

def entropy(vals):
    N=len(vals); W=fwht(vals); H=0.0
    for c in W:
        if c:
            p=(c*c)/(N*N)
            H -= p*math.log2(p)
    return H

def inf_coord(vals,i):
    N=len(vals); c=0
    for x in range(N):
        if ((x>>i)&1)==0 and vals[x]!=vals[x|(1<<i)]:
            c+=1
    return c/(N//2)

def influence(vals):
    n=(len(vals).bit_length()-1)
    return sum(inf_coord(vals,i) for i in range(n))

def qphase(n,linear,edge_mask,const):
    edges=[(i,j) for i in range(n) for j in range(i+1,n)]
    out=[]
    for x in range(1<<n):
        b=const ^ (((linear & x).bit_count())&1)
        for e,(i,j) in enumerate(edges):
            if ((edge_mask>>e)&1) and ((x>>i)&1) and ((x>>j)&1):
                b ^= 1
        out.append(-1 if b else 1)
    return out

def rows(n,edge_mask):
    rs=[0]*n; e=0
    for i in range(n):
        for j in range(i+1,n):
            if (edge_mask>>e)&1:
                rs[i]|=1<<j; rs[j]|=1<<i
            e+=1
    return rs

def apply_defects(vals,D):
    out=list(vals)
    for x in D: out[x]*=-1
    return out

def Ct(t):
    L=math.ceil(math.log2(t)) if t>1 else 0
    a=max(3,L)
    dcut=max(1,L+a-1)
    return 12.04+math.log2(dcut)

# 1. Exhaustive sparse-core FEI ratios in dimensions <=4.
sparse_cases=0
max_sparse_ratio=0.0
max_sparse_witness=None
for n in range(1,5):
    N=1<<n
    for m in range(1,N//2+1):
        for D in itertools.combinations(range(N),m):
            DS=set(D)
            vals=[-1 if x in DS else 1 for x in range(N)]
            H=entropy(vals); I=influence(vals)
            ratio=H/I
            sparse_cases += 1
            if ratio>max_sparse_ratio:
                max_sparse_ratio=ratio
                max_sparse_witness=[n,m,list(D),H,I,ratio]

# 2. Exhaustive local nonzero-polar pivot toggle bound in dimensions <=4,
#    for all quadratic edge masks and defect sets of size <=2.
pivot_cases=0
max_pivot_violation=-1.0
pivot_witness=None
for n in range(2,5):
    N=1<<n; ne=n*(n-1)//2
    defects=[()]
    defects += [(x,) for x in range(N)]
    defects += list(itertools.combinations(range(N),2))
    for em in range(1<<ne):
        rs=rows(n,em)
        nz=[i for i,r in enumerate(rs) if r]
        if not nz: continue
        base=qphase(n,0,em,0)
        for D in defects:
            vals=apply_defects(base,D)
            rhs=len(D)/(2**(n-1))
            for i in nz:
                alpha=inf_coord(vals,i)
                viol=abs(alpha-0.5)-rhs
                pivot_cases += 1
                if viol>max_pivot_violation:
                    max_pivot_violation=viol
                    pivot_witness=[n,em,list(D),i,alpha,rhs]

# 3. Deterministic-seed random finite-defect quadratic functions.
rng=random.Random(20260920)
sample_cases=0
max_class_ratio=0.0
max_class_witness=None
max_class_bound_violation=-1e99
for n in range(1,8):
    N=1<<n; ne=n*(n-1)//2
    for s in range(500):
        em=rng.getrandbits(ne)
        lm=rng.getrandbits(n)
        const=rng.getrandbits(1)
        tmax=min(8,N//2)
        m=rng.randint(1,tmax)
        D=set(rng.sample(range(N),m))
        vals=apply_defects(qphase(n,lm,em,const),D)
        H=entropy(vals); I=influence(vals); ratio=(H/I if I>1e-15 else 0.0)
        bound=Ct(m)
        sample_cases += 1
        max_class_ratio=max(max_class_ratio,ratio)
        max_class_bound_violation=max(max_class_bound_violation,ratio-bound)
        if max_class_witness is None or ratio==max_class_ratio:
            max_class_witness=[n,m,em,lm,const,H,I,ratio,bound]

# 4. Scalar constants used in the proof.
eta=0.25
h2=lambda x: -x*math.log2(x)-(1-x)*math.log2(1-x)
local_total=h2(eta)/eta + 2/math.log(2)
c0=math.log2(math.e)-1
# For a=max(3,L), the high-dimensional sparse leaf bound is <= 6.2952.
worst_sparse_analytic=4+2*(1+c0/3)

out={
    "status":"PASS" if max_pivot_violation<=1e-12 and max_class_bound_violation<=1e-12 else "FAIL",
    "sparse_exhaustive_cases":sparse_cases,
    "max_sparse_ratio_n_le_4":max_sparse_ratio,
    "max_sparse_witness":max_sparse_witness,
    "pivot_exhaustive_cases":pivot_cases,
    "max_pivot_bound_violation":max_pivot_violation,
    "pivot_witness":pivot_witness,
    "sampled_quadratic_defect_cases":sample_cases,
    "max_sample_class_ratio":max_class_ratio,
    "max_sample_class_bound_violation":max_class_bound_violation,
    "max_sample_class_witness":max_class_witness,
    "local_total_constant_at_eta_1_4":local_total,
    "analytic_high_dim_sparse_constant_upper":worst_sparse_analytic,
    "note":"Finite checks support, but do not replace, the all-dimensional proofs in the report."
}
print(json.dumps(out,indent=2,sort_keys=True))
