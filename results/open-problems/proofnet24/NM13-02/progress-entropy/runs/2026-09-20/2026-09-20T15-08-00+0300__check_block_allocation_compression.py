#!/usr/bin/env python3
import itertools, math, random, json

TOL=2e-10

def wht(vals):
    a=[float(x) for x in vals]
    N=len(a); h=1
    while h<N:
        for s in range(0,N,2*h):
            for j in range(s,s+h):
                x=a[j]; y=a[j+h]
                a[j]=x+y; a[j+h]=x-y
        h*=2
    return [x/N for x in a]

def hprob(ps):
    z=0.0
    for p in ps:
        if p>1e-18:
            z-=p*math.log2(p)
    return z

def h2(p):
    if p<=1e-18 or p>=1-1e-18: return 0.0
    return -p*math.log2(p)-(1-p)*math.log2(1-p)

def restrict_vals(vals,n,i,b):
    out=[]
    for r in range(1<<(n-1)):
        lo=r & ((1<<i)-1)
        hi=r>>i
        idx=lo | (hi<<(i+1)) | (b<<i)
        out.append(vals[idx])
    return out

def B_coord(vals,n,i):
    a=wht(vals); out=0.0
    for mask in range(1<<n):
        if (mask>>i)&1: continue
        u=a[mask]; v=a[mask|(1<<i)]
        w=u*u+v*v
        if w>1e-18:
            out += w*h2(v*v/w)
    return out

def B_block(vals,n,A):
    A=set(A); C=[j for j in range(n) if j not in A]
    a=wht(vals); groups={}
    for mask,x in enumerate(a):
        p=x*x
        key=0
        for q,j in enumerate(C): key |= ((mask>>j)&1)<<q
        groups.setdefault(key,[]).append(p)
    out=0.0
    for ps in groups.values():
        s=sum(ps)
        if s>1e-18:
            out += s*hprob([p/s for p in ps])
    return out

def R_prefix(vals,n,order):
    states=[(vals,list(range(n)),1.0)]
    R=0.0
    for orig in order:
        nxt=[]
        for v,labels,w in states:
            i=labels.index(orig)
            R += w*B_coord(v,len(labels),i)
            for b in (0,1):
                nxt.append((restrict_vals(v,len(labels),i,b),labels[:i]+labels[i+1:],w/2))
        states=nxt
    return R

def influence(vals,n,i):
    bad=0
    for x in range(1<<n):
        if vals[x]!=vals[x^(1<<i)]: bad+=1
    return bad/(1<<n)

def recursive_majority_bits(d):
    # return phase bit P_d truth table, with h=(-1)^P; d=0 is one bit
    P=[0,1]
    n=1
    for _ in range(d):
        old=P; oldn=n
        n=3*oldn
        P=[]
        mask=(1<<oldn)-1
        for x in range(1<<n):
            a=x & mask
            b=(x>>oldn)&mask
            c=(x>>(2*oldn))&mask
            pa=old[a]; pb=old[b]; pc=old[c]
            P.append((pa*pb)^(pa*pc)^(pb*pc))
    return P,n

def controller_family(d,m):
    P,nA=recursive_majority_bits(d)
    n=nA+m
    vals=[]
    maskA=(1<<nA)-1
    for x in range(1<<n):
        a=x&maskA
        y=x>>nA
        delta = 1 if y==0 else 0
        phase=P[a]*delta
        vals.append(-1 if phase else 1)
    return vals,n,nA

max_gap=-1e9; max_ratio=0.0; cases=0
# Exhaust all Boolean functions through n=3, modulo global sign, all nonempty blocks and all fixed orders.
for n in range(1,4):
    N=1<<n
    for code in range(1<<(N-1)):
        vals=[1]+[1 if (code>>(k-1))&1 else -1 for k in range(1,N)]
        for k in range(1,n+1):
            for A in itertools.combinations(range(n),k):
                BB=B_block(vals,n,A)
                for order in itertools.permutations(A):
                    R=R_prefix(vals,n,order)
                    gap=R-BB
                    max_gap=max(max_gap,gap)
                    if BB>1e-14: max_ratio=max(max_ratio,R/BB)
                    if gap>TOL:
                        raise AssertionError(("block",n,code,A,order,R,BB,gap))
                    cases+=1

