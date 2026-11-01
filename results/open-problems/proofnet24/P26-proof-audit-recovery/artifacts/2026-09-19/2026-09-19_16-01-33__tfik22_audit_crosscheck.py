#!/usr/bin/env python3
from __future__ import annotations
import itertools
from collections import Counter, deque, defaultdict
import networkx as nx

# P26 independent exact audit cross-check for R01 TFIK22 package.
# All finite checks combinatorial; nx.check_planarity and graph isomorphism are exact algorithms.

def tri(G): return sum(nx.triangles(G).values())//3

def two_apex(G):
    V=sorted(G.nodes())
    if nx.check_planarity(G)[0]: return ()
    for u in V:
        H=G.copy(); H.remove_node(u)
        if nx.check_planarity(H)[0]: return (u,)
    for u,v in itertools.combinations(V,2):
        H=G.copy(); H.remove_nodes_from((u,v))
        if nx.check_planarity(H)[0]: return (u,v)
    return None

def graph(E,n):
    G=nx.Graph(); G.add_nodes_from(range(n)); G.add_edges_from(E); return G

def contract(G,e):
    H=nx.contracted_nodes(G,e[0],e[1],self_loops=False,copy=True)
    return nx.convert_node_labels_to_integers(nx.Graph(H))

# Basic source arithmetic.
sol=[]
for a in range(12):
    for b in range(15):
        if 4*a+3*b==44: sol.append((a,b))
assert sol==[(2,12),(5,8),(8,4),(11,0)]

# (11,0) quartic-profile representatives from Mattman-Pierce.
E1=[(0,5),(0,8),(0,9),(0,10),(1,5),(1,8),(1,9),(1,10),(2,6),(2,7),(2,8),(2,9),(3,6),(3,7),(3,8),(3,10),(4,6),(4,7),(4,9),(4,10),(5,6),(5,7)]
E2=[(0,4),(0,5),(0,6),(0,7),(1,5),(1,6),(1,7),(1,8),(2,6),(2,7),(2,8),(2,9),(3,7),(3,8),(3,9),(3,10),(4,8),(4,9),(4,10),(5,9),(5,10),(6,10)]
Q=[graph(E1,11),graph(E2,11)]
for G in Q:
    assert G.number_of_edges()==22 and set(dict(G.degree()).values())=={4} and tri(G)==0 and nx.is_connected(G)
    assert two_apex(G) is None
assert not nx.is_isomorphic(*Q)

# Family generation for positive certificates.
def sig(G): return (G.number_of_nodes(),G.number_of_edges(),tuple(sorted(dict(G.degree()).values())),tri(G))
def idx_iso(fam,G):
    s=sig(G)
    for i,H in enumerate(fam):
        if sig(H)==s and nx.is_isomorphic(H,G): return i
    return None

def dy_moves(G):
    V=sorted(G.nodes())
    for a,b,c in itertools.combinations(V,3):
        if all(G.has_edge(*e) for e in ((a,b),(a,c),(b,c))):
            H=G.copy(); H.remove_edges_from(((a,b),(a,c),(b,c)))
            w=max(H.nodes(),default=-1)+1; H.add_node(w); H.add_edges_from(((w,a),(w,b),(w,c)))
            yield nx.convert_node_labels_to_integers(H)
def yd_moves(G):
    for v in sorted(G.nodes()):
        if G.degree(v)!=3: continue
        N=tuple(sorted(G.neighbors(v)))
        if any(G.has_edge(x,y) for x,y in itertools.combinations(N,2)): continue
        H=G.copy(); H.remove_node(v); H.add_edges_from(itertools.combinations(N,2))
        yield nx.convert_node_labels_to_integers(H)
def closure(base,full):
    fam=[base]; q=deque([0])
    while q:
        G=fam[q.popleft()]
        it=dy_moves(G)
        if full: it=itertools.chain(it,yd_moves(G))
        for H in it:
            if idx_iso(fam,H) is None:
                fam.append(H); q.append(len(fam)-1)
    return fam
K7=nx.complete_graph(7)
K7dy=closure(K7,False)
assert len(K7dy)==14 and all(H.number_of_edges()==21 for H in K7dy)
parts=((0,1,2),(3,4,5),(6,),(7,))
K3311=nx.Graph(); K3311.add_nodes_from(range(8))
for i in range(4):
    for j in range(i+1,4):
        K3311.add_edges_from((u,v) for u in parts[i] for v in parts[j])
Kfam=closure(K3311,True)
assert len(Kfam)==58 and all(H.number_of_edges()==22 for H in Kfam)
assert Counter(H.number_of_nodes() for H in Kfam)==Counter({8:1,9:4,10:11,11:21,12:15,13:5,14:1})

