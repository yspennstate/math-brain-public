#!/usr/bin/env python3
"""Independent numerical and rational checks of one-sided Chebyshev GP bounds.

Run: python research/code/a27_gp_checks.py
Requires numpy and scipy. Writes a27_gp_results.json beside this script.
This is a floating-point diagnostic, not a proof of uniform inequalities.
"""

from __future__ import annotations

import itertools
import json
import math
from fractions import Fraction as Q
from pathlib import Path

import numpy as np
from scipy.special import gammainc


SEED = 271828
RADIUS = 1.0
ELL = 0.75
DTYPE = np.float64


def sym(a: np.ndarray) -> np.ndarray:
    return (a + a.T) / 2


def mineig(a: np.ndarray) -> float:
    return float(np.linalg.eigvalsh(sym(a))[0])


def assert_leq(left: float, right: float, *, atol: float = 2e-9) -> None:
    assert left <= right + atol * max(1.0, abs(left), abs(right)), (left, right)


def as_str(x: Q) -> str:
    return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"


def cheb_parameters(a: float, b: float, degree: int) -> tuple[float, float, float]:
    """Return rho, delta_D=1/T_D(z0), epsilon_D=2 delta/(1+delta)."""
    assert 0 < a <= b and degree >= 1
    if a == b:
        return 0.0, 0.0, 0.0
    rho = (math.sqrt(b / a) - 1) / (math.sqrt(b / a) + 1)
    power = rho**degree
    delta = 2 * power / (1 + power * power)
    epsilon = 2 * delta / (1 + delta)
    assert_leq(abs(epsilon - 4 * power / (1 + power) ** 2), 0, atol=1e-14)
    return rho, delta, epsilon


def residual(lam: np.ndarray, a: float, b: float, degree: int) -> np.ndarray:
    """Shifted one-sided residual (T_D(z)+1)/(T_D(z0)+1)."""
    lam = np.asarray(lam, dtype=DTYPE)
    if a == b:
        return np.zeros_like(lam)
    _, delta, _ = cheb_parameters(a, b, degree)
    z = np.clip((a + b - 2 * lam) / (b - a), -1.0, 1.0)
    t = np.cos(degree * np.arccos(z))
    return delta * (t + 1) / (1 + delta)


def direct_matrix_polynomial(
    a_mat: np.ndarray, rhs: np.ndarray, a: float, b: float, degree: int
) -> np.ndarray:
    """Spectral evaluation of the actual degree-(D-1) polynomial P_D(A).

    This path does not use the solver recurrence or a numerical inverse.
    It avoids unstable monomial coefficients for the ill-conditioned cases.
    """
    if a == b:
        return rhs / a
    eig, vec = np.linalg.eigh(sym(a_mat))
    assert mineig(a_mat) >= a - 1e-9 * max(1, b)
    assert eig[-1] <= b + 1e-9 * max(1, b)
    scale = (1 - residual(eig, a, b, degree)) / eig
    return vec @ (scale[:, None] * (vec.T @ rhs))


def cheb_recurrence(
    a_mat: np.ndarray, rhs: np.ndarray, a: float, b: float, degree: int
) -> np.ndarray:
    """Ordinary Chebyshev semi-iteration, finally divided by 1+delta_D."""
    if a == b:
        return rhs / a
    h, d = (a + b) / 2, (b - a) / 2
    z0 = h / d
    x_prev = np.zeros_like(rhs)
    x = rhs / h
    w = 1 / z0
    for _j in range(1, degree):
        w_next = 1 / (2 * z0 - w)
        beta = w * w_next
        alpha = 2 * w_next / d
        x_next = x + beta * (x - x_prev) + alpha * (rhs - a_mat @ x)
        x_prev, x, w = x, x_next, w_next
    delta = cheb_parameters(a, b, degree)[1]
    return x / (1 + delta)


def feature_map(x: np.ndarray, degree: int, ell: float) -> np.ndarray:
    """Full multi-index coordinates through total degree, in graded order."""
    dim = x.shape[1]
    indices = sorted(
        (alpha for alpha in itertools.product(range(degree + 1), repeat=dim)
         if sum(alpha) <= degree),
        key=lambda alpha: (sum(alpha), alpha),
    )
    factor = np.exp(-np.sum(x * x, axis=1) / (2 * ell * ell))
    columns = []
    for alpha in indices:
        col = factor.copy()
        for j, power in enumerate(alpha):
            col *= (x[:, j] / ell) ** power / math.sqrt(math.factorial(power))
        columns.append(col)
    return np.column_stack(columns)


