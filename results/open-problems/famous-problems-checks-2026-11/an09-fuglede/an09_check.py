"""Exact finite checks of the two 60-point sets of arXiv 2607.15632 in G = Z60 x Z12.

Everything is recomputed from the explicit formulas (23), (24), (30) and the displayed formula for A+,
in G coordinates.  Character sums are tested for zero exactly, in Z[x]/(Phi_N(x)); a floating-point value
is computed beside it and the two tests must agree.

Tile, not spectral (A-):
  T1  A- + T- = G, |A-| = 60, |T-| = 12.
  T2  Z = zero set of the Fourier transform of 1_{A-} on the dual of G.  S = {(a, b): 5 | a} has index 5.
      A spectrum has 60 points, so 12 of them lie in one coset of S and their differences lie in Z and S.
      The largest clique of Cay(S, Z cap S) is computed exhaustively; below 12 means A- has no spectrum.
Spectral, not tile (A+):
  S1  Lambda+ is a spectrum of A+: |A+| = |Lambda+| = 60 and all nonzero differences lie in Z(A+).
  S2  A+ + T = G with |T| = 12 iff (T - T) meets (A+ - A+) only in 0.  The largest clique of
      Cay(G, G minus (A+ - A+)) is computed exhaustively; below 12 means A+ does not tile G.
Controls (the same search must find 12 where the paper says a set exists):
  C1  seed sets in H = Z12 x Z12: E is a common tiling complement of B0, B1, B2 (clique 12 expected), and
      they have no common spectrum (below 12 expected).
  C2  V0, V1, V2 have the common spectrum E (clique 12 expected) and no common tiling complement (below 12).
"""
import cmath
import itertools
import sys
import time

sys.setrecursionlimit(10000)


def cyclotomic(n):
    """Phi_n as a list of integer coefficients, lowest degree first."""
    def polydiv(num, den):
        num = num[:]
        out = [0] * (len(num) - len(den) + 1)
        for i in range(len(num) - len(den), -1, -1):
            q = num[i + len(den) - 1] // den[-1]
            out[i] = q
            for j, d in enumerate(den):
                num[i + j] -= q * d
        assert not any(num), "inexact division"
        return out
    cache = {}
    def phi(m):
        if m in cache:
            return cache[m]
        p = [-1] + [0] * (m - 1) + [1]
        for d in range(1, m):
            if m % d == 0:
                p = polydiv(p, phi(d))
        cache[m] = p
        return p
    return phi(n)


class Group:
    """Z_n1 x Z_n2 with the pairing <(a,b),(x,y)> = a x / n1 + b y / n2."""
    def __init__(self, n1, n2):
        self.n1, self.n2 = n1, n2
        self.N = n1 * n2 // __import__("math").gcd(n1, n2)
        self.s1, self.s2 = self.N // n1, self.N // n2
        self.phi = cyclotomic(self.N)
        self.deg = len(self.phi) - 1
        self.elems = [(a, b) for a in range(n1) for b in range(n2)]
        self.roots = [cmath.exp(2j * cmath.pi * k / self.N) for k in range(self.N)]

    def norm(self, p):
        return (p[0] % self.n1, p[1] % self.n2)

    def sub(self, p, q):
        return ((p[0] - q[0]) % self.n1, (p[1] - q[1]) % self.n2)

    def add(self, p, q):
        return ((p[0] + q[0]) % self.n1, (p[1] + q[1]) % self.n2)

    def hat_is_zero(self, A, xi):
        c = [0] * self.N
        for (x, y) in A:
            c[(xi[0] * x * self.s1 + xi[1] * y * self.s2) % self.N] += 1
        # exact: reduce sum c[k] x^k modulo Phi_N
        r = c[:]
        for i in range(self.N - 1, self.deg - 1, -1):
            q = r[i]
            if q:
                for j, d in enumerate(self.phi):
                    r[i - self.deg + j] -= q * d
        exact = not any(r[: self.deg])
        val = sum(c[k] * self.roots[k] for k in range(self.N))
        approx = abs(val) < 1e-7
        assert exact == approx, ("exact and floating tests disagree", xi, val)
        return exact

    def zero_set(self, A):
        return {xi for xi in self.elems if xi != (0, 0) and self.hat_is_zero(A, xi)}

    def diffs(self, A):
        return {self.sub(p, q) for p in A for q in A}


def max_clique_cayley(verts, conn, sub, want=None):
    """Largest clique of the Cayley graph on `verts` (a subgroup) with symmetric connection set `conn`.
    By vertex transitivity a largest clique contains 0, so the search runs inside conn.
    Exhaustive branch and bound with a greedy colouring bound.  Returns (size, clique, nodes)."""
    conn = sorted(conn)
    idx = {v: i for i, v in enumerate(conn)}
    n = len(conn)
    adj = [0] * n
    cs = set(conn)
    for i, v in enumerate(conn):
        m = 0
        for j, w in enumerate(conn):
            if i != j and sub(v, w) in cs:
                m |= 1 << j
        adj[i] = m
    for i in range(n):
        for j in range(n):
            assert ((adj[i] >> j) & 1) == ((adj[j] >> i) & 1), "connection set not symmetric"
    best = [0, []]
    nodes = [0]

    def colour_order(cand):
        order, bounds = [], []
        col = 0
        rest = cand
        while rest:
            col += 1
            q = rest
            while q:
                v = (q & -q).bit_length() - 1
                order.append(v)
                bounds.append(col)
                q &= ~adj[v]
                q &= ~(1 << v)
                rest &= ~(1 << v)
        return order, bounds

    def expand(cur, cand):
        nodes[0] += 1
        order, bounds = colour_order(cand)
        for k in range(len(order) - 1, -1, -1):
            if len(cur) + bounds[k] <= best[0]:
                return
            v = order[k]
            cur.append(v)
            nc = cand & adj[v]
            if nc:
                expand(cur, nc)
            elif len(cur) > best[0]:
                best[0], best[1] = len(cur), cur[:]
            cur.pop()
            cand &= ~(1 << v)
            if want is not None and best[0] + 1 >= want:
                return

    expand([], (1 << n) - 1)
    clique = [(0, 0)] + [conn[i] for i in best[1]]
    return best[0] + 1, clique, nodes[0]


