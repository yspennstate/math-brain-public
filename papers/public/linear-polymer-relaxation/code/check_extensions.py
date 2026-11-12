#!/usr/bin/env python3
"""Independent finite checks for the revised polymer manuscript.

These checks verify algebra and independently constructed finite generators.
The proofs in the manuscript, rather than sampled eigenvalues, establish the
all-parameter results. Requires NumPy and SciPy; no network access is used.
"""
from __future__ import annotations

from collections import defaultdict
from datetime import datetime, timezone
from fractions import Fraction
from itertools import combinations
import json
import platform
from math import factorial, prod, sqrt
from pathlib import Path

import numpy as np
import scipy
from scipy.linalg import eigh_tridiagonal

from check_certificates import Polynomial, edge_rates, polymer_rates, polymer_states


def exact_identities():
    n, a, k, ell = (Polynomial.variable(i) for i in range(4))
    r = k - ell + 1
    # Substitute beta=a(a-1)/[n(n+a+1)] and clear positive denominators.
    sharp = (
        2*a*(a-1)*(k+a-1)*(k+a+2)
        + 2*a*(a-1)*(n-k-1)*(k+a-1)
        + 2*k*a*(n+a+1)*(k+a+2)
        - 2*a*(n+a+1)*(k+a-1)*(k+a+2)
        + 6*a*(a-1)*(n+a+1)
    )
    # Here beta=a^2/[n(n+a)], for the new degree-one certificate.
    degree_one = (
        a*a*(k+a-1)*(k+a+1)
        + (k-1)*(n+a)*(k+a-1)*(k+a+1)
        + a*a*(n-k-1)*(k+a-1)
        - (k-1)*(k-1)*(n+a)*(k+a+1)
        - a*(n+a)*(k+a-1)*(k+a+1)
        + 2*a*a*(n+a)
    )
    identities = {
        "sharp_rising_factorial_certificate": sharp,
        "higher_sector_birth_difference": (n-k-ell)-(n-r-1)+2*(ell-1),
        "higher_sector_death_difference":
            (k-1)*(k-ell)-r*(r-1)-(ell-2)*(r-1),
        "higher_sector_killing_difference":
            ell*(k-1)-2*r-(ell-2)*(r+ell),
        "sharp_degree_one_reciprocal_certificate": degree_one,
        # In these two identities a denotes b and ell denotes h(k+1)/h(k).
        # Death terms are identical and cancel before denominators are cleared.
        "critical_count_finite_error_quotient":
            a*(n-k-1)*(1-ell)+a+2*k*n
            - n*(a*(1-ell)+2*k)
            - a*(1+(k+1)*(ell-1)),
        "critical_degree_one_finite_error_quotient":
            a*(n-k-2)*(1-ell)+a+k*n
            - n*(a*(1-ell)+k)
            - a*(1+(k+2)*(ell-1)),
    }
    for name, residual in identities.items():
        assert not residual.terms, (name, residual.terms)
    rational_cases = 0
    for n0 in range(2, 15):
        for b in (Fraction(1, 1000), Fraction(1, n0*n0), Fraction(1, n0), Fraction(3)):
            for k0 in range(1, n0):
                h = lambda x: Fraction(1, x)
                q = b
                if k0 < n0-1:
                    q += b*(n0-k0-1)*(1-h(k0+1)/h(k0))
                if k0 > 1:
                    q += Fraction((k0-1)**2, n0)*(1-h(k0-1)/h(k0))
                q += Fraction(k0-1, n0)
                assert q == b*n0/Fraction(k0+1)
                rational_cases += 1
    return {"polynomial_identities": list(identities), "all_zero": True,
            "degree_one_exact_rational_cases": rational_cases}


def radial_data(n, beta, ell=None):
    if ell is None:  # Count derivative, whose bottom is the count gap.
        k = np.arange(1, n, dtype=float)
        birth = beta*(n-k-1)
        death = k*(k-1)/n
        killing = beta+2*k/n
    else:
        k = np.arange(ell, n-ell+1, dtype=float)
        birth = beta*(n-k-ell)
        death = (k-1)*(k-ell)/n
        killing = ell*beta+ell*(k-1)/n
    return birth, death, killing