def exact_rbf(x: np.ndarray, ell: float) -> np.ndarray:
    sq = np.sum((x[:, None, :] - x[None, :, :]) ** 2, axis=2)
    return np.exp(-sq / (2 * ell * ell))


def kl_forward(mu: np.ndarray, cov: np.ndarray,
               mu_hat: np.ndarray, cov_hat: np.ndarray) -> float:
    m = len(mu)
    sign1, logdet1 = np.linalg.slogdet(cov)
    sign2, logdet2 = np.linalg.slogdet(cov_hat)
    assert sign1 > 0 and sign2 > 0
    displacement = mu_hat - mu
    value = (np.trace(np.linalg.solve(cov_hat, cov)) - m
             + logdet2 - logdet1
             + displacement @ np.linalg.solve(cov_hat, displacement)) / 2
    assert value >= -3e-9
    return float(max(0.0, value))


def moments(gram: np.ndarray, y: np.ndarray, n: int, s: float,
            poly: np.ndarray | None = None) -> tuple[np.ndarray, np.ndarray]:
    g = gram[:n, :n]
    h = gram[:n, n:]
    j = gram[n:, n:]
    a_mat = g + s * np.eye(n)
    solved = (np.linalg.solve(a_mat, np.column_stack((y, h)))
              if poly is None else poly)
    mu = h.T @ solved[:, 0]
    cov = sym(j + s * np.eye(j.shape[0]) - h.T @ solved[:, 1:])
    return mu, cov


def check_grid_residual() -> dict:
    rows = []
    for a, b in [(1., 3.), (.001, 8.001), (1e-5, 12.00001)]:
        for degree in [1, 2, 3, 4, 5, 10, 20, 40]:
            xs = np.linspace(a, b, 10001)
            rr = residual(xs, a, b, degree)
            rho, delta, eps = cheb_parameters(a, b, degree)
            assert mineig(np.diag([float(rr.min()), float(eps - rr.max())])) >= -1e-10
            assert abs(rr[0] - eps) < 1e-12
            if degree % 2 == 0:
                half = degree // 2
                z = (a + b - 2 * xs) / (b - a)
                q = (2 * rho**half / (1 + rho ** (2 * half))) * np.cos(
                    half * np.arccos(np.clip(z, -1, 1)))
                assert np.max(np.abs(rr - q*q)) < 2e-12
            rows.append({"a": a, "b": b, "D": degree,
                         "rho": rho, "delta": delta, "epsilon": eps,
                         "sample_min": float(rr.min()),
                         "sample_max": float(rr.max())})
    # Singleton spectrum does not require an affine Chebyshev mapping.
    mat = np.eye(2) * 1.25
    rhs = np.array([[1., -3.], [2., 4.]])
    assert np.array_equal(cheb_recurrence(mat, rhs, 1.25, 1.25, 5), rhs / 1.25)
    assert np.array_equal(direct_matrix_polynomial(mat, rhs, 1.25, 1.25, 5), rhs / 1.25)
    return {"grid_rows": rows, "singleton_exact": True}