# Deterministic n=4 sample, all blocks and all orders.
rng=random.Random(202609201508)
random_cases=0
for _ in range(600):
    n=4; N=1<<n
    vals=[rng.choice((-1,1)) for _ in range(N)]
    for k in range(1,n+1):
        for A in itertools.combinations(range(n),k):
            BB=B_block(vals,n,A)
            for order in itertools.permutations(A):
                R=R_prefix(vals,n,order)
                gap=R-BB
                max_gap=max(max_gap,gap)
                if BB>1e-14: max_ratio=max(max_ratio,R/BB)
                if gap>TOL:
                    raise AssertionError(("random4",A,order,R,BB,gap))
                random_cases+=1

# Check balanced-controller formulas and the <4 hereditary certificate on explicit connected cores.
family=[]
Cchi=2+1/(math.sqrt(math.e)*math.log(2))
for d in (1,):
    for m in range(1,6):
        vals,n,nA=controller_family(d,m)
        A=tuple(range(nA))
        BB=B_block(vals,n,A)
        Rp=R_prefix(vals,n,A)
        alpha=2.0**(-m)
        Ih=(1.5)**d
        Hh=4*(Ih-1)
        IA=alpha*Ih
        IL=m*alpha
        bound=h2(alpha)+alpha*Hh
        total_bound=bound+Cchi*IL
        Iroot=sum(influence(vals,n,i) for i in range(n))
        if abs(Iroot-(IA+IL))>1e-12: raise AssertionError(("Iformula",d,m,Iroot,IA+IL))
        if BB-bound>TOL or Rp-BB>TOL or total_bound-4*Iroot>TOL:
            raise AssertionError(("family",d,m,Rp,BB,bound,total_bound,4*Iroot))
        family.append({
            "d":d,"m":m,"n":n,"B_A":BB,"R_prefix":Rp,
            "B_A_upper":bound,"I_A":IA,"I_leaf_avg":IL,
            "I_root":Iroot,"certificate_over_I":total_bound/Iroot,
        })

formula_max=0.0
formula_arg=None
for d in range(1,31):
    Ih=(1.5)**d
    Hh=4*(Ih-1)
    for m in range(1,41):
        alpha=2.0**(-m)
        total=(h2(alpha)+alpha*Hh+Cchi*m*alpha)/(alpha*(Ih+m))
        if total>formula_max:
            formula_max=total; formula_arg=(d,m,total)
        if total>=4+1e-12:
            raise AssertionError(("formula4",d,m,total))

out={
    "status":"PASS",
    "theorem":"For every Boolean f, every physical block A, and every fixed order of A, the accumulated hereditary allocation while completely querying A is <= H(S_A|S_Ac). Analytic proof covers adaptive orders as well.",
    "exhaustive_dimensions":[1,2,3],
    "exhaustive_fixed_order_cases":cases,
    "deterministic_dimension4_functions":600,
    "deterministic_dimension4_fixed_order_cases":random_cases,
    "max_R_minus_block_conditional_entropy":max_gap,
    "max_R_over_block_conditional_entropy_positive":max_ratio,
    "controller_family":family,
    "Cchi":Cchi,
    "controller_formula_max_d1to30_m1to40":formula_max,
    "controller_formula_argmax":formula_arg,
    "notes":[
        "Finite checks are sanity checks only; the theorem is proved analytically by induction plus concavity of conditional entropy.",
        "The controller-family total_bound includes the inherited one-point-defect hereditary constant only for checking the stated grafted certificate."
    ]
}
print(json.dumps(out,indent=2,sort_keys=True))
