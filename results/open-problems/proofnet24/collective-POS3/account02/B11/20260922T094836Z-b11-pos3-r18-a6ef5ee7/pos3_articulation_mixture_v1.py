#!/usr/bin/env python3
"""Exact regression for POS3 articulation insertion kernels.

No external packages.  All probabilities are for uniform full linear extensions.
Finite enumeration is a regression check only, never a closure argument.
"""
from functools import lru_cache
from fractions import Fraction
from itertools import combinations
from math import comb

def closure(n, mask):
    pairs=[(i,j) for i in range(n) for j in range(i+1,n)]
    r=[[False]*n for _ in range(n)]
    for k,(i,j) in enumerate(pairs):
        if (mask>>k)&1: r[i][j]=True
    for k in range(n):
        for i in range(n):
            if r[i][k]:
                for j in range(n):
                    if r[k][j]: r[i][j]=True
    out=0
    for k,(i,j) in enumerate(pairs):
        if r[i][j]: out |= 1<<k
    return out

def rel(n, mask):
    pairs=[(i,j) for i in range(n) for j in range(i+1,n)]
    r=[[False]*n for _ in range(n)]
    for k,(i,j) in enumerate(pairs):
        if (mask>>k)&1: r[i][j]=True
    return r

def extensions(vertices, r):
    V=tuple(sorted(vertices))
    idx={v:i for i,v in enumerate(V)}
    m=len(V)
    preds=[0]*m
    for a in V:
        for b in V:
            if r[a][b]:
                preds[idx[b]] |= 1<<idx[a]
    @lru_cache(None)
    def rec(mask):
        if mask==(1<<m)-1: return ((),)
        out=[]
        for i,v in enumerate(V):
            if not (mask>>i)&1 and not (preds[i] & ~mask):
                for t in rec(mask | (1<<i)):
                    out.append((v,)+t)
        return tuple(out)
    return rec(0)

def width(vertices, r):
    V=list(vertices); best=0
    for mask in range(1<<len(V)):
        k=mask.bit_count()
        if k<=best: continue
        S=[V[i] for i in range(len(V)) if (mask>>i)&1]
        if all(not(r[a][b] or r[b][a]) for a,b in combinations(S,2)):
            best=k
    return best

def graph_connected(vertices, r, incompar=True):
    V=list(vertices)
    if len(V)<=1: return True
    seen={V[0]}; stack=[V[0]]
    while stack:
        a=stack.pop()
        for b in V:
            if b in seen or b==a: continue
            c=r[a][b] or r[b][a]
            edge=(not c) if incompar else c
            if edge: seen.add(b); stack.append(b)
    return len(seen)==len(V)

def inc_components(vertices, r):
    unseen=set(vertices); out=[]
    while unseen:
        s=min(unseen); unseen.remove(s); C={s}; stack=[s]
        while stack:
            a=stack.pop()
            for b in list(unseen):
                if not (r[a][b] or r[b][a]):
                    unseen.remove(b); C.add(b); stack.append(b)
        out.append(C)
    return out

def ordered_components(comps,r):
    # insertion sort; distinct incomparability components are uniformly comparable
    out=[]
    for C in comps:
        placed=False
        c=min(C)
        for i,D in enumerate(out):
            d=min(D)
            if r[c][d]:
                out.insert(i,C); placed=True; break
        if not placed: out.append(C)
    for i in range(len(out)):
        for j in range(i+1,len(out)):
            assert all(r[a][b] for a in out[i] for b in out[j])
    return out

def prob(exts,a,b,weights=None):
    if weights is None: weights=[1]*len(exts)
    den=sum(weights); num=0
    for e,w in zip(exts,weights):
        pos={x:i for i,x in enumerate(e)}
        if pos[a]<pos[b]: num+=w
    return Fraction(num,den)

