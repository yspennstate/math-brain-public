#!/usr/bin/env python3
"""
P0219 admission-screen self-check: exact finite routing-tax witness.

This script uses only integer/bit-mask arithmetic. It verifies:
  (1) the n=4 four-closed-edge witness has poset width W=2;
  (2) a concrete vertex-set dual certificate forces U>=3;
  (3) three explicit edge-disjoint boundary-to-boundary paths cover all
      four closed edges, so U=3;
  (4) the arbitrary-set dual value K=3 while the downset-restricted
      value is 2;
  (5) as a sanity check on the general dual theorem proved in the report,
      for every closed-edge set on n=2 and n=3, the dual value agrees with
      a completely independent brute-force enumeration of pairwise
      edge-disjoint path families.
No floating point is used.
"""

from itertools import combinations

def vertices(n):
    return [(x,y) for x in range(n) for y in range(n)]

def edges(n):
    E=[]
    index={}
    for x in range(n):
        for y in range(n):
            if x+1<n:
                index[((x,y),(x+1,y))]=len(E)
                E.append(((x,y),(x+1,y)))
            if y+1<n:
                index[((x,y),(x,y+1))]=len(E)
                E.append(((x,y),(x,y+1)))
    return E,index

def sources(n):
    return [(0,j) for j in range(n-1)] + [(i,0) for i in range(1,n-1)]

def sinks(n):
    return [(i,n-1) for i in range(n)] + [(n-1,j) for j in range(n-2,-1,-1)]

def dual_value(n, Cmask):
    E,_=edges(n)
    V=vertices(n)
    best=-10**9
    bestA=None
    for amask in range(1<<len(V)):
        A={V[i] for i in range(len(V)) if (amask>>i)&1}
        closed_out=0
        incoming=0
        for ei,(u,v) in enumerate(E):
            if u in A and v not in A and ((Cmask>>ei)&1):
                closed_out += 1
            if u not in A and v in A:
                incoming += 1
        val=closed_out-incoming
        if val>best:
            best=val
            bestA=A
    return best,bestA

def is_downset(A,n):
    for x,y in A:
        for xx in range(x+1):
            for yy in range(y+1):
                if (xx,yy) not in A:
                    return False
    return True

def downset_value(n,Cmask):
    E,_=edges(n)
    V=vertices(n)
    best=0
    bestA=set()
    for amask in range(1<<len(V)):
        A={V[i] for i in range(len(V)) if (amask>>i)&1}
        if not is_downset(A,n):
            continue
        closed_out=sum(
            1 for ei,(u,v) in enumerate(E)
            if u in A and v not in A and ((Cmask>>ei)&1)
        )
        if closed_out>best:
            best=closed_out
            bestA=A
    return best,bestA

def comparable(e,f):
    """Can directed edge e be traversed before directed edge f?"""
    _,ve=e
    uf,_=f
    return ve[0] <= uf[0] and ve[1] <= uf[1]

def width_bruteforce(n,Cidx):
    E,_=edges(n)
    C=list(Cidx)
    best=0
    bestset=None
    for r in range(len(C)+1):
        for S in combinations(C,r):
            ok=True
            for a,b in combinations(S,2):
                if comparable(E[a],E[b]) or comparable(E[b],E[a]):
                    ok=False
                    break
            if ok and r>best:
                best=r
                bestset=S
    return best,bestset

def enumerate_paths(n):
    E,idx=edges(n)
    sinkset=set(sinks(n))
    ans=set()
    def dfs(v,mask):
        # A path may end as soon as it reaches an allowed sink, or continue
        # along the top/right boundary and end later.
        if v in sinkset and mask:
            ans.add(mask)
        x,y=v
        if x+1<n:
            dfs((x+1,y), mask | (1<<idx[(v,(x+1,y))]))
        if y+1<n:
            dfs((x,y+1), mask | (1<<idx[(v,(x,y+1))]))
    for s in sources(n):
        dfs(s,0)
    return sorted(ans)

def disjoint_path_unions(n):
    """Map every union of a pairwise-edge-disjoint path family to min size."""
    P=enumerate_paths(n)
    best={0:0}
    def dfs(start,used,k):
        old=best.get(used)
        if old is None or k<old:
            best[used]=k
        for j in range(start,len(P)):
            p=P[j]
            if not (used&p):
                dfs(j+1,used|p,k+1)
    dfs(0,0,0)
    return best

def brute_U_from_path_families(n):
    E,_=edges(n)
    allmask=(1<<len(E))-1
    unions=disjoint_path_unions(n)
    U={}
    for Cmask in range(allmask+1):
        val=None
        for umask,k in unions.items():
            if Cmask & ~umask == 0:
                if val is None or k<val:
                    val=k
        assert val is not None
        U[Cmask]=val
    return U

def check_explicit_path(n,path_vertices):
    E,idx=edges(n)
    assert path_vertices[0] in set(sources(n))
    assert path_vertices[-1] in set(sinks(n))
    mask=0
    for u,v in zip(path_vertices,path_vertices[1:]):
        assert (u,v) in idx
        mask |= 1<<idx[(u,v)]
    return mask

