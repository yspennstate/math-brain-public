from fractions import Fraction
from itertools import combinations

def uf_forest(n, edges_mask, edges):
    p=list(range(n))
    def find(a):
        while p[a]!=a:
            p[a]=p[p[a]]
            a=p[a]
        return a
    for i,(u,v) in enumerate(edges):
        if (edges_mask>>i)&1:
            a,b=find(u),find(v)
            if a==b: return False
            p[a]=b
    return True

def brute_K(n):
    edges=list(combinations(range(n),2))
    m=len(edges)
    Z=0
    cnt=[0]*m
    pair={}
    for mask in range(1<<m):
        if not uf_forest(n,mask,edges): continue
        Z+=1
        inds=[i for i in range(m) if (mask>>i)&1]
        for i in inds: cnt[i]+=1
        for a,b in combinations(inds,2):
            pair[a,b]=pair.get((a,b),0)+1
    E=cnt[0] if m else 0
    adj=dis=None
    if m>=2:
        e0=edges[0]
        for j in range(1,m):
            val=pair.get((0,j),0)
            if len(set(e0+edges[j]))==3 and adj is None: adj=val
            if len(set(e0+edges[j]))==4 and dis is None: dis=val
    return Z,E,adj,dis

def hermites(x,N):
    H=[1]
    if N==0:return H
    H.append(x)
    for j in range(1,N):
        H.append(x*H[j]-j*H[j-1])
    return H

def formulas(n):
    x=n+1
    H=hermites(x,n)
    def D(j):
        if j<0:return None
        return H[j]-(j*H[j-1] if j else 0)
    Z=D(n)
    E=D(n-2) if n>=2 else None
    adj=D(n-3) if n>=3 else None
    dis=None
    if n>=4:
        k=n-4
        dis=5*H[k]-(k*H[k-1] if k else 0)
    return Z,E,adj,dis,H

def P(n):
    return 2*n**6+70*n**5-33*n**4+185*n**3+1369*n**2-3147*n+1170

def Pshift(t):
    return 2*t**6+142*t**5+3147*t**4+33233*t**3+187651*t**2+551661*t+666396

print("INDEPENDENT_FOREST_KN_REVIEW")
for n in range(2,7):
    b=brute_K(n)
    f=formulas(n)[:4]
    print("K",n,"brute",b,"formula",f)
    assert b==f

for n in range(3,1001):
    Z,E,Jadj,Jdis,H=formulas(n)
    k=n-4
    if n>=4:
        a=H[k]
        s=Fraction(k*H[k-1],a) if k else Fraction(0)
        assert Jdis == a*(5-s)
        assert Jadj == a*(4-s)
        assert E == a*(2*n+6-3*s)
        assert Z == a*(n*n+3*n+10-(n+4)*s)
        G=(5-n)*s*s+(n*n-4*n-6)*s-n*n+9*n-14
        assert E*E-Z*Jdis == a*a*G
        if n>=6:
            L=Fraction((n-4)*(n-1)*(n+4),(n+1)**3)
            assert s>=L and s<1
            assert n*n-6*n+4>0
            GL=(5-n)*L*L+(n*n-4*n-6)*L-n*n+9*n-14
            assert GL == Fraction(P(n),(n+1)**6)
            assert P(n)==Pshift(n-6)
            assert Pshift(n-6)>0
            assert G>0
            assert E*E-Z*Jdis>0
            assert E*E-Z*Jadj>0
print("range_3_1000_exact_identities=PASS")
print("small_bruteforce=PASS")
print("hermite_gap_formula=PASS")
print("root_bound_numeric_regression=PASS")
print("shift_polynomial=PASS")
print("ALL_INDEPENDENT_REVIEW_CHECKS_PASS")
