#!/usr/bin/env python3
from fractions import Fraction
from collections import Counter
from math import comb
import itertools
import sympy as sp

a,b,c = sp.symbols("a b c")
A = sp.Matrix([
    [1-a-b, 1+a,   1+b],
    [1+a,   1-a-c, 1+c],
    [1+b,   1+c,   1-b-c],
])
assert [sp.expand(sum(A[i,j] for j in range(3))) for i in range(3)] == [3,3,3]

D = {}
for i,j,k in itertools.product(range(3), repeat=3):
    D[i,j,k] = sp.expand(sum(A[w,i]*A[w,j]*A[w,k] for w in range(3)))

Fexpr = -3**10
for z in itertools.product(range(3), repeat=5):
    term = 1
    for i in range(5):
        term *= D[z[i], z[(i+1)%5], z[(i+2)%5]]
    Fexpr += term
F = sp.Poly(sp.expand(Fexpr), a,b,c, domain=sp.ZZ)
assert len(F.terms()) == 664
deg_counts = Counter(sum(exp) for exp, coeff in F.terms())
expected_counts = {4:15,6:28,7:33,8:45,9:52,10:66,11:75,12:82,13:87,14:90,15:91}
assert dict(sorted(deg_counts.items())) == expected_counts

# One full 3^10-coloring regression at the nontrivial vertex V1=(2,-1,-1).
edges = [(j,5+i) for i in range(5) for j in (i,(i+1)%5,(i+2)%5)]
M = [[0,3,0],[3,0,0],[0,0,3]]
direct = 0
for phi in itertools.product(range(3), repeat=10):
    p = 1
    for u,v in edges:
        p *= M[phi[u]][phi[v]]
    direct += p
assert direct - 3**10 == int(F.eval({a:2,b:-1,c:-1}))

r,s,t,z = sp.symbols("r s t z")

def normalized_poly(face):
    v = (1-s)*t
    if face == "lower":
        fa,fb,fc = -1+3*s, -1+3*v, -1
    else:
        fa = sp.Rational(1,2)*(1+3*s-3*v)
        fb = sp.Rational(1,2)*(1-3*s+3*v)
        fc = sp.Rational(1,2)*(1-3*s-3*v)
    expr = 0
    for (ea,eb,ec), coeff in F.terms():
        deg = ea+eb+ec
        expr += sp.Rational(int(coeff),3**10) * r**(deg-4) * fa**ea * fb**eb * fc**ec
    P = sp.Poly(sp.expand(expr), r,s,t, domain=sp.QQ)
    assert P.degree(r) <= 11 and P.degree(s) <= 15 and P.degree(t) <= 15
    return P

def power_tensor(poly, degrees=(11,15,15)):
    d0,d1,d2 = degrees
    out = [[[Fraction(0) for _ in range(d2+1)] for _ in range(d1+1)] for _ in range(d0+1)]
    for exps, q in poly.terms():
        i,j,k = exps
        out[i][j][k] = Fraction(int(q.p), int(q.q))
    return out

def bernstein_tensor(power, degrees=(11,15,15)):
    d0,d1,d2 = degrees
    x = [[[Fraction(0) for _ in range(d2+1)] for _ in range(d1+1)] for _ in range(d0+1)]
    for i in range(d0+1):
        for p in range(i+1):
            fac = Fraction(comb(i,p), comb(d0,p))
            for j in range(d1+1):
                for k in range(d2+1):
                    x[i][j][k] += fac*power[p][j][k]
    y = [[[Fraction(0) for _ in range(d2+1)] for _ in range(d1+1)] for _ in range(d0+1)]
    for j in range(d1+1):
        for q in range(j+1):
            fac = Fraction(comb(j,q), comb(d1,q))
            for i in range(d0+1):
                for k in range(d2+1):
                    y[i][j][k] += fac*x[i][q][k]
    out = [[[Fraction(0) for _ in range(d2+1)] for _ in range(d1+1)] for _ in range(d0+1)]
    for k in range(d2+1):
        for m in range(k+1):
            fac = Fraction(comb(k,m), comb(d2,m))
            for i in range(d0+1):
                for j in range(d1+1):
                    out[i][j][k] += fac*y[i][j][m]
    return out

expected = {
    ("lower",0): Fraction(17929,38220),
    ("lower",1): Fraction(43,84),
    ("upper",0): Fraction(725117,3179904),
    ("upper",1): Fraction(5055,11648),
}
mins = {}
for face in ("lower","upper"):
    Q = normalized_poly(face)
    for half in (0,1):
        sub = z/2 if half==0 else (1+z)/2
        P = sp.Poly(sp.expand(Q.as_expr().subs(s,sub)), r,z,t, domain=sp.QQ)
        B = bernstein_tensor(power_tensor(P))
        vals = [B[i][j][k] for i in range(12) for j in range(16) for k in range(16)]
        assert len(vals)==3072
        mn = min(vals)
        mins[(face,half)] = mn
        assert mn == expected[(face,half)]
        assert all(v > Fraction(1,5) for v in vals)

global_min = min(mins.values())
assert global_min == Fraction(725117,3179904)
assert global_min > Fraction(1,5)

entry_deficits = {sp.expand(1-A[i,j]) for i in range(3) for j in range(3)}
assert entry_deficits == {-a,-b,-c,a+b,a+c,b+c}

print("CLAIM C30-EQUAL-THREE-BLOCK-STABILITY-20260917")
print("AUDIT_SCOPE theorem1 continuum Bernstein certificate + graph normalization + radial rho identity")
print("MONOMIALS", len(F.terms()))
print("DEGREE_COUNTS", dict(sorted(deg_counts.items())))
for key in [("lower",0),("lower",1),("upper",0),("upper",1)]:
    print("MIN", key[0], key[1], mins[key])
print("GLOBAL_MIN", global_min)
print("GLOBAL_MIN_GT_1_5", global_min > Fraction(1,5))
print("DIRECT_COLORING_REGRESSION", 3**10, "colorings at V1")
print("RESULT PASS")
