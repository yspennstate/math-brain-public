#!/usr/bin/env python3
from fractions import Fraction

def forest_ok(n, chosen):
    parent = list(range(n))
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    for u,v in chosen:
        a,b = find(u), find(v)
        if a == b:
            return False
        parent[a] = b
    return True

def book_edges(k):
    # Vertices 0,1 are the common spine endpoints; pages are 2,...,k+1.
    # g=01; page i has edges a_i=0-(i+2), b_i=1-(i+2).
    E=[(0,1)]
    for i in range(k):
        x=i+2
        E += [(0,x),(1,x)]
    return E

def exact_counts(k):
    E=book_edges(k)
    g=0
    e=1          # a_1
    f=3          # a_2, so k>=2
    A=B=a0=a1=b0=b1=c0=c1=0
    for mask in range(1<<len(E)):
        chosen=[E[j] for j in range(len(E)) if (mask>>j)&1]
        if not forest_ok(k+2, chosen):
            continue
        ee=(mask>>e)&1
        ff=(mask>>f)&1
        gg=(mask>>g)&1
        if gg:
            B += 1; a1 += ee; b1 += ff; c1 += ee*ff
        else:
            A += 1; a0 += ee; b0 += ff; c0 += ee*ff
    return (A,B,a0,a1,b0,b1,c0,c1)

def formulas(k):
    A = 3**(k-1)*(k+3)
    B = 3**k
    a0=b0=3**(k-2)*(k+5)
    a1=b1=3**(k-1)
    c0 = 3 if k == 2 else 3**(k-3)*(k+7)
    c1=3**(k-2)
    return (A,B,a0,a1,b0,b1,c0,c1)

for k in range(2,7):
    got=exact_counts(k)
    want=formulas(k)
    assert got==want, (k,got,want)
    A,B,a0,a1,b0,b1,c0,c1=got
    D0=a0*b0-A*c0
    D1=a1*b1-B*c1
    M=a0*b1+a1*b0-A*c1-B*c0
    Pe=B*a0-A*a1
    Pf=B*b0-A*b1
    assert D0 == 4*3**(2*k-4)
    assert D1 == 0 and M == 0
    assert Pe == Pf == 2*3**(2*k-2)

    p0=Fraction(a0,A)
    p1=Fraction(a1,B)
    drift=p0-p1
    c0neg=p0*p0-Fraction(c0,A)
    c1neg=p1*p1-Fraction(c1,B)
    assert drift == Fraction(2,3*(k+3))
    assert c0neg == drift*drift
    assert c1neg == 0

    # Contracting g produces k parallel classes of size 2. Exact aggregation
    # is a weighted star with class weights 2, so B=3^k and a fixed
    # original member has derivative count 3^(k-1).
    B_exact=3**k
    a1_exact=3**(k-1)
    assert (B_exact,a1_exact)==(B,a1)

    # Naively forgetting multiplicity gives a unit star and flips the
    # hybrid cross-gap used by deletion/contraction bookkeeping.
    B_naive=2**k
    a1_naive=2**(k-1)
    Pe_naive=B_naive*a0-A*a1_naive
    want_naive=2**(k-1)*3**(k-2)*(1-k)
    assert Pe_naive==want_naive
    assert Pe_naive<0

    print(
        f"k={k} counts={got} "
        f"Qcoeff={(D0,M,D1)} Pe={Pe} "
        f"drift={drift} c0={c0neg} c1={c1neg} "
        f"naive_Pe={Pe_naive}"
    )

print("STATUS=PASS")
