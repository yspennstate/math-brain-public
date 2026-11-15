"""Exact arithmetic audit of arbitrary-depth scalar attention.

OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 \
    PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3 audit_depth.py

Standard library only. No numerical training, root finder, or array library.
"""

import itertools
import math
import os
import resource
import sys
import time
from fractions import Fraction as Q


def mul(p, q, degree=None):
    size = len(p) + len(q) - 1
    if degree is not None:
        size = min(size, degree + 1)
    result = [Q(0)] * size
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            if i + j < size:
                result[i+j] += a*b
    return result


def add(p, q):
    result = [Q(0)] * max(len(p), len(q))
    for i, v in enumerate(p):
        result[i] += v
    for i, v in enumerate(q):
        result[i] += v
    return result


def scale(p, c):
    return [c*x for x in p]


def expect(p, moments):
    assert len(p) <= len(moments)
    return sum((v*moments[i] for i, v in enumerate(p)), Q(0))


def gaussian_expansion(n, degree):
    """Gaussian IBP and exponentiation of the single-variable EGF.

    This avoids the chi-square moment product formula. The identity
    E[x^(2k)]=(2k-1) E[x^(2k-2)] supplies the single Gaussian moments.
    Exponentiation by squaring computes the n-fold independent sum.
    """
    gaussian_moment = 1
    base = [Q(1)]
    for k in range(1, degree+1):
        gaussian_moment *= 2*k-1
        base.append(Q(gaussian_moment, math.factorial(k)))
    product = [Q(1)]
    power = n
    while power:
        if power % 2:
            product = mul(product, base, degree)
        power //= 2
        if power:
            base = mul(base, base, degree)
    return [product[k]*Q(math.factorial(k), n**k)
            for k in range(degree+1)]


def gamma_moments(n, degree):
    m = [Q(1)]
    for k in range(degree):
        m.append(m[-1]*Q(n+2*k, n))
    return m


def solve(matrix, rhs):
    """Fraction-only Gauss-Jordan solve, without the claimed optimum."""
    size = len(rhs)
    rows = [list(matrix[i]) + [rhs[i]] for i in range(size)]
    for col in range(size):
        pivot = next(i for i in range(col, size) if rows[i][col])
        rows[col], rows[pivot] = rows[pivot], rows[col]
        factor = rows[col][col]
        rows[col] = [x/factor for x in rows[col]]
        for i in range(size):
            if i != col:
                factor = rows[i][col]
                rows[i] = [x-factor*y for x, y in zip(rows[i], rows[col])]
    return [row[-1] for row in rows]


def determinant(matrix):
    rows = [list(row) for row in matrix]
    result = Q(1)
    for col in range(len(rows)):
        pivot = next((i for i in range(col, len(rows)) if rows[i][col]), None)
        if pivot is None:
            return Q(0)
        if pivot != col:
            rows[col], rows[pivot] = rows[pivot], rows[col]
            result = -result
        value = rows[col][col]
        result *= value
        for i in range(col+1, len(rows)):
            factor = rows[i][col]/value
            for j in range(col+1, len(rows)):
                rows[i][j] -= factor*rows[col][j]
    return result


def rising(value, k):
    result = Q(1)
    for j in range(k):
        result *= value+j
    return result


def claimed_residual(n, depth):
    alpha = Q(n, 2)
    return [(-1)**k * math.comb(depth, k)*alpha**k/rising(alpha+1, k)
            for k in range(depth+1)]


def residual(steps):
    product = [Q(1)]
    for a in steps:
        product = mul(product, [Q(1), -a])
    return product


def loss_gradient(steps, moments):
    """Differentiate the product polynomial directly."""
    r = residual(steps)
    derivs = [[Q(0)] + scale(residual(steps[:i]+steps[i+1:]), Q(-1))
              for i in range(len(steps))]
    gradient = [2*expect(mul(r, dr), moments) for dr in derivs]
    return expect(mul(r, r), moments), gradient, derivs


def token_update(xs, w, xq, steps):
    top = xs + [xq]
    labels = [w*x for x in xs] + [Q(0)]
    for a in steps:
        # The old label row is used in the entire simultaneous update.
        contraction = sum((labels[i]*xs[i] for i in range(len(xs))), Q(0))
        labels = [y-a*contraction*x/len(xs) for y, x in zip(labels, top)]
    return -labels[-1]


def evaluate(p, x):
    value = Q(0)
    for v in reversed(p):
        value = value*x+v
    return value


def sturm_positive_roots(p):
    """Independent exact root count, without numerical roots or Laguerre facts."""
    def trim(poly):
        while len(poly) > 1 and poly[-1] == 0:
            poly.pop()
        return poly

    def remainder(a, b):
        a = list(a)
        while len(a) >= len(b) and any(a):
            shift = len(a)-len(b)
            factor = a[-1]/b[-1]
            for i, v in enumerate(b):
                a[i+shift] -= factor*v
            trim(a)
        return a

    sequence = [list(p), [k*p[k] for k in range(1, len(p))]]
    while len(sequence[-1]) > 1:
        rem = remainder(sequence[-2], sequence[-1])
        assert any(rem), "Repeated polynomial root"
        sequence.append(scale(rem, Q(-1)))

    def changes(values):
        values = [1 if x > 0 else -1 for x in values if x]
        return sum(a != b for a, b in zip(values, values[1:]))

    return (changes([p[0] for p in sequence])
            - changes([p[-1] for p in sequence]))


