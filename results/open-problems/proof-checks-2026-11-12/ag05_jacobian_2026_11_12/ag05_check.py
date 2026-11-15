"""The three-dimensional Keller map of arXiv 2609.17795 (van den Essen), checked two ways.

F1 = u^3 z + y^2 p(u),  F2 = x u^2 z + y q(u),  F3 = x + x^2 y + x^3 z,
u = 1 - (2/3) x y,  p(u) = -(2/3) u^2 - (2/9) u,  q(u) = u^2 + q1 u - 2/9  (q1 solved for below).

Check A (sympy, exact): the Jacobian determinant as a polynomial; the q1 for which it is constant.
Check B (own arithmetic, Fractions, no sympy): polynomials as dicts, the determinant recomputed, and
two different rational points with the same image.
"""
import sys
from fractions import Fraction as Fr
from itertools import product


# ---------- check B machinery: polynomials in x, y, z as {(i, j, k): Fraction} ----------
def padd(a, b, s=1):
    r = dict(a)
    for m, c in b.items():
        r[m] = r.get(m, 0) + s * c
        if r[m] == 0:
            del r[m]
    return r


def pmul(a, b):
    r = {}
    for (i, j, k), c in a.items():
        for (l, m, n), d in b.items():
            key = (i + l, j + m, k + n)
            r[key] = r.get(key, 0) + c * d
    return {m: c for m, c in r.items() if c != 0}


def ppow(a, n):
    r = {(0, 0, 0): Fr(1)}
    for _ in range(n):
        r = pmul(r, a)
    return r


def pscal(a, c):
    return {m: c * v for m, v in a.items()} if c != 0 else {}


def pdiff(a, v):
    r = {}
    for m, c in a.items():
        if m[v]:
            n = list(m)
            n[v] -= 1
            r[tuple(n)] = c * m[v]
    return r


def peval(a, pt):
    return sum(c * pt[0] ** i * pt[1] ** j * pt[2] ** k for (i, j, k), c in a.items())


def det3(M):
    def m2(a, b, c, d):
        return padd(pmul(a, d), pmul(b, c), -1)
    t0 = pmul(M[0][0], m2(M[1][1], M[1][2], M[2][1], M[2][2]))
    t1 = pmul(M[0][1], m2(M[1][0], M[1][2], M[2][0], M[2][2]))
    t2 = pmul(M[0][2], m2(M[1][0], M[1][1], M[2][0], M[2][1]))
    return padd(padd(t0, t1, -1), t2)


X = {(1, 0, 0): Fr(1)}
Y = {(0, 1, 0): Fr(1)}
Z = {(0, 0, 1): Fr(1)}
ONE = {(0, 0, 0): Fr(1)}


def build(q1):
    u = padd(ONE, pscal(pmul(X, Y), Fr(2, 3)), -1)
    p = padd(pscal(ppow(u, 2), Fr(-2, 3)), pscal(u, Fr(-2, 9)))
    q = padd(padd(ppow(u, 2), pscal(u, q1)), pscal(ONE, Fr(-2, 9)))
    F1 = padd(pmul(ppow(u, 3), Z), pmul(ppow(Y, 2), p))
    F2 = padd(pmul(pmul(X, ppow(u, 2)), Z), pmul(Y, q))
    F3 = padd(padd(X, pmul(ppow(X, 2), Y)), pmul(ppow(X, 3), Z))
    return [F1, F2, F3]


