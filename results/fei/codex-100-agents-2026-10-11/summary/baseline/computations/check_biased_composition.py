#!/usr/bin/env python3
"""Finite checks for biased thresholds and disjoint composition.

Run with Python 3.10+: python check_biased_composition.py
No third-party packages, randomness, network, or repository access are used.

Fourier probabilities, influence/variance, and coefficient/composition identities
are checked with exact Fraction arithmetic. Only entropy logarithms use floats.
Passing these finite checks is a reproducibility aid, not a formal proof.
"""
from fractions import Fraction as Q
from math import fsum, isclose, log, log2
import json

A = 23 + log(16)
C_THRESHOLD = 20 * A / log(2)
ABS_TOL, REL_TOL = 2e-12, 2e-10


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def entropy_term(p, reference=Q(1)):
    if not p:
        return 0.0
    require(p > 0 and reference > 0, "entropy requires positive support")
    return float(p) * log2(float(reference / p))


def spectrum(probabilities, function):
    """Canonical Fourier data, freezing coordinates with probability 0 or 1.

    The exact tensor transform expands f in products of (y_i-q_i).
    If c[S] is that rational coefficient, the orthonormal Fourier probability
    is c[S]^2 * product_{i in S} q_i(1-q_i).
    """
    qs = tuple(map(Q, probabilities))
    require(all(0 <= q <= 1 for q in qs), "invalid input probability")
    active = [i for i, q in enumerate(qs) if 0 < q < 1]
    coefficients = []
    for mask in range(1 << len(active)):
        x = [int(q == 1) for q in qs]
        for j, i in enumerate(active):
            x[i] = (mask >> j) & 1
        value = function(tuple(x))
        require(value in (-1, 1), "the function must be Boolean ±1")
        coefficients.append(Q(value))
    for j, i in enumerate(active):
        step = 1 << j
        for start in range(0, len(coefficients), 2 * step):
            for offset in range(step):
                k = start + offset
                left, right = coefficients[k], coefficients[k + step]
                coefficients[k] = (1 - qs[i]) * left + qs[i] * right
                coefficients[k + step] = right - left

    c, p, sigma = {}, {}, {}
    for mask, coefficient in enumerate(coefficients):
        original_mask = sum(1 << i for j, i in enumerate(active)
                            if (mask >> j) & 1)
        variance_product = Q(1)
        for j, i in enumerate(active):
            if (mask >> j) & 1:
                variance_product *= qs[i] * (1 - qs[i])
        c[original_mask] = coefficient
        p[original_mask] = coefficient * coefficient * variance_product
        sigma[original_mask] = (4 ** mask.bit_count()) * variance_product
        require(0 <= p[original_mask] <= sigma[original_mask],
                "P(S) must lie between 0 and sigma_S^2")

    mean = c[0]
    variance = sum((mass for mask, mass in p.items() if mask), Q())
    influences = [sum((mass for mask, mass in p.items() if mask & (1 << i)),
                      Q()) for i in range(len(qs))]
    influence = sum(influences, Q())
    require(sum(p.values(), Q()) == 1, "Parseval")
    require(variance == 1 - mean * mean, "variance normalization")
    require(influence >= variance, "nonnegative spectral deficit")
    hplus = fsum(entropy_term(mass, sigma[mask])
                 for mask, mass in p.items() if mask)
    require(hplus >= -ABS_TOL, "nonnegative corrected entropy")
    return dict(q=qs, c=c, p=p, sigma=sigma, mean=mean, variance=variance,
                influence=influence, influences=influences,
                deficit=influence - variance, hplus=hplus,
                entropy=fsum(entropy_term(mass) for mass in p.values()))


def threshold(t):
    return lambda x: 1 if sum(x) >= t else -1


def parity(x):
    return 1 if sum(x) % 2 == 0 else -1


def count_probability(qs, target):
    law = [Q(1)]
    for q in qs:
        new = [Q()] * (len(law) + 1)
        for k, mass in enumerate(law):
            new[k] += (1 - q) * mass
            new[k + 1] += q * mass
        law = new
    return law[target] if 0 <= target < len(law) else Q()


