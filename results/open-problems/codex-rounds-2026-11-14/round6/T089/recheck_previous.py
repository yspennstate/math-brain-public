#!/usr/bin/env python3
"""Independent exact audit of round 5's target remainder. Standard library."""
from fractions import Fraction as Q
from math import factorial, isqrt, comb
from pathlib import Path
import json
import os
import resource
import time

START = time.monotonic()
P = Q(22, 7)


def guard():
    assert os.environ['OMP_NUM_THREADS'] == '1'
    assert os.getpriority(os.PRIO_PROCESS, 0) >= 15
    assert time.monotonic() - START < 120
    assert resource.getrusage(resource.RUSAGE_SELF).ru_maxrss < 256*1024**2


def formula(r, k):
    degree = k*(k-1)//2
    f = 1
    for j in range(k):
        f *= factorial(j)
    a = Q(k-1, 4) + sum((Q(1, j*j) for j in range(1, k+1)), Q(0))
    d = a**k
    for i in range(1, k+1):
        d *= Q(k, i*i) + P**2*sum(
            (Q(1, (i+j)**2) for j in range(1, k+1) if j != i), Q(0))
    return (Q(2**(k-1), factorial(k)*f)**4 * k**(2*k)
            * r**(4*(k+degree)) * (P/4)**(4*degree) * d)


def matrix_product(r, k):
    # Fill the entire majorant in grouped (u_1,...,u_k,v_1,...,v_k) order.
    matrix = [[Q(0)]*(2*k) for _ in range(2*k)]
    for i in range(k):
        for j in range(k):
            matrix[i][k+j] = matrix[k+j][i] = Q(1, j+1)
            if i != j:
                matrix[i][j] = Q(1, 2)
                matrix[k+i][k+j] = P/(i+j+2)
    result = Q(1)
    for row in matrix:
        result *= sum((v*v for v in row), Q(0))
    # Integrate the Chebyshev column norm bound and congruence factors.
    # Form all fourth powers incrementally, without K, F_k or factorial().
    for i in range(1, k+1):
        result *= (r/i)**4 * k*k
        if i > 1:
            result *= 16
        for j in range(1, i):
            result *= (r*P/(4*j))**4
    return result


def main():
    guard()
    cases = 0
    firsts = []
    for r in (Q(1, 2), Q(1), Q(2)):
        first = None
        for k in range(1, 25):
            guard()
            value = formula(r, k)
            assert value == matrix_product(r, k)
            cases += 1
            if k % 2 == 0 and first is None and value < Q(1, 10**24):
                first = k
        firsts.append(first)
    assert firsts == [6, 8, 10]
    q10, q20 = formula(Q(2), 10), formula(Q(2), 20)
    assert Q(517385, 10**12)**4 < q10 < Q(517386, 10**12)**4
    assert q20 < Q(1, 10**356)
    saved = json.loads(Path('~/codex_op_1114r5/briefs/T089/repulsion_data.json').read_text())
    assert q10 == Q(saved['constants']['R2_order10_fourth_power'])
    assert q20 == Q(saved['constants']['R2_order20_fourth_power'])
    identities = 0
    for n in range(65):
        for m in range(21):
            s = sum((-1)**j*comb(n, j) for j in range(min(m, n)+1))
            answer = 1 if n == 0 else (-1)**m*(comb(n-1, m) if m < n else 0)
            assert s == answer
            identities += 1
    guard()
    result = dict(previous_result_holds=True, exact_formula_vs_matrix_checks=cases,
                  first_even_orders=firsts, order10_enclosure_holds=True,
                  order20_less_than_1e_minus89=True, saved_fractions_match=True,
                  binomial_identities=identities,
                  nice=os.getpriority(os.PRIO_PROCESS, 0),
                  peak_rss_bytes_macos=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
                  elapsed_seconds=round(time.monotonic()-START, 3))
    Path(__file__).with_name('recheck_data.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, sort_keys=True))


if __name__ == '__main__':
    main()
