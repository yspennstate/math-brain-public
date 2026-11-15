"""Second check of arXiv 2607.15632, built differently from an09_check.py.

Works in K = Z12 x Z12 x Z5 from the layer definitions (not from the explicit formulas in G), uses floating
character sums only, and replaces the clique search by a layered backtracking:
  - a 12-point set of frequencies with last coordinate 0 whose nonzero differences are zeros of the transform
    of A- has pairwise different first coordinates as soon as no zero has the form (0, v, 0); so it has exactly
    one point over each u in Z12 and is found, or excluded, by choosing v_u for u = 1..11 (v_0 = 0 by translation);
  - the same for a tiling complement of A+: T - T avoids A+ - A+, which contains H x (Z5 minus 0) and every
    (0, k, 0), so T sits in one layer and has one point over each first coordinate.
It also maps the layer sets through Phi(x, y, t) = (25x + 36t mod 60, y mod 12) and compares them with the
explicit formulas (23), (24), (30) of the paper.
"""
import cmath
import sys
import time

f = (0, 5, 0, 7, 9, 2, 10, 4, 7, 8, 10, 10)
W = [cmath.exp(2j * cmath.pi * k / 60) for k in range(60)]


def hat(A, u, v, r):
    return sum(W[(5 * u * x + 5 * v * y + 12 * r * t) % 60] for (x, y, t) in A)


def layered(ok):
    """ok(du, dv) -> True when the difference (du, dv) is allowed.  Count sets {(u, v_u)}, v_0 = 0, all
    pairwise differences allowed; return (number found, deepest level reached, nodes)."""
    found = [0]
    deepest = [1]
    nodes = [0]
    chosen = [0]

    def rec(u):
        nodes[0] += 1
        if u > deepest[0]:
            deepest[0] = u
        if u == 12:
            found[0] += 1
            return
        for v in range(12):
            if all(ok((u - w) % 12, (v - chosen[w]) % 12) and ok((w - u) % 12, (chosen[w] - v) % 12) for w in range(u)):
                chosen.append(v)
                rec(u + 1)
                chosen.pop()

    rec(1)
    return found[0], deepest[0], nodes[0]


