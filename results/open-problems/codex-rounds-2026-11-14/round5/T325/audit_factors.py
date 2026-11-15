"""Exact arithmetic checks for scalar, factorized attention.

OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 \
PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3 audit_factors.py

No imports from earlier workers, numerical training, or external libraries.
"""

import math
import os
import random
import resource
import signal
import sys
import time
from fractions import Fraction as Q


def multiply(p, q):
    result = [Q(0)] * (len(p) + len(q) - 1)
    for i, u in enumerate(p):
        for j, v in enumerate(q):
            result[i+j] += u*v
    return result


def residual(steps):
    r = [Q(1)]
    for a in steps:
        r = multiply(r, [Q(1), -a])
    return r


def expectation(poly, moments):
    return sum((c*moments[i] for i, c in enumerate(poly)), Q(0))


def moments_by_recurrence(n, degree):
    result = [Q(1)]
    for j in range(degree):
        result.append(result[-1] * Q(n + 2*j, n))
    return result


def moments_by_gaussians(n, degree):
    # Gaussian integration by parts, then n independent EGF multiplications.
    # n is at most five in calls to this independent implementation.
    even = 1
    egf = [Q(1)]
    for j in range(1, degree + 1):
        even *= 2*j-1
        egf.append(Q(even, math.factorial(j)))
    product = [Q(1)]
    for _ in range(n):
        product = multiply(product, egf)[:degree+1]
    return [product[j]*Q(math.factorial(j), n**j)
            for j in range(degree+1)]


def solve(matrix, rhs):
    rows = [list(row) + [b] for row, b in zip(matrix, rhs)]
    size = len(rhs)
    for i in range(size):
        pivot = next(j for j in range(i, size) if rows[j][i])
        rows[i], rows[pivot] = rows[pivot], rows[i]
        scale = rows[i][i]
        rows[i] = [x/scale for x in rows[i]]
        for j in range(size):
            if j != i:
                scale = rows[j][i]
                rows[j] = [x-scale*y for x, y in zip(rows[j], rows[i])]
    return [row[-1] for row in rows]


def product_derivatives(steps, moments):
    size = len(steps)
    r = residual(steps)
    first = [[Q(0)] + [-c for c in residual(steps[:i]+steps[i+1:])]
             for i in range(size)]
    g = [2*expectation(multiply(r, dr), moments) for dr in first]
    hessian = [[Q(0)]*size for _ in range(size)]
    for i in range(size):
        for j in range(size):
            value = 2*expectation(multiply(first[i], first[j]), moments)
            if i != j:
                remaining = [a for t, a in enumerate(steps) if t not in (i, j)]
                second = [Q(0), Q(0)] + residual(remaining)
                value += 2*expectation(multiply(r, second), moments)
            hessian[i][j] = value
    return expectation(multiply(r, r), moments), g, hessian


def bivariate_multiply(p, q):
    # Sparse coefficient map (power of S, power of perturbation t) -> Fraction.
    out = {}
    for (s, t), a in p.items():
        for (u, v), b in q.items():
            index = (s+u, t+v)
            out[index] = out.get(index, Q(0)) + a*b
    return {key: value for key, value in out.items() if value}


def factor_path_loss(factors, direction, moments):
    # Expand the actual factored residual along a straight factor-space path.
    # No gradient or Hessian formula is used in this computation.
    r = {(0, 0): Q(1)}
    for (k, q), (u, v) in zip(factors, direction):
        term = {(0, 0): Q(1), (1, 0): -k*q,
                (1, 1): -(q*u+k*v), (1, 2): -u*v}
        term = {key: value for key, value in term.items() if value}
        r = bivariate_multiply(r, term)
    squared = bivariate_multiply(r, r)
    out = [Q(0)]*(4*len(factors)+1)
    for (s, t), value in squared.items():
        out[t] += value*moments[s]
    return out


def factor_hessian(factors, gradient, hessian):
    size = len(factors)
    matrix = [[Q(0)]*(2*size) for _ in range(2*size)]
    for i, (k, q) in enumerate(factors):
        for j, (kk, qq) in enumerate(factors):
            for u, bi in enumerate((q, k)):
                for v, bj in enumerate((qq, kk)):
                    matrix[2*i+u][2*j+v] = bi*hessian[i][j]*bj
        # Hessian chain-rule correction, important off product critical points.
        matrix[2*i][2*i+1] += gradient[i]
        matrix[2*i+1][2*i] += gradient[i]
    return matrix


def quadratic(matrix, vector):
    return sum((u*matrix[i][j]*v
                for i, u in enumerate(vector) for j, v in enumerate(vector)), Q(0))


def lift_linear_product_path(factors, product_direction):
    result = []
    for (k, q), value in zip(factors, product_direction):
        assert k or q
        result.append((value/q, Q(0)) if q else (Q(0), value/k))
    return result


