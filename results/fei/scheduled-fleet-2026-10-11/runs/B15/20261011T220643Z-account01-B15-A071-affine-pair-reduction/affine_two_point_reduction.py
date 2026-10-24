#!/usr/bin/env python3
"""Exact A071 audit of signed affine two-point conditional cells.

The calculation proves the finite classification used in REPORT.md:
among all signed two-point cells in F_2^4, a normalized squared Walsh law is
product iff the two points form a coordinate edge.  It also independently
checks all eight relative-sign choices on the archived 40/17 witness.
"""

from collections import Counter
from fractions import Fraction
from itertools import combinations, product

M = 4
N = 1 << M


def parity(x: int) -> int:
    return x.bit_count() & 1


def chi(s: int, x: int) -> int:
    return -1 if parity(s & x) else 1


def walsh(values: list[int]) -> list[int]:
    return [sum(values[x] * chi(s, x) for x in range(len(values))) for s in range(len(values))]


def is_product_squared(w: list[int], bits: int) -> bool:
    q = [z * z for z in w]
    total = sum(q)
    if total == 0:
        return False
    marg = []
    for i in range(bits):
        one = sum(q[s] for s in range(1 << bits) if (s >> i) & 1)
        marg.append((total - one, one))
    scale = total ** (bits - 1)
    for s, qs in enumerate(q):
        rhs = 1
        for i in range(bits):
            rhs *= marg[i][(s >> i) & 1]
        if qs * scale != rhs:
            return False
    return True


def signed_cell(u: int, v: int, eps: int) -> list[int]:
    h = [0] * N
    h[u] = 1
    h[v] = eps
    return h


def conditional_degree(w: list[int]) -> Fraction:
    q = [z * z for z in w]
    total = sum(q)
    return Fraction(sum(s.bit_count() * q[s] for s in range(N)), total)


def full_table(g: list[int], edges: tuple[tuple[int, int], ...], signs: tuple[int, ...]) -> list[int]:
    data = {}
    for a, ((u, v), eps) in enumerate(zip(edges, signs), start=1):
        data[u] = (a, 1)
        data[v] = (a, eps)
    out = []
    for x in range(N):
        for y in range(4):
            if g[x]:
                value = g[x]
            else:
                a, t = data[x]
                value = t * chi(a, y)
            assert value in (-1, 1)
            out.append(value)
    return out


def full_metrics(table: list[int]) -> tuple[Fraction, Fraction, Counter]:
    assert len(table) == 64
    w = [sum(table[x] * chi(s, x) for x in range(64)) for s in range(64)]
    assert sum(z * z for z in w) == 64 * 64
    qhist = Counter(z * z for z in w if z)
    # In this family all nonzero masses are dyadic with q in {16,64,256,...};
    # compute entropy exactly as sum (q/4096)*(12-log2(q)).
    H = Fraction(0)
    for q, mult in qhist.items():
        assert q > 0 and q & (q - 1) == 0
        H += mult * Fraction(q, 4096) * (12 - (q.bit_length() - 1))
    I = Fraction(sum(s.bit_count() * z * z for s, z in enumerate(w)), 4096)
    return H, I, qhist


def main() -> None:
    total = product_count = 0
    product_constant = product_alternating = 0
    direction_hist = Counter()
    degree_hist = Counter()
    for u, v in combinations(range(N), 2):
        d = u ^ v
        for eps in (1, -1):
            total += 1
            w = walsh(signed_cell(u, v, eps))
            prod = is_product_squared(w, M)
            predicted = d.bit_count() == 1
            assert prod == predicted
            if not prod:
                continue
            product_count += 1
            direction_hist[d] += 1
            nonzero = [z * z for z in w if z]
            assert len(nonzero) == 8 and set(nonzero) == {4}
            deg = conditional_degree(w)
            expected = Fraction(3, 2) if eps == 1 else Fraction(5, 2)
            assert deg == expected
            degree_hist[deg] += 1
            if eps == 1:
                product_constant += 1
            else:
                product_alternating += 1

    assert total == 240
    assert product_count == 64
    assert product_constant == product_alternating == 32

    # Archived maximizing residual and its edge partition.
    g = [1, -1, -1, 0, -1, 0, 0, 1, -1, -1, -1, 0, -1, 0, 0, 1]
    edges = ((3, 11), (5, 13), (6, 14))
    signature_counts = Counter()
    for signs in product((1, -1), repeat=3):
        k = sum(eps == -1 for eps in signs)
        table = full_table(g, edges, signs)
        H, I, qhist = full_metrics(table)
        assert H == 5
        assert I == Fraction(17 + k, 8)
        signature_counts[(k, H, I, tuple(sorted(qhist.items())))] += 1

    assert [sum(v for (k, *_), v in signature_counts.items() if k == j) for j in range(4)] == [1, 3, 3, 1]

    print("B15 A071 signed affine two-point classification")
    print(f"all_signed_two_point_cells={total}")
    print(f"product_squared_cells={product_count}")
    print(f"product_constant_cells={product_constant}")
    print(f"product_alternating_cells={product_alternating}")
    print("product_direction_histogram=", dict(sorted(direction_hist.items())), sep="")
    print("conditional_degree_histogram=", {str(k): v for k, v in sorted(degree_hist.items())}, sep="")
    print("archived_witness_signed_extensions=")
    for (k, H, I, qhist), count in sorted(signature_counts.items()):
        print(f"  alternating={k} count={count} H={H} I={I} H_over_I={H/I} qhist={dict(qhist)}")
    print("PROVED_BY_EXHAUSTION: product iff coordinate-edge direction")
    print("PROVED_BY_EXHAUSTION: alternating sign adds exactly 1/8 influence per edge")
    print("ALL_EXACT_ASSERTIONS_PASS")


if __name__ == "__main__":
    main()
