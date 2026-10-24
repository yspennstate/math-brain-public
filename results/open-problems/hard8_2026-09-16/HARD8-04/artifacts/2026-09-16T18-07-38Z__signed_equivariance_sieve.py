#!/usr/bin/env python3
from itertools import permutations, product
from functools import lru_cache
from math import isqrt

P = 523
N = P - 1

# Signed permutation R acts by R e_i = signs[i] e_{perm[i]}.
def key(R):
    p,s = R
    return tuple(p)+tuple(s)

def identity():
    return ((0,1,2,3),(1,1,1,1))

def compose(R,S):  # R after S
    pR,sR=R; pS,sS=S
    p=tuple(pR[pS[i]] for i in range(4))
    s=tuple(sS[i]*sR[pS[i]] for i in range(4))
    return (p,s)

def inverse(R):
    p,s=R
    pinv=[0]*4
    sinv=[0]*4
    for i in range(4):
        pinv[p[i]]=i
        sinv[p[i]]=s[i]
    # R e_i=s_i e_p(i); R^{-1}e_j=s_{p^{-1}(j)}e_{p^{-1}(j)}
    return (tuple(pinv),tuple(sinv))

def power(R,k):
    out=identity(); base=R
    while k:
        if k&1: out=compose(base,out)
        base=compose(base,base); k//=2
    return out

def order(R):
    x=identity()
    for k in range(1,25):
        x=compose(R,x)
        if x==identity(): return k
    raise RuntimeError('order too large')

def act(R,v):
    p,s=R
    y=[0,0,0,0]
    for i,x in enumerate(v):
        y[p[i]] += s[i]*x
    return tuple(y)

def add(a,b): return tuple(x+y for x,y in zip(a,b))
def sub(a,b): return tuple(x-y for x,y in zip(a,b))

def basis(i,sgn=1):
    v=[0,0,0,0]; v[i]=sgn; return tuple(v)

ALL=[]
for p in permutations(range(4)):
    for s in product((-1,1),repeat=4):
        ALL.append((tuple(p),tuple(s)))
ALL.sort(key=key)
assert len(ALL)==384 and len(set(ALL))==384
ALLSET=set(ALL)
assert all(compose(R,inverse(R))==identity() for R in ALL)

# Exact conjugacy classes of B4.
unseen=set(ALL)
classes=[]
while unseen:
    seed=min(unseen,key=key)
    cls={compose(compose(g,seed),inverse(g)) for g in ALL}
    assert cls <= ALLSET
    classes.append(tuple(sorted(cls,key=key)))
    unseen -= cls
classes.sort(key=lambda c:key(c[0]))
assert sum(len(c) for c in classes)==384
assert len(classes)==20
orders=sorted(set(order(c[0]) for c in classes))
assert orders==[1,2,3,4,6,8]

# All exact integer row-sum vectors r with ||r||^2 = 523.
# Pair-square generation avoids a 45^4 loop.
pairs={}
B=isqrt(P)
for a in range(-B,B+1):
    for b in range(-B,B+1):
        pairs.setdefault(a*a+b*b,[]).append((a,b))
RVECS=[]
for s1,lst1 in pairs.items():
    s2=P-s1
    if s2 not in pairs: continue
    for a,b in lst1:
        for c,d in pairs[s2]:
            RVECS.append((a,b,c,d))
RVECS=sorted(set(RVECS))
assert len(RVECS)==4192
assert all(sum(x*x for x in r)==P for r in RVECS)

DIVS=[d for d in range(1,N+1) if N%d==0]
assert DIVS==[1,2,3,6,9,18,29,58,87,174,261,522]

basis_signed=[basis(i,s) for i in range(4) for s in (-1,1)]

def row_gate(rep,d):
    m=order(rep)
    if d%m: return []
    L=d//m
    q0s=[q for q in basis_signed if act(rep,q)==q]
    out=[]
    for q0 in q0s:
        for r in RVECS:
            if act(rep,r)!=r: continue
            if all((r[i]-q0[i])%L==0 for i in range(4)):
                out.append((q0,r))
    return out

