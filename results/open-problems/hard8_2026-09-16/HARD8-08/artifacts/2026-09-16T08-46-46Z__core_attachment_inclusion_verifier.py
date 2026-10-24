#!/usr/bin/env python3
"""Exact finite verifier for HARD8-08 checkpoint 4.

Pure Python, no third-party dependencies.

Checks on every connected labelled graph with 2..6 vertices:
  * exact chromatic number by exhaustive backtracking;
  * edge-critical k-chromatic cores for k=3,4;
  * the corrected two-terminal attachment criterion against direct extension logic;
  * the inclusion theorem: if terminals u,v are forced equal and u has at
    most k-1 neighbours in the core, then N_C(u) subset N_C(v), and symmetrically;
  * consequently, if both core-neighbourhoods have size k-1, they are equal;
  * the edge-deletion saturation condition for every exclusive core neighbour.

Also prints sharp examples where a size-(k-1) neighbourhood is properly
contained in a larger neighbourhood, so equality of neighbourhoods is not
forced when only one terminal has minimum degree.
"""


def pairs(n):
    return [(i,j) for i in range(n) for j in range(i+1,n)]


def adj_from_mask(n, mask):
    es=pairs(n)
    adj=[0]*n
    for b,(i,j) in enumerate(es):
        if (mask>>b)&1:
            adj[i]|=1<<j; adj[j]|=1<<i
    return adj


def connected(adj):
    n=len(adj)
    seen=1
    frontier=1
    while frontier:
        ubit=frontier & -frontier
        frontier-=ubit
        u=ubit.bit_length()-1
        new=adj[u] & ~seen
        seen |= new
        frontier |= new
    return seen==(1<<n)-1


def edge_list(adj):
    return [(i,j) for i in range(len(adj)) for j in range(i+1,len(adj)) if (adj[i]>>j)&1]


def remove_edge(adj,e):
    i,j=e
    b=[x for x in adj]
    b[i]&=~(1<<j); b[j]&=~(1<<i)
    return b


def k_colorings(adj,k, stop_after=None):
    n=len(adj)
    order=sorted(range(n), key=lambda v: (adj[v].bit_count(),v), reverse=True)
    col=[-1]*n
    out=[]
    def rec(t):
        if stop_after is not None and len(out)>=stop_after:
            return
        if t==n:
            out.append(tuple(col)); return
        v=order[t]
        forbidden=0
        nb=adj[v]
        while nb:
            bit=nb & -nb; nb-=bit; w=bit.bit_length()-1
            c=col[w]
            if c>=0: forbidden|=1<<c
        for c in range(k):
            if not ((forbidden>>c)&1):
                col[v]=c; rec(t+1); col[v]=-1
    rec(0)
    return out


def colorable(adj,k):
    return bool(k_colorings(adj,k,1))


def chromatic(adj, maxk=5):
    for k in range(1,maxk+1):
        if colorable(adj,k): return k
    return maxk+1


def edge_critical(adj,k):
    if chromatic(adj,k)!=k: return False
    for e in edge_list(adj):
        if not colorable(remove_edge(adj,e),k-1): return False
    return True


def colors_on(c,S):
    return {c[v] for v in range(len(c)) if (S>>v)&1}


def lists_for(c,S,k):
    return set(range(k))-colors_on(c,S)


def forced_equal_direct(core_colorings,k,A,B):
    any_extension=False
    for c in core_colorings:
        LA=lists_for(c,A,k); LB=lists_for(c,B,k)
        for a in LA:
            for b in LB:
                any_extension=True
                if a!=b: return False
    return any_extension


def corrected_criterion(core_colorings,k,A,B):
    any_extension=False
    for c in core_colorings:
        LA=lists_for(c,A,k); LB=lists_for(c,B,k)
        if LA and LB:
            any_extension=True
            if len(LA)!=1 or LA!=LB: return False
    return any_extension


def subset_vertices(S,n):
    return tuple(i for i in range(n) if (S>>i)&1)


def saturation_holds(adj,k,A,B):
    """Necessary condition for every exclusive a in A\\B."""
    n=len(adj)
    for a in range(n):
        if not ((A>>a)&1) or ((B>>a)&1):
            continue
        for z in range(n):
            if not ((adj[a]>>z)&1):
                continue
            H=remove_edge(adj,(min(a,z),max(a,z)))
            phis=k_colorings(H,k-1)
            assert phis, ("edge critical colouring missing",a,z)
            for phi in phis:
                seen={phi[x] for x in range(n) if x!=a and ((A>>x)&1)}
                if len(seen)!=k-1:
                    return False
    return True


def verify():
    total_graphs=0
    critical_counts={3:0,4:0}
    attachment_pairs=0
    forced_pairs=0
    sharp={3:None,4:None}
    saturation_checks=0
    for n in range(2,7):
        m=n*(n-1)//2
        for mask in range(1<<m):
            adj=adj_from_mask(n,mask)
            if not connected(adj): continue
            total_graphs+=1
            for k in (3,4):
                if n<k or not edge_critical(adj,k): continue
                critical_counts[k]+=1
                cols=k_colorings(adj,k)
                subsets=range(1,1<<n)
                for A in subsets:
                    for B in subsets:
                        if A==B: continue
                        d=forced_equal_direct(cols,k,A,B)
                        q=corrected_criterion(cols,k,A,B)
                        attachment_pairs+=1
                        assert d==q, ("criterion mismatch",n,k,A,B)
                        if not d: continue
                        forced_pairs+=1
                        assert saturation_holds(adj,k,A,B), ("A saturation failure",n,k,A,B)
                        assert saturation_holds(adj,k,B,A), ("B saturation failure",n,k,A,B)
                        saturation_checks+=2
                        a_size=A.bit_count(); b_size=B.bit_count()
                        if a_size<=k-1:
                            assert A & ~B == 0, ("A inclusion failure",n,k,A,B,edge_list(adj))
                        if b_size<=k-1:
                            assert B & ~A == 0, ("B inclusion failure",n,k,A,B,edge_list(adj))
                        if a_size==k-1 and b_size==k-1:
                            assert A==B, ("minimum-neighbourhood equality failure",n,k,A,B)
                        if sharp[k] is None and a_size==k-1 and b_size>k-1 and (A & ~B)==0:
                            sharp[k]=(n,edge_list(adj),subset_vertices(A,n),subset_vertices(B,n))
    print("connected_labelled_graphs_checked",total_graphs)
    print("edge_critical_k3_cores",critical_counts[3])
    print("edge_critical_k4_cores",critical_counts[4])
    print("ordered_attachment_pairs_checked",attachment_pairs)
    print("forced_equal_attachment_pairs",forced_pairs)
    print("directed_saturation_conditions_checked",saturation_checks)
    print("sharp_k3_example",sharp[3])
    print("sharp_k4_example",sharp[4])
    print("ALL_CHECKS_PASSED")

if __name__=='__main__':
    verify()
