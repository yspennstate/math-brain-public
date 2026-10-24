"""Count-splitting (hierarchical hypergeometric) tree references.

For a rooted tree T whose leaves are the coordinates, write c_v = |S cap B_v| (B_v = leaves below v).
The count-splitting reference along T is
    Q_T(S) = Pr[c_root = |S|] * prod_{internal v} Pr[(c_u)_{u child of v} | c_v],
with the TRUE conditional laws computed from the spectral sample.  Its expected code length is
    CS(T) = H(|S|) + sum_{internal v} [ H((c_u)_{u child of v}) - H(c_v) ].
Hit-only tree-Markov references are the same with every count truncated to min(c, 1).
"""
import numpy as np
import wlib as W


def _mask(t):
    return W.tree_mask(t)


def _H_of_labels(p, labels):
    """entropy (bits) of the discrete random variable labels(S), S ~ p."""
    _, inv = np.unique(labels, return_inverse=True)
    q = np.bincount(inv.ravel(), weights=p)
    return W.H_of(q)


def cs_cost(p, n, t, truncate=False):
    N = 1 << n
    S = np.arange(N, dtype=np.int64)
    pc_cache = {}

    def counts(B):
        if B not in pc_cache:
            c = W.popcounts(N)[S & B] if False else _pop(S & B)
            if truncate:
                c = np.minimum(c, 1)
            pc_cache[B] = c
        return pc_cache[B]

    total = _H_of_labels(p, counts(N - 1))

    def rec(node):
        nonlocal total
        if isinstance(node, (int, np.integer)):
            return
        kids = [_mask(c) for c in node]
        B = 0
        for k in kids:
            B |= k
        lab = np.zeros(N, dtype=np.int64)
        for k in kids:
            lab = lab * (n + 1) + counts(k)
        total += _H_of_labels(p, lab) - _H_of_labels(p, counts(B))
        for c in node:
            rec(c)
    rec(t)
    return total


_POP = None


def _pop(x):
    global _POP
    x = np.asarray(x, dtype=np.int64)
    out = np.zeros_like(x)
    y = x.copy()
    while y.any():
        out += y & 1
        y >>= 1
    return out


def balanced_tree(coords):
    coords = list(coords)
    if len(coords) == 1:
        return coords[0]
    m = len(coords) // 2
    return (balanced_tree(coords[:m]), balanced_tree(coords[m:]))


def caterpillar(coords):
    coords = list(coords)
    t = coords[-1]
    for c in reversed(coords[:-1]):
        t = (c, t)
    return t


def ternary_tree(depth, offset=0):
    if depth == 0:
        return offset
    k = 3 ** (depth - 1)
    return tuple(ternary_tree(depth - 1, offset + j * k) for j in range(3))


def binarize(t):
    if isinstance(t, (int, np.integer)):
        return t
    kids = [binarize(c) for c in t]
    while len(kids) > 2:
        kids = [(kids[0], kids[1])] + kids[2:]
    return tuple(kids)
