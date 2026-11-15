"""rec_coins.py - for the 18-variable record: at which settings x of the nine high-influence variables does the
output depend on the nine coins, and how.
usage: python rec_coins.py results/rec18.txt
"""
import sys
from collections import Counter

import numpy as np

from rec_anatomy import load


def main():
    n, tt = load(sys.argv[1])
    m = 9
    T = tt.reshape(1 << m, 1 << m)  # T[y, x]: x = low 9 bits, y = high 9 bits
    ones_x = T.sum(axis=0)
    print("x settings: constant 0: %d, constant 1: %d, coin-dependent: %d" % (
        int((ones_x == 0).sum()), int((ones_x == 512).sum()), int(((ones_x > 0) & (ones_x < 512)).sum())))
    # the base function: majority over the coins
    base = (ones_x * 2 > 512).astype(int)
    print("ones of tt over coins, histogram:", sorted(Counter(int(v) for v in ones_x).items()))
    dep = [x for x in range(1 << m) if 0 < ones_x[x] < 512]
    for x in dep:
        col = T[:, x]
        # which coins matter
        act = []
        for j in range(m):
            ys = np.arange(1 << m)
            if not np.array_equal(col[ys & ~(1 << j)], col[ys | (1 << j)]):
                act.append(j)
        # describe as function of the active coins
        k = len(act)
        sub = []
        for z in range(1 << k):
            y = sum(((z >> t) & 1) << act[t] for t in range(k))
            sub.append(int(col[y]))
        mat = "".join(str((x >> b) & 1) for b in range(m))
        print("x=%s (rows %s|%s|%s) weight %d  coins %s  table %s  ones %d/512" % (
            mat, mat[0:3], mat[3:6], mat[6:9], bin(x).count("1"), act, "".join(map(str, sub)), int(ones_x[x])))
    # the constant part: is it a perfect-matching function under some labelling?  print minimal 1-points of the
    # coin-free upper function (all coins 1) and lower function (all coins 0)
    for name, row in (("coins all 0", T[0]), ("coins all 1", T[-1])):
        mins = []
        for x in range(1 << m):
            if row[x] and all(not row[x & ~(1 << b)] for b in range(m) if (x >> b) & 1):
                mins.append(x)
        print(name, "ones", int(row.sum()), "minimal points", len(mins), "by weight", sorted(Counter(bin(x).count("1") for x in mins).items()))
        print("   ", " ".join("".join(str((x >> b) & 1) for b in range(m)) for x in mins[:40]))


if __name__ == "__main__":
    main()
