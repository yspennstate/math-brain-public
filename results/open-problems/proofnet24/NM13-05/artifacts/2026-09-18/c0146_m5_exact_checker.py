#!/usr/bin/env python3
from itertools import combinations
from collections import defaultdict, Counter

# Exact finite certificate for NM13-05 / C0146.
# No floating point is used.

def comps(n, edges, mask):
    p=list(range(n))
    def find(x):
        while p[x]!=x:
            p[x]=p[p[x]]
            x=p[x]
        return x
    for i,(u,v) in enumerate(edges):
        if (mask>>i)&1:
            a,b=find(u),find(v)
            if a!=b:
                p[b]=a
    return len({find(i) for i in range(n)})

def is_connected(n, edges):
    if n==0: return True
    return comps(n, edges, (1<<len(edges))-1)==1

def is_2connected(n, edges):
    if n < 3 or not is_connected(n, edges):
        return False
    for z in range(n):
        relabel={}
        j=0
        for v in range(n):
            if v!=z:
                relabel[v]=j; j+=1
        ee=[(relabel[u],relabel[v]) for u,v in edges if u!=z and v!=z]
        if comps(n-1, ee, (1<<len(ee))-1)!=1:
            return False
    return True

def is_cycle(n, edges):
    deg=[0]*n
    for u,v in edges:
        deg[u]+=1; deg[v]+=1
    return len(edges)==n and all(d==2 for d in deg) and is_connected(n,edges)

def is_diamond(n, edges):
    if n!=4 or len(edges)!=5: return False
    deg=sorted(sum(1 for e in edges if v in e) for v in range(n))
    return deg==[2,2,3,3] and is_connected(n,edges)

# Classification core: every 2-connected simple graph with <=5 edges is
# a cycle or the diamond K4-e.
count_2conn=0
for n in range(3,6):
    E=list(combinations(range(n),2))
    for m in range(1,min(5,len(E))+1):
        for es in combinations(E,m):
            if is_2connected(n,list(es)):
                count_2conn += 1
                assert is_cycle(n,list(es)) or is_diamond(n,list(es)), (n,es)

# Diamond: edge 0 is shared by two triangles 0,1,2 and 0,3,4.
n=4
edges=[(0,1),(0,2),(1,2),(0,3),(1,3)]
M=5
layers={r:[a for a in range(1<<M) if a.bit_count()==r] for r in range(M+1)}
kc={a:comps(n,edges,a) for a in range(1<<M)}
assert Counter(kc[a] for a in layers[0]) == Counter({4:1})
assert Counter(kc[a] for a in layers[1]) == Counter({3:5})
assert Counter(kc[a] for a in layers[2]) == Counter({2:10})
assert Counter(kc[a] for a in layers[3]) == Counter({1:8,2:2})
assert Counter(kc[a] for a in layers[4]) == Counter({1:5})
assert Counter(kc[a] for a in layers[5]) == Counter({1:1})

# Endpoint integer flows for adjacent fixed-size layer transports.
# A pair key (a,b) means flow from mask a to mask b, always a subset b.
F23_0={
 (3,11):18,(3,19):6,(5,13):18,(5,21):6,(6,14):18,(6,22):6,
 (9,11):12,(9,13):12,(10,14):12,(10,26):12,(12,28):24,
 (17,19):24,(18,22):24,(20,21):24,(24,26):18,(24,28):6,
}
F23_1={
 (3,7):30,(5,13):30,(6,14):30,(9,11):30,(10,26):30,
 (12,28):30,(17,19):30,(18,22):30,(20,21):30,(24,25):30,
}
F34_0={
 (11,15):8,(11,27):2,(13,15):8,(13,29):2,(14,30):10,
 (19,23):6,(19,27):4,(21,23):6,(21,29):4,(22,23):4,
 (22,30):6,(26,27):10,(28,29):10,
}
F34_1={
 (7,15):10,(11,15):10,(13,29):10,(14,30):10,(19,23):10,
 (21,23):10,(22,30):10,(25,27):10,(26,27):10,(28,29):10,
}

def check_affine_flow(F0,F1,src,dst,row_const,row_q,col_rule):
    # F(q)=(1-q)F0+qF1 = F0 + q(F1-F0).
    keys=set(F0)|set(F1)
    row0=defaultdict(int); row1=defaultdict(int)
    col0=defaultdict(int); col1=defaultdict(int)
    for a,b in keys:
        assert a in src and b in dst and (a & b)==a
        x0=F0.get((a,b),0)
        x1=F1.get((a,b),0)
        # Convex interpolation is nonnegative for 0<=q<=1 because endpoints are.
        assert x0>=0 and x1>=0
        row0[a]+=x0; row1[a]+=x1-x0
        col0[b]+=x0; col1[b]+=x1-x0
    for a in src:
        c0,c1=row_const(a),row_q(a)
        assert (row0[a],row1[a])==(c0,c1),(a,row0[a],row1[a],c0,c1)
    for b in dst:
        c0,c1=col_rule(b)
        assert (col0[b],col1[b])==(c0,c1),(b,col0[b],col1[b],c0,c1)

# 2 -> 3. Common scale: source rows 24+6q.
# Target 3-sets: spanning trees (k=1) have column 30; the two triangles
# (k=2) have column 30q.
check_affine_flow(
    F23_0,F23_1,layers[2],layers[3],
    row_const=lambda a:24,row_q=lambda a:6,
    col_rule=lambda b:(30,0) if kc[b]==1 else (0,30),
)

# 3 -> 4. Source 3-set rows: tree 10, triangle 10q.
# Target 4-sets are uniform: columns 16+4q.
check_affine_flow(
    F34_0,F34_1,layers[3],layers[4],
    row_const=lambda a:10 if kc[a]==1 else 0,
    row_q=lambda a:0 if kc[a]==1 else 10,
    col_rule=lambda b:(16,4),
)

print("two_connected_simple_graphs_checked", count_2conn)
print("diamond_layer_counts", [len(layers[r]) for r in range(6)])
print("F23_endpoint_support_sizes", len(F23_0), len(F23_1))
print("F34_endpoint_support_sizes", len(F34_0), len(F34_1))
print("ALL_EXACT_CHECKS_PASS")
