"""Exact checks for the paper, in SymPy.

1. The binary identities: the discriminant, f(f(x)) - x = (f(x) - x) H(x), and the two-cycle of f_delta.
2. The threshold equations: the binary value and the roots of the contraction condition.
3. The two-cycle of Section 5 for symbolic t and for m = 3, ..., 8 by full substitution in the tensor.
4. The examples of Remark 5.2 (m = 3, 4, 5): full substitution and the eigenvalues of the derivative of V^2.

Writes data/exact_checks.json. Run from the repository root: python code/exact_checks.py
"""
import itertools
import json
from pathlib import Path

import sympy as sp

OUT = Path(__file__).resolve().parent.parent / "data" / "exact_checks.json"
results = {}


def record(name, ok):
    results[name] = bool(ok)
    print(("ok   " if ok else "FAIL ") + name)


# 1. binary case
x, a, b, c, d = sp.symbols("x a b c delta", real=True)
f = a * x**2 + 2 * b * x * (1 - x) + c * (1 - x) ** 2
A, B, C = a - 2 * b + c, 2 * (b - c), c
D = (B - 1) ** 2 - 4 * A * C
record("discriminant equals (2b-1)^2 + 4c(1-a)", sp.expand(D - ((2 * b - 1) ** 2 + 4 * c * (1 - a))) == 0)
H = A**2 * x**2 + A * (B + 1) * x + A * C + B + 1
record("f(f(x)) - x = (f(x) - x) H(x)", sp.expand(f.subs(x, f) - x - (f - x) * H) == 0)
record("H = (Ax + (B+1)/2)^2 + (4 - D)/4", sp.expand(H - ((A * x + (B + 1) / 2) ** 2 + (4 - D) / 4)) == 0)
dstar = (3 - sp.sqrt(7)) / 4
record("5 - 12 delta + 8 delta^2 = 4 at (3 - sqrt 7)/4", sp.simplify(5 - 12 * dstar + 8 * dstar**2 - 4) == 0)
t = 1 - 2 * d
fd = d + t * (1 - x) ** 2
rad = 4 * t * (1 - d) - 3
xp = (2 * t - 1 + sp.sqrt(rad)) / (2 * t)
xm = (2 * t - 1 - sp.sqrt(rad)) / (2 * t)
for dv in [sp.Rational(1, 100), sp.Rational(1, 20), sp.Rational(2, 25), sp.Rational(88, 1000)]:
    ok = sp.simplify(fd.subs({d: dv, x: xp.subs(d, dv)}) - xm.subs(d, dv)) == 0
    ok &= sp.simplify(fd.subs({d: dv, x: xm.subs(d, dv)}) - xp.subs(d, dv)) == 0
    ok &= bool(rad.subs(d, dv) > 0) and bool(0 < xm.subs(d, dv) < xp.subs(d, dv) < 1)
    record(f"two-cycle of f_delta at delta = {dv}", ok)
record("radicand vanishes at delta*", sp.simplify(rad.subs(d, dstar)) == 0)

# 2. contraction condition
m, mu = sp.symbols("m mu", positive=True)
poly = sp.expand(2 * (1 - m * mu) ** 2 - (1 - (m - 2) * mu))
record("2t^2 - (t + 2mu) = 2m^2mu^2 - (3m+2)mu + 1", sp.expand(poly - (2 * m**2 * mu**2 - (3 * m + 2) * mu + 1)) == 0)
Cm = 2 / (3 * m + 2 + sp.sqrt(m**2 + 12 * m + 4))
for mv in range(2, 12):
    record(f"C_m is a root of the contraction quadratic, m = {mv}", sp.simplify(poly.subs({m: mv, mu: Cm.subs(m, mv)})) == 0)
record("C_2 = (2 - sqrt 2)/4", sp.simplify(Cm.subs(m, 2) - (2 - sp.sqrt(2)) / 4) == 0)


# 3. the two-cycle of Section 5
def tensor(mv, ell):
    """P[(i,j)][k] for 0-based types; type 1 -> index 0, type 2 -> 1, type 3 -> 2, B = {1, 3, ..., mv-1}."""
    cls = {0: "A", 2: "C"}
    t_ = 1 - mv * ell
    P = {}
    for i, j in itertools.combinations_with_replacement(range(mv), 2):
        pair = "".join(sorted(cls.get(i, "B") + cls.get(j, "B")))
        child = {"AA": 2, "AB": 2, "CC": 0, "BC": 0, "AC": 1, "BB": 1}[pair]
        P[(i, j)] = [ell + (t_ if k == child else 0) for k in range(mv)]
    return P


