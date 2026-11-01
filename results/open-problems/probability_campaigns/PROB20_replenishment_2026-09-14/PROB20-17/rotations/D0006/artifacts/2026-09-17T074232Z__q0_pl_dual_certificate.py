#!/usr/bin/env python3
"""
Exact rational certificate for the first midpoint-refined PL dual space on

    Q0 = conv{(-7,-5),(5,-5),(11,1),(-7,7)}.

For every continuous piecewise-affine f on the fixed 16-triangle refinement,
the exact identity

  integral_Q0 f =
      sum_j lambda_j [f(x_j)+f(y_j)+f(z_j)]

holds, with every lambda_j > 0 and every displayed triple satisfying
x_j+y_j+z_j=0 inside Q0.

Hence any such PL f that is nonnegative on every zero-sum triple
(f(x)+f(y)+f(z) >= 0 whenever x+y+z=0) has nonnegative integral.
So this finite PL level contains no negative-integral dual separator.

All arithmetic below is fractions.Fraction exact arithmetic.
"""

from fractions import Fraction as F

def det(a,b):
    return a[0]*b[1]-a[1]*b[0]

def sub(a,b):
    return (a[0]-b[0], a[1]-b[1])

def polygon_area2(poly):
    s=F(0)
    for p,q in zip(poly, poly[1:]+poly[:1]):
        s += det(p,q)
    return s

def polygon_centroid(poly):
    a2=polygon_area2(poly)
    cx=F(0); cy=F(0)
    for p,q in zip(poly, poly[1:]+poly[:1]):
        c=det(p,q)
        cx += (p[0]+q[0])*c
        cy += (p[1]+q[1])*c
    return (cx/(3*a2), cy/(3*a2))

Q0=[(F(-7),F(-5)),(F(5),F(-5)),(F(11),F(1)),(F(-7),F(7))]
assert polygon_area2(Q0)==F(288)
assert polygon_centroid(Q0)==(F(0),F(0))

nodes=[
    (F(-7),F(-5)),
    (F(5),F(-5)),
    (F(11),F(1)),
    (F(-7),F(7)),
    (F(0),F(0)),
    (F(-7,2),F(-5,2)),
    (F(-1),F(-5)),
    (F(5,2),F(-5,2)),
    (F(8),F(-2)),
    (F(11,2),F(1,2)),
    (F(2),F(4)),
    (F(-7,2),F(7,2)),
    (F(-7),F(1)),
]

triangles=[
    (0,6,5),(1,7,6),(4,5,7),(5,6,7),
    (1,8,7),(2,9,8),(4,7,9),(7,8,9),
    (2,10,9),(3,11,10),(4,9,11),(9,10,11),
    (3,12,11),(0,5,12),(4,11,5),(11,12,5),
]

def tri_area2(t):
    a,b,c=(nodes[i] for i in t)
    return abs(det(sub(b,a),sub(c,a)))

weights=[F(0) for _ in nodes]
for t in triangles:
    area=tri_area2(t)/2
    assert area>0
    for i in t:
        weights[i]+=area/3

expected_weights=[
    F(6),F(5),F(6),F(7),F(12),F(18),F(15,2),
    F(15),F(15,2),F(18),F(21,2),F(21),F(21,2)
]
assert weights==expected_weights
assert sum(weights)==F(144)

def barycentric_row(p,t):
    a,b,c=(nodes[i] for i in t)
    D=det(sub(b,a),sub(c,a))
    assert D != 0
    pa=sub(p,a); ba=sub(b,a); ca=sub(c,a)
    u=det(pa,ca)/D
    v=det(ba,pa)/D
    l0=F(1)-u-v
    if min(l0,u,v) < 0:
        return None
    r=[F(0) for _ in nodes]
    r[t[0]]=l0; r[t[1]]=u; r[t[2]]=v
    return r

def pl_eval_row(p):
    rows=[barycentric_row(p,t) for t in triangles]
    rows=[r for r in rows if r is not None]
    assert rows, ("point outside triangulation",p)
    first=rows[0]
    assert all(r==first for r in rows), ("inconsistent shared-face representation",p)
    return first

triples=[
    ((F(5,2),F(-5,2)), (F(1),F(13,3)), (F(-7,2),F(-11,6))),
    ((F(-35,11),F(-25,11)), (F(112,11),F(14,11)), (F(-7),F(1))),
    ((F(5,2),F(-5,2)), (F(9,2),F(5,6)), (F(-7),F(5,3))),
    ((F(-1),F(-5,2)), (F(8),F(-2)), (F(-7),F(9,2))),
    ((F(5),F(-5)), (F(-5,22),F(53,22)), (F(-105,22),F(57,22))),
    ((F(21,2),F(21,22)), (F(-7,2),F(7,2)), (F(-7),F(-49,11))),
    ((F(11,2),F(1,2)), (F(3,2),F(25,6)), (F(-7),F(-14,3))),
    ((F(-7,2),F(-5,2)), (F(7),F(7,11)), (F(-7,2),F(41,22))),
    ((F(2),F(-2)), (F(5),F(-5)), (F(-7),F(7))),
    ((F(-1),F(-5)), (F(11,7),F(1,7)), (F(-4,7),F(34,7))),
    ((F(0),F(0)), (F(7,2),F(-53,22)), (F(-7,2),F(53,22))),
]

lambdas=[
    F(13811332995,7229243504),
    F(1115827141,903655438),
    F(36002058345,7229243504),
    F(2855644836,451827719),
    F(8659339095,1807310876),
    F(2651652509,903655438),
    F(1594238526,451827719),
    F(3661077068,451827719),
    F(377215285,1807310876),
    F(15,2),
    F(11727387243,1807310876),
]
assert len(triples)==len(lambdas)==11
assert all(lam>0 for lam in lambdas)

triple_rows=[]
for tr in triples:
    sx=sum((p[0] for p in tr),F(0))
    sy=sum((p[1] for p in tr),F(0))
    assert (sx,sy)==(F(0),F(0))
    row=[F(0) for _ in nodes]
    for p in tr:
        pr=pl_eval_row(p)
        row=[a+b for a,b in zip(row,pr)]
    assert sum(row)==F(3)
    triple_rows.append(row)

certificate=[
    sum((lam*row[i] for lam,row in zip(lambdas,triple_rows)),F(0))
    for i in range(len(nodes))
]
assert certificate==weights

print("Q0_area=144")
print("Q0_centroid=(0,0)")
print("triangulation_nodes=13")
print("triangulation_triangles=16")
print("certificate_zero_sum_triples=11")
print("all_lambda_positive=True")
print("exact_weight_identity=True")
print("integration_weights=" + ",".join(str(x) for x in weights))
print("lambda_values=" + ",".join(str(x) for x in lambdas))
print("CONCLUSION=no_negative_integral_separator_in_this_continuous_PL_space")
print("ALL_ASSERTIONS_PASSED")