def profile(n, kind):
    patterns = {
        "fair": [Q(1, 2)],
        "equal_rare": [Q(1, 31)],
        "heterogeneous": [Q(1, 3), Q(2, 5), Q(5, 7), Q(3, 4)],
        "near_deterministic": [Q(1, 4096), Q(4095, 4096),
                               Q(1, 64), Q(63, 64), Q(1, 3)],
        "frozen": [Q(0), Q(1), Q(1, 2), Q(2, 7)],
    }
    pattern = patterns[kind]
    return tuple(pattern[i % len(pattern)] for i in range(n))


def threshold_checks():
    count = zero_deficit = near_case = zero_coefficients = unit_mass = 0
    worst = dict(ratio=0.0)
    for n in range(8):
        for kind in ("fair", "equal_rare", "heterogeneous",
                     "near_deterministic", "frozen"):
            qs = profile(n, kind)
            for t in range(n + 2):  # Includes both constant functions.
                data = spectrum(qs, threshold(t))
                rho = [count_probability(qs[:i] + qs[i + 1:], t - 1)
                       for i in range(n)]
                for i in range(n):
                    sigma_i = 4 * qs[i] * (1 - qs[i])
                    require(data["influences"][i] == sigma_i * rho[i],
                            "pivotal influence normalization")
                    require(data["p"].get(1 << i, Q()) ==
                            sigma_i * rho[i] ** 2,
                            "singleton coefficient normalization")
                j = sum((4 * qs[i] * (1 - qs[i]) * rho[i] * (1 - rho[i])
                         for i in range(n)), Q())
                require(j == sum((mask.bit_count() * mass
                                  for mask, mass in data["p"].items()
                                  if mask.bit_count() >= 2), Q()),
                        "J equals higher-degree influence")
                require(j <= 2 * data["deficit"], "J <= 2 Delta")
                tolerance = ABS_TOL + REL_TOL * data["hplus"]
                require(data["hplus"] * log(2) <=
                        A * float(data["influence"]) + tolerance,
                        "finite weak threshold inequality")
                require(data["hplus"] <=
                        C_THRESHOLD * float(data["deficit"]) + tolerance,
                        "finite strong threshold inequality")
                if data["deficit"] == 0:
                    zero_deficit += 1
                    require(data["hplus"] == 0.0, "zero deficit must give H+=0")
                else:
                    ratio = data["hplus"] / float(data["deficit"])
                    if ratio > worst["ratio"]:
                        worst = dict(ratio=ratio, n=n, threshold=t,
                                     biases=list(map(str, qs)))
                near_case += bool(rho and max(rho) > Q(9, 10))
                zero_coefficients += sum(mass == 0 for mass in data["p"].values())
                unit_mass += any(mass == 1 for mass in data["p"].values())
                count += 1
    # Explicit coefficient-zero/one and biased-dictator sanity checks.
    for n in range(1, 8):
        data = spectrum(profile(n, "fair"), parity)
        require(data["p"][(1 << n) - 1] == 1, "uniform parity atom")
        require(data["entropy"] == data["hplus"] == 0.0, "unit atom entropy")
    dictator = spectrum([Q(1, 4096)], threshold(1))
    require(dictator["deficit"] == dictator["hplus"] == 0,
            "corrected biased dictator normalization")
    require(dictator["entropy"] > 0, "raw biased entropy differs from H+")
    return dict(instances=count, zero_deficit_instances=zero_deficit,
                near_dictator_instances=near_case,
                exact_zero_coefficients=zero_coefficients,
                unit_spectral_atom_instances=unit_mass,
                uniform_parity_cases=7, largest_observed_hplus_over_deficit=worst,
                rare_dictator_raw_entropy_over_influence=
                dictator["entropy"] / float(dictator["influence"]))


