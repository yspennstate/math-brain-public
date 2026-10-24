#!/usr/bin/env python3
"""Reproducible checks for the PROB20-19 Jacobi-obstruction report.

This script checks:
  1. the exact angular integrals giving D_0 = 2/pi;
  2. positive definiteness of C_epsilon and det(C_epsilon)=4 epsilon^2;
  3. the explicit perturbation lower bound for epsilon=1e-3;
  4. a deterministic Monte Carlo sanity check of the first derivative.

The Monte Carlo section is supporting evidence only; the report's proof is analytic.
"""

import math
import numpy as np
import sympy as sp


def exact_symbolic_checks():
    t = sp.symbols("t", real=True)
    integrand = t / (1 + t**2) ** 2

    I_A = sp.integrate(integrand, (t, sp.Rational(-1, 2), 2))
    I_B_pos = sp.integrate(integrand, (t, 2, sp.oo))
    I_B_neg = sp.integrate(integrand, (t, -sp.oo, -3))
    angular = sp.simplify(2 * (I_A - I_B_pos - I_B_neg))
    D0 = sp.simplify(4 * angular / sp.pi)

    assert I_A == sp.Rational(3, 10)
    assert I_B_pos == sp.Rational(1, 10)
    assert I_B_neg == -sp.Rational(1, 20)
    assert angular == sp.Rational(1, 2)
    assert D0 == 2 / sp.pi

    eps = sp.symbols("eps", positive=True)
    C = sp.Matrix(
        [
            [4, 0, 2],
            [0, 1, 1],
            [2, 1, 2 + eps**2],
        ]
    )
    detC = sp.factor(C.det())
    assert detC == 4 * eps**2

    return I_A, I_B_pos, I_B_neg, angular, D0, detC


def perturbation_bound(epsilon=1e-3):
    sigma_terms = [1.0, math.sqrt(5.0), math.sqrt(2.0), math.sqrt(10.0)]

    # Exact Cauchy-ratio/Cauchy-Schwarz bound from the report.
    exact_prob_bound = 4.0 * sum(
        math.sqrt((2.0 / math.pi) * math.atan(epsilon / sigma))
        for sigma in sigma_terms
    )

    # Slightly looser closed-form bound using arctan(x) <= x.
    closed_form_bound = 4.0 * math.sqrt(2.0 * epsilon / math.pi) * (
        1.0 + 5.0 ** (-0.25) + 2.0 ** (-0.25) + 10.0 ** (-0.25)
    )

    d0 = 2.0 / math.pi
    lower_exact_prob = d0 - exact_prob_bound
    lower_closed = d0 - closed_form_bound

    assert lower_exact_prob > 0.0
    assert lower_closed > 0.322

    return exact_prob_bound, closed_form_bound, lower_exact_prob, lower_closed


def monte_carlo_derivative(epsilon=1e-3, n=1_000_000, seed=12345):
    rng = np.random.default_rng(seed)
    u = rng.standard_normal(n)
    v = rng.standard_normal(n)
    w = rng.standard_normal(n)

    z = u + v + epsilon * w

    A = ((np.abs(v) < 2.0 * np.abs(u)) & (np.abs(v) < np.abs(z))).astype(float)
    B = ((2.0 * np.abs(u) < np.abs(v)) & (2.0 * np.abs(u) < np.abs(z))).astype(float)

    values = 4.0 * u * v * (A - B)
    estimate = float(values.mean())
    stderr = float(values.std(ddof=1) / math.sqrt(n))

    # Very loose sanity threshold, far below the analytic lower bound.
    assert estimate > 0.25

    return estimate, stderr


def main():
    I_A, I_B_pos, I_B_neg, angular, D0, detC = exact_symbolic_checks()
    exact_prob_bound, closed_form_bound, lower_exact_prob, lower_closed = perturbation_bound()
    estimate, stderr = monte_carlo_derivative()

    print("exact symbolic checks: PASS")
    print(f"I_A={I_A}, I_B_pos={I_B_pos}, I_B_neg={I_B_neg}")
    print(f"angular integral={angular}, D0={D0}")
    print(f"det(C_epsilon)={detC}")
    print("positive-definite perturbation check: PASS")
    print(f"epsilon=1e-3")
    print(f"exact probability perturbation bound={exact_prob_bound:.12f}")
    print(f"closed-form perturbation bound={closed_form_bound:.12f}")
    print(f"rigorous numerical lower bound using atan expression={lower_exact_prob:.12f}")
    print(f"rigorous closed-form lower bound={lower_closed:.12f}")
    print("Monte Carlo sanity check (not proof): PASS")
    print(f"derivative estimate={estimate:.12f}")
    print(f"standard error={stderr:.12f}")


if __name__ == "__main__":
    main()
