"""Finite parts of arXiv 2610.17662 (Ivanov, zero divisors in odd characteristic), recomputed.

What is checked (all of it finite arithmetic; none of it is the geometric part of the proof):
  C1  Proposition 5.3: M phi <= theta phi entrywise, phi = (p+1, 1, 1), theta = 1 - 1/(4(q+1)), exactly, for
      every odd prime p < 1000 and q = p^3, p^4, p^5.
  C2  p = 3: PG(2, 27) built from F_27 = F_3[x]/(x^3 + 2x + 1); the type table of Construction 3.2 at n = 2 v^2;
      Lemma 3.3 (letter frequencies), Lemma 3.4 (cross-intersections), Lemma 5.1 (turn weights), Lemma 5.2
      (the 760 x 760 matrix lumps to the 3 x 3 matrix), and the two spectral radii.
  C3  Table 2 and Remark 5.4: spectral radius of the lumped matrix for p = 3, 5, 7, 11, 13 at q = p^3, at q = p
      (p = 3) and at q = p^2.
  C4  Lemma 2.2 on random instances with p = q = 3 (338 vertices a side, small girth, no group claimed): every
      component of the step graph has signed degree sum 0 and signed vertex count divisible by 3.
      Controls: a non-bipartite first graph, and a design with one extra letter in place of three.
"""
import random
import sys
import time
from fractions import Fraction

import numpy as np


def primes_below(n):
    s = bytearray([1]) * n
    s[0:2] = b"\0\0"
    for i in range(2, int(n ** 0.5) + 1):
        if s[i]:
            s[i * i::i] = bytearray(len(s[i * i::i]))
    return [i for i in range(n) if s[i]]


def lumped(p, q):
    v = q * q + q + 1
    a = Fraction(1, (q + 1) ** 2)
    b = Fraction(q + 1, v) ** 2
    return [[b * p, Fraction(p - 1), b * (v - p)],
            [a * (p - 1), b * p, a * (v - p)],
            [a * p, b * p, a * (v - p - 1)]]


def rho(M):
    return max(abs(np.linalg.eigvals(np.array([[float(x) for x in r] for r in M]))))


def test_vector_ok(p, q):
    M = lumped(p, q)
    phi = [Fraction(p + 1), Fraction(1), Fraction(1)]
    theta = 1 - Fraction(1, 4 * (q + 1))
    return all(sum(M[i][j] * phi[j] for j in range(3)) <= theta * phi[i] for i in range(3))