# (5,8): independently cross-check all four surviving classes and their positive certificates.
C58_EDGES=(
((0,1),(0,4),(0,5),(0,10),(1,2),(1,6),(1,12),(2,3),(2,7),(2,11),(3,8),(3,10),(3,12),(4,9),(4,11),(4,12),(5,8),(5,11),(6,8),(6,9),(7,9),(7,10)),
((0,1),(0,4),(0,8),(0,9),(1,2),(1,7),(1,12),(2,3),(2,8),(2,10),(3,9),(3,11),(3,12),(4,10),(4,11),(4,12),(5,7),(5,8),(5,11),(6,7),(6,9),(6,10)),
((0,1),(0,4),(0,9),(0,10),(1,2),(1,6),(1,12),(2,3),(2,9),(2,11),(3,7),(3,10),(3,12),(4,8),(4,11),(4,12),(5,6),(5,10),(5,11),(6,8),(7,8),(7,9)),
((0,1),(0,4),(0,7),(0,9),(1,2),(1,10),(1,11),(2,3),(2,8),(2,12),(3,4),(3,9),(3,10),(4,11),(4,12),(5,6),(5,8),(5,11),(6,7),(6,10),(7,12),(8,9)))
C58=[graph(E,13) for E in C58_EDGES]
for G in C58:
    assert G.number_of_edges()==22 and tri(G)==0 and Counter(dict(G.degree()).values())==Counter({4:5,3:8})
    assert two_apex(G) is None
assert all(not nx.is_isomorphic(C58[i],C58[j]) for i in range(4) for j in range(i))
pos58_family=sum(idx_iso(Kfam,G) is not None for G in C58)
pos58_k7minor=0
for G in C58:
    if idx_iso(Kfam,G) is not None: continue
    found=False
    for e in list(G.edges()):
        M=contract(G,e)
        if M.number_of_edges()==21 and idx_iso(K7dy,M) is not None:
            found=True; break
    if found: pos58_k7minor+=1
assert (pos58_family,pos58_k7minor)==(2,2)

# (2,12): direct structural quotient for the largest case plus all small exceptional cases.
PERMS=tuple(itertools.permutations(range(3))); EDGES=tuple((i,j) for i in range(3) for j in range(3)); EIDX={e:k for k,e in enumerate(EDGES)}
def alt(k,s):
    t='B' if s=='R' else 'R'; return ''.join(s if i%2==0 else t for i in range(k))
WORDS=['']
for k in range(1,7): WORDS.extend([alt(k,'R'),alt(k,'B')])
WORDS=tuple(dict.fromkeys(WORDS))
def assigns(rtot,btot):
    out=[]
    def rec(i,r,b,cur):
        if i==9:
            if (r,b)==(rtot,btot): out.append(tuple(cur))
            return
        for w in WORDS:
            rr=w.count('R'); bb=w.count('B')
            if r+rr<=rtot and b+bb<=btot:
                cur.append(w); rec(i+1,r+rr,b+bb,cur); cur.pop()
    rec(0,0,0,[]); return out
A11=assigns(1,1); A33=assigns(3,3); assert len(A11)==90 and len(A33)==22530
GROUP=tuple((p,q,s,c) for p in PERMS for q in PERMS for s in (0,1) for c in (0,1)); assert len(GROUP)==144
def trans(X,p,q,swap_side,swap_col):
    out=['']*9; tr=str.maketrans('RB','BR')
    for k,(i,j) in enumerate(EDGES):
        w=X[k]
        if swap_side: e=(q[j],p[i]); w=w[::-1]
        else: e=(p[i],q[j])
        if swap_col: w=w.translate(tr)
        out[EIDX[e]]=w
    return tuple(out)
def canon(X): return min(trans(X,*g) for g in GROUP)
def subK33(words):
    G=nx.Graph(); G.add_nodes_from(range(6)); nxt=6; R=[];B=[]
    for (i,j),w in zip(EDGES,words):
        last=i
        for ch in w:
            z=nxt; nxt+=1; G.add_edge(last,z); last=z; (R if ch=='R' else B).append(z)
        G.add_edge(last,3+j)
    return G,nxt,R,B
def build212_conn(words):
    G,nxt,R,B=subK33(words); assert nxt==12 and len(R)==len(B)==3
    G.add_edge(12,13); G.add_edges_from((12,z) for z in R); G.add_edges_from((13,z) for z in B)
    return G
buckets=defaultdict(list)
for X in A33: buckets[canon(X)].append(X)
assert len(buckets)==199 and Counter(map(len,buckets.values()))==Counter({144:124,72:59,36:9,18:3,12:4})
non2orbits=[]
for rep,orb in buckets.items():
    G=build212_conn(rep)
    if two_apex(G) is None: non2orbits.append((rep,len(orb),G))
