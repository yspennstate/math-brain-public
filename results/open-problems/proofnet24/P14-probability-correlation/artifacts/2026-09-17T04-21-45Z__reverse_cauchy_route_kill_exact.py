#!/usr/bin/env python3
"""P14 exact checks: strict reverse-Cauchy route kill, minimal physical order,
and an independent finite audit slice for P15-I0066-UNITARY-QUADRATIC-DATA-NOGO-06C.

All arithmetic in the P14 forest calculations is exact Fraction arithmetic.
Graph enumeration is exhaustive over every labelled simple side graph on 3
and 4 vertices, every 3-terminal set, and every pair of present old edges
whose unit-star apex extension is 3-connected.
"""
from fractions import Fraction as Q
from itertools import combinations

def roots_if_forest(n, edges, mask):
    parent=list(range(n))
    def find(x):
        while parent[x]!=x:
            parent[x]=parent[parent[x]]
            x=parent[x]
        return x
    for i,(u,v) in enumerate(edges):
        if (mask>>i)&1:
            a,b=find(u),find(v)
            if a==b:
                return None
            parent[a]=b
    return [find(i) for i in range(n)]

def terminal_state(roots, t):
    x,y,z=t
    xy=roots[x]==roots[y]
    xz=roots[x]==roots[z]
    yz=roots[y]==roots[z]
    if xy and xz: return "T"
    if xy: return "P"
    if xz: return "Q"
    if yz: return "S"
    return "D"

def transfer_stats(n, edges, terminals, eidx, fidx):
    # A = F(1/4,1/4,1/4); K = D = F_uv.
    coeff={"D":Q(31,16),"P":Q(3,2),"Q":Q(3,2),"S":Q(3,2),"T":Q(1)}
    A=[Q(0) for _ in range(4)]
    K=[Q(0) for _ in range(4)]
    for mask in range(1<<len(edges)):
        roots=roots_if_forest(n,edges,mask)
        if roots is None:
            continue
        st=terminal_state(roots,terminals)
        ie=(mask>>eidx)&1
        jf=(mask>>fidx)&1
        flags=(1,ie,jf,ie*jf)
        for k,on in enumerate(flags):
            if on:
                A[k]+=coeff[st]
                if st=="D":
                    K[k]+=1
    return A,K

def gap_data(A,K):
    A0,Ae,Af,Aef=A
    K0,Ke,Kf,Kef=K
    dA=Ae*Af-A0*Aef
    dK=Ke*Kf-K0*Kef
    C=Ae*Kf+Ke*Af-A0*Kef-K0*Aef
    rc_slack=C*C-4*dA*dK
    return dA,dK,C,rc_slack

def connected_after_removal(n, edges, removed):
    live=[v for v in range(n) if v not in removed]
    if len(live)<=1:
        return True
    adj={v:[] for v in live}
    for u,v in edges:
        if u in adj and v in adj:
            adj[u].append(v)
            adj[v].append(u)
    seen={live[0]}
    stack=[live[0]]
    while stack:
        u=stack.pop()
        for v in adj[u]:
            if v not in seen:
                seen.add(v)
                stack.append(v)
    return len(seen)==len(live)

def vertex_connectivity_at_least_3(n, edges):
    if not connected_after_removal(n,edges,set()):
        return False
    for k in (1,2):
        for rem in combinations(range(n),k):
            if not connected_after_removal(n,edges,set(rem)):
                return False
    return True

def physical_counts(n, H_edges, terminals, eidx, fidx):
    G_edges=list(H_edges)+[(n,t) for t in terminals]
    Z=Ze=Zf=Zef=0
    for mask in range(1<<len(G_edges)):
        roots=roots_if_forest(n+1,G_edges,mask)
        if roots is None:
            continue
        ie=(mask>>eidx)&1
        jf=(mask>>fidx)&1
        Z+=1; Ze+=ie; Zf+=jf; Zef+=ie*jf
    return (Z,Ze,Zf,Zef,Ze*Zf-Z*Zef),G_edges

