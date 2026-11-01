#!/usr/bin/env python3
import json, math, random
from functools import lru_cache
from itertools import combinations

SEED=20260920
rng=random.Random(SEED)

def parity(x): return x.bit_count() & 1

def fwht(vals):
    a=[float(v) for v in vals]
    h=1
    while h<len(a):
        for i in range(0,len(a),2*h):
            for j in range(i,i+h):
                x,y=a[j],a[j+h]
                a[j],a[j+h]=x+y,x-y
        h*=2
    N=len(a)
    return [x/N for x in a]

def entropy_truth(vals):
    H=0.0
    for a in fwht(vals):
        p=a*a
        if p>0: H-=p*math.log2(p)
    return H

def influences(vals):
    N=len(vals); n=N.bit_length()-1
    out=[]
    for i in range(n):
        d=sum(vals[x]!=vals[x^(1<<i)] for x in range(N))/N
        out.append(d)
    return out

def allocation(vals):
    coeff=fwht(vals); p=[x*x for x in coeff]
    H=0.0
    for q in p:
        if q>0: H-=q*math.log2(q)
    uw={}
    N=len(p)
    for s,ps in enumerate(p):
        if ps==0: continue
        for t,pt in enumerate(p):
            if pt==0: continue
            key=(s^t,s&t)
            uw[key]=uw.get(key,0.0)+ps*pt
    Huw=-sum(q*math.log2(q) for q in uw.values() if q>0)
    return 2*H-Huw

@lru_cache(None)
def accumulated_allocation(vals):
    vals=tuple(vals)
    if all(v==vals[0] for v in vals):
        return 0.0
    N=len(vals)
    A=allocation(vals)
    child=0.0
    for z in range(N):
        der=tuple(vals[x]*vals[x^z] for x in range(N))
        child += accumulated_allocation(der)
    return A+0.5*child/N

def allocation_rhs(vals):
    js=[min(a,1-a) for a in influences(vals)]
    return 2*sum(j*math.log2(1/j) for j in js if j>0)

def pointwise_alloc_rhs(vals):
    js=[min(a,1-a) for a in influences(vals)]
    return 2*sum(j*(1-j) for j in js)

def span_subspaces(n):
    uniq={frozenset({0})}
    todo=[frozenset({0})]
    vecs=range(1,1<<n)
    while todo:
        U=todo.pop()
        for v in vecs:
            if v not in U:
                V=frozenset(set(U)|{x^v for x in U})
                if V not in uniq:
                    uniq.add(V); todo.append(V)
    return list(uniq)

def affine_flats(n):
    flats=set()
    for U in span_subspaces(n):
        unseen=set(range(1<<n))
        while unseen:
            a=next(iter(unseen))
            C=frozenset(a^u for u in U)
            flats.add(C); unseen-=set(C)
    return list(flats)

def triple_density_exact():
    out=[]
    for n in range(1,5):
        fs=affine_flats(n)
        min_num=None; min_den=None; witness=None
        checked=0; nonempty=0
        for A,B,C in combinations(fs,3):
            checked+=1
            D=A^B^C
            if not D: continue
            nonempty+=1
            x=max(len(A),len(B),len(C))
            if min_num is None or len(D)*min_den < min_num*x:
                min_num,min_den=len(D),x
                witness=[len(A),len(B),len(C),len(D)]
            assert 4*len(D)>=x
        out.append({"n":n,"flats":len(fs),"triples":checked,"nonempty_xor":nonempty,
                    "min_nonzero_ratio": None if min_num is None else f"{min_num}/{min_den}",
                    "witness_sizes":witness})
    return out

def rank_masks(rows,n):
    rows=[r for r in rows if r]
    rank=0
    for col in range(n):
        pivot=next((k for k in range(rank,len(rows)) if (rows[k]>>col)&1),None)
        if pivot is None: continue
        rows[rank],rows[pivot]=rows[pivot],rows[rank]
        for k in range(len(rows)):
            if k!=rank and ((rows[k]>>col)&1):
                rows[k]^=rows[rank]
        rank+=1
    return rank

def random_independent_rows(n,r):
    rows=[]
    while len(rows)<r:
        v=rng.randrange(1,1<<n)
        if rank_masks(rows+[v],n)>len(rows):
            rows.append(v)
    return rows

def flat_from_equations(n,r):
    rows=random_independent_rows(n,r)
    rhs=[rng.randrange(2) for _ in rows]
    mask=0
    for x in range(1<<n):
        if all(parity(row & x)==b for row,b in zip(rows,rhs)):
            mask |= 1<<x
    return mask,rows,rhs

def vals_from_mask(n,mask):
    return [-1 if (mask>>x)&1 else 1 for x in range(1<<n)]

def random_quadratic(n):
    lin=rng.randrange(1<<n)
    const=rng.randrange(2)
    nbr=[0]*n
    pairs=[]
    for i in range(n):
        for j in range(i+1,n):
            if rng.randrange(2):
                pairs.append((i,j))
                nbr[i]|=1<<j; nbr[j]|=1<<i
    rank=rank_masks(nbr,n)
    q=[]
    for x in range(1<<n):
        b=const^parity(lin & x)
        for i,j in pairs: b ^= ((x>>i)&1)&((x>>j)&1)
        q.append(-1 if b else 1)
    return q,nbr,rank