def V(P, xs):
    mv = len(xs)
    return [sp.expand(sum(P[tuple(sorted((i, j)))][k] * xs[i] * xs[j] for i in range(mv) for j in range(mv))) for k in range(mv)]


def cycle_points(mv, ell):
    t_ = 1 - mv * ell
    z = 1 / t_ - 1
    s = 2 - 1 / t_
    Dm = s**2 - 4 * ell / t_
    u, v = (s + sp.sqrt(Dm)) / 2, (s - sp.sqrt(Dm)) / 2
    rest = [ell] * (mv - 3)
    X = [u, z - (mv - 3) * ell, v] + rest
    Y = [v, z - (mv - 3) * ell, u] + rest
    return X, Y, Dm


tt = sp.symbols("t", positive=True)
for mv in range(3, 9):
    Dm = cycle_points(mv, (1 - tt) / mv)[2]
    record(f"D_m = ((m+1)(2t-1)^2 - 1)/(m t^2), m = {mv}", sp.simplify(Dm - ((mv + 1) * (2 * tt - 1) ** 2 - 1) / (mv * tt**2)) == 0)
    Lm = (1 - 1 / sp.sqrt(mv + 1)) / (2 * mv)
    for frac in [sp.Rational(1, 2), sp.Rational(9, 10)]:
        ell = sp.nsimplify(sp.Rational(int(frac * Lm * 10**6), 10**6))
        P = tensor(mv, ell)
        X, Y, _ = cycle_points(mv, ell)
        ok = all(sp.simplify(sum(row) - 1) == 0 for row in P.values())
        ok &= min(min(row) for row in P.values()) == ell
        ok &= all(sp.simplify(p - q) == 0 for p, q in zip(V(P, X), Y))
        ok &= all(sp.simplify(p - q) == 0 for p, q in zip(V(P, Y), X))
        ok &= all(bool(sp.N(xi, 30) > 0) for xi in X) and sp.simplify(sum(X) - 1) == 0 and bool(sp.N(X[0] - X[2], 30) > 0)
        record(f"V(X) = Y, V(Y) = X, floor ell = {ell}, m = {mv}", ok)

# 4. examples of Remark 5.2
examples = {3: sp.Rational(2, 25), 4: sp.Rational(11, 160), 5: sp.Rational(7, 120)}
eig = {}
for mv, ell in examples.items():
    P = tensor(mv, ell)
    X, Y, _ = cycle_points(mv, ell)
    ok = all(sp.simplify(p - q) == 0 for p, q in zip(V(P, X), Y))
    ok &= max(max(row) for row in P.values()) == 1 - (mv - 1) * ell
    record(f"example m = {mv}: V(X) = Y and coefficients ell, 1-(m-1)ell", ok)
    ys = sp.symbols(f"y0:{mv}")
    img = V(P, list(ys))
    J = sp.Matrix([[sp.diff(img[k], ys[i]) for i in range(mv)] for k in range(mv)])
    J2 = J.subs(dict(zip(ys, Y))) * J.subs(dict(zip(ys, X)))
    basis = sp.Matrix([[1 if r == i else (-1 if r == mv - 1 else 0) for i in range(mv - 1)] for r in range(mv)])
    # the derivative maps the tangent space {sum h = 0} to itself; write it in the basis e_i - e_m
    T = sp.simplify((basis.T * basis).inv() * basis.T * J2 * basis)
    tr, det = sp.nsimplify(sp.simplify(T.trace())), sp.simplify(T.det())
    rad_ = max(abs(complex(sp.N(e, 30))) for e in T.eigenvals())
    eig[mv] = {"trace": str(tr), "det": str(det), "spectral_radius": float(rad_)}
    record(f"example m = {mv}: spectral radius of D(V^2) on the tangent space < 1", rad_ < 1)

results["examples"] = eig
OUT.parent.mkdir(exist_ok=True)
OUT.write_text(json.dumps(results, indent=2) + "\n", encoding="utf-8")
print("all passed" if all(v for k, v in results.items() if k != "examples") else "SOME FAILED")
