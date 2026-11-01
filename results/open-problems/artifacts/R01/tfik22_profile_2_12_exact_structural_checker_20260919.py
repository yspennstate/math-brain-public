#!/usr/bin/env python3
"""Exact finite core for the R01 triangle-free IK 22-edge profile (n4,n3)=(2,12).

The proof outside this script reduces every graph in the profile to the cases
checked here whenever G-{a,b} is nonplanar, where a,b are the two degree-4
vertices.  The script then:
  * checks every nonplanar structural orbit for nonadjacent a,b with t=3,4;
  * checks all connected nonplanar structural words for adjacent a,b (22,530
    color-word placements on a K_3,3 subdivision);
  * checks the only disconnected nonplanar adjacent-a,b cases;
  * deduplicates the non-2-apex survivors exactly by graph isomorphism;
  * independently generates the pure-Delta-Y K7 family and full
    Delta-Y/Y-Delta K_{3,3,1,1} family;
  * proves the three survivor classes are respectively C14+e, a one-edge
    split of the unique order-13 pure-Delta-Y K7 descendant, and the unique
    order-14 K_{3,3,1,1}-family graph.

All graph and planarity computations are combinatorial; there is no floating
point arithmetic.  NetworkX's planarity routine is an exact combinatorial
planarity test.  This is a self-check, not an independent audit.
"""
from __future__ import annotations
import itertools
from collections import Counter, deque
import networkx as nx

K33_EDGES = tuple((i,3+j) for i in range(3) for j in range(3))


def triangles(G):
    return sum(nx.triangles(G).values()) // 3


def is_2apex(G):
    for u,v in itertools.combinations(sorted(G.nodes()),2):
        H=G.copy(); H.remove_nodes_from((u,v))
        if nx.check_planarity(H)[0]:
            return True,(u,v)
    return False,None


def target_ok(G):
    return (G.number_of_nodes()==14 and G.number_of_edges()==22 and
            triangles(G)==0 and
            Counter(dict(G.degree()).values())==Counter({3:12,4:2}))


def graph_sig(G):
    return (G.number_of_nodes(), tuple(sorted(dict(G.degree()).values())))


def iso_index(fam,G):
    s=graph_sig(G)
    for i,H in enumerate(fam):
        if graph_sig(H)==s and nx.is_isomorphic(G,H): return i
    return None


def dy_moves(G):
    for a,b,c in itertools.combinations(sorted(G.nodes()),3):
        if G.has_edge(a,b) and G.has_edge(a,c) and G.has_edge(b,c):
            H=G.copy(); H.remove_edges_from(((a,b),(a,c),(b,c)))
            w=max(H.nodes())+1
            H.add_node(w); H.add_edges_from(((w,a),(w,b),(w,c)))
            yield nx.convert_node_labels_to_integers(H),("DY",(a,b,c))


def yd_moves(G):
    for v in sorted(G.nodes()):
        if G.degree(v)!=3: continue
        N=tuple(sorted(G.neighbors(v)))
        if any(G.has_edge(a,b) for a,b in itertools.combinations(N,2)): continue
        H=G.copy(); H.remove_node(v); H.add_edges_from(itertools.combinations(N,2))
        yield nx.convert_node_labels_to_integers(H),("YD",v,N)


def closure(base, allow_yd):
    fam=[base]; parent=[None]; q=deque([0])
    while q:
        i=q.popleft(); moves=dy_moves(fam[i])
        if allow_yd: moves=itertools.chain(moves,yd_moves(fam[i]))
        for H,mv in moves:
            if iso_index(fam,H) is None:
                fam.append(H); parent.append((i,mv)); q.append(len(fam)-1)
    return fam,parent


def k7(): return nx.complete_graph(7)


def k3311():
    parts=((0,1,2),(3,4,5),(6,),(7,))
    G=nx.Graph(); G.add_nodes_from(range(8))
    for i in range(4):
        for j in range(i+1,4):
            G.add_edges_from((u,v) for u in parts[i] for v in parts[j])
    assert G.number_of_edges()==22
    return G


def alt_word(k,start):
    return tuple(start if i%2==0 else ('B' if start=='R' else 'R') for i in range(k))

WORD_OPTIONS=[()]
for k in range(1,7):
    WORD_OPTIONS.extend((alt_word(k,'R'),alt_word(k,'B')))
WORD_OPTIONS=list(dict.fromkeys(WORD_OPTIONS))


