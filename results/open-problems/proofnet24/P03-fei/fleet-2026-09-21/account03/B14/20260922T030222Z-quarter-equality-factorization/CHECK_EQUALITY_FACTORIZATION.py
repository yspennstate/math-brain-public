#!/usr/bin/env python3
"""Exact structural classification for the arity-5 quarter-slice equality family.

The previously certified quarter-slice theorem establishes that among all
8-subsets A of Q_5 exactly 1920 essential cases attain
H(1-2 1_A)=6 I(1-2 1_A)-4, all with I=5/4 and H=7/2.

This checker independently constructs the full input-NPN orbit of one reported
equality support A0={0,1,2,3,4,5,8,10}, proves that the orbit has 1920 distinct
members, verifies exact Fourier data, and proves every orbit member lies in a
unique coordinate face. Hence the certified equality count plus this orbit
construction classifies the entire essential equality family.

No floating-point comparison decides any claim.
"""
from itertools import permutations, product
from fractions import Fraction

A0 = frozenset((0, 1, 2, 3, 4, 5, 8, 10))
B0 = frozenset((0, 1, 2, 3, 4, 5, 8, 10))


def walsh(A, n):
    N = 1 << n
    out = []
    for s in range(N):
        w = 0
        for x in range(N):
            fx = -1 if x in A else 1
            w += fx * (-1 if ((s & x).bit_count() & 1) else 1)
        out.append(w)
    return out


def exact_H_signature(W, n):
    N = 1 << n
    sig = {}
    H = Fraction(0)
    for w in W:
        if not w:
            continue
        a = abs(w)
        sig[a] = sig.get(a, 0) + 1
        q = Fraction(w * w, N * N)
        assert q.numerator & (q.numerator - 1) == 0
        assert q.denominator & (q.denominator - 1) == 0
        log_inv = ((q.denominator.bit_length() - 1)
                   - (q.numerator.bit_length() - 1))
        H += q * log_inv
    return sig, H


def exact_I(W, n):
    N = 1 << n
    return sum(Fraction(s.bit_count() * w * w, N * N)
               for s, w in enumerate(W))


def influences(A, n):
    vals = []
    for i in range(n):
        disagree = 0
        for x in range(1 << n):
            if (x >> i) & 1:
                continue
            if ((x in A) != ((x | (1 << i)) in A)):
                disagree += 1
        vals.append(Fraction(disagree, 1 << (n - 1)))
    return vals


def transform(A, n, perm, flips):
    out = set()
    for x in range(1 << n):
        z = 0
        for i in range(n):
            bit = ((x >> i) & 1) ^ flips[i]
            z |= bit << perm[i]
        if z in A:
            out.add(x)
    return frozenset(out)


def cofactor_count(A, n, Bmask):
    B = [i for i in range(n) if (Bmask >> i) & 1]
    C = [i for i in range(n) if not ((Bmask >> i) & 1)]
    rows = set()
    for zb in range(1 << len(B)):
        row = []
        for yc in range(1 << len(C)):
            x = 0
            for q, i in enumerate(B):
                if (zb >> q) & 1:
                    x |= 1 << i
            for q, i in enumerate(C):
                if (yc >> q) & 1:
                    x |= 1 << i
            row.append(x in A)
        rows.add(tuple(row))
    return len(rows)


def containing_faces(A, n):
    faces = []
    for i in range(n):
        bits = {(x >> i) & 1 for x in A}
        if len(bits) == 1:
            faces.append((i, next(iter(bits))))
    return faces


def main():
    # Base structural factorization A0={x4=0} intersect lift(B0).
    assert all(x < 16 for x in A0)
    assert len(B0) == 8
    assert A0 == frozenset(B0)

    W4 = walsh(B0, 4)
    sig4, H4 = exact_H_signature(W4, 4)
    I4 = exact_I(W4, 4)
    inf4 = influences(B0, 4)
    assert sig4 == {4: 8, 8: 2}
    assert H4 == 3
    assert I4 == Fraction(3, 2)
    assert all(v > 0 for v in inf4)

    # The four-bit factor is composition-prime: every nontrivial block has
    # at least three distinct cofactors, so it cannot be compressed to one bit.
    block_counts = {}
    for Bmask in range(1, 15):
        k = Bmask.bit_count()
        if 2 <= k <= 3:
            c = cofactor_count(B0, 4, Bmask)
            block_counts[Bmask] = c
            assert c >= 3

    W5 = walsh(A0, 5)
    sig5, H5 = exact_H_signature(W5, 5)
    I5 = exact_I(W5, 5)
    inf5 = influences(A0, 5)
    assert sig5 == {4: 16, 8: 4, 16: 2}
    assert H5 == Fraction(7, 2)
    assert I5 == Fraction(5, 4)
    assert 6 * I5 - 4 == H5
    assert all(v > 0 for v in inf5)
    assert containing_faces(A0, 5) == [(4, 0)]

    # Generate the complete input-NPN orbit: coordinate permutations and
    # literal flips preserve the quarter slice, exact H/I, and factorization.
    orbit = set()
    for perm in permutations(range(5)):
        for flips in product((0, 1), repeat=5):
            orbit.add(transform(A0, 5, perm, flips))
    assert len(orbit) == 1920

    face_hist = {(i, b): 0 for i in range(5) for b in (0, 1)}
    for A in orbit:
        faces = containing_faces(A, 5)
        assert len(faces) == 1
        face_hist[faces[0]] += 1
        assert len(A) == 8
    assert set(face_hist.values()) == {192}

    print("PASS")
    print("base_inner_signature", sig4)
    print("base_inner_H", H4)
    print("base_inner_I", I4)
    print("base_inner_influences", [str(x) for x in inf4])
    print("base_inner_composition_prime", True)
    print("base_inner_block_cofactor_counts", sorted(block_counts.items()))
    print("base_outer_signature", sig5)
    print("base_outer_H", H5)
    print("base_outer_I", I5)
    print("base_outer_influences", [str(x) for x in inf5])
    print("input_npn_orbit_size", len(orbit))
    print("unique_face_for_every_orbit_member", True)
    print("members_per_coordinate_literal_face", sorted(face_hist.items()))
    print("classification_logic", "peer equality count 1920 + distinct equality orbit 1920 => exhaustive")
    print("full_FEI", "OPEN_NOT_PROVED")


if __name__ == "__main__":
    main()
