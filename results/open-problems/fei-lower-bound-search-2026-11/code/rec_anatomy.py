"""rec_anatomy.py - structure of a library gate "n hex": influences, two-variable modules, cofactor counts.
usage: python rec_anatomy.py LIBFILE [line_index]
A pair (i, j) is a module when the four cofactors of g in (x_i, x_j) take at most two distinct values, i.e.
g depends on the pair only through one Boolean function h(x_i, x_j).
"""
import sys

import numpy as np


def load(path, k=0):
    lines = [l.split() for l in open(path, encoding="utf-8") if l.strip() and not l.startswith("#")]
    n, hx = int(lines[k][0]), lines[k][1]
    tab = int(hx, 16)
    b = np.frombuffer(tab.to_bytes((1 << n) // 8, "little"), dtype=np.uint8)
    return n, np.unpackbits(b, bitorder="little").astype(np.int8)


def walsh(tt):
    a = 1.0 - 2.0 * tt.astype(np.float64)
    h = 1
    while h < len(a):
        a = a.reshape(-1, 2, h)
        lo, hi = a[:, 0, :].copy(), a[:, 1, :].copy()
        a[:, 0, :] = (lo + hi) / 2
        a[:, 1, :] = (lo - hi) / 2
        a = a.reshape(-1)
        h *= 2
    return a


def cof(tt, n, i, j, a, b):
    idx = np.arange(1 << n)
    m = (((idx >> i) & 1) == a) & (((idx >> j) & 1) == b)
    return tt[m]


def main():
    n, tt = load(sys.argv[1], int(sys.argv[2]) if len(sys.argv) > 2 else 0)
    N = 1 << n
    idx = np.arange(N)
    a = walsh(tt)
    w = a * a
    size = np.array([bin(t).count("1") for t in range(N)])
    I = float((w * size).sum())
    nz = w > 1e-300
    H = float(-(w[nz] * np.log2(w[nz])).sum())
    print("n %d  mean %.10f  I %.10f (x128 = %.6f)  H %.12f  H/(I-1) %.12f  nonzero coefficients %d" % (
        n, a[0], I, I * 128, H, H / (I - 1), int(nz.sum())))
    inf = [float(w[((idx >> i) & 1) == 1].sum()) for i in range(n)]
    print("influences x 2^%d:" % (n - 1), " ".join("%g" % (v * (1 << (n - 1))) for v in inf))
    # monotone direction of each variable
    dirs = []
    for i in range(n):
        lo = tt[((idx >> i) & 1) == 0]
        hi = tt[((idx >> i) & 1) == 1]
        dirs.append("+" if (hi >= lo).all() else "-" if (hi <= lo).all() else "?")
    print("monotone direction per variable (tt bit rising with x_i):", "".join(dirs))
    # level weights
    print("weight by level:", " ".join("%d:%.6f" % (k, float(w[size == k].sum())) for k in range(n + 1) if w[size == k].sum() > 1e-15))
    # modules
    mods = []
    for i in range(n):
        for j in range(i + 1, n):
            c = [cof(tt, n, i, j, x, y) for x in (0, 1) for y in (0, 1)]
            cls = []
            lab = []
            for v in c:
                for t, u in enumerate(cls):
                    if np.array_equal(u, v):
                        lab.append(t)
                        break
                else:
                    cls.append(v)
                    lab.append(len(cls) - 1)
            if len(cls) <= 2:
                mods.append((i, j, lab))
    print("two-variable modules (i, j, class of cofactor 00 01 10 11):")
    for m in mods:
        print("  ", m)
    # which variables carry no weight on sets made only of a candidate aux set: report, for each variable set
    # given by the modules' second members, the total weight on non-empty subsets of that set
    if mods:
        for name, pick in (("first members", 0), ("second members", 1)):
            S = sorted({m[pick] for m in mods})
            mask = sum(1 << s for s in S)
            inside = (idx & ~mask) == 0
            inside[0] = False
            print("weight on non-empty subsets of the %s %s: %.3e" % (name, S, float(w[inside].sum())))
    # quotient gate: fix one representative assignment per module class
    if len(mods) * 2 == n:
        k = len(mods)
        q = np.zeros(1 << k, dtype=np.int8)
        for y in range(1 << k):
            x = 0
            for t, (i, j, lab) in enumerate(mods):
                want = (y >> t) & 1
                # class label of cofactor 11 is taken as "1" when it differs from 00's
                pos = [p for p in range(4) if (lab[p] == lab[3]) == bool(want)]
                p0 = pos[0]
                if (p0 >> 1) & 1:
                    x |= 1 << i
                if p0 & 1:
                    x |= 1 << j
            q[y] = tt[x]
        hx = "%x" % sum(int(b) << t for t, b in enumerate(q))
        print("quotient gate on %d inputs: %s  (ones %d of %d)" % (k, hx, int(q.sum()), 1 << k))
        for t, (i, j, lab) in enumerate(mods):
            ones = sum(1 for p in range(4) if lab[p] == lab[3])
            print("   module %d = vars (%d,%d): inner function true on %d of 4 points, labels %s" % (t, i, j, ones, lab))


if __name__ == "__main__":
    main()
