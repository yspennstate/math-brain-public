#!/usr/bin/env python3
from collections import Counter
from fractions import Fraction
from math import factorial, gcd

def partitions(n, maxpart=None):
    if n == 0:
        yield []
        return
    if maxpart is None or maxpart > n:
        maxpart = n
    for first in range(maxpart, 0, -1):
        for rest in partitions(n-first, first):
            yield [first] + rest

def representative_perm(parts):
    n = sum(parts)
    p = list(range(n))
    start = 0
    for ell in parts:
        cyc = list(range(start, start+ell))
        for i, v in enumerate(cyc):
            p[v] = cyc[(i+1) % ell]
        start += ell
    return p

def cycle_type_multiplicity(parts):
    c = Counter(parts)
    den = 1
    for ell, mult in c.items():
        den *= (ell**mult) * factorial(mult)
    return factorial(sum(parts)) // den

def edge_orbit_count(n, p):
    edges = [(i,j) for j in range(1,n) for i in range(j)]
    edge_index = {e:k for k,e in enumerate(edges)}
    seen = [False]*len(edges)
    orbits = 0
    for k, (a,b) in enumerate(edges):
        if seen[k]:
            continue
        orbits += 1
        cur = k
        while not seen[cur]:
            seen[cur] = True
            a,b = edges[cur]
            x,y = p[a],p[b]
            if x > y:
                x,y = y,x
            cur = edge_index[(x,y)]
    return orbits

def unlabeled_graph_count(n):
    numerator = 0
    for parts in partitions(n):
        p = representative_perm(parts)
        eorbits = edge_orbit_count(n,p)
        numerator += cycle_type_multiplicity(parts) * (1 << eorbits)
    assert numerator % factorial(n) == 0
    return numerator // factorial(n)

U7 = unlabeled_graph_count(7)
U8 = unlabeled_graph_count(8)
U9 = unlabeled_graph_count(9)
assert (U7,U8,U9) == (1044,12346,274668)

# Independent K9 hom(H,K9) calculation from the five-variable
# common-neighbor contraction. In K9, a triple has 9-|{a,b,c}| common neighbors.
n = 9
def C(a,b,c):
    return n - len({a,b,c})

h = 0
for a in range(n):
    for b in range(n):
        for c in range(n):
            for d in range(n):
                for e in range(n):
                    h += (C(c,d,e)*C(d,e,a)*C(e,a,b)*
                          C(a,b,c)*C(b,c,d))
assert h == 601891992

num = h * n**20
den = 72**15
assert num == 7317601481221369317436061592
assert den == 7244150201408990671659859968
g = gcd(num,den)
assert (num//g, den//g) == (4442640029451,4398046511104)
ratio = Fraction(num,den)
assert ratio > 1

assert U7 * 2**7 == 133632
assert U8 * 2**8 == 3160576

print("C29 independent audit checker for C30 order-nine Sidorenko package")
print(f"independent_cycle_type_Burnside_U7={U7}")
print(f"independent_cycle_type_Burnside_U8={U8}")
print(f"independent_cycle_type_Burnside_U9={U9}")
print("C30_augmentation_raw_counts=PASS")
print(f"independent_K9_hom={h}")
print(f"independent_K9_ratio_reduced={num//g}/{den//g}")
print("independent_K9_ratio_gt_1=PASS")
print("AUDIT_ARITHMETIC_CROSSCHECK=PASS")
print("ALL_EXACT_CHECKS_PASS")