def token_update(factors, xs, w, xq):
    # Direct key/query score and label-row contraction, retaining both factors.
    top = xs + [xq]
    labels = [w*x for x in xs] + [Q(0)]
    for k, q in factors:
        keys = [k*x for x in xs]
        queries = [q*x for x in top]
        contraction = sum((y*key for y, key in zip(labels, keys)), Q(0))
        labels = [y-contraction*query/len(xs)
                  for y, query in zip(labels, queries)]
    return -labels[-1]


def run():
    started = time.monotonic()
    priority = os.getpriority(os.PRIO_PROCESS, 0)
    assert priority >= 15
    assert os.environ.get('OMP_NUM_THREADS') == '1'
    print(f'Process nice: {priority}')
    old_soft, old_hard = resource.getrlimit(resource.RLIMIT_CPU)
    soft = 120 if old_hard == resource.RLIM_INFINITY else min(120, old_hard)
    resource.setrlimit(resource.RLIMIT_CPU, (soft, old_hard))
    signal.alarm(120)  # Wall timeout as well as CPU timeout.

    normal_cases = 0
    for n in (1, 2, 5, 100):
        m = moments_by_recurrence(n, 12)
        if n <= 5:
            assert m == moments_by_gaussians(n, 12)
        for depth in range(1, 7):
            matrix = [[m[i+j] for j in range(1, depth+1)]
                      for i in range(1, depth+1)]
            c = [Q(1)] + solve(matrix, [-m[i] for i in range(1, depth+1)])
            squared_risk = expectation(multiply(c, c), m)
            schur_risk = 1+sum((c[i]*m[i] for i in range(1, depth+1)), Q(0))
            product_risk = Q(2**depth*math.factorial(depth),
                             math.prod(n+2*i for i in range(1, depth+1)))
            alpha = Q(n, 2)
            alternating_risk = sum(((-1)**i*math.comb(depth, i)*alpha/(alpha+i)
                                    for i in range(depth+1)), Q(0))
            assert squared_risk == schur_risk == product_risk == alternating_risk
            if n == 2:
                assert squared_risk == Q(1, depth+1)
            normal_cases += 1
    print(f'{normal_cases} normal-system/squared-risk/Schur/binomial checks passed.')

    rng = random.Random(325)
    flow_cases = hessian_cases = token_cases = 0
    for n in (1, 2, 5):
        for depth in range(1, 7):
            m = moments_by_recurrence(n, 2*depth)
            patterns = [
                [(Q(0), Q(0)), (Q(0), Q(2)), (Q(-1), Q(1)),
                 (Q(2), Q(1, 2)), (Q(-3, 2), Q(-2)), (Q(1), Q(0))][:depth],
                [(Q(rng.randint(-3, 3), 2), Q(rng.randint(-3, 3), 2))
                 for _ in range(depth)],
            ]
            for factors in patterns:
                a = [k*q for k, q in factors]
                value, g, hessian = product_derivatives(a, m)
                velocity = [(-q*gi, -k*gi) for (k, q), gi in zip(factors, g)]
                full_hessian = factor_hessian(factors, g, hessian)
                direction = [(Q(i+1, 3), Q(2-i, 5)) for i in range(depth)]
                path = factor_path_loss(factors, direction, m)
                flat_direction = [x for pair in direction for x in pair]
                assert path[0] == value
                assert path[1] == sum(((q*u+k*v)*gi
                                      for (k, q), (u, v), gi in zip(factors, direction, g)), Q(0))
                assert 2*path[2] == quadratic(full_hessian, flat_direction)
                hessian_cases += 1
                for (k, q), (kp, qp), gi in zip(factors, velocity, g):
                    assert 2*k*kp-2*q*qp == 0
                    assert kp*q+k*qp == -(k*k+q*q)*gi
                    assert (k*k+q*q)**2 == (k*k-q*q)**2 + 4*(k*q)**2
                    assert k*k <= abs(k*k-q*q)+abs(k*q)
                    assert q*q <= abs(k*k-q*q)+abs(k*q)
                    flow_cases += 1
                slope = factor_path_loss(factors, velocity, m)[1]
                assert slope == -sum(((k*k+q*q)*gi*gi
                                     for (k, q), gi in zip(factors, g)), Q(0))
                xs, w, xq = [Q(1, 3), Q(-2), Q(5, 4)], Q(-4, 5), Q(7, 3)
                sample_s = sum((x*x for x in xs), Q(0))/len(xs)
                expected = w*xq*(1-math.prod(1-step*sample_s for step in a))
                assert token_update(factors, xs, w, xq) == expected
                token_cases += 1
    print(f'{flow_cases} imbalance/product-speed/boundedness identities passed.')
    print(f'{hessian_cases} independent factor-path Hessian checks; '
          f'{token_cases} token checks passed.')

    zero_cases = repeated_cases = critical_cases = 0
    for n in (1, 2, 5):
        for depth in range(1, 7):
            m = moments_by_recurrence(n, 2*depth)
            for i in range(depth):
                factors = [(Q(j+1, 3), Q(-1 if j % 2 else 2))
                           for j in range(depth)]
                factors[i] = (Q(0), Q(0))
                steps = [k*q for k, q in factors]
                value, g, hessian = product_derivatives(steps, m)
                rest = residual(steps[:i]+steps[i+1:])
                mass = expectation([Q(0)]+multiply(rest, rest), m)
                direction = [(Q(0), Q(0))]*depth
                direction[i] = (Q(1), Q(1))
                path = factor_path_loss(factors, direction, m)
                assert g[i] == -2*mass < 0
                assert 2*path[2] == 2*g[i] == -4*mass < 0
                fh = factor_hessian(factors, g, hessian)
                assert fh[2*i][2*i] == fh[2*i+1][2*i+1] == 0
                assert fh[2*i][2*i+1] == fh[2*i+1][2*i] == g[i]
                assert all(path[j] == 0 for j in range(len(path)) if j not in (0, 2, 4))
                zero_cases += 1

            # A family of actual nonglobal critical points: one active optimal
            # layer and every remaining pair double zero. For L=1 it is global.
            factors = [(Q(n, n+2), Q(1))] + [(Q(0), Q(0))]*(depth-1)
            value, g, hessian = product_derivatives([k*q for k, q in factors], m)
            assert value == Q(2, n+2) and g[0] == 0
            assert all(q*gi == k*gi == 0 for (k, q), gi in zip(factors, g))
            if depth >= 2:
                assert g[1] < 0
                assert value > Q(2**depth*math.factorial(depth),
                                 math.prod(n+2*j for j in range(1, depth+1)))
            critical_cases += 1

            if depth < 2:
                continue
            for repeated in (Q(-1), Q(0), Q(2, 3)):
                factors = [(Q(1), repeated), (Q(2), repeated/2)]
                factors += [(Q(j+1), Q(1, j+2)) for j in range(depth-2)]
                steps = [k*q for k, q in factors]
                rest = residual(steps[2:])
                poly_a = multiply(multiply([Q(1), -repeated], [Q(1), -repeated]),
                                  multiply(rest, rest))
                aa = expectation([Q(0), Q(0)] + poly_a, m)
                bb = expectation([Q(0)]*4 + multiply(rest, rest), m)
                direction = lift_linear_product_path(factors, [Q(1), Q(-1)] + [Q(0)]*(depth-2))
                path = factor_path_loss(factors, direction, m)
                assert aa > 0 and bb > 0
                assert path[2] == -2*aa and path[4] == bb
                assert all(path[j] == 0 for j in range(len(path)) if j not in (0, 2, 4))
                _, g, hessian = product_derivatives(steps, m)
                fh = factor_hessian(factors, g, hessian)
                assert quadratic(fh, [x for pair in direction for x in pair]) == -4*aa
                repeated_cases += 1
    print(f'{zero_cases} double-zero Hessian checks; {repeated_cases} lifted '
          f'repeated-product checks; {critical_cases} critical-point checks passed.')

    # A load-bearing counterexample to importing product-order preservation.
    factors = [(Q(1), Q(1)), (Q(2), Q(1, 2))]
    _, g, _ = product_derivatives([Q(1), Q(1)], moments_by_recurrence(2, 4))
    assert g == [Q(22), Q(22)]
    speeds = [-(k*k+q*q)*gi for (k, q), gi in zip(factors, g)]
    assert speeds[0]-speeds[1] == Q(99, 2)
    print('Equal products 1,1 with unequal imbalances: gap derivative=99/2.')

    # Anti-balanced one-layer flow fails, and the origin really is a saddle.
    for n in (1, 2, 5, 100):
        for k in (Q(-2), Q(1, 3), Q(3)):
            q = -k
            _, g, _ = product_derivatives([k*q], moments_by_recurrence(n, 2))
            kp, qp = -q*g[0], -k*g[0]
            assert kp+qp == 0
            assert kp == -2*k*(1+Q(n+2, n)*k*k)
            assert k*kp < 0
        # Verify claimed factor magnitudes using a rational actual factor pair,
        # squaring the radical formula without using floating-point square roots.
        k, q = Q(2), Q(3, 5)
        a, dd = k*q, k*k-q*q
        hh = k*k+q*q
        assert hh*hh == dd*dd+4*a*a and hh > 0
        assert (hh+dd)/2 == k*k and (hh-dd)/2 == q*q
    print('Anti-balanced obstruction and limiting factor-magnitude formulas passed.')

    signal.alarm(0)
    rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    rss_bytes = rss if sys.platform == 'darwin' else rss*1024
    elapsed = time.monotonic()-started
    assert rss_bytes < 1024**3 and elapsed < 120
    print(f'Elapsed: {elapsed:.3f} seconds; peak RSS: {rss_bytes/1024**2:.2f} MiB')
    print('All exact factor audits passed.')


if __name__ == '__main__':
    run()