def run():
    start = time.monotonic()
    priority = os.getpriority(os.PRIO_PROCESS, 0)
    print(f"Process nice: {priority}")
    assert priority >= 15
    assert os.environ.get("OMP_NUM_THREADS") == "1"
    # CPU time limit; the fixed arithmetic cases normally finish in seconds.
    old_cpu_soft, old_cpu_hard = resource.getrlimit(resource.RLIMIT_CPU)
    cpu_cap = 120 if old_cpu_hard == resource.RLIM_INFINITY else min(120, old_cpu_hard)
    resource.setrlimit(resource.RLIMIT_CPU, (cpu_cap, old_cpu_hard))
    print(f"CPU soft limit: {cpu_cap} seconds")

    cases = 0
    for n in [1, 2, 3, 5, 10, 100, 1000]:
        moments = gaussian_expansion(n, 16)
        assert moments == gamma_moments(n, 16)
        for depth in range(1, 9):
            h = [[moments[i+j] for j in range(1, depth+1)]
                 for i in range(1, depth+1)]
            optimum = [Q(1)] + solve(h, [-moments[i] for i in range(1, depth+1)])
            assert optimum == claimed_residual(n, depth)
            direct_risk = expect(mul(optimum, optimum), moments)
            formula = Q(2**depth * math.factorial(depth),
                        math.prod(n+2*j for j in range(1, depth+1)))
            assert direct_risk == formula == expect(optimum, moments)
            assert direct_risk == 1+sum(optimum[k]*moments[k]
                                       for k in range(1, depth+1))
            for j in range(1, depth+1):
                assert expect([Q(0)]*j+optimum, moments) == 0
            assert sturm_positive_roots(optimum) == depth
            cases += 1
            if depth in [2, 3, 8]:
                print(f"n={n}, L={depth}: exact risk={formula}; "
                      f"positive simple roots={depth}")
    print(f"{cases} independent moment-system/closed-form/risk/Sturm checks passed.")

    gradient_cases = 0
    collision_cases = 0
    for depth in range(1, 7):
        steps = [Q(-7), Q(0), Q(2, 3), Q(2), Q(3), Q(100)][:depth]
        for n in [1, 3, 10]:
            moments = gaussian_expansion(n, 2*depth)
            value, gradient, derivs = loss_gradient(steps, moments)
            r = residual(steps)
            # Chain rule through coefficients, independently from product derivative.
            coefficient_gradient = [2*expect([Q(0)]*k+r, moments)
                                    for k in range(1, depth+1)]
            jacobian = [[derivs[i][k] for i in range(depth)]
                        for k in range(1, depth+1)]
            for i in range(depth):
                assert gradient[i] == sum(jacobian[k][i]*coefficient_gradient[k]
                                          for k in range(depth))
            # Square of Vandermonde avoids an irrelevant determinant sign.
            vandermonde = math.prod(steps[j]-steps[i]
                                   for i in range(depth) for j in range(i+1, depth))
            assert determinant(jacobian)**2 == vandermonde**2 != 0
            optimum = claimed_residual(n, depth)
            delta = add(r, scale(optimum, Q(-1)))
            assert value-expect(mul(optimum, optimum), moments) == expect(mul(delta, delta), moments)
            for i, j in itertools.combinations(range(depth), 2):
                others = [a for k, a in enumerate(steps) if k not in [i, j]]
                rest = residual(others)
                coefficient = 2*expect([Q(0), Q(0)] + mul(
                    mul([Q(1), -steps[i]], [Q(1), -steps[j]]), mul(rest, rest)), moments)
                assert -gradient[i]+gradient[j] == (steps[i]-steps[j])*coefficient
                midpoint = (steps[i]+steps[j])/2
                gap = steps[i]-steps[j]
                midpoint_k = expect([Q(0), Q(0)] + mul(
                    mul([Q(1), -midpoint], [Q(1), -midpoint]), mul(rest, rest)), moments)
                midpoint_t = expect([Q(0)]*4 + mul(rest, rest), moments)
                assert coefficient == 2*midpoint_k-gap**2*midpoint_t/2
                gradient_cases += 1

                # Check pair splitting at a repeated pair, including c=0 and c<0.
                for c in [Q(-2), Q(0), Q(3, 4)]:
                    repeated = list(steps)
                    repeated[i] = repeated[j] = c
                    k_poly = mul(mul([Q(1), -c], [Q(1), -c]), mul(rest, rest))
                    k_value = expect([Q(0), Q(0)] + k_poly, moments)
                    t_value = expect([Q(0)]*4 + mul(rest, rest), moments)
                    assert k_value > 0 and t_value > 0
                    base_loss, _, _ = loss_gradient(repeated, moments)
                    for h_step in [Q(1, 100), Q(-2, 7)]:
                        split = list(repeated)
                        split[i], split[j] = c+h_step, c-h_step
                        split_loss, _, _ = loss_gradient(split, moments)
                        assert split_loss == base_loss-2*h_step**2*k_value+h_step**4*t_value
                    _, repeated_gradient, _ = loss_gradient(repeated, moments)
                    assert repeated_gradient[i] == repeated_gradient[j]
                    collision_cases += 1

            xs, w, xq = [Q(1, 3), Q(-2), Q(5, 4)], Q(-4, 5), Q(7, 3)
            s = sum(x*x for x in xs)/len(xs)
            pred = token_update(xs, w, xq, steps)
            assert pred == w*xq*(1-evaluate(r, s))
            assert pred == token_update(xs, w, xq, list(reversed(steps)))

    print(f"{gradient_cases} pair-difference checks and {collision_cases} collision checks passed.")
    print("Coefficient Jacobian, loss gap, zero/negative steps and token updates passed.")
    elapsed = time.monotonic()-start
    rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    rss_bytes = rss if sys.platform == "darwin" else rss*1024
    print(f"Elapsed: {elapsed:.3f} seconds; peak RSS: {rss_bytes/1024**2:.2f} MiB")
    assert elapsed < 1200 and rss_bytes < 1024**3


if __name__ == "__main__":
    run()
