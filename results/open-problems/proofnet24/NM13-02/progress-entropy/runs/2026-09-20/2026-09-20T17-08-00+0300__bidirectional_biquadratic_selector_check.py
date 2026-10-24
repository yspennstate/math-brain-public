import itertools, json, math, random
from functools import lru_cache
import numpy as np

RHO = 2.0 / math.log(2.0)
CSTAR = 1.5 + 1.0 / math.log(2.0)
TOL = 1e-10

def walsh_probs(vals):
    a=np.array(vals,dtype=float)
    N=len(a)
    v=a.copy()
    h=1
    while h<N:
        for i in range(0,N,2*h):
            x=v[i:i+h].copy(); y=v[i+h:i+2*h].copy()
            v[i:i+h]=x+y
            v[i+h:i+2*h]=x-y
        h*=2
    v/=N
    return v*v

def entropy_probs(p):
    p=np.array(p,dtype=float)
    nz=p[p>1e-18]
    return float(-(nz*np.log2(nz)).sum())

def total_influence(vals):
    vals=np.array(vals,dtype=int)
    N=len(vals); n=N.bit_length()-1
    out=0.0
    idx=np.arange(N)
    for i in range(n):
        mask=1<<i
        base=idx[(idx & mask)==0]
        out += float(np.mean(vals[base] != vals[base|mask]))
    return out

