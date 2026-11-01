from functools import lru_cache
from fractions import Fraction
from collections import defaultdict

# Exact checker for the C30 beta-splitting growth martingale candidate.
# A full ordered binary tree is represented recursively by None (leaf) or (L,R).
# For an internal clade edge C, r_C := exp(-ell_C/|C|) is treated as a formal variable.
# The checker works over Q[r_C] and does not use floating point arithmetic.

def padd(a,b):
    out=dict(a)
    for mon,c in b.items():
        out[mon]=out.get(mon,Fraction(0))+c
        if out[mon]==0:
            del out[mon]
    return out

def pneg(a): return {m:-c for m,c in a.items()}
def psub(a,b): return padd(a,pneg(b))
def pscale(a,q):
    q=Fraction(q)
    return {m:c*q for m,c in a.items() if c*q}
def pmul(a,b):
    out=defaultdict(Fraction)
    for ma,ca in a.items():
        for mb,cb in b.items():
            out[tuple(sorted(ma+mb))]+=ca*cb
    return {m:c for m,c in out.items() if c}

ONE={():Fraction(1)}
ZERO={}
def var(name): return {(name,):Fraction(1)}

@lru_cache(None)
def ordered_trees(n):
    if n==1:
        return (None,)
    out=[]
    for i in range(1,n):
        for L in ordered_trees(i):
            for R in ordered_trees(n-i):
                out.append((L,R))
    return tuple(out)

def size(T): return 1 if T is None else size(T[0])+size(T[1])

def paths(T,p=()):
    out=[p]
    if T is not None:
        out += paths(T[0],p+(0,))
        out += paths(T[1],p+(1,))
    return out

def leaf_paths(T,p=()):
    if T is None:
        return [p]
    return leaf_paths(T[0],p+(0,))+leaf_paths(T[1],p+(1,))

def sub(T,p):
    x=T
    for b in p:
        x=x[b]
    return x

def replace(T,p,new):
    if not p:
        return new
    if p[0]==0:
        return (replace(T[0],p[1:],new),T[1])
    return (T[0],replace(T[1],p[1:],new))

def insert(T,p):
    # Hit the edge carrying clade p and insert a new sibling leaf.
    return replace(T,p,(sub(T,p),None))

def ancestors(p):
    return [p[:k] for k in range(len(p))]

def sym(p):
    return 'rR' if not p else 'r'+''.join(map(str,p))

def node_surv(T,p):
    assert sub(T,p) is not None
    return var(sym(p))

def p_formula(T,p):
    # p_T(C) = |C|/n * product_{A strict ancestor C} r_A * (1-r_C),
    # with the terminal leaf factor interpreted as 1 in the extended representation.
    n=size(T); m=size(sub(T,p))
    surv=ONE
    for a in ancestors(p):
        surv=pmul(surv,node_surv(T,a))
    stop=ONE if sub(T,p) is None else psub(ONE,node_surv(T,p))
    return pscale(pmul(surv,stop),Fraction(m,n))

def p_direct(T):
    # Independent construction: average the first-stop law over each uniformly selected target leaf.
    n=size(T)
    probs={p:ZERO for p in paths(T)}
    for lp in leaf_paths(T):
        surv=ONE
        for k in range(len(lp)+1):
            p=lp[:k]
            if sub(T,p) is None:
                probs[p]=padd(probs[p],pscale(surv,Fraction(1,n)))
                break
            stop=psub(ONE,node_surv(T,p))
            probs[p]=padd(probs[p],pscale(pmul(surv,stop),Fraction(1,n)))
            surv=pmul(surv,node_surv(T,p))
    return probs

def counts(T):
    d=defaultdict(int)
    for p in paths(T):
        m=size(sub(T,p))
        if m>=2:
            d[m]+=1
    return d

def d_struct(T,p,r):
    return counts(insert(T,p))[r]-counts(T)[r]

def d_closed(T,p,r):
    # Exact one-step increment in the number of r-clades.
    s=size(sub(T,p))
    val=1 if s+1==r else 0
    for a in ancestors(p):
        sa=size(sub(T,a))
        if sa==r-1:
            val+=1
        if sa==r:
            val-=1
    return val

def peval(poly,vals):
    total=Fraction(0)
    for mon,c in poly.items():
        z=c
        for v in mon:
            z*=vals[v]
        total+=z
    return total

def run(maxn=8):
    shapes=events=dchecks=0
    max_r=0
    naive=None
    for n in range(1,maxn+1):
        for T in ordered_trees(n):
            shapes+=1
            direct=p_direct(T)
            total=ZERO
            for p in paths(T):
                pf=p_formula(T,p)
                assert direct[p]==pf, ('hit-probability mismatch',n,T,p,direct[p],pf)
                total=padd(total,pf)
                events+=1
                for r in range(2,n+2):
                    ds=d_struct(T,p,r)
                    dc=d_closed(T,p,r)
                    assert ds==dc, ('clade increment mismatch',n,T,p,r,ds,dc)
                    dchecks+=1
                    max_r=max(max_r,r)
            assert total==ONE, ('probability normalization mismatch',n,T,total)

            # Counterexample-first sanity check: N_2(n)/n is not a martingale.
            # Specialize every finite-edge survival variable to 1/2, still using exact rationals.
            if naive is None and n>=2:
                vals={sym(p):Fraction(1,2) for p in paths(T) if sub(T,p) is not None}
                old=Fraction(counts(T)[2],n)
                enew=Fraction(0)
                for p in paths(T):
                    enew += peval(p_formula(T,p),vals)*Fraction(counts(insert(T,p))[2],n+1)
                if enew!=old:
                    naive=(n,repr(T),old,enew,enew-old)

    print('PASS: exact symbolic/rational checker completed')
    print(f'max_pre_state_n={maxn}')
    print(f'ordered_full_binary_shapes_checked={shapes}')
    print(f'clade_hit_events_checked={events}')
    print(f'clade_count_increment_identities_checked={dchecks}')
    print(f'largest_resulting_clade_size_checked={max_r}')
    assert naive is not None
    n,t,old,enew,diff=naive
    print('counterexample_to_naive_N2_over_n_martingale:')
    print(f'  n={n}, tree={t}, all_internal_survivals=1/2')
    print(f'  N2/n before={old}; conditional expectation after={enew}; difference={diff}')

if __name__=='__main__':
    run(8)
