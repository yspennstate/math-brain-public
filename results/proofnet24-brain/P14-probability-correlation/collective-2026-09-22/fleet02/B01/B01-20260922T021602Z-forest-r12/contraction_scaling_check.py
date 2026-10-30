#!/usr/bin/env python3
from itertools import combinations

def forest(n, edge_list):
    p=list(range(n))
    def find(x):
        while p[x]!=x:
            p[x]=p[p[x]]
            x=p[x]
        return x
    for u,v in edge_list:
        a,b=find(u),find(v)
        if a==b:
            return False
        p[b]=a
    return True

# G=K4. Contract g=01. Then 02/12 form a parallel class of size 2,
# 03/13 form another class of size 2, and 23 remains a singleton.
edges=[(0,1),(0,2),(1,2),(0,3),(1,3),(2,3)]
g,e,f=0,1,3
Z=Ze=Zf=Zef=0
for mask in range(1<<len(edges)):
    if not ((mask>>g)&1):
        continue
    chosen=[edges[i] for i in range(len(edges)) if (mask>>i)&1]
    if not forest(4,chosen):
        continue
    Z += 1
    ie=(mask>>e)&1
    jf=(mask>>f)&1
    Ze += ie
    Zf += jf
    Zef += ie*jf
specific_gap=Ze*Zf-Z*Zef

# Simplified contracted graph is a triangle with edge activities (2,2,1).
# Enumerate its weighted forests exactly.
tri=[(0,1),(0,2),(1,2)]
w=[2,2,1]
W=Wx=Wy=Wxy=0
for mask in range(1<<3):
    chosen=[tri[i] for i in range(3) if (mask>>i)&1]
    if not forest(3,chosen):
        continue
    weight=1
    for i in range(3):
        if (mask>>i)&1:
            weight*=w[i]
    W += weight
    Wx += weight*((mask>>0)&1)
    Wy += weight*((mask>>1)&1)
    Wxy += weight*((mask>>0)&1)*((mask>>1)&1)
class_gap=Wx*Wy-W*Wxy

print("K4_CONTRACTION_SPECIFIC_COPY_CHECK")
print("conditioned_specific_counts", Z, Ze, Zf, Zef, "gap", specific_gap)
print("weighted_class_counts", W, Wx, Wy, Wxy, "gap", class_gap)
print("parallel_class_sizes", 2, 2)
print("scaled_class_gap", class_gap//4)
assert (Z,Ze,Zf,Zef)==(14,4,4,1)
assert (W,Wx,Wy,Wxy)==(14,8,8,4)
assert class_gap==8 and specific_gap==2 and class_gap==4*specific_gap
print("PASS")
