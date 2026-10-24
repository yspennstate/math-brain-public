from fractions import Fraction
from itertools import combinations

def hermites(k, x):
    H=[1]
    if k>=1: H.append(x)
    for j in range(2,k+1):
        H.append(x*H[-1]-(j-1)*H[-2])
    return H

def c2(k):
    return Fraction(k*(k*k+9*k+27), (k+5)*(k*k+8*k+28))

def G(k,s):
    return (1-k)*s*s + (k*k+4*k-6)*s - k*k+k+6

def closed_G_c2(k):
    num=4*k**6+115*k**5+1499*k**4+10815*k**3+46297*k**2+111160*k+117600
    den=(k+5)**2*(k*k+8*k+28)**2
    return Fraction(num,den)

def is_forest(n, edges_subset):
    parent=list(range(n))
    def find(x):
        while parent[x]!=x:
            parent[x]=parent[parent[x]]
            x=parent[x]
        return x
    for u,v in edges_subset:
        a,b=find(u),find(v)
        if a==b: return False
        parent[a]=b
    return True

def brute(n):
    edges=list(combinations(range(n),2))
    e=(0,1)
    fadj=(0,2) if n>=3 else None
    fdis=(2,3) if n>=4 else None
    Z=E=Jadj=Jdis=0
    for mask in range(1<<len(edges)):
        chosen=[edges[i] for i in range(len(edges)) if mask>>i & 1]
        if not is_forest(n,chosen): continue
        Z+=1
        if e in chosen: E+=1
        if fadj and e in chosen and fadj in chosen: Jadj+=1
        if fdis and e in chosen and fdis in chosen: Jdis+=1
    return Z,E,Jadj,Jdis

expected = {
    3:(7,3,1,0),
    4:(38,14,4,5),
    5:(291,93,23,29),
    6:(2932,822,178,226),
}
for n,v in expected.items():
    assert brute(n)==v, (n, brute(n), v)

for n in range(6,501):
    k=n-4; x=k+5
    H=hermites(k,x)
    s=Fraction(k*H[k-1],H[k])
    C2=c2(k)
    assert s>=C2 and s<1
    assert G(k,s)>0
    assert G(k,C2)==closed_G_c2(k)
    assert closed_G_c2(k)>0

print("STATUS=PASS; brute K3..K6; C2/G exact n=6..500")
