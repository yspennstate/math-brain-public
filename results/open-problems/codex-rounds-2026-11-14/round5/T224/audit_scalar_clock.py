"""Independent finite-time and exact-arithmetic checks for PROOF.md.

Standard library only. The proof, not this computation, supplies all-time bounds.
Every file written is relative to the current task folder.
"""

import json
import math
import os
import random
import resource
import time
from fractions import Fraction as R
from itertools import product
from pathlib import Path

started = time.monotonic()
rng = random.Random(2240501)


def Q(w):
    return w + w ** 3 / 3


def psi_flow(s, z):
    return 2 * math.sinh(math.asinh(1.5 * (s + Q(z))) / 3)


def a(s, z):
    return math.atan(psi_flow(s, z))


def rk4(field, state, dt):
    k1 = field(state)
    k2 = field(tuple(x + dt * k / 2 for x, k in zip(state, k1)))
    k3 = field(tuple(x + dt * k / 2 for x, k in zip(state, k2)))
    k4 = field(tuple(x + dt * k for x, k in zip(state, k3)))
    return tuple(x + dt * (u + 2 * v + 2 * w + z) / 6
                 for x, u, v, w, z in zip(state, k1, k2, k3, k4))


# Check the closed-form autonomous flow by a polynomial identity, its group
# property, and a centered derivative, all at independently sampled locations.
max_Q_error = max_group_error = max_derivative_error = 0.
for _ in range(500):
    s, r, z = (rng.uniform(-3, 3) for _ in range(3))
    w = psi_flow(s, z)
    max_Q_error = max(max_Q_error, abs(Q(w) - s - Q(z)))
    max_group_error = max(max_group_error,
                          abs(psi_flow(r, w) - psi_flow(s + r, z)))
    eps = 1e-5
    derivative = (a(s + eps, z) - a(s - eps, z)) / (2 * eps)
    exact_derivative = 1 / (1 + w * w) ** 2
    max_derivative_error = max(max_derivative_error,
                               abs(derivative - exact_derivative))
    assert 0 <= exact_derivative <= 1
assert max_Q_error < 5e-14
assert max_group_error < 5e-14
assert max_derivative_error < 2e-9


# Exact multinomial/ordered-sample variance check at deterministic clocks.
# These are arbitrary path laws; no temporal independence is imposed.
path_law = ((R(-1), R(0), R(1)), (R(1, 4), R(1, 2), R(1, 4)))
values, probabilities = path_law
mu = sum(p * v for p, v in zip(probabilities, values))
variance = sum(p * (v - mu) ** 2 for p, v in zip(probabilities, values))
exact_variance_checks = 0
for m in range(1, 7):
    measured = R(0)
    for labels in product(range(3), repeat=m):
        probability = math.prod(probabilities[j] for j in labels)
        empirical_mean = sum(values[j] for j in labels) / m
        measured += probability * (empirical_mean - mu) ** 2
    assert measured == variance / m
    exact_variance_checks += 1


# Test the clock comparison with exact constant-coefficient evolution on
# piecewise intervals. Sign-changing forcing, zero damping, and long intervals
# are allowed; no Euler discretization of the comparison is used.
max_clock_to_integral_ratio = 0.
for _ in range(500):
    q = integral = 0.
    for interval in range(12):
        damping = rng.choice((0., .001, .1, 1., 10.))
        forcing = rng.uniform(-2, 2)
        duration = 10 ** rng.uniform(-2, 2)
        if damping:
            decay = math.exp(-damping * duration)
            q = decay * q + forcing * math.expm1(-damping * duration) / damping
        else:
            q -= forcing * duration
        integral += abs(forcing) * duration
        assert abs(q) <= integral * (1 + 1e-13)
        max_clock_to_integral_ratio = max(max_clock_to_integral_ratio,
                                          abs(q) / integral)


# Independently integrate raw particle equations and the clock equations.
# The law has atoms 0 and 1 with equal probabilities; enumerate all binomial
# compositions. Include a stationary mean-field trajectory whose finite clocks
# initially point in opposite directions for different samples.
targets = (-math.pi / 2, .2, math.pi / 8, .7, math.pi / 2)
widths = (1, 2, 4, 8)
dt, steps = .005, 400
max_particle_clock_error = max_clock_comparison_violation = 0.
max_expected_error_to_bound_ratio = 0.
stationary_opposite_signs = False
finite_flow_cases = 0
for gamma in targets:
    for m in widths:
        all_errors = [0.] * (steps + 1)
        for n in range(m + 1):
            p = n / m
            probability = math.comb(m, n) / 2 ** m

            # State = (population clock, empirical clock, integral |zeta|,
            #          raw population atom 0, raw population atom 1,
            #          raw finite atom 0, raw finite atom 1).
            state = (0., 0., 0., 0., 1., 0., 1.)

            def field(s):
                tau, tau_m, _, v0, v1, w0, w1 = s
                f_tau = (a(tau, 0) + a(tau, 1)) / 2
                empirical_at_tau = (1 - p) * a(tau, 0) + p * a(tau, 1)
                empirical_at_random_clock = ((1 - p) * a(tau_m, 0)
                                               + p * a(tau_m, 1))
                raw_f = (math.atan(v0) + math.atan(v1)) / 2
                raw_fm = (1 - p) * math.atan(w0) + p * math.atan(w1)
                return (gamma - f_tau, gamma - empirical_at_random_clock,
                        abs(empirical_at_tau - f_tau),
                        (gamma - raw_f) / (1 + v0 * v0),
                        (gamma - raw_f) / (1 + v1 * v1),
                        (gamma - raw_fm) / (1 + w0 * w0),
                        (gamma - raw_fm) / (1 + w1 * w1))

            for j in range(steps + 1):
                tau, tau_m, integral, v0, v1, w0, w1 = state
                max_particle_clock_error = max(
                    max_particle_clock_error,
                    abs(v0 - psi_flow(tau, 0)), abs(v1 - psi_flow(tau, 1)),
                    abs(w0 - psi_flow(tau_m, 0)), abs(w1 - psi_flow(tau_m, 1)))
                max_clock_comparison_violation = max(
                    max_clock_comparison_violation, abs(tau_m - tau) - integral)
                raw_f = (math.atan(v0) + math.atan(v1)) / 2
                raw_fm = (1 - p) * math.atan(w0) + p * math.atan(w1)
                all_errors[j] += probability * (raw_fm - raw_f) ** 2
                if gamma == math.pi / 8 and j == steps:
                    assert abs(tau) < 1e-13
                    if n == 0:
                        assert tau_m > 0
                    if n == m:
                        assert tau_m < 0
                        stationary_opposite_signs = True
                if j < steps:
                    state = rk4(field, state, dt)
            finite_flow_cases += 1
        for j, expected_error in enumerate(all_errors):
            bound = (math.pi / 2) ** 2 * (1 + j * dt) ** 2 / m
            assert expected_error <= bound + 1e-12
            max_expected_error_to_bound_ratio = max(
                max_expected_error_to_bound_ratio, expected_error / bound)

