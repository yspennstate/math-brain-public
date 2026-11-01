#!/usr/bin/env python3
from itertools import combinations

def is_forest(n, edges, mask):
    parent=list(range(n))
    rank=[0]*n
    def find(x):
        while parent[x]!=x:
            parent[x]=parent[parent[x]]
            x=parent[x]
        return x
    def union(a,b):
        ra,rb=find(a),find(b)
        if ra==rb:
            return False
        if rank[ra]<rank[rb]:
            ra,rb=rb,ra
        parent[rb]=ra
        if rank[ra]==rank[rb]:
            rank[ra]+=1
        return True
    for i,(u,v) in enumerate(edges):
        if (mask>>i)&1 and not union(u,v):
            return False
    return True

def forest_masks(n, edges):
    return [m for m in range(1<<len(edges)) if is_forest(n,edges,m)]

def affine_counts(masks,e,f,g):
    out={}
    for name,req in (("Z",()),("e",(e,)),("f",(f,)),("ef",(e,f))):
        c=[0,0]
        for mask in masks:
            if all((mask>>r)&1 for r in req):
                c[(mask>>g)&1]+=1
        out[name]=c
    return out

def delta_coeffs(v):
    A,B=v["Z"]; C,D=v["e"]; E,F=v["f"]; G,H=v["ef"]
    c=C*E-A*G
    b=C*F+D*E-A*H-B*G
    a=D*F-B*H
    return c,b,a

def all_weight_safe(c,b,a):
    if c<0 or a<0:
        return False
    if a==0:
        return b>=0
    if b>=0:
        return True
    return b*b<=4*a*c

graphs=0
instances=0
negative_middle=0
weighted_failures=0
identity_failures=0
first=None

for n in range(2,6):
    complete=list(combinations(range(n),2))
    for gm in range(1<<len(complete)):
        graphs+=1
        edges=[complete[i] for i in range(len(complete)) if (gm>>i)&1]
        m=len(edges)
        if m<3:
            continue
        masks=forest_masks(n,edges)
        for e in range(m):
            for f in range(e+1,m):
                for g in range(m):
                    if g==e or g==f:
                        continue
                    instances+=1
                    v=affine_counts(masks,e,f,g)
                    c,b,a=delta_coeffs(v)
                    A,B=v["Z"]; C,D=v["e"]; E,F=v["f"]
                    p=B*C-A*D
                    q=B*E-A*F
                    if A*B*b != B*B*c + A*A*a - p*q:
                        identity_failures+=1
                    if b<0:
                        negative_middle+=1
                        if first is None:
                            first=(n,edges,e,f,g,(c,b,a),v,p,q)
                    if not all_weight_safe(c,b,a):
                        weighted_failures+=1

assert graphs==1098
assert instances==46563
assert identity_failures==0
assert weighted_failures==0
assert negative_middle==540

n,edges,e,f,g,coef,v,p,q=first
assert n==5
assert edges==[(0,2),(0,3),(0,4),(1,2),(1,3),(1,4),(2,3)]
assert (e,f,g)==(0,4,6)
assert coef==(36,-2,4)
assert v=={"Z":[54,32],"e":[24,10],"f":[24,10],"ef":[10,3]}
assert p==q==228

# True contraction by g preserves edge identities and creates parallel pairs.
contracted=[(0,2),(0,2),(0,3),(1,2),(1,2),(1,3)]
cm=forest_masks(4,contracted)
def marked_counts(masks,e,f=None):
    z=len(masks)
    ze=sum((m>>e)&1 for m in masks)
    if f is None:
        return z,ze
    zf=sum((m>>f)&1 for m in masks)
    zef=sum(((m>>e)&1) and ((m>>f)&1) for m in masks)
    return z,ze,zf,zef
true_counts=marked_counts(cm,0,4)
assert true_counts==(32,10,10,3)

# False simplification merges each marked+unmarked parallel pair to one unit edge.
collapsed=[(0,2),(0,3),(1,2),(1,3)]
sm=forest_masks(4,collapsed)
naive_counts=marked_counts(sm,0,2)
assert naive_counts==(15,7,7,3)

A,C=54,24
B_true,D_true=32,10
B_naive,D_naive=15,7
p_true=B_true*C-A*D_true
p_naive=B_naive*C-A*D_naive
assert (p_true,p_naive)==(228,-18)

print("FOREST single-boundary-weight exact checker")
print("labelled_simple_graphs_n2_to_n5 =",graphs)
print("marked_(e,f,g)_instances =",instances)
print("quadratic_identity_failures =",identity_failures)
print("all_positive_weight_failures =",weighted_failures)
print("negative_middle_coeff_instances =",negative_middle)
print("first_negative_middle_graph_edges =",edges)
print("marks e,f,g =",edges[e],edges[f],edges[g])
print("affine_counts Z,Ze,Zf,Zef =",v)
print("Rayleigh_polynomial =",f"{coef[2]}*w^2 {coef[1]:+d}*w {coef[0]:+d}")
print("completed_square = 4*(w-1/4)^2 + 143/4")
print("true_contraction_counts Z,Ze,Zf,Zef =",true_counts)
print("naive_simple_collapse_counts =",naive_counts)
print("Delta(g,e): true_contraction =",p_true,"naive_collapse =",p_naive)
print("status = PASS (finite regression only; no parent closure)")
