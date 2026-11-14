"""Tally superbase types from ust_torus_theta.py (4 columns) or ust_torus_shear.py (5 columns) output.
A class (a, b) is the period a + b*tau, tau = (s + i n2) / n1. Usage: python classify.py file1.tsv [...]"""
import sys
from collections import Counter


def key(cls, tau):
    vs = []
    for a, b in cls:
        if a < 0 or (a == 0 and b < 0):
            a, b = -a, -b
        vs.append((round(abs(a + b * tau) ** 2, 9), a, b))
    vs.sort()
    return tuple((a, b) for _, a, b in vs)


cnt = Counter()
two = 0
tot = 0
tau = None
for fn in sys.argv[1:]:
    for line in open(fn, encoding="utf-8"):
        f = line.rstrip("\n").split("\t")
        if len(f) == 4:
            n1, n2, m, s = f
            sh = 0
        else:
            n1, n2, sh, m, s = f
        tau = complex(int(sh), int(n2)) / int(n1)
        tot += 1
        cls = [tuple(map(int, x.split(","))) for x in s.split(";")] if s else []
        if int(m) != 3:
            two += 1
            continue
        cnt[key(cls, tau)] += 1
print(f"samples {tot}, figure-eight {two} = {two / tot:.4f}, tau {tau}")
for k, v in cnt.most_common(25):
    print(f"{v / tot:.5f}  {v:7d}  {k}")