def word_assignments(rtot,btot):
    out=[]
    def rec(i,r,b,cur):
        if i==9:
            if r==rtot and b==btot: out.append(tuple(cur))
            return
        for w in WORD_OPTIONS:
            rr=w.count('R'); bb=w.count('B')
            if r+rr<=rtot and b+bb<=btot:
                cur.append(w); rec(i+1,r+rr,b+bb,cur); cur.pop()
    rec(0,0,0,[])
    return out


def subdivided_k33(words):
    G=nx.Graph(); G.add_nodes_from(range(6)); nextv=6; R=[]; B=[]
    for (u,v),word in zip(K33_EDGES,words):
        last=u
        for col in word:
            w=nextv; nextv+=1; G.add_edge(last,w); last=w
            (R if col=='R' else B).append(w)
        G.add_edge(last,v)
    return G,nextv,R,B


def build_x1_connected(words):
    G,nxt,R,B=subdivided_k33(words); assert nxt==12
    a,b=12,13; G.add_nodes_from((a,b)); G.add_edge(a,b)
    G.add_edges_from((a,x) for x in R); G.add_edges_from((b,x) for x in B)
    assert target_ok(G)
    return G


def build_x1_c4(words):
    G,nxt,R,B=subdivided_k33(words); assert nxt==8
    cyc=(8,9,10,11)
    for i,x in enumerate(cyc):
        (R if i%2==0 else B).append(x); G.add_edge(x,cyc[(i+1)%4])
    a,b=12,13; G.add_nodes_from((a,b)); G.add_edge(a,b)
    G.add_edges_from((a,x) for x in R); G.add_edges_from((b,x) for x in B)
    assert target_ok(G)
    return G


def build_x1_c6():
    G=nx.complete_bipartite_graph(3,3); cyc=(6,7,8,9,10,11); R=[];B=[]
    for i,x in enumerate(cyc):
        (R if i%2==0 else B).append(x); G.add_edge(x,cyc[(i+1)%6])
    a,b=12,13; G.add_nodes_from((a,b)); G.add_edge(a,b)
    G.add_edges_from((a,x) for x in R); G.add_edges_from((b,x) for x in B)
    assert target_ok(G)
    return G


def build_x0_t3(words):
    G,nxt,R,B=subdivided_k33(words); assert nxt==8
    center=8; commons=(9,10,11); G.add_node(center)
    G.add_edges_from((center,c) for c in commons)
    a,b=12,13; G.add_nodes_from((a,b))
    G.add_edges_from((a,x) for x in R); G.add_edges_from((b,x) for x in B)
    for c in commons: G.add_edge(a,c); G.add_edge(b,c)
    assert target_ok(G)
    return G


def build_x0_t4_double_star():
    G=nx.complete_bipartite_graph(3,3); p,q=6,7; leaves=(8,9,10,11)
    G.add_edge(p,q)
    for x in leaves[:2]: G.add_edge(p,x)
    for x in leaves[2:]: G.add_edge(q,x)
    a,b=12,13; G.add_nodes_from((a,b))
    for x in leaves: G.add_edge(a,x); G.add_edge(b,x)
    assert target_ok(G)
    return G


def build_x0_t4_internal():
    G=nx.complete_bipartite_graph(3,3); u,v=0,3; G.remove_edge(u,v)
    p=6; leaf=7; q=8; leaves=(9,10,11)
    G.add_edges_from(((u,p),(p,v),(p,leaf)))
    G.add_edges_from((q,x) for x in leaves)
    a,b=12,13; G.add_nodes_from((a,b))
    for x in (leaf,)+leaves: G.add_edge(a,x); G.add_edge(b,x)
    assert target_ok(G)
    return G


def dedup(graphs):
    reps=[]
    for G in graphs:
        if not any(nx.is_isomorphic(G,H) for H in reps): reps.append(G.copy())
    return reps


def split_degree4(G,v,pair):
    nbr=set(G.neighbors(v)); A=set(pair); B=nbr-A
    assert len(A)==len(B)==2
    H=G.copy(); H.remove_node(v); x=max(G.nodes())+1; y=x+1
    H.add_nodes_from((x,y)); H.add_edge(x,y)
    H.add_edges_from((x,u) for u in A); H.add_edges_from((y,u) for u in B)
    return nx.convert_node_labels_to_integers(H)


