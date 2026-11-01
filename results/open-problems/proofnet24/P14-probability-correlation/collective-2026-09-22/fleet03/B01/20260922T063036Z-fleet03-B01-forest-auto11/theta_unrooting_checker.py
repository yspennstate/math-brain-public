from fractions import Fraction
from itertools import combinations

def is_forest(n, edges, mask):
    p=list(range(n))
    def find(x):
        while p[x]!=x:
            p[x]=p[p[x]]
            x=p[x]
        return x
    for i,(u,v) in enumerate(edges):
        if (mask>>i)&1:
            a,b=find(u),find(v)
            if a==b:
                return False
            p[a]=b
    return True

def forest_counts(n, edges, weights, e, f):
    Z=Ze=Zf=Zef=0
    for mask in range(1<<len(edges)):
        if not is_forest(n, edges, mask):
            continue
        w=1
        for i,a in enumerate(weights):
            if (mask>>i)&1:
                w*=a
        xe=(mask>>e)&1
        xf=(mask>>f)&1
        Z+=w; Ze+=w*xe; Zf+=w*xf; Zef+=w*xe*xf
    return Z,Ze,Zf,Zef,Ze*Zf-Z*Zef

for L in range(2,9):
    M=2**L-1
    k=2*M
    q0=Fraction(2**(L-1)-1,M)
    delta=Fraction(2**(L-2),M*M)
    dilution=Fraction(k*L)*delta*delta
    assert Fraction(k,M)==2
    assert delta == (1-q0)/k
    print("theta",L,"paths",k,"effective",Fraction(k,M),
          "q0",q0,"delta",delta,"sum_delta2",dilution)

L=2; M=3; k=6
theta_edges=[]
for z in range(2,2+k):
    theta_edges += [(0,z),(z,1)]
A=B=0
for mask in range(1<<len(theta_edges)):
    if not is_forest(2+k,theta_edges,mask):
        continue
    p=list(range(2+k))
    def find(x):
        while p[x]!=x:
            p[x]=p[p[x]]
            x=p[x]
        return x
    for i,(u,v) in enumerate(theta_edges):
        if (mask>>i)&1:
            a,b=find(u),find(v); p[a]=b
    if find(0)==find(1): B+=1
    else: A+=1
assert (A,B)==(729,1458)
print("K2,6 disconnected",A,"connected",B,"ratio",Fraction(B,A))

sk=list(combinations(range(4),2))
d=sk.index((0,1)); e=sk.index((0,2)); f=sk.index((1,3))
weights=[1]*len(sk); weights[d]=2
cw=forest_counts(4,sk,weights,e,f)
print("weighted_K4",cw)

exp=[ed for ed in sk if ed!=(0,1)]
for z in range(4,10):
    exp += [(0,z),(z,1)]
ee=exp.index((0,2)); ff=exp.index((1,3))
ce=forest_counts(10,exp,[1]*len(exp),ee,ff)
print("expanded_K4",ce)
assert ce[0] == A*cw[0]
assert ce[1] == A*cw[1]
assert ce[2] == A*cw[2]
assert ce[3] == A*cw[3]
assert ce[4] == A*A*cw[4]
print("gap_scale",ce[4]//cw[4],"expected",A*A)
print("ALL_EXACT_ASSERTIONS_PASSED")