assert len(non2orbits)==3 and sorted(s for _,s,_ in non2orbits)==[12,12,36]

def build_t3(words):
    G,nxt,R,B=subK33(words); assert nxt==8
    G.add_node(8); common=(9,10,11); G.add_edges_from((8,c) for c in common)
    for c in common: G.add_edge(12,c); G.add_edge(13,c)
    G.add_edges_from((12,z) for z in R); G.add_edges_from((13,z) for z in B)
    return G
def build_c4(words):
    G,nxt,R,B=subK33(words); assert nxt==8
    cyc=(8,9,10,11)
    for i,z in enumerate(cyc):
        (R if i%2==0 else B).append(z); G.add_edge(z,cyc[(i+1)%4])
    G.add_edge(12,13); G.add_edges_from((12,z) for z in R); G.add_edges_from((13,z) for z in B)
    return G
assert all(two_apex(build_t3(x)) is not None for x in A11)
assert all(two_apex(build_c4(x)) is not None for x in A11)
# t=4 two forms.
G=nx.complete_bipartite_graph(3,3); G.add_edge(6,7)
for z in (8,9): G.add_edge(6,z)
for z in (10,11): G.add_edge(7,z)
for z in (8,9,10,11): G.add_edge(12,z); G.add_edge(13,z)
assert two_apex(G) is not None
G=nx.complete_bipartite_graph(3,3); G.remove_edge(0,3); G.add_edges_from(((0,6),(6,3),(6,7),(8,9),(8,10),(8,11)))
for z in (7,9,10,11): G.add_edge(12,z); G.add_edge(13,z)
assert two_apex(G) is not None
# C6 form.
G=nx.complete_bipartite_graph(3,3); cyc=(6,7,8,9,10,11)
for i,z in enumerate(cyc): G.add_edge(z,cyc[(i+1)%6])
G.add_edge(12,13)
for z in cyc[::2]: G.add_edge(12,z)
for z in cyc[1::2]: G.add_edge(13,z)
assert two_apex(G) is not None

# Positive certificates for the three non-2-apex connected orbits.
C14s=[H for H in K7dy if H.number_of_nodes()==14]; H13s=[H for H in K7dy if H.number_of_nodes()==13]
assert len(C14s)==len(H13s)==1
C14=C14s[0]; H13=H13s[0]
def target212(G): return G.number_of_nodes()==14 and G.number_of_edges()==22 and tri(G)==0 and Counter(dict(G.degree()).values())==Counter({3:12,4:2})
certs=[]
for u,v in itertools.combinations(C14.nodes(),2):
    if not C14.has_edge(u,v):
        H=C14.copy(); H.add_edge(u,v)
        if target212(H) and not any(nx.is_isomorphic(H,X) for X in certs): certs.append(H)
for v,d in list(H13.degree()):
    if d!=4: continue
    N=sorted(H13.neighbors(v))
    for pair in itertools.combinations(N,2):
        if N[0] not in pair: continue
        Aset=set(pair); Bset=set(N)-Aset
        H=H13.copy(); H.remove_node(v); x=max(H13.nodes())+1; y=x+1
        H.add_edge(x,y); H.add_edges_from((x,z) for z in Aset); H.add_edges_from((y,z) for z in Bset)
        H=nx.convert_node_labels_to_integers(H)
        if target212(H) and not any(nx.is_isomorphic(H,X) for X in certs): certs.append(H)
for H in Kfam:
    if H.number_of_nodes()==14 and target212(H) and not any(nx.is_isomorphic(H,X) for X in certs): certs.append(H)
assert len(certs)==3
for _,_,G in non2orbits:
    assert sum(nx.is_isomorphic(G,C) for C in certs)==1

print('networkx',nx.__version__)
print('degree_profiles',sol)
print('quartic_representatives',len(Q),'non2apex','yes','nonisomorphic','yes')
print('K7_pure_DY_size',len(K7dy))
print('K3311_family_size',len(Kfam),'order_distribution',tuple(sorted(Counter(H.number_of_nodes() for H in Kfam).items())))
print('profile_5_8_survivors_crosschecked',len(C58),'positive_family',pos58_family,'positive_K7minor',pos58_k7minor)
print('profile_2_12_connected_raw',len(A33),'structural_orbits',len(buckets),'non2_orbits',len(non2orbits),'raw_mass',sum(s for _,s,_ in non2orbits))
print('profile_2_12_positive_classes',len(certs))
print('P26_TFIK22_INDEPENDENT_EXACT_CORE_PASS')
