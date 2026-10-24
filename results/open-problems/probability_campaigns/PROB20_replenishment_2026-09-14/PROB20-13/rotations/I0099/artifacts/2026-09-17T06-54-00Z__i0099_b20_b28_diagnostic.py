#!/usr/bin/env python3
from itertools import combinations, permutations
from collections import Counter, defaultdict

P=97

def leg(a,p=P):
    a%=p
    if a==0: return 0
    z=pow(a,(p-1)//2,p)
    return 1 if z==1 else -1

QR={x*x%P for x in range(1,P)}

def is_edge(a,b):
    return a!=b and ((a-b)%P in QR)

def is_clique(C):
    return all(is_edge(a,b) for a,b in combinations(C,2))

def common_neighbors(C):
    C=set(C)
    return [x for x in range(P) if x not in C and all(is_edge(x,c) for c in C)]

def R_pairs(C):
    out=[]
    for s in range(P):
        for n in range(P):
            if leg(s*s-4*n)!=-1:
                continue
            if all(leg(c*c-s*c+n)==1 for c in C):
                out.append((s,n))
    return out

def tau0_pair(s,n,c):
    ni=pow(n,P-2,P)
    return (c*s*ni%P, c*c*ni%P)

def pair_signs(pair,C):
    s,n=pair
    return [leg(c*c-s*c+n) for c in C]

def mobius_from_triples(src,dst):
    rows=[]
    for x,y in zip(src,dst):
        rows.append([x%P,1,(-y*x)%P,(-y)%P])
    M=[r[:] for r in rows]
    piv=[]; rr=0
    for col in range(4):
        pivot=next((i for i in range(rr,3) if M[i][col]%P),None)
        if pivot is None: continue
        M[rr],M[pivot]=M[pivot],M[rr]
        iv=pow(M[rr][col],P-2,P)
        M[rr]=[(v*iv)%P for v in M[rr]]
        for i in range(3):
            if i!=rr and M[i][col]%P:
                fac=M[i][col]%P
                M[i]=[(M[i][j]-fac*M[rr][j])%P for j in range(4)]
        piv.append(col); rr+=1
        if rr==3: break
    free=[c for c in range(4) if c not in piv]
    if len(free)!=1: return None
    fc=free[0]
    v=[0]*4; v[fc]=1
    for i,col in enumerate(piv):
        v[col]=(-M[i][fc])%P
    A,B,C,D=v
    if (A*D-B*C)%P==0: return None
    first=next(x for x in v if x)
    iv=pow(first,P-2,P)
    return tuple(x*iv%P for x in v)

def mob_eval(g,x):
    A,B,C,D=g
    den=(C*x+D)%P
    if den==0: return None
    return (A*x+B)*pow(den,P-2,P)%P

def pgl_stabilizers(C):
    C=tuple(sorted(C)); src=C[:3]
    gs=set()
    for dst in permutations(C,3):
        g=mobius_from_triples(src,dst)
        if g is None: continue
        if g in gs: continue
        vals=[mob_eval(g,x) for x in C]
        if None not in vals and set(vals)==set(C):
            gs.add(g)
    return gs

C5=(0,1,3,4,12)
assert is_clique(C5)
N5=common_neighbors(C5)
assert N5==[36,65]
R5=R_pairs(C5)
assert len(R5)==132 and len(R5)%4==0

pair=(1,93)
assert pair in R5
pair2=tau0_pair(*pair,3)
assert pair2==(72,22)
assert leg(pair2[0]*pair2[0]-4*pair2[1])==-1
signs=pair_signs(pair2,C5)
assert signs==[1,1,1,-1,-1]

stabs=pgl_stabilizers(C5)
assert stabs=={(1,0,0,1)}

H=[x for x in range(P) if x not in (0,1) and is_edge(x,0) and is_edge(x,1)]
assert len(H)==23

# Precompute all irreducible quadratics good at 0 and 1 for exact all-triple census.
base=[]
for s in range(P):
    for n in range(P):
        if leg(s*s-4*n)==-1 and leg(n)==1 and leg(1-s+n)==1:
            base.append((s,n))
good={c:set() for c in H}
for idx,(s,n) in enumerate(base):
    for c in H:
        if leg(c*c-s*c+n)==1:
            good[c].add(idx)

stats_t=defaultdict(Counter)
stats_r=defaultdict(Counter)
stats_joint=defaultdict(Counter)
for abc in combinations(H,3):
    e=sum(is_edge(a,b) for a,b in combinations(abc,2))
    C=(0,1)+abc
    t=len(common_neighbors(C))
    inds=good[abc[0]] & good[abc[1]] & good[abc[2]]
    r=len(inds)
    stats_t[e][t%2]+=1
    stats_r[e][r%4]+=1
    stats_joint[e][(r%4,t%2)]+=1

expected_t={
    3:Counter({0:180}),
    2:Counter({0:360,1:252}),
    1:Counter({1:432,0:324}),
    0:Counter({0:135,1:88}),
}
expected_r={
    3:Counter({0:180}),
    2:Counter({2:360,0:252}),
    1:Counter({2:432,0:324}),
    0:Counter({0:135,2:88}),
}
assert dict(stats_t)==expected_t
assert dict(stats_r)==expected_r

Codd=(0,1,2,3,12)
nonedges_odd=[(a,b) for a,b in combinations(Codd,2) if not is_edge(a,b)]
assert nonedges_odd==[(2,12)]
assert common_neighbors(Codd)==[4]

Cr=(0,1,2,3,9)
nonedges_r=[(a,b) for a,b in combinations(Cr,2) if not is_edge(a,b)]
assert nonedges_r==[(2,9)]
Rr=R_pairs(Cr)
assert len(Rr)==114 and len(Rr)%4==2

print("I0099_B20_B28_EXACT_DIAGNOSTIC")
print(f"p={P}")
print(f"C5={C5} clique=PASS common_neighbors={N5} t5={len(N5)} R={len(R5)} Rmod4={len(R5)%4}")
print(f"triple_V4_tau0_coefficient_counterexample: pair={pair} -> {pair2} signs_on_C5={signs}")
print(f"C5_PGL2_set_stabilizer={sorted(stabs)} size={len(stabs)}")
for e in (3,2,1,0):
    print(f"internal_edges_among_extra3={e} t_parity_counts={dict(stats_t[e])} Rmod4_counts={dict(stats_r[e])} joint={dict(stats_joint[e])}")
print(f"one_missing_edge_odd_t: C={Codd} missing={nonedges_odd} common_neighbors={common_neighbors(Codd)}")
print(f"one_missing_edge_R_not_div4: C={Cr} missing={nonedges_r} R={len(Rr)} Rmod4={len(Rr)%4}")
print("ALL_I0099_B20_B28_EXACT_DIAGNOSTICS_PASS")