def composition_checks():
    """Check signed coefficients, squared probabilities, and entropy identities."""
    const_plus = lambda x: 1
    const_minus = lambda x: -1
    families = [
        [(3, threshold(2)), (2, parity), (2, threshold(1))],
        [(2, threshold(2)), (2, threshold(1)), (3, threshold(2))],
        [(1, threshold(1)), (2, const_plus), (1, const_minus)],
        [(1, const_plus), (1, const_minus), (1, const_plus)],
    ]
    gates = [
        ("or", threshold(1)), ("majority", threshold(2)),
        ("and", threshold(3)), ("parity", parity),
        ("selector", lambda z: 2 * (z[1] if z[0] else z[2]) - 1),
    ]
    count = coefficients_checked = constant_children = 0
    max_entropy_error = 0.0
    for family in families:
        n = sum(size for size, _ in family)
        for kind in ("fair", "heterogeneous", "near_deterministic", "frozen"):
            qs = profile(n, kind)
            children, offsets = [], []
            offset = 0
            for size, function in family:
                offsets.append(offset)
                children.append(spectrum(qs[offset:offset + size], function))
                offset += size
            output_q = [(1 + child["mean"]) / 2 for child in children]
            for _, gate in gates:
                outer = spectrum(output_q, gate)

                def composed(x):
                    outputs = [(function(x[offset:offset + size]) + 1) // 2
                               for (size, function), offset in zip(family, offsets)]
                    return gate(tuple(outputs))

                full = spectrum(qs, composed)
                for mask in range(1 << n):
                    active_blocks = 0
                    coefficient_product = Q(1)
                    probability_product = Q(1)
                    possible = True
                    for i, ((size, _), offset, child) in enumerate(
                            zip(family, offsets, children)):
                        local = (mask >> offset) & ((1 << size) - 1)
                        if local:
                            active_blocks |= 1 << i
                            coefficient_product *= child["c"].get(local, Q()) / 2
                            if child["variance"] == 0:
                                possible = False
                            else:
                                probability_product *= (child["p"].get(local, Q()) /
                                                        child["variance"])
                    expected_c = outer["c"].get(active_blocks, Q()) * coefficient_product
                    expected_p = (outer["p"].get(active_blocks, Q()) * probability_product
                                  if possible else Q())
                    require(full["c"].get(mask, Q()) == expected_c,
                            "exact signed composition coefficient")
                    require(full["p"].get(mask, Q()) == expected_p,
                            "exact composition Fourier probability")
                    coefficients_checked += 1
                weights = [(outer["influences"][i] / child["variance"]
                            if child["variance"] else Q())
                           for i, child in enumerate(children)]
                require(full["variance"] == outer["variance"], "composition variance")
                require(full["influence"] ==
                        sum((a * child["influence"]
                             for a, child in zip(weights, children)), Q()),
                        "exact composition influence")
                require(full["deficit"] == outer["deficit"] +
                        sum((a * child["deficit"]
                             for a, child in zip(weights, children)), Q()),
                        "exact composition deficit")
                expected_hplus = outer["hplus"] + fsum(
                    float(a) * child["hplus"] for a, child in zip(weights, children))
                error = abs(full["hplus"] - expected_hplus)
                max_entropy_error = max(max_entropy_error, error)
                require(isclose(full["hplus"], expected_hplus,
                                abs_tol=ABS_TOL, rel_tol=REL_TOL),
                        "composition corrected entropy")
                constant_children += sum(child["variance"] == 0 for child in children)
                count += 1
    return dict(instances=count, exact_coefficient_and_probability_checks=coefficients_checked,
                constant_child_occurrences=constant_children,
                largest_absolute_entropy_identity_error=max_entropy_error)


def main():
    result = {
        "status": "PASS",
        "scope": "Deterministic finite checks; not a formal verification or proof.",
        "arithmetic": "Exact fractions except entropy logarithms and inequality constants.",
        "entropy_tolerance": {"absolute": ABS_TOL, "relative": REL_TOL},
        "threshold_constant": C_THRESHOLD,
        "thresholds": threshold_checks(),
        "composition": composition_checks(),
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

