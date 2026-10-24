#!/usr/bin/env python3
"""Exact finite self-checks for the all-m theorem in ADDRESSING_BARRIER_2026-09-18.md.

No floating arithmetic in decisions. NumPy, when available, only supplies int64
Walsh transforms for the 21-variable (m=4) truth table. m=2 is stdlib-only.
The large-m entries evaluate the proved formula, not a truth-table enumeration.
"""
from collections import Counter
from fractions import Fraction as F
from math import isqrt
from pathlib import Path
import json

from certify_nand80 import wht, IV, edge, rational_interval


def bent(x, m):
    parity = sum(((x >> j) & 1) * ((x >> (j+1)) & 1)
                 for j in range(0, m, 2)) % 2
    return 1 - 2*parity


def full_walsh(m, numpy=False):
    N = 1 << m
    n = m + 1 + N
    size = 1 << n
    if not numpy:
        values = []
        for t in range(size):
            x = t & (N-1)
            values.append(bent(x, m) if not (t & (1 << m))
                          else 1-2*((t >> (m+1+x)) & 1))
        return wht(values)
    import numpy as np
    indices = np.arange(size, dtype=np.uint64)
    x = indices & (N-1)
    parity = np.zeros(size, dtype=np.uint64)
    for j in range(0, m, 2):
        parity ^= ((x >> j) & 1) & ((x >> (j+1)) & 1)
    addressed = (indices >> (m+1+x)) & 1
    bits = np.where((indices >> m) & 1, addressed, parity)
    a = 1 - 2*bits.astype(np.int64)
    step = 1
    while step < size:
        rows = a.reshape(-1, 2*step)
        u, v = rows[:, :step].copy(), rows[:, step:].copy()
        rows[:, :step] = u+v
        rows[:, step:] = u-v
        step *= 2
    return a


def expected_coefficients(m):
    N = 1 << m
    gw = wht([bent(x, m) for x in range(N)])
    assert all(t*t == N for t in gw)
    coeff = {}
    for S in range(N):
        for z in [0, 1]:
            base = S | (z << m)
            coeff[base] = F(gw[S], 2*N)
            for a in range(N):
                sign = 1-2*((z+(S & a).bit_count()) % 2)
                coeff[base | (1 << (m+1+a))] = F(sign, 2*N)
    return coeff


def fourth_root(x):
    a, b = isqrt(isqrt(x.numerator)), isqrt(isqrt(x.denominator))
    assert a**4 == x.numerator and b**4 == x.denominator
    return F(a, b)


def check(m, numpy=False):
    N = 1 << m
    n = m+1+N
    size = 1 << n
    raw = full_walsh(m, numpy=numpy)
    observed = {s: F(int(v), size) for s, v in enumerate(raw) if v}
    expected = expected_coefficients(m)
    assert observed == expected
    assert len(observed) == 2*N+2*N*N
    p = {s: v*v for s, v in observed.items()}
    assert sum(p.values(), F(0)) == 1
    influence = sum((s.bit_count()*v for s, v in p.items()), F(0))
    assert influence == F(m+2, 2)
    marginals = [sum((v for s, v in p.items() if s & (1 << i)), F(0))
                 for i in range(n)]
    assert marginals == [F(1, 2)]*(m+1)+[F(1, 2*N)]*N
    hist = Counter()
    for s, ps in p.items():
        for i in range(n):
            if not (s & (1 << i)) and (s | (1 << i)) in p:
                hist[tuple(sorted((ps, p[s | (1 << i)])))] += 1
    big, small = F(1, 4*N), F(1, 4*N*N)
    expected_hist = Counter({(big, big): (m+1)*N,
                             (small, small): (m+1)*N*N,
                             (small, big): 2*N*N})
    assert hist == expected_hist
    minimum_sum = sum((r*count for (r, s), count in hist.items()), F(0))
    assert minimum_sum == influence
    logarithmic_cost = F(m, 2)  # only unequal pairs; log2(big/small)=m
    assert hist[(small, big)]*small*m == logarithmic_cost
    entropy = F(0)
    for v in p.values():
        assert v.numerator == 1 and v.denominator & (v.denominator-1) == 0
        entropy += v*(v.denominator.bit_length()-1)
    assert entropy == F(4+3*m, 2)
    B = sum((edge(r, s)*count for (r, s), count in hist.items()), IV(0))
    formula_B = IV(m+1)+edge(F(N), F(1))*F(1, 2)
    assert max(B.lo, formula_B.lo) <= min(B.hi, formula_B.hi)
    assert B.hi < entropy
    convolution_checks = 0
    if m == 2:
        for U in range(size):
            total = sum((v*observed.get(S ^ U, F(0))
                         for S, v in observed.items()), F(0))
            assert total == int(U == 0)
            convolution_checks += 1
    quarter = None
    if m % 4 == 0:
        quarter = sum((fourth_root(r**3*s)*count
                       for (r, s), count in hist.items()), F(0))
        assert quarter == F(m+1+(1 << (m//4)), 2)
    return {'m': m, 'N': N, 'dimension': n,
            'full_truth_table_entries': size,
            'integer_walsh_backend': 'numpy.int64' if numpy else 'python int',
            'all_signed_coefficients_match': True,
            'nonzero_coefficients': len(observed),
            'edge_histogram': [{'smaller': str(r), 'larger': str(s), 'count': c}
                               for (r, s), c in sorted(hist.items())],
            'I': str(influence), 'H': str(entropy), 'K': str(logarithmic_cost),
            'B_interval': rational_interval(B),
            'T_one_quarter_exact': str(quarter) if quarter is not None else None,
            'signed_convolution_identities_checked': convolution_checks}


def main():
    checks = [check(2)]
    try:
        import numpy  # noqa: F401
    except ImportError:
        extra_status = 'm=4 not run: optional NumPy unavailable'
    else:
        checks.append(check(4, numpy=True))
        extra_status = 'm=4 full truth table checked with integer arithmetic'
    ratios = []
    for m in [4, 16, 32, 64, 128]:
        ratio = F(m+1+(1 << (m//4)), m+2)
        ratios.append({'m': m, 'formal_dimension': m+1+(1 << m),
                       'T_one_quarter_over_I': str(ratio),
                       'evaluation': 'exact formula; not full enumeration'})
    result = {'status': 'PASS', 'arithmetic': 'exact integers and rational intervals',
              'full_transform_checks': checks, 'optional_check': extra_status,
              'formula_ratio_examples': ratios,
              'proof_scope': 'All positive gamma fail by the analytic all-m proof; finite checks are self-checks, not independent audits or universal enumeration.',
              'FEI_status': 'OPEN; this family has H/I < 3'}
    Path('addressing_barrier_certificate.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
