"""For a Boolean property c (G-invariant) with a deficit of true cells, try every set of false orbits whose sizes
sum to the deficit (and, symmetrically, sets of true orbits for an excess), make them holes, evaluate H/(I-1)."""
import psutil; _p = psutil.Process(); _p.nice(psutil.BELOW_NORMAL_PRIORITY_CLASS); _p.cpu_affinity([2, 3, 14, 15])
import itertools, sys, time
import numpy as np
from orbsa2 import Model2
from holecore import summarize


def subset_sums(M, vprop, max_k=4):
    size = M.size
    bal = int((M.size * vprop).sum())      # sum c0 = (#false - #true) for +-1 values
    target = abs(bal)
    side = 1 if bal > 0 else -1             # holes must be taken from cells with value = side
    cands = [o for o in range(M.no) if vprop[o] == side and size[o] <= target]
    res = []
    for k in range(1, max_k + 1):
        for S in itertools.combinations(cands, k):
            if sum(int(size[o]) for o in S) == target:
                v = vprop.copy(); v[list(S)] = 0
                R, I, b = M.evaluate(v)
                assert b == 0
                res.append((R, S, I))
    res.sort(key=lambda t: -t[0])
    return bal, res
