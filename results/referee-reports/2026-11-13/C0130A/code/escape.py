"""Escape probability of a bounded deterministic cookie stack.

Run with OPENBLAS_NUM_THREADS=1. No simulation workers or background children.
The affine-tail Poisson bounds are proved in REPORT.md. mpmath evaluates their
exact rational definitions; --exact uses SymPy rational arithmetic throughout.
"""

import argparse
import json
import math
import os
import resource
import sys
import time
from pathlib import Path

os.environ.setdefault('OPENBLAS_NUM_THREADS', '1')
os.environ.setdefault('OMP_NUM_THREADS', '1')
import mpmath as mp

if hasattr(sys, 'set_int_max_str_digits'):
    sys.set_int_max_str_digits(1000000)

# Hard address-space limit where supported. macOS Python may reject RLIMIT_AS;
# actual problem sizes here are small (the exact arithmetic is the largest).
try:
    resource.setrlimit(resource.RLIMIT_AS, (3 * 1024**3, 3 * 1024**3))
except (ValueError, OSError):
    pass


def kernel_row(stack, i, K, scalar=mp.mpf):
    """P(F_(i+1)=j), 0<=j<K, and its untruncated first moment.

    Enumerate only the M non-placebo Bernoulli trials. Stop paths that reach
    the required number of successes; extend the survivors by a fair NB law.
    """
    r = i + 1
    active = {(0, 0): scalar(1)}
    row = [scalar(0) for _ in range(K)]
    mean = scalar(0)
    half = scalar(1) / 2
    for p in stack:
        new = {}
        for (s, f), mass in active.items():
            if s + 1 == r:
                if f < K:
                    row[f] += mass * p
                mean += mass * p * f
            else:
                new[s + 1, f] = new.get((s + 1, f), scalar(0)) + mass * p
            new[s, f + 1] = new.get((s, f + 1), scalar(0)) + mass * (1 - p)
        active = new
    for (s, f), mass in active.items():
        remaining = r - s
        mean += mass * (f + remaining)
        term = half ** remaining
        for n in range(max(0, K - f)):
            row[f + n] += mass * term
            term *= scalar(remaining + n) / (2 * (n + 1))
    return row, mean


def successes_law(stack, scalar=mp.mpf):
    a = [scalar(1)]
    for p in stack:
        b = [scalar(0)] * (len(a) + 1)
        for s, v in enumerate(a):
            b[s] += v * (1 - p)
            b[s + 1] += v * p
        a = b
    return a


def poisson_bounds(params, K=40, dps=80, exact=False):
    """Bounds with rationally defined endpoint constants, no tail truncation.

    exact=False is high-precision arithmetic, not directed interval arithmetic.
    exact=True produces mathematically certified rational endpoints.
    """
    mp.mp.dps = dps
    if exact:
        import sympy as sp
        scalar = sp.Rational
        matrix = sp.Matrix
    else:
        scalar = mp.mpf
        matrix = mp.matrix
    stack = [scalar(p) for p in params]
    M = len(stack)
    delta = sum(2 * p - 1 for p in stack)
    d = delta - 1
    if d <= 0 or K < max(M, 2):
        raise ValueError('Need delta>1 and K>=max(M,2)')
    rows_means = [kernel_row(stack, i, K, scalar) for i in range(K)]
    mat = matrix([[int(i == j) - rows_means[i][0][j]
                   for j in range(1, K)] for i in range(1, K)])
    rhs = matrix([[1 + (mean - sum(j * row[j] for j in range(K))) / d,
                   1 - sum(row)] for row, mean in rows_means[1:]])
    if exact:
        # DomainMatrix's fraction-free solve avoids rational elimination swell.
        from sympy.polys.matrices import DomainMatrix
        dm = DomainMatrix.from_Matrix(mat)
        db = DomainMatrix.from_Matrix(rhs)
        dm, db = dm.unify(db)
        num, den = dm.solve_den(db)
        solution = (num.to_Matrix() / dm.domain.to_sympy(den)).applyfunc(sp.cancel)
        # Use a common denominator in the residual certificate. Repeatedly
        # reducing rational sums is much slower than these integer dot products.
        a = [scalar(0)] + list(solution[:, 0])
        b = [scalar(0)] + list(solution[:, 1])
    else:
        a = [scalar(0)] + list(mp.lu_solve(mat, rhs[:, 0]))
        b = [scalar(0)] + list(mp.lu_solve(mat, rhs[:, 1]))
    law = successes_law(stack, scalar)
    ratios = []
    if exact:
        # Every w_(ell,j) shares one easily computed denominator.
        common = sp.ilcm(*(v.q for v in a + b + [1/d]))
        ai = [int(common*v) for v in a]
        bi = [int(common*v) for v in b]
        slope = int(common/d)
        law_common = sp.ilcm(*(v.q for v in law))
        law_int = [int(v*law_common) for v in law]
    for ell in range(K):
        num = scalar(0)
        den = scalar(0)
        for j in range(ell, K):
            weight = sum((law_int[s] if exact else law[s]) * math.comb(K + j - M, j - M + s - ell)
                         for s in range(M + 1)
                         if 0 <= j - M + s - ell <= K + j - M)
            if exact:
                weight *= 2**(K-1-j)
                num += weight * (ai[j] - j*slope)
                den += weight * (common - bi[j])
            else:
                weight *= scalar(2) ** (M - j - 1)
                num += weight * (a[j] - scalar(j) / d)
                den += weight * (1 - b[j])
        assert den > 0
        ratios.append(num / den)
    c_lo, c_hi = min(ratios), max(ratios)
    row, mean = rows_means[0]
    A = 1 + sum(row[j] * a[j] for j in range(K))
    A += (mean - sum(j * row[j] for j in range(K))) / d
    B = sum(row[j] * b[j] for j in range(K)) + 1 - sum(row)
    assert B >= 0
    assert all(a[j] + b[j] * c_lo >= 0 for j in range(1, K))
    assert scalar(K) / d + c_lo >= 0
    lo = stack[0] / (A + B * c_hi)
    hi = stack[0] / (A + B * c_lo)
    assert 0 < lo <= hi <= stack[0]
    def out(v):
        if exact:
            return mp.nstr(mp.mpf(str(sp.N(v, dps + 5))), dps)
        return mp.nstr(v, dps)
    result = dict(params=params, K=K, dps=dps, exact=exact,
                  delta=out(delta), lower=out(lo), upper=out(hi),
                  width=out(hi-lo), c_lower=out(c_lo), c_upper=out(c_hi),
                  priority=os.getpriority(os.PRIO_PROCESS, 0),
                  peak_rss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    if exact:
        result['rational_lower'] = str(lo)
        result['rational_upper'] = str(hi)
    return result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--p', nargs='+', required=True)
    parser.add_argument('--K', type=int, default=40)
    parser.add_argument('--dps', type=int, default=80)
    parser.add_argument('--exact', action='store_true')
    parser.add_argument('--output')
    args = parser.parse_args()
    start = time.monotonic()
    result = poisson_bounds(args.p, args.K, args.dps, args.exact)
    result['seconds'] = time.monotonic() - start
    contents = json.dumps(result, indent=2) + '\n'
    if args.output:
        Path(args.output).write_text(contents)
    print(contents)


if __name__ == '__main__':
    main()