def radial_eigen(n, beta, ell=None, vectors=False):
    birth, death, killing = radial_data(n, beta, ell)
    diagonal = birth+death+killing
    off = -np.sqrt(birth[:-1]*death[1:])
    return eigh_tridiagonal(diagonal, off, select="i", select_range=(0, 0),
                            eigvals_only=not vectors)


def reversible_matrix(states, rates):
    index = {state: i for i, state in enumerate(states)}
    out = {state: rates(state) for state in states}
    matrix = np.zeros((len(states), len(states)))
    for state, outgoing in out.items():
        i = index[state]
        matrix[i, i] = sum(map(float, outgoing.values()))
        for target, rate in outgoing.items():
            matrix[i, index[target]] = -sqrt(float(rate)*float(out[target][state]))
    return matrix


def spectral_checks():
    worst_equality = 0.0
    cases = 0
    for n in range(2, 11):
        for beta in (1e-9, 1/n**2, 1/n, 1.0, 100.0):
            gamma = float(radial_eigen(n, beta)[0])
            matrix = reversible_matrix(polymer_states(n),
                                       lambda m: polymer_rates(m, n, beta))
            actual = float(np.linalg.eigvalsh(matrix)[1])
            error = abs(actual-gamma)/max(1.0, gamma)
            worst_equality = max(worst_equality, error)
            assert error < 2e-10, (n, beta, actual, gamma)
            for ell in range(2, n//2+1):
                sector = float(radial_eigen(n, beta, ell)[0])
                bound = gamma+(ell-2)*(ell+1)/n
                assert sector+1e-9*max(1, sector) >= bound
            cases += 1
    sharp_cases = 0
    degree_one_quotient_points = 0
    maximum_degree_one_quotient_error = 0.0
    asymptotic_rows = []
    for n in (2, 3, 5, 10, 30, 100, 300, 1000):
        for beta in dict.fromkeys((1e-12, 1/n**2, 1/n, .01, 1.0, 100.0)):
            gamma = float(radial_eigen(n, beta)[0])
            a = (beta*n+1+sqrt((beta*n+1)**2+4*beta*n*(n+1)))/2
            c = 2*a/n-beta
            lo = c-6*(a-1)/(n*(a+3))
            hi = c-6*a*(a-1)/(n*(n+a-2)*(n+a+1))
            tol = 2e-9*max(1.0, gamma)
            assert lo <= gamma+tol and gamma <= hi+tol, (n, beta, lo, gamma, hi)
            d = sqrt(beta*beta+4*beta)
            assert d-5/n <= gamma+tol and gamma <= d+4/n+tol
            eta = float(radial_eigen(n, beta, 1)[0])
            c1 = (beta+d)/2
            a1 = n*c1
            eta_lo = c1-2*a1/(n*(a1+2))
            eta_hi = c1-2*a1*a1/(n*(n+a1-2)*(n+a1))
            assert eta_lo <= eta+tol and eta <= eta_hi+tol
            assert c1-2/n <= eta+tol and eta <= c1+tol
            birth, death, killing = radial_data(n, beta, 1)
            k = np.arange(1, n, dtype=float)
            quotient = (killing + birth/(k+a1+1)
                        - death/(k+a1-1))
            predicted = c1-2*a1*a1/(n*(k+a1-1)*(k+a1+1))
            quotient_error = float(np.max(np.abs(quotient-predicted))
                                   / max(1.0, c1))
            assert quotient_error < 2e-10, (n, beta, quotient_error)
            maximum_degree_one_quotient_error = max(
                maximum_degree_one_quotient_error, quotient_error)
            degree_one_quotient_points += len(k)
            u = beta+min(n*beta, sqrt(beta))
            assert eta >= u/8-tol and eta <= u+tol
            assert eta <= gamma-2/n+tol
            sharp_cases += 1
            if beta == 1/n:
                asymptotic_rows.append({"n": n, "beta": beta, "gamma": gamma,
                                        "sqrt_n_times_gamma": sqrt(n)*gamma})
    return {"polymer_count_equality_cases": cases,
            "maximum_scaled_equality_error": worst_equality,
            "sharp_and_degree_one_bound_cases": sharp_cases,
            "sharp_degree_one_quotient_points": degree_one_quotient_points,
            "maximum_scaled_degree_one_quotient_error":
                maximum_degree_one_quotient_error,
            "inverse_mass_asymptotics": asymptotic_rows}


def graph_laplacian(n, edges):
    matrix = np.zeros((n, n))
    for x, y, c in edges:
        matrix[x, x] += c
        matrix[y, y] += c
        matrix[x, y] -= c
        matrix[y, x] -= c
    return matrix


def spatial_checks():
    records = []
    for n in range(2, 8):
        graphs = {
            "weighted_path": [(i, i+1, 1+(i%3)/3) for i in range(n-1)],
            "complete": [(i, j, 1/n) for i in range(n) for j in range(i+1, n)],
        }
        if n >= 3:
            graphs["cycle"] = [(i, (i+1)%n, 1.0) for i in range(n)]
        for name, edges in graphs.items():
            lambda_g = float(np.linalg.eigvalsh(graph_laplacian(n, edges))[1])
            for beta, diffusion in ((1e-7, 0.0), (1/n**2, .02),
                                    (1/n, .5), (1.0, 10.0)):
                def rates(mask):
                    result = defaultdict(float, edge_rates(mask, n, beta))
                    for x, y, conductance in edges:
                        if bool(mask & (1 << x)) != bool(mask & (1 << y)):
                            result[mask ^ (1 << x) ^ (1 << y)] += diffusion*conductance
                    return dict(result)
                matrix = reversible_matrix(list(range(1, 1 << n)), rates)
                actual = float(np.linalg.eigvalsh(matrix)[1])
                gamma = float(radial_eigen(n, beta)[0])
                eta = float(radial_eigen(n, beta, 1)[0])
                predicted = min(gamma, eta+diffusion*lambda_g)
                error = abs(actual-predicted)/max(1.0, actual, predicted)
                assert error < 2e-10, (n, name, beta, diffusion, actual, predicted)
                records.append({"n": n, "graph": name, "beta": beta,
                                "D": diffusion, "actual": actual,
                                "predicted": predicted, "scaled_error": error})
    return {"cases": len(records),
            "largest_matrix": 127,
            "maximum_scaled_error": max(r["scaled_error"] for r in records),
            "records": records}


def critical_jacobi(b, cutoff, degree_one=False):
    """Reflect at the last state; retain the original killing potential.

    Count states are 1,...,R, while degree-one states are 0,...,R.
    The analytic errors to the infinite eigenvalues are, respectively,
    2b/(R+3) and b/(R+2), from the proved ground-state ratio bounds.
    Floating finite eigenvalues are not interval-certified by this routine.
    """
    if degree_one:
        j = np.arange(cutoff+1, dtype=float)
        diagonal = j*(j+1)+b
        off = -sqrt(b)*np.arange(1, cutoff+1, dtype=float)
        truncation = b/(cutoff+2)
    else:
        k = np.arange(1, cutoff+1, dtype=float)
        diagonal = k*(k+1)+b
        off = -np.sqrt(b*k[:-1]*(k[:-1]+1))
        truncation = 2*b/(cutoff+3)
    diagonal[-1] -= b
    eigenvalue = float(eigh_tridiagonal(
        diagonal, off, select="i", select_range=(0, 0),
        eigvals_only=True)[0])
    return eigenvalue, truncation


def critical_checks():
    records = []
    truncation_records = []
    cutoff = 512
    maximum_inequality_excess = 0.0
    for b in (.01, .25, 1.0, 4.0, 25.0):
        rho, rho_error = critical_jacobi(b, cutoff)
        sigma, sigma_error = critical_jacobi(b, cutoff, degree_one=True)
        # Account separately for ordinary floating error and analytic tails.
        numeric_allowance = 2e-9*max(1.0, b)
        for smaller in (1, 16, 64):
            rho_small, rho_small_error = critical_jacobi(b, smaller)
            sigma_small, sigma_small_error = critical_jacobi(
                b, smaller, degree_one=True)
            for name, small, small_error, large, large_error in (
                ("rho", rho_small, rho_small_error, rho, rho_error),
                ("sigma", sigma_small, sigma_small_error, sigma, sigma_error),
            ):
                # Each interval must meet the other analytically justified
                # approximation interval; no exact infinite value is assumed.
                excess = max(small-large-large_error,
                             large-small-small_error, 0.0)
                assert excess <= numeric_allowance
                truncation_records.append({
                    "function": name, "b": b, "smaller_cutoff": smaller,
                    "larger_cutoff": cutoff,
                    "smaller_finite_eigenvalue": small,
                    "smaller_analytic_tail_bound": small_error,
                    "larger_finite_eigenvalue": large,
                    "larger_analytic_tail_bound": large_error,
                    "numeric_allowance": numeric_allowance,
                })
        for n in (2, 3, 10, 50, 200):
            beta = b/n**2
            count_value = n*float(radial_eigen(n, beta)[0])
            degree_one_value = n*float(radial_eigen(n, beta, 1)[0])
            error_bound = b/n
            # rho in [rho_R,rho_R+tail] and |n gamma-rho| <= b/n.
            rho_delta = count_value-rho
            rho_excess = max(-error_bound-rho_delta,
                             rho_delta-error_bound-rho_error, 0.0)
            # sigma in [sigma_R,sigma_R+tail] and
            # 0 <= n eta-sigma <= b/n.
            sigma_delta = degree_one_value-sigma
            sigma_excess = max(-sigma_delta,
                               sigma_delta-error_bound-sigma_error, 0.0)
            maximum_inequality_excess = max(
                maximum_inequality_excess, rho_excess, sigma_excess)
            assert max(rho_excess, sigma_excess) <= numeric_allowance, (
                n, b, rho_excess, sigma_excess)
            records.append({
                "n": n, "b": b, "beta": beta, "cutoff": cutoff,
                "n_gamma": count_value, "rho_finite": rho,
                "rho_analytic_tail_bound": rho_error,
                "n_eta1": degree_one_value, "sigma_finite": sigma,
                "sigma_analytic_tail_bound": sigma_error,
                "finite_size_error_bound": error_bound,
                "numeric_allowance": numeric_allowance,
                "count_difference_interval_before_floating_allowance":
                    [rho_delta-rho_error, rho_delta],
                "degree_one_difference_interval_before_floating_allowance":
                    [sigma_delta-sigma_error, sigma_delta],
            })
    return {
        "finite_size_parameter_cases": len(records),
        "finite_size_inequality_checks": 2*len(records),
        "truncation_consistency_checks": len(truncation_records),
        "largest_jacobi_dimension": cutoff+1,
        "maximum_inequality_excess_before_numeric_allowance":
            maximum_inequality_excess,
        "interpretation": (
            "Floating finite eigenvalues are compared with the formulas "
            "after explicitly allowing the proved infinite-state truncation "
            "errors. These are not interval-certified floating eigenvalues."
        ),
        "records": records, "truncation_records": truncation_records,
    }


def generator_matrix(states, outgoing):
    index = {state: i for i, state in enumerate(states)}
    matrix = np.zeros((len(states), len(states)))
    for state in states:
        i = index[state]
        for target, rate in outgoing[state].items():
            assert target != state
            matrix[i, index[target]] += float(rate)
        matrix[i, i] = -sum(map(float, outgoing[state].values()))
    return matrix


def weighted_negative_generator(generator, weights):
    roots = np.sqrt(np.asarray(weights, dtype=float))
    return -roots[:, None]*generator/roots[None, :]


def nonzero_real_gap(matrix):
    values = np.linalg.eigvals(matrix)
    zero = int(np.argmin(np.abs(values)))
    assert abs(values[zero]) <= 2e-9*max(1.0, np.linalg.norm(matrix, ord=2))
    return float(np.min(np.delete(values, zero).real))


def local_permutation(n, cycle):
    permutation = list(range(n))
    for source, target in zip(cycle, cycle[1:]+cycle[:1]):
        permutation[source] = target
    return tuple(permutation)


def strict_permutations(n):
    assert n in (3, 6)
    width = n//3
    permutations = []
    for w in range(width):
        sites = [i*width+w for i in range(3)]
        for cycle, rate in ((sites[:2], .5), (sites[1:], .5), (sites, 1.0)):
            permutations.append((local_permutation(n, cycle), rate))
    if width == 2:
        # G on two vertices has edge rate 3/2 and gap 3 >= 5/2.
        for i in range(3):
            permutations.append((
                local_permutation(n, [i*width, i*width+1]), 1.5))
    return permutations


def permutation_matrix_on_points(n, permutations):
    matrix = np.zeros((n, n))
    for permutation, rate in permutations:
        for x, y in enumerate(permutation):
            if x != y:
                matrix[x, y] += rate
                matrix[x, x] -= rate
    return matrix


def permute_mask(mask, permutation):
    return sum(1 << permutation[i] for i in range(len(permutation))
               if mask & (1 << i))


def nonreversible_permutation_checks():
    records = []
    point_records = []
    h3 = np.array([[-1.5, 1.5, 0.0],
                   [.5, -2.0, 1.5],
                   [1.0, .5, -1.5]])
    maximum_error = maximum_stationary_residual = 0.0
    for n in (3, 6):
        permutations = strict_permutations(n)
        h = permutation_matrix_on_points(n, permutations)
        predicted_h = h3 if n == 3 else (
            np.kron(h3, np.eye(2))
            + np.kron(np.eye(3), np.array([[-1.5, 1.5], [1.5, -1.5]])))
        assert np.array_equal(h, predicted_h)
        assert np.max(np.abs(h.sum(axis=0))) == 0
        assert np.max(np.abs(h.sum(axis=1))) == 0
        kappa = nonzero_real_gap(-h)
        kappa_s = float(np.linalg.eigvalsh(-(h+h.T)/2)[1])
        assert abs(kappa-2.5) < 1e-12 and abs(kappa_s-2.0) < 1e-12
        if n == 3:
            assert np.max(np.abs(np.poly(-h)-[1, -5, 27/4, 0])) < 1e-12
        point_records.append({
            "n": n, "generator": h.tolist(),
            "asymptotic_gap": kappa, "symmetric_gap": kappa_s,
        })
        states = list(range(1, 1 << n))
        for beta in (1/n**2, 1/n, 1.0):
            gamma = float(radial_eigen(n, beta)[0])
            eta = float(radial_eigen(n, beta, 1)[0])
            threshold = (gamma-eta)/2.5
            raw_weights = np.array([
                (beta*n)**mask.bit_count()/factorial(mask.bit_count()-1)
                for mask in states])
            weights = raw_weights/raw_weights.sum()
            for fraction in (0.0, .3, 1.2, 10.0):
                diffusion = fraction*threshold
                outgoing = {}
                for mask in states:
                    rates = defaultdict(float, edge_rates(mask, n, beta))
                    for permutation, rate in permutations:
                        target = permute_mask(mask, permutation)
                        if target != mask:
                            rates[target] += diffusion*rate
                    outgoing[mask] = dict(rates)
                generator = generator_matrix(states, outgoing)
                stationary_residual = float(np.max(np.abs(weights@generator)))
                maximum_stationary_residual = max(
                    maximum_stationary_residual, stationary_residual)
                assert stationary_residual < 1e-11
                matrix = weighted_negative_generator(generator, weights)
                actual = nonzero_real_gap(matrix)
                actual_s = float(np.linalg.eigvalsh((matrix+matrix.T)/2)[1])
                predicted = min(gamma, eta+2.5*diffusion)
                predicted_s = min(gamma, eta+2*diffusion)
                error = max(abs(actual-predicted), abs(actual_s-predicted_s))
                error /= max(1.0, actual, predicted)
                maximum_error = max(maximum_error, error)
                assert error < 2e-10, (n, beta, fraction, actual, predicted)
                if fraction == .3:
                    assert actual-actual_s > .1*diffusion
                records.append({
                    "n": n, "beta": beta, "D": diffusion,
                    "actual_asymptotic_gap": actual,
                    "predicted_asymptotic_gap": predicted,
                    "actual_symmetric_gap": actual_s,
                    "predicted_symmetric_gap": predicted_s,
                    "scaled_error": error,
                })
    return {
        "point_generator_cases": len(point_records),
        "full_cut_generator_cases": len(records),
        "largest_full_matrix": 63,
        "maximum_scaled_gap_error": maximum_error,
        "maximum_stationary_residual": maximum_stationary_residual,
        "point_records": point_records, "records": records,
    }


def polymer_weights(states, n, beta):
    raw = {(m): (beta*n)**sum(m)/prod(factorial(count) for count in m)
           for m in states}
    total = sum(raw.values())
    return {m: weight/total for m, weight in raw.items()}


def multiplicity_state(n, parts):
    return tuple(parts.count(size) for size in range(1, n+1))


def circulation_checks():
    records = []
    exact_flux_identities = exact_stationarity_identities = 0
    maximum_symmetric_error = 0.0
    for n in range(4, 9):
        states = polymer_states(n)
        cycle = [
            multiplicity_state(n, [2]+[1]*(n-2)),
            multiplicity_state(n, [2, 2]+[1]*(n-4)),
            multiplicity_state(n, [4]+[1]*(n-4)),
            multiplicity_state(n, [3]+[1]*(n-3)),
        ]
        assert len(set(cycle)) == 4
        for beta in (Fraction(1, n), Fraction(1)):
            weights = polymer_weights(states, n, beta)
            original = {m: polymer_rates(m, n, beta) for m in states}
            generator = generator_matrix(states, original)
            weight_array = [float(weights[m]) for m in states]
            baseline = weighted_negative_generator(generator, weight_array)
            gamma = float(np.linalg.eigvalsh(baseline)[1])
            conductance_min = min(
                weights[x]*original[x][y]
                for x, y in zip(cycle, cycle[1:]+cycle[:1]))
            for sign in (-1, 1):
                epsilon = sign*conductance_min/2
                modified = {m: dict(rates) for m, rates in original.items()}
                for x, y in zip(cycle, cycle[1:]+cycle[:1]):
                    modified[x][y] += epsilon/weights[x]
                    modified[y][x] -= epsilon/weights[y]
                for x in states:
                    assert min(modified[x].values()) > 0
                    assert sum(modified[x].values()) == sum(original[x].values())
                    incoming = sum(
                        weights[y]*modified[y].get(x, Fraction(0)) for y in states)
                    assert incoming == weights[x]*sum(modified[x].values())
                    exact_stationarity_identities += 1
                    for y in modified[x]:
                        assert (weights[x]*modified[x][y]
                                + weights[y]*modified[y][x]
                                == 2*weights[x]*original[x][y])
                        exact_flux_identities += 1
                perturbed_generator = generator_matrix(states, modified)
                perturbed = weighted_negative_generator(
                    perturbed_generator, weight_array)
                symmetric_error = float(np.max(np.abs(
                    (perturbed+perturbed.T)/2-baseline)))
                maximum_symmetric_error = max(
                    maximum_symmetric_error, symmetric_error)
                assert symmetric_error < 2e-12
                accelerated = nonzero_real_gap(perturbed)
                gain = accelerated-gamma
                assert gain > 1e-10, (n, str(beta), sign, gamma, accelerated)
                records.append({
                    "n": n, "beta": float(beta),
                    "cycle_current": float(epsilon),
                    "fraction_of_minimum_conductance": sign*.5,
                    "baseline_gap": gamma, "asymptotic_gap": accelerated,
                    "strict_gap_gain": gain,
                    "symmetric_part_maximum_entry_error": symmetric_error,
                })
    return {
        "generator_cases": len(records), "n_range": [4, 8],
        "largest_matrix": len(polymer_states(8)),
        "exact_stationarity_identities": exact_stationarity_identities,
        "exact_symmetric_flux_identities": exact_flux_identities,
        "maximum_symmetric_part_error": maximum_symmetric_error,
        "smallest_observed_strict_gain":
            min(row["strict_gap_gain"] for row in records),
        "records": records,
    }


def shared_kernel_rates(m, n, beta, multiplier):
    """Enumerate every polymer instance, link, and unordered instance pair."""
    rates = defaultdict(Fraction)
    instances = [size for size, count in enumerate(m, 1) for _ in range(count)]
    for size in instances:
        for left in range(1, size):
            right = size-left
            target = list(m)
            target[size-1] -= 1
            target[left-1] += 1
            target[right-1] += 1
            rates[tuple(target)] += beta*multiplier(left, right)
    for left, right in combinations(instances, 2):
        target = list(m)
        target[left-1] -= 1
        target[right-1] -= 1
        target[left+right-1] += 1
        rates[tuple(target)] += Fraction(2, n)*multiplier(left, right)
    return dict(rates)


def growing_kernel_checks():
    records = []
    drift_identities = detailed_balance_identities = covariance_cases = 0
    maximum_inequality_excess = 0.0
    for n in range(2, 10):
        states = polymer_states(n)
        for beta in (Fraction(1, n*n), Fraction(1, n), Fraction(1)):
            weights = polymer_weights(states, n, beta)
            gamma = float(radial_eigen(n, float(beta))[0])
            mean_x = sum(weights[m]*m[0] for m in states)
            mean_k = sum(weights[m]*sum(m) for m in states)
            variance = sum(weights[m]*(m[0]-mean_x)**2 for m in states)
            covariance = sum(weights[m]*(m[0]-mean_x)*(sum(m)-mean_k)
                             for m in states)
            assert variance > 0 and covariance <= variance
            covariance_cases += 1
            for name, multiplier, scale in (
                ("product", lambda i, j: i*j, 1),
                ("additive", lambda i, j: i+j, 2),
            ):
                outgoing = {
                    m: shared_kernel_rates(m, n, beta, multiplier) for m in states}
                for m in states:
                    x, k = m[0], sum(m)
                    drift = sum(rate*(target[0]-x)
                                for target, rate in outgoing[m].items())
                    expected = (
                        2*beta*(n-k)-Fraction(2*(n-1)*x, n)
                        if name == "product"
                        else 2*beta*(n-x)-Fraction(2*x*(n+k-2), n))
                    assert drift == expected, (n, str(beta), name, m)
                    drift_identities += 1
                    for target, rate in outgoing[m].items():
                        assert (weights[m]*rate
                                == weights[target]*outgoing[target][m])
                        detailed_balance_identities += 1
                matrix = reversible_matrix(states, lambda m: outgoing[m])
                actual = float(np.linalg.eigvalsh(matrix)[1])
                lower = scale*gamma
                upper = scale*(2*float(beta)+2*(n-1)/n)
                excess = max(lower-actual, actual-upper, 0.0)
                maximum_inequality_excess = max(maximum_inequality_excess, excess)
                assert excess < 2e-10*max(1.0, actual, upper)
                record = {
                    "n": n, "beta": float(beta), "kernel": name,
                    "gap": actual, "comparison_lower_bound": lower,
                    "proved_upper_bound": upper,
                    "monomer_count_covariance_over_variance":
                        float(covariance/variance),
                }
                if name == "product":
                    rayleigh = float(
                        Fraction(2*(n-1), n)+2*beta*covariance/variance)
                    assert actual <= rayleigh+2e-10*max(1.0, rayleigh)
                    record["monomer_rayleigh_quotient"] = rayleigh
                records.append(record)
    return {
        "generator_cases": len(records), "n_range": [2, 9],
        "largest_matrix": len(polymer_states(9)),
        "exact_monomer_drift_identities": drift_identities,
        "exact_detailed_balance_identities": detailed_balance_identities,
        "exact_monomer_covariance_cases": covariance_cases,
        "maximum_inequality_excess": maximum_inequality_excess,
        "records": records,
    }


def main():
    report = {
        "created_utc": datetime.now(timezone.utc).isoformat(),
        "status": "passed",
        "software": {"Python": platform.python_version(), "NumPy": np.__version__, "SciPy": scipy.__version__},
        "scope": "Finite reproducibility checks; analytic proofs are in the manuscript.",
        "exact_algebra": exact_identities(),
        "reaction_spectra": spectral_checks(),
        "spatial_spectra": spatial_checks(),
        "critical_scaling": critical_checks(),
        "nonreversible_permutations": nonreversible_permutation_checks(),
        "polymer_circulations": circulation_checks(),
        "growing_kernels": growing_kernel_checks(),
    }
    dest = Path(__file__).resolve().parent.parent/"results"/"extension_checks.json"
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(json.dumps(report, indent=2)+"\n")
    summary = {}
    for key, value in report.items():
        summary[key] = ({name: item for name, item in value.items()
                         if not name.endswith("records")}
                        if isinstance(value, dict) else value)
    print(json.dumps(summary, indent=2))
    print(str(dest))


if __name__ == "__main__":
    main()
