#!/usr/bin/env python3
import math, random, json

SEED = 202609200549
RANDOM_TWO_FLAT_PER_N = 400
RANDOM_MIXED_PER_N = 300

def fwht(vals):
    a=[float(v) for v in vals]
    n=len(a); h=1
    while h<n:
        for i in range(0,n,2*h):
            for j in range(i,i+h):
                x,y=a[j],a[j+h]
                a[j],a[j+h]=x+y,x-y
        h*=2
    return [x/n for x in a]

def entropy(vals):
    ans=0.0
    for c in fwht(vals):
        p=c*c
        if p>0:
            ans -= p*math.log2(p)
    return ans

def influences(vals,n):
    N=1<<n
    return [sum(vals[x]!=vals[x^(1<<i)] for x in range(N))/N for i in range(n)]

def gf2_rank(rows,n):
    rows=list(rows); r=0
    for c in range(n-1,-1,-1):
        p=next((k for k in range(r,len(rows)) if (rows[k]>>c)&1),None)
        if p is None: continue
        rows[r],rows[p]=rows[p],rows[r]
        for k in range(len(rows)):
            if k!=r and ((rows[k]>>c)&1):
                rows[k] ^= rows[r]
        r+=1
    return r

def random_independent_rows(n,r,rng):
    rows=[]
    while len(rows)<r:
        v=rng.randrange(1,1<<n)
        if gf2_rank(rows+[v],n)>len(rows):
            rows.append(v)
    return rows

def affine_flat(n,r,rng):
    rows=random_independent_rows(n,r,rng)
    bits=[rng.randrange(2) for _ in range(r)]
    A=frozenset(x for x in range(1<<n)
                if all(((row&x).bit_count()&1)==b for row,b in zip(rows,bits)))
    return A

def sigma(n,A):
    return [-1 if x in A else 1 for x in range(1<<n)]

def product(*arrays):
    return [math.prod(z) for z in zip(*arrays)]

def random_quadratic(n,rng):
    lin=rng.randrange(1<<n)
    rows=[0]*n
    edges=[]
    for i in range(n):
        for j in range(i+1,n):
            if rng.randrange(2):
                edges.append((i,j))
                rows[i] |= 1<<j
                rows[j] |= 1<<i
    vals=[]
    for x in range(1<<n):
        p=(lin&x).bit_count()&1
        for i,j in edges:
            p ^= ((x>>i)&1)&((x>>j)&1)
        vals.append(-1 if p else 1)
    return vals,rows

# Analytic codimension stress for S <= 3 * [edge-isoperimetric lower bound].
codim_worst={"ratio":0.0}
for a in range(4,31):
    x=2.0**(-a)
    for b in range(a,31):
        y=2.0**(-b)
        S=2*a*x+2*b*y
        candidates=[("disjoint",x+y,None)]
        if b>a:
            candidates.append(("nested",x-y,None))
        for c in range(b+1,a+b+1):
            candidates.append(("proper_intersection",x+y-2.0**(1-c),c))
        for typ,delta,c in candidates:
            iso=2*delta*math.log2(1/delta)
            ratio=S/(3*iso)
            if ratio>codim_worst["ratio"]:
                codim_worst={"ratio":ratio,"type":typ,"a":a,"b":b,"c":c,
                             "delta":delta,"S":S,"edge_iso_lower":iso}

# Exhaustive two distinct point-flats in dimension four.
point_rows=[]
max_point_ratio=0.0
max_point_84S=0.0
for u in range(16):
    A=frozenset({u})
    for v in range(u+1,16):
        B=frozenset({v})
        h=product(sigma(4,A),sigma(4,B))
        H=entropy(h); I=sum(influences(h,4))
        S=2*4/16+2*4/16
        max_point_ratio=max(max_point_ratio,H/I)
        max_point_84S=max(max_point_84S,H/(84*S))
        point_rows.append((u,v,H,I))

