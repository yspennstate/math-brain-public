"""Independent finite bookkeeping checks for the multi-order centered FEI proof.

All derivative, support, character-shift, and Fourier-domination checks below
use integers or Fractions. They do not prove the all-dimensional entropy bound.
"""
from fractions import Fraction
from itertools import combinations
import json
import random


def transform(values):
    """Unnormalized Fourier coefficients for physical signs x_j=2 bit_j-1."""
    a = list(values)
    width = 1
    while width < len(a):
        for start in range(0, len(a), 2 * width):
            for j in range(width):
                u, v = a[start + j], a[start + j + width]
                a[start + j], a[start + j + width] = u + v, u - v
        width *= 2
    return [v * (-1 if mask.bit_count() % 2 else 1)
            for mask, v in enumerate(a)]


def signs(mask, n):
    return [1 if mask >> j & 1 else -1 for j in range(n)]


def character(mask, subset, n):
    return -1 if ((~mask) & subset & ((1 << n) - 1)).bit_count() % 2 else 1


def insert_bit(mask, i, value):
    low = mask & ((1 << i) - 1)
    high = mask >> i
    return low | (value << i) | (high << (i + 1))


def derivative(table, i):
    return [(table[insert_bit(y, i, 1)] -
             table[insert_bit(y, i, 0)]) // 2
            for y in range(len(table) // 2)]


def antichain_support(piece, pivot, order, orientation, n):
    predecessors = order[:order.index(pivot)]
    pred_set = set(predecessors)
    other = [j for j in range(n) if j != pivot and j not in pred_set]
    fibers = {}
    for reduced_mask, val in enumerate(piece):
        if val == 0:
            continue
        full_mask = insert_bit(reduced_mask, pivot, 0)
        x = signs(full_mask, n)
        key = tuple(x[j] for j in other)
        pattern = sum((1 << k) for k, j in enumerate(predecessors)
                      if x[j] * orientation[j] == 1)
        fibers.setdefault(key, []).append(pattern)
    comparisons = 0
    for patterns in fibers.values():
        for p, q in combinations(patterns, 2):
            assert p != q
            assert p & q != p and p & q != q
            comparisons += 1
    return comparisons


def main():
    rng = random.Random(20261011)
    counters = dict(families=0, nonconstant=0, character_coefficients=0,
                    pivots=0, modulated_pieces=0, antichain_pairs=0,
                    exact_domination_checks=0, high_influence_coordinates=0)
    for case in range(96):
        n = 3 + case % 5
        m = 1 + (case // 5) % 4
        N = 1 << n
        weights = [[rng.choice([-5, -3, -2, -1, 1, 2, 3, 5])
                    for _ in range(n)] for _ in range(m)]
        if case % 3 == 0:
            weights = [weights[0][:] for _ in range(m)]
        thresholds = [rng.randint(-7, 7) + Fraction(1, 2)
                      for _ in range(m)]
        gates = []
        for w, threshold in zip(weights, thresholds):
            gates.append([1 if sum(a * b for a, b in zip(w, signs(x, n)))
                           > threshold else -1 for x in range(N)])
        outer = [rng.choice([-1, 1]) for _ in range(1 << m)]
        g = [outer[sum((gates[l][x] == 1) << l for l in range(m))]
             for x in range(N)]
        dg = [derivative(g, i) for i in range(n)]
        alpha_numer = [sum(v * v for v in d) for d in dg]
        U = sum((1 << i) for i, count in enumerate(alpha_numer)
                if 2 * count > N // 2)
        b = U.bit_count()
        assert b < 4 * m * m
        h = [character(x, U, n) * g[x] for x in range(N)]
        hg, hh = transform(g), transform(h)
        for S in range(N):
            assert hh[S] == hg[S ^ U]
            counters["character_coefficients"] += 1
        Ih_num = sum(sum(v * v for v in derivative(h, i)) for i in range(n))
        assert Ih_num == sum(min(v, N // 2 - v) for v in alpha_numer)
        counters["families"] += 1
        counters["nonconstant"] += len(set(g)) > 1
        counters["high_influence_coordinates"] += b
        for i in range(n):
            if U >> i & 1 or alpha_numer[i] == 0:
                continue
            counters["pivots"] += 1
            dh = derivative(h, i)
            gate_derivatives = [derivative(t, i) for t in gates]
            pieces = [[0] * (N // 2) for _ in range(m)]
            for y, val in enumerate(dg[i]):
                if val:
                    owner = next(l for l in range(m) if gate_derivatives[l][y])
                    full_mask = insert_bit(y, i, 0)
                    pieces[owner][y] = character(full_mask, U, n) * val
            assert [sum(p[y] for p in pieces) for y in range(N // 2)] == dh
            nonzero = []
            for l, piece in enumerate(pieces):
                norm = sum(v * v for v in piece)
                if norm == 0:
                    continue
                order = sorted(range(n), key=lambda j: (-abs(weights[l][j]), j))
                orientation = [1 if w > 0 else -1 for w in weights[l]]
                counters["antichain_pairs"] += antichain_support(
                    piece, i, order, orientation, n)
                nonzero.append((transform(piece), norm))
                counters["modulated_pieces"] += 1
            assert sum(norm for _, norm in nonzero) == alpha_numer[i]
            dhat = transform(dh)
            for T in range(N // 2):
                lhs = Fraction(dhat[T] ** 2, alpha_numer[i])
                rhs = sum((Fraction(phat[T] ** 2, norm)
                           for phat, norm in nonzero), Fraction(0))
                assert lhs <= rhs
                counters["exact_domination_checks"] += 1
    print(json.dumps({"status": "PASS", "scope": "finite exact bookkeeping",
                      **counters}, indent=2))


if __name__ == "__main__":
    main()