def check_fraction_examples() -> dict:
    # Rational 2x2 SPD matrix A=[[2,1],[1,2]], eigenvalues 1 and 3.
    # The D=2 one-sided polynomial is P_1(A)=I-A/4.
    amat = ((Q(2), Q(1)), (Q(1), Q(2)))
    pmat = ((Q(1, 2), Q(-1, 4)), (Q(-1, 4), Q(1, 2)))
    ainverse = ((Q(2, 3), Q(-1, 3)), (Q(-1, 3), Q(2, 3)))
    diff = tuple(tuple(ainverse[i][j] - pmat[i][j] for j in range(2))
                 for i in range(2))
    assert diff == ((Q(1, 6), Q(-1, 12)), (Q(-1, 12), Q(1, 6)))
    assert pmat[0][0] > 0 and pmat[0][0]*pmat[1][1]-pmat[0][1]**2 > 0
    assert diff[0][0] > 0 and diff[0][0]*diff[1][1]-diff[0][1]**2 > 0
    assert amat[0][0]*amat[1][1]-amat[0][1]**2 == 3

    # One training point and two identical query points: full 3x3 Gram is
    # all ones, hence PSD. Use deliberately loose [a,b]=[1,3], A=[2].
    s, a, b, y = Q(1), Q(1), Q(3), Q(3)
    p0 = Q(1, 3)  # D=1 shifted polynomial, constant in lambda.
    cinv = Q(1, 2)
    mu = y * cinv
    muhat = y * p0
    c_offdiag = 1 - cinv
    chat_offdiag = 1 - p0
    c_diag = s + c_offdiag
    chat_diag = s + chat_offdiag
    delta_entry = chat_diag - c_diag
    assert (mu, muhat, c_diag, chat_diag, delta_entry) == (
        Q(3, 2), Q(1), Q(3, 2), Q(5, 3), Q(1, 6))
    # C and Chat have eigenvalues (1,2) and (1,7/3), respectively.
    assert c_diag + c_offdiag == 2 and c_diag-c_offdiag == s
    assert chat_diag + chat_offdiag == Q(7, 3)
    assert chat_diag-chat_offdiag == s
    exact_kl_expression = 0.5 * math.log(7/6) + 1/28
    assert abs(kl_forward(np.array([float(mu)]*2),
                          np.array([[float(c_diag), float(c_offdiag)],
                                    [float(c_offdiag), float(c_diag)]]),
                          np.array([float(muhat)]*2),
                          np.array([[float(chat_diag), float(chat_offdiag)],
                                    [float(chat_offdiag), float(chat_diag)]]))
               - exact_kl_expression) < 1e-14
    return {
        "A_2x2": [[as_str(q) for q in row] for row in amat],
        "P_D2_2x2": [[as_str(q) for q in row] for row in pmat],
        "A_inverse_minus_P": [[as_str(q) for q in row] for row in diff],
        "joint_all_ones_gram_size": 3,
        "joint_D1": {"a": as_str(a), "b": as_str(b), "s": as_str(s),
                     "P": as_str(p0), "mu_each": as_str(mu),
                     "muhat_each": as_str(muhat),
                     "C_diagonal": as_str(c_diag), "C_offdiagonal": as_str(c_offdiag),
                     "Chat_diagonal": as_str(chat_diag),
                     "Chat_offdiagonal": as_str(chat_offdiag),
                     "Chat_minus_C_each_entry": as_str(delta_entry),
                     "forward_KL": exact_kl_expression,
                     "forward_KL_formula": "log(7/6)/2 + 1/28"},
    }


def check_ordinary_counterexample() -> dict:
    # K_train+query=[[1,1],[1,1]] PSD (same feature at both locations).
    s = Q(1, 10)
    a, b = s, 1 + s
    h = (a + b) / 2
    inv = 1 / b
    unshifted = 1 / h       # D=1 ordinary Chebyshev iterate X1=B/h.
    shifted = 10 * Q(1, 11) # P_0=(1-q1)/[(1+delta1)lambda].
    assert shifted == inv
    c_true = 1 + s - inv
    c_bad = 1 + s - unshifted
    c_good = 1 + s - shifted
    assert (h, unshifted, shifted, c_true, c_bad) == (
        Q(3, 5), Q(5, 3), Q(10, 11), Q(21, 110), Q(-17, 30))
    assert c_bad < 0 < s < c_good
    return {"full_2x2_gram": [[1, 1], [1, 1]],
            "s": as_str(s), "a": as_str(a), "b": as_str(b),
            "ordinary_D1_inverse_approximation": as_str(unshifted),
            "one_sided_D1_inverse_approximation": as_str(shifted),
            "exact_predictive_variance": as_str(c_true),
            "ordinary_predictive_variance": as_str(c_bad),
            "one_sided_predictive_variance": as_str(c_good)}


def sample_ball(rng: np.random.Generator, rows: int, dim: int = 2) -> np.ndarray:
    raw = rng.normal(size=(rows, dim))
    raw /= np.linalg.norm(raw, axis=1)[:, None]
    return raw * (RADIUS * rng.uniform(.15, 1., size=(rows, 1)))


