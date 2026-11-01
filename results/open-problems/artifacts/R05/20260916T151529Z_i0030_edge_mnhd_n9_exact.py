#!/usr/bin/env python3
# Exact finite certificate for R05 / Aldous-Fill Open Problem 7.30.
# Classifies ALL connected arc-transitive simple graphs on 9 labeled vertices
# via exhaustive labeled regular-graph enumeration and exact automorphism checks.
#
# No floating-point arithmetic is used.

import itertools
import math
import networkx as nx

N=9

def connected(adj):
    n=len(adj)
    seen=1
    stack=[0]
    while stack:
        i=stack.pop()
        m=adj[i]
        for j in range(n):
            if ((m>>j)&1) and not ((seen>>j)&1):
                seen |= (1<<j)
                stack.append(j)
    return seen == (1<<n)-1

def complement(adj):
    n=len(adj)
    full=(1<<n)-1
    return tuple(full ^ (1<<i) ^ adj[i] for i in range(n))

def degree(adj,i):
    return int(adj[i].bit_count())

def enumerate_labeled_regular(n,d,callback):
    # Unique recursion: when the least unfinished vertex i is processed,
    # choose all still-missing neighbors of i among higher-index vertices.
    deg=[0]*n
    adj=[0]*n
    total=0

    def rec(i):
        nonlocal total
        while i<n and deg[i]==d:
            i+=1
        if i==n:
            total += 1
            callback(tuple(adj))
            return

        need=d-deg[i]
        candidates=[j for j in range(i+1,n) if deg[j]<d]
        if need<0 or need>len(candidates):
            return

        for comb in itertools.combinations(candidates,need):
            ok=True
            for j in comb:
                deg[i]+=1
                deg[j]+=1
                if deg[j]>d:
                    ok=False
                adj[i] |= (1<<j)
                adj[j] |= (1<<i)
            if ok:
                # Exact degree-feasibility pruning. This is only a necessary
                # completion test; it never removes a realizable graph.
                feasible=True
                for j in range(i+1,n):
                    if deg[j]>d:
                        feasible=False
                        break
                    avail=sum(1 for k in range(i+1,n)
                              if k!=j and deg[k]<d and not ((adj[j]>>k)&1))
                    if deg[j]+avail < d:
                        feasible=False
                        break
                if feasible:
                    rec(i+1)
            for j in comb:
                deg[i]-=1
                deg[j]-=1
                adj[i] &= ~(1<<j)
                adj[j] &= ~(1<<i)
    rec(0)
    return total

def necessary_arc_prefilter(adj,d):
    # Every arc-transitive graph is vertex-transitive and edge-transitive.
    # Hence:
    # (1) common-neighbor count is constant on edges;
    # (2) for each vertex, the multiset of common-neighbor counts with
    #     non-neighbors is vertex-invariant.
    # These exact invariants are necessary, not assumed sufficient.
    if not connected(adj):
        return False

    edge_common=None
    n=len(adj)
    for i in range(n):
        if degree(adj,i)!=d:
            return False
        for j in range(i+1,n):
            if (adj[i]>>j)&1:
                c=(adj[i]&adj[j]).bit_count()
                if edge_common is None:
                    edge_common=c
                elif c!=edge_common:
                    return False

    vertex_sig=None
    for i in range(n):
        sig=tuple(sorted(
            (adj[i]&adj[j]).bit_count()
            for j in range(n)
            if j!=i and not ((adj[i]>>j)&1)
        ))
        if vertex_sig is None:
            vertex_sig=sig
        elif sig!=vertex_sig:
            return False
    return True

def to_nx(adj):
    G=nx.Graph()
    G.add_nodes_from(range(len(adj)))
    for i in range(len(adj)):
        for j in range(i+1,len(adj)):
            if (adj[i]>>j)&1:
                G.add_edge(i,j)
    return G

def automorphisms(adj):
    G=to_nx(adj)
    GM=nx.algorithms.isomorphism.GraphMatcher(G,G)
    return list(GM.isomorphisms_iter())

def arc_transitive_from_auts(adj,auts):
    arcs=[(i,j) for i in range(len(adj)) for j in range(len(adj))
          if (adj[i]>>j)&1]
    base=arcs[0]
    orbit={(phi[base[0]],phi[base[1]]) for phi in auts}
    return len(orbit)==len(arcs), len(orbit), len(arcs)

def graph6(adj):
    G=to_nx(adj)
    return nx.to_graph6_bytes(G,header=False).decode().strip()

