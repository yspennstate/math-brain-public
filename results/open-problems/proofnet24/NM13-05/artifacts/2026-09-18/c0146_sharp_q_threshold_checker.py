#!/usr/bin/env python3
from fractions import Fraction
from collections import defaultdict

V = tuple(range(7))
E = (
    (0,1),(0,2),(0,3),(0,4),(0,5),
    (1,2),(1,3),(1,4),(1,6),(5,6),
)
DIST = 0
M = len(E)


def component_count(mask):
    parent = list(V)
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    for i, (u, v) in enumerate(E):
        if (mask >> i) & 1:
            a, b = find(u), find(v)
            if a != b:
                parent[b] = a
    return len({find(v) for v in V})


all_count = defaultdict(int)
edge_count = defaultdict(int)
for mask in range(1 << M):
    r = mask.bit_count()
    c = r - len(V) + component_count(mask)
    assert c >= 0
    all_count[(r,c)] += 1
    if (mask >> DIST) & 1:
        edge_count[(r,c)] += 1

maxc = max(c for (r,c) in all_count)


def q_polys(x):
    x = Fraction(x)
    D = [Fraction(0) for _ in range(maxc+1)]
    N = [Fraction(0) for _ in range(maxc+1)]
    for (r,c), a in all_count.items():
        D[c] += a * x**r
    for (r,c), a in edge_count.items():
        N[c] += a * x**r
    return D, N


def conv(a,b):
    out = [Fraction(0) for _ in range(len(a)+len(b)-1)]
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            out[i+j] += x*y
    return out


def eval_poly(coeffs, z):
    z = Fraction(z)
    s = Fraction(0)
    p = Fraction(1)
    for a in coeffs:
        s += a*p
        p *= z
    return s

# Method-24 rationalization near the derivative saddle found in method-5 scouting.
x1 = Fraction(512,25)    # 20.48
x2 = Fraction(2049,100)  # 20.49
assert x1 < x2
D1,N1 = q_polys(x1)
D2,N2 = q_polys(x2)
H = [a-b for a,b in zip(conv(N1,D2), conv(N2,D1))]
while H and H[-1] == 0:
    H.pop()

# Clear denominators to expose the exact sign pattern.
def lcm(a,b):
    import math
    return abs(a*b)//math.gcd(a,b)
common_den = 1
for a in H:
    common_den = lcm(common_den, a.denominator)
H_int = [a.numerator*(common_den//a.denominator) for a in H]
expected_H_int = [
    986531766884142045004854319525937500000000000,
    -32143509596466558162391026506370142400687500000000,
    -1146450076641884513896040584662442340620694062500000,
    -16463066302403334230838924672590135582374476301562500,
    -124838805506322909059280302383078512952746815601265625,
    -551294838926831492907614492140885444938167683645440000,
    -1396895177743892375801230881843324555409397430563635200,
    -1539243308922527919763929859402064180194372632390402048,
]
assert H_int == expected_H_int
assert H_int[0] > 0 and all(a < 0 for a in H_int[1:])

# Therefore H'(q)<0 for q>0. It suffices to verify H(q0)>0 at the right endpoint.
q0 = Fraction(1,32618)
Hq0 = eval_poly(H, q0)
expected_Hq0 = Fraction(
    3059721428192140729677709720042967828909885630965023987229789597682419,
    1873144967280370161332960272637939453125000000000000000000000000,
)
assert Hq0 == expected_Hq0 and Hq0 > 0

# Translate x=p/[q(1-p)] back to source p coordinates.
p1 = x1*q0/(1+x1*q0)
p2 = x2*q0/(1+x2*q0)
assert p1 == Fraction(256,407981)
assert p2 == Fraction(2049,3263849)
assert p1 < p2

P1 = eval_poly(N1,q0)/eval_poly(D1,q0)
P2 = eval_poly(N2,q0)/eval_poly(D2,q0)
drop = P1-P2
assert P1 == Fraction(
    13497273509071773805642009057600701796864,
    38188477772779164561962899231286395649889,
)
assert P2 == Fraction(
    227097780491540948519918200390273843901961405801,
    642538549487122449716007539469431589617741514001,
)
assert drop == Fraction(
    65659206279454767316202326084448371475909637836063916062803471774477067725,
    1291451006065407417825123791982739179970979856393742659933835109721438845221985851978731,
)
assert drop > 0

# Because H is strictly decreasing on q>0 and H(q0)>0,
# N1(q)/D1(q) > N2(q)/D2(q) for every 0<q<=q0.
# This is a one-edge increasing-event reversal at p1(q)<p2(q).
for test_q in (Fraction(1,10**9), Fraction(1,40000), q0):
    assert test_q <= q0
    assert eval_poly(H,test_q) > 0
    assert eval_poly(N1,test_q)/eval_poly(D1,test_q) > eval_poly(N2,test_q)/eval_poly(D2,test_q)

print('vertices', len(V))
print('edges', M)
print('edge_list', E)
print('distinguished_edge', E[DIST])
print('x1', x1)
print('x2', x2)
print('H_integer_coefficients', H_int)
print('q_endpoint', q0)
print('H_at_endpoint', Hq0)
print('p1_endpoint', p1)
print('p2_endpoint', p2)
print('edge_prob_p1', P1)
print('edge_prob_p2', P2)
print('exact_edge_marginal_drop', drop)
print('certified_positive_q_interval', '0 < q <= 1/32618')
print('previous_endpoint', Fraction(1,40000))
print('endpoint_ratio_new_over_old', q0/Fraction(1,40000))
print('ALL_EXACT_CHECKS_PASS')