# ----------------------------------------------------------------------
# 1. Strict reverse-Cauchy route counterexample with a 3-connected
#    physical star extension.
# ----------------------------------------------------------------------
H=[(0,1),(0,2),(0,3),(0,4),(1,2),(1,3),(2,3),(3,4)]
terminals=(2,4,1)
eidx,fidx=0,6
A,K=transfer_stats(5,H,terminals,eidx,fidx)
assert A == [Q(2865,16),Q(971,16),Q(971,16),Q(319,16)]
assert K == [Q(23),Q(5),Q(5),Q(1)]
dA,dK,C,rc_slack=gap_data(A,K)
assert dA == Q(14453,128) > 0
assert dK == Q(2) > 0
assert C == Q(-123,4) < 0
assert rc_slack == Q(169,4) > 0
# Therefore C^2 > 4 dA dK: the proposed reverse-Cauchy inequality is false.

full,G=physical_counts(5,H,terminals,eidx,fidx)
assert vertex_connectivity_at_least_3(6,G)
assert full == (722,244,244,80,1776)
# Check the exact star-mesh gap decomposition.
assert Q(full[4]) == 16*dA + C + Q(1,16)*dK

# ----------------------------------------------------------------------
# 2. Minimality inside the strict 3-connected route-kill class:
#    no physical graph on 4 or 5 vertices (side n=3 or 4) has
#    dA>0, dK>0, C<0, and C^2>4 dA dK.
# ----------------------------------------------------------------------
small_counts={}
for n in (3,4):
    all_edges=list(combinations(range(n),2))
    tested=0
    strict_negative_cross=0
    bad=0
    for gmask in range(1<<len(all_edges)):
        edges=[e for i,e in enumerate(all_edges) if (gmask>>i)&1]
        if len(edges)<2:
            continue
        for terms in combinations(range(n),3):
            Gx=edges+[(n,t) for t in terms]
            if not vertex_connectivity_at_least_3(n+1,Gx):
                continue
            for ei,fi in combinations(range(len(edges)),2):
                tested += 1
                Ax,Kx=transfer_stats(n,edges,terms,ei,fi)
                da,dk,c,s=gap_data(Ax,Kx)
                if da>0 and dk>0 and c<0:
                    strict_negative_cross += 1
                    if s>0:
                        bad += 1
    assert bad==0
    small_counts[n]=(tested,strict_negative_cross,bad)
assert small_counts[3] == (3,0,0)
assert small_counts[4] == (180,0,0)

# ----------------------------------------------------------------------
# 3. Independent finite audit slice for P15 claim 06C.
#    Re-derive, without matrix multiplication code, the exact stationary
#    block recursion and amplification for m=1..8.
# ----------------------------------------------------------------------
p15=[]
for m in range(1,9):
    lam=[Q(4**i) for i in range(m+1)]
    # Candidate H-level quadratic margin is 1 because C is a permutation:
    # 2*A - A^(1/2) C^*C A^(1/2) = A.
    # Relative conjugation A^(1/2) C A^(-1/2) has squared weights
    # 4 on upward edges and 4^(-m) on the wrap edge, hence norm^2=4.
    ratios=[lam[i+1]/lam[i] for i in range(m)] + [lam[0]/lam[m]]
    assert max(ratios)==4
    v0=Q(1,1)/(Q(2)-Q(1,2**m))
    v=[v0]
    for i in range(1,m+1):
        v.append(v[-1]/8)
    assert -2*lam[0]*v[0] + lam[m]*v[m] + 1 == 0
    for i in range(1,m+1):
        assert -2*lam[i]*v[i] + lam[i-1]*v[i-1] == 0
    amp=(lam[m]**2*v[m])/v0
    assert amp==2**m
    p15.append(int(amp))
assert p15 == [2,4,8,16,32,64,128,256]

print("P14-REVERSE-CAUCHY-ROUTE-KILL-62: PASS")
print("witness_side_edges=", H)
print("witness_terminals=", terminals)
print("witness_target_edges=", H[eidx], H[fidx])
print("A_stats=", [str(x) for x in A])
print("K_stats=", [str(x) for x in K])
print("delta_A=", dA, "delta_K=", dK, "cross=", C)
print("reverse_cauchy_excess=", rc_slack)
print("physical_graph_3connected=YES")
print("physical_counts=", full)
print("small_strict_route_census=", small_counts)
print("P15-independent-amplification-sequence=", p15)
print("ALL_EXACT_CHECKS_PASSED")
