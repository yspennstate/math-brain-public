"""Generators of permutation groups on small designs, for group-invariant core search.
Each function returns (m, list of point permutations as tuples)."""
import itertools
import numpy as np


def _pg_points(q, d):
    """Normalized nonzero vectors of F_q^(d) (projective space PG(d-1,q)), q prime."""
    pts = []
    for v in itertools.product(range(q), repeat=d):
        if any(v):
            # normalize: first nonzero coordinate = 1
            i = next(k for k in range(d) if v[k])
            inv = pow(v[i], q - 2, q)
            w = tuple((x * inv) % q for x in v)
            if w not in pts:
                pts.append(w)
    return pts


def _normalize(v, q):
    i = next(k for k in range(len(v)) if v[k])
    inv = pow(v[i], q - 2, q)
    return tuple((x * inv) % q for x in v)


def pg_group(q, d, mats):
    pts = _pg_points(q, d)
    idx = {p: i for i, p in enumerate(pts)}
    perms = []
    for M in mats:
        M = np.array(M) % q
        perm = []
        for p in pts:
            w = tuple(int(x) % q for x in (M @ np.array(p)))
            perm.append(idx[_normalize(w, q)])
        perms.append(tuple(perm))
    return len(pts), perms, pts


def ag_group(q, d, mats, translations=True):
    pts = list(itertools.product(range(q), repeat=d))
    idx = {p: i for i, p in enumerate(pts)}
    perms = []
    for M in mats:
        M = np.array(M) % q
        perms.append(tuple(idx[tuple(int(x) % q for x in (M @ np.array(p)))] for p in pts))
    if translations:
        for k in range(d):
            e = [0] * d; e[k] = 1
            perms.append(tuple(idx[tuple((p[j] + e[j]) % q for j in range(d))] for p in pts))
    return len(pts), perms, pts


def fano():
    # GL(3,2) generators
    A = [[1, 1, 0], [0, 1, 0], [0, 0, 1]]
    B = [[0, 0, 1], [1, 0, 0], [0, 1, 0]]
    return pg_group(2, 3, [A, B])[:2]


def ag32():
    A = [[1, 1, 0], [0, 1, 0], [0, 0, 1]]
    B = [[0, 0, 1], [1, 0, 0], [0, 1, 0]]
    return ag_group(2, 3, [A, B])[:2]


def agl23():
    A = [[1, 1], [0, 1]]
    B = [[0, 1], [2, 0]]
    C = [[2, 0], [0, 1]]
    return ag_group(3, 2, [A, B, C])[:2]


def pg23():
    A = [[1, 1, 0], [0, 1, 0], [0, 0, 1]]
    B = [[0, 0, 1], [1, 0, 0], [0, 1, 0]]
    C = [[2, 0, 0], [0, 1, 0], [0, 0, 1]]
    return pg_group(3, 3, [A, B, C])[:2]


def pg32():
    A = [[1, 1, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
    B = [[0, 0, 0, 1], [1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0]]
    return pg_group(2, 4, [A, B])[:2]


def paley11():
    # Z_11 x| QR(11): x -> x+1, x -> 3x (3 generates the squares mod 11)
    m = 11
    t = tuple((x + 1) % m for x in range(m))
    s = tuple((3 * x) % m for x in range(m))
    return m, [t, s]


def cyclic(m, mult=None):
    t = tuple((x + 1) % m for x in range(m))
    g = [t]
    if mult is not None:
        g.append(tuple((mult * x) % m for x in range(m)))
    return m, g


def singer13():
    # PG(2,3) Singer cycle: points indexed 0..12 via a perfect difference set {0,1,3,9}
    m = 13
    return m, [tuple((x + 1) % m for x in range(m)), tuple((3 * x) % m for x in range(m))]
