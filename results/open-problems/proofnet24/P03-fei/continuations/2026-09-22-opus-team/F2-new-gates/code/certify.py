"""Standalone certifier for balanced Boolean functions given as "core with holes filled by fresh variables".

Input: a JSON file with
  m        : number of core variables
  core     : string of length 2^m over {'+','-','0'}: value of c0 at cell x (bit i of x = core variable i;
             '-' = -1 = true, '+' = +1 = false, '0' = hole)
  groups   : list of lists of hole cells; group j is filled by fresh variable m+j (F = y_j, i.e. +1/-1 with the
             variable, on every cell of the group)
The checker
  1. checks that the groups partition the holes,
  2. builds the full truth table of F on n = m + #groups variables (entry index = x + 2^m * y),
  3. computes the integer Walsh transform W (F^(S) = W(S)/2^n) with numpy int64,
  4. checks sum F = 0 (balance) and Parseval sum W^2 = 4^n exactly,
  5. computes I = sum |S| W(S)^2 / 4^n as an exact Fraction,
  6. encloses H = sum_S (W/2^n)^2 log2(4^n/W^2) = sum_v cnt_v (v^2/4^n)(2n - 2 log2 v) with mpmath interval
     arithmetic (outward rounded), grouping coefficients by |W| = v,
  7. prints an interval for H/(I-1) and compares its lower end with a given threshold using interval arithmetic.
No floating-point value decides any comparison.
usage: python certify.py description.json [threshold_as_decimal_string]
"""
import sys, json
from fractions import Fraction
import numpy as np
import mpmath
from mpmath import iv


def fwht_inplace(a):
    h = 1
    n = a.shape[0]
    while h < n:
        b = a.reshape(-1, 2 * h)
        x = b[:, :h].copy()
        b[:, :h] += b[:, h:]
        b[:, h:] = x - b[:, h:]
        h *= 2
    return a


def build_table(m, core, groups):
    Nc = 1 << m
    assert len(core) == Nc
    c0 = np.array([{'+': 1, '-': -1, '0': 0}[ch] for ch in core], dtype=np.int64)
    holes = set(np.where(c0 == 0)[0].tolist())
    seen = set()
    for g in groups:
        for x in g:
            assert x in holes and x not in seen, "groups must partition the holes"
            seen.add(x)
    assert seen == holes, "every hole must belong to a group"
    k = len(groups)
    n = m + k
    T = np.empty((1 << k, Nc), dtype=np.int64)
    T[:] = c0
    yv = np.arange(1 << k)
    for j, g in enumerate(groups):
        col = np.where((yv >> j) & 1, -1, 1)
        for x in g:
            T[:, x] = col
    return T.reshape(-1), n


def certify(desc, threshold=None, dps=60):
    m = desc['m']; core = desc['core']; groups = desc['groups']
    F, n = build_table(m, core, groups)
    N = 1 << n
    assert F.shape == (N,)
    assert set(np.unique(F).tolist()) <= {-1, 1}
    s = int(F.sum())
    assert s == 0, f"not balanced: sum = {s}"
    W = fwht_inplace(F.copy())
    # Parseval (exact, python ints to avoid overflow)
    vals, cnts = np.unique(np.abs(W), return_counts=True)
    par = sum(int(v) * int(v) * int(c) for v, c in zip(vals, cnts))
    assert par == N * N, "Parseval failed"
    # influence: sum |S| W^2, exact
    pc = np.zeros(N, dtype=np.int64)
    for i in range(n):
        pc += (np.arange(N) >> i) & 1
    Inum = 0
    # accumulate in python ints by level to avoid int64 overflow
    W2 = W.astype(object) if N <= (1 << 12) else None
    for lev in range(n + 1):
        sel = W[pc == lev]
        if sel.size:
            v, c = np.unique(np.abs(sel), return_counts=True)
            Inum += lev * sum(int(a) * int(a) * int(b) for a, b in zip(v, c))
    I = Fraction(Inum, N * N)
    # entropy enclosure
    mpmath.mp.dps = dps
    iv.dps = dps
    H = iv.mpf(0)
    two_n = iv.mpf(2 * n)
    for v, c in zip(vals, cnts):
        v = int(v); c = int(c)
        if v == 0:
            continue
        p = iv.mpf(v * v) / iv.mpf(N * N)
        H += c * p * (two_n - 2 * iv.log(iv.mpf(v)) / iv.log(iv.mpf(2)))
    Iiv = iv.mpf(I.numerator) / iv.mpf(I.denominator)
    Rng = H / (Iiv - 1)
    out = dict(n=n, I=str(I), I_float=float(I), H_lo=mpmath.nstr(H.a, 40), H_hi=mpmath.nstr(H.b, 40),
               R_lo=mpmath.nstr(Rng.a, 40), R_hi=mpmath.nstr(Rng.b, 40),
               nonzero_coefficients=int((W != 0).sum()), distinct_magnitudes=int((vals != 0).sum()))
    if threshold is not None:
        t = iv.mpf(threshold)
        out['threshold'] = threshold
        out['certified_above_threshold'] = bool(Rng.a > t.b)
    return out


if __name__ == '__main__':
    desc = json.load(open(sys.argv[1], encoding='utf-8'))
    thr = sys.argv[2] if len(sys.argv) > 2 else None
    res = certify(desc, thr)
    for k, v in res.items():
        print(f"{k}: {v}")
