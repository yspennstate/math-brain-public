"""Small independent diagnostics for PROOF.md, not an SPDE simulation.

Integrate the two-stage Gaussian density to check both entropy directions,
including asymmetric history-dependent energy. Check time-average errors
by exact integration of piecewise polynomials. Standard library only.
"""

from fractions import Fraction as Q
import math
import os
import resource
import sys
import time


def simpson(f, left, right, panels=2000):
    step = (right - left) / panels
    total = f(left) + f(right)
    total += 4 * math.fsum(f(left + j * step)
                           for j in range(1, panels, 2))
    total += 2 * math.fsum(f(left + j * step)
                           for j in range(2, panels, 2))
    return total * step / 3


def phi(x):
    return math.exp(-x * x / 2) / math.sqrt(2 * math.pi)


def gaussian_check(s, d, a, k):
    shift = a * math.sqrt(s)
    first_energy = a * a * s
    second_energy = k * k * d
    prob_positive = (1 + math.erf(shift / math.sqrt(2))) / 2

    # Integrate each half-line separately; the gate jumps at zero.
    norm = forward = reverse = energy0 = energyb = 0.0
    for left, right, gate in ((-13.0, 0.0, 0), (0.0, 13.0, 1)):
        def tilted(r):
            return phi(r) * math.exp(shift * r - first_energy / 2)

        norm += simpson(tilted, left, right)
        # Integrating out the second independent Gaussian increment
        # gives these conditional expectations, before the r integral.
        forward += simpson(
            lambda r: tilted(r) * (shift * r - first_energy / 2
                                   + second_energy * gate / 2), left, right)
        reverse += simpson(
            lambda r: phi(r) * (-shift * r + first_energy / 2
                                + second_energy * gate / 2), left, right)
        energy0 += simpson(
            lambda r: phi(r) * (first_energy + second_energy * gate),
            left, right)
        energyb += simpson(
            lambda r: tilted(r) * (first_energy + second_energy * gate),
            left, right)

    target0 = first_energy + second_energy / 2
    targetb = first_energy + second_energy * prob_positive
    assert abs(norm - 1) < 2e-9
    assert math.isclose(energy0, target0, abs_tol=2e-8, rel_tol=2e-9)
    assert math.isclose(energyb, targetb, abs_tol=2e-8, rel_tol=2e-9)
    assert math.isclose(reverse, target0 / 2, abs_tol=2e-8, rel_tol=2e-9)
    assert math.isclose(forward, targetb / 2, abs_tol=2e-8, rel_tol=2e-9)
    if k != 0 and a != 0:
        assert (forward - reverse) * a > 0
    return max(abs(norm - 1), abs(2 * reverse - target0),
               abs(2 * forward - targetb))


def polynomial_integral(coefficients, left, right):
    return sum((coefficient * (right ** (j + 1) - left ** (j + 1))
                / (j + 1) for j, coefficient in enumerate(coefficients)), Q(0))


def average_check(tau):
    # Causal average of 1_[a,b) over a window tau. Direct polynomial
    # integration of the error, compared with independent triangle areas.
    a, b = Q(1, 4), Q(1, 2)
    assert tau < b - a and b + tau < 1
    total_l1 = total_l2_square = Q(0)
    # On the rising edge, |average - f| = 1 - (t-a)/tau.
    # On the falling edge, |average - f| = 1 - (t-b)/tau.
    for edge in (a, b):
        intercept, slope = 1 + edge / tau, -1 / tau
        total_l1 += polynomial_integral((intercept, slope), edge, edge + tau)
        total_l2_square += polynomial_integral(
            (intercept ** 2, 2 * intercept * slope, slope ** 2),
            edge, edge + tau)
    assert total_l1 == tau
    assert total_l2_square == 2 * tau / 3


def main():
    started = time.monotonic()
    assert os.environ.get("OMP_NUM_THREADS") == "1"
    priority = os.getpriority(os.PRIO_PROCESS, 0)
    assert priority >= 15, priority
    largest = 0.0
    count = 0
    for s in (0.25, 1.0, 2.25):
        for d in (1 / 3, 2.0):
            for a in (-2.0, 0.0, 1.5):
                for k in (-3.0, 0.0, 2.0):
                    largest = max(largest, gaussian_check(s, d, a, k))
                    count += 1
    print(f"Two-stage history-dependent Gaussian laws: {count} cases passed")
    print("Normalization and both entropies checked by 1D quadrature")
    print("Positive/negative first drift and history control; zero cases included")
    print(f"Largest normalization/doubled-entropy residual: {largest:.3g}")
    print("Entropy difference has the sign of the first drift when k != 0")
    for denominator in (8, 16, 64, 1000):
        average_check(Q(1, denominator))
    print("Causal time average: four exact piecewise-polynomial error checks")
    print("L1 error = window; squared L2 error = 2*window/3")
    peak = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    peak_bytes = peak if sys.platform == "darwin" else peak * 1024
    elapsed = time.monotonic() - started
    assert peak_bytes < 1024**3
    assert elapsed < 1200
    print(f"nice={priority}; elapsed={elapsed:.3f}s; "
          f"peak RSS={peak_bytes / 1024**2:.2f} MiB")


if __name__ == "__main__":
    main()
