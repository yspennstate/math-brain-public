"""Affine partitions of F_2^a (points = integers 0..2^a-1, addition = XOR)."""
import itertools
import numpy as np


def linear_subspaces(a):
    """All linear subspaces of F_2^a as sorted tuples of vectors (ints)."""
    subs = {(0,)}
    frontier = [frozenset([0])]
    seen = {frozenset([0])}
    while frontier:
        new = []
        for V in frontier:
            for v in range(1, 1 << a):
                if v in V:
                    continue
                W = frozenset(list(V) + [u ^ v for u in V])
                if W not in seen:
                    seen.add(W)
                    new.append(W)
        frontier = new
    return [tuple(sorted(V)) for V in seen]


def affine_partitions(a, limit=None):
    """Enumerate all partitions of F_2^a into affine subspaces (cells as sorted tuples)."""
    N = 1 << a
    subs = sorted(linear_subspaces(a), key=len, reverse=True)
    out = []

    def rec(uncovered, cells):
        if limit is not None and len(out) >= limit:
            return
        if not uncovered:
            out.append(tuple(sorted(cells)))
            return
        x0 = min(uncovered)
        for V in subs:
            cell = tuple(sorted(x0 ^ v for v in V))
            if all(c in uncovered for c in cell):
                rec(uncovered - set(cell), cells + [cell])

    rec(set(range(N)), [])
    return sorted(set(out))


def dual(cell, a):
    """Dual subspace V^perp of the direction space V of an affine cell (as a list of masks)."""
    x0 = cell[0]
    V = [x0 ^ c for c in cell]
    return [s for s in range(1 << a) if all(bin(s & v).count("1") % 2 == 0 for v in V)]


def codim(cell, a):
    return a - (len(cell).bit_length() - 1)


def support_coords(cell, a):
    D = dual(cell, a)
    m = 0
    for s in D:
        m |= s
    return bin(m).count("1")


def reducible(cells, a):
    """True if some hyperplane {l.x = 0} vs {l.x = 1} separates every cell (a parity decision tree root)."""
    if len(cells) == 1:
        return True
    for l in range(1, 1 << a):
        ok = True
        for c in cells:
            vals = {bin(l & x).count("1") % 2 for x in c}
            if len(vals) > 1:
                ok = False
                break
        if ok:
            return True
    return False


def labels(cells, a):
    L = np.empty(1 << a, dtype=np.int64)
    for k, c in enumerate(cells):
        for x in c:
            L[x] = k
    return L


def random_affine_partition(a, rng, maxtries=1000):
    """Greedy random partition: repeatedly cover the least uncovered point with a random affine cell."""
    subs = linear_subspaces(a)
    N = 1 << a
    for _ in range(maxtries):
        unc = set(range(N))
        cells = []
        okk = True
        while unc:
            x0 = rng.choice(sorted(unc))
            cand = []
            for V in subs:
                cell = tuple(sorted(x0 ^ v for v in V))
                if all(c in unc for c in cell):
                    cand.append(cell)
            # bias toward mid-size cells
            w = np.array([1.0 / (1 + abs(len(c) - 2)) for c in cand])
            cell = cand[rng.choice(len(cand), p=w / w.sum())]
            cells.append(cell)
            unc -= set(cell)
        return tuple(sorted(cells))
