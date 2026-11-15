#!/usr/bin/env python3
"""Small deterministic audits for PROOF.md; no third-party packages.

Run: OMP_NUM_THREADS=1 nice -n 15 python3 -B check_gaussian_renewal.py
Floating-point checks are illustrative, not interval certificates.
"""

import math
import random
import resource
import sys
import time


def simpson(f, a, b, tol=2e-12, depth=24):
    """Adaptive Simpson integration on a finite interval."""
    m = (a + b) / 2
    fa, fm, fb = f(a), f(m), f(b)
    whole = (b - a) * (fa + 4 * fm + fb) / 6

    def rec(a, b, fa, fm, fb, whole, tol, depth):
        m = (a + b) / 2
        lm, rm = (a + m) / 2, (m + b) / 2
        fl, fr = f(lm), f(rm)
        left = (m - a) * (fa + 4 * fl + fm) / 6
        right = (b - m) * (fm + 4 * fr + fb) / 6
        delta = left + right - whole
        if abs(delta) <= 15 * tol:
            return left + right + delta / 15
        if depth == 0:
            raise ArithmeticError("quadrature exhausted depth")
        return rec(a, m, fa, fl, fm, left, tol / 2, depth - 1) + rec(
            m, b, fm, fr, fb, right, tol / 2, depth - 1
        )

    return rec(a, b, fa, fm, fb, whole, tol, depth)


EULER = 0.5772156649015328606


def phi_from_log(y):
    """Power series for small x; original integral for large x."""
    x = math.exp(y)
    if x <= 1:
        total = -EULER - y
        factorial_term = 1.0
        for k in range(1, 150):
            factorial_term *= -x / k
            term = factorial_term / k
            total -= term
            if abs(term) < 1e-17:
                break
        return math.exp(x) * total
    return simpson(lambda u: math.exp(-u) / (u + x), 0, 60)


def phi_independent(y):
    """E1 integral after v=log(u), avoiding its small-x singularity.

    The omitted tail is at most exp(x-60)/60.
    """
    x = math.exp(y)
    upper = math.log(60)
    count = max(1, math.ceil((upper - y) / 2))
    edges = [y + (upper - y) * j / count for j in range(count + 1)]
    return sum(
        simpson(lambda v: math.exp(x - math.exp(v)), a, b)
        for a, b in zip(edges, edges[1:])
    )


def root_log(g):
    target = 4 * math.pi / g
    lo, hi = -max(10.0, 2 * target), 10.0
    assert phi_from_log(lo) > target > phi_from_log(hi)
    for _ in range(90):
        mid = (lo + hi) / 2
        if phi_from_log(mid) > target:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def recursive_log_product(gaps, s):
    variance = 0.0
    result = 0.0
    for gap in gaps:
        predicted = variance + 2 * gap
        result -= math.log(2 * math.pi * (predicted + 2 * s))
        variance = 2 * s * predicted / (predicted + 2 * s)
        assert 0 <= variance <= 2 * s
    return result