def main():
    print('TFIK22 (2,12) exact structural core')

    A11=word_assignments(1,1); assert len(A11)==90
    t3=[build_x0_t3(w) for w in A11]
    assert all(is_2apex(G)[0] for G in t3)
    t3reps=dedup(t3)
    print('X0_T3_RAW',len(t3),'ISO_CLASSES',len(t3reps),'ALL_2APEX',True)
    assert len(t3reps)==3
    for i,G in enumerate(t3reps,1): print(' X0_T3_CLASS',i,'WITNESS',is_2apex(G)[1])

    t4=[build_x0_t4_double_star(),build_x0_t4_internal()]
    assert all(is_2apex(G)[0] for G in t4)
    print('X0_T4_FORMS',len(t4),'ALL_2APEX',True,
          'WITNESSES',tuple(is_2apex(G)[1] for G in t4))

    A33=word_assignments(3,3); assert len(A33)==22530
    non2=[]; non2raw=0; two=0
    for w in A33:
        G=build_x1_connected(w); ok,_=is_2apex(G)
        if ok: two+=1
        else:
            non2raw+=1
            if not any(nx.is_isomorphic(G,H) for H in non2): non2.append(G.copy())
    print('X1_CONNECTED_WORDS',len(A33),'TWO_APEX',two,'NON2_RAW',non2raw,'NON2_ISO',len(non2))
    assert (two,non2raw,len(non2))==(22470,60,3)

    c4=[build_x1_c4(w) for w in A11]
    assert all(is_2apex(G)[0] for G in c4)
    c4reps=dedup(c4); c6=build_x1_c6(); assert is_2apex(c6)[0]
    print('X1_C4_RAW',len(c4),'ISO_CLASSES',len(c4reps),'ALL_2APEX',True)
    print('X1_C6_ALL_2APEX',True,'WITNESS',is_2apex(c6)[1])

    k7dy,k7par=closure(k7(),False); assert len(k7dy)==14
    H13=[G for G in k7dy if G.number_of_nodes()==13]; C14=[G for G in k7dy if G.number_of_nodes()==14]
    assert len(H13)==len(C14)==1
    H13,C14=H13[0],C14[0]
    assert Counter(dict(H13.degree()).values())==Counter({3:10,4:3})
    assert triangles(H13)==1 and Counter(dict(C14.degree()).values())==Counter({3:14}) and triangles(C14)==0

    c14plus=[]
    for u,v in itertools.combinations(C14.nodes(),2):
        if C14.has_edge(u,v): continue
        G=C14.copy(); G.add_edge(u,v)
        if target_ok(G) and not any(nx.is_isomorphic(G,H) for H in c14plus): c14plus.append(G)
    assert len(c14plus)==1

    h13split=[]; splitcert=[]
    for v,d in H13.degree():
        if d!=4: continue
        N=sorted(H13.neighbors(v))
        for pair in itertools.combinations(N,2):
            if N[0] not in pair: continue
            G=split_degree4(H13,v,pair)
            if target_ok(G):
                if not any(nx.is_isomorphic(G,H) for H in h13split): h13split.append(G)
                splitcert.append((v,pair))
    assert len(h13split)==1

    kfam,kpar=closure(k3311(),True); assert len(kfam)==58
    k14=[G for G in kfam if G.number_of_nodes()==14]
    assert len(k14)==1 and target_ok(k14[0])

    positives=(c14plus[0],h13split[0],k14[0])
    assert all(not nx.is_isomorphic(positives[i],positives[j]) for i in range(3) for j in range(i))
    match=[]
    for G in non2:
        row=tuple(nx.is_isomorphic(G,P) for P in positives); assert sum(row)==1; match.append(row)
    assert all(any(nx.is_isomorphic(P,G) for G in non2) for P in positives)
    print('POSITIVE_MATCH_MATRIX',tuple(match))
    print('K7_PURE_DY_SIZE',len(k7dy),'K3311_FULL_FAMILY_SIZE',len(kfam))
    print('H13_VALID_SPLIT_RAW_CERTS',tuple(splitcert))

    names=('C14_PLUS_EDGE','H13_VERTEX_SPLIT','K3311_UNIQUE_ORDER14')
    for name,G in zip(names,positives):
        hi=tuple(v for v,d in G.degree() if d==4)
        print(name,'D4',hi,'D4_ADJACENT',G.has_edge(*hi),
              'GRAPH6',nx.to_graph6_bytes(G,header=False).decode().strip())
        print(name,'EDGES',tuple(sorted(tuple(sorted(e)) for e in G.edges())))

    print('FINAL_PROFILE_IK_ISO_CLASSES',3)
    print('ALL_EXACT_TFIK22_2_12_CHECKS_PASS')

if __name__=='__main__': main()
