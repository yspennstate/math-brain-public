#!/usr/bin/env python3
from itertools import combinations

def forests(n, edges):
    for mask in range(1 << len(edges)):
        parent=list(range(n))
        def find(x):
            while parent[x]!=x:
                parent[x]=parent[parent[x]]
                x=parent[x]
            return x
        ok=True
        for i,(u,v) in enumerate(edges):
            if (mask>>i)&1:
                ru,rv=find(u),find(v)
                if ru==rv:
                    ok=False
                    break
                parent[ru]=rv
        if ok:
            yield mask,[find(i) for i in range(n)]

G=[(0,2),(0,3),(0,4),(1,2),(1,3),(1,4),(2,3)]
e=(0,2); f=(1,3); g=(2,3)
H=[h for h in G if h not in (e,f)]
gi=H.index(g)
C={name:[0,0] for name in ("A","B","C","D","Q")}
for mask,roots in forests(5,H):
    ae=roots[e[0]]!=roots[e[1]]
    af=roots[f[0]]!=roots[f[1]]
    ce=tuple(sorted((roots[e[0]],roots[e[1]])))
    cf=tuple(sorted((roots[f[0]],roots[f[1]])))
    jointly=ae and af and ce!=cf
    reconnect=ae and af and not jointly
    bit=(mask>>gi)&1
    C["A"][bit]+=1
    C["B"][bit]+=ae
    C["C"][bit]+=af
    C["D"][bit]+=jointly
    C["Q"][bit]+=reconnect

def mul(p,q):
    return [p[0]*q[0], p[0]*q[1]+p[1]*q[0], p[1]*q[1]]
def sub(p,q):
    return [a-b for a,b in zip(p,q)]

Delta=sub(mul(C["B"],C["C"]),mul(C["A"],C["D"]))
qA=mul(C["Q"],C["A"])
cov_num=sub(qA,Delta)

print("BOUNDARY_COEFFICIENTS",C)
print("DELTA_COEFFICIENTS",Delta)
print("RECONNECTION_TIMES_A_COEFFICIENTS",qA)
print("COVARIANCE_NUMERATOR_COEFFICIENTS",cov_num)
print("IDENTITY_COEFFICIENTS",sub(qA,cov_num))
assert C=={"A":[16,15],"B":[14,7],"C":[14,7],"D":[10,3],"Q":[3,1]}
assert Delta==[36,-2,4]
assert qA==[48,61,15]
assert cov_num==[12,63,11]
assert sub(qA,cov_num)==Delta
assert (-2)**2-4*4*36==-572
print("DELTA(w)=36-2*w+4*w^2; discriminant=-572; positive for all real w")
print("q(w)=(3+w)/(16+15*w)")
print("Cov(A_e,A_f)=(12+63*w+11*w^2)/(16+15*w)^2")
print("STATUS=PARTNER_WITNESS_RECONNECTION_IDENTITY_PASS")
