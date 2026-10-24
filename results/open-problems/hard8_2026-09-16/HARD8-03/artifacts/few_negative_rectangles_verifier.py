"""Exact sanity-checker for the HARD8-03 few-negative-rectangles lemma.

Given a signed rectangle decomposition

    M = sum_i 1_{A_i x B_i} - sum_j 1_{C_j x D_j}

whose resulting matrix M is Boolean, the accompanying report proves that if
there are a positive and b negative rectangles, then the 1-entries of M admit
a disjoint rectangle partition of size at most

    sum_{q=0}^b binom(b,q) 2^(b-q) binom(a,q+1)
    <= a (a+2)^b.

This script implements the constructive proof using the 3^b ternary blocks
induced by the negative rectangles and checks exact coverage/disjointness.
It uses integer arithmetic only.
"""

from itertools import combinations, product
import random


def signed_matrix(m, n, positives, negatives):
    M = [[0 for _ in range(n)] for _ in range(m)]
    for A, B in positives:
        for x in A:
            for y in B:
                M[x][y] += 1
    for C, D in negatives:
        for x in C:
            for y in D:
                M[x][y] -= 1
    return M


def ternary_blocks(m, n, negatives):
    """Partition X x Y into at most 3^b rectangles.

    For negative rectangle C_j x D_j, a cell (x,y) receives state
      0 if x notin C_j,
      1 if x in C_j and y notin D_j,
      2 if x in C_j and y in D_j.
    State 2 is exactly 'negative rectangle j is active'.
    """
    b = len(negatives)
    for sigma in product(range(3), repeat=b):
        X = []
        for x in range(m):
            ok = True
            for j, (C, D) in enumerate(negatives):
                if sigma[j] == 0 and x in C:
                    ok = False
                    break
                if sigma[j] in (1, 2) and x not in C:
                    ok = False
                    break
            if ok:
                X.append(x)

        Y = []
        for y in range(n):
            ok = True
            for j, (C, D) in enumerate(negatives):
                if sigma[j] == 1 and y in D:
                    ok = False
                    break
                if sigma[j] == 2 and y not in D:
                    ok = False
                    break
                # sigma[j] == 0 imposes no condition on y.
            if ok:
                Y.append(y)

        if X and Y:
            yield sigma, tuple(X), tuple(Y)


def construct_one_partition(m, n, positives, negatives):
    """Construct the disjoint positive rectangle partition from the proof."""
    parts = []
    for sigma, X, Y in ternary_blocks(m, n, negatives):
        q = sum(s == 2 for s in sigma)
        if q + 1 > len(positives):
            continue
        X0, Y0 = set(X), set(Y)
        for chosen in combinations(range(len(positives)), q + 1):
            XX, YY = set(X0), set(Y0)
            for i in chosen:
                A, B = positives[i]
                XX.intersection_update(A)
                YY.intersection_update(B)
            if XX and YY:
                parts.append((tuple(sorted(XX)), tuple(sorted(YY)), sigma, chosen))
    return parts


def verify(m, n, positives, negatives):
    M = signed_matrix(m, n, positives, negatives)
    assert all(v in (0, 1) for row in M for v in row), "decomposition is not Boolean"

    parts = construct_one_partition(m, n, positives, negatives)
    cover = [[0 for _ in range(n)] for _ in range(m)]
    for X, Y, _, _ in parts:
        for x in X:
            for y in Y:
                cover[x][y] += 1

    assert cover == M, "constructed rectangles fail exact disjoint coverage"

    a, b = len(positives), len(negatives)
    exact_bound = sum(
        _binom(b, q) * (2 ** (b - q)) * _binom(a, q + 1)
        for q in range(b + 1)
    )
    coarse_bound = a * ((a + 2) ** b) if a else 0
    assert len(parts) <= exact_bound <= coarse_bound
    return len(parts), exact_bound, coarse_bound


def _binom(n, k):
    if k < 0 or k > n:
        return 0
    if k == 0 or k == n:
        return 1
    k = min(k, n - k)
    out = 1
    for j in range(1, k + 1):
        out = out * (n - k + j) // j
    return out


def random_nonempty_subset(size, rng):
    while True:
        S = {i for i in range(size) if rng.randrange(2)}
        if S:
            return S


def random_rectangle(m, n, rng):
    return random_nonempty_subset(m, rng), random_nonempty_subset(n, rng)


def guaranteed_boolean_case(m, n, b, rng):
    """Build a Boolean target and a signed decomposition of it.

    We first choose the target M and b arbitrary negative rectangles.  Then for
    each cell we add as many positive singleton rectangles as needed so that
    positive multiplicity minus negative multiplicity equals M[x][y].
    """
    target = [[rng.randrange(2) for _ in range(n)] for _ in range(m)]
    negatives = [random_rectangle(m, n, rng) for _ in range(b)]

    neg_depth = [[0 for _ in range(n)] for _ in range(m)]
    for C, D in negatives:
        for x in C:
            for y in D:
                neg_depth[x][y] += 1

    positives = []
    for x in range(m):
        for y in range(n):
            multiplicity = target[x][y] + neg_depth[x][y]
            positives.extend([({x}, {y})] * multiplicity)
    return positives, negatives


def main():
    rng = random.Random(20260916)
    checked = 0
    for b in range(4):
        for _ in range(250):
            positives, negatives = guaranteed_boolean_case(4, 5, b, rng)
            verify(4, 5, positives, negatives)
            checked += 1
    print(f"verified {checked} exact Boolean signed decompositions")


if __name__ == "__main__":
    main()
