#!/usr/bin/env python3
"""Numerical audits of PROOF.md; standard library, one thread, bounded work.

Run: OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 verify.py
The proof does not depend on these floating-point or Monte Carlo checks.
"""

import bisect
import csv
import json
import math
import os
from pathlib import Path
import random
import resource
import sys
import time


START = time.monotonic()
resource.setrlimit(resource.RLIMIT_CPU, (60, 60))
ROOT = Path(__file__).resolve().parent
PRIORITY = os.getpriority(os.PRIO_PROCESS, 0)
if PRIORITY < 15:
    raise RuntimeError(f"Expected nice >= 15; actual priority is {PRIORITY}")


def integrate(f, left=0.0, right=10.0, tolerance=2e-13):
    """Adaptive Simpson quadrature with a fixed depth limit."""
    def split(a, b, fa, fc, fb, previous, eps, depth):
        c = (a + b) / 2
        d, e = (a + c) / 2, (c + b) / 2
        fd, fe = f(d), f(e)
        first = (c - a) * (fa + 4 * fd + fc) / 6
        second = (b - c) * (fc + 4 * fe + fb) / 6
        change = first + second - previous
        if abs(change) <= 15 * eps:
            return first + second + change / 15
        if depth == 0:
            raise ArithmeticError("quadrature depth exhausted")
        return split(a, c, fa, fd, fc, first, eps / 2, depth - 1) + split(
            c, b, fc, fe, fb, second, eps / 2, depth - 1
        )

    # Seed with width <= 1/8. A single initial panel on [0,10] can
    # sample only tiny values and miss the integrand's peak near u=1.
    panels = max(1, math.ceil((right - left) * 8))
    answers = []
    for j in range(panels):
        a = left + (right - left) * j / panels
        b = left + (right - left) * (j + 1) / panels
        c = (a + b) / 2
        fa, fc, fb = f(a), f(c), f(b)
        whole = (b - a) * (fa + 4 * fc + fb) / 6
        answers.append(split(a, b, fa, fc, fb, whole, tolerance / panels, 26))
    return math.fsum(answers)


def upper_gamma(a, x):
    """Gamma(a,x) by a convergent positive series for the lower gamma.

    Used only for a=1/3,2/3 and 0 <= x <= 8. This has a different
    implementation from the quadrature of the original density formula.
    """
    if x == 0:
        return math.gamma(a)
    term = total = 1 / a
    for n in range(1, 1000):
        term *= x / (a + n)
        total += term
        if term < abs(total) * 1e-17:
            return math.gamma(a) - math.exp(a * math.log(x) - x) * total
    raise ArithmeticError("incomplete gamma series did not converge")


def q_integral(d, t):
    return integrate(lambda u: d * u ** (d - 1) * math.exp(-((u + t) ** d)))


def q_closed(d, t):
    if d == 2:
        return math.exp(-(t * t)) - math.sqrt(math.pi) * t * math.erfc(t)
    if d == 3:
        return (
            math.exp(-(t**3))
            - 2 * t * upper_gamma(2 / 3, t**3)
            + t * t * upper_gamma(1 / 3, t**3)
        )
    raise ValueError(d)


def coefficient_a(d):
    return (d - 1) * math.gamma(1 - 1 / d)


def coefficient_b(d):
    return d * d * integrate(lambda u: u ** (2 * d - 2) * math.exp(-(u**d)))


