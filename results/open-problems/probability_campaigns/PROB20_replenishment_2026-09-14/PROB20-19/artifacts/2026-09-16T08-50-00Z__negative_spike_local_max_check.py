#!/usr/bin/env python3
"""Reproducible self-checks for the PROB20-19 2026-09-16T08-45-00Z report.

This script is supporting self-review only. The theorem in the report is analytic.
It checks the Hadamard identities symbolically, the singular curvature formula,
and deterministic Monte Carlo sanity tests near the balanced negative-spike point.
"""

import math
import numpy as np
import sympy as sp


def symbolic_checks():
    x1, x2, x3, x4 = sp.symbols("x1 x2 x3 x4", real=True)
    D = (x1 + x2 + x3 + x4) / 2
    A = (x1 + x2 - x3 - x4) / 2
    B = (x1 - x2 + x3 - x4) / 2
    C = (x1 - x2 - x3 + x4) / 2
    T = x1**2 + x2**2 + x3**2 + x4**2

    identities = [
        sp.expand(x1**2 + x2**2 - (T/2 + D*A + B*C)),
        sp.expand(x3**2 + x4**2 - (T/2 - D*A - B*C)),
        sp.expand(x1**2 + x3**2 - (T/2 + D*B + A*C)),
        sp.expand(x2**2 + x4**2 - (T/2 - D*B - A*C)),
        sp.expand(x1**2 + x4**2 - (T/2 + D*C + A*B)),
        sp.expand(x2**2 + x3**2 - (T/2 - D*C - A*B)),
    ]
    assert all(v == 0 for v in identities)

    th, X, Y, Z = sp.symbols("th X Y Z", real=True)
    q1 = X*Z - Y**2 * sp.sin(th) * sp.cos(th)
    q2 = Y * (Z*sp.cos(th) - X*sp.sin(th))
    q3 = Y * (X*sp.cos(th) - Z*sp.sin(th))
    assert sp.simplify(sp.diff(q1, th, 2).subs(th, 0)) == 0
    assert sp.simplify(sp.diff(q2, th, 2).subs(th, 0) + Y*Z) == 0
    assert sp.simplify(sp.diff(q3, th, 2).subs(th, 0) + Y*X) == 0

    exact_EM = 2 * sp.sqrt(3) / sp.pi
    exact_curvature = -sp.Rational(2, 3) * exact_EM
    gamma0 = sp.Rational(1, 2) - 2 * (sp.sqrt(3) - 1) / sp.pi

    print("symbolic_hadamard_identities=PASS")
    print("symbolic_branch_second_derivatives=PASS")
    print("E_M_exact=", sp.simplify(exact_EM), "~=", float(exact_EM.evalf(16)))
    print("singular_curvature_exact=", sp.simplify(exact_curvature), "~=", float(exact_curvature.evalf(16)))
    print("analytic_KL_gap_lower_bound_gamma0=", gamma0, "~=", float(gamma0.evalf(16)))
    assert float(gamma0.evalf()) > 0


def top2_values(X):
    sq = X * X
    return np.partition(sq, 2, axis=1)[:, 2:].sum(axis=1)


def samples_for_u(Z, u, lam):
    # C_{lam,u}^{1/2}=P_u+sqrt(lam) uu^T = I-(1-sqrt(lam)) uu^T
    coeff = 1.0 - math.sqrt(lam)
    g = Z @ u
    return Z - coeff * g[:, None] * u[None, :]


def monte_carlo_checks(seed=20260916, n=900_000):
    rng = np.random.default_rng(seed)
    Z = rng.standard_normal((n, 4))
    u0 = np.ones(4) / 2.0
    h = np.array([1.0, 1.0, -1.0, -1.0]) / 2.0
    e1 = np.array([1.0, 0.0, 0.0, 0.0])

    # Singular value check against exact balanced formula.
    v0 = top2_values(samples_for_u(Z, u0, 0.0))
    exact_balanced = 1.5 + 2.0 * math.sqrt(3.0) / math.pi
    print("balanced_singular_mc=", v0.mean())
    print("balanced_singular_exact=", exact_balanced)
    print("balanced_singular_abs_error=", abs(v0.mean() - exact_balanced))

    # Finite-difference curvature along the analytically used tangent.
    eps = 0.025
    vals = []
    for th in (-eps, 0.0, eps):
        u = u0 * math.cos(th) + h * math.sin(th)
        vals.append(top2_values(samples_for_u(Z, u, 0.0)))
    fd_sample = (vals[0] - 2.0 * vals[1] + vals[2]) / (eps * eps)
    fd_mean = float(fd_sample.mean())
    fd_se = float(fd_sample.std(ddof=1) / math.sqrt(n))
    exact_curv = -4.0 * math.sqrt(3.0) / (3.0 * math.pi)
    print("singular_curvature_fd=", fd_mean, "+/-", fd_se)
    print("singular_curvature_exact=", exact_curv)

    # KL-vs-balanced sanity at lambda=0 and small positive lambdas.
    for lam in (0.0, 1e-4, 1e-3, 1e-2):
        kl = top2_values(samples_for_u(Z, e1, lam))
        bal = top2_values(samples_for_u(Z, u0, lam))
        diff = kl - bal
        print(
            f"lambda={lam:g} KL={kl.mean():.9f} balanced={bal.mean():.9f} "
            f"KL_minus_balanced={diff.mean():.9f} se={diff.std(ddof=1)/math.sqrt(n):.9f}"
        )

    # Local perturbation sanity at small positive lambda. This is not used in the theorem.
    for lam in (1e-4, 1e-3, 1e-2):
        base = top2_values(samples_for_u(Z, u0, lam))
        for th in (0.03, 0.06):
            u = u0 * math.cos(th) + h * math.sin(th)
            v = top2_values(samples_for_u(Z, u, lam))
            diff = v - base
            print(
                f"local lambda={lam:g} theta={th:.3f} delta={diff.mean():.9e} "
                f"se={diff.std(ddof=1)/math.sqrt(n):.9e}"
            )


if __name__ == "__main__":
    symbolic_checks()
    monte_carlo_checks()