# Exact n=4 witness.
n=4
E,_=edges(n)
Cidx={0,2,11,12}
Cmask=sum(1<<i for i in Cidx)
assert [E[i] for i in sorted(Cidx)] == [
    ((0,0),(1,0)),
    ((0,1),(1,1)),
    ((1,2),(2,2)),
    ((1,2),(1,3)),
]

W,anti=width_bruteforce(n,Cidx)
assert W==2

# Explicit two-chain cover witnesses W<=2.
chain1=[0,11]
chain2=[2,12]
for chain in [chain1,chain2]:
    assert comparable(E[chain[0]],E[chain[1]])
assert set(chain1+chain2)==Cidx

# Explicit antichain witnesses W>=2.
assert not comparable(E[0],E[2])
assert not comparable(E[2],E[0])

# Arbitrary-set dual certificate A: four closed exits, one incoming grid edge.
A={(0,0),(0,1),(0,2),(1,2)}
closed_out=[
    i for i,(u,v) in enumerate(E)
    if u in A and v not in A and i in Cidx
]
incoming=[
    i for i,(u,v) in enumerate(E)
    if u not in A and v in A
]
assert set(closed_out)==Cidx
assert incoming==[10]
assert len(closed_out)-len(incoming)==3

# Three explicit pairwise edge-disjoint source-to-sink paths cover C.
Pverts=[
    [(0,0),(1,0),(1,1),(1,2),(2,2),(2,3)],
    [(0,1),(1,1),(2,1),(2,2),(3,2)],
    [(0,2),(1,2),(1,3)],
]
Pmasks=[check_explicit_path(n,p) for p in Pverts]
for a,b in combinations(Pmasks,2):
    assert (a&b)==0
assert Cmask & ~(Pmasks[0]|Pmasks[1]|Pmasks[2]) == 0

# So U>=3 by the cut certificate and U<=3 by the explicit paths.
U=3

K,K_A=dual_value(n,Cmask)
D,D_A=downset_value(n,Cmask)
assert K==3
assert D==2
assert U==K and W==D and U-W==1

print("WITNESS_N=4")
print("CLOSED_EDGE_INDICES", sorted(Cidx))
print("CLOSED_EDGES", [E[i] for i in sorted(Cidx)])
print("WIDTH_W", W)
print("DUAL_CERTIFICATE_A", sorted(A))
print("DUAL_CLOSED_OUT", sorted(closed_out))
print("DUAL_INCOMING", incoming)
print("DUAL_LOWER_BOUND", len(closed_out)-len(incoming))
print("EXPLICIT_COVER_PATHS", Pverts)
print("U", U)
print("ROUTING_TAX_U_MINUS_W", U-W)
print("ARBITRARY_SET_DUAL_K", K)
print("DOWNSET_DUAL", D)

# Independent small-grid sanity check of the report's general dual theorem:
# compare the cut formula to literal exhaustive path-family enumeration.
for nn in (2,3):
    Umap=brute_U_from_path_families(nn)
    total=1<<len(edges(nn)[0])
    for C in range(total):
        Kc,_=dual_value(nn,C)
        assert Umap[C]==Kc, (nn,C,Umap[C],Kc)
    print("EXHAUSTIVE_DUAL_CHECK_N", nn, "CLOSED_SETS", total, "PASS")

# Exhaustive minimality inside the n=4 grid: no closed set of size <=3
# has routing tax. This uses only the proved dual/downset formulas and
# enumerates all 2325 such closed-edge sets.
V4=vertices(4)
E4,_=edges(4)
vix={v:i for i,v in enumerate(V4)}
out_masks=[]
incoming_counts=[]
downset_indices=[]
for amask in range(1<<len(V4)):
    A={V4[i] for i in range(len(V4)) if (amask>>i)&1}
    omask=0
    inc=0
    for ei,(u,v) in enumerate(E4):
        if u in A and v not in A:
            omask |= 1<<ei
        if u not in A and v in A:
            inc += 1
    out_masks.append(omask)
    incoming_counts.append(inc)
    if is_downset(A,4):
        downset_indices.append(amask)

def dual_fast_4(Cmask):
    return max((Cmask & out_masks[a]).bit_count()-incoming_counts[a]
               for a in range(1<<len(V4)))

def down_fast_4(Cmask):
    return max((Cmask & out_masks[a]).bit_count()
               for a in downset_indices)

tested=0
for r in range(4):
    for comb in combinations(range(len(E4)),r):
        tested += 1
        cmask=sum(1<<i for i in comb)
        assert dual_fast_4(cmask)==down_fast_4(cmask), comb
assert tested==2325
print("EXHAUSTIVE_N4_ROUTING_TAX_ZERO_FOR_CLOSED_SETS_SIZE_LE_3", tested, "PASS")

print("ALL_EXACT_P0219_ROUTING_TAX_CHECKS_PASS")
