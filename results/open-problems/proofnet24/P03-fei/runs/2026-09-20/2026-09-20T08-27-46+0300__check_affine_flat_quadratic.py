import itertools, math, random, json

SEED = 202609200827
SAMPLES_PER_CUTOFF = 2500
FLAT_SAMPLES = 500

def h2(t):
    if t <= 0.0 or t >= 1.0:
        return 0.0
    return -t*math.log2(t) - (1.0-t)*math.log2(1.0-t)

def kappa(s):
    if s <= 1:
        return 0.0
    return (2**(s-1))*h2(2**(1-s))

def c_local(s):
    a = 0.5 - 2.0**(-s)
    return h2(a)/a

def c_fei(s):
    return max(kappa(s), 4.0, c_local(s) + 2.0/math.log(2.0))

def fwht(vals):
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
    H=0.0
    for z in fwht(vals):
        p=z*z
        if p>0:
            H -= p*math.log2(p)
    return H

def influences(vals,d):
    N=1<<d
    ans=[]
    for i in range(d):
        bit=1<<i
        ans.append(sum(vals[x]!=vals[x^bit] for x in range(N))/N)
    return ans

def B_i(vals,d,i):
    p=[z*z for z in fwht(vals)]
    bit=1<<i
    ans=0.0
    for s in range(1<<d):
        if s & bit:
            continue
        a,b=p[s],p[s|bit]
        m=a+b
        if m>0 and a>0 and b>0:
            t=b/m
            ans += m*h2(t)
    return ans

def remove_bit(x,i):
    return (x & ((1<<i)-1)) | ((x>>(i+1))<<i)

def restrict_vals(vals,d,i,b):
    return [vals[x] for x in range(1<<d) if ((x>>i)&1)==b]

def restrict_A(A,d,i,b):
    return frozenset(remove_bit(x,i) for x in A if ((x>>i)&1)==b)

def restrict_polar(rows,d,i):
    return [remove_bit(rows[a] & ~(1<<i),i) for a in range(d) if a!=i]

def gf2_rank(rows,n):
    rows=list(rows)
    rank=0
    for col in range(n-1,-1,-1):
        pivot=next((j for j in range(rank,len(rows)) if (rows[j]>>col)&1),None)
        if pivot is None:
            continue
        rows[rank],rows[pivot]=rows[pivot],rows[rank]
        for j in range(len(rows)):
            if j!=rank and ((rows[j]>>col)&1):
                rows[j] ^= rows[rank]
        rank += 1
    return rank

def random_independent_rows(n,r,rng):
    rows=[]
    while len(rows)<r:
        v=rng.randrange(1,1<<n)
        if gf2_rank(rows+[v],n)>len(rows):
            rows.append(v)
    return rows

def affine_from_constraints(n,rows,bits):
    return frozenset(
        x for x in range(1<<n)
        if all((((row & x).bit_count() & 1)==b) for row,b in zip(rows,bits))
    )

def all_linear_subspaces(n):
    vecs=list(range(1,1<<n))
    subs={frozenset({0})}
    frontier=[frozenset({0})]
    while frontier:
        U=frontier.pop()
        for v in vecs:
            if v in U:
                continue
            V=frozenset(set(U)|{x^v for x in U})
            if V not in subs:
                subs.add(V)
                frontier.append(V)
    return list(subs)

def all_affine_subspaces(n):
    out=set()
    for V in all_linear_subspaces(n):
        for a in range(1<<n):
            out.add(frozenset(x^a for x in V))
    return list(out)

def quadratic_from_mask(n,mask):
    lin = mask & ((1<<n)-1)
    qm = mask>>n
    rows=[0]*n
    idx=0
    for i in range(n):
        for j in range(i+1,n):
            if (qm>>idx)&1:
                rows[i] |= 1<<j
                rows[j] |= 1<<i
            idx += 1
    vals=[]
    for x in range(1<<n):
        bit=(lin & x).bit_count() & 1
        for i in range(n):
            if (x>>i)&1:
                bit ^= (rows[i] & x & ~((1<<(i+1))-1)).bit_count() & 1
        vals.append(-1 if bit else 1)
    return vals,rows

def defect_sign(n,A):
    return [-1 if x in A else 1 for x in range(1<<n)]

def product(a,b):
    return [x*y for x,y in zip(a,b)]

def tree_stats(vals,rows,A,d,s):
    Ivec=influences(vals,d) if d else []
    Iroot=sum(Ivec)
    Hroot=entropy(vals)
    if not A:
        return dict(R=0.0,Q=0.0,IL=Iroot,local_count=0,min_j=1.0,
                    max_local_ratio=0.0,leaf_violation=Hroot-kappa(s)*Iroot)
    size=len(A)
    lg=size.bit_length()-1
    assert (1<<lg)==size
    r=d-lg
    polar_nonzero=any(rows)
    if r<=s or not polar_nonzero:
        leafC=kappa(s) if r<=s else 4.0
        return dict(R=0.0,Q=0.0,IL=Iroot,local_count=0,min_j=1.0,
                    max_local_ratio=0.0,leaf_violation=Hroot-leafC*Iroot)
    i=next(i for i,row in enumerate(rows) if row)
    alpha=Ivec[i]
    j=min(alpha,1-alpha)
    Bi=B_i(vals,d,i)
    ch=[]
    for b in (0,1):
        ch.append(tree_stats(
            restrict_vals(vals,d,i,b),
            restrict_polar(rows,d,i),
            restrict_A(A,d,i,b),
            d-1,s))
    return dict(
        R=Bi+0.5*(ch[0]["R"]+ch[1]["R"]),
        Q=alpha+0.5*(ch[0]["Q"]+ch[1]["Q"]),
        IL=0.5*(ch[0]["IL"]+ch[1]["IL"]),
        local_count=1+ch[0]["local_count"]+ch[1]["local_count"],
        min_j=min(j,ch[0]["min_j"],ch[1]["min_j"]),
        max_local_ratio=max(Bi/j if j else 0.0,
                            ch[0]["max_local_ratio"],ch[1]["max_local_ratio"]),
        leaf_violation=max(ch[0]["leaf_violation"],ch[1]["leaf_violation"])
    )

