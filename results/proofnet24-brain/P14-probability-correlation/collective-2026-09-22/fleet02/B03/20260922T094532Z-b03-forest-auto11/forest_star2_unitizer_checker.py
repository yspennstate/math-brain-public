from itertools import combinations
from collections import Counter

def is_forest(n, edges, mask):
    parent=list(range(n))
    def find(x):
        while parent[x]!=x:
            parent[x]=parent[parent[x]]
            x=parent[x]
        return x
    for i,(u,v) in enumerate(edges):
        if not (mask>>i)&1:
            continue
        ru,rv=find(u),find(v)
        if ru==rv:
            return False
        parent[rv]=ru
    return True

def terminal_counts(n, edges, s=0, t=1):
    D=C=0
    for mask in range(1<<len(edges)):
        if not is_forest(n,edges,mask):
            continue
        parent=list(range(n))
        def find(x):
            while parent[x]!=x:
                parent[x]=parent[parent[x]]
                x=parent[x]
            return x
        def union(a,b):
            ra,rb=find(a),find(b)
            if ra!=rb: parent[rb]=ra
        for i,(u,v) in enumerate(edges):
            if (mask>>i)&1: union(u,v)
        if find(s)==find(t): C+=1
        else: D+=1
    return D,C

def triple_coeffs(n, edges, e, f, h):
    ie,jf,kh=edges.index(e),edges.index(f),edges.index(h)
    A=B=a0=a1=b0=b1=c0=c1=0
    for mask in range(1<<len(edges)):
        if not is_forest(n,edges,mask): continue
        xe=(mask>>ie)&1; xf=(mask>>jf)&1; xh=(mask>>kh)&1
        if xh: B+=1
        else: A+=1
        if xe:
            if xh:a1+=1
            else:a0+=1
        if xf:
            if xh:b1+=1
            else:b0+=1
        if xe and xf:
            if xh:c1+=1
            else:c0+=1
    D0=a0*b0-A*c0
    D1=a1*b1-B*c1
    M=a0*b1+a1*b0-A*c1-B*c0
    return (A,B,a0,a1,b0,b1,c0,c1,D0,D1,M)

# Exact response-2 gadget census on <=5 vertices, fixed terminals 0,1.
counts={}
witnesses={}
for n in range(2,6):
    E=list(combinations(range(n),2))
    hits=[]
    for gmask in range(1<<len(E)):
        edges=[E[i] for i in range(len(E)) if (gmask>>i)&1]
        D,C=terminal_counts(n,edges)
        if C==2*D:
            hits.append((edges,D,C))
    counts[n]=len(hits)
    witnesses[n]=hits
assert counts=={2:0,3:0,4:0,5:1}
gadget_edges=[(0,1),(0,2),(0,3),(0,4),(1,2),(1,3),(1,4)]
assert witnesses[5]==[(gadget_edges,27,54)]

# Edge-minimality: any connected terminal component with <=6 edges has <=7 vertices.
# Adding isolates embeds it in K7, so exhaustive fixed-terminal scan of all
# K7 subgraphs with <=6 edges certifies no response-2 simple unit network exists.
E7=list(combinations(range(7),2))
scanned=0
for m in range(7):
    for idxs in combinations(range(len(E7)),m):
        edges=[E7[i] for i in idxs]
        D,C=terminal_counts(7,edges)
        scanned+=1
        assert C!=2*D
assert scanned==82160

# Overlapping-cycle core: q(w)=158-14 w+4 w^2.
core=[(0,1),(0,2),(0,3),(0,4),(1,2),(1,3),(1,4),(2,3),(2,4)]
e=(0,3); f=(1,4); h=(0,1)
vals=triple_coeffs(5,core,e,f,h)
assert vals==(134,64,52,18,52,18,19,5,158,4,-14)
D0,D1,M=vals[-3:]
q1=D0+M+D1
q2=D0+2*M+4*D1
assert (q1,q2)==(148,146)
assert q2==2*q1-D0+2*D1

# Source-simple triangle lift: split endpoint 0 into 0 and 5, contract g=(0,5).
parent=[(0,5),(0,1),(5,1),(0,2),(0,3),(0,4),(1,2),(1,3),(1,4),(2,3),(2,4)]
pvals=triple_coeffs(6,parent,(0,3),(1,4),(0,5))
assert pvals[-3:]==(592,146,580)
assert pvals[-2]==q2
parent_gap=sum(pvals[-3:])
assert parent_gap==1318

print("response2_counts_n2_to_n5", counts)
print("unique_n5_response2_edges", gadget_edges)
print("unique_n5_response2_D_C", (27,54))
print("scanned_K7_subgraphs_m_le_6", scanned)
print("response2_with_m_le_6", 0)
print("core_coefficients_A_B_a0_a1_b0_b1_c0_c1_D0_D1_M", vals)
print("core_q1_q2", (q1,q2))
print("parent_triangle_conditional_gap_q2", pvals[-2])
print("parent_unit_gap", parent_gap)
print("STATUS=PASS")