def random_three_flat_stress(samples=140):
    max_hi=0.0; max_twist=0.0; min_active_j=1.0
    cases=0
    for _ in range(samples):
        n=rng.randint(6,10)
        flats=[]
        for k in range(3):
            r=rng.randint(6,n)
            m,_,_=flat_from_equations(n,r)
            flats.append(m)
        hmask=flats[0]^flats[1]^flats[2]
        h=vals_from_mask(n,hmask)
        q,nbr,rho=random_quadratic(n)
        f=[a*b for a,b in zip(h,q)]
        Ih=sum(influences(h)); If=sum(influences(f))
        Hh=entropy_truth(h); Hf=entropy_truth(f)
        if Ih>1e-15: max_hi=max(max_hi,Hh/Ih)
        if If>1e-15: max_twist=max(max_twist,Hf/If)
        assert Hf <= Hh+rho+1e-8
        infh=influences(h); inff=influences(f)
        for i,row in enumerate(nbr):
            jh=min(infh[i],1-infh[i]); jf=min(inff[i],1-inff[i])
            if row:
                min_active_j=min(min_active_j,jf)
                assert jf+1e-10>=13/32
                assert jf+1e-10>=jh
            else:
                assert abs(jf-jh)<1e-9
        cases+=1
    return {"cases":cases,"max_H_over_I_character_leaf":max_hi,
            "max_H_over_I_quadratic_twist":max_twist,
            "min_active_quadratic_row_folded_influence":min_active_j}

def sibling_checks():
    out=[]
    for n in range(2,9):
        r=max(1,n-1)
        A=[];B=[];C=[]
        for x in range(1<<n):
            inA=(x & ((1<<r)-1))==0
            if inA:
                A.append(x)
                if (x>>r)&1: C.append(x)
                else: B.append(x)
        D=set(A)^set(B)^set(C)
        assert not D
        out.append({"n":n,"codims":[r,n,n],"xor_size":0})
    return out

def named_families():
    fam={}
    for n in range(2,7):
        vals=[-1]+[1]*((1<<n)-1)
        fam[f"one_point_{n}"]=vals
    for n in [3,5]:
        vals=[]
        for x in range(1<<n):
            vals.append(1 if x.bit_count()>=((n+1)//2) else -1)
        fam[f"majority_{n}"]=vals
    for n in [2,4,6]:
        vals=[]
        for x in range(1<<n):
            b=0
            for i in range(0,n,2):
                b ^= ((x>>i)&1)&((x>>(i+1))&1)
            vals.append(-1 if b else 1)
        fam[f"quadratic_{n}"]=vals
    n=6; vals=[]
    for x in range(1<<n):
        addr=(x&1)+2*((x>>1)&1)
        bit=(x>>(2+addr))&1
        vals.append(-1 if bit else 1)
    fam["addressing_k2"]=vals
    vals=[]
    for x in range(1<<5):
        z=x&7; y=(x>>3)&3
        seed=-1 if y==0 else 1
        vals.append(seed if z==0 else 1)
    fam["fresh_control_c3_onepoint2"]=vals
    w3=[-1]+[1]*7
    vals=[a*b for a in w3 for b in w3]
    fam["tensor_w3_w3"]=vals
    return fam

def allocation_checks():
    rows=[]
    max_total=0.0
    exhaustive=0
    for n in range(1,4):
        N=1<<n
        for bits in range(1<<N):
            vals=tuple(1 if (bits>>x)&1 else -1 for x in range(N))
            A=allocation(vals); pr=pointwise_alloc_rhs(vals)
            assert A<=pr+1e-9
            T=accumulated_allocation(vals); rhs=allocation_rhs(vals)
            assert T<=rhs+1e-8
            if rhs>1e-15: max_total=max(max_total,T/rhs)
            exhaustive+=1
    for name,vals in named_families().items():
        A=allocation(tuple(vals)); pr=pointwise_alloc_rhs(vals)
        T=accumulated_allocation(tuple(vals)); rhs=allocation_rhs(vals)
        assert A<=pr+1e-9 and T<=rhs+1e-8
        rows.append({"name":name,"n":len(vals).bit_length()-1,
                     "A":A,"pointwise_rhs":pr,"T":T,"log_rhs":rhs,
                     "T_over_log_rhs": None if rhs==0 else T/rhs})
    return {"exhaustive_truth_tables":exhaustive,"max_T_over_bound_exhaustive":max_total,
            "named":rows}

def main():
    result={
      "status":"PASS",
      "seed":SEED,
      "exact_three_flat_density":triple_density_exact(),
      "sibling_cancellation":sibling_checks(),
      "random_high_codim_three_flat":random_three_flat_stress(),
      "accumulated_allocation":allocation_checks(),
      "limitations":[
        "Affine-flat density checks are exhaustive only through ambient dimension 4; the report contains the all-dimensional proof.",
        "High-codimension three-flat/quadratic checks are deterministic-seed floating-point stress tests, not proofs.",
        "Allocation checks use floating logarithms; the universal allocation inequality is proved analytically in the report.",
        "No independent audit, Lean verification, or exhaustive all-dimensional Boolean search is performed."
      ]
    }
    print(json.dumps(result,indent=2,sort_keys=True))

if __name__=="__main__":
    main()