exhaustive_cases=0
max_exhaustive_ratio=0.0
max_kappa4_violation=-1e100
for n in range(1,5):
    flats=all_affine_subspaces(n)
    totalq=1<<(n+n*(n-1)//2)
    for A in flats:
        ds=defect_sign(n,A)
        for mask in range(totalq):
            qv,_=quadratic_from_mask(n,mask)
            vals=product(qv,ds)
            I=sum(influences(vals,n))
            H=entropy(vals)
            if I>0:
                max_exhaustive_ratio=max(max_exhaustive_ratio,H/I)
            max_kappa4_violation=max(max_kappa4_violation,H-kappa(4)*I)
            exhaustive_cases += 1

sampled={}
for s in (3,4):
    rng=random.Random(SEED+s)
    max_budget_error=0.0
    min_j=1.0
    max_local_ratio=0.0
    max_allocation_violation=-1e100
    max_fei_violation=-1e100
    max_leaf_violation=-1e100
    internal_nodes=0
    Aconst=max(kappa(s),4.0)
    C=c_fei(s)
    for _ in range(SAMPLES_PER_CUTOFF):
        n=rng.randint(max(5,s+1),8)
        r=rng.randint(s+1,n)
        cons=random_independent_rows(n,r,rng)
        bits=[rng.randrange(2) for _ in range(r)]
        A=affine_from_constraints(n,cons,bits)
        mask=rng.randrange(1<<(n+n*(n-1)//2))
        qv,prows=quadratic_from_mask(n,mask)
        vals=product(qv,defect_sign(n,A))
        I=sum(influences(vals,n))
        H=entropy(vals)
        st=tree_stats(vals,prows,A,n,s)
        max_budget_error=max(max_budget_error,abs(st["Q"]+st["IL"]-I))
        min_j=min(min_j,st["min_j"])
        max_local_ratio=max(max_local_ratio,st["max_local_ratio"])
        max_allocation_violation=max(
            max_allocation_violation,
            st["R"]+Aconst*st["IL"]-Aconst*I)
        max_fei_violation=max(max_fei_violation,H-C*I)
        max_leaf_violation=max(max_leaf_violation,st["leaf_violation"])
        internal_nodes += st["local_count"]
    sampled[str(s)]={
        "samples":SAMPLES_PER_CUTOFF,
        "internal_nodes":internal_nodes,
        "min_internal_folded_influence":min_j,
        "required_internal_folded_influence":0.5-2.0**(-s),
        "max_local_B_over_j":max_local_ratio,
        "local_constant":c_local(s),
        "max_influence_budget_error":max_budget_error,
        "max_leaf_bound_violation":max_leaf_violation,
        "max_hereditary_allocation_violation":max_allocation_violation,
        "max_direct_FEI_violation":max_fei_violation
    }

max_flat_formula_ratio=0.0
for r in range(1,31):
    delta=2.0**(-r)
    p0=(1-2*delta)**2
    p=4*delta*delta
    H=0.0
    if p0>0:
        H -= p0*math.log2(p0)
    H -= (2**r-1)*p*math.log2(p)
    max_flat_formula_ratio=max(max_flat_formula_ratio,H/(2*delta*r))

rng=random.Random(SEED+99)
max_oblique_flat_violation=-1e100
for _ in range(FLAT_SAMPLES):
    n=rng.randint(3,10)
    r=rng.randint(1,n)
    cons=random_independent_rows(n,r,rng)
    bits=[rng.randrange(2) for _ in range(r)]
    A=affine_from_constraints(n,cons,bits)
    lin=rng.randrange(1<<n)
    qv,_=quadratic_from_mask(n,lin)
    vals=product(qv,defect_sign(n,A))
    I=sum(influences(vals,n))
    H=entropy(vals)
    max_oblique_flat_violation=max(max_oblique_flat_violation,H-4*I)

out={
    "status":"PASS",
    "constants":{
        "kappa3":kappa(3),
        "kappa4":kappa(4),
        "c3":c_local(3),
        "c4":c_local(4),
        "hereditary_cutoff3_constant":max(kappa(3),4.0),
        "FEI_cutoff3_constant":c_fei(3),
        "FEI_cutoff4_constant":c_fei(4)
    },
    "exhaustive":{
        "dimensions":"1..4",
        "quadratic_times_affine_flat_cases":exhaustive_cases,
        "max_H_over_I":max_exhaustive_ratio,
        "max_degree4_bound_violation":max_kappa4_violation
    },
    "sampled_trees":sampled,
    "flat_leaf":{
        "formula_codimensions":"1..30",
        "max_formula_H_over_2delta_r":max_flat_formula_ratio,
        "random_oblique_affine_character_cases":FLAT_SAMPLES,
        "max_H_minus_4I":max_oblique_flat_violation
    }
}
print(json.dumps(out,indent=2,sort_keys=True))
