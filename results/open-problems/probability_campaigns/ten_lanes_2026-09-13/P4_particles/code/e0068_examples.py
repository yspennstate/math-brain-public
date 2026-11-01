# E0068 / Problem 21 of arXiv:0902.4207 : QSOs with V^r(x) = V(x) for all x, some r >= 2.
# Exact verification (sympy, rational arithmetic) of the examples and identities claimed
# in E0068_bernstein_periodic.md.
import sympy as sp
from itertools import product

def qso_from_P(P, m, xs):
    """P: dict (i,j) -> list of m coefficients (i<=j, symmetric).  Returns list V(x)_k."""
    V = [sp.Integer(0)] * m
    for (i, j), row in P.items():
        c = xs[i] * xs[j] * (1 if i == j else 2)
        for k in range(m):
            V[k] += sp.nsimplify(row[k]) * c
    return [sp.expand(v) for v in V]

def check_qso(P, m, xs, name):
    ok_rows = all(sum(sp.nsimplify(c) for c in row) == 1 and all(sp.nsimplify(c) >= 0 for c in row)
                  for row in P.values())
    V = qso_from_P(P, m, xs)
    ok_sum = sp.expand(sum(V) - sum(xs) ** 2) == 0
    print(f"{name}: rows stochastic&nonneg={ok_rows}  sum V = (sum x)^2 : {ok_sum}")
    return V

def compose(V, xs, subs_target):
    return [sp.expand(v.subs(dict(zip(xs, subs_target)), simultaneous=True)) for v in V]

def homog_reduce(expr, xs):
    """on the simplex sum xs = 1 ; substitute the last variable"""
    return sp.expand(expr.subs(xs[-1], 1 - sum(xs[:-1])))

# ---------------- m = 2 : the transposition ----------------
x1, x2 = sp.symbols('x1 x2')
P2 = {(0, 0): [0, 1], (0, 1): [sp.Rational(1, 2), sp.Rational(1, 2)], (1, 1): [1, 0]}
V2 = check_qso(P2, 2, [x1, x2], "m=2 transposition")
print("   V(x) =", V2)
V2V2 = compose(V2, [x1, x2], V2)
print("   V(V(x)) - (x1+x2)^3 x  =",
      [sp.expand(V2V2[k] - (x1 + x2) ** 3 * [x1, x2][k]) for k in range(2)])

# ---------------- m = 3 : the 3-cycle permutation ----------------
y = sp.symbols('y1 y2 y3')
h = sp.Rational(1, 2)
# V_sigma(x)_k = x_{sigma^{-1}(k)} ; sigma = (1 2 3) so V(x) = (x3, x1, x2)
P3 = {(0, 0): [0, 1, 0], (1, 1): [0, 0, 1], (2, 2): [1, 0, 0],
      (0, 1): [0, h, h], (0, 2): [h, h, 0], (1, 2): [h, 0, h]}
V3 = check_qso(P3, 3, list(y), "m=3 3-cycle permutation")
print("   V(x) - (x3,x1,x2)*(sum x) =",
      [sp.expand(V3[k] - [y[2], y[0], y[1]][k] * sum(y)) for k in range(3)])
V3_2 = compose(V3, list(y), V3)
V3_3 = compose(V3, list(y), V3_2)
print("   V^3(x) - (sum x)^7 x =",
      [sp.expand(V3_3[k] - sum(y) ** 7 * y[k]) for k in range(3)])

# ---------------- m = 3 : retraction onto an edge, flipped ----------------
# V(x)_1 = x1 x2 + x2^2 ,  V(x)_3 = 0
Pe = {(0, 0): [0, 1, 0], (0, 1): [h, h, 0], (0, 2): [0, 1, 0],
      (1, 1): [1, 0, 0], (1, 2): [0, 1, 0], (2, 2): [0, 1, 0]}
Ve = check_qso(Pe, 3, list(y), "m=3 edge retraction + flip")
print("   V(x) =", Ve)
Ve2 = compose(Ve, list(y), Ve)
Ve3 = compose(Ve, list(y), Ve2)
print("   V^3(x) - (sum x)^6 V(x) =",
      [sp.expand(Ve3[k] - sum(y) ** 6 * Ve[k]) for k in range(3)])
print("   V^2(x) - (sum x)^2 V(x) =",
      [sp.expand(Ve2[k] - sum(y) ** 2 * Ve[k]) for k in range(3)],
      "   (nonzero => V is NOT idempotent)")
print("   image lies on the edge x3=0 :", sp.expand(Ve[2]) == 0)

# ---------------- m = 2 : no other non-idempotent ----------------
A, B, C, xx = sp.symbols('A B C x')
f = sp.expand(A * xx ** 2 + 2 * B * xx * (1 - xx) + C * (1 - xx) ** 2)
a = sp.expand(f.coeff(xx, 2))
print("\nm=2 leading coefficient a =", a)
print("f o f leading coefficient =", sp.expand(sp.expand(f.subs(xx, f)).coeff(xx, 4)),
      " (so f o f = id forces a = 0)")
sol = sp.solve([sp.Eq(a, 0), sp.Eq(sp.expand(f.coeff(xx, 1)), -1), sp.Eq(f.subs(xx, 0), 1)],
               [A, B, C], dict=True)
print("affine decreasing involution preserving [0,1]:", sol)
