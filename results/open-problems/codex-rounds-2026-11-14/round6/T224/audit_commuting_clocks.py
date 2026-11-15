"""Independent algebra and finite-flow audits for PROOF.md; standard library.

The all-time theorem is proved analytically. Finite trajectories test identities,
not an infinite-time or sharpness assertion. All output paths are local to cwd.
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
rng = random.Random(2240601)


def dot(x, y):
    return sum(a * b for a, b in zip(x, y))


def norm(x):
    return math.sqrt(dot(x, x))


def sub(x, y):
    return tuple(a - b for a, b in zip(x, y))


def matvec(C, v):
    return tuple(dot(row, v) for row in C)


def transpose_vec(C, v):
    return tuple(sum(C[i][j] * v[i] for i in range(len(C)))
                 for j in range(len(C[0])))


def Q(w):
    return w + w ** 3 / 3


def invQ(q):
    return 2 * math.sinh(math.asinh(1.5 * q) / 3)


def scalar_flow(s, z):
    return invQ(s + Q(z))


def joint_flow(s, z, C):
    clocks = transpose_vec(C, s)
    return tuple(scalar_flow(u, x) for u, x in zip(clocks, z))


def feature(w, C):
    return matvec(C, tuple(math.atan(x) for x in w))


def gradient_rows(w, C):
    return tuple(tuple(c / (1 + x * x) for c, x in zip(row, w))
                 for row in C)


def mean_feature(points, weights, C):
    fs = [feature(w, C) for w in points]
    return tuple(sum(p * f[j] for p, f in zip(weights, fs))
                 for j in range(len(C)))


def rk4(field, state, dt):
    k1 = field(state)
    k2 = field(tuple(x + dt * k / 2 for x, k in zip(state, k1)))
    k3 = field(tuple(x + dt * k / 2 for x, k in zip(state, k2)))
    k4 = field(tuple(x + dt * k for x, k in zip(state, k3)))
    return tuple(x + dt * (a + 2 * b + 2 * c + d) / 6
                 for x, a, b, c, d in zip(state, k1, k2, k3, k4))


# Exact Gram positivity in dimensions k,d that need not be equal. No numerical
# eigensolver is used. Singular matrices and zero diagonal entries are allowed.
for _ in range(300):
    k, d = rng.randrange(1, 5), rng.randrange(1, 5)
    C = tuple(tuple(R(rng.randrange(-5, 6), 7) for _ in range(d))
              for _ in range(k))
    h = tuple(R(rng.randrange(-5, 6), 3) for _ in range(k))
    diagonal = tuple(R(rng.randrange(0, 9), 8) for _ in range(d))
    J = tuple(tuple(sum(C[i][l] * diagonal[l] * C[j][l]
                        for l in range(d)) for j in range(k))
              for i in range(k))
    assert all(J[i][j] == J[j][i] for i in range(k) for j in range(k))
    Ct_h = transpose_vec(C, h)
    assert dot(h, matvec(J, h)) == sum(a * b * b
                                      for a, b in zip(diagonal, Ct_h)) >= 0


# Closed-form action and finite differences for a coupled two-output feature map.
# The nonorthogonal mixing C produces off-diagonal Gram matrices. Its two
# feature gradients commute although physical output clocks are coupled.
C = ((1., .5), (1 / 3, 1.))
B2 = sum(c * c for row in C for c in row)  # Frobenius bound on ||Dpsi||^2
A2 = B2 * math.pi ** 2 / 2
max_group_error = max_action_derivative_error = max_gram_error = 0.
largest_offdiagonal = 0.
for _ in range(500):
    s, r, z = (tuple(rng.uniform(-2, 2) for _ in range(2)) for _ in range(3))
    w = joint_flow(s, z, C)
    lhs = joint_flow(r, w, C)
    rhs = joint_flow(tuple(a + b for a, b in zip(s, r)), z, C)
    max_group_error = max(max_group_error, norm(sub(lhs, rhs)))
    rows = gradient_rows(w, C)
    eps = 1e-5
    for j in range(2):
        sp = tuple(a + (eps if l == j else 0) for l, a in enumerate(s))
        sm = tuple(a - (eps if l == j else 0) for l, a in enumerate(s))
        action_fd = tuple(a / (2 * eps) for a in
                          sub(joint_flow(sp, z, C), joint_flow(sm, z, C)))
        max_action_derivative_error = max(max_action_derivative_error,
                                          norm(sub(action_fd, rows[j])))
        output_fd = tuple(a / (2 * eps) for a in
                          sub(feature(joint_flow(sp, z, C), C),
                              feature(joint_flow(sm, z, C), C)))
        gram_column = tuple(dot(row, rows[j]) for row in rows)
        max_gram_error = max(max_gram_error, norm(sub(output_fd, gram_column)))
    largest_offdiagonal = max(largest_offdiagonal, abs(dot(rows[0], rows[1])))
assert max_group_error < 1e-13
assert max_action_derivative_error < 1e-8
assert max_gram_error < 1e-8
assert largest_offdiagonal > .1


# Exact vector iid variance, with correlated output coordinates and a nonuniform
# law. Ordered samples are used, independently of multinomial enumeration below.
atoms_exact = ((R(1), R(-1)), (R(2), R(3)), (R(-2), R(1)))
probs_exact = (R(1, 4), R(1, 4), R(1, 2))
mu = tuple(sum(p * a[j] for a, p in zip(atoms_exact, probs_exact))
           for j in range(2))
variance = sum(p * dot(sub(a, mu), sub(a, mu))
               for a, p in zip(atoms_exact, probs_exact))
for m in range(1, 7):
    measured = R(0)
    for labels in product(range(3), repeat=m):
        p = math.prod(probs_exact[j] for j in labels)
        sample_mean = tuple(sum(atoms_exact[j][l] for j in labels) / m
                            for l in range(2))
        measured += p * dot(sub(sample_mean, mu), sub(sample_mean, mu))
    assert measured == variance / m


# Independent time-dependent PSD comparison, using exact exponentials of
# rank-one matrices. Successive matrices are usually noncommuting; assuming a
# scalar integrating factor would be invalid. Zero damping is included.
max_clock_forcing_ratio = 0.
largest_matrix_commutator = 0.
for _ in range(500):
    q, integral, previous = (0., 0.), 0., None
    for _ in range(12):
        angle = rng.uniform(-math.pi, math.pi)
        v = (math.cos(angle), math.sin(angle))
        damping = rng.choice((0., .001, .1, 1., 10.))
        duration = 10 ** rng.uniform(-2, 2)
        forcing = tuple(rng.uniform(-2, 2) for _ in range(2))
        parallel_q, parallel_f = dot(v, q), dot(v, forcing)
        if damping:
            decay = math.exp(-damping * duration)
            integrated_decay = -math.expm1(-damping * duration) / damping
        else:
            decay, integrated_decay = 1., duration
        q = tuple(q[j] + (decay - 1) * parallel_q * v[j]
                  - duration * (forcing[j] - parallel_f * v[j])
                  - integrated_decay * parallel_f * v[j] for j in range(2))
        integral += duration * norm(forcing)
        assert norm(q) <= integral * (1 + 2e-13)
        max_clock_forcing_ratio = max(max_clock_forcing_ratio, norm(q) / integral)
        K = tuple(tuple(damping * a * b for b in v) for a in v)
        if previous:
            comm = tuple(tuple(sum(K[i][l] * previous[l][j]
                                    - previous[i][l] * K[l][j] for l in range(2))
                               for j in range(2)) for i in range(2))
            largest_matrix_commutator = max(largest_matrix_commutator,
                                             max(abs(x) for row in comm for x in row))
        previous = K
assert largest_matrix_commutator > .1


# Compare separately integrated raw neurons and vector clocks, summing exactly
# over every three-atom sample composition. Population atoms have correlated
# coordinates. The same sampled law drives both output directions.
atoms = ((0., 0.), (1., -.5), (-.5, 1.))
probabilities = tuple(float(p) for p in probs_exact)
f0 = mean_feature(atoms, probabilities, C)
targets = (f0, (.2, -.3), matvec(C, (math.pi / 2, math.pi / 2)))
widths = (1, 2, 4, 8)
dt, steps = .005, 200
max_raw_clock_error = max_comparison_violation = 0.
max_expected_error_ratio = max_stationary_clock = 0.
flow_cases = 0
for gamma in targets:
    for m in widths:
        expected_errors = [0.] * (steps + 1)
        total_probability = R(0)
        for n0 in range(m + 1):
            for n1 in range(m - n0 + 1):
                counts = (n0, n1, m - n0 - n1)
                weights = tuple(n / m for n in counts)
                coefficient = math.factorial(m)
                for n in counts:
                    coefficient //= math.factorial(n)
                exact_probability = R(coefficient) * math.prod(
                    p ** n for p, n in zip(probs_exact, counts))
                total_probability += exact_probability
                probability = float(exact_probability)
                # tau(2), tau_m(2), integral|zeta|(1), raw population(6),
                # raw empirical(6). Zero-weight atoms cause no problems.
                state = (0.,) * 5 + tuple(x for a in atoms for x in a) * 2

                def field(s):
                    tau, taum = s[:2], s[2:4]
                    pop = tuple(tuple(s[5 + 2 * i:7 + 2 * i]) for i in range(3))
                    finite = tuple(tuple(s[11 + 2 * i:13 + 2 * i]) for i in range(3))
                    population_at_clock = tuple(joint_flow(tau, a, C) for a in atoms)
                    empirical_at_clock = tuple(joint_flow(taum, a, C) for a in atoms)
                    F = mean_feature(population_at_clock, probabilities, C)
                    Fm = mean_feature(empirical_at_clock, weights, C)
                    zeta = sub(mean_feature(population_at_clock, weights, C), F)
                    pop_r = sub(gamma, mean_feature(pop, probabilities, C))
                    empirical_r = sub(gamma, mean_feature(finite, weights, C))
                    raw = []
                    for points, residual in ((pop, pop_r), (finite, empirical_r)):
                        for w in points:
                            raw.extend(transpose_vec(gradient_rows(w, C), residual))
                    return sub(gamma, F) + sub(gamma, Fm) + (norm(zeta),) + tuple(raw)

                for j in range(steps + 1):
                    tau, taum, integral = state[:2], state[2:4], state[4]
                    pop = tuple(tuple(state[5 + 2 * i:7 + 2 * i]) for i in range(3))
                    finite = tuple(tuple(state[11 + 2 * i:13 + 2 * i]) for i in range(3))
                    for points, clock in ((pop, tau), (finite, taum)):
                        for initial, actual in zip(atoms, points):
                            max_raw_clock_error = max(max_raw_clock_error,
                                norm(sub(actual, joint_flow(clock, initial, C))))
                    max_comparison_violation = max(max_comparison_violation,
                                                    norm(sub(taum, tau)) - integral)
                    delta = sub(mean_feature(finite, weights, C),
                                mean_feature(pop, probabilities, C))
                    expected_errors[j] += probability * dot(delta, delta)
                    if gamma == f0:
                        max_stationary_clock = max(max_stationary_clock, norm(tau))
                    if j < steps:
                        state = rk4(field, state, dt)
                flow_cases += 1
        assert total_probability == 1
        for j, error in enumerate(expected_errors):
            bound = A2 * (1 + B2 * j * dt) ** 2 / m
            assert error <= bound + 1e-11
            max_expected_error_ratio = max(max_expected_error_ratio, error / bound)
assert max_raw_clock_error < 2e-8
assert max_comparison_violation < 2e-7
assert max_stationary_clock < 1e-12


# Noncommuting obstruction: derive rational matrix from gradient and flow
# derivatives independently, then compare with a finite difference of the exact
# ordered flow. The example has normalized input second moment E X^2=1.
alpha2 = R(2, 5)
assert (alpha2 + 4 * alpha2) / 2 == 1
output_factors = (R(1, 2), R(2, 5))
clock_factors = (R(1, 5), R(2, 5))
J = tuple(tuple(alpha2 / 2 * a * b for b in clock_factors)
          for a in output_factors)
assert J == ((R(1, 50), R(1, 25)), (R(2, 125), R(4, 125)))
h = (R(1), R(-1))
negative_form = dot(h, matvec(J, h))
sym_offdiagonal = (J[0][1] + J[1][0]) / 2
negative_determinant = J[0][0] * J[1][1] - sym_offdiagonal ** 2
assert negative_form == R(-1, 250)
assert negative_determinant == R(-9, 62500)
alpha = math.sqrt(float(alpha2))
sstar = (0., 35 / (6 * math.sqrt(2)))


def ordered_feature(s):
    u1 = invQ(float(alpha2) / math.sqrt(2) * s[0])
    q2 = u1 + 4 * u1 ** 3 / 3
    u2 = invQ(2 * q2 + 2 * math.sqrt(2) * float(alpha2) * s[1]) / 2
    return (math.atan(u2) / math.sqrt(2), math.atan(2 * u2) / math.sqrt(2))


assert norm(sub(ordered_feature(sstar),
                (math.atan(1) / math.sqrt(2), math.atan(2) / math.sqrt(2)))) < 1e-14
eps = 1e-5
max_obstruction_jacobian_error = 0.
for j in range(2):
    plus = tuple(x + (eps if l == j else 0) for l, x in enumerate(sstar))
    minus = tuple(x - (eps if l == j else 0) for l, x in enumerate(sstar))
    fd = tuple(x / (2 * eps) for x in sub(ordered_feature(plus), ordered_feature(minus)))
    max_obstruction_jacobian_error = max(max_obstruction_jacobian_error,
                                         max(abs(fd[i] - float(J[i][j])) for i in range(2)))
assert max_obstruction_jacobian_error < 1e-9
monotonicity_ratios = []
for eps in (.01, .001, .0001):
    plus = tuple(x + eps * float(v) for x, v in zip(sstar, h))
    ratio = dot(h, sub(ordered_feature(plus), ordered_feature(sstar))) / eps
    assert ratio < 0
    assert abs(ratio - float(negative_form)) < 1e-4
    monotonicity_ratios.append(ratio)
# Direct derivatives at u=1 check the bracket constant separately.
X1, X2 = alpha / (2 * math.sqrt(2)), 2 * alpha / (5 * math.sqrt(2))
DX1, DX2 = -float(alpha2) / (2 * math.sqrt(2)), -8 * math.sqrt(2) * float(alpha2) / 25
bracket = DX2 * X1 - DX1 * X2
assert abs(bracket + 6 * alpha ** 3 / 100) < 1e-16


# A separate random stream checks commutation from raw field derivatives,
# rather than assuming it from the joint action. Rational points give exact
# cancellation, including degenerate fields and unequal k,d.
second_rng = random.Random(2240602)
for _ in range(300):
    k, d = second_rng.randrange(1, 5), second_rng.randrange(1, 5)
    mixing = tuple(tuple(R(second_rng.randrange(-5, 6), 7) for _ in range(d))
                   for _ in range(k))
    w = tuple(R(second_rng.randrange(-5, 6), 3) for _ in range(d))
    fields = tuple(tuple(c / (1 + x * x) for c, x in zip(row, w))
                   for row in mixing)
    derivative_diagonals = tuple(tuple(-2 * c * x / (1 + x * x) ** 2
                                       for c, x in zip(row, w)) for row in mixing)
    for i in range(k):
        for j in range(k):
            assert all(derivative_diagonals[j][l] * fields[i][l]
                       - derivative_diagonals[i][l] * fields[j][l] == 0
                       for l in range(d))


# Check the transported bracket integral independently by quadrature after
# changing variables from clock to parameter. The endpoint derivative formula
# gives E=X2(end)*(X1(start)/X2(start)-X1(end)/X2(end)); the bracket integral gives
# -X2(end)*integral R'(u)du, where R(u)=(1+4u^2)/(2(1+u^2)).
# Include both signs of the oriented integration interval.
max_defect_integral_error = 0.
for _ in range(60):
    u0, u1 = (second_rng.uniform(-2, 2) for _ in range(2))
    X2_end = math.sqrt(2) * alpha / (1 + 4 * u1 * u1)
    ratio0 = (1 + 4 * u0 * u0) / (2 * (1 + u0 * u0))
    ratio1 = (1 + 4 * u1 * u1) / (2 * (1 + u1 * u1))
    endpoint_defect = X2_end * (ratio0 - ratio1)
    n = 400
    step = (u1 - u0) / n

    def integrand(u):
        return -X2_end * 3 * u / (1 + u * u) ** 2

    integral_defect = step / 3 * (integrand(u0) + integrand(u1)
        + sum((4 if j % 2 else 2) * integrand(u0 + j * step) for j in range(1, n)))
    max_defect_integral_error = max(max_defect_integral_error,
                                    abs(endpoint_defect - integral_defect))
assert max_defect_integral_error < 1e-9


# Independently compare source two-input raw equations and the old scalar
# equations under a_j=sqrt(2)w_j. All 300 residuals include both signs.
max_source_rescaling_error = 0.
for _ in range(300):
    a, residual = (second_rng.uniform(-3, 3) for _ in range(2))
    w = a / math.sqrt(2)
    psi_derivative = 1 / (1 + 2 * w * w)
    raw_wprime = (residual / math.sqrt(2)) * psi_derivative
    scalar_aprime = residual / (1 + a * a)
    max_source_rescaling_error = max(max_source_rescaling_error,
        abs(math.sqrt(2) * raw_wprime - scalar_aprime))
assert max_source_rescaling_error < 2e-15


# Constants and exponents re-derived with exact arithmetic, in vector form.
for _ in range(300):
    B = R(rng.randrange(0, 31), 10)
    u = R(rng.randrange(1, 50))
    assert 1 + B * B * (u - 1) <= max(R(1), B * B) * u
    e = tuple(R(rng.randrange(-20, 21), 7) for _ in range(3))
    r = tuple(R(rng.randrange(-20, 21), 7) for _ in range(3))
    er = tuple(a + b for a, b in zip(e, r))
    assert 2 * dot(er, er) + 2 * dot(r, r) <= 4 * dot(e, e) + 6 * dot(r, r)
exponents = []
for c in (R(1, 10), R(1, 4), R(1, 2), R(1), R(3, 2), R(2)):
    horizon, rate = 1 / (c + 2), c / (c + 2)
    assert 2 * horizon - 1 == -rate == -c * horizon
    exponents.append({"c": str(c), "rate": str(rate)})
# Input scaling in the source example cancels exactly in a_j=sqrt(2)w_j.
assert R(2) * R(1, 2) == 1
assert R(1, 2) * R(1, 2) + R(1, 2) * R(1, 2) == R(1, 2)

nice_value = os.getpriority(os.PRIO_PROCESS, 0)
rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
assert nice_value >= 15
assert rss < 1024 ** 3
result = {
    "status": "PASS", "seed": 2240601,
    "exact_gram_cases": 300,
    "exact_raw_field_commutation_cases": 300,
    "joint_flow_cases": 500,
    "max_joint_group_error": max_group_error,
    "max_joint_action_derivative_error": max_action_derivative_error,
    "max_feature_gram_jacobian_error": max_gram_error,
    "largest_gram_offdiagonal": largest_offdiagonal,
    "exact_vector_variance_checks": 6,
    "piecewise_exact_matrix_comparisons": 6000,
    "largest_time_matrix_commutator_entry": largest_matrix_commutator,
    "max_clock_to_integrated_forcing_ratio": max_clock_forcing_ratio,
    "raw_particle_clock_flow_cases": flow_cases,
    "time_points_per_case": steps + 1,
    "max_raw_particle_clock_error": max_raw_clock_error,
    "max_clock_comparison_violation": max_comparison_violation,
    "max_expected_error_to_bound_ratio": max_expected_error_ratio,
    "stationary_population_clock_maximum": max_stationary_clock,
    "noncommuting_obstruction": {
        "exact_jacobian": [[str(x) for x in row] for row in J],
        "negative_quadratic_form": str(negative_form),
        "symmetric_part_determinant": str(negative_determinant),
        "max_jacobian_finite_difference_error": max_obstruction_jacobian_error,
        "finite_difference_monotonicity_ratios": monotonicity_ratios,
        "bracket_at_scaled_parameter_one": bracket,
        "transported_defect_integral_checks": 60,
        "max_transported_defect_integral_error": max_defect_integral_error,
    },
    "source_example_rescaling_checks": 300,
    "max_source_example_rescaling_error": max_source_rescaling_error,
    "exact_vector_prefactor_checks": 300,
    "exact_exponents": exponents,
    "actual_nice": nice_value,
    "max_rss_bytes_macos": rss,
    "elapsed_seconds": time.monotonic() - started,
    "scope": "Finite-flow and algebra audits; all-time theorem is analytic. Noncommuting example obstructs the clock proof, not T224 itself.",
}
Path("commuting_clock_results.json").write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps(result, indent=2))