assert max_particle_clock_error < 2e-9
assert max_clock_comparison_violation < 2e-9


# Exact rational arithmetic for the horizon prefactor and exponent, including
# T=0, B=0, A=0. The exponent balance is obtained separately from the two powers.
for _ in range(500):
    A, B, C = (R(rng.randrange(0, 31), 10) for _ in range(3))
    u = R(rng.randrange(1, 50), 1)
    T = u - 1
    assert 1 + B * B * T <= max(R(1), B * B) * u
    assert 4 * A * A * (1 + B * B * T) ** 2 <= (
        4 * A * A * max(R(1), B ** 4) * u ** 2)
    # The two triangle inequalities used for the all-time factor 4 and 6.
    e, r = (R(rng.randrange(-30, 31), 7) for _ in range(2))
    assert 2 * (e + r) ** 2 + 2 * r ** 2 <= 4 * e ** 2 + 6 * r ** 2

exponents = []
for c in (R(1, 10), R(1, 4), R(1, 2), R(1), R(3, 2), R(2)):
    horizon_power = 1 / (c + 2)
    exponent = c / (c + 2)
    assert 2 * horizon_power - 1 == -exponent
    assert -c * horizon_power == -exponent
    # Independent optimization over rational polynomial horizon scales.
    for j in range(501):
        s = R(j, 1000)
        assert min(1 - 2 * s, c * s) <= exponent
    exponents.append({"c": str(c), "width_exponent": str(exponent)})


# Re-derive the arctan example's constants without using the clock integral:
# at large w, w' ~ 1/w^3, whence w^4 ~ 4t and L ~ 1/(2 sqrt(t)).
# Exact arithmetic checks the clock calculation produces the same constants.
# Raise (3^(4/3)/4) * (2 sqrt(2)/3)^(4/3)=1 to the third power.
assert R(3) ** 4 / R(4) ** 3 * (R(2) ** 6 / R(3) ** 4) == 1
beta = 3 * math.sqrt(3) / 8
assert abs(2 / math.sqrt(3) / (1 + R(1, 3)) ** 2 - beta) < 1e-15
assert abs(beta * 2 * math.sqrt(2) / 3 - math.sqrt(6) / 4) < 1e-15

asymptotic_samples = []
for s in (1e3, 1e6, 1e9, 1e12):
    # Use atan(1/w), avoiding loss of precision near pi/2.
    e = (math.atan(1 / psi_flow(s, 0))
         + math.atan(1 / psi_flow(s, 1))) / 2
    ratio = e * (3 * s) ** (1 / 3)
    assert abs(ratio - 1) < .02
    asymptotic_samples.append({"clock": s, "residual_to_asymptotic_ratio": ratio})

nice_value = os.getpriority(os.PRIO_PROCESS, 0)
rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
assert nice_value >= 15
assert rss < 1024 ** 3
result = {
    "status": "PASS", "seed": 2240501,
    "autonomous_flow_checks": 500,
    "max_implicit_flow_identity_error": max_Q_error,
    "max_flow_group_identity_error": max_group_error,
    "max_feature_clock_derivative_error": max_derivative_error,
    "exact_ordered_sample_variance_checks": exact_variance_checks,
    "piecewise_exact_clock_comparisons": 6000,
    "max_clock_to_integrated_forcing_ratio": max_clock_to_integral_ratio,
    "finite_neural_flow_cases": finite_flow_cases,
    "finite_neural_flow_time_points_per_case": steps + 1,
    "max_raw_particle_to_clock_error": max_particle_clock_error,
    "max_clock_comparison_violation": max_clock_comparison_violation,
    "max_expected_output_error_to_bound_ratio": max_expected_error_to_bound_ratio,
    "stationary_mean_field_opposite_empirical_clocks_checked": stationary_opposite_signs,
    "exact_horizon_prefactor_checks": 500,
    "exact_exponents": exponents,
    "asymptotic_samples": asymptotic_samples,
    "actual_nice": nice_value, "max_rss_bytes_macos": rss,
    "elapsed_seconds": time.monotonic() - started,
    "scope": "Finite-time flow, scalar comparison, variance and constant checks; no infinite-time simulation or sharpness claim."
}
Path("scalar_clock_results.json").write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps(result, indent=2))
