"""Deep towers for selected sym_enum codes: the enumeration caps the depth (default 14), and a nearly balanced
base converges slowly, so a value reported at the cap may still be rising.

Usage: python sym_deep.py group maxdepth code [code ...]
Prints, for each code and each sign pattern pp, mm, mp, pm: best value, its depth, the depth-one value, and the
value sequence at depths 1, 2, 4, 8, ... up to maxdepth (each from its own run with that cap, so "best" is the
running maximum up to the cap).
"""
import sys

import numpy as np

import sym_enum


def table(name, code):
    k, gens = sym_enum.group_gens(name)
    m, inv, tr = sym_enum.orbits(k, gens)
    sg = np.ones(m)
    for j in range(1, m):
        sg[j] = 1.0 - 2.0 * ((code >> (j - 1)) & 1)
    return k, sg[inv]


def main():
    name = sys.argv[1]
    maxdepth = int(sys.argv[2])
    codes = [int(a) for a in sys.argv[3:]]
    caps = []
    d = 1
    while d < maxdepth:
        caps.append(d)
        d *= 2
    caps.append(maxdepth)
    for code in codes:
        k, F = table(name, code)
        print("group %s code %d mean %.10f" % (name, code, F.mean()))
        for pat in ("pp", "mm", "mp", "pm"):
            row = []
            for cap in caps:
                bt = sym_enum.BatchTower(k, cap)
                best, bdep, g1 = bt.values(F[None, :], pat)
                row.append("%d:%.12f@%d" % (cap, best[0], bdep[0]))
            print("  %s  %s" % (pat, "  ".join(row)))


if __name__ == "__main__":
    main()
