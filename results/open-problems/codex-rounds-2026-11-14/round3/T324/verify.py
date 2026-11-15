"""Checks for the unequal-mass two-atom theorem; Python standard library only.

Run with the thread limits and nice command recorded in LOG.md.
All generated files are placed beside this script.
"""

import json
import math
import os
from pathlib import Path
import resource
import sys
import time


ROOT = Path(__file__).resolve().parent
DELTA, INITIAL = 0.4, 1.2
A = 1 - math.cos(INITIAL)


def logistic_minus(t):
    if t >= 0:
        z = math.exp(-t)
        return z / (1 + z)
    return 1 / (1 + math.exp(t))


def drift(beta, ell, s):
    a = 1 - math.cos(s)
    return math.sin(s) * (
        logistic_minus(beta * a - ell) + logistic_minus(beta * a + ell))


def adaptive(f, lo, hi, tol=1e-15, depth=24):
    """Adaptive Simpson quadrature, distinct from the former uniform mesh."""
    mid = (lo + hi) / 2
    fa, fm, fb = f(lo), f(mid), f(hi)
    initial = (hi - lo) * (fa + 4 * fm + fb) / 6

    def rec(a, b, va, vm, vb, whole, eps, left_depth):
        m = (a + b) / 2
        vl, vr = f((a + m) / 2), f((m + b) / 2)
        left = (m - a) * (va + 4 * vl + vm) / 6
        right = (b - m) * (vm + 4 * vr + vb) / 6
        error = left + right - whole
        roundoff = 128 * sys.float_info.epsilon * (abs(left) + abs(right))
        if abs(error) <= max(15 * eps, roundoff):
            return left + right + error / 15
        assert left_depth > 0, 'quadrature depth exhausted'
        return (rec(a, m, va, vl, vm, left, eps / 2, left_depth - 1)
                + rec(m, b, vm, vr, vb, right, eps / 2, left_depth - 1))

    return rec(lo, hi, fa, fm, fb, initial, tol, depth)


def simpson(f, lo, hi, n):
    step = (hi - lo) / n
    return step / 3 * (f(lo) + f(hi)
                      + 4 * sum(f(lo + i * step) for i in range(1, n, 2))
                      + 2 * sum(f(lo + i * step) for i in range(2, n, 2)))


def primitive(beta, ell, s):
    a = 1 - math.cos(s)
    # The primitive check is used at moderate parameters, where both exponents
    # are small enough for direct log1p evaluation.
    return (math.log1p(math.exp(ell - beta * a))
            + math.log1p(math.exp(-ell - beta * a))) / beta


def nested_mean(beta, ell, nu, n):
    """Direct two-dimensional quadrature using the explicit primitive."""
    def inner(y):
        fy = primitive(beta, ell, y)
        return adaptive(lambda z: math.exp(
            -(fy - primitive(beta, ell, z)) / (2 * nu)), y, math.pi,
            tol=1e-12)
    return simpson(inner, DELTA, INITIAL, n) / (2 * nu)


def bvp_mean(beta, ell, nu, n):
    """Independent central-difference linear system, absorbing/Neumann BCs."""
    step = (math.pi - DELTA) / n
    lower, diag, upper, rhs = [], [], [], []
    for i in range(1, n):
        h = drift(beta, ell, DELTA + i * step)
        peclet = h * step / (4 * nu)
        assert peclet < 1
        lower.append(1 + peclet)
        diag.append(-2.0)
        upper.append(1 - peclet)
        rhs.append(-step * step / (2 * nu))
    # At pi the drift vanishes. Centered reflection gives this final row.
    lower.append(-1.0)
    diag.append(1.0)
    upper.append(0.0)
    rhs.append(step * step / (4 * nu))
    for i in range(1, n):
        ratio = lower[i] / diag[i - 1]
        diag[i] -= ratio * upper[i - 1]
        rhs[i] -= ratio * rhs[i - 1]
    values = [0.0] * (n + 1)
    values[n] = rhs[-1] / diag[-1]
    for i in range(n - 2, -1, -1):
        values[i + 1] = (rhs[i] - upper[i] * values[i + 2]) / diag[i]
    pos = (INITIAL - DELTA) / step
    i = int(pos)
    return values[i] + (pos - i) * (values[i + 1] - values[i])


