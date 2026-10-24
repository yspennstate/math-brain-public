"""Exact two-sided McNemar p values for the discordant pairs reported in the paper."""
from math import comb
def p(b, c):
    n = b + c; k = min(b, c)
    s = sum(comb(n, i) for i in range(k + 1)) / 2 ** n
    return min(1.0, 2 * s)
for b, c in [(15,4),(12,3),(10,1),(5,3),(10,4),(9,4),(27,8),(2,3),(10,3),(14,40),(6,8),(8,3),(462,0),(143,16),(134,12),(549,1),(427,1),(1,2),(3,10),(1,10),(112,0),(119,0)]:
    print(b, c, "%.3g" % p(b, c))
