#!/usr/bin/env python3
"""
Sanity checker for NM13-02 T01 hybrid hereditary decision-tree recursion.

Checks:
1. exhaustive full-binary tree shapes through 10 leaves against the proved
   height and leaf-count envelopes;
2. the exact nested-canalizing spine recursion and its <3 formula;
3. direct Walsh/Fourier hereditary allocation for h_k=(-1)^p_k under every
   quadratic twist through k=4 and deterministic random quadratic twists
   for k=5,6, using the designated physical spine followed by full
   completions on quadratic leaves.

The analytic report, not this numerical program, proves the theorem.
"""
import math, itertools, random, functools, json

CCHI = 2 + 1/(math.sqrt(math.e)*math.log(2))
C0 = 1/math.log(2)
A_LEAF = CCHI - math.log2(3)

def hybrid_k(kp, km):
    descendant = max(C0, 1+kp, 1+km)
    minor = max(CCHI, kp, km, 1+(kp+km)/2)
    return min(descendant, minor)

def spine_k(depth):
    k=1.0
    for _ in range(depth):
        k=hybrid_k(1.0,k)
    return k

@functools.lru_cache(None)
def shapes(L):
    if L==1:
        return (None,)
    out=[]
    for l in range(1,L):
        for a in shapes(l):
            for b in shapes(L-l):
                out.append((a,b))
    return tuple(out)

def tree_k(t):
    if t is None:
        return 1.0
    return hybrid_k(tree_k(t[0]),tree_k(t[1]))

def tree_h(t):
    if t is None:
        return 0
    return 1+max(tree_h(t[0]),tree_h(t[1]))

def fwht(vals):
    a=[float(v) for v in vals]
    n=len(a); h=1
    while h<n:
        for i in range(0,n,2*h):
            for j in range(i,i+h):
                x=a[j]; y=a[j+h]
                a[j]=x+y; a[j+h]=x-y
        h*=2
    return [x/n for x in a]

def B_i(vals,i):
    n=len(vals).bit_length()-1
    coeff=fwht(vals)
    p=[c*c for c in coeff]
    bit=1<<i
    total=0.0
    for m in range(1<<n):
        if m & bit:
            continue
        p0,p1=p[m],p[m|bit]
        q=p0+p1
        if p0>0:
            total -= p0*math.log2(p0/q)
        if p1>0:
            total -= p1*math.log2(p1/q)
    return total

def influence_i(vals,i):
    n=len(vals).bit_length()-1
    bit=1<<i
    dif=0
    for m in range(1<<n):
        if not (m&bit) and vals[m]!=vals[m|bit]:
            dif+=1
    return dif/(1<<(n-1))

def total_influence(vals):
    n=len(vals).bit_length()-1
    return sum(influence_i(vals,i) for i in range(n))

def restrict(vals,i,b):
    n=len(vals).bit_length()-1
    out=[]
    for m in range(1<<(n-1)):
        low=m&((1<<i)-1)
        high=m>>i
        orig=low|(b<<i)|(high<<(i+1))
        out.append(vals[orig])
    return out

@functools.lru_cache(None)
def full_R_tuple(vals_t):
    vals=list(vals_t)
    n=len(vals).bit_length()-1
    if n==0:
        return 0.0
    return (B_i(vals,0)
            +0.5*full_R_tuple(tuple(restrict(vals,0,0)))
            +0.5*full_R_tuple(tuple(restrict(vals,0,1))))

def spine_R(vals,remaining_depth):
    if remaining_depth==0:
        return full_R_tuple(tuple(vals))
    return (B_i(vals,0)
            +0.5*full_R_tuple(tuple(restrict(vals,0,0)))
            +0.5*spine_R(restrict(vals,0,1),remaining_depth-1))

def p_nested(bits):
    prod=1
    s=0
    for x in bits:
        prod &= x
        s ^= prod
    return s

def quadratic_terms(n):
    return [()] + [(i,) for i in range(n)] + [
        (i,j) for i in range(n) for j in range(i+1,n)
    ]

