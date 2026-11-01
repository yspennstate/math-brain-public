"""Exact curve of H/(I-1) against the number k of auxiliary variables for the PM(K_{3,3}) core with its 18 hole
cells (9 cross pairs).  k <= 9: every partition of the 9 sites into k groups (sites are pairwise non-adjacent, so
influence does not depend on the grouping; the entropy of a group is that of the Walsh transform of the indicator
of its cells).  k = 9 + j: j sites split into two singleton coins each.  Entropies in mpmath (60 digits); the
max for each k is reported, and the published 14- and 17-variable values are compared."""
import psutil; _p = psutil.Process(); _p.nice(psutil.BELOW_NORMAL_PRIORITY_CLASS); _p.cpu_affinity([2, 3, 14, 15])
import json
from fractions import Fraction
import numpy as np
import mpmath as mp
from holecore import fwht_int, core_I2

mp.mp.dps = 60
BASE = r"~/mop-fei-opus/proofnet24/P03-fei/continuations/2026-09-22-opus-team"
c0 = np.load(BASE + "/F2-new-gates/logs/numaro_core_c0.npy").astype(np.int64)
hosts = json.load(open(BASE + "/F2-new-gates/logs/numaro_decomposition.json", encoding="utf-8"))["hosts"]
m, N = 9, 512


def Hspec(W):
    vals, cnts = np.unique(np.abs(W[W != 0]), return_counts=True)
    s = mp.mpf(0)
    for v, c in zip(vals, cnts):
        p = mp.mpf(int(v)) ** 2 / N ** 2
        s += int(c) * p * mp.log(1 / p, 2)
    return s


Hcore = Hspec(fwht_int(c0))
I2core = int(core_I2(c0, m))
Hgrp = {}
for mask in range(1, 512):
    ind = np.zeros(N, dtype=np.int64)
    for j in range(9):
        if (mask >> j) & 1:
            for x in hosts[j]:
                ind[x] = 1
    Hgrp[mask] = Hspec(fwht_int(ind))
# influence: core + per pair (m+2)*2 - 2 = 2m + 2 (sites pairwise non-adjacent: check)
for i in range(9):
    for j in range(i + 1, 9):
        for a in hosts[i]:
            for b in hosts[j]:
                assert bin(a ^ b).count("1") > 1, "sites adjacent"
I = Fraction(I2core + 9 * (2 * m + 2), 2 * N)
assert I == Fraction(261, 128)
Im1 = mp.mpf(I.numerator) / I.denominator - 1


def partitions(elems):
    if not elems:
        yield []
        return
    first, rest = elems[0], elems[1:]
    for p in partitions(rest):
        for i in range(len(p)):
            yield p[:i] + [[first] + p[i]] + p[i + 1:]
        yield [[first]] + p


best = {}
count = 0
allvals = {}
for p in partitions(list(range(9))):
    count += 1
    H = Hcore + sum(Hgrp[sum(1 << j for j in g)] for g in p)
    R = H / Im1
    k = len(p)
    if k not in best or R > best[k][0]:
        best[k] = (R, p)
    allvals.setdefault(k, set()).add(mp.nstr(R, 18))
print("partitions enumerated:", count)
for k in sorted(best):
    R, p = best[k]
    print(f"k={k:2d} aux (n={9+k:2d}): max H/(I-1) = {mp.nstr(R, 22)}   distinct values over partitions: {len(allvals[k])}   e.g. {p}")
# splits beyond 9
H9 = Hcore + sum(Hgrp[1 << j] for j in range(9))
for jsp in range(1, 10):
    H = H9 + mp.mpf(4 * jsp) / N          # each split: pair entropy 4(m-1)/N -> two singletons 2*2m/N: +4/N
    Iv = Im1 + mp.mpf(jsp) / N           # influence +1/N per split: (m+2) - ... pair 2m+2 -> 2(m+2): +2 in I2
    print(f"k={9+jsp:2d} aux (n={18+jsp:2d}): H/(I-1) = {mp.nstr(H / Iv, 22)}")
pub14 = mp.mpf("6.4901128435233943")
pub17 = mp.mpf("6.514326913930565372")
print("published 14-variable value 6.4901128435233943 among k=5 partition values:",
      any(abs(mp.mpf(v) - pub14) < mp.mpf("1e-15") for v in allvals[5]))
print("published 17-variable value among k=8 partition values:",
      any(abs(mp.mpf(v) - pub17) < mp.mpf("1e-15") for v in allvals[8]))