def one_leaf_parameters(A,B,v,z,r):
    ea=extensions(A,r); eb=extensions(B,r)
    predv={x for x in A if r[x][v]}
    succv={x for x in B if r[v][x]}
    wa=[]
    for e in ea:
        pos={x:i for i,x in enumerate(e)}
        last=max((pos[x] for x in predv), default=-1)
        wa.append(len(A)-1-last+1)  # a+1
    wb=[]
    for e in eb:
        pos={x:i for i,x in enumerate(e)}
        first=min((pos[x] for x in succv), default=len(B))
        wb.append(first+1)           # b+1
    NA=len(eb)*sum(wa)              # N(v<z)
    NB=len(ea)*sum(wb)              # N(z<v)
    return ea,eb,wa,wb,NA,NB

# Exhaustive naturally-labelled regression through n=6.
natural=0; width3=0; cut_states=0; one_leaf=0; formulas=0; unbalanced=0
for n in range(2,7):
    closed={closure(n,m) for m in range(1<<(n*(n-1)//2))}
    natural += len(closed)
    for m in closed:
        r=rel(n,m); V=list(range(n))
        if width(V,r)>3: continue
        width3 += 1
        if not graph_connected(V,r,True): continue
        full=extensions(V,r); E=len(full)
        for v in V:
            comps=inc_components([x for x in V if x!=v],r)
            if len(comps)<=1: continue
            cut_states += 1
            comps=ordered_components(comps,r)
            if len(comps)!=3 or len(comps[1])!=1: continue
            A=set(comps[0]); z=next(iter(comps[1])); B=set(comps[2])
            assert not (r[v][z] or r[z][v])
            one_leaf += 1
            ea,eb,wa,wb,Nvz,Nzv=one_leaf_parameters(A,B,v,z,r)
            actual=sum(1 for e in full if e.index(v)<e.index(z))
            assert Nvz==actual and Nvz+Nzv==E
            # Conditional uniformity: on v<z every B-extension has the same count,
            # and on z<v every A-extension has the same count.
            Bcounts={bext:0 for bext in eb}; Acounts={aext:0 for aext in ea}
            for e in full:
                if e.index(v)<e.index(z):
                    bext=tuple(x for x in e if x in B); Bcounts[bext]+=1
                else:
                    aext=tuple(x for x in e if x in A); Acounts[aext]+=1
            assert len(set(Bcounts.values()))==1
            assert len(set(Acounts.values()))==1
            formulas += 1
            lam=Fraction(Nvz,E)
            if lam<Fraction(1,3) or lam>Fraction(2,3): unbalanced += 1

def build_one_leaf(A_r,B_r,D,U):
    na=len(A_r); nb=len(B_r); z=na; off=na+1; v=na+nb+1; n=v+1
    r=[[False]*n for _ in range(n)]
    for i in range(na):
        for j in range(na):
            if A_r[i][j]: r[i][j]=True
    for i in range(nb):
        for j in range(nb):
            if B_r[i][j]: r[off+i][off+j]=True
    for a in range(na):
        r[a][z]=True
        for b in range(nb): r[a][off+b]=True
    for b in range(nb): r[z][off+b]=True
    for a in D: r[a][v]=True
    for b in U: r[v][off+b]=True
    for k in range(n):
        for i in range(n):
            if r[i][k]:
                for j in range(n):
                    if r[k][j]: r[i][j]=True
    return r,z,v,set(range(na)),set(range(off,off+nb))

# Structured fixture 1: one dominant-block balanced pair can be destroyed.
# A is a 2-antichain.  B has only 0<1, with 2 incomparable to both.
# Pred(v)∩A=empty; Succ(v)∩B={0,1}.
A_r=[[False]*2 for _ in range(2)]
B_r=[[False]*3 for _ in range(3)]; B_r[0][1]=True
ea=extensions(range(2),A_r); eb=extensions(range(3),B_r)
wa=[3,3]  # a+1
wb=[]
for e in eb:
    pos={x:i for i,x in enumerate(e)}
    wb.append(min(pos[0],pos[1])+1)
Aplus=Fraction(sum(wa),len(wa)); Bplus=Fraction(sum(wb),len(wb))
lam=Aplus/(Aplus+Bplus)
assert lam==Fraction(9,13)
q02=prob(eb,0,2); t02=prob(eb,0,2,wb); p02=lam*q02+(1-lam)*t02
q12=prob(eb,1,2); t12=prob(eb,1,2,wb); p12=lam*q12+(1-lam)*t12
assert (q02,t02,p02)==(Fraction(2,3),Fraction(1,2),Fraction(8,13))
assert (q12,t12,p12)==(Fraction(1,3),Fraction(1,4),Fraction(4,13))
rfix,zfix,vfix,Afix,Bfix=build_one_leaf(A_r,B_r,set(),{0,1})
F=extensions(range(len(rfix)),rfix)
assert len(F)==26 and width(range(len(rfix)),rfix)==3
assert graph_connected(range(len(rfix)),rfix,True) and graph_connected(range(len(rfix)),rfix,False)
assert prob(F,vfix,zfix)==Fraction(9,13)
# B local labels 0,1,2 correspond to full labels 3,4,5.
assert prob(F,4,5)==Fraction(4,13) and prob(F,3,5)==Fraction(8,13)

# Structured fixture 2: the articulation pair itself need not be balanced.
# A is 0<1<2<3 plus isolated 4, Pred(v)∩A={0}; B is a singleton.
Ar=[[False]*5 for _ in range(5)]
for i in range(4):
    for j in range(i+1,4): Ar[i][j]=True
Ae=extensions(range(5),Ar)
wa=[]
for e in Ae:
    pos={x:i for i,x in enumerate(e)}
    wa.append(5-pos[0])
assert len(Ae)==5 and sum(wa)==24
Aplus2=Fraction(24,5); Bplus2=Fraction(2,1)
lam2=Aplus2/(Aplus2+Bplus2)
assert lam2==Fraction(12,17)
B1=[[False]]
rfix2,zfix2,vfix2,Afix2,Bfix2=build_one_leaf(Ar,B1,{0},set())
F2=extensions(range(len(rfix2)),rfix2)
assert len(F2)==34 and width(range(len(rfix2)),rfix2)==3
assert graph_connected(range(len(rfix2)),rfix2,True) and graph_connected(range(len(rfix2)),rfix2,False)
assert prob(F2,vfix2,zfix2)==Fraction(12,17)

# Named partner account03/B19 r12 family P_m, applied to the k=2 kernel.
# For v=d, P_m-d={e} ordinal-sum B_m and the exact uniform-B branch
# has mass 2 e(B_m), where e(B_m)=(m+1)(m+3).
for m in range(0,9):
    p=comb(m+3,3); q=comb(m+2,2); rr=m+1
    E=3*p+4*q+rr
    eB=(m+1)*(m+3)
    uniform_B_mass=2*eB
    assert E==(m+1)*(m*m+9*m+16)//2
    assert Fraction(uniform_B_mass,E)==Fraction(4*(m+3),m*m+9*m+16)

print("POS3_ARTICULATION_MIXTURE_V1_PASS")
print(f"natural_transitive_closures_n2_to_n6={natural}")
print(f"width_le3={width3}")
print(f"inc_connected_cut_states={cut_states}")
print(f"one_leaf_articulation_states={one_leaf}")
print(f"one_leaf_exact_factorizations_checked={formulas}")
print(f"one_leaf_unbalanced_vz_nle6={unbalanced}")
print("destroyed_pair_fixture=E=26 lambda=9/13 q(1<2)=1/3 tilted=1/4 global=4/13; q(0<2)=2/3 global=8/13 survives")
print("unbalanced_articulation_fixture=E=34 lambda=12/17 with A=(4-chain + isolated), B=singleton")
m=8
E=(m+1)*(m*m+9*m+16)//2
mass=2*(m+1)*(m+3)
print(f"partner_P8_k2_uniform_B_branch={mass}/{E}={Fraction(mass,E)}")
print("partner_Pm_k2_uniform_B_weight=4(m+3)/(m^2+9m+16)->0")
