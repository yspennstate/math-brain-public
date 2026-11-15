"""Exhaustive packing checks and exact overlap-sum audits; standard library only."""

import itertools
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


def e(k):
    return k*(k-1)//2


def choose(n, k):
    return math.comb(n, k) if 0 <= k <= n else 0


def exact_expectation(n, k):
    mu = Fraction(choose(n, k), 2**e(k))
    # Direct union-of-edge-constraints count, including the unordered-pair factor.
    by_overlap = [Fraction(choose(n, k)*choose(k, j)*choose(n-k, k-j),
                           2**(2*e(k)-e(j)+1)) for j in range(1, k)]
    return mu, by_overlap


def packing_dp(family, n):
    # dp[S] = best packing contained in S. Either leave its least vertex unused,
    # or use one family member containing that vertex.
    by_vertex = [[A for A in family if A & (1 << v)] for v in range(n)]
    dp = [0]*(1 << n)
    for S in range(1, 1 << n):
        bit = S & -S
        v = bit.bit_length()-1
        best = dp[S ^ bit]
        for A in by_vertex[v]:
            if A & S == A:
                best = max(best, 1+dp[S ^ A])
        dp[S] = best
    return dp[-1]


def brute_packing(family, n, k):
    # Independent search over subfamilies, capped by the vertex budget.
    for count in range(n//k, 0, -1):
        for candidate in itertools.combinations(family, count):
            union = 0
            for A in candidate:
                if union & A:
                    break
                union |= A
            else:
                return count
    return 0


def exhaustive(n):
    edges = list(itertools.combinations(range(n), 2))
    graphs = 1 << len(edges)
    k_values = range(2, n+1)
    sums = {k: {'X': 0, 'M': 0, 'Y': [0]*(k-1), 'deficit_max': 0}
            for k in k_values}
    for graph in range(graphs):
        adjacency = [0]*n
        for index, (u, v) in enumerate(edges):
            if graph & (1 << index):
                adjacency[u] |= 1 << v
                adjacency[v] |= 1 << u
        independent = [True]*(1 << n)
        families = {k: [] for k in k_values}
        for S in range(1, 1 << n):
            bit = S & -S
            rest = S ^ bit
            independent[S] = independent[rest] and not (adjacency[bit.bit_length()-1] & rest)
            k = S.bit_count()
            if independent[S] and k >= 2:
                families[k].append(S)
        for k, family in families.items():
            X = len(family)
            M = packing_dp(family, n)
            # Every packing in this enumeration is checked by a second algorithm.
            assert M == brute_packing(family, n, k)
            by_overlap = [0]*(k-1)
            weighted_conflicts = 0
            for A, B in itertools.combinations(family, 2):
                j = (A & B).bit_count()
                if j:
                    by_overlap[j-1] += 1
                    weighted_conflicts += j
            Y = sum(by_overlap)
            assert 0 <= X-M <= Y
            # Independent incidence double count, including multiple intersections.
            degrees = [sum(bool(A & (1 << v)) for A in family) for v in range(n)]
            assert sum(d*(d-1)//2 for d in degrees) == weighted_conflicts
            row = sums[k]
            row['X'] += X
            row['M'] += M
            row['deficit_max'] = max(row['deficit_max'], X-M)
            for j, count in enumerate(by_overlap):
                row['Y'][j] += count
    rows = []
    for k, row in sums.items():
        mu, formula = exact_expectation(n, k)
        assert Fraction(row['X'], graphs) == mu
        observed = [Fraction(y, graphs) for y in row['Y']]
        assert observed == formula
        deficit = Fraction(row['X']-row['M'], graphs)
        assert deficit <= sum(formula)
        rows.append({'k': k, 'mean_X': str(mu), 'mean_M': str(Fraction(row['M'], graphs)),
                     'mean_deficit': str(deficit), 'mean_Y': str(sum(formula)),
                     'mean_Y_by_overlap': [str(x) for x in formula],
                     'maximum_deficit': row['deficit_max']})
    return {'n': n, 'graphs': graphs, 'rows': rows}


def at_phase(exponent, phase):
    with localcontext() as ctx:
        ctx.prec = 130
        ell = Decimal(2).ln()
        C = 1+ell.ln()
        L = Decimal(exponent)*ell
        f = 2/ell*(L-L.ln()+C)-1
        target = int(f)+Decimal(phase)
        for _ in range(15):
            residual = 2/ell*(L-L.ln()+C)-1-target
            L -= residual/(2/ell*(1-1/L))
        assert abs(2/ell*(L-L.ln()+C)-1-target) < Decimal('1e-110')
        n = int(L.exp().to_integral_value())
        actual = 2/ell*(Decimal(n).ln()-Decimal(n).ln().ln()+C)-1
        return n, int(actual), str(actual-int(actual))


def asymptotic_audit(exponent, phase):
    n, k, actual_phase = at_phase(exponent, phase)
    denominator = 2**e(k)
    mu = Fraction(choose(n, k), denominator)
    # Start with complete intersection and descend using a hypergeometric ratio.
    coefficients = [0]*(k+1)
    coefficients[k] = 1
    for j in range(k, 0, -1):
        numerator = coefficients[j]*j*(n-2*k+j)
        divisor = (k-j+1)**2
        coefficients[j-1], remainder = divmod(numerator, divisor)
        assert remainder == 0
    assert sum(coefficients) == choose(n, k)
    for j in {0, 1, 2, k//2, k-1, k}:
        assert coefficients[j] == choose(k, j)*choose(n-k, k-j)
    h = [Fraction(coefficients[j], 2**(e(k)-e(j))) for j in range(k+1)]
    EY = mu*sum(h[1:k])/2
    leading = mu**2*Fraction(k*k, 2*n)
    one_ratio = Fraction(choose(n-k, k-1), choose(n-1, k-1))
    assert mu*h[1]/2/leading == one_ratio
    product_ratio = Fraction(1)
    for i in range(k-1):
        product_ratio *= Fraction(n-k-i, n-1-i)
    assert one_ratio == product_ratio
    assert 1-Fraction((k-1)**2, n-k+1) <= one_ratio <= 1

    m, mp = k//2, (k+1)//2
    A = Fraction(k*k, n-k)
    B = Fraction(k*n, 2**k)
    v2, vm = A**2*2, A**m*2**e(m)
    w1, wmp = 2*B, B**mp*2**(mp*(mp+1)//2)
    assert sum(h[2:m+1]) <= mu*m*max(v2, vm)
    assert sum(h[m+1:k]) <= mp*max(w1, wmp)
    assert vm <= v2 and wmp <= w1
    finite_upper = mu**2*Fraction(k*k, 2*n)+mu**2*m*max(v2, vm)/2+mu*mp*max(w1, wmp)/2
    assert EY <= finite_upper
    sqrt_mu = math.sqrt(float(mu))
    return {'log2_n': math.log2(n), 'target_phase': phase, 'actual_phase': actual_phase,
            'k': k, 'mean': float(mu), 'EY_over_leading': float(EY/leading),
            'EY1_over_leading_minus_one': float(one_ratio-1),
            'larger_overlap_over_leading': float(mu*sum(h[2:k])/2/leading),
            'EY_over_sqrt_mean': float(EY)/sqrt_mu,
            'leading_over_sqrt_mean': float(leading)/sqrt_mu,
            'finite_upper_over_sqrt_mean': float(finite_upper)/sqrt_mu}


small = [exhaustive(5), exhaustive(6)]
large = [asymptotic_audit(exponent, phase)
         for exponent, phase in [(40, '.5'), (80, '.5'), (160, '.5'),
                                 (80, '.625'), (160, '.625'), (320, '.625'),
                                 (80, '.75'), (160, '.75'), (320, '.75')]]
result = {'status': 'all exact packing and overlap checks passed',
          'nice': os.getpriority(os.PRIO_PROCESS, 0), 'small_graphs': small,
          'asymptotic_diagnostics': large, 'elapsed_seconds': time.monotonic()-started,
          'peak_rss_bytes': resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}
Path('packing_verification.json').write_text(json.dumps(result, indent=2)+'\n')
print(json.dumps(result, indent=2))