rng=random.Random(SEED)
random_two_flat_count=0
max_H_over_I=0.0
max_H_over_84S=0.0
max_S_over_3I=0.0
max_H_minus_252I=-1e100
internal_rows=0
min_internal_j=1.0
for n in range(4,9):
    for _ in range(RANDOM_TWO_FLAT_PER_N):
        a=rng.randint(4,n)
        b=rng.randint(4,n)
        A=affine_flat(n,a,rng); B=affine_flat(n,b,rng)
        if A==B:
            continue
        h=product(sigma(n,A),sigma(n,B))
        H=entropy(h); ivec=influences(h,n); I=sum(ivec)
        x=2.0**(-a); y=2.0**(-b)
        S=2*a*x+2*b*y
        if I>0:
            max_H_over_I=max(max_H_over_I,H/I)
            max_H_minus_252I=max(max_H_minus_252I,H-252*I)
            max_S_over_3I=max(max_S_over_3I,S/(3*I))
        max_H_over_84S=max(max_H_over_84S,H/(84*S))
        random_two_flat_count += 1

        q,rows=random_quadratic(n,rng)
        f=product(q,h)
        finf=influences(f,n)
        for i,row in enumerate(rows):
            if row:
                internal_rows += 1
                min_internal_j=min(min_internal_j,min(finf[i],1-finf[i]))

# Mixed codim-3 / high-codim leaf test for the C=16 transfer.
mixed_count=0
max_mixed_H_over_I=0.0
max_mixed_H_minus_16I=-1e100
for n in range(4,9):
    for _ in range(RANDOM_MIXED_PER_N):
        A=affine_flat(n,3,rng)
        b=rng.randint(4,n)
        B=affine_flat(n,b,rng)
        q,_=random_quadratic(n,rng)
        f=product(q,sigma(n,A),sigma(n,B))
        H=entropy(f); I=sum(influences(f,n))
        if I>0:
            max_mixed_H_over_I=max(max_mixed_H_over_I,H/I)
            max_mixed_H_minus_16I=max(max_mixed_H_minus_16I,H-16*I)
        mixed_count += 1

# Scope stress: one-point is a one-flat leaf; pure quadratic is zero-flat;
# a tensor of two one-point signs is represented by two lifted affine flats.
# Here is an explicit 3+3 tensor check.
n1=n2=3; n=6
A=frozenset(x for x in range(1<<n) if (x & 7)==0)
B=frozenset(x for x in range(1<<n) if ((x>>3)&7)==0)
tensor_h=product(sigma(n,A),sigma(n,B))
tensor_ratio=entropy(tensor_h)/sum(influences(tensor_h,n))

assert codim_worst["ratio"] <= 1.0 + 1e-12
assert max_point_84S <= 1.0 + 1e-12
assert max_H_over_84S <= 1.0 + 1e-12
assert max_S_over_3I <= 1.0 + 1e-12
assert max_H_minus_252I <= 1e-10
assert min_internal_j >= 0.25 - 1e-12
assert max_mixed_H_minus_16I <= 1e-10

out={
    "status":"PASS",
    "scope":"Self-checks for the two-affine-flat quadratic hereditary theorem. Floating entropy numerics do not replace the all-dimensional proof.",
    "seed":SEED,
    "analytic_codimension_stress":{
        "ranges":"4 <= a <= b <= 30; all proper-intersection codimensions b+1..a+b plus nested/disjoint",
        "worst":codim_worst
    },
    "exhaustive_dimension4_two_point_flats":{
        "pairs":len(point_rows),
        "max_H_over_I":max_point_ratio,
        "max_H_over_84S":max_point_84S
    },
    "random_two_flat_high_codimension":{
        "dimensions":"4..8",
        "cases":random_two_flat_count,
        "max_H_over_I":max_H_over_I,
        "max_H_over_84S":max_H_over_84S,
        "max_S_over_3I":max_S_over_3I,
        "max_H_minus_252I":max_H_minus_252I
    },
    "random_internal_quadratic_rows":{
        "relevant_coordinate_checks":internal_rows,
        "minimum_observed_folded_influence":min_internal_j,
        "proved_threshold":0.25
    },
    "mixed_codim3_highcodim_leaf":{
        "dimensions":"4..8",
        "cases":mixed_count,
        "max_H_over_I":max_mixed_H_over_I,
        "max_H_minus_16I":max_mixed_H_minus_16I
    },
    "tensor_scope_check":{
        "description":"product of two 3-bit one-point signs lifted to disjoint blocks",
        "H_over_I":tensor_ratio
    },
    "limits":[
        "addressing, majority-substitution, coded, and generic fresh-control examples are not generally two-flat defects and are outside this theorem's scope",
        "the checker uses floating logarithms; structural inequalities and the theorem are proved analytically in the report",
        "this is not an independent audit and not a full FEI check"
    ]
}
print(json.dumps(out,indent=2,sort_keys=True))
