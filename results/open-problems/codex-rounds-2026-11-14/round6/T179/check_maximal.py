"""Arithmetic checks for the maximal estimate; no SPDE simulation.

Checks factorization by two changes of variable, a smooth beta-integral
quadrature, and delayed Brownian variances by covariance and isometry.
Standard library only; no files are written.
"""

from fractions import Fraction as Q
import math
import os
import resource
import sys
import time


def integrate_polynomial(coefficients, right):
    return sum((c * right ** (j + 1) / (j + 1)
                for j, c in enumerate(coefficients)), Q(0))


def simpson(function, panels=2000):
    step = 1 / panels
    total = function(0) + function(1)
    total += 4 * math.fsum(function(j * step) for j in range(1, panels, 2))
    total += 2 * math.fsum(function(j * step) for j in range(2, panels, 2))
    return total * step / 3


def main():
    started = time.monotonic()
    assert os.environ.get("OMP_NUM_THREADS") == "1"
    priority = os.getpriority(os.PRIO_PROCESS, 0)
    assert priority >= 15, priority

    p, eta = Q(8), Q(3, 16)
    conjugate = p / (p - 1)
    assert 1 / p < eta < Q(1, 4)
    inner_regular = -2 * eta
    inner_singular = -2 * eta - Q(1, 2)
    outer = (eta - 1) * conjugate
    assert (inner_regular, inner_singular, outer) == (
        Q(-3, 8), Q(-7, 8), Q(-13, 14))
    assert 1 / (1 + outer) == 14
    outer_time = (1 + outer) * (p - 1)
    total_time = outer_time + (1 + inner_singular) * p / 2
    assert outer_time == Q(1, 2)
    assert total_time == 1
    print("p=8, eta=3/16: inner exponents -3/8 and -7/8; outer -13/14")
    print("outer factor 14^7*t^(1/2); combined singular factor t^1")

    for moment in (Q(5), Q(6), Q(8), Q(16), Q(100)):
        alpha = (1 / moment + Q(1, 4)) / 2
        assert 1 / moment < alpha < Q(1, 4)
        power = moment * alpha - 1 + (Q(1, 2) - 2 * alpha) * moment / 2
        assert power == moment / 4 - 1 > 0
    print("five independent p>4 scaling checks: p/4 - 1")

    # v=x^8 turns the inner singularities into 8*x^4 and 8*d.
    count = 0
    for root in (Q(1, 4), Q(1), Q(3, 2)):
        for heat_constant in (Q(1, 10), Q(1, 5), Q(1)):
            horizon = root ** 8
            polynomial = (8 * heat_constant, Q(0), Q(0), Q(0), Q(8))
            integral = integrate_polynomial(polynomial, root)
            direct = Q(8, 5) * root ** 5 + 8 * heat_constant * root
            assert integral == direct
            assert root ** 4 * integral ** 4 == (
                horizon * (Q(8, 5) * root ** 4 + 8 * heat_constant) ** 4)
            count += 1
    print(f"inner time integral and factored F(t): {count} exact checks")

    ito_coefficient = p * (p - 1) / 2
    doob = (p / (p - 1)) ** p
    bdg_constant = ito_coefficient ** (p / 2) * doob ** ((p - 2) / 2)
    assert bdg_constant == 28 ** 4 * Q(8, 7) ** 24
    print("terminal martingale constant: 28^4*(8/7)^24, exact")

    # Beta(eta,1-eta): x=y^16 in its (0,infinity) integral,
    # followed by inversion on (1,infinity), removes both singularities.
    beta_quadrature = simpson(lambda y: 16 * (y ** 2 + y ** 12) / (1 + y ** 16))
    beta_closed = math.pi / math.sin(math.pi * float(eta))
    residual = abs(beta_quadrature - beta_closed)
    assert residual < 2e-10
    print(f"factorization beta integral: quadrature residual {residual:.3g}")

    cases = 0
    for delay in (Q(1, 10), Q(1, 2), Q(1), Q(3)):
        cross_covariance = integrate_polynomial((Q(0), Q(1)), delay)
        area_variance = 2 * integrate_polynomial((Q(0), Q(0), Q(1, 2)), delay)
        for drift in (Q(-10), -Q(3, 2) / delay, Q(-1), Q(0), Q(1), Q(5)):
            by_covariance = 2 * delay + 2 * drift * cross_covariance + drift ** 2 * area_variance
            intercept, slope = 1 + drift * delay, -drift
            by_isometry = delay + integrate_polynomial(
                (intercept ** 2, 2 * intercept * slope, slope ** 2), delay)
            completed_square = (5 * delay / 4
                                + delay ** 3 / 3 * (drift + Q(3, 2) / delay) ** 2)
            assert by_covariance == by_isometry == completed_square
            assert by_covariance >= 5 * delay / 4
            if drift == -Q(3, 2) / delay:
                assert by_covariance == 5 * delay / 4
            cases += 1
    print(f"delayed mass variance: {cases} exact covariance/isometry/square checks")

    # Continuous bumps start at zero, with centers uniform on [1/4,3/4].
    # Height sqrt(n), half-width 1/n: E X_t^2 <=4/3 but E max X^2=n.
    for n in (8, 16, 256, 65536):
        half_area = integrate_polynomial((Q(n), Q(-2 * n * n), Q(n ** 3)), Q(1, n))
        marginal_bound = 2 * 2 * half_area
        assert marginal_bound == Q(4, 3)
        assert Q(n) > marginal_bound
    print("four continuous fixed-start spike laws: marginal bound 4/3; max square n")

    for norm in (Q(0), Q(1, 100), Q(1), Q(1000)):
        assert 1 + norm ** 8 <= (1 + norm ** 2) ** 4
    print("four initial-norm moment reductions checked exactly")

    peak = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    peak_bytes = peak if sys.platform == "darwin" else peak * 1024
    elapsed = time.monotonic() - started
    assert peak_bytes < 1024 ** 3
    assert elapsed < 1200
    print(f"nice={priority}; elapsed={elapsed:.3f}s; peak RSS={peak_bytes / 1024**2:.2f} MiB")


if __name__ == "__main__":
    main()