def B_coord(vals,i):
    p=walsh_probs(vals)
    N=len(p)
    marg=np.zeros(N//2)
    low=(1<<i)-1
    for s,ps in enumerate(p):
        t=(s & low) | ((s>>(i+1))<<i)
        marg[t]+=ps
    return entropy_probs(p)-entropy_probs(marg)

def restrict_coord(vals,i,b):
    vals=np.array(vals,dtype=int)
    return tuple(vals[x] for x in range(len(vals)) if ((x>>i)&1)==b)

@lru_cache(None)
def R_order(vals,order):
    if not order: return 0.0
    i=order[0]
    neworder=tuple(j if j<i else j-1 for j in order[1:])
    return (B_coord(vals,i)
            +0.5*R_order(restrict_coord(vals,i,0),neworder)
            +0.5*R_order(restrict_coord(vals,i,1),neworder))

def all_bool(m):
    N=1<<m
    for mask in range(1<<N):
        yield tuple(-1 if (mask>>x)&1 else 1 for x in range(N))

def js_bits(P,Q):
    M=0.5*(P+Q)
    ans=0.0
    for X in (P,Q):
        nz=(X>1e-18)
        ans += 0.5*float(np.sum(X[nz]*np.log2(X[nz]/M[nz])))
    return ans

pair_cases=0
max_js_minus=-1e9
max_js_ratio=0.0
for m in range(4):
    funcs=list(all_bool(m))
    probs=[walsh_probs(f) for f in funcs]
    for ai,g in enumerate(funcs):
        for bi,h in enumerate(funcs):
            P,Q=probs[ai],probs[bi]
            corr=sum(x*y for x,y in zip(g,h))/len(g)
            j=0.5*(1.0-abs(corr))
            js=js_bits(P,Q)
            rhs=RHO*j
            max_js_minus=max(max_js_minus,js-rhs)
            if j>1e-15:
                max_js_ratio=max(max_js_ratio,js/j)
            pair_cases+=1

def truth_from_mask4(mask):
    vals=[1]*16
    for x in range(1,16):
        if (mask>>(x-1))&1: vals[x]=-1
    return tuple(vals)

n4_cases=0
n4_viol=0
n4_max_ratio=0.0
for mask in range(1<<15):
    f=truth_from_mask4(mask)
    I=total_influence(f)
    if I<1e-15:
        continue
    rA=R_order(f,(0,1,2,3))
    rY=R_order(f,(2,3,0,1))
    r=min(rA,rY)
    if r > CSTAR*I + TOL:
        n4_viol += 1
    n4_max_ratio=max(n4_max_ratio,r/I)
    n4_cases+=1

def eval_poly(n,terms):
    out=[]
    for x in range(1<<n):
        bits=[(x>>i)&1 for i in range(n)]
        p=0
        for term in terms:
            z=1
            for i in term: z &= bits[i]
            p ^= z
        out.append(-1 if p else 1)
    return tuple(out)

def random_bidegree_terms(a,y,rng):
    A=range(a); Y=range(a,a+y)
    allowed=[]
    for ra in range(0,min(2,a)+1):
        for ry in range(0,min(2,y)+1):
            if ra+ry==0: continue
            for aa in itertools.combinations(A,ra):
                for yy in itertools.combinations(Y,ry):
                    allowed.append(tuple(aa)+tuple(yy))
    return [t for t in allowed if rng.random()<0.5]

def cycle_terms(d):
    return [tuple(sorted((j,(j+1)%d,d+j,d+(j+1)%d))) for j in range(d)]

def random_quadratic_terms(n,rng):
    out=[]
    for i in range(n):
        if rng.random()<0.5: out.append((i,))
    for i in range(n):
        for j in range(i+1,n):
            if rng.random()<0.5: out.append((i,j))
    return out

def signed_translation_symmetries(vals):
    N=len(vals); out=[]
    for t in range(1,N):
        s=vals[0]*vals[t]
        ok=True
        for x in range(1,N):
            if vals[x]*vals[x^t] != s:
                ok=False; break
        if ok: out.append((t,s))
    return out

rng=random.Random(20260920)

bideg_samples=200
bideg_viol=0
bideg_max_ratio=0.0
for _ in range(bideg_samples):
    f=eval_poly(6,random_bidegree_terms(3,3,rng))
    I=total_influence(f)
    if I<1e-15: continue
    rA=R_order(f,(0,1,2,3,4,5))
    rY=R_order(f,(3,4,5,0,1,2))
    r=min(rA,rY)
    if r > CSTAR*I + TOL:
        bideg_viol += 1
    bideg_max_ratio=max(bideg_max_ratio,r/I)

cycle={}
for d in (3,4):
    f=eval_poly(2*d,cycle_terms(d))
    I=total_influence(f)
    rA=R_order(f,tuple(range(d))+tuple(range(d,2*d)))
    rY=R_order(f,tuple(range(d,2*d))+tuple(range(d)))
    syms=signed_translation_symmetries(f)
    cycle[str(d)]={
        "I":I,
        "expected_I":3*d/8,
        "min_R_over_I":min(rA,rY)/I,
        "signed_translation_symmetries":len(syms)
    }

twists={}
for d,samples in ((3,100),(4,40)):
    max_ratio=0.0; sym_fail=0; bound_fail=0
    for _ in range(samples):
        terms=cycle_terms(d)+random_quadratic_terms(2*d,rng)
        f=eval_poly(2*d,terms)
        I=total_influence(f)
        rA=R_order(f,tuple(range(d))+tuple(range(d,2*d)))
        rY=R_order(f,tuple(range(d,2*d))+tuple(range(d)))
        ratio=min(rA,rY)/I if I else 0.0
        max_ratio=max(max_ratio,ratio)
        if min(rA,rY) > CSTAR*I + TOL:
            bound_fail+=1
        if signed_translation_symmetries(f):
            sym_fail+=1
    twists[str(d)]={"samples":samples,"max_ratio":max_ratio,
                    "bound_failures":bound_fail,
                    "rigidity_failures":sym_fail}

grid_max=-1e9
for k in range(20001):
    t=k/20000
    if t==1.0:
        lhs=2*math.log(2.0)
        rhs=2.0
    else:
        lhs=(1+t)*math.log(1+t)+(1-t)*math.log(1-t)
        rhs=2*(1-math.sqrt(1-t*t))
    grid_max=max(grid_max,lhs-rhs)

result={
    "status":"PASS" if (max_js_minus<=TOL and n4_viol==0 and bideg_viol==0
                        and all(v["bound_failures"]==0 and v["rigidity_failures"]==0 for v in twists.values())
                        and all(v["signed_translation_symmetries"]==0 for v in cycle.values())
                        and grid_max<=TOL) else "FAIL",
    "constants":{"rho_2_over_ln2":RHO,"Cstar_3over2_plus_1overln2":CSTAR},
    "one_step":{"ordered_child_pairs":pair_cases,"max_JS_minus_rho_j":max_js_minus,
                "max_JS_over_j":max_js_ratio},
    "n4_exhaustive":{"canonical_nonconstant_functions":n4_cases,"violations":n4_viol,
                     "max_min_block_order_R_over_I":n4_max_ratio},
    "bidegree_3plus3":{"samples":bideg_samples,"violations":bideg_viol,
                       "max_min_block_order_R_over_I":bideg_max_ratio},
    "quartic_cycle":cycle,
    "quadratic_twists":twists,
    "scalar_js_hellinger_grid":{"points":20001,"max_lhs_minus_rhs":grid_max}
}
print(json.dumps(result,indent=2,sort_keys=True))