def main():
    t0 = time.time()
    Z12 = range(12)
    B0 = {(x, 0) for x in Z12}
    B1 = {(x, (-x) % 12) for x in Z12}
    B2 = {((3 * c + 4 * a) % 12, (4 * a + 6 * b) % 12) for a in range(3) for b in range(2) for c in range(2)}
    E = {(f[y], y) for y in Z12}
    V0 = {(0, k) for k in Z12}
    V1 = {(k, k) for k in Z12}
    H0 = {((4 * k) % 12, (2 * k) % 12) for k in range(12)}
    V2 = H0 | {((1 + a) % 12, (2 + b) % 12) for (a, b) in H0}
    lay_m = {0: B0, 1: B2, 2: B2, 3: B1, 4: B1}
    lay_p = {0: V0, 1: V0, 2: V0, 3: V2, 4: V1}
    Am = {(x, y, t) for t in range(5) for (x, y) in lay_m[t]}
    Ap = {(x, y, t) for t in range(5) for (x, y) in lay_p[t]}
    Gam = {(x, y, r) for (x, y) in E for r in range(5)}
    print("sizes |A-| %d |A+| %d |Gamma| %d" % (len(Am), len(Ap), len(Gam)))

    # agreement with the explicit formulas in G
    def Phi(p):
        return ((25 * p[0] + 36 * p[2]) % 60, p[1] % 12)
    def Psi(p):
        return ((5 * p[0] + 12 * p[2]) % 60, p[1] % 12)
    Gm = {((25 * x) % 60, 0) for x in Z12} | {((25 * x + 36 * t) % 60, (-x) % 12) for t in (3, 4) for x in Z12} \
        | {((25 * (3 * c + 4 * a) + 36 * t) % 60, (4 * a + 6 * b) % 12) for t in (1, 2) for a in range(3) for b in range(2) for c in range(2)}
    Gp = {((36 * t) % 60, k) for t in (0, 1, 2) for k in Z12} | {((25 * k + 24) % 60, k) for k in Z12} | {((25 * u + 48) % 60, v) for (u, v) in V2}
    GL = {((5 * f[y] + 12 * r) % 60, y) for y in Z12 for r in range(5)}
    print("Phi(A-) equals (23): %s; Phi(A+) equals the display: %s; dual image of Gamma equals (30): %s" % (
        {Phi(p) for p in Am} == Gm, {Phi(p) for p in Ap} == Gp, {Psi(p) for p in Gam} == GL))

    # tile side
    cover = {((x + e[0]) % 12, (y + e[1]) % 12, t) for (x, y, t) in Am for e in E}
    print("(E x 0) + A- = K: %s" % (len(cover) == 720))
    zero0 = {(u, v): abs(hat(Am, u, v, 0)) < 1e-7 for u in Z12 for v in Z12}
    gap = min(abs(hat(Am, u, v, 0)) for u in Z12 for v in Z12 if not zero0[(u, v)])
    print("zeros of the transform of A- at last coordinate 0: %d of 143; smallest nonzero modulus %.3f; zeros with u = 0: %d" % (
        sum(zero0.values()), gap, sum(1 for v in Z12 if zero0[(0, v)])))
    n, deep, nodes = layered(lambda du, dv: zero0[(du, dv)])
    print("12-point orthogonal families in one fibre: %d (deepest level %d of 12, %d nodes) -> A- spectral: %s" % (n, deep, nodes, "possible" if n else "NO"))

    # spectral side
    bad = sum(1 for p in Gam for q in Gam if p != q and abs(hat(Ap, p[0] - q[0], p[1] - q[1], p[2] - q[2])) > 1e-7)
    print("Gamma is a spectrum of A+: %s (%d failing pairs)" % (bad == 0, bad))
    D = {((p[0] - q[0]) % 12, (p[1] - q[1]) % 12, (p[2] - q[2]) % 5) for p in Ap for q in Ap}
    cross = all((x, y, t) in D for x in Z12 for y in Z12 for t in range(1, 5))
    vert = all((0, k, 0) in D for k in Z12)
    print("A+ - A+ contains H x (Z5 minus 0): %s; contains every (0, k, 0): %s; |A+ - A+| = %d" % (cross, vert, len(D)))
    n, deep, nodes = layered(lambda du, dv: (du, dv, 0) not in D)
    print("12-point tiling complements of A+: %d (deepest level %d of 12, %d nodes) -> A+ tiles K: %s" % (n, deep, nodes, "possible" if n else "NO"))

    # positive controls for the layered search
    DB = set()
    for B in (B0, B1, B2):
        DB |= {((p[0] - q[0]) % 12, (p[1] - q[1]) % 12) for p in B for q in B}
    # E is a graph over the second coordinate (B0 forbids differences (x, 0)), so the layers are the second coordinate
    n, deep, nodes = layered(lambda dv, du: (du, dv) not in DB)
    print("control: common tiling complements of B0, B1, B2 through 0: %d (E is one of them: expected > 0)" % n)
    zV = {(u, v): all(abs(sum(W[(5 * u * x + 5 * v * y) % 60] for (x, y) in V)) < 1e-7 for V in (V0, V1, V2)) for u in Z12 for v in Z12}
    # the transform of V0 vanishes exactly off v = 0, so a common spectrum has distinct second coordinates
    n, deep, nodes = layered(lambda dv, du: zV[(du, dv)])
    print("control: common spectra of V0, V1, V2 through 0: %d (E - E(0) is one: expected > 0)" % n)
    print("time %.1f s" % (time.time() - t0))


if __name__ == "__main__":
    main()