def main():
    rows = []
    grid = [0.0, 0.000001, 0.001, 0.01, 0.1, 0.25, 0.5, 1.0, 2.0]
    max_error = 0.0
    print("Independent numerical audit; no numerical claim is used as a proof.")
    print(f"inherited_nice_priority={PRIORITY}; OMP_NUM_THREADS={os.environ.get('OMP_NUM_THREADS')}")
    print("d,t,q_integral,q_closed,absolute_difference,linear_lower_bound")
    for d in [2, 3]:
        for t in grid:
            qa, qb = q_integral(d, t), q_closed(d, t)
            error = abs(qa - qb)
            lower = 1 - coefficient_a(d) * t
            assert error < 1e-10, (d, t, qa, qb)
            assert -1e-12 <= qa <= 1 + 1e-12
            assert qa >= lower - 1e-12
            max_error = max(max_error, error)
            rows.append(dict(d=d, t=t, q_integral=qa, q_closed=qb,
                             absolute_difference=error, linear_lower_bound=lower))
            print(f"{d},{t:g},{qa:.12g},{qb:.12g},{error:.3g},{lower:.12g}")

    constants = []
    print("Constants: gamma expression, independent integral, small-t slope")
    for d in [2, 3, 4, 8]:
        ca, cb = coefficient_a(d), coefficient_b(d)
        slope = (1 - q_integral(d, 1e-6)) / 1e-6
        assert abs(ca - cb) < 2e-10, (d, ca, cb)
        assert abs(ca - slope) < 1e-4, (d, ca, slope)
        constants.append(dict(d=d, gamma=ca, integral=cb, finite_difference=slope))
        print(f"d={d}: {ca:.12g}, {cb:.12g}, {slope:.12g}")

    # Equation (7) is an independent probabilistic route to the formula.
    # Bonferroni + Hoeffding: each estimate misses by delta with probability
    # <= 2 exp(-2 N delta^2); four estimates give total <= 0.001.
    count = 200000
    family_failure = 0.001
    delta = math.sqrt(math.log(8 / family_failure) / (2 * count))
    trials = []
    rng = random.Random(80080)
    print(f"Order-statistic Monte Carlo: N={count}, seed=80080, error allowance={delta:.8g}")
    for d in [2, 3]:
        gaps = []
        for _ in range(count):
            first = rng.expovariate(1.0)
            second_increment = rng.expovariate(1.0)
            gaps.append((first + second_increment) ** (1 / d) - first ** (1 / d))
        gaps.sort()
        for t in [0.1, 0.5]:
            empirical = (count - bisect.bisect_right(gaps, t)) / count
            expected = q_integral(d, t)
            error = abs(empirical - expected)
            assert error <= delta, (d, t, empirical, expected, delta)
            trials.append(dict(d=d, t=t, empirical=empirical, exact_formula=expected,
                               absolute_difference=error, error_allowance=delta))
            print(f"d={d}, t={t}: observed={empirical:.8g}, formula={expected:.8g}, error={error:.5g}")

    # Check the algebraic substitution used in the density/covariance tradeoff.
    for d in [2, 3, 8]:
        vd = math.pi ** (d / 2) / math.gamma(1 + d / 2)
        for eps in [0.01, 0.1, 0.5]:
            t = eps / (2 * coefficient_a(d))
            lam = t**d / vd
            distance = 1000.0
            left = lam * vd * (distance / 4) ** d
            right = (eps * distance / (8 * coefficient_a(d))) ** d
            assert math.isclose(left, right, rel_tol=1e-12)
            assert (1 - eps / 2) ** 2 >= 1 - eps - 1e-15

    with (ROOT / "q_table.csv").open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    elapsed = time.monotonic() - START
    rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    peak_mib = rss / (1024**2 if sys.platform == "darwin" else 1024)
    data = dict(status="PASS", max_formula_discrepancy=max_error,
                constants=constants, monte_carlo=trials, sample_size=count,
                monte_carlo_seed=80080, family_failure_bound=family_failure,
                elapsed_seconds=elapsed, peak_rss_mib=peak_mib)
    data["nice_priority"] = PRIORITY
    (ROOT / "verification.json").write_text(json.dumps(data, indent=2) + "\n")
    print(f"PASS: maximum formula discrepancy={max_error:.3g}")
    print(f"elapsed_seconds={elapsed:.3f}; peak_rss_mib={peak_mib:.3f}")
    print("Wrote q_table.csv and verification.json")


if __name__ == "__main__":
    main()
