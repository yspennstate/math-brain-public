#!/usr/bin/env python3
"""Exact finite reduction for R01 / KIM-MATTMAN-OH-2026-TFIK22-D34.

Target profile: triangle-free simple graphs with 22 edges and degree profile
(n4,n3)=(5,8).  Vertices 0..4 are the five degree-4 vertices A and 5..12
are the eight degree-3 vertices B.

The script:
  * enumerates all 14 unlabeled triangle-free induced graphs H=G[A];
  * enumerates all B-to-A incidence multisets satisfying the exact degree sums;
  * uses the source pair-deletion edge-count criterion only when its upper bound
    is <=8, which is an unconditional nIK certificate;
  * exhaustively completes the B-B graph, enforcing exact degrees and triangle-freeness;
  * runs the exact combinatorial planarity algorithm on every vertex-pair deletion
    (2-apex test);
  * deduplicates the non-2-apex survivors by graph isomorphism;
  * checks immediate proper minors of survivor representatives.

No floating point arithmetic is used.  NetworkX check_planarity implements a
combinatorial planarity algorithm.  This is a self-check, not an independent audit.
"""
from __future__ import annotations
import itertools
import networkx as nx

A = tuple(range(5))
B = tuple(range(5,13))


def triangle_count(G):
    return sum(nx.triangles(G).values()) // 3


def triangle_free_five_vertex_types():
    out=[]
    for G in nx.graph_atlas_g():
        if G.number_of_nodes()!=5:
            continue
        G=nx.convert_node_labels_to_integers(G)
        if triangle_count(G)==0:
            out.append(G)
    out.sort(key=lambda g:(g.number_of_edges(), sorted(dict(g.degree()).values()), nx.to_graph6_bytes(g, header=False)))
    assert len(out)==14
    return out


def independent_subsets(H):
    out=[]
    for r in range(4):
        for S in itertools.combinations(A,r):
            if H.subgraph(S).number_of_edges()==0:
                out.append(tuple(S))
    return out


def incidence_multisets(H):
    """Eight B-neighborhoods in A, unordered, exact A-column sums."""
    caps=tuple(4-H.degree(i) for i in A)
    subs=independent_subsets(H)
    vecs=[tuple(int(i in S) for i in A) for S in subs]
    ans=[]
    def rec(start,k,rem,chosen):
        if k==0:
            if all(x==0 for x in rem):
                ans.append(tuple(chosen))
            return
        for j in range(start,len(subs)):
            v=vecs[j]
            if all(v[i] <= rem[i] for i in A):
                new=tuple(rem[i]-v[i] for i in A)
                chosen.append(j)
                rec(j,k-1,new,chosen)
                chosen.pop()
    rec(0,8,caps,[])
    return subs,ans


def pair_deletion_upper_bound(H, rows, a,b):
    """Valid for a,b nonadjacent degree-4 vertices.

    After deleting a,b, suppressing the degree <=2 vertices forced by their
    degree-3 neighbors and common degree-4 neighbors leaves at most
       6 + r_a+r_b+t_ab-c_ab
    edges. Further cascades only lower this number.
    """
    assert not H.has_edge(a,b)
    ra,rb=H.degree(a),H.degree(b)
    t=sum((a in S and b in S) for S in rows)
    c=len(set(H.neighbors(a)) & set(H.neighbors(b)))
    return 6+ra+rb+t-c


def incidence_survives_source_le8_filter(H, rows):
    for a,b in itertools.combinations(A,2):
        if H.has_edge(a,b):
            continue
        if pair_deletion_upper_bound(H,rows,a,b) <= 8:
            return False
    return True


def bb_completions(rows):
    """All labelled simple triangle-free B-graphs with exact residual degrees.

    If two B vertices share an A-neighbor then they may not be adjacent, otherwise
    A-B-B is a triangle. We also forbid triangles internal to B.
    """
    n=8
    target=[3-len(S) for S in rows]
    allowed=[[i!=j and set(rows[i]).isdisjoint(rows[j]) for j in range(n)] for i in range(n)]
    G=nx.Graph(); G.add_nodes_from(range(n))
    rem=target[:]

    def rec():
        if all(r==0 for r in rem):
            yield tuple(sorted(G.edges()))
            return
        cand=[i for i,r in enumerate(rem) if r>0]
        i=min(cand, key=lambda u:(sum(1 for v in range(n) if v!=u and rem[v]>0 and allowed[u][v] and not G.has_edge(u,v)), -rem[u],u))
        di=rem[i]
        avail=[v for v in range(n) if v!=i and rem[v]>0 and allowed[i][v] and not G.has_edge(i,v)]
        if len(avail)<di:
            return
        for nbrs in itertools.combinations(avail,di):
            ok=True
            for v in nbrs:
                if set(G.neighbors(i)) & set(G.neighbors(v)):
                    ok=False; break
            if ok:
                for v,w in itertools.combinations(nbrs,2):
                    if G.has_edge(v,w):
                        ok=False; break
            if not ok:
                continue
            for v in nbrs:
                G.add_edge(i,v); rem[v]-=1
            old=rem[i]; rem[i]=0
            bad=any(r<0 for r in rem)
            if not bad:
                for u in range(n):
                    if rem[u]>0:
                        av=sum(1 for v in range(n) if v!=u and rem[v]>0 and allowed[u][v] and not G.has_edge(u,v))
                        if av<rem[u]:
                            bad=True; break
            if not bad:
                yield from rec()
            rem[i]=old
            for v in nbrs:
                rem[v]+=1; G.remove_edge(i,v)
    yield from rec()


