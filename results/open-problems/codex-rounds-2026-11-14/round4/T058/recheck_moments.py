"""Independent Walsh-expansion recheck of round 3, using exact integers."""
import json
import math
import os
import resource
import time
from decimal import Decimal, localcontext
from fractions import Fraction
from pathlib import Path

assert os.environ.get('OMP_NUM_THREADS') == '1'
assert os.getpriority(os.PRIO_PROCESS, 0) >= 15
started = time.monotonic()


def e(j):
    return j * (j - 1) // 2


def choose(n, j):
    return math.comb(n, j) if 0 <= j <= n else 0


def at_phase(exponent, phase):
    # Bisection in log_2(n), unlike round 3's Newton solve in log(n).
    with localcontext() as ctx:
        ctx.prec = 140
        ell = Decimal(2).ln()

        def f(x):
            return 2*x - 2*x.ln()/ell + 2/ell - 1

        target = int(f(Decimal(exponent))) + Decimal(phase)
        lo, hi = Decimal(exponent-2), Decimal(exponent+2)
        assert f(lo) < target < f(hi)
        for _ in range(470):
            mid = (lo+hi)/2
            if f(mid) < target:
                lo = mid
            else:
                hi = mid
        n = int((ell*(lo+hi)/2).exp().to_integral_value())
        actual = f(Decimal(n).ln()/ell)
        return n, int(actual), str(actual-int(actual))


def support_counts(K):
    # a[v] counts edge subsets on v labelled vertices without isolated vertices.
    # Partition all graphs by their set of non-isolated vertices.
    a = [1]
    for v in range(1, K+1):
        a.append(2**e(v)-sum(choose(v, u)*a[u] for u in range(v)))
    assert a[1:5] == [0, 1, 4, 41][:min(4, K)]
    return a


def pair(n, K, l, a):
    # Orthogonality of products of independent fair +/-1 edge variables gives
    # Cov(X_K,X_l)/mu_K = 2^(-e(l)) * W.
    W = sum(choose(K, v)*a[v]*choose(n-v, l-v) for v in range(2, l+1))
    # Separately compare against direct conditioning on |A intersect B|.
    S = sum(choose(K, j)*choose(n-K, l-j)*(2**e(j)-1)
            for j in range(2, l+1))
    assert W == S
    endpoint = choose(K, l)
    ratio = Fraction(W, endpoint*2**e(l))
    return {'K': K, 'l': l,
            'ratio_to_containment_scale': float(ratio),
            'excess_over_one': float(ratio-1)}


rows = []
for exponent, phase in [(80, '.25'), (80, '.5'), (80, '.75'),
                         (160, '.75'), (320, '.75')]:
    n, k, t = at_phase(exponent, phase)
    a = support_counts(k)
    checks = [pair(n, K, l, a) for K, l in [(k,k), (k-1,k-1), (k,k-1)]]
    rows.append({'target_phase': phase, 'phase': t, 'log2_n': math.log2(n),
                 'k': k, 'checks': checks})

result = {'status': 'all Walsh/overlap identities passed',
          'nice': os.getpriority(os.PRIO_PROCESS, 0), 'rows': rows,
          'elapsed_seconds': time.monotonic()-started,
          'peak_rss_bytes': resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}
Path('recheck_moments.json').write_text(json.dumps(result, indent=2)+'\n')
print(json.dumps(result, indent=2))