def cell_mean(beta, ell, nu, n):
    """Exact transfers for a piecewise constant midpoint approximation of h.

    Backward recursion for p=u' avoids overflow of an integrating factor.
    Integrate p exactly within each cell, including the partial cell at x.
    """
    step = (math.pi - DELTA) / n
    right_p, result = 0.0, 0.0
    for i in range(n - 1, -1, -1):
        left = DELTA + i * step
        h = drift(beta, ell, left + step / 2)
        exponent = h * step / (2 * nu)
        left_p = (-math.expm1(-exponent) / h
                  + math.exp(-exponent) * right_p)
        length = min(step, max(0.0, INITIAL - left))
        if length > 0:
            t = h * length / (2 * nu)
            if t < 1e-4:
                one_minus_phi = t / 2 - t*t / 6 + t**3 / 24 - t**4 / 120
            else:
                one_minus_phi = 1 + math.expm1(-t) / t
            # p at the end of the included part of this cell.
            remaining = step - length
            k = h * remaining / (2 * nu)
            end_p = -math.expm1(-k) / h + math.exp(-k) * right_p
            result += length * (one_minus_phi / h
                                + end_p * (1 - one_minus_phi))
        right_p = left_p
    return result


def main():
    started = time.monotonic()
    assert os.getpriority(os.PRIO_PROCESS, 0) >= 15
    for name in ('OMP_NUM_THREADS', 'OPENBLAS_NUM_THREADS',
                 'VECLIB_MAXIMUM_THREADS', 'MKL_NUM_THREADS'):
        assert os.environ.get(name) == '1', name

    # Direct row weights, the odds representation, and the rational expression.
    algebra_errors = []
    for p in (0.5, 0.2, 0.01, 0.8):
        q = 1 - p
        ell = abs(math.log(p / q))
        cp = p / q + q / p
        for beta in (0.0, 4.0, 20.0):
            for s in (DELTA, INITIAL, 2.7):
                e = math.exp(beta * (1 - math.cos(s)))
                direct = math.sin(s) * (q / (p * e + q) + p / (q * e + p))
                rational = math.sin(s) * (cp * e + 2) / (e*e + cp*e + 1)
                algebra_errors.extend((abs(direct / drift(beta, ell, s) - 1),
                                       abs(direct / rational - 1)))
    assert max(algebra_errors) < 2e-14

    deterministic = []
    for p in (0.5, 0.2, 0.01):
        q = 1 - p
        ell, cp = abs(math.log(p / q)), p / q + q / p
        for beta in (20, 80, 320):
            scale = math.exp(-beta * A)
            angular = adaptive(lambda s: scale / drift(beta, ell, s), DELTA, INITIAL)

            def cosine_integrand(c):
                e = math.exp(beta * (1 - c))
                w = q / (p * e + q) + p / (q * e + p)
                return scale / (w * (1 - c*c))

            cosine = adaptive(cosine_integrand, math.cos(INITIAL), math.cos(DELTA))
            relative = abs(angular / cosine - 1)
            assert relative < 2e-8
            ratio = angular * cp * beta * math.sin(INITIAL)**2
            deterministic.append(dict(p=p, beta=beta, scaled_time=angular,
                                      coordinate_relative_difference=relative,
                                      exact_over_asymptotic=ratio))

    # Moderate parameters permit three genuinely different numerical solves.
    noisy = []
    for beta, p, nu in ((4, 0.5, 0.03), (4, 0.2, 0.03), (12, 0.2, 0.002)):
        ell = abs(math.log(p / (1 - p)))
        potential = primitive(beta, ell, DELTA) - primitive(beta, ell, 2.7)
        integrated = adaptive(lambda s: drift(beta, ell, s), DELTA, 2.7)
        assert abs(potential / integrated - 1) < 1e-9
        coarse = nested_mean(beta, ell, nu, 256)
        direct = nested_mean(beta, ell, nu, 512)
        assert abs(coarse / direct - 1) < 5e-6
        bvp = bvp_mean(beta, ell, nu, 8192)
        cells = cell_mean(beta, ell, nu, 32768)
        assert abs(bvp / direct - 1) < 2e-6
        assert abs(cells / direct - 1) < 2e-6
        noisy.append(dict(beta=beta, p=p, nu=nu, nested_quadrature=direct,
                          finite_difference=bvp, cell_transfer=cells,
                          bvp_relative_difference=abs(bvp / direct - 1),
                          cell_relative_difference=abs(cells / direct - 1)))

    baseline = math.log(math.tan(INITIAL / 2) / math.tan(DELTA / 2))
    mass_scaling = []
    bound_errors = []
    for kappa in (0.0, 0.25, A, 0.9):
        for beta in (20, 80, 320):
            ell = kappa * beta
            # Scale by the predicted exponential order rather than a(x).
            target = max(A - kappa, 0)
            scaled_time = adaptive(lambda s: math.exp(-beta * target)
                                   / drift(beta, ell, s), DELTA, INITIAL)
            scaled_j = adaptive(lambda s: math.exp(beta * (1-math.cos(s)-A))
                                / math.sin(s), DELTA, INITIAL)
            cp = math.exp(ell) + math.exp(-ell)
            j_over_c = scaled_j * math.exp(beta * A) / cp
            time_value = scaled_time * math.exp(beta * target)
            lo, hi = max(baseline, j_over_c), baseline + j_over_c
            bound_error = max(0.0, lo / time_value - 1, time_value / hi - 1)
            assert bound_error < 2e-10
            bound_errors.append(bound_error)
            second_order_center = j_over_c + (1 - 2 / cp**2) * baseline
            remainder = second_order_center - time_value
            remainder_bound = baseline / (cp * math.exp(beta * (1-math.cos(DELTA))))
            # Allow the relative quadrature roundoff when subtracting large times.
            rounding = 2e-10 * max(1.0, time_value)
            assert -rounding <= remainder <= remainder_bound + rounding
            mass_scaling.append(dict(kappa=kappa, beta=beta,
                                     log_time_over_beta=target + math.log(scaled_time)/beta,
                                     predicted_limit=target,
                                     time=time_value, comparison_lower=lo,
                                     comparison_upper=hi,
                                     exact_over_mass_dependent_asymptotic=(
                                         scaled_time * cp * beta * math.sin(INITIAL)**2
                                         * math.exp(beta * (target-A))),
                                     time_over_sine_limit=(scaled_time / baseline
                                                          if target == 0 else None)))

    critical = []
    for sign in (-1, 1):
        for beta in (40, 160, 320):
            ell = beta * A + sign * math.sqrt(beta)
            value = adaptive(lambda s: 1 / drift(beta, ell, s), DELTA, INITIAL,
                             tol=1e-10)
            cp = math.exp(ell) + math.exp(-ell)
            asymptotic = math.exp(beta*A) / (cp*beta*math.sin(INITIAL)**2)
            critical.append(dict(sign=sign, beta=beta, time=value,
                                 sine_limit=baseline,
                                 mass_dependent_asymptotic=asymptotic))

    critical_constants = []
    for b in (-1, 0, 1):
        for beta in (80, 320):
            ell = beta * A - math.log(beta) + b
            value = adaptive(lambda s: 1 / drift(beta, ell, s), DELTA, INITIAL,
                             tol=1e-12)
            critical_constants.append(dict(
                b=b, beta=beta, time=value,
                predicted_limit=baseline + math.exp(-b) / math.sin(INITIAL)**2))

    crossover = []
    for kappa, r in ((0, 0.3), (0.25, 0.2), (0.25, A - 0.25),
                     (0.25, 0.8), (A, 0.4), (0.9, 0.4)):
        for beta in (40, 160, 320):
            nu, ell = math.exp(-r * beta), kappa * beta
            coarse = cell_mean(beta, ell, nu, 32768)
            mean = cell_mean(beta, ell, nu, 65536)
            relative = abs(coarse / mean - 1)
            assert relative < 2e-3
            crossover.append(dict(kappa=kappa, r=r, beta=beta, mean=mean,
                                  log_mean_over_beta=math.log(mean)/beta,
                                  predicted_limit=min(max(A-kappa, 0), r),
                                  mesh_relative_difference=relative))

    elapsed = time.monotonic() - started
    peak_raw = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    peak_mb = peak_raw / (1024**2 if sys.platform == 'darwin' else 1024)
    assert peak_mb < 1024
    output = dict(delta=DELTA, initial=INITIAL, a_initial=A,
                  max_drift_algebra_error=max(algebra_errors),
                  deterministic=deterministic, noisy=noisy,
                  mass_scaling=mass_scaling, critical=critical,
                  critical_constants=critical_constants, crossover=crossover,
                  elapsed_seconds=elapsed, peak_rss_mb=peak_mb,
                  effective_nice=os.getpriority(os.PRIO_PROCESS, 0))
    (ROOT / 'verification.json').write_text(json.dumps(output, indent=2) + '\n')
    print(f'effective nice={output["effective_nice"]}; peak RSS={peak_mb:.2f} MiB')
    print(f'Drift algebra max relative error: {max(algebra_errors):.3e}')
    print('Deterministic coordinate max relative error: '
          f'{max(row["coordinate_relative_difference"] for row in deterministic):.3e}')
    print('Fixed masses: p, beta, exact/asymptotic')
    for row in deterministic:
        print(f'{row["p"]:.2f}, {row["beta"]}, {row["exact_over_asymptotic"]:.9f}')
    print('Noisy direct quadrature / BVP / cell transfer: beta, p, three means')
    for row in noisy:
        print(f'{row["beta"]}, {row["p"]}, {row["nested_quadrature"]:.10g}, '
              f'{row["finite_difference"]:.10g}, {row["cell_transfer"]:.10g}')
    print('Mass scaling: kappa, beta, log(T)/beta, predicted limit, T/sine-limit if available')
    for row in mass_scaling:
        print(f'{row["kappa"]:.9f}, {row["beta"]}, '
              f'{row["log_time_over_beta"]:.9f}, {row["predicted_limit"]:.9f}, '
              f'{row["time_over_sine_limit"]}')
    print('Noise crossover: kappa, r, beta, log(mean)/beta, predicted limit')
    for row in crossover:
        print(f'{row["kappa"]:.9f}, {row["r"]:.9f}, {row["beta"]}, '
              f'{row["log_mean_over_beta"]:.9f}, {row["predicted_limit"]:.9f}')
    print('Critical mass corrections: sign, beta, time, sine limit, mass-dependent asymptotic')
    for row in critical:
        print(f'{row["sign"]}, {row["beta"]}, {row["time"]:.9g}, '
              f'{row["sine_limit"]:.9g}, {row["mass_dependent_asymptotic"]:.9g}')
    print('Critical constants: b, beta, time, predicted limit')
    for row in critical_constants:
        print(f'{row["b"]}, {row["beta"]}, {row["time"]:.9g}, '
              f'{row["predicted_limit"]:.9g}')
    print('Maximum crossover mesh discrepancy: '
          f'{max(row["mesh_relative_difference"] for row in crossover):.3e}')
    print(f'All checks passed in {elapsed:.3f} seconds; wrote verification.json.')


if __name__ == '__main__':
    main()
