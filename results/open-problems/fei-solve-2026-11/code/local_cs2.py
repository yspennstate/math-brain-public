"""Witnesses with more than one count (FLOW 11(h)(2), after local_cs.py).

For a labelling lab(T) of the subsets T of [n] - i, the witness is
    L^lab_i = H(1[i in U] | lab(U - i)) = sum over labels of Phi(A_label, B_label)  >=  E_i.
Tested on AND_w o MAJ_r and OR o AND o OR with i = coordinate 0 and the labellings
    one   : |T n mates|                                   (the single-set witness of local_cs.py)
    two   : (|T n mates|, |T n rest|)
    empty : (|T n mates|, [T n rest empty])
    blocks: (|T n mates|, number of other blocks that T meets)
    vec   : (|T n mates|, |T n block_2|, ..., |T n block_w|) sorted over the other blocks
    exact : T itself (gives E_i)

usage: python local_cs2.py
"""
import numpy as np
from local_cs import wht, phi, pts


def witness(p, q, lab):
    """p, q: weights of T and T + i; lab: integer label per T."""
    _, inv = np.unique(lab, return_inverse=True)
    k = inv.max() + 1
    A = np.bincount(inv, weights=p, minlength=k)
    B = np.bincount(inv, weights=q, minlength=k)
    return float(phi(A, B).sum()), k


def run(name, f, n, blocks):
    """blocks: list of lists of coordinates; coordinate 0 is in blocks[0]."""
    mu = wht(f, n) ** 2
    idx = np.arange(1 << n)
    lo = idx[(idx & 1) == 0]
    p = mu[lo]
    q = mu[lo | 1]
    inf = float(q.sum())
    bits = (lo[:, None] >> np.arange(n)[None, :]) & 1
    mates = [c for c in blocks[0] if c != 0]
    cm = bits[:, mates].sum(axis=1)
    others = blocks[1:]
    cnt = np.stack([bits[:, b].sum(axis=1) for b in others], axis=1) if others else np.zeros((len(lo), 0), int)
    rest = cnt.sum(axis=1)
    touched = (cnt > 0).sum(axis=1)
    srt = np.sort(cnt, axis=1)
    base = n + 1
    vec = cm.copy()
    for j in range(srt.shape[1]):
        vec = vec * base + srt[:, j]
    labs = dict(one=cm, two=cm * base + rest, empty=cm * 2 + (rest == 0), blocks=cm * base + touched, vec=vec,
                exact=np.arange(len(lo)))
    out = []
    for key in ("exact", "one", "empty", "blocks", "two", "vec"):
        L, k = witness(p, q, labs[key])
        out.append("%s=%.4f(%d)" % (key, L / inf, k))
    print("%-14s n=%2d Inf=%.5f  %s" % (name, n, inf, "  ".join(out)), flush=True)


def main():
    for w, r in ((2, 3), (3, 3), (4, 3), (5, 3), (6, 3), (2, 5), (3, 5), (2, 7)):
        n = w * r
        if n > 18:
            continue
        b = pts(n).reshape(-1, w, r)
        inner = (b.sum(axis=2) * 2 > r)
        blocks = [list(range(j * r, (j + 1) * r)) for j in range(w)]
        run("AND%d_MAJ%d" % (w, r), np.where(inner.all(axis=1), -1.0, 1.0), n, blocks)
    for s in (4, 6, 8):
        n = 2 * s
        b = pts(n).reshape(-1, s, 2)
        blocks = [list(range(2 * j, 2 * j + 2)) for j in range(s)]
        run("TRIBES_2x%d" % s, np.where(b.all(axis=2).any(axis=1), -1.0, 1.0), n, blocks)
    for t in (2, 3, 4):
        n = 4 * t
        b = pts(n).reshape(-1, t, 2, 2)
        f = np.where(b.any(axis=3).all(axis=2).any(axis=1), -1.0, 1.0)
        # blocks: the OR-pair of 0, its AND-partner pair, then the other top-level groups
        blocks = [[0, 1], [2, 3]] + [list(range(4 * j, 4 * j + 4)) for j in range(1, t)]
        run("OR_AND_OR_%d" % n, f, n, blocks)


if __name__ == "__main__":
    main()
