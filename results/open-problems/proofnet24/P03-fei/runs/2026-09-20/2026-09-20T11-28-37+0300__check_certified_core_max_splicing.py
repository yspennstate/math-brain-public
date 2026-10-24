#!/usr/bin/env python3
import math, random, json

LN2 = math.log(2.0)
CCHI = 2.0 + 1.0/(math.sqrt(math.e)*LN2)
CREC = 2.0/LN2
CQUAD_NC = CCHI + CREC
TOL = 2e-10

def fwt(vals):
    a = [float(x) for x in vals]
    n = len(a)
    h = 1
    while h < n:
        for i in range(0,n,2*h):
            for j in range(i,i+h):
                x,y = a[j],a[j+h]
                a[j],a[j+h] = x+y,x-y
        h *= 2
    return [x/n for x in a]

def entropy(vals):
    a=fwt(vals)
    ans=0.0
    for x in a:
        p=x*x
        if p>0.0:
            ans -= p*math.log(p,2)
    return ans

def influences(vals):
    N=len(vals); n=(N.bit_length()-1)
    out=[]
    for i in range(n):
        d=sum(vals[x] != vals[x^(1<<i)] for x in range(N))
        out.append(d/N)
    return out

def total_influence(vals):
    return sum(influences(vals))

def parent_entropy_decrement(g,h):
    a=fwt(g); b=fwt(h)
    hp=0.0
    for x,y in zip(a,b):
        for z in ((x+y)/2.0,(x-y)/2.0):
            p=z*z
            if p>0:
                hp -= p*math.log(p,2)
    return hp - 0.5*(entropy(g)+entropy(h))

def h2(x):
    if x <= 0.0 or x >= 1.0:
        return 0.0
    return -x*math.log(x,2)-(1-x)*math.log(1-x,2)

def char_delta_formula(delta):
    W=4.0*delta*(1.0-delta)
    q=(1.0-delta)**2+delta**2
    B=2.0*delta*(1.0-delta)+q*h2(delta**2/q if q else 0.0)
    JS=h2(W/2.0)-0.5*h2(W)
    return B+JS

def nested_vals(n, rng):
    order=list(range(n))
    rng.shuffle(order)
    canal=[rng.randrange(2) for _ in range(n)]
    side=[1 if rng.randrange(2) else -1 for _ in range(n)]
    terminal=1 if rng.randrange(2) else -1
    vals=[]
    for x in range(1<<n):
        y=terminal
        for t,i in enumerate(order):
            if ((x>>i)&1)==canal[t]:
                y=side[t]
                break
        vals.append(y)
    return vals

def quadratic_sign(n,rng, pair_mask=None):
    lin=[rng.randrange(2) for _ in range(n)]
    c=rng.randrange(2)
    if pair_mask is None:
        pairs={(i,j):rng.randrange(2) for i in range(n) for j in range(i+1,n)}
    else:
        pairs=dict(pair_mask)
    vals=[]
    for x in range(1<<n):
        p=c
        for i,b in enumerate(lin):
            if b and ((x>>i)&1): p ^= 1
        for (i,j),b in pairs.items():
            if b and ((x>>i)&1) and ((x>>j)&1): p ^= 1
        vals.append(-1 if p else 1)
    return vals,pairs

def multiply(a,b):
    return [x*y for x,y in zip(a,b)]

def lift_block(vals, block, n):
    out=[]
    for x in range(1<<n):
        y=0
        for k,i in enumerate(block):
            y |= ((x>>i)&1)<<k
        out.append(vals[y])
    return out

# 1. Exhaustive character-child check through residual dimension 4.
char_cases=0
max_formula_err=0.0
max_char_violation=-1e100
max_char_ratio=0.0
for m in range(0,5):
    N=1<<m
    g=[1]*N
    for mask in range(1<<N):
        h=[1 if ((mask>>x)&1) else -1 for x in range(N)]
        raw=sum(a!=b for a,b in zip(g,h))/N
        if raw>0.5:
            h=[-x for x in h]
            delta=1.0-raw
        else:
            delta=raw
        dec=parent_entropy_decrement(g,h)
        formula=char_delta_formula(delta)
        max_formula_err=max(max_formula_err,abs(dec-formula))
        viol=dec-5.0*delta
        max_char_violation=max(max_char_violation,viol)
        if delta>0:
            max_char_ratio=max(max_char_ratio,dec/delta)
        char_cases += 1

