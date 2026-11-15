import math, sys, itertools
from fractions import Fraction as F
sys.path.insert(0, r"~\AppData\Local\Temp\claude\727c9a8b9fa813fe\agent-82f2-44c5-b3e3-c0011e4a519a\scratchpad\fpp")
from et3 import words, wait  # et3 prints its own check on import; harmless

def et_exact(W):
    n = len(W[0]); k = len(W)
    M = [[F(sum(2 ** L for L in range(1, n + 1) if W[i][n - L:] == W[j][:L])) for j in range(k)] for i in range(k)]
    # solve M x = 1 exactly, ET = 1 / sum(x)
    A = [row[:] + [F(1)] for row in M]
    for c in range(k):
        p = next(r for r in range(c, k) if A[r][c] != 0)
        A[c], A[p] = A[p], A[c]
        pv = A[c][c]; A[c] = [x / pv for x in A[c]]
        for r in range(k):
            if r != c and A[r][c] != 0:
                f = A[r][c]; A[r] = [x - f * y for x, y in zip(A[r], A[c])]
    return 1 / sum(A[r][k] for r in range(k))

print("--- definition of Section 1 (floor), lambda = -1")
for n in range(3, 13):
    fl = math.floor(-math.sqrt(n))
    l = fl if (fl - n) % 2 == 0 else fl + 1
    a = -l; W = words(n, a)
    e = et_exact(W) if len(W) <= 60 else None
    print(n, a, len(W), e, round(float(e), 6) if e is not None else None, round(wait(W), 6), flush=True)