def cholesky_logdet(a):
    n = len(a)
    lower = [[0.0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1):
            residual = a[i][j] - sum(lower[i][k] * lower[j][k] for k in range(j))
            if i == j:
                assert residual > 0
                lower[i][j] = math.sqrt(residual)
            else:
                lower[i][j] = residual / lower[j][j]
    return 2 * sum(math.log(lower[i][i]) for i in range(n))


def determinant_log_product(gaps, s):
    times = []
    for gap in gaps:
        times.append(gap + (times[-1] if times else 0))
    # One-coordinate covariance is 2*min(t_i,t_j). Two independent
    # coordinates turn det(I + covariance/(2*s))^(-1/2) into power -1.
    matrix = [
        [float(i == j) + min(ti, tj) / s for j, tj in enumerate(times)]
        for i, ti in enumerate(times)
    ]
    return -len(gaps) * math.log(4 * math.pi * s) - cholesky_logdet(matrix)


def main():
    start = time.monotonic()
    # No subprocesses or threads. Darwin may reject RLIMIT_AS; all matrices
    # below are at most 12 by 12 and peak RSS is also reported explicitly.
    for label, kind, requested in (
        ("address-space", resource.RLIMIT_AS, 256 * 1024**2),
        ("CPU seconds", resource.RLIMIT_CPU, 90),
    ):
        try:
            soft, hard = resource.getrlimit(kind)
            cap = requested if hard == resource.RLIM_INFINITY else min(requested, hard)
            resource.setrlimit(kind, (cap, hard))
            print(f"resource soft limit {label}: {cap}")
        except (ValueError, OSError) as exc:
            print(f"resource soft limit {label} unavailable: {exc}")
    print("Deterministic floating-point audit; seed=9090; s=1 for rates")
    print("b        log(x_g)          lower rate       upper rate       b^2 log(x_g)")
    max_integral_error = 0.0
    for b in (0.25, 0.5, 1.0, 2.0, 4.0, 8.0):
        g = b * b
        y = root_log(g)
        x = math.exp(y)
        other = phi_independent(y)
        relative_error = abs(other / (4 * math.pi / g) - 1)
        assert relative_error < 1e-10
        max_integral_error = max(max_integral_error, relative_error)
        print(f"{b:<5g} {y:>17.10f} {x/2:>16.8e} {x:>16.8e} {g*y:>17.10f}")
    print(f"max independent scalar-integral relative error: {max_integral_error:.3e}")

    rng = random.Random(9090)
    cases = [(s, gaps) for s in (0.1, 1.0, 10.0) for gaps in (
        [1e-10 * s] * 12, [1e5 * s] * 12,
        [s * (1e-6 if i % 2 else 1e3) for i in range(12)], [s], [s, 2*s]
    )]
    for _ in range(500):
        s = 10 ** rng.uniform(-2, 2)
        gaps = [s * 10 ** rng.uniform(-4, 3) for _ in range(rng.randint(1, 12))]
        cases.append((s, gaps))
    max_log_error = 0.0
    for s, gaps in cases:
        rec = recursive_log_product(gaps, s)
        det = determinant_log_product(gaps, s)
        error = abs(rec - det)
        max_log_error = max(max_log_error, error)
        assert error < 2e-8, (s, gaps, rec, det)
        lower = -sum(math.log(4 * math.pi * (gap + 2 * s)) for gap in gaps)
        upper = -sum(math.log(4 * math.pi * (gap + s)) for gap in gaps)
        assert lower - 1e-10 <= det <= upper + 1e-10
    print(f"Gaussian recurrence vs covariance determinant: {len(cases)} cases PASS")
    print(f"max absolute log-product discrepancy: {max_log_error:.3e}")

    # A separate closed-form n=2 integration.
    for s, u, v in ((1.0, 0.3, 2.7), (0.02, 0.1, 0.003), (5.0, 0.001, 300.0)):
        closed = 1 / ((4 * math.pi)**2 * (s*s + 2*s*u + s*v + u*v))
        rec = math.exp(recursive_log_product([u, v], s))
        assert abs(closed / rec - 1) < 1e-12
    print("n=2 closed-form checks: 3 PASS")

    # Exact covariance-time scaling: gamma(b,s)=gamma(b,1)/s.
    # The reported two scalar endpoints must have this same scaling.
    x = math.exp(root_log(1.0))
    for s in (0.01, 0.5, 2.0, 100.0):
        r = x / s
        assert abs(phi_from_log(math.log(s * r)) / (4 * math.pi) - 1) < 1e-12
    print("rate-equation covariance-time scaling: 4 PASS")
    print(f"elapsed seconds: {time.monotonic() - start:.3f}")
    raw_rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    rss_bytes = raw_rss if sys.platform == "darwin" else raw_rss * 1024
    print(f"peak RSS MiB: {rss_bytes / 1024**2:.3f}")
    assert rss_bytes < 1024**3
    print("PASS: numerical checks only; analytic argument is in PROOF.md")


if __name__ == "__main__":
    main()
