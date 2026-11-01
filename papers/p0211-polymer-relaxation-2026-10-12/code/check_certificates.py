#!/usr/bin/env python3
"""Reproduce finite checks for the linear-polymer relaxation theorem.

Run with Python 3.10 or later:

    python code/check_certificates.py

The standard-library checks use exact rational arithmetic. They verify the
stationary projection, direct polymer transition rates, the discrete-gradient
intertwining, the scalar certificates, and both coupling marginals. Small
multivariate-polynomial calculations check the certificate cancellations as
identities, rather than only at sample parameter values.

If NumPy is installed, a separate numerical check compares the entire labelled
cut-chain spectrum with the independently constructed radial-sector spectra,
and checks the bounds against directly enumerated polymer generators.

These checks are reproducibility aids. The all-parameter theorem is proved in
the accompanying paper; this program is not a formalization of that proof.
No network access or nonstandard dependency is required for the exact checks.
"""

from __future__ import annotations

import argparse
from collections import Counter, defaultdict
from datetime import datetime, timezone
from fractions import Fraction as F
from itertools import combinations
import json
from math import comb, factorial, prod, sqrt
from pathlib import Path
import platform
import sys


class Polynomial:
    """Small exact polynomial ring Q[n, a, k, ell]."""

    def __init__(self, terms=None):
        self.terms = {e: F(c) for e, c in (terms or {}).items() if c}

    @classmethod
    def constant(cls, value):
        return cls({(0, 0, 0, 0): value})

    @classmethod
    def variable(cls, index):
        exponent = [0] * 4
        exponent[index] = 1
        return cls({tuple(exponent): 1})

    @staticmethod
    def cast(value):
        return value if isinstance(value, Polynomial) else Polynomial.constant(value)

    def __add__(self, other):
        out = defaultdict(F, self.terms)
        for exponent, coefficient in self.cast(other).terms.items():
            out[exponent] += coefficient
        return Polynomial(out)

    __radd__ = __add__

    def __neg__(self):
        return Polynomial({e: -c for e, c in self.terms.items()})

    def __sub__(self, other):
        return self + (-self.cast(other))

    def __rsub__(self, other):
        return self.cast(other) + (-self)

    def __mul__(self, other):
        out = defaultdict(F)
        for e1, c1 in self.terms.items():
            for e2, c2 in self.cast(other).terms.items():
                out[tuple(x + y for x, y in zip(e1, e2))] += c1 * c2
        return Polynomial(out)

    __rmul__ = __mul__


def polynomial_identities():
    n, a, k, ell = (Polynomial.variable(i) for i in range(4))
    identities = {
        "double_reciprocal_death_killing_cancellation":
            -2 * k * (k - 1) + 2 * k * (k + a - 1) - 2 * k * a,
        "count_reciprocal_positive_remainder":
            k * (k + a - 1) - k * (k - 1) - k * a,
        "harmonic_sector_death_killing_cancellation":
            -(k - 1) * (k - ell)
            + ell * (k - 1) * (k + a - 1)
            - (k - 1) * ((ell - 1) * k + ell * a),
        "coupling_stage_II_death_killing_cancellation":
            -k * k + k * (k + a - 1) - k * (a - 1),
        "up_down_tower_induction_coefficient":
            (k - 1) * (n - 2 * ell - k + 2)
            + n - 2 * (ell + k - 1)
            - k * (n - 2 * ell - k + 1),
    }
    for name, residual in identities.items():
        assert not residual.terms, (name, residual.terms)
    return {"identities": list(identities), "all_residual_coefficients_zero": True}


def add_rate(rates, target, rate):
    if rate:
        rates[target] += rate


def edge_rates(mask, n, beta):
    rates = defaultdict(F)
    k = mask.bit_count()
    for i in range(n):
        bit = 1 << i
        if mask & bit:
            if k > 1:
                add_rate(rates, mask ^ bit, F(k - 1, n))
        else:
            add_rate(rates, mask | bit, beta)
    return dict(rates)


def cut_partition(mask, n):
    cuts = [i for i in range(n) if mask & (1 << i)]
    lengths = [((cuts[(i + 1) % len(cuts)] - cuts[i]) % n) or n
               for i in range(len(cuts))]
    multiplicities = Counter(lengths)
    return tuple(multiplicities[j] for j in range(1, n + 1))


def integer_partitions(n, minimum=1):
    if n == 0:
        yield ()
    for part in range(minimum, n + 1):
        for tail in integer_partitions(n - part, part):
            yield (part,) + tail


