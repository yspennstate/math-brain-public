#!/usr/bin/env python3
"""Exact audit for the A079 shared-variable correlated encoder barrier.

All Walsh and influence calculations use integers/Fractions. Decimal entropy
values are printed only as finite illustrations; the all-k statements are
proved in CORRELATED_AUXILIARY_CONSTRUCTION.tex.
"""
from fractions import Fraction as Q
from decimal import Decimal, getcontext

getcontext().prec = 70


def walsh(values):
    a = list(values)
    n = len(a)
    h = 1
    while h < n:
        for i in range(0, n, 2*h):
            for j in range(i, i+h):
                x, y = a[j], a[j+h]
                a[j], a[j+h] = x+y, x-y
        h *= 2
    return [Q(x, n) for x in a]


def influence(values, n):
    total = 0
    for x in range(1 << n):
        for i in range(n):
            total += values[x] != values[x ^ (1 << i)]
    return Q(total, 1 << n)


def h2(x):
    if x in (Decimal(0), Decimal(1)):
        return Decimal(0)
    ln2 = Decimal(2).ln()
    return (-x*x.ln()-(1-x)*(1-x).ln())/ln2


checks = 0
print("k points P(U) P(V) P(UV) I exact_ratio_to_iso H/I conditional_label_bits mean_product_degree")
for k in range(1, 6):
    n = 2*k
    N = 1 << n
    mask = (1 << k)-1
    vals = []
    cu = cv = cuv = 0
    for x in range(N):
        a = x & mask
        b = (x >> k) & mask
        u = int(a == 0)
        v = int((a ^ b) == 0)
        cu += u
        cv += v
        cuv += u*v
        vals.append(1-2*u*v)
    eps = Q(1, 1 << k)
    delta = eps*eps
    assert Q(cu,N) == eps; checks += 1
    assert Q(cv,N) == eps; checks += 1
    assert Q(cuv,N) == delta; checks += 1
    coeff = walsh(vals)
    masses = [c*c for c in coeff]
    assert sum(masses) == 1; checks += 1
    assert masses[0] == (1-2*delta)**2; checks += 1
    assert all(q == 4*delta*delta for q in masses[1:]); checks += 1
    I = influence(vals,n)
    iso = 4*k*delta
    assert I == iso; checks += 1

    # The product of the two centered encoder characters has labels
    # (S xor T,T), with S,T nonempty.  This map is injective and forces
    # R!=T.  Its conditional label entropy is log2(2^k-1).
    nonempty = range(1, 1 << k)
    image = {(s ^ t, t) for s in nonempty for t in nonempty}
    assert len(image) == ((1 << k)-1)**2; checks += 1
    assert all(r != t and t != 0 for r,t in image); checks += 1
    degree_sum = sum(r.bit_count()+t.bit_count() for r,t in image)
    mean_degree = Q(degree_sum, len(image))
    q = Q(1 << (k-1), (1 << k)-1)
    expected_degree = k*q + 2*k*q*(1-q)
    assert mean_degree == expected_degree; checks += 1

    d = Decimal(delta.numerator)/Decimal(delta.denominator)
    W = 4*d*(1-d)
    H = h2(W) + W*(Decimal((1 << (2*k))-1).ln()/Decimal(2).ln())
    HdI = H/(Decimal(I.numerator)/Decimal(I.denominator))
    cond = Decimal((1 << k)-1).ln()/Decimal(2).ln()
    md = Decimal(mean_degree.numerator)/Decimal(mean_degree.denominator)
    print(k,N,str(eps),str(eps),str(delta),str(I),str(I/iso),
          f"{HdI:.12f}",f"{cond:.12f}",f"{md:.12f}")

print(f"PASS: {checks} exact assertions; deterministic; no random seed")