summary={}
viable_by_d={}
for d in DIVS:
    rows=[]
    for idx,cls in enumerate(classes):
        rep=cls[0]; m=order(rep)
        if d%m: continue
        pairs_gate=row_gate(rep,d)
        if pairs_gate:
            rows.append((idx,m,len(cls),d//m,len(pairs_gate),rep,pairs_gate))
    viable_by_d[d]=rows
    summary[d]=[(m,cs,L,np) for _,m,cs,L,np,_,__ in rows]

# Expected row-sum/congruence gate at the high-symmetry orders.
assert summary[522]==[]
assert summary[261]==[]
assert summary[174]==[]
assert summary[87]==[]
assert summary[58]==[]
assert summary[29]==[]
assert len(summary[18])==3 and all(x[0]==2 and x[2]==9 for x in summary[18])
assert len(summary[9])==1 and summary[9][0][0]==1 and summary[9][0][2]==9
assert len(summary[6])==3 and all(x[0]==2 and x[2]==3 for x in summary[6])
assert sorted(x[0] for x in summary[3])==[1,3]
assert len(summary[2])==3 and all(x[0]==2 and x[2]==1 for x in summary[2])

# For d=18, go beyond row sums: each nonzero K-orbit contributes the exact
# orbit-sum sum_{j=0}^{17} R^j b. There are exactly 29 nonzero K-orbits.
def orbit_contributions(rep,d):
    vals=[]
    for b in basis_signed:
        v=(0,0,0,0)
        x=b
        for _ in range(d):
            v=add(v,x)
            x=act(rep,x)
        vals.append((b,v))
    # unique contribution vectors for reachability
    uniq=sorted(set(v for _,v in vals))
    return vals,uniq

# Exact reachability by n orbit contributions. Target-aware recursion with
# canonical nondecreasing contribution index converts sequences to multisets.
def reachable_multiset(target, contributions, n):
    contrib=tuple(contributions)
    k=len(contrib)
    maxabs=[[0]*4 for _ in range(k+1)]
    for start in range(k-1,-1,-1):
        for j in range(4):
            maxabs[start][j]=max(maxabs[start+1][j],abs(contrib[start][j]))
    @lru_cache(None)
    def rec(start,left,res):
        if left==0:
            return res==(0,0,0,0)
        if start>=k:
            return False
        for j in range(4):
            if abs(res[j])>left*maxabs[start][j]:
                return False
        # choose count c of current contribution, then recurse on higher indices
        v=contrib[start]
        for c in range(left+1):
            newres=tuple(res[j]-c*v[j] for j in range(4))
            if rec(start+1,left-c,newres):
                return True
        return False
    return rec(0,n,tuple(target))

D18=[]
for idx,m,cs,L,np,rep,pairs_gate in viable_by_d[18]:
    vals,uniq=orbit_contributions(rep,18)
    viable=[]
    for q0,r in pairs_gate:
        target=sub(r,q0)
        if reachable_multiset(target,uniq,29):
            viable.append((q0,r))
    D18.append((idx,cs,rep,vals,uniq,pairs_gate,viable))

# Exactly one conjugacy class survives full orbit-sum feasibility.
counts=sorted(len(x[-1]) for x in D18)
assert counts==[0,0,4], counts
survivor=[x for x in D18 if len(x[-1])==4][0]
_,surv_class_size,surv_rep,surv_vals,surv_uniq,surv_gate,surv_pairs=survivor
assert order(surv_rep)==2

# Canonical survivor must be equivalent to: fix e0; swap e1,e3; flip e2.
CANON=((0,3,2,1),(1,1,-1,1))
# Confirm CANON is conjugate to the surviving representative.
surv_cls=set(classes[[x[0] for x in D18 if len(x[-1])==4][0]])
assert CANON in surv_cls
canon_vals,canon_uniq=orbit_contributions(CANON,18)
assert set(canon_uniq)=={
    (-18,0,0,0),(18,0,0,0),
    (0,-9,0,-9),(0,9,0,9),
    (0,0,0,0)
}
canon_gate=row_gate(CANON,18)
canon_viable=[(q0,r) for q0,r in canon_gate if reachable_multiset(sub(r,q0),canon_uniq,29)]
assert len(canon_viable)==4
expected=set()
for s0 in (-1,1):
    # q0=s0 e0; r0 has same sign and magnitude 19; e1/e3 share sign
    for s13 in (-1,1):
        expected.add((basis(0,s0),(19*s0,9*s13,0,9*s13)))
assert set(canon_viable)==expected, canon_viable

print('SIGNED_PERMUTATION_GROUP_SIZE',len(ALL))
print('SIGNED_PERMUTATION_CONJUGACY_CLASSES',len(classes))
print('SIGNED_PERMUTATION_ELEMENT_ORDERS',orders)
print('NORM523_INTEGER_ROW_VECTORS',len(RVECS))
print('DIVISORS_522',DIVS)
print('ROW_GATE_SUMMARY')
for d in DIVS:
    simple=[{'class':idx,'image_order':m,'class_size':cs,'L':L,'q0_r_pairs':np}
            for idx,m,cs,L,np,rep,pairs_gate in viable_by_d[d]]
    print(' d=',d,' viable=',simple)
print('DIVISIBLE_BY_29_SURVIVORS',sum(len(viable_by_d[d]) for d in (29,58,87,174,261,522)))
print('D18_FULL_ORBIT_SUM_FEASIBILITY')
for idx,cs,rep,vals,uniq,pairs_gate,viable in D18:
    print(' class=',idx,'class_size=',cs,'rep=',rep,'unique_contributions=',uniq,
          'row_gate_pairs=',len(pairs_gate),'orbit_sum_viable_pairs=',len(viable))
print('D18_CANONICAL_SURVIVOR_REP',CANON)
print('D18_CANONICAL_UNIQUE_CONTRIBUTIONS',canon_uniq)
print('D18_CANONICAL_VIABLE_PAIRS',canon_viable)
print('D18_CANONICAL_NORMAL_FORM','q0=e0, r=(19,9,0,9), up to global sign and centralizer sign on the swapped pair')
print('ALL_EXACT_SIGNED_EQUIVARIANCE_SIEVE_CHECKS_PASSED')
