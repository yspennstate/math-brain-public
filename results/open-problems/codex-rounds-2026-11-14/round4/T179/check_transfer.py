"""Scalar diagnostics for PROOF.md; no SPDE simulation or uniqueness test.

Checks Volterra constants in two forms, two heat trace expansions, and
Girsanov density signs by exact rational Gaussian calculations.
"""

from fractions import Fraction as Q
import math
import os
import resource
import sys
import time


def main():
    started = time.monotonic()
    if os.environ.get('OMP_NUM_THREADS') != '1':
        raise SystemExit('Set OMP_NUM_THREADS=1')
    priority = os.getpriority(os.PRIO_PROCESS, 0)
    if priority < 15:
        raise SystemExit(f'nice={priority}; need at least 15')

    count = 0
    for horizon in (Q(1, 100), Q(1), Q(10)):
        for drift_bound in (Q(0), Q(1, 3), Q(7)):
            for growth_bound in (Q(1, 10), Q(1), Q(5)):
                a1 = 6 * (horizon * drift_bound**2 + growth_bound**2)
                # a2=6 G^2/sqrt(8 pi); 16 pi a2^2=72 G^4.
                a2_square_times_pi = Q(9, 2) * growth_bound**4
                lam = 1 + 4 * a1 + 16 * a2_square_times_pi
                simplified = (1 + 24 * (horizon * drift_bound**2
                                         + growth_bound**2)
                              + 72 * growth_bound**4)
                assert lam == simplified
                assert 4 * a1 <= lam
                # Equivalent to a2 sqrt(pi)/sqrt(lambda) <= 1/4.
                assert 16 * a2_square_times_pi <= lam
                absorption = float(a1 / lam) + math.sqrt(
                    float(a2_square_times_pi / lam))
                assert absorption <= 0.5
                count += 1
    print(f'Volterra absorption: {count} exact parameter triples passed')
    print('lambda = 1 + 24(T B^2 + G^2) + 72 G^4')
    print('each Laplace-kernel term <= 1/4; total <= 1/2')

    for r in (1e-6, 1e-4, 1e-2, 1.0):
        fourier = 1 + 2 * math.fsum(
            math.exp(-8 * math.pi**2 * k * k * r)
            for k in range(1, 2001))
        images = math.ceil(math.sqrt(8 * r * 50))
        gaussian = (1 + 2 * math.fsum(
            math.exp(-m * m / (8 * r))
            for m in range(1, images + 1))) / math.sqrt(8 * math.pi * r)
        upper = 1 + 1 / math.sqrt(8 * math.pi * r)
        assert math.isclose(fourier, gaussian, rel_tol=3e-14, abs_tol=3e-14)
        assert fourier <= upper
        print(f'r={r:g}; heat trace={fourier:.12g}; upper={upper:.12g}; '
              f'expansion gap={abs(fourier-gaussian):.3g}')

    count = 0
    for sigma in (Q(-3), Q(-1, 2), Q(1, 2), Q(2)):
        for drift in (Q(-2), Q(0), Q(3, 2)):
            for horizon in (Q(1, 5), Q(2)):
                theta = drift / sigma
                energy = theta**2 * horizon
                # Under the tilted law W^0 = W^b + theta t.
                brownian_sample = Q(7, 11)
                w0 = brownian_sample + theta * horizon
                log_forward = theta * w0 - energy / 2
                log_reverse = -theta * brownian_sample - energy / 2
                assert log_forward + log_reverse == 0
                # Gaussian MGF normalization: exponent + variance/2=0.
                assert -energy / 2 + theta**2 * horizon / 2 == 0
                mass_mean_after_tilt = sigma * theta * horizon
                assert mass_mean_after_tilt == drift * horizon
                expected_log_forward = theta**2 * horizon - energy / 2
                expected_log_inverse_under_zero = energy / 2
                assert expected_log_forward == energy / 2
                assert expected_log_inverse_under_zero == energy / 2
                count += 1
    print(f'Gaussian density, inverse signs, both entropies: {count} exact cases')
    print('sigma of either sign; positive, zero, negative drift included')

    # The example h=dist(x,0)^(-a) is in L2 precisely when 2a<1.
    for a in (Q(1, 10), Q(1, 4), Q(49, 100)):
        assert 1 - 2 * a > 0
    assert 1 - 2 * Q(1, 2) == 0
    print('rough initial example: 3 integrable exponents; a=1/2 excluded')

    peak = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    peak_bytes = peak if sys.platform == 'darwin' else peak * 1024
    assert peak_bytes < 1024**3
    elapsed = time.monotonic() - started
    assert elapsed < 30
    print(f'nice={priority}; elapsed={elapsed:.3f}s; '
          f'peak RSS={peak_bytes / 1024**2:.2f} MiB')


if __name__ == '__main__':
    main()
