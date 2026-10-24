#!/usr/bin/env python3
"""Exact colored-two-graph quotient certificate for R7-06 / F0011 through n=8.

This script starts from the exact diagonal-switching-normalized census used in the
previous F0011 run, and adds the quotient by coordinate permutations.

For a symmetric sign matrix M, with off-diagonal signs s_ij and diagonal signs d_i,
define the switching invariant tau_ijk=s_ij*s_jk*s_ki.  The pair
    (d_i ; {ijk : tau_ijk=-1})
is a colored two-graph.  Equality up to a vertex permutation is exactly equivalence
under signed-permutation conjugation M -> P^T D M D P.

We enumerate all switching-normalized matrices through n=8 exactly:
  * diagonal switching fixes the first-row off-diagonal signs to +1;
  * the remaining off-diagonal pattern is a graph on n-1 vertices;
  * NetworkX graph_atlas_g() is a complete atlas of unlabeled graphs through 7
    vertices, and each atlas graph is weighted by (n-1)!/|Aut(G)|;
  * all 2^n diagonal sign patterns are enumerated;
  * integrality is certified by integer power sums tr(M^k), k=1,...,n, matched
    against all integer spectra satisfying the exact trace-square/parity constraints.

The signed-permutation orbits inside each integral-spectrum fiber are then obtained
by exact graph isomorphism of an incidence graph encoding the colored two-graph.
No floating eigenvalue computation is used.
"""
from itertools import combinations, combinations_with_replacement
from collections import Counter, defaultdict
from fractions import Fraction
import math
import numpy as np
import networkx as nx

ATLAS = nx.graph_atlas_g()
EXPECTED_I = {1:2,2:2,3:10,4:10,5:154,6:274,7:15446,8:111290}
EXPECTED_KMAX = {1:1,2:1,3:1,4:1,5:1,6:1,7:2,8:5}
EXPECTED_FMAX = {1:1,2:1,3:3,4:6,5:30,6:45,7:1575,8:24360}

def candidates(n):
    """All possible sorted integral spectra under exact necessary constraints."""
    out=[]
    for lam in combinations_with_replacement(range(-n,n+1),n):
        if sum(x*x for x in lam) != n*n:
            continue
        # Exact mod-2 theorem for symmetric sign matrices.
        if n % 2 == 0:
            if any(x & 1 for x in lam):
                continue
        else:
            if sum(abs(x) & 1 for x in lam) != 1:
                continue
        tr=sum(lam)
        if abs(tr)>n or ((tr-n)&1):
            continue
        powers=tuple(sum(x**k for x in lam) for k in range(1,n+1))
        out.append((lam,powers))
    return out

def atlas_graphs(m):
    if m == 0:
        return [nx.empty_graph(0)]
    return [g for g in ATLAS if g.number_of_nodes()==m]

def aut_size(g):
    if g.number_of_nodes() <= 1:
        return 1
    return sum(1 for _ in nx.algorithms.isomorphism.GraphMatcher(g,g).isomorphisms_iter())

def build_normalized_A(n,g):
    """Zero-diagonal off-diagonal sign matrix, first row normalized to +1."""
    A=np.zeros((n,n),dtype=np.int64)
    if n>1:
        A[0,1:]=1
        A[1:,0]=1
    for i in range(n-1):
        for j in range(i+1,n-1):
            v=1 if g.has_edge(i,j) else -1
            A[i+1,j+1]=A[j+1,i+1]=v
    return A

def diag_patterns(n):
    ids=np.arange(1<<n,dtype=np.uint16)
    D=np.empty((1<<n,n),dtype=np.int64)
    for i in range(n):
        # Cast before subtraction: avoid unsigned underflow.
        D[:,i]=2*((ids>>i)&1).astype(np.int64)-1
    return D

def colored_twograph_incidence(M):
    """Exact isomorphism object for diagonal-switching + permutation quotient."""
    n=M.shape[0]
    H=nx.Graph()
    for i in range(n):
        H.add_node(("v",i), kind=0, diag=int(M[i,i]))
    tid=0
    for i,j,k in combinations(range(n),3):
        tau=int(M[i,j]*M[j,k]*M[k,i])
        if tau == -1:
            t=("t",tid); tid+=1
            H.add_node(t, kind=1, diag=0)
            H.add_edge(t,("v",i)); H.add_edge(t,("v",j)); H.add_edge(t,("v",k))
    return H

NODE_MATCH=nx.algorithms.isomorphism.categorical_node_match(["kind","diag"],[-1,0])

def same_colored_twograph(H1,H2):
    if H1.number_of_nodes()!=H2.number_of_nodes() or H1.number_of_edges()!=H2.number_of_edges():
        return False
    return nx.is_isomorphic(H1,H2,node_match=NODE_MATCH)