def build_graph(H,rows,bedges):
    G=nx.Graph(); G.add_nodes_from(range(13)); G.add_edges_from(H.edges())
    for j,S in enumerate(rows):
        bj=5+j
        for a in S: G.add_edge(a,bj)
    for u,v in bedges: G.add_edge(5+u,5+v)
    return G


def is_2apex(G, witness=False):
    for a,b in itertools.combinations(sorted(G.nodes()),2):
        H=G.copy(); H.remove_nodes_from((a,b))
        if nx.check_planarity(H)[0]:
            return (True,(a,b)) if witness else True
    return (False,None) if witness else False


def contract_simple(G,e):
    u,v=e
    H=nx.contracted_nodes(G,u,v,self_loops=False)
    return nx.convert_node_labels_to_integers(nx.Graph(H))


def immediate_minor_summary(G):
    out={"delete":[],"contract":[],"vdelete":[]}
    for e in sorted(G.edges()):
        H=G.copy(); H.remove_edge(*e)
        if not is_2apex(H): out["delete"].append(e)
        H=contract_simple(G,e)
        if not is_2apex(H): out["contract"].append(e)
    for v in sorted(G.nodes()):
        H=G.copy(); H.remove_node(v)
        if not is_2apex(H): out["vdelete"].append(v)
    return out


def degsig(G):
    c={d:0 for d in range(14)}
    for _,d in G.degree(): c[d]+=1
    return tuple((d,c[d]) for d in range(14) if c[d])


def main():
    types=triangle_free_five_vertex_types()
    print("TFIK22 (5,8) exact finite reduction")
    print("triangle-free H=G[A] isomorphism types:",len(types))
    all_non2=[]
    table=[]
    for idx,H in enumerate(types):
        subs,msets=incidence_multisets(H)
        surviving=[]
        for inds in msets:
            rows=tuple(subs[j] for j in inds)
            if incidence_survives_source_le8_filter(H,rows):
                surviving.append(rows)
        completions=twoapex=non2=0
        for rows in surviving:
            for bedges in bb_completions(rows):
                G=build_graph(H,rows,bedges)
                assert G.number_of_nodes()==13 and G.number_of_edges()==22
                assert triangle_count(G)==0
                assert sorted(dict(G.degree()).values()) == [3]*8+[4]*5
                completions+=1
                if is_2apex(G):
                    twoapex+=1
                else:
                    non2+=1
                    all_non2.append((idx,H.copy(),rows,bedges,G.copy()))
        table.append((idx,H.number_of_edges(),tuple(sorted(dict(H.degree()).values())),len(msets),len(surviving),completions,twoapex,non2))
        print("H%02d e=%d deg=%s incidence=%d survives_le8=%d completions=%d two_apex=%d non2apex=%d" % table[-1])

    classes=[]
    for item in all_non2:
        G=item[4]
        for cl in classes:
            if nx.is_isomorphic(G,cl[0][4]):
                cl.append(item); break
        else:
            classes.append([item])
    print("TOTAL_NON2APEX_LABELLED",len(all_non2))
    print("TOTAL_NON2APEX_ISO_CLASSES",len(classes))
    assert len(all_non2)==15
    assert len(classes)==4

    classes.sort(key=lambda cl:(cl[0][0],tuple(sorted(cl[0][4].edges()))))
    for j,cl in enumerate(classes,1):
        idx,H,rows,bedges,G=cl[0]
        print("CLASS",j,"Htype",idx,"multiplicity",len(cl),"Hedges",tuple(sorted(H.edges())))
        print("  rows",rows)
        print("  Bedges",bedges)
        print("  full_edges",tuple(sorted(G.edges())))
        m=immediate_minor_summary(G)
        print("  non2apex_immediate_deletions",tuple(m["delete"]))
        print("  non2apex_immediate_contractions",tuple(m["contract"]))
        print("  non2apex_immediate_vertex_deletions",tuple(m["vdelete"]))
        if not m["delete"] and not m["contract"] and not m["vdelete"]:
            print("  COMPUTED_MMN2A yes")
        else:
            print("  COMPUTED_MMN2A no")
        for e in m["contract"]:
            M=contract_simple(G,e)
            if M.number_of_edges()==21 and not is_2apex(M) and triangle_count(M)==0:
                print("  TF_NON2APEX_21_CONTRACTION",e,"order",M.number_of_nodes(),"degsig",degsig(M),"edges",tuple(sorted(M.edges())))

    minimal=[]; h12minor=[]
    for cl in classes:
        G=cl[0][4]; m=immediate_minor_summary(G)
        minimal.append(not any(m.values()))
        found=False
        for e in m["contract"]:
            M=contract_simple(G,e)
            if M.number_of_nodes()==12 and M.number_of_edges()==21 and triangle_count(M)==0 and not is_2apex(M) and degsig(M)==((3,6),(4,6)):
                found=True
        h12minor.append(found)
    print("MMN2A_PATTERN",tuple(minimal))
    print("H12_SIGNATURE_MINOR_PATTERN",tuple(h12minor))
    assert tuple(minimal)==(True,False,False,True)
    assert tuple(h12minor)==(False,True,True,False)
    print("ALL_EXACT_TFIK22_58_REDUCTION_CHECKS_PASS")

if __name__=='__main__':
    main()
