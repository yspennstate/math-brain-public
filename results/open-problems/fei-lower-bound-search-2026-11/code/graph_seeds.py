"""Truth tables of monotone gates built from small graphs, one per line: m hex name.

For a graph with edge inputs, 'star' is true when some vertex has all its edges present and 'pm' is true when
the present edges contain a perfect matching (for K34: a matching that covers the side of size 3).
The 9-input gate under the record 6.521845710923 is star(K33) = pm(K33).

usage: python3 graph_seeds.py OUT
"""
import sys
import itertools
import numpy as np


def bip(a, b, keep=lambda i, j: True):
    return a + b, [(i, a + j) for i in range(a) for j in range(b) if keep(i, j)]


def graphs():
    g = {}
    g["k33"] = bip(3, 3)
    g["prism"] = (6, [(0, 1), (1, 2), (0, 2), (3, 4), (4, 5), (3, 5), (0, 3), (1, 4), (2, 5)])
    g["k4"] = (4, list(itertools.combinations(range(4), 2)))
    g["q3"] = (8, [(u, u ^ (1 << b)) for u in range(8) for b in range(3) if u < u ^ (1 << b)])
    out = [(i, (i + 1) % 5) for i in range(5)]
    g["pet"] = (10, out + [(5 + i, 5 + (i + 2) % 5) for i in range(5)] + [(i, 5 + i) for i in range(5)])
    g["k34"] = bip(3, 4)
    g["k44"] = bip(4, 4)
    g["k5"] = (5, list(itertools.combinations(range(5), 2)))
    g["octa"] = (6, [(u, v) for u, v in itertools.combinations(range(6), 2) if v != u + 3])
    g["k6"] = (6, list(itertools.combinations(range(6), 2)))
    g["mob8"] = (8, [(i, (i + 1) % 8) for i in range(8)] + [(i, i + 4) for i in range(4)])
    g["b5c"] = bip(5, 5, lambda i, j: (j - i) % 5 in (0, 1, 2))
    g["k24"] = bip(2, 4)
    g["k23"] = bip(2, 3)
    g["c6k"] = bip(3, 3, lambda i, j: i != j)
    g["k4m"] = bip(4, 4, lambda i, j: i != j)
    return g


def matchings(nv, edges, cover):
    """edge masks of the matchings that cover every vertex in 'cover'"""
    res = []

    def rec(left, mask):
        if not left:
            res.append(mask)
            return
        v = min(left)
        for e, (a, b) in enumerate(edges):
            if v in (a, b):
                w = b if a == v else a
                if w in used:
                    continue
                used.add(v)
                used.add(w)
                rec(left - {v, w}, mask | (1 << e))
                used.discard(v)
                used.discard(w)
    used = set()
    rec(frozenset(cover), 0)
    return sorted(set(res))


def table(m, masks):
    x = np.arange(1 << m, dtype=np.int64)
    f = np.zeros(1 << m, dtype=bool)
    for mk in masks:
        f |= (x & mk) == mk
    return f


def hexof(f):
    return "%x" % int.from_bytes(np.packbits(f, bitorder="little").tobytes(), "little")


def main():
    out = open(sys.argv[1], "w")
    for name, (nv, edges) in graphs().items():
        m = len(edges)
        star = [sum(1 << e for e, (a, b) in enumerate(edges) if v in (a, b)) for v in range(nv)]
        fam = [("star", star)]
        cover = range(3) if name == "k34" else range(2) if name in ("k24", "k23") else range(nv)
        pm = matchings(nv, edges, cover)
        if pm:
            fam.append(("pm", pm))
        for kind, masks in fam:
            f = table(m, masks)
            out.write("%d %s %s_%s terms %d true %d\n" % (m, hexof(f), kind, name, len(masks), int(f.sum())))
    out.close()


if __name__ == "__main__":
    main()