def q_eval(bits,mask,terms):
    s=0
    for idx,t in enumerate(terms):
        if (mask>>idx)&1:
            v=1
            for i in t:
                v &= bits[i]
            s ^= v
    return s

def nested_twist_vals(n,mask):
    terms=quadratic_terms(n)
    out=[]
    for m in range(1<<n):
        bits=[(m>>i)&1 for i in range(n)]
        e=p_nested(bits)^q_eval(bits,mask,terms)
        out.append(-1 if e else 1)
    return out

shape_rows=[]
max_height_violation=-1e100
max_leaf_violation=-1e100
for L in range(1,11):
    vals=[]
    for t in shapes(L):
        k=tree_k(t)
        vals.append(k)
        max_height_violation=max(max_height_violation,k-(tree_h(t)+1))
        max_leaf_violation=max(max_leaf_violation,k-(A_LEAF+math.log2(L)))
    shape_rows.append({
        "leaves":L,
        "shape_count":len(vals),
        "min_kappa":min(vals),
        "max_kappa":max(vals),
        "leaf_envelope":A_LEAF+math.log2(L)
    })

spine_rows=[]
for d in range(0,13):
    k=spine_k(d)
    if d>=2:
        formula=3-(3-CCHI)/(2**(d-2))
    elif d==1:
        formula=2.0
    else:
        formula=1.0
    spine_rows.append({"depth":d,"kappa":k,"formula":formula,"difference":k-formula})

fourier_rows=[]
max_fourier_violation=-1e100
worst=None
for n in range(1,5):
    nq=1<<len(quadratic_terms(n))
    localmax=0.0
    skipped=0
    for mask in range(nq):
        vals=nested_twist_vals(n,mask)
        I=total_influence(vals)
        R=spine_R(vals,n)
        if I<1e-14:
            skipped+=1
            if abs(R)>1e-10:
                raise AssertionError(("zero influence nonzero R",n,mask,R))
            continue
        ratio=R/I
        localmax=max(localmax,ratio)
        violation=R-spine_k(n)*I
        if violation>max_fourier_violation:
            max_fourier_violation=violation
            worst=(n,mask,I,R,ratio,spine_k(n))
    fourier_rows.append({
        "n":n,"quadratic_twists":nq,"zero_influence_skipped":skipped,
        "max_observed_R_over_I":localmax,"theorem_kappa":spine_k(n)
    })

random.seed(20260920)
sample_rows=[]
for n,samples in [(5,300),(6,200)]:
    nq=1<<len(quadratic_terms(n))
    localmax=0.0
    min_margin=1e100
    for _ in range(samples):
        mask=random.randrange(nq)
        vals=nested_twist_vals(n,mask)
        I=total_influence(vals)
        R=spine_R(vals,n)
        if I>1e-14:
            localmax=max(localmax,R/I)
            min_margin=min(min_margin,spine_k(n)*I-R)
    sample_rows.append({
        "n":n,"samples":samples,"max_observed_R_over_I":localmax,
        "theorem_kappa":spine_k(n),"min_margin_kappaI_minus_R":min_margin
    })

assert max_height_violation <= 1e-12
assert max_leaf_violation <= 1e-12
assert max(abs(r["difference"]) for r in spine_rows) <= 1e-12
assert max_fourier_violation <= 1e-10
assert all(r["min_margin_kappaI_minus_R"] >= -1e-10 for r in sample_rows)

out={
    "status":"PASS",
    "constants":{
        "C_chi":CCHI,
        "one_over_ln2":C0,
        "leaf_envelope_additive_constant_Cchi_minus_log2_3":A_LEAF,
        "conditional_spine_FEI_with_P03_recombination_limit":3+2/math.log(2)
    },
    "tree_shape_exhaustion":shape_rows,
    "max_height_envelope_violation":max_height_violation,
    "max_leaf_envelope_violation":max_leaf_violation,
    "spine_formula":spine_rows,
    "fourier_exhaustive_quadratic_twists":fourier_rows,
    "fourier_max_violation_R_minus_kappaI":max_fourier_violation,
    "fourier_worst_margin_case":worst,
    "fourier_random_quadratic_twists":sample_rows
}
print(json.dumps(out,indent=2,sort_keys=True))