def check_kernel_features(x: np.ndarray, max_degrees: list[int]) -> dict:
    full = exact_rbf(x, ELL)
    assert mineig(full) >= -1e-10
    u = np.sum(x*x, axis=1) / ELL**2
    a_radius = RADIUS**2 / ELL**2
    previous = np.zeros_like(full)
    rows = []
    grams = {}
    for p in sorted(max_degrees):
        phi = feature_map(x, p - 1, ELL)
        gram = sym(phi @ phi.T)
        grams[p] = gram
        diag_tail = gammainc(p, u)  # Poisson(u) survival at p.
        tail = full - gram
        delta = a_radius**p / math.factorial(p)
        assert mineig(gram) >= -2e-10
        assert mineig(tail) >= -2e-10
        assert mineig(gram - previous) >= -2e-10
        assert np.max(np.abs(tail)) <= delta + 2e-14
        assert np.max(np.abs(np.diag(tail) - diag_tail)) < 3e-14
        assert np.max(diag_tail) <= delta + 2e-14
        # Direct degree-group formula, independent of explicit multiindices.
        inner = x @ x.T / ELL**2
        scalar_sum = sum(inner**j / math.factorial(j) for j in range(p))
        pref = np.exp(-(u[:, None] + u[None, :]) / 2)
        assert np.max(np.abs(gram - pref * scalar_sum)) < 3e-13
        rows.append({"p": p, "features": phi.shape[1], "delta_bound": delta,
                     "max_abs_kernel_error": float(np.max(np.abs(tail))),
                     "min_full_minus_truncated_eigenvalue": mineig(tail),
                     "min_increment_eigenvalue": mineig(gram - previous),
                     "max_diagonal_poisson_tail": float(np.max(diag_tail))})
        previous = gram
    return {"rows": rows, "grams": grams, "full": full}


def check_gp_case(name: str, x: np.ndarray, n: int, p: int, s: float,
                  y: np.ndarray, degrees: list[int]) -> dict:
    m = len(x) - n
    b = s + n
    a = s
    result = check_kernel_features(x, [1, 2, 5, 20])
    full, trunc = result["full"], result["grams"][p]
    mu, cov = moments(full, y, n, s)
    muk, covk = moments(trunc, y, n, s)
    assert mineig(cov) >= s - 2e-9 and mineig(covk) >= s - 2e-9
    B = float(max(abs(y)))
    delta = (RADIUS / ELL) ** (2*p) / math.factorial(p)
    M = n*math.sqrt(m)*B/s * (1 + n/s)
    V = m * (1+n/s)**2
    S = n*math.sqrt(m)*B/s
    U = n*m/s
    assert_leq(float(np.linalg.norm(mu-muk)), M*delta)
    assert_leq(float(np.linalg.norm(cov-covk, ord="fro")), math.sqrt(m)*V*delta)
    trunc_bound = (M*delta)**2/(2*s) + m*(V*delta)**2/(4*s*s)
    trunc_kl = kl_forward(mu, cov, muk, covk)
    assert_leq(trunc_kl, trunc_bound, atol=5e-9)
    g, h, j = trunc[:n, :n], trunc[:n, n:], trunc[n:, n:]
    amat = g + s*np.eye(n)
    eigs = np.linalg.eigvalsh(amat)
    assert eigs[0] >= s - 1e-9 and eigs[-1] <= b + 1e-9
    solver_rows = []
    for degree in degrees:
        rhs = np.column_stack((y, h))
        poly = cheb_recurrence(amat, rhs, a, b, degree)
        direct = direct_matrix_polynomial(amat, rhs, a, b, degree)
        rel = float(np.linalg.norm(poly-direct) / max(1.0, np.linalg.norm(direct)))
        assert rel < 3e-8, (name, degree, rel)
        _, _, eps = cheb_parameters(a, b, degree)
        e_actual = float(np.max(residual(eigs, a, b, degree)))
        assert_leq(e_actual, eps, atol=2e-12)
        eig_poly = (1-residual(eigs, a, b, degree))/eigs
        min_poly = float(eig_poly.min())
        min_inverse_minus_poly = float(np.min(1/eigs - eig_poly))
        assert min_poly >= -2e-9 and min_inverse_minus_poly >= -2e-9
        muhat, chat = moments(trunc, y, n, s, poly)
        diff = sym(chat-covk)
        assert mineig(diff) >= -3e-9
        assert mineig(chat) >= s - 3e-9
        mean_err = float(np.linalg.norm(muk-muhat))
        assert_leq(mean_err**2, eps**2*n*B*B*m/s, atol=1e-8)
        assert_leq(float(np.linalg.norm(diff, ord=2)),
                   eps*float(np.linalg.norm(j, ord=2)), atol=2e-8)
        solver_kl = kl_forward(muk, covk, muhat, chat)
        solver_bound = eps**2/(4*s*s)*(2*n*B*B*m + m*m)
        assert_leq(solver_kl, solver_bound, atol=1e-8)
        composed_kl = kl_forward(mu, cov, muhat, chat)
        composed_bound = ((M*delta + S*eps)**2/(2*s)
                          + m*(V*delta + U*eps)**2/(4*s*s))
        assert_leq(composed_kl, composed_bound, atol=1e-8)
        solver_rows.append({"D": degree, "L_when_even": degree//2 if degree % 2 == 0 else None,
                            "relative_recurrence_vs_spectral_polynomial": rel,
                            "spectral_max_residual": e_actual, "uniform_residual_bound": eps,
                            "min_P_eigenvalue": min_poly,
                            "min_Ainv_minus_P_eigenvalue": min_inverse_minus_poly,
                            "min_Chat_minus_Ck_eigenvalue": mineig(diff),
                            "min_Chat_eigenvalue": mineig(chat),
                            "mean_error_finite_kernel": mean_err,
                            "solver_forward_KL": solver_kl,
                            "solver_forward_KL_bound": solver_bound,
                            "true_to_approx_forward_KL": composed_kl,
                            "composition_bound": composed_bound})
    return {"name": name, "n": n, "m": m, "p": p, "s": s,
            "a": a, "b": b, "actual_kappa": float(eigs[-1]/eigs[0]),
            "spectral_interval_kappa": b/a, "B": B,
            "delta_kernel_bound": delta,
            "min_full_cov_eigenvalue": mineig(cov),
            "min_finite_cov_eigenvalue": mineig(covk),
            "truncation_forward_KL": trunc_kl,
            "truncation_forward_KL_bound": trunc_bound,
            "kernel_feature_checks": result["rows"],
            "solver_checks": solver_rows}


