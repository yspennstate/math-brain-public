# Independent check of Table 1: E T_n for bridge words, by first-step analysis on the last n-1 letters
# (a different route from the matching matrix). Exact rational arithmetic via sympy for n <= 8, floats above.
import math, itertools, sys
import numpy as np
from fractions import Fraction

def lam_n(lam, n):
    f = math.floor(lam * math.sqrt(n))
    return f if (f - n) % 2 == 0 else f + 1

def ET(lam, n, exact):
    L = lam_n(lam, n)
    m = n - 1
    S = 1 << m
    # state: last m letters as bits (1 = +1), oldest letter in the high bit
    sums = np.array([2 * bin(s).count("1") - m for s in range(S)])
    idx = {}
    rows = []
    if exact:
        import sympy
        A = sympy.zeros(S, S); b = sympy.ones(S, 1)
        for s in range(S):
            A[s, s] += 1
            for x in (0, 1):
                tot = sums[s] + (1 if x else -1)
                if tot == L: continue
                t = ((s << 1) | x) & (S - 1)
                A[s, t] -= sympy.Rational(1, 2)
        h = A.LUsolve(b)
        val = sympy.Rational(m) + sum(h) / S
        return val
    A = np.eye(S); b = np.ones(S)
    for s in range(S):
        for x in (0, 1):
            tot = sums[s] + (1 if x else -1)
            if tot == L: continue
            t = ((s << 1) | x) & (S - 1)
            A[s, t] -= 0.5
    h = np.linalg.solve(A, b)
    return m + h.mean()

for lam in (0, 1):
    for n in (2, 3, 4, 5, 6, 7, 8, 10, 12):
        v = ET(lam, n, exact=(n <= 6))
        print(lam, n, lam_n(lam, n), v, float(v), float(v) / n)
