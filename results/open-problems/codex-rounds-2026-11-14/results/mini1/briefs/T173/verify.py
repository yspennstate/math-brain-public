#!/usr/bin/env python3
"""Exact finite-state coefficient checks; no simulation or third-party imports."""
import os
import resource
import json
from fractions import Fraction as F
from itertools import product
from pathlib import Path
from time import monotonic

os.environ['OMP_NUM_THREADS'] = '1'
resource.setrlimit(resource.RLIMIT_CPU, (60, 60))
# The complete computation uses ten-state matrices; peak RSS is reported below.
# This sandbox rejects changes to the advisory macOS RLIMIT_RSS.


def poly_mul(a, b):
    out = [F(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i+j] += x*y
    return out


def solve(a, b):
    """Rational Gauss-Jordan elimination."""
    n = len(b)
    aug = [list(a[i]) + [b[i]] for i in range(n)]
    for j in range(n):
        k = next(i for i in range(j, n) if aug[i][j])
        aug[j], aug[k] = aug[k], aug[j]
        pivot = aug[j][j]
        aug[j] = [x/pivot for x in aug[j]]
        for i in range(n):
            if i != j:
                q = aug[i][j]
                aug[i] = [x-q*y for x, y in zip(aug[i], aug[j])]
    return [r[-1] for r in aug]


def coefficients(p, p_tag, arrival_scale, closure):
    m = len(p)
    states = [q for q in product(range(3), repeat=m) if sum(q) <= 2]
    states.sort(key=lambda q: (sum(q), q))
    idx = {q: i for i, q in enumerate(states)}
    n = len(states)
    matrices = [[[F(0) for _ in states] for _ in states] for _ in range(max(m, 2)+1)]
    # Enumerate every light/tagged coin and every arrival vector independently.
    for u, q in enumerate(states):
        for coins in product((0, 1), repeat=m+1):
            coin_prob = F(1)
            for coin, prob in zip(coins, list(p)+[p_tag]):
                coin_prob *= prob if coin else 1-prob
            active = [i for i in range(m) if q[i] and coins[i]]
            after = list(q)
            if not coins[-1] and len(active) == 1:
                after[active[0]] -= 1
            for arrivals in product((0, 1), repeat=m):
                polynomial = [coin_prob]
                for bit, a in zip(arrivals, arrival_scale):
                    polynomial = poly_mul(polynomial, [F(0), a] if bit else [F(1), -a])
                nxt = tuple(x+y for x, y in zip(after, arrivals))
                if sum(nxt) > 2:
                    nxt = (0,)*m if closure == 'reset' else q
                v = idx[nxt]
                for degree, coefficient in enumerate(polynomial):
                    matrices[degree][u][v] += coefficient
    # Each row is a probability polynomial with total exactly one.
    for degree, matrix in enumerate(matrices):
        for row in matrix:
            assert sum(row) == (1 if degree == 0 else 0)
    base = [[F(i == j)-matrices[0][j][i] for j in range(n)] for i in range(n)]
    base[-1] = [F(1)] * n
    stationary = []
    for degree in range(3):
        rhs = [F(0)]*n
        for r in range(1, degree+1):
            for j in range(n):
                rhs[j] += sum(stationary[degree-r][i]*matrices[r][i][j] for i in range(n))
        rhs[-1] = F(degree == 0)
        v = solve(base, rhs)
        # Check all balance equations, including the one replaced by normalization.
        for j in range(n):
            lhs = v[j]-sum(v[i]*matrices[0][i][j] for i in range(n))
            expected = sum(stationary[degree-r][i]*matrices[r][i][j]
                           for r in range(1, degree+1) for i in range(n))
            assert lhs == expected
        stationary.append(v)
    observable = [p_tag * prod(1-p[i] for i in range(m) if q[i]) for q in states]
    mu = [sum(x*y for x, y in zip(v, observable)) for v in stationary]
    pairs = {}
    for i in range(m):
        for j in range(i+1, m):
            pairs[f'{i+1},{j+1}'] = [sum(v[k] for k, q in enumerate(states) if q[i] and q[j])
                                    for v in stationary]
    return {'states': states, 'stationary_coefficients': stationary, 'mu': mu, 'pairs': pairs}


def prod(xs):
    out = F(1)
    for x in xs:
        out *= x
    return out


def formula(p, p_tag, a):
    c = 1-p_tag
    quadratic = -p_tag/c**2 * sum(a[i]*a[j]*(p[i]+p[j]-c*p[i]*p[j]) /
                                 (p[i]+p[j]-2*p[i]*p[j])
                                 for i in range(len(p)) for j in range(i+1, len(p)))
    return [p_tag, -p_tag*sum(a)/c, quadratic]


def encode(x):
    if isinstance(x, F):
        return str(x)
    if isinstance(x, dict):
        return {k: encode(v) for k, v in x.items()}
    if isinstance(x, (list, tuple)):
        return [encode(y) for y in x]
    return x


def main():
    t0 = monotonic()
    assert os.getpriority(os.PRIO_PROCESS, 0) >= 15
    cases = [
        ('four_half', [F(1,2)]*3, F(1,2), [F(1)]*3),
        ('four_quarter', [F(1,4)]*3, F(1,4), [F(1)]*3),
        ('four_asymmetric', [F(1,3), F(2,5), F(1,4)], F(2,7), [F(1), F(2), F(3)]),
        ('two_user_sanity', [F(2,5)], F(1,3), [F(2)]),
    ]
    data = {}
    for name, p, tag, a in cases:
        r = coefficients(p, tag, a, 'reset')
        h = coefficients(p, tag, a, 'hold')
        assert r == h, 'The two overflow rules must agree through degree two.'
        assert r['mu'] == formula(p, tag, a)
        c = 1-tag
        for i in range(len(p)):
            for j in range(i+1, len(p)):
                expected = a[i]*a[j]*(p[i]+p[j]-c*p[i]*p[j]) / (c*c*p[i]*p[j]*(p[i]+p[j]-2*p[i]*p[j]))
                assert r['pairs'][f'{i+1},{j+1}'] == [0, 0, expected]
        data[name] = {'p_light': p, 'p_tag': tag, 'arrival_scale': a, **r}
        print(name, 'mu coefficients:', ', '.join(map(str, r['mu'])))
        for key, val in r['pairs'].items():
            print('  pair', key, 'quadratic coefficient:', val[2])

    delta, g0, beta0 = F(3,16), F(33,32)**3, F(55,64)*F(33,32)**3
    moment_bound = delta*g0/(1-beta0)
    assert moment_bound < 4
    tail2, tail3 = 4*32**2, 4*32**3
    error_terms = {'empty': 17, 'singletons_i_j': 2*(F(3,4)*8192 + 16*2),
                   'singleton_k': 4, 'other_level_two': 3*tail2,
                   'level_three_and_above': tail3, 'diagonal': 3*tail2}
    pair_state_error = 4*sum(error_terms.values())
    pair_busy_error = pair_state_error + tail3
    service_error = (3*pair_busy_error + tail3)/8
    assert pair_state_error == 672084 and pair_busy_error == 803156
    assert service_error == F(635135,2) < 400000
    print('moment bound:', moment_bound, '< 4')
    print('pair busy remainder constant:', pair_busy_error)
    print('service remainder constant:', service_error, '< 400000')

    e = F(1, 10**6)
    tagged = F(1,2)-3*e-8*e**2
    center = F(1,2)-3*e-F(21,2)*e**2
    upper = center+400000*e**3
    lower = center-400000*e**3
    assert 0 < e <= F(1,128) and tagged > upper
    # Explicit boundary witness for the downward independent-queue region.
    x = 2*e+9*e**2
    rho = 2*x
    light_boundary = x*(1-x)**2/2
    tag_boundary = (1-x)**3/2
    assert 0 < rho < 1
    assert light_boundary > e and tag_boundary > tagged
    data['certificate'] = {'epsilon': e, 'tagged_arrival': tagged,
                           'service_lower': lower, 'service_upper': upper,
                           'unstable_margin': tagged-upper, 'rho_light': rho,
                           'independent_light_boundary': light_boundary,
                           'independent_tag_boundary': tag_boundary,
                           'light_slack': light_boundary-e, 'tag_slack': tag_boundary-tagged,
                           'moment_bound': moment_bound, 'pair_error_terms': error_terms,
                           'pair_busy_error': pair_busy_error, 'service_error': service_error}
    print('epsilon:', e)
    print('tagged arrival:', tagged, '=', format(float(tagged), '.15f'))
    print('certified service interval:', lower, upper)
    print('unstable margin:', tagged-upper)
    print('independent boundary light slack:', light_boundary-e)
    print('independent boundary tagged slack:', tag_boundary-tagged)
    Path('verification.json').write_text(json.dumps(encode(data), indent=2)+'\n')
    print('ALL EXACT CHECKS PASSED')
    print('elapsed seconds:', round(monotonic()-t0, 3))
    print('peak RSS bytes (macOS):', resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)


if __name__ == '__main__':
    main()