def main() -> None:
    rng = np.random.default_rng(SEED)
    cases = []
    specifications = [
        ("singleton", 1, 1, 1, 1.0, "random"),
        ("small_joint", 2, 3, 2, .2, "random"),
        ("medium_joint", 5, 2, 5, .01, "random"),
        ("clustered", 8, 4, 5, .001, "clustered"),
        ("singular_training_ill_conditioned", 12, 5, 20, 1e-5, "duplicates"),
    ]
    for name, n, m, p, s, geometry in specifications:
        points = sample_ball(rng, n+m)
        if geometry == "clustered":
            center = np.array([.3, -.2])
            points[:n] = center + .005*rng.normal(size=(n, 2))
        elif geometry == "duplicates":
            points[:n] = np.array([.8, .2])
        y = rng.uniform(-1.0, 1.0, n)
        cases.append(check_gp_case(name, points, n, p, s, y,
                                   [1, 2, 3, 4, 5, 10, 20, 40]))
    grid = check_grid_residual()
    exact = check_fraction_examples()
    adversarial = check_ordinary_counterexample()
    rows = [row for case in cases for row in case["solver_checks"]]
    summary = {
        "gp_prompt_cases": len(cases), "solver_case_checks": len(rows),
        "largest_actual_condition_number": max(case["actual_kappa"] for case in cases),
        "largest_recurrence_relative_discrepancy": max(row["relative_recurrence_vs_spectral_polynomial"] for row in rows),
        "smallest_approx_cov_minus_noise_eigenvalue": min(
            row["min_Chat_eigenvalue"] - case["s"]
            for case in cases for row in case["solver_checks"]),
        "largest_composed_KL_to_bound_ratio": max(
            row["true_to_approx_forward_KL"] / row["composition_bound"]
            for row in rows if row["composition_bound"] > 0),
    }
    output = {"scope": "deterministic numerical checks, exact Fraction edge identities; not proof",
              "numpy_version": np.__version__, "seed": SEED, "radius": RADIUS,
              "ell": ELL, "degrees_checked": [1, 2, 3, 4, 5, 10, 20, 40],
              "L_even_degree_equivalents": [1, 2, 5, 10, 20],
              "summary": summary, "residual_grid": grid,
              "exact_rational_examples": exact,
              "adversarial_ordinary_chebyshev": adversarial,
              "cases": cases}
    path = Path(__file__).with_name("a27_gp_results.json")
    path.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
    print(json.dumps(summary, indent=2, sort_keys=True))
    print(f"wrote {path}")


if __name__ == "__main__":
    main()
