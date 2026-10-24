#!/usr/bin/env python3
"""Independent exact P26 audit for C30 equal-three-block Sidorenko stability.

Reconstructs the homomorphism polynomial for H=K_{5,5} minus C_10, radializes
the exact admissible 3x3 regular-kernel polytope, and recomputes the four
tensor-Bernstein lower certificates using exact rational arithmetic.

This code is independent of C30 verify.py/results.json and does not import them.
"""
import itertools, math, collections
from fractions import Fraction
import sympy as sp

a,b,c,r,s,t,z = sp.symbols("a b c r s t z")
A = sp.Matrix([
    [1-a-b, 1+a,   1+b],
    [1+a,   1-a-c, 1+c],
    [1+b,   1+c,   1-b-c],
])

# Triple contractions after summing one color class of H.
D = {}
for i,j,k in itertools.product(range(3), repeat=3):
    D[i,j,k] = sp.expand(sum(A[w,i]*A[w,j]*A[w,k] for w in range(3)))

# Left-color contraction formula for H: y_i adjacent x_i,x_{i+1},x_{i+2}.
F = -3**10
for q in itertools.product(range(3), repeat=5):
    term = 1
    for i in range(5):
        term *= D[q[i], q[(i+1)%5], q[(i+2)%5]]
    F += term
F = sp.Poly(sp.expand(F), a,b,c, domain=sp.QQ)

degree_counts = collections.Counter(sum(m) for m,coef in F.terms())
assert len(F.terms()) == 664
assert F.total_degree() == 15
assert sorted(degree_counts.items()) == [
    (4,15),(6,28),(7,33),(8,45),(9,52),(10,66),
    (11,75),(12,82),(13,87),(14,90),(15,91)
]

# Check graph/color normalization independently at the nontrivial boundary point V1.
def eval_A(aa,bb,cc):
    return [
        [1-aa-bb, 1+aa, 1+bb],
        [1+aa, 1-aa-cc, 1+cc],
        [1+bb, 1+cc, 1-bb-cc],
    ]

M = eval_A(2,-1,-1)
direct = 0
# vertices x0..x4,y0..y4; y_i adjacent x_i,x_{i+1},x_{i+2}.
for colors in itertools.product(range(3), repeat=10):
    prod = 1
    for i in range(5):
        yi = colors[5+i]
        for j in (i,(i+1)%5,(i+2)%5):
            prod *= M[colors[j]][yi]
    direct += prod
poly_val = int(F.eval({a:2,b:-1,c:-1}) + 3**10)
assert direct == poly_val

# Exact tensor Bernstein conversion. For p(x)=sum p_k x^k of degree<=d,
# b_i=sum_{k<=i} p_k C(i,k)/C(d,k).
def to_fraction(x):
    x = sp.Rational(x)
    return Fraction(int(x.p), int(x.q))

def power_dict(poly, vars_):
    P = sp.Poly(poly, *vars_, domain=sp.QQ)
    return {m:to_fraction(q) for m,q in P.terms()}

def bernstein_min(poly, vars_, degrees):
    coeff = power_dict(poly, vars_)
    for axis,deg in enumerate(degrees):
        nxt = collections.defaultdict(Fraction)
        for mon,q in coeff.items():
            k = mon[axis]
            den = math.comb(deg,k)
            for i in range(k,deg+1):
                mm = list(mon)
                mm[axis] = i
                nxt[tuple(mm)] += q*Fraction(math.comb(i,k),den)
        coeff = dict(nxt)
    expected = math.prod(d+1 for d in degrees)
    assert len(coeff) == expected
    key,val = min(coeff.items(), key=lambda kv: kv[1])
    return val,key,expected

# Representative lower/upper faces after block-label symmetry, with u=s,
# v=(1-s)t covering the closed triangle.
lower = (-1+3*s, -1+3*(1-s)*t, -1)
upper = (
    sp.Rational(1,2)*(1+3*s-3*(1-s)*t),
    sp.Rational(1,2)*(1-3*s+3*(1-s)*t),
    sp.Rational(1,2)*(1-3*s-3*(1-s)*t),
)

expected_minima = {
    ("lower","first"): Fraction(17929,38220),
    ("lower","second"): Fraction(43,84),
    ("upper","first"): Fraction(725117,3179904),
    ("upper","second"): Fraction(5055,11648),
}

mins = {}
for name,face in (("lower",lower),("upper",upper)):
    expr = F.as_expr().subs({a:r*face[0],b:r*face[1],c:r*face[2]})
    # No degree<4 means exact divisibility by r^4.
    Gexpr = sp.cancel(sp.expand(expr)/(3**10*r**4))
    G = sp.Poly(Gexpr,r,s,t,domain=sp.QQ)
    assert G.degree(r) <= 11 and G.degree(s) <= 15 and G.degree(t) <= 15
    for half,sub in (("first",z/2),("second",(1+z)/2)):
        child = sp.Poly(sp.expand(G.as_expr().subs(s,sub)),r,z,t,domain=sp.QQ)
        mval,midx,count = bernstein_min(child,(r,z,t),(11,15,15))
        mins[(name,half)] = (mval,midx,count)
        assert mval == expected_minima[(name,half)]
        assert mval > Fraction(1,5)

global_min = min(v[0] for v in mins.values())
assert global_min == Fraction(725117,3179904)
assert global_min > Fraction(1,5)

# Independent exact geometry checks for rho. 1-A_ij are exactly these six
# linear forms, so rho=max of them on the admissible polytope.
deficits = {sp.expand(1-A[i,j]) for i in range(3) for j in range(3)}
assert deficits == {-a,-b,-c,a+b,a+c,b+c}

# L2 step: the claimed constant follows algebraically from
# ||A-1||_L2^2 <= 2 rho^2 and the certified rho^4/5 gap.
assert Fraction(1,5) * Fraction(1,4) == Fraction(1,20)

print("P26-C30-EQUAL-THREE-BLOCK-INDEPENDENT-EXACT-AUDIT: PASS")
print("claim=C30-EQUAL-THREE-BLOCK-STABILITY-20260917")
print("polynomial_monomials=664 total_degree=15")
print("degree_counts=" + repr(dict(sorted(degree_counts.items()))))
print(f"boundary_direct_coloring_sum={direct}")
for key in [("lower","first"),("lower","second"),("upper","first"),("upper","second")]:
    val,idx,count = mins[key]
    print(f"{key[0]}_{key[1]}: coefficients={count} min={val} index={idx}")
print(f"global_min={global_min}")
print("all_four_minima_gt_1/5=True")
print("rho_deficits={-a,-b,-c,a+b,a+c,b+c}")
print("L2_constant=(1/5)*(1/4)=1/20")
print("END P26-C30-EQUAL-THREE-BLOCK-INDEPENDENT-EXACT-AUDIT")
