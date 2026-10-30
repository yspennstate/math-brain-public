from fractions import Fraction
from itertools import combinations

def he_values(x, m):
    H=[1]
    if m==0: return H
    H.append(x)
    for j in range(1,m):
        H.append(x*H[j]-j*H[j-1])
    return H

def hermite_counts(n):
    x=n+1
    H=he_values(x,n)
    def D(j):
        return H[j] - (j*H[j-1] if j else 0)
    Z=D(n)
    E=D(n-2)
    Jadj=D(n-3) if n>=3 else None
    if n>=4:
        k=n-4
        Jdis=D(k)+4*H[k]
    else:
        Jdis=None
    return Z,E,Jadj,Jdis

def brute_kn(n):
    edges=list(combinations(range(n),2))
    idx={e:i for i,e in enumerate(edges)}
    e=(0,1)
    fadj=(0,2) if n>=3 else None
    fdis=(2,3) if n>=4 else None
    Z=E=Ja=Jd=0
    for mask in range(1<<len(edges)):
        parent=list(range(n))
        def find(a):
            while parent[a]!=a:
                parent[a]=parent[parent[a]]
                a=parent[a]
            return a
        ok=True
        for i,(u,v) in enumerate(edges):
            if (mask>>i)&1:
                u=find(u); v=find(v)
                if u==v:
                    ok=False; break
                parent[u]=v
        if not ok: continue
        Z+=1
        if (mask>>idx[e])&1:
            E+=1
            if fadj and (mask>>idx[fadj])&1: Ja+=1
            if fdis and (mask>>idx[fdis])&1: Jd+=1
    return Z,E,Ja if n>=3 else None,Jd if n>=4 else None

for n in range(3,7):
    b=brute_kn(n)
    h=hermite_counts(n)
    assert b==h,(n,b,h)
    print("K",n,"counts",b,"gaps",
          (b[1]*b[1]-b[0]*b[2] if n>=3 else None),
          (b[1]*b[1]-b[0]*b[3] if n>=4 else None))

for n in range(6,501):
    k=n-4
    H=he_values(n+1,k)
    s=Fraction(k*H[k-1],H[k])
    L=Fraction((n-4)*(n-1)*(n+4),(n+1)**3)
    assert L <= s < 1
    G=(5-n)*s*s+(n*n-4*n-6)*s-n*n+9*n-14
    P=2*n**6+70*n**5-33*n**4+185*n**3+1369*n**2-3147*n+1170
    assert G >= Fraction(P,(n+1)**6) > 0
print("HERMITE_EXACT_REVIEW_PASS n=6..500")
