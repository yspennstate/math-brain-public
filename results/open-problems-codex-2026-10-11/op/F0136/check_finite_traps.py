"""Deterministic checks; no simulation can certify nonzero asymptotic speed."""
from pathlib import Path
import json, math, time

start = time.monotonic()
grid = [(x, y) for x in range(4) for y in range(4)]
weight_tests = [(1, 1), (1, 3), (3, 1), (2, 5), (5, 2)]
tested = 0
for mask in range(1, 1 << 16):
    S = {grid[i] for i in range(16) if mask >> i & 1}
    n = len(S)
    R = sum((x-1, y) not in S for x, y in S)
    C = sum((x, y-1) not in S for x, y in S)
    r = len({y for x, y in S})
    c = len({x for x, y in S})
    assert n <= r*c <= R*C
    for s, t in weight_tests:
        beta = s*R+t*C
        direct = sum(s for x, y in S if (x+1, y) not in S)
        direct += sum(t for x, y in S if (x, y+1) not in S)
        assert beta == direct  # one edge per orientation; opposing weights add
        kappa = s+t+min(s, t)
        if n >= 2:
            assert beta >= kappa
            if beta == kappa:
                assert n == 2
                u, v = tuple(S)
                assert abs(u[0]-v[0])+abs(u[1]-v[1]) == 1
        if n >= 3:
            assert beta >= kappa+min(s, t)
        assert beta*beta >= 4*s*t*n
        tested += 1

series = []
for scale in (0.9, 1.0, 1.01, 1.1, 1.5):
    alpha = [scale*x for x in (0.31, 0.1, 0.29, 0.1)]
    A = sum(alpha)
    a, b = alpha[0], alpha[2]
    k = 2*A-a-b
    mp = mq = 1.0
    total = 0.0
    values = {}
    final_term = 0.0
    for n in range(100001):
        next_mp = mp*(a+n)/(A+n)
        term = (mp+next_mp)*mq
        total += term
        if n in (100, 1000, 10000, 100000):
            values[str(n)] = total
        final_term = term
        mp = next_mp
        mq *= (b+n)/(A+n)
    const = 2*math.exp(2*math.lgamma(A)-math.lgamma(a)-math.lgamma(b))
    ratio = final_term*(100000**k)/const
    assert abs(ratio-1) < 0.0001
    series.append(dict(alpha=alpha, drift=[alpha[0]-alpha[2],0],
                       pair_exponent=k, partial_mean_series=values,
                       asymptotic_term_ratio=ratio))

result = dict(subsets=65535, weight_tests=weight_tests, algebra_checks=tested,
              pair_series=series, elapsed_seconds=time.monotonic()-start,
              limitation="Finite checks and finite partial sums do not prove ballisticity or moment finiteness.")
Path(__file__).with_name('finite_checks.json').write_text(json.dumps(result, indent=2), encoding='utf-8')
print(json.dumps(result, indent=2))
