#!/usr/bin/env python3
"""Small exact checks supporting REFEREE.md; no third-party dependencies."""
from fractions import Fraction
from itertools import product
from math import prod, log, pi
import hashlib
import random
import resource

# One process, matrices of order at most 11, at most 2^10 local candidate pairs.
# The sandbox rejects setrlimit; report measured peak RSS at completion instead.


def rank(a):
    rows = [sum((v & 1) << j for j, v in enumerate(row)) for row in a]
    pivots = {}
    for x in rows:
        while x:
            j = x.bit_length() - 1
            if j in pivots:
                x ^= pivots[j]
            else:
                pivots[j] = x
                break
    return len(pivots)


def mv(a, x):
    return [sum(v * w for v, w in zip(row, x)) % 2 for row in a]


def transpose(a):
    return [list(row) for row in zip(*a)]


def prime(p):
    return p >= 2 and all(p % d for d in range(2, int(p**0.5) + 1))


def bit(a, p):
    a %= p
    assert a
    return int(pow(a, (p - 1) // 2, p) == p - 1)


def matrix(q):
    a = [[0 if i == j else bit(q[j], q[i])
          for j in range(len(q))] for i in range(len(q))]
    for i, row in enumerate(a):
        row[i] = sum(row) % 2
    return a


def verify_identities(k, s):
    n = len(s)
    assert all(k[i][j] ^ k[j][i] == (s[i] * s[j] ^ (s[i] if i == j else 0))
               for i in range(n) for j in range(n))
    assert not any(mv(k, [1] * n))
    if sum(s) % 2:
        assert not any(mv(transpose(k), [1] * n))
        N = [[v ^ (s[i] if i == j else 0) for j, v in enumerate(row)]
             for i, row in enumerate(k)]
        for x in product(range(2), repeat=n):
            assert (not any(mv(N, x))) == (
                not any(mv(transpose(k), x)) and sum(a*b for a, b in zip(s, x)) % 2 == 0)


def actual_example(B, J, auxiliaries):
    beta, theta = prod(B), prod(J)
    n = prod(B + auxiliaries)
    assert beta % 8 == theta % 8 == 1
    assert beta % 3 == 2 and theta % 3 == 1
    assert all(prime(q) for q in B + J + auxiliaries)
    assert all(bit(theta, q) == 0 for q in B)
    assert all(bit(beta, q) == 0 for q in J)
    for extra in ([], J):
        q = B + auxiliaries + extra
        k = matrix(q)
        s = [bit(-1, p) for p in q]
        lam = [bit(3, p) for p in q]
        b = [int(p in B) for p in q]
        verify_identities(k, s)
        assert len(q) - rank(k) == 2
        assert not any(mv(k, b))
        assert rank([row + [v] for row, v in zip(k, lam)]) == rank(k) + 1
        l = prod(q)
        assert l % 4 == 3 and l % 3 == 2
        N = [[v ^ (s[i] if i == j else 0) for j, v in enumerate(row)]
             for i, row in enumerate(k)]
        solutions = []
        for delta in range(2):
            for u in product(range(2), repeat=len(q)):
                for v in product(range(2), repeat=len(q)):
                    if any(mv(N, v)) or sum((a ^ b) * c for a, b, c in zip(lam, s, v)) % 2:
                        continue
                    if all(a ^ (b*c) == delta*b for a, b, c in zip(mv(k, u), lam, v)):
                        solutions.append((delta, u, v))
        assert len(solutions) == 4
        assert all(d == 0 and not any(v) for d, u, v in solutions)
        print(f"actual beta={beta}, theta={theta}, n={n}, l={l}: "
              f"rank K={rank(k)}, normalized solutions={len(solutions)}")


def abstract_trial(b, j, rng):
    # B, I, q0, J in this order; C columns e_i+e_(b-1).
    i_count = b - 1
    q0 = b + i_count
    size = q0 + 1 + j
    B, I, J = list(range(b)), list(range(b, q0)), list(range(q0 + 1, size))
    s = [0] * size
    lam = [0] * size
    for indices, parity in ((B, 0), (J, 0)):
        if indices:
            for x in indices[:-1]:
                s[x] = rng.randrange(2)
            s[indices[-1]] = sum(s[x] for x in indices[:-1]) % 2 ^ parity
    for indices, parity in ((B, 1), (J, 0)):
        if indices:
            for x in indices[:-1]:
                lam[x] = rng.randrange(2)
            lam[indices[-1]] = sum(lam[x] for x in indices[:-1]) % 2 ^ parity
    s[q0] = lam[q0] = 1
    edges = [[0] * size for _ in range(size)]

    def setedge(x, y, val):
        edges[x][y] = val
        edges[y][x] = val ^ (s[x] * s[y])

    for indices in (B, J):
        for pos, x in enumerate(indices):
            for y in indices[pos + 1:]:
                setedge(x, y, rng.randrange(2))
    # A B-by-J block with zero row sums and reverse-column sums;
    # compatibility uses the zero s sums in both sets.
    if J:
        for x in B[:-1]:
            for y in J[:-1]:
                setedge(x, y, rng.randrange(2))
            setedge(x, J[-1], sum(edges[x][y] for y in J[:-1]) % 2)
        for y in J:
            val = sum(edges[y][x] for x in B[:-1]) % 2
            setedge(B[-1], y, val ^ (s[B[-1]] * s[y]))
        assert all(sum(edges[x][y] for y in J) % 2 == 0 for x in B)
        assert all(sum(edges[y][x] for x in B) % 2 == 0 for y in J)
    for col, idx in enumerate(I):
        for x in B:
            setedge(x, idx, int(x in (col, b - 1)))
    for x in B:
        setedge(x, q0, sum(edges[x][idx] for idx in I) % 2)
    for idx in I:
        setedge(idx, q0, 0)
        for y in J:
            setedge(idx, y, 0)
    a = [int(x in (0, q0)) for x in range(size)]

    def construct(indices):
        k = [[edges[x][y] for y in indices] for x in indices]
        for ii, row in enumerate(k):
            row[ii] = sum(row) % 2
        lb = [lam[x] for x in indices]
        av = [a[x] for x in indices]
        ks = [[val ^ (lb[ii] * av[jj]) for jj, val in enumerate(row)]
              for ii, row in enumerate(k)]
        kept = [ii for ii, x in enumerate(indices) if x != q0]
        deleted = [[ks[ii][jj] for jj in kept] for ii in kept]
        return k, lb, ks, deleted

    k0, _, _, m0 = construct(list(range(q0 + 1)))
    assert rank(m0) == len(m0)
    found = 0
    for choices in product(range(2), repeat=j):
        for y, val in zip(J, choices):
            setedge(y, q0, val)
        k, lb, ks, deleted = construct(list(range(size)))
        bvec = [int(x in B) for x in range(size)]
        assert not any(mv(k, bvec))
        assert not any(mv(ks, [1] * size))
        assert not any(mv(transpose(ks), [1] * size))
        if rank(deleted) == len(deleted):
            found += 1
            assert size - rank(k) == 2
            assert rank([row + [v] for row, v in zip(k, lb)]) == rank(k) + 1
    assert found


def main():
    # Discriminants and the two independent Riemann-Hurwitz calculations.
    root_differences = (1, 3, 4)
    poly_disc_coefficient = prod(x*x for x in root_differences)
    assert poly_disc_coefficient == 144
    assert 16 * poly_disc_coefficient == 2304
    area_over_2pi = Fraction(prod(p - 1 for p in (2, 3, 5, 7)), 6)
    genus = 1 + area_over_2pi / 2
    assert area_over_2pi == 8 and genus == 5
    assert 16 * (-2) + 5 * 8 == 2 * genus - 2
    print(f"discriminants: 144 l^6, 2304 l^6; area/(2pi)={area_over_2pi}, genus={genus}")
    for m, p in ((30, 7), (42, 5), (70, 3)):
        assert bit(-m, p) == 1
        print(f"embedding check: -{m} mod {p} = {(-m)%p}, nonsquare")
    # For squarefree negative d, discriminant is d if d=1 mod4, otherwise 4d.
    for m in (30, 42, 70, 105, 210):
        disc = -m if (-m) % 4 == 1 else -4*m
        assert all(disc % p == 0 or bit(-m, p) == 1
                   for p in (3, 5, 7))
        assert disc % 2 == 0  # 2 is ramified for all five fields.
        print(f"Q(sqrt(-{m})): fundamental discriminant {disc}")
    count = 0
    for l in (3, 7):
        for u in (1, 3, 5, 7):
            assert ((l + 2*u)*u*(u + 2*l) - l) % 8 == 0
            count += 1
    print(f"2-adic residue calculation: {count} cases")
    actual_example([17], [409], [19])
    actual_example([5, 13], [601], [37, 7])
    rng = random.Random(20261113)
    trials = 0
    for b in range(1, 5):
        for j in range(4):
            for _ in range(40):
                abstract_trial(b, j, rng)
                trials += 1
    print(f"abstract two-support construction: {trials} deterministic trials, all passed")
    # Recover the final polynomial exponent with the proof's a=2.
    a = 2
    assert 2 + 5 * 2 == 12             # g0 * deg_B^5
    assert 2 * a == 4 and 12 * a == 24 # dimension and source height
    assert 5 * (2*a) == 20            # dominant log-degree term g^5 log(g)
    print("height powers: N^12; g=O(M^4); hF(source)=O(M^24); "
          "log degree=O(M^20(1+log M)); final admissible exponent c=24")
    assert abs(log(pi) - log(2*pi*pi)/2 + log(2)/2) < 1e-14
    digest = hashlib.sha256(open('paper_c.txt', 'rb').read()).hexdigest()
    assert digest == '66c49b33aa151329eb8740f417638c0a2bcf122b12a07bfe53bee61165ac0517'
    print('input SHA-256 unchanged:', digest)
    print('peak resident bytes (macOS):', resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    assert resource.getrusage(resource.RUSAGE_SELF).ru_maxrss < 1024**3


if __name__ == '__main__':
    main()