def main():
    # ---------- check A ----------
    try:
        import sympy as sp
        x, y, z, q1 = sp.symbols("x y z q1")
        u = 1 - sp.Rational(2, 3) * x * y
        p = -sp.Rational(2, 3) * u ** 2 - sp.Rational(2, 9) * u
        q = u ** 2 + q1 * u - sp.Rational(2, 9)
        F = sp.Matrix([u ** 3 * z + y ** 2 * p, x * u ** 2 * z + y * q, x + x ** 2 * y + x ** 3 * z])
        d = sp.expand(F.jacobian([x, y, z]).det())
        P = sp.Poly(d, x, y, z)
        nonconst = [c for m, c in P.terms() if m != (0, 0, 0)]
        sol = sp.solve(nonconst, q1, dict=True)
        print("A: sympy %s; non-constant coefficients of det JF: %d; q1 making all of them vanish: %s" % (sp.__version__, len(nonconst), sol))
        q1v = sol[0][q1] if sol else None
        if q1v is not None:
            dv = sp.expand(d.subs(q1, q1v))
            print("A: with q1 = %s the determinant is %s" % (q1v, dv))
            Fv = F.subs(q1, q1v)
            print("A: total degrees of F1, F2, F3: %s" % [sp.Poly(sp.expand(f), x, y, z).total_degree() for f in Fv])
            print("A: F3 factors as %s" % sp.factor(Fv[2]))
            q1f = Fr(int(q1v.p), int(q1v.q))
        else:
            q1f = Fr(-2, 3)
    except ImportError:
        print("A: sympy not installed; check A skipped")
        q1f = Fr(-2, 3)

    # ---------- check B ----------
    F = build(q1f)
    J = [[pdiff(f, v) for v in range(3)] for f in F]
    D = det3(J)
    print("B: q1 = %s; det JF computed with own arithmetic has %d term(s): %s" % (q1f, len(D), D))
    print("B: degrees %s; number of terms %s" % ([max(sum(m) for m in f) for f in F], [len(f) for f in F]))
    # other values of q1 as a control: the determinant must stop being constant
    for bad in (Fr(-1, 2), Fr(0), Fr(-7, 9)):
        Fb = build(bad)
        Db = det3([[pdiff(f, v) for v in range(3)] for f in Fb])
        print("B control: q1 = %s gives a determinant with %d terms" % (bad, len(Db)))
    # two points with one image.  On x = 0 the map is (y, z) -> (z - (8/9) y^2 ..., y q(1), 0); the surface
    # 1 + x y + x^2 z = 0 is also sent into the plane w = 0.
    pt1 = (Fr(1), Fr(0), Fr(-1))
    img1 = tuple(peval(f, pt1) for f in F)
    print("B: F%s = %s" % (tuple(str(c) for c in pt1), tuple(str(c) for c in img1)))
    found = []
    # solve on x = 0 by hand: F(0, y, z) = (z + y^2 p(1), y q(1), 0)
    p1 = Fr(-2, 3) + Fr(-2, 9)
    qq1 = 1 + q1f - Fr(2, 9)
    if qq1 != 0:
        y0 = img1[1] / qq1
        z0 = img1[0] - y0 * y0 * p1
        pt2 = (Fr(0), y0, z0)
        img2 = tuple(peval(f, pt2) for f in F)
        print("B: F%s = %s" % (tuple(str(c) for c in pt2), tuple(str(c) for c in img2)))
        print("B: two different points, same image: %s" % (pt1 != pt2 and img1 == img2))
        found.append((pt1, pt2))
    # a small exhaustive hunt for more collisions among rational points with small entries
    vals = [Fr(a, b) for a in range(-3, 4) for b in (1, 2, 3)]
    vals = sorted(set(vals))
    seen = {}
    coll = 0
    for pt in product(vals, repeat=3):
        im = tuple(peval(f, pt) for f in F)
        if im in seen and seen[im] != pt:
            coll += 1
            if coll <= 3:
                print("B: collision %s and %s -> %s" % (tuple(map(str, seen[im])), tuple(map(str, pt)), tuple(map(str, im))))
        else:
            seen[im] = pt
    print("B: grid of %d points, %d collisions" % (len(vals) ** 3, coll))
    # the determinant at random rational points, from the evaluated Jacobian matrix (third way)
    import random
    rng = random.Random(3)
    ds = set()
    for _ in range(200):
        pt = tuple(Fr(rng.randint(-50, 50), rng.randint(1, 9)) for _ in range(3))
        M = [[peval(J[i][j], pt) for j in range(3)] for i in range(3)]
        dd = (M[0][0] * (M[1][1] * M[2][2] - M[1][2] * M[2][1]) - M[0][1] * (M[1][0] * M[2][2] - M[1][2] * M[2][0]) + M[0][2] * (M[1][0] * M[2][1] - M[1][1] * M[2][0]))
        ds.add(dd)
    print("B: determinant of the evaluated Jacobian at 200 random rational points takes the values %s" % sorted(map(str, ds)))


if __name__ == "__main__":
    main()