def classify(n):
    C=candidates(n)
    by_ps={p:lam for lam,p in C}
    assert len(by_ps)==len(C)
    D=diag_patterns(n)
    idx=np.arange(n)
    spec=Counter()
    # representatives[lambda] stores (colored-two-graph incidence graph, exact
    # number of switching-normalized labeled matrices represented by this item).
    representatives=defaultdict(list)
    total=0

    for g in atlas_graphs(n-1):
        aut=aut_size(g)
        w=math.factorial(n-1)//aut
        A=build_normalized_A(n,g)
        M=np.broadcast_to(A,(1<<n,n,n)).copy()
        M[:,idx,idx]=D
        total += w*(1<<n)

        # Integer traces.  For n<=8, |(M^k)_ij| <= n^(k-1), safely in int64.
        P=M.copy()
        traces=[np.trace(P,axis1=1,axis2=2)]
        for k in range(2,n+1):
            P=P@M
            traces.append(np.trace(P,axis1=1,axis2=2))

        for d in range(1<<n):
            powers=tuple(int(traces[k][d]) for k in range(n))
            lam=by_ps.get(powers)
            if lam is None:
                continue
            spec[lam]+=w
            H=colored_twograph_incidence(M[d])
            representatives[lam].append((H,w))

    expected_total=1 << (n + (n-1)*(n-2)//2)
    assert total==expected_total,(n,total,expected_total)
    I=sum(spec.values())
    assert I==EXPECTED_I[n],(n,I,EXPECTED_I[n])

    # Cluster exact switching-normalized mass by colored-two-graph isomorphism.
    orbit_sizes_by_spec={}
    for lam,reps in representatives.items():
        clusters=[]  # [representative graph, total exact weight]
        for H,w in reps:
            for c in clusters:
                if same_colored_twograph(H,c[0]):
                    c[1]+=w
                    break
            else:
                clusters.append([H,w])
        sizes=sorted((c[1] for c in clusters), reverse=True)
        # Every full signed-permutation orbit intersects the switching-normalized
        # transversal in n!/|Aut_colored_two_graph| representatives.
        assert all(math.factorial(n)%s==0 for s in sizes),(n,lam,sizes)
        assert sum(sizes)==spec[lam]
        orbit_sizes_by_spec[lam]=sizes

    Kmax=max(len(v) for v in orbit_sizes_by_spec.values())
    Fmax=max(spec.values())
    assert Kmax==EXPECTED_KMAX[n],(n,Kmax)
    assert Fmax==EXPECTED_FMAX[n],(n,Fmax)
    return C,spec,total,orbit_sizes_by_spec,len(atlas_graphs(n-1))

def main():
    print("F0011 exact colored-two-graph quotient certificate")
    print("n atlas_graphs candidates total I_n spectra colored_classes Kmax Fmax probability")
    results={}
    for n in range(1,9):
        C,spec,total,orbits,ng=classify(n)
        Ktotal=sum(len(v) for v in orbits.values())
        Kmax=max(len(v) for v in orbits.values())
        Fmax=max(spec.values())
        f=Fraction(sum(spec.values()),total)
        print(n,ng,len(C),total,sum(spec.values()),len(spec),Ktotal,Kmax,Fmax,
              f"{f.numerator}/{f.denominator}")
        results[n]=(spec,orbits)

    print("\nn=7 spectra with maximum colored-two-graph multiplicity")
    spec7,orb7=results[7]
    for lam in sorted(l for l,v in orb7.items() if len(v)==2):
        print(lam,"F=",spec7[lam],"signed-permutation orbit sizes=",orb7[lam])

    print("\nn=8 spectra with maximum colored-two-graph multiplicity")
    spec8,orb8=results[8]
    extremal=sorted(l for l,v in orb8.items() if len(v)==5)
    for lam in extremal:
        print(lam,"F=",spec8[lam],"signed-permutation orbit sizes=",orb8[lam])

    expected_extremal=[
        (-4,-4,-2,-2,0,2,2,4),
        (-4,-2,-2,0,2,2,4,4),
    ]
    assert extremal==expected_extremal
    expected_sizes=[10080,5040,5040,2520,1680]
    assert all(orb8[lam]==expected_sizes for lam in extremal)

    print("\nExact theorem checked:")
    print("K_n(lambda) <= F_n(lambda) <= n! K_n(lambda) fiber-by-fiber;")
    print("finite values through n=8 have max K_n = 1,1,1,1,1,1,2,5.")
    print("ALL_EXACT_ASSERTIONS_PASS")

if __name__=="__main__":
    main()