# 2. Dense scalar check, independent of Walsh enumeration.
grid_n=200000
grid_max_violation=-1e100
grid_max_ratio=0.0
grid_arg=0.0
for k in range(1,grid_n+1):
    d=0.5*k/grid_n
    val=char_delta_formula(d)
    grid_max_violation=max(grid_max_violation,val-5*d)
    if val/d>grid_max_ratio:
        grid_max_ratio=val/d; grid_arg=d

# 3. Random quadratic-twisted nested-canalizing cores.
rng=random.Random(20260920112837)
nested_cases=2500
max_nested_violation=-1e100
max_nested_ratio=0.0
for _ in range(nested_cases):
    n=rng.randrange(1,10)
    h=nested_vals(n,rng)
    q,_=quadratic_sign(n,rng)
    f=multiply(h,q)
    I=total_influence(f); H=entropy(f)
    if I>0:
        max_nested_ratio=max(max_nested_ratio,H/I)
        max_nested_violation=max(max_nested_violation,H-CQUAD_NC*I)
    else:
        max_nested_violation=max(max_nested_violation,H)

# 4. Random products of nested cores under arbitrary global quadratic twists.
product_cases=2500
max_product_violation=-1e100
max_product_ratio=0.0
max_cross_inf_err=0.0
cross_checks=0
for _ in range(product_cases):
    n=rng.randrange(2,10)
    cut1=rng.randrange(1,n)
    if n>=4 and rng.random()<0.5:
        cut2=rng.randrange(cut1+1,n) if cut1+1<n else n
        blocks=[list(range(0,cut1)),list(range(cut1,cut2))]
        if cut2<n: blocks.append(list(range(cut2,n)))
    else:
        blocks=[list(range(0,cut1)),list(range(cut1,n))]
    base=[1]*(1<<n)
    for B in blocks:
        hv=nested_vals(len(B),rng)
        base=multiply(base,lift_block(hv,B,n))
    q,pairs=quadratic_sign(n,rng)
    f=multiply(base,q)
    I=total_influence(f); H=entropy(f)
    if I>0:
        max_product_ratio=max(max_product_ratio,H/I)
        max_product_violation=max(max_product_violation,H-CQUAD_NC*I)
    else:
        max_product_violation=max(max_product_violation,H)
    block_of={}
    for bi,B in enumerate(blocks):
        for i in B: block_of[i]=bi
    inf=influences(f)
    active_endpoints=set()
    for (i,j),b in pairs.items():
        if b and block_of[i]!=block_of[j]:
            active_endpoints.add(i); active_endpoints.add(j)
    for i in active_endpoints:
        max_cross_inf_err=max(max_cross_inf_err,abs(inf[i]-0.5))
        cross_checks += 1

status="PASS"
checks = {
    "character_cases": char_cases,
    "max_character_formula_error": max_formula_err,
    "max_character_5delta_violation": max_char_violation,
    "max_character_ratio_exhaustive": max_char_ratio,
    "scalar_grid_points": grid_n,
    "scalar_grid_max_5delta_violation": grid_max_violation,
    "scalar_grid_max_ratio": grid_max_ratio,
    "scalar_grid_argmax": grid_arg,
    "nested_quadratic_cases": nested_cases,
    "max_nested_H_over_I": max_nested_ratio,
    "max_nested_C_violation": max_nested_violation,
    "product_cases": product_cases,
    "max_product_H_over_I": max_product_ratio,
    "max_product_C_violation": max_product_violation,
    "cross_edge_endpoint_checks": cross_checks,
    "max_cross_edge_half_influence_error": max_cross_inf_err,
    "Cchi": CCHI,
    "Crecombination": CREC,
    "Cquad_nested": CQUAD_NC,
}
if (max_formula_err>TOL or max_char_violation>TOL or grid_max_violation>TOL or
    max_nested_violation>TOL or max_product_violation>TOL or max_cross_inf_err>TOL):
    status="FAIL"
print(json.dumps({"status":status,"checks":checks},indent=2,sort_keys=True))
if status!="PASS":
    raise SystemExit(1)