def polymer_states(n):
    return sorted({tuple(parts.count(j) for j in range(1, n + 1))
                   for parts in integer_partitions(n)})


def polymer_rates(m, n, beta):
    """Construct transitions directly from unordered polymer instances."""
    rates = defaultdict(F)
    for size in range(2, n + 1):
        count = m[size - 1]
        if not count:
            continue
        for left in range(1, size // 2 + 1):
            right = size - left
            target = list(m)
            target[size - 1] -= 1
            target[left - 1] += 1
            target[right - 1] += 1
            add_rate(rates, tuple(target), beta * count * (1 if left == right else 2))
    for left in range(1, n + 1):
        if not m[left - 1]:
            continue
        for right in range(left, n - left + 1):
            if not m[right - 1] or (left == right and m[left - 1] < 2):
                continue
            target = list(m)
            target[left - 1] -= 1
            target[right - 1] -= 1
            target[left + right - 1] += 1
            if left == right:
                rate = F(m[left - 1] * (m[left - 1] - 1), n)
            else:
                rate = F(2 * m[left - 1] * m[right - 1], n)
            add_rate(rates, tuple(target), rate)
    return dict(rates)


def projection_checks():
    cases = cut_sets = rate_identities = detailed_balance_identities = 0
    for n in range(2, 9):
        states = polymer_states(n)
        p = {mask: cut_partition(mask, n) for mask in range(1, 1 << n)}
        multiplicity = Counter(p.values())
        assert set(multiplicity) == set(states)
        for m in states:
            formula = F(n * factorial(sum(m) - 1), prod(factorial(x) for x in m))
            assert formula == multiplicity[m], (n, m, formula, multiplicity[m])
        cut_sets += len(p)
        for beta in (F(1, 100), F(1, n), F(3)):
            cases += 1
            flow = {m: defaultdict(F) for m in states}
            for mask, m in p.items():
                for target, rate in edge_rates(mask, n, beta).items():
                    flow[m][p[target]] += rate
            weights = {m: (beta * n) ** sum(m) / prod(factorial(x) for x in m)
                       for m in states}
            direct = {m: polymer_rates(m, n, beta) for m in states}
            for m in states:
                averaged = {target: rate / multiplicity[m]
                            for target, rate in flow[m].items()}
                assert averaged == direct[m], (n, str(beta), m, averaged, direct[m])
                rate_identities += len(direct[m])
                for target, rate in direct[m].items():
                    assert weights[m] * rate == weights[target] * direct[target][m]
                    detailed_balance_identities += 1
    return {"n_range": [2, 8], "parameter_cases": cases,
            "distinct_cut_sets_enumerated": cut_sets,
            "averaged_transition_rate_identities": rate_identities,
            "polymer_detailed_balance_identities": detailed_balance_identities,
            "includes_n_2_and_two_cluster_double_boundaries": True}


def count_intertwining_checks():
    entries = cases = 0
    for n in range(2, 13):
        for beta in (F(1, 10000), F(1, n), F(100)):
            cases += 1
            q = [[F(0) for _ in range(n)] for _ in range(n)]
            for row, k in enumerate(range(1, n + 1)):
                if k < n:
                    q[row][row + 1] = beta * (n - k)
                if k > 1:
                    q[row][row - 1] = F(k * (k - 1), n)
                q[row][row] = -sum(q[row])
            a = [[F(0) for _ in range(n - 1)] for _ in range(n - 1)]
            for row, k in enumerate(range(1, n)):
                birth = beta * (n - k - 1)
                death = F(k * (k - 1), n)
                if row + 1 < n - 1:
                    a[row][row + 1] = birth
                if row:
                    a[row][row - 1] = death
                a[row][row] = -birth - death - beta - F(2 * k, n)
            for row in range(n - 1):
                ad = [F(0) for _ in range(n)]
                for j in range(n - 1):
                    ad[j] -= a[row][j]
                    ad[j + 1] += a[row][j]
                dq = [q[row + 1][j] - q[row][j] for j in range(n)]
                assert ad == dq, (n, beta, row)
                entries += n
    return {"n_range": [2, 12], "parameter_cases": cases,
            "exact_matrix_entry_identities": entries}


def killed_quotient(birth, death, killing, z, h):
    value = killing
    if birth:
        value += birth * (1 - h(z + 1) / h(z))
    if death:
        value += death * (1 - h(z - 1) / h(z))
    return value


def sample_integers(lower, upper, a):
    if upper < lower:
        return []
    if upper - lower <= 40:
        return range(lower, upper + 1)
    floor_a = a.numerator // a.denominator
    return sorted({x for x in (lower, lower + 1, upper - 1, upper,
                               (lower + upper) // 2, floor_a - 1,
                               floor_a, floor_a + 1) if lower <= x <= upper})


def certificate_checks():
    counts = Counter()
    minima = {"count_reciprocal_over_sqrt_beta": None,
              "sector_reciprocal_over_sqrt_beta": None,
              "coupling_stage_II_over_sqrt_beta": None}

    def track(key, value):
        if minima[key] is None or value < minima[key]:
            minima[key] = value

    for n in (2, 3, 4, 5, 7, 8, 9, 16, 31, 100, 1000):
        for root_scale in sorted({F(1, 10), F(1, 2), F(1), F(2),
                                  F(n, 4), F(n, 2), F(n), F(2 * n), F(100 * n)}):
            sqrt_beta = root_scale / n
            beta = sqrt_beta ** 2
            a = max(F(1), root_scale)
            h = lambda k: 1 / ((k + a) * (k + a + 1))
            for k in sample_integers(1, n - 1, a):
                actual = killed_quotient(beta * (n - k - 1), F(k * (k - 1), n),
                                         beta + F(2 * k, n), k, h)
                claimed = 2 * beta * (n - k - 1) / (k + a + 2) + beta \
                    + 2 * k * a / (n * (k + a - 1))
                assert actual == claimed
                assert actual <= beta + 4 * max(sqrt_beta, F(1, n))
                counts["double_reciprocal_upper"] += 1
            s = beta + sqrt_beta + F(1, n)
            available_lower_bound = beta + F(2, n)
            if n >= 8 and F(4, n * n) <= beta <= F(1, 16):
                available_lower_bound = max(available_lower_bound, sqrt_beta / 5)
            assert available_lower_bound >= s / 6
            counts["final_parameter_combination"] += 1

    for n in (8, 9, 16, 31, 100, 1000):
        for a in sorted({F(2), F(n, 4), (F(2) + F(n, 4)) / 2}):
            sqrt_beta = a / n
            beta = sqrt_beta ** 2
            h = lambda z: 1 / (z + a)
            for k in sample_integers(1, n - 1, a):
                actual = killed_quotient(beta * (n - k - 1), F(k * (k - 1), n),
                                         beta + F(2 * k, n), k, h)
                simple_lower = beta * (n - k - 1) / (k + a + 1) + beta + F(k, n)
                assert actual >= simple_lower >= sqrt_beta / 5
                track("count_reciprocal_over_sqrt_beta", actual / sqrt_beta)
                counts["count_reciprocal_lower"] += 1
            degrees = range(1, n // 2 + 1) if n <= 31 else sorted({1, 2, 3, n // 4, n // 2})
            for ell in degrees:
                for k in sample_integers(ell, n - ell, a):
                    birth = beta * (n - k - ell)
                    death = F((k - 1) * (k - ell), n)
                    killing = ell * beta + F(ell * (k - 1), n)
                    actual = killed_quotient(birth, death, killing, k, h)
                    claimed = birth / (k + a + 1) + ell * beta \
                        + F(k - 1, n) * ((ell - 1) * k + ell * a) / (k + a - 1)
                    assert actual == claimed and actual >= sqrt_beta / 5
                    track("sector_reciprocal_over_sqrt_beta", actual / sqrt_beta)
                    counts["harmonic_sector_reciprocal_lower"] += 1
            for r in sample_integers(0, n - 2, a):
                actual = killed_quotient(beta * (n - r - 2), F(r * r, n),
                                         beta + F(r, n), r, h)
                claimed = beta * (n - r - 2) / (r + a + 1) + beta \
                    + F(r, n) * (a - 1) / (r + a - 1)
                assert actual == claimed and actual >= sqrt_beta / 5
                track("coupling_stage_II_over_sqrt_beta", actual / sqrt_beta)
                counts["coupling_stage_II_reciprocal_lower"] += 1
    return {"checked_parameter_point_counts": dict(counts),
            "minimum_ratios_on_checked_points":
                {key: {"exact": str(value), "decimal": float(value)}
                 for key, value in minima.items()},
            "sampling_scope": "All relevant k and degrees for n <= 31; selected boundary and interior points for n = 100, 1000."}


def stage_one_events(x, y, n, beta):
    events = defaultdict(F)
    k = x.bit_count()
    assert x & y == x and (x ^ y).bit_count() == 1
    for i in range(n):
        bit = 1 << i
        if not y & bit:
            add_rate(events, (x | bit, y | bit), beta)
        elif x & bit:
            add_rate(events, (x ^ bit, y ^ bit), F(k - 1, n))
            add_rate(events, (x, y ^ bit), F(1, n))
        else:
            add_rate(events, (x | bit, y), beta)
            add_rate(events, (x, y ^ bit), F(k, n))
    return dict(events)


def stage_two_events(x, y, n, beta):
    events = defaultdict(F)
    r = (x & y).bit_count()
    assert x.bit_count() == y.bit_count() == r + 1
    for i in range(n):
        bit = 1 << i
        if not (x | y) & bit:
            add_rate(events, (x | bit, y | bit), beta)
        elif (x & y) & bit:
            add_rate(events, (x ^ bit, y ^ bit), F(r, n))
    add_rate(events, (x | y, x | y), beta)
    add_rate(events, (x & y, x & y), F(r, n))
    return dict(events)


def check_marginals(events, x, y, n, beta):
    marginal_x, marginal_y = defaultdict(F), defaultdict(F)
    for (next_x, next_y), rate in events.items():
        assert next_x and next_y and rate > 0
        if next_x != x:
            marginal_x[next_x] += rate
        if next_y != y:
            marginal_y[next_y] += rate
    assert dict(marginal_x) == edge_rates(x, n, beta)
    assert dict(marginal_y) == edge_rates(y, n, beta)


def coupling_checks():
    counts = Counter()
    for n in range(2, 8):
        masks = range(1, 1 << n)
        for beta in (F(1, 100), F(1, n)):
            for x in masks:
                for i in range(n):
                    if x & (1 << i):
                        continue
                    y = x | (1 << i)
                    events = stage_one_events(x, y, n, beta)
                    check_marginals(events, x, y, n, beta)
                    k = x.bit_count()
                    internal = defaultdict(F)
                    exit_rate = F(0)
                    for (next_x, next_y), rate in events.items():
                        if next_x != next_y and next_x & next_y == next_x:
                            assert (next_x ^ next_y).bit_count() == 1
                            internal[next_x.bit_count() - k] += rate
                        else:
                            if next_x != next_y:
                                assert next_x.bit_count() == next_y.bit_count()
                                assert (next_x ^ next_y).bit_count() == 2
                            exit_rate += rate
                    assert internal[1] == beta * (n - k - 1)
                    assert internal[-1] == F(k * (k - 1), n)
                    assert exit_rate == beta + F(2 * k, n)
                    counts["stage_I_state_parameter_cases"] += 1
            for x, y in combinations(masks, 2):
                if x.bit_count() != y.bit_count() or (x ^ y).bit_count() != 2:
                    continue
                events = stage_two_events(x, y, n, beta)
                check_marginals(events, x, y, n, beta)
                r = (x & y).bit_count()
                internal = defaultdict(F)
                absorption = F(0)
                for (next_x, next_y), rate in events.items():
                    if next_x == next_y:
                        absorption += rate
                    else:
                        assert next_x.bit_count() == next_y.bit_count()
                        assert (next_x ^ next_y).bit_count() == 2
                        internal[(next_x & next_y).bit_count() - r] += rate
                assert internal[1] == beta * (n - r - 2)
                assert internal[-1] == F(r * r, n)
                assert absorption == beta + F(r, n)
                counts["stage_II_state_parameter_cases"] += 1
    return {"n_range": [2, 7], **dict(counts),
            "marginals_internal_rates_and_absorption_rates_exact": True}


def numerical_checks():
    try:
        import numpy as np
    except ImportError:
        return {"status": "skipped", "reason": "NumPy is not installed."}

    def symmetric_negative_generator(states, rate_function):
        index = {state: i for i, state in enumerate(states)}
        rates = {state: rate_function(state) for state in states}
        matrix = np.zeros((len(states), len(states)), dtype=float)
        for state, outgoing in rates.items():
            row = index[state]
            matrix[row, row] = float(sum(outgoing.values()))
            for target, rate in outgoing.items():
                matrix[row, index[target]] = -sqrt(float(rate) * float(rates[target][state]))
        return matrix

    def radial_spectrum(n, beta, ell):
        first, last = (1, n) if ell == 0 else (ell, n - ell)
        matrix = np.zeros((last - first + 1, last - first + 1))
        for row, k in enumerate(range(first, last + 1)):
            birth = float(beta * (n - k - ell))
            death = (k - 1) * (k - ell) / n
            killing = float(ell * beta) + ell * (k - 1) / n
            matrix[row, row] = birth + death + killing
            if k < last:
                next_death = k * (k + 1 - ell) / n
                matrix[row, row + 1] = matrix[row + 1, row] = -sqrt(birth * next_death)
        return np.linalg.eigvalsh(matrix)

    cases = 0
    max_error = 0.0
    max_scaled_error = 0.0
    sample_rows = []
    for n in range(2, 9):
        for beta in (F(1, 10**8), F(1, n * n), F(1, n), F(1), F(100)):
            cases += 1
            states_b = list(range(1, 1 << n))
            direct_b = np.linalg.eigvalsh(symmetric_negative_generator(
                states_b, lambda mask: edge_rates(mask, n, beta)))
            count_spectrum = radial_spectrum(n, beta, 0)
            sectors = list(count_spectrum)
            for ell in range(1, n // 2 + 1):
                multiplicity = comb(n, ell) - comb(n, ell - 1)
                sectors.extend(np.repeat(radial_spectrum(n, beta, ell), multiplicity))
            sectors = np.sort(sectors)
            assert len(sectors) == len(direct_b)
            error = float(np.max(np.abs(sectors - direct_b)))
            scale = max(1.0, float(np.max(np.abs(direct_b))))
            max_error = max(max_error, error)
            max_scaled_error = max(max_scaled_error, error / scale)
            assert error <= 1e-10 * scale, (n, beta, error, scale)
            direct_m = np.linalg.eigvalsh(symmetric_negative_generator(
                polymer_states(n), lambda m: polymer_rates(m, n, beta)))
            gamma_m = float(direct_m[1])
            gamma_b = float(direct_b[1])
            gamma_q = float(count_spectrum[1])
            b = float(beta)
            s = b + sqrt(b) + 1 / n
            tolerance = 1e-9 * max(1.0, gamma_m, gamma_q)
            assert gamma_m + tolerance >= s / 6
            assert gamma_m <= 4 * s + tolerance
            assert gamma_m + tolerance >= b + 2 / n
            assert gamma_m <= gamma_q + tolerance
            assert gamma_m + tolerance >= gamma_b
            if n >= 8 and F(4, n * n) <= beta <= F(1, 16):
                assert gamma_b + tolerance >= sqrt(b) / 5
            if beta == F(1, n):
                sample_rows.append({"n": n, "beta": str(beta),
                                    "polymer_gap": gamma_m,
                                    "count_gap": gamma_q,
                                    "cut_gap": gamma_b,
                                    "polymer_gap_over_sqrt_beta": gamma_m / sqrt(b)})
    return {"status": "passed", "numpy_version": np.__version__,
            "n_range": [2, 8], "parameter_cases": cases,
            "largest_full_cut_matrix_dimension": 255,
            "maximum_full_spectrum_absolute_discrepancy": max_error,
            "maximum_full_spectrum_scaled_discrepancy": max_scaled_error,
            "absolute_discrepancy_tolerance": "1e-10 times max(1, spectral radius)",
            "beta_equals_one_over_n_samples": sample_rows}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path,
                        default=Path(__file__).resolve().parents[1] / "results" / "verification_results.json")
    parser.add_argument("--skip-numerical", action="store_true")
    args = parser.parse_args()
    results = {
        "status": "passed",
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "python_version": platform.python_version(),
        "scope": "Exact finite checks and optional numerical checks; not a formal proof of the full theorem.",
        "polynomial_identities": polynomial_identities(),
        "stationary_projection": projection_checks(),
        "count_intertwining": count_intertwining_checks(),
        "scalar_certificates": certificate_checks(),
        "coupling": coupling_checks(),
        "numerical_spectra": {"status": "skipped", "reason": "Requested --skip-numerical."}
                            if args.skip_numerical else numerical_checks(),
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(results, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": results["status"], "output": str(args.output),
                      "numerical_status": results["numerical_spectra"]["status"]}, indent=2))


if __name__ == "__main__":
    if not __debug__:
        sys.exit("Run without -O: exact verification uses Python assertions.")
    main()
