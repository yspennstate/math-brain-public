#!/usr/bin/env python3
"""Exact arithmetic, cross-method checks, and direct small-n character sums."""
import csv
import json
import os
from fractions import Fraction as Q
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PREVIOUS = Path('~/codex_op_1114/briefs/T142')


def subsequences(x, n):
    out = {()}
    for i in range(n):
        out |= {s + ((x >> i) & 1,) for s in out}
    return out


def read(path):
    return [json.loads(line) for line in path.read_text().splitlines()]


def main():
    assert os.environ.get('OMP_NUM_THREADS') == '1'
    assert os.getpriority(os.PRIO_PROCESS, 0) >= 15
    primary = read(ROOT / 'stream_bits.jsonl')
    secondary = read(ROOT / 'stream_dp.jsonl')
    old = read(PREVIOUS / 'results_bits.jsonl')
    assert [r['n'] for r in primary] == list(range(1, 17))
    assert len(secondary) == 10
    assert primary[:10] == secondary
    for r, earlier in zip(primary[:12], old):
        for key, value in r.items():
            assert value == earlier[key], (r['n'], key)

    rows, coefficients = [], []
    previous_mean = Q(0)
    for r in primary:
        n, M = r['n'], r['pairs']
        assert M == 4**n == sum(r['hist'])
        s1 = sum(k*h for k, h in enumerate(r['hist']))
        s2 = sum(k*k*h for k, h in enumerate(r['hist']))
        assert s1 == r['sum'] and s2 == r['sum2']
        mu = Q(s1, M)
        var = Q(s2, M) - mu**2
        centered = sum(h*(Q(k)-mu)**2 for k, h in enumerate(r['hist']))/M
        assert var == centered
        # A third moment formula uses pairwise differences of histogram bins.
        difference = sum(h*g*(j-k)**2 for j, h in enumerate(r['hist'])
                         for k, g in enumerate(r['hist'])) / Q(2*M*M)
        assert var == difference
        c = {(i, j): v for i, j, v in r['quadratic']}
        assert len(c) == n*(2*n-1)
        assert all(0 <= i < j < 2*n for i, j in c)
        a = {(i, j): Q(c[i, j], M) for i in range(n) for j in range(i+1, n)}
        b = {(i, j): Q(c[i, n+j], M) for i in range(n) for j in range(n)}
        same = sum(x*x for x in a.values())
        cross = sum(x*x for x in b.values())
        assert same == Q(r['same_mass'], M*M)
        assert cross == Q(r['cross_mass'], M*M)
        w2 = 2*same + cross
        assert w2 == sum(Q(v, M)**2 for v in c.values())
        assert all(c[i, j] == c[n+i, n+j] for i, j in a)
        assert all(b[i, j] == b[j, i] for i, j in b)
        assert all(a[i, j] == a[n-1-j, n-1-i] for i, j in a)
        assert all(b[i, j] == b[n-1-i, n-1-j] for i, j in b)
        boundary = 1 + previous_mean - mu
        assert b[0, 0] == b[n-1, n-1] == boundary
        assert all(a[0, j] == -b[j, 0] for j in range(1, n))
        assert all(a[i, n-1] == -b[i, n-1] for i in range(n-1))
        previous_mean = mu
        derivative = 2*sum(a[i, i+1] for i in range(n-1))
        assert derivative == Q(r['adjacent'], M)
        markov_lower = derivative**2 / (2*(n-1)) if n > 1 else Q(0)
        word_lower = 2*(Q(r['conditional_sum_squares'], 2**(3*n))-mu**2)
        assert 0 <= markov_lower <= 2*same <= word_lower <= var <= Q(n, 4)
        assert 0 <= w2 <= var
        if n <= 5:
            # Neither a dynamic program nor a Walsh transform is used here.
            m = 2**n
            sets = [subsequences(x, n) for x in range(m)]
            scores = [max(map(len, sets[x] & sets[y]))
                      for x in range(m) for y in range(m)]
            assert [scores.count(k) for k in range(n+1)] == r['hist']
            direct = {}
            for i, j in c:
                direct[i, j] = sum(l*(-1 if (((x | (y << n)) >> i)
                                   ^ ((x | (y << n)) >> j)) & 1 else 1)
                                   for x in range(m) for y in range(m)
                                   for l in [scores[x*m+y]])
            assert direct == c
        rows.append(dict(n=n, pairs=M, mean=str(mu), variance=str(var),
                         variance_over_n=str(var/n), W2=str(w2),
                         W2_over_variance=str(w2/var),
                         same_word_quadratic=str(2*same), cross_word_quadratic=str(cross),
                         conditional_word_lower=str(word_lower),
                         markov_derivative=str(derivative),
                         markov_derivative_over_n=str(derivative/n),
                         markov_lower=str(markov_lower), boundary_coefficient=str(boundary)))
        coefficients.extend(dict(n=n, i=i, j=j, numerator=v, denominator=M)
                            for (i, j), v in c.items())
        print(f'n={n:2d} variance={float(var):.10f} W2={float(w2):.10f} '
              f'W2/variance={float(w2/var):.8f} Fprime/n={float(derivative/n):.8f} PASS')
    for name, data in [('summary.csv', rows), ('quadratic.csv', coefficients)]:
        with (ROOT / name).open('w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=list(data[0]))
            writer.writeheader()
            writer.writerows(data)
    out = dict(verdict='PASS', streaming_max_n=16, independent_dp_max_n=10,
               earlier_full_cube_agreement_max_n=12,
               literal_subsequence_and_direct_character_max_n=5,
               total_pairs=sum(r['pairs'] for r in primary),
               exact_checks=['three variance formulas', 'quadratic mass from explicit coefficients',
                             'direct adjacent sum', 'both boundary identities',
                             'word exchange and reversal', 'projection inequalities'])
    (ROOT / 'audit.json').write_text(json.dumps(out, indent=2)+'\n')
    print(json.dumps(out))


if __name__ == '__main__':
    main()