def field(p, k, low=None):
    """Addition and multiplication tables of F_{p^k}; low = coefficients c_0..c_{k-1} with x^k = sum c_i x^i."""
    q = p ** k
    if k == 1:
        return q, [[(a + b) % p for b in range(q)] for a in range(q)], [[(a * b) % p for b in range(q)] for a in range(q)]
    dec = [[(n // p ** i) % p for i in range(k)] for n in range(q)]
    enc = lambda c: sum(ci * p ** i for i, ci in enumerate(c))
    add = [[enc([(x + y) % p for x, y in zip(dec[a], dec[b])]) for b in range(q)] for a in range(q)]
    mul = [[0] * q for _ in range(q)]
    for a in range(q):
        for b in range(q):
            prod = [0] * (2 * k - 1)
            for i, x in enumerate(dec[a]):
                for j, y in enumerate(dec[b]):
                    prod[i + j] += x * y
            for d in range(2 * k - 2, k - 1, -1):
                c = prod[d] % p
                prod[d] = 0
                for i in range(k):
                    prod[d - k + i] += c * low[i]
            mul[a][b] = enc([x % p for x in prod[:k]])
    assert all(1 in mul[a] for a in range(1, q)), "not a field"
    return q, add, mul


def plane(q, add, mul):
    """Incidence matrix of PG(2, q): rows lines, columns points."""
    pts = [(1, a, b) for a in range(q) for b in range(q)] + [(0, 1, a) for a in range(q)] + [(0, 0, 1)]
    v = len(pts)
    inc = np.zeros((v, v), dtype=np.int64)
    for i, l in enumerate(pts):
        for j, x in enumerate(pts):
            if add[add[mul[l[0]][x[0]]][mul[l[1]][x[1]]]][mul[l[2]][x[2]]] == 0:
                inc[i, j] = 1
    assert (inc.sum(axis=1) == q + 1).all() and (inc.sum(axis=0) == q + 1).all()
    assert (inc @ inc.T == q * np.eye(v, dtype=np.int64) + 1).all(), "two lines do not meet in one point"
    return inc


def alphabet(v, ne):
    """Letters 0..v-1 points, v..v+ne-1 extras; involution: extra i <-> point i, other points paired in order."""
    bar = list(range(v + ne))
    for i in range(ne):
        bar[v + i], bar[i] = i, v + i
    rest = list(range(ne, v))
    assert len(rest) % 2 == 0
    for i in range(0, len(rest), 2):
        bar[rest[i]], bar[rest[i + 1]] = rest[i + 1], rest[i]
    assert all(bar[bar[t]] == t and bar[t] != t for t in range(v + ne))
    return bar


def check_c2(p=3):
    q, add, mul = field(3, 3, [2, 1, 0])  # x^3 = x + 2, that is x^3 + 2x + 1 = 0
    inc = plane(q, add, mul)
    v = inc.shape[0]
    nT = v + p
    bar = alphabet(v, p)
    # distinct types of B at n = 2 v^2: (line, with E) 2(q+1) times, (line, without E) 2v - 2(q+1) times
    Tm = np.zeros((2 * v, nT), dtype=np.int64)
    Tm[:v, :v] = inc
    Tm[:v, v:] = 1
    Tm[v:, :v] = inc
    mult = np.array([2 * (q + 1)] * v + [2 * v - 2 * (q + 1)] * v, dtype=np.int64)
    n = int(mult.sum())
    C = Tm.T @ (Tm * mult[:, None])
    freq = set(int(C[t, t]) for t in range(nT))
    cross = sorted(set(int(x) for x in np.unique(Tm @ Tm.T)))
    print("C2  PG(2,27): v = %d, |T| = %d, n = %d = 2v^2: %s" % (v, nT, n, n == 2 * v * v))
    print("C2  Lemma 3.3 letter frequency |B_t|: %s (f n = %s)" % (sorted(freq), Fraction(q + 1, v) * n))
    print("C2  Lemma 3.4 values of |S_x cap S_y| over all pairs of types: %s; all = 1 mod %d: %s" % (cross, p, all(c % p == 1 for c in cross)))
    d = freq.pop()
    weights = set()
    cls = ["E" if bar[t] >= v else ("S" if t >= v else "O") for t in range(nT)]
    L = lumped(p, q)
    order = {"E": 0, "S": 1, "O": 2}
    idx = {K: np.array([u for u in range(nT) if cls[u] == K]) for K in order}
    lump_ok = True
    Mfull = np.zeros((nT, nT))
    for t in range(nT):
        row = C[bar[t]].copy()
        row[bar[t]] = 0
        weights |= set(Fraction(int(x), d) for x in np.unique(row))
        Mfull[t] = (row / d) ** 2
        for K in order:
            s = Fraction(int((row[idx[K]] ** 2).sum()), d * d)
            if s != L[order[cls[t]]][order[K]]:
                lump_ok = False
    print("C2  Lemma 5.1 turn weights met: %s" % sorted(weights))
    print("C2  Lemma 5.2 class sizes E %d S %d O %d; every row of the 760 x 760 matrix lumps to the 3 x 3 matrix exactly: %s" % (
        cls.count("E"), cls.count("S"), cls.count("O"), lump_ok))
    print("C2  spectral radius: full matrix %.6f, lumped %.6f" % (max(abs(np.linalg.eigvals(Mfull))), rho(L)))


def sample(q, p, ne, inc, rng, bipartite=True):
    """Random graphs of the shape of Constructions 3.2 and 4.1 at n = 2 v^2.  Returns types and out-maps."""
    v = inc.shape[0]
    bar = alphabet(v, ne)
    lines = [frozenset(int(j) for j in np.nonzero(inc[i])[0]) for i in range(v)]
    E = frozenset(range(v, v + ne))

    def types(m):
        out = []
        per, withE = m // v, m * (q + 1) // (v * v)
        assert per * v == m and withE * v * v == m * (q + 1)
        for l in lines:
            out += [l | E] * withE + [l] * (per - withE)
        return out

    n = 2 * v * v
    SA = types(n // 2) + types(n // 2)       # A+ = 0..n/2-1, A- = n/2..n-1
    SB = types(n)
    eps = [1] * (n // 2) + [-1] * (n // 2)
    outA = [dict() for _ in range(n)]
    outB = [dict() for _ in range(n)]

    def match(src, dst, out, t):
        assert len(src) == len(dst), "frequencies differ"
        dst = dst[:]
        rng.shuffle(dst)
        for x, y in zip(src, dst):
            assert t not in out[x] and bar[t] not in out[y]
            out[x][t] = y
            out[y][bar[t]] = x

    for t in range(v + ne):
        if t > bar[t]:
            continue
        match([x for x in range(n) if t in SB[x]], [x for x in range(n) if bar[t] in SB[x]], outB, t)
        if bipartite:
            match([x for x in range(n // 2) if t in SA[x]], [x for x in range(n // 2, n) if bar[t] in SA[x]], outA, t)
            match([x for x in range(n // 2, n) if t in SA[x]], [x for x in range(n // 2) if bar[t] in SA[x]], outA, t)
        else:
            match([x for x in range(n) if t in SA[x]], [x for x in range(n) if bar[t] in SA[x]], outA, t)
    assert all(set(outA[x]) == set(SA[x]) for x in range(n)) and all(set(outB[x]) == set(SB[x]) for x in range(n))
    return n, SA, SB, eps, outA, outB


def step_graph(n, SA, SB, eps, outA, outB, p):
    parent = list(range(n * n))

    def find(a):
        while parent[a] != a:
            parent[a] = parent[parent[a]]
            a = parent[a]
        return a

    deg = [0] * (n * n)
    for x in range(n):
        for y in range(n):
            com = SA[x] & SB[y]
            deg[x * n + y] = len(com)
            for t in com:
                ra, rb = find(x * n + y), find(outA[x][t] * n + outB[y][t])
                if ra != rb:
                    parent[ra] = rb
    size, cnt, dsum = {}, {}, {}
    for x in range(n):
        for y in range(n):
            r = find(x * n + y)
            size[r] = size.get(r, 0) + 1
            cnt[r] = cnt.get(r, 0) + eps[x]
            dsum[r] = dsum.get(r, 0) + eps[x] * deg[x * n + y]
    comps = len(size)
    big = sorted(size, key=lambda r: -size[r])[:3]
    return dict(comps=comps,
                size_not_0=sum(1 for r in size if size[r] % p),
                handshake_fail=sum(1 for r in dsum if dsum[r] != 0),
                signed_not_0_mod_p=sum(1 for r in cnt if cnt[r] % p),
                signed_nonzero=sum(1 for r in cnt if cnt[r] != 0),
                largest=[(size[r], cnt[r]) for r in big],
                degs=sorted(set(deg)))


def main():
    t0 = time.time()
    # C1
    bad = [(p, k) for p in primes_below(1000) if p > 2 for k in (3, 4, 5) if not test_vector_ok(p, p ** k)]
    print("C1  M phi <= theta phi, odd primes p < 1000 (%d of them), q = p^3, p^4, p^5: failures %d" % (len(primes_below(1000)) - 1, len(bad)))
    # C2
    check_c2()
    # C3
    for p in (3, 5, 7, 11, 13):
        r3, r2 = rho(lumped(p, p ** 3)), rho(lumped(p, p ** 2))
        print("C3  p = %2d: q = p^3: rho %.5f, 1 - rho %.2e, 1/(4Q) %.2e | q = p^2: rho %.5f, test vector holds: %s" % (
            p, r3, 1 - r3, 1 / (4 * (p ** 3 + 1)), r2, test_vector_ok(p, p ** 2)))
    print("C3  p = 3, q = p: rho %.4f" % rho(lumped(3, 3)))
    # C4
    q, add, mul = field(3, 1)
    inc = plane(q, add, mul)
    for seed in (1, 2, 3):
        r = step_graph(*sample(3, 3, 3, inc, random.Random(seed)), p=3)
        print("C4  seed %d: %d components; size not 0 mod 3: %d; signed degree sum nonzero: %d; signed count not 0 mod 3: %d; signed count nonzero over Z: %d; largest (size, signed count): %s; degrees %s" % (
            seed, r["comps"], r["size_not_0"], r["handshake_fail"], r["signed_not_0_mod_p"], r["signed_nonzero"], r["largest"], r["degs"]))
    r = step_graph(*sample(3, 3, 3, inc, random.Random(1), bipartite=False), p=3)
    print("C4  control, first graph not bipartite: %d components; signed degree sum nonzero: %d; signed count not 0 mod 3: %d" % (
        r["comps"], r["handshake_fail"], r["signed_not_0_mod_p"]))
    r = step_graph(*sample(3, 3, 1, inc, random.Random(1)), p=3)
    print("C4  control, one extra letter (degrees %s): %d components; signed degree sum nonzero: %d; signed count not 0 mod 3: %d" % (
        r["degs"], r["comps"], r["handshake_fail"], r["signed_not_0_mod_p"]))
    print("time %.1f s" % (time.time() - t0))


if __name__ == "__main__":
    main()