def main():
    t0 = time.time()
    G = Group(60, 12)
    H = Group(12, 12)
    f = (0, 5, 0, 7, 9, 2, 10, 4, 7, 8, 10, 10)
    Z12, Z3, Z2 = range(12), range(3), range(2)

    # ---- explicit sets in G, from (23), (24), (30) and the display for A+
    Am = {G.norm((25 * x, 0)) for x in Z12}
    Am |= {G.norm((25 * x + 36 * t, -x)) for t in (3, 4) for x in Z12}
    Am |= {G.norm((25 * (3 * c + 4 * a) + 36 * t, 4 * a + 6 * b)) for t in (1, 2) for a in Z3 for b in Z2 for c in Z2}
    Tm = {G.norm((25 * f[y], y)) for y in Z12}
    H0 = {H.norm((4 * k, 2 * k)) for k in range(12)}
    V2 = H0 | {H.add((1, 2), h) for h in H0}
    Ap = {G.norm((36 * t, k)) for t in (0, 1, 2) for k in Z12}
    Ap |= {G.norm((25 * k + 24, k)) for k in Z12}
    Ap |= {G.norm((25 * u + 48, v)) for (u, v) in V2}
    Lp = {G.norm((5 * f[y] + 12 * r, y)) for y in Z12 for r in range(5)}
    print("sizes  |A-| %d  |T-| %d  |A+| %d  |Lambda+| %d  |H0| %d  |V2| %d" % (len(Am), len(Tm), len(Ap), len(Lp), len(H0), len(V2)))

    # ---- T1
    sums = [G.add(a, t) for a in Am for t in Tm]
    print("T1  A- + T- = G: %s (%d sums, %d distinct, |G| = %d)" % (len(set(sums)) == 720 and len(sums) == 720, len(sums), len(set(sums)), len(G.elems)))

    # ---- T2
    Zm = G.zero_set(Am)
    S = [(a, b) for (a, b) in G.elems if a % 5 == 0]
    ZmS = {z for z in Zm if z[0] % 5 == 0}
    size, cl, nodes = max_clique_cayley(S, ZmS, G.sub)
    print("T2  zeros of the transform of A-: %d of 719; in S (index 5, %d points): %d" % (len(Zm), len(S), len(ZmS)))
    print("T2  largest clique of Cay(S, Z cap S): %d (need 12 for a spectrum; %d search nodes)  -> A- spectral: %s" % (size, nodes, "not excluded" if size >= 12 else "NO"))
    print("T2  a largest clique:", sorted(cl))

    # ---- S1
    Zp = G.zero_set(Ap)
    bad = [(l, m) for l in Lp for m in Lp if l != m and G.sub(l, m) not in Zp]
    print("S1  Lambda+ spectrum of A+: %s (%d ordered pairs fail of %d)" % (not bad and len(Ap) == len(Lp) == 60, len(bad), 60 * 59))

    # ---- S2
    Dp = G.diffs(Ap)
    free = {g for g in G.elems if g not in Dp}
    size, cl, nodes = max_clique_cayley(G.elems, free, G.sub)
    print("S2  |A+ - A+| = %d of 720; complement %d" % (len(Dp), len(free)))
    print("S2  largest clique of Cay(G, G minus (A+ - A+)): %d (need 12 for a tiling; %d search nodes)  -> A+ tiles G: %s" % (size, nodes, "not excluded" if size >= 12 else "NO"))

    # ---- controls in H
    B0 = {(x, 0) for x in Z12}
    B1 = {H.norm((x, -x)) for x in Z12}
    B2 = {H.norm((3 * c + 4 * a, 4 * a + 6 * b)) for a in Z3 for b in Z2 for c in Z2}
    E = {(f[y], y) for y in Z12}
    V0 = {(0, k) for k in Z12}
    V1 = {(k, k) for k in Z12}
    for name, sets in (("B", (B0, B1, B2)), ("V", (V0, V1, V2))):
        assert all(len(s) == 12 for s in sets)
        dz = set(H.elems)
        zz = set(H.elems) - {(0, 0)}
        for s in sets:
            dz -= H.diffs(s)
            zz &= H.zero_set(s)
        s1, c1, n1 = max_clique_cayley(H.elems, dz, H.sub)
        s2, c2, n2 = max_clique_cayley(H.elems, zz, H.sub)
        print("C   %s0,%s1,%s2: largest common tiling complement %d (nodes %d); largest common orthogonal set %d (nodes %d)" % (name, name, name, s1, n1, s2, n2))
    ok_tile = all(len({H.add(e, b) for e in E for b in Bj}) == 144 for Bj in (B0, B1, B2))
    ok_spec = all(all(H.sub(p, q) in H.zero_set(Vj) for p in E for q in E if p != q) for Vj in (V0, V1, V2))
    print("C   E + Bj = H for j = 0, 1, 2: %s;  E is a spectrum of V0, V1, V2: %s" % (ok_tile, ok_spec))
    print("time %.1f s" % (time.time() - t0))


if __name__ == "__main__":
    main()
