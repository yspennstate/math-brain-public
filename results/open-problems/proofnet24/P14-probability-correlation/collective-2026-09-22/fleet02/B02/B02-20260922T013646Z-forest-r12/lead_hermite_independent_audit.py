from fractions import Fraction
from itertools import combinations

def hermite(m, x):
    if m == 0:
        return 1
    h0, h1 = 1, x
    if m == 1:
        return h1
    for j in range(1, m):
        h0, h1 = h1, x*h1 - j*h0
    return h1

def D(j, x):
    return hermite(j, x) - (j * hermite(j-1, x) if j else 0)

def forest_counts_kn(n):
    edges = list(combinations(range(n), 2))
    e = (0, 1)
    f_adj = (0, 2) if n >= 3 else None
    f_dis = (2, 3) if n >= 4 else None
    Z = E = Ja = Jd = 0
    for mask in range(1 << len(edges)):
        parent = list(range(n))
        rank = [0]*n
        ok = True
        contains_e = contains_a = contains_d = False
        for idx,(u,v) in enumerate(edges):
            if not (mask >> idx) & 1:
                continue
            ru, rv = u, v
            while parent[ru] != ru:
                parent[ru] = parent[parent[ru]]
                ru = parent[ru]
            while parent[rv] != rv:
                parent[rv] = parent[parent[rv]]
                rv = parent[rv]
            if ru == rv:
                ok = False
                break
            if rank[ru] < rank[rv]:
                ru, rv = rv, ru
            parent[rv] = ru
            if rank[ru] == rank[rv]:
                rank[ru] += 1
            edge = (u,v)
            if edge == e: contains_e = True
            if f_adj is not None and edge == f_adj: contains_a = True
            if f_dis is not None and edge == f_dis: contains_d = True
        if not ok:
            continue
        Z += 1
        E += contains_e
        Ja += contains_e and contains_a
        Jd += contains_e and contains_d
    return Z,E,Ja,Jd

for n in range(2,7):
    Z,E,Ja,Jd = forest_counts_kn(n)
    x = n+1
    fZ = D(n,x)
    fE = D(n-2,x)
    fJa = D(n-3,x) if n>=3 else 0
    if n >= 4:
        k=n-4
        fJd = 5*hermite(k,x) - k*(hermite(k-1,x) if k else 0)
    else:
        fJd = 0
    assert (Z,E,Ja,Jd) == (fZ,fE,fJa,fJd), (n,(Z,E,Ja,Jd),(fZ,fE,fJa,fJd))
    if n>=3:
        assert E*E-Z*Ja >= 0
    if n>=4:
        assert E*E-Z*Jd >= 0
    print("K",n,"counts",Z,E,Ja,Jd,"FORMULA_MATCH")

# exact all-n algebraic audit at integer n values; proof is in report.
for n in range(6,501):
    k=n-4
    x=n+1
    Hk=hermite(k,x)
    Hkm1=hermite(k-1,x)
    s=Fraction(k*Hkm1,Hk)
    L=Fraction((n-4)*(n-1)*(n+4),(n+1)**3)
    assert L <= s < 1
    G=(5-n)*s*s+(n*n-4*n-6)*s-n*n+9*n-14
    assert G > 0
    P=2*n**6+70*n**5-33*n**4+185*n**3+1369*n**2-3147*n+1170
    assert P > 0
    assert (5-n)*L*L+(n*n-4*n-6)*L-n*n+9*n-14 == Fraction(P,(n+1)**6)

print("HERMITE_BOUND_AND_GAP_REGRESSION_PASS_6_TO_500")
print("INDEPENDENT_AUDIT_PASS")