def exact_walk_identity(adj,max_m=20):
    # Verify (A^(m+1))_{xx}=d(A^m)_{xy} for every oriented edge.
    # This is the coefficient identity behind a'(t)=b(t)-a(t).
    n=len(adj)
    d=degree(adj,0)
    A=[[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            A[i][j]=1 if ((adj[i]>>j)&1) else 0

    def matmul(X,Y):
        return [[sum(X[i][k]*Y[k][j] for k in range(n))
                 for j in range(n)] for i in range(n)]

    I=[[int(i==j) for j in range(n)] for i in range(n)]
    powers=[I,A]
    for _ in range(2,max_m+2):
        powers.append(matmul(powers[-1],A))

    for m in range(max_m+1):
        Am=powers[m]
        Amp1=powers[m+1]
        diag={Am[i][i] for i in range(n)}
        if len(diag)!=1:
            return False,("diag",m,diag)
        edgevals={Am[i][j] for i in range(n) for j in range(n)
                  if (adj[i]>>j)&1}
        if len(edgevals)!=1:
            return False,("edge",m,edgevals)
        for i in range(n):
            for j in range(n):
                if (adj[i]>>j)&1:
                    if Amp1[i][i] != d*Am[i][j]:
                        return False,("identity",m,i,j,Amp1[i][i],d*Am[i][j])
    return True,None

# For n=9, nd is even, so every regular graph has even degree.
# Connected arc-transitive graphs therefore can only have d=2,4,6,8.
summary={}
representatives={}

summary[2]={"total":0,"connected":0,"prefilter":0}
def process_d2(adj):
    summary[2]["total"] += 1
    if connected(adj):
        summary[2]["connected"] += 1
        if necessary_arc_prefilter(adj,2):
            summary[2]["prefilter"] += 1
            representatives.setdefault(2,adj)
tot2=enumerate_labeled_regular(N,2,process_d2)
assert tot2==summary[2]["total"]

summary[4]={"total":0,"connected":0,"prefilter":0}
def process_d4(adj):
    summary[4]["total"] += 1
    if connected(adj):
        summary[4]["connected"] += 1
        if necessary_arc_prefilter(adj,4):
            summary[4]["prefilter"] += 1
            representatives.setdefault(4,adj)
tot4=enumerate_labeled_regular(N,4,process_d4)
assert tot4==summary[4]["total"]

# d=6 is the complement of d=2, bijectively on labeled graphs.
summary[6]={"total":0,"connected":0,"prefilter":0}
def process_for_d6(adj2):
    adj=complement(adj2)
    summary[6]["total"] += 1
    if connected(adj):
        summary[6]["connected"] += 1
        if necessary_arc_prefilter(adj,6):
            summary[6]["prefilter"] += 1
            representatives.setdefault(6,adj)
enumerate_labeled_regular(N,2,process_for_d6)

# d=8: unique K9.
full=(1<<N)-1
K9=tuple(full ^ (1<<i) for i in range(N))
summary[8]={"total":1,"connected":1,"prefilter":1}
representatives[8]=K9

# Generated exact raw counts.
assert summary[2]["total"]==30016, summary[2]
assert summary[4]["total"]==1024380, summary[4]
assert summary[6]["total"]==30016, summary[6]
assert summary[8]["total"]==1

# Exact necessary-prefilter counts.
assert summary[2]["connected"]==20160, summary[2]
assert summary[2]["prefilter"]==20160, summary[2]
assert summary[4]["connected"]==1024380, summary[4]
assert summary[4]["prefilter"]==5040, summary[4]
assert summary[6]["connected"]==30016, summary[6]
assert summary[6]["prefilter"]==280, summary[6]
assert summary[8]["prefilter"]==1

accepted=[]
for d in (2,4,6,8):
    rep=representatives[d]
    auts=automorphisms(rep)
    is_arc,orbit_size,narcs=arc_transitive_from_auts(rep,auts)
    assert is_arc

    aut_order=len(auts)
    label_orbit=math.factorial(N)//aut_order

    # All relabelings of an accepted representative pass the necessary
    # prefilter. If its relabeling orbit already exhausts the entire
    # prefilter candidate set, there can be no additional arc-transitive class.
    assert label_orbit==summary[d]["prefilter"], (
        d,label_orbit,summary[d]["prefilter"],aut_order
    )

    ok,why=exact_walk_identity(rep,20)
    assert ok,why

    accepted.append({
        "degree":d,
        "graph6":graph6(rep),
        "aut_order":aut_order,
        "oriented_arcs":narcs,
        "arc_orbit":orbit_size,
        "labeled_orbit":label_orbit,
        "walk_identity_m_max":20,
    })

assert len(accepted)==4

print("R05 I0030 exact n=9 certificate")
print("n",N)
print("parity_allowed_connected_degrees", [2,4,6,8])
for d in (2,4,6,8):
    print("degree",d,
          "labeled_regular_total",summary[d]["total"],
          "connected",summary[d]["connected"],
          "necessary_prefilter",summary[d]["prefilter"])
print("arc_transitive_isomorphism_types",len(accepted))
for row in accepted:
    print("AT",
          "degree",row["degree"],
          "graph6",row["graph6"],
          "aut_order",row["aut_order"],
          "oriented_arcs",row["oriented_arcs"],
          "arc_orbit",row["arc_orbit"],
          "labeled_orbit",row["labeled_orbit"],
          "walk_identity_m_max",row["walk_identity_m_max"])
print("all_prefilter_candidates_exhausted_by_relabel_orbits",True)
print("metric_largest_fully_certified_vertex_count",9)
print("RESULT PASS")
