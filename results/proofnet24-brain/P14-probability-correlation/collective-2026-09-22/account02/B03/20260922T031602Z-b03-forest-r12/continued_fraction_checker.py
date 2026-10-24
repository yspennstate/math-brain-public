from fractions import Fraction
from itertools import combinations

def he_values(m, x):
    h = [0]*(m+1)
    h[0] = 1
    if m >= 1:
        h[1] = x
    for j in range(2, m+1):
        h[j] = x*h[j-1] - (j-1)*h[j-2]
    return h

def d(h, j):
    if j == 0:
        return h[0]
    return h[j] - j*h[j-1]

def formula_counts(n):
    x = n+1
    h = he_values(n, x)
    Z = d(h, n)
    E = d(h, n-2)
    Jadj = d(h, n-3) if n >= 3 else None
    if n >= 4:
        k = n-4
        Jdis = d(h, k) + 4*h[k]
    else:
        Jdis = None
    return Z,E,Jadj,Jdis,h

def forest(edge_subset, n):
    parent=list(range(n))
    def find(a):
        while parent[a] != a:
            parent[a] = parent[parent[a]]
            a = parent[a]
        return a
    for u,v in edge_subset:
        ru,rv=find(u),find(v)
        if ru==rv:
            return False
        parent[ru]=rv
    return True

def brute_counts(n):
    edges=list(combinations(range(n),2))
    e=(0,1)
    f_adj=(0,2) if n>=3 else None
    f_dis=(2,3) if n>=4 else None
    Z=E=Jadj=Jdis=0
    m=len(edges)
    for mask in range(1<<m):
        S=[edges[i] for i in range(m) if (mask>>i)&1]
        if not forest(S,n):
            continue
        Z += 1
        has_e=e in S
        if has_e: E += 1
        if f_adj is not None and has_e and f_adj in S:
            Jadj += 1
        if f_dis is not None and has_e and f_dis in S:
            Jdis += 1
    return Z,E,Jadj if n>=3 else None,Jdis if n>=4 else None

def G(n, s):
    return (5-n)*s*s + (n*n-4*n-6)*s - n*n + 9*n - 14

print("CONTINUED_FRACTION_FOREST_CHECK")
for n in range(3,7):
    fc=formula_counts(n)[:4]
    bc=brute_counts(n)
    print("BRUTE", n, "formula", fc, "brute", bc, "match", fc==bc)
    assert fc == bc

for n in range(4,501):
    Z,E,Jadj,Jdis,h = formula_counts(n)
    if n >= 4:
        gap_dis=E*E-Z*Jdis
        assert gap_dis > 0
    if n >= 3:
        gap_adj=E*E-Z*Jadj
        assert gap_adj > 0
    if n >= 5:
        k=n-4
        x=n+1
        s=Fraction(k*h[k-1], h[k])
        C=Fraction(k*x, x*x-k+1)
        assert Fraction(0) < s < Fraction(1)
        assert s >= C
        assert Fraction(gap_dis, h[k]*h[k]) == G(n,s)
        num = 3*k**4 + 88*k**3 + 709*k**2 + 2704*k + 4056
        den = (k*k+9*k+26)**2
        assert G(n,C) == Fraction(num,den)
        if n >= 6:
            assert n*n - 6*n + 4 > 0
            assert G(n,s) >= G(n,C) > 0

print("K3_GAP_ADJ", formula_counts(3)[1]**2-formula_counts(3)[0]*formula_counts(3)[2])
print("K4_GAP_DIS", formula_counts(4)[1]**2-formula_counts(4)[0]*formula_counts(4)[3])
print("K5_GAP_DIS", formula_counts(5)[1]**2-formula_counts(5)[0]*formula_counts(5)[3])
print("BOUND_IDENTITY", "G(C)=(3k^4+88k^3+709k^2+2704k+4056)/(k^2+9k+26)^2")
print("STATUS=PASS n=4..500, brute K3..K6")
