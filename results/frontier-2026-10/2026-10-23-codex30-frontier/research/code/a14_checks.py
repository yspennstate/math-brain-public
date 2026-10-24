#!/usr/bin/env python3
"""Reproducible quadrature and exact-moment checks for T228 SGD examples.

Run: python research/code/a14_checks.py
Requires scipy (and its numpy dependency). All strict inequalities used for
contraction are certified by Fraction arithmetic; quadrature is descriptive.
"""

from __future__ import annotations

import json
import math
from fractions import Fraction as Q
from pathlib import Path

from scipy.integrate import quad
from scipy.optimize import brentq
from scipy.special import ellipe, hyp2f1


D = 2
SMOOTH_ETA = Q(13, 25)
SMOOTH_EPS = Q(1, 1000)
LEAKY_A = Q(1, 2)
LEAKY_ETA = Q(3, 5)
T_MAX = 100.0


def rising(x: Q, n: int) -> Q:
    result = Q(1)
    for j in range(n):
        result *= x + j
    return result


def binomial(n: int, k: int) -> int:
    return math.comb(n, k)


def moment_even(d: int, beta: Q, k: int) -> Q:
    """Exact E ||(I-beta X X^T)e||^(2k), X standard Gaussian.

    T=||X||^2 is chi-square_d, U=(e.X)^2/T is Beta(1/2,(d-1)/2)
    independently, and M^2=1-(2 beta T-beta^2 T^2)U.
    """
    if d < 2 or k < 0:
        raise ValueError("d >= 2, k >= 0 required")
    total = Q(0)
    for j in range(k + 1):
        q_moment = sum(
            (
                Q(binomial(j, ell))
                * (-1) ** ell
                * (2 * beta) ** (j - ell)
                * beta ** (2 * ell)
                * 2 ** (j + ell)
                * rising(Q(d, 2), j + ell)
                for ell in range(j + 1)
            ),
            Q(0),
        )
        u_moment = rising(Q(1, 2), j) / rising(Q(d, 2), j)
        total += binomial(k, j) * (-1) ** j * u_moment * q_moment
    return total


def mixture_even(d: int, eta: Q, a: Q, k: int) -> Q:
    return (moment_even(d, eta, k) + moment_even(d, eta * a * a, k)) / 2


def closed_m2_m4(d: int, eta: Q, a: Q) -> tuple[Q, Q]:
    mu = [Q(1)] + [(1 + a ** (2 * j)) / 2 for j in range(1, 5)]
    m2 = 1 - 2 * eta * mu[1] + (d + 2) * eta * eta * mu[2]
    m4 = (
        1
        - 4 * eta * mu[1]
        + 2 * (d + 8) * eta**2 * mu[2]
        - 12 * (d + 4) * eta**3 * mu[3]
        + 3 * (d + 4) * (d + 6) * eta**4 * mu[4]
    )
    return m2, m4


def certified_h1_upper(m2: Q, m4: Q, m6: Q) -> Q:
    """Rational upper bound from a quadratic Jensen deficit.

    With S=M^2, sqrt(S) <= (1+S)/2-(S-1)^2/[4(S+1)].
    Cauchy gives E[(S-1)^2/(S+1)] >=
        (E(S-1)^2)^2 / E[(S-1)^2(S+1)].
    """
    variance_around_one = m4 - 2 * m2 + 1
    weighted = m6 - m4 - m2 + 1
    assert variance_around_one > 0 and weighted > 0
    return (1 + m2) / 2 - variance_around_one**2 / (4 * weighted)


def angular_average(p: float, t: float) -> float:
    q = 2 * t - t * t
    return float(hyp2f1(-p / 2, 0.5, 1.0, q))


def radial_quadrature(p: float, beta: Q, *, tolerance: float = 2e-13) -> tuple[float, float]:
    """d=2 exact angular integration followed by adaptive radial quadrature.

    Here t=beta ||X||^2 has exponential density exp(-t/(2 beta))/(2 beta).
    Splitting at t=1 isolates the integrable angular cusp M=0.
    """
    scale = 2 * float(beta)

    def integrand(t: float) -> float:
        return angular_average(p, t) * math.exp(-t / scale) / scale

    parts = [quad(integrand, lo, hi, epsabs=tolerance, epsrel=tolerance, limit=600)
             for lo, hi in ((0, 1), (1, 4), (4, 20), (20, T_MAX))]
    # p in [1,2]. Since M<=1+t, a conservative tail bound uses (1+t)^2.
    tail_bound = math.exp(-T_MAX / scale) * (
        (1 + T_MAX) ** 2 + 2 * scale * (1 + T_MAX) + 2 * scale**2
    )
    return sum(x for x, _ in parts), sum(err for _, err in parts) + tail_bound


def elliptic_h1(beta: Q) -> tuple[float, float]:
    """Independent special-function check: E_theta M=(2/pi)EllipticE(q)."""
    scale = 2 * float(beta)

    def integrand(t: float) -> float:
        q = 2 * t - t * t
        return (2 / math.pi) * ellipe(q) * math.exp(-t / scale) / scale

    parts = [quad(integrand, lo, hi, epsabs=2e-13, epsrel=2e-13, limit=600)
             for lo, hi in ((0, 1), (1, 4), (4, 20), (20, T_MAX))]
    tail_bound = math.exp(-T_MAX / scale) * (
        (1 + T_MAX) ** 2 + 2 * scale * (1 + T_MAX) + 2 * scale**2
    )
    return sum(x for x, _ in parts), sum(err for _, err in parts) + tail_bound


def mixture_quadrature(p: float, eta: Q, a: Q) -> tuple[float, float]:
    if a == 1:
        return radial_quadrature(p, eta)
    first, first_err = radial_quadrature(p, eta)
    second, second_err = radial_quadrature(p, eta * a * a)
    return (first + second) / 2, (first_err + second_err) / 2


def frac(q: Q) -> str:
    return str(q.numerator) if q.denominator == 1 else f"{q.numerator}/{q.denominator}"


def leaky_update(w: tuple[Q, ...], x: tuple[Q, ...], y: Q, eta: Q, a: Q) -> tuple[Q, ...]:
    z = sum((u * v for u, v in zip(w, x)), Q(0))
    assert z != 0
    c = Q(1) if z > 0 else a
    return tuple(wi - eta * c * (c * z - y) * xi for wi, xi in zip(w, x))


def affine_gate_update(w: tuple[Q, ...], x: tuple[Q, ...], y: Q, eta: Q, c: Q) -> tuple[Q, ...]:
    z = sum((u * v for u, v in zip(w, x)), Q(0))
    return tuple(wi - eta * c * (c * z - y) * xi for wi, xi in zip(w, x))


def check_antipodal_pair() -> int:
    """Exact Fraction identity of *unordered* conditional output pairs.

    (X,Y)->(-X,-Y) preserves XX^T and YX while flipping sign(w.X).
    This proves the transition-kernel reduction, not pathwise gate equality.
    """
    examples = [
        ((Q(1), Q(2)), (Q(3), Q(-1)), Q(5, 7)),
        ((Q(-2), Q(1)), (Q(1, 2), Q(4)), Q(-3, 8)),
        ((Q(5, 3), Q(-4)), (Q(2), Q(3, 5)), Q(7)),
    ]
    for w, x, y in examples:
        antix = tuple(-xi for xi in x)
        actual = {leaky_update(w, x, y, LEAKY_ETA, LEAKY_A),
                  leaky_update(w, antix, -y, LEAKY_ETA, LEAKY_A)}
        surrogate = {affine_gate_update(w, x, y, LEAKY_ETA, Q(1)),
                     affine_gate_update(w, x, y, LEAKY_ETA, LEAKY_A)}
        assert actual == surrogate and len(actual) == 2
    return len(examples)


def summarize(name: str, eta: Q, a: Q) -> dict:
    m2 = mixture_even(D, eta, a, 1)
    m4 = mixture_even(D, eta, a, 2)
    m6 = mixture_even(D, eta, a, 3)
    assert (m2, m4) == closed_m2_m4(D, eta, a)
    upper = certified_h1_upper(m2, m4, m6)
    assert upper < 1 < m2
    h1, h1_err = mixture_quadrature(1, eta, a)
    h1_elliptic, h1_elliptic_err = elliptic_h1(eta)
    if a != 1:
        second, second_err = elliptic_h1(eta * a * a)
        h1_elliptic = (h1_elliptic + second) / 2
        h1_elliptic_err = (h1_elliptic_err + second_err) / 2
    assert abs(h1 - h1_elliptic) < 1e-11
    for k in (1, 2):
        numeric, numeric_err = mixture_quadrature(2 * k, eta, a)
        exact = (m2, m4)[k - 1]
        assert abs(numeric - float(exact)) < max(1e-11, 20 * numeric_err)

    def root_function(p: float) -> float:
        return mixture_quadrature(p, eta, a)[0] - 1

    alpha = brentq(root_function, 1.0, 2.0, xtol=5e-14)
    root_residual, root_integral_err = mixture_quadrature(alpha, eta, a)
    assert 1 < alpha < 2 and abs(root_residual - 1) < 2e-11
    return {
        "name": name,
        "d": D,
        "eta": frac(eta),
        "a": frac(a),
        "exact_moments": {"h2": frac(m2), "h4": frac(m4), "h6": frac(m6)},
        "analytic_certificate": {
            "h1_upper_exact": frac(upper),
            "h1_upper_decimal": float(upper),
            "h2_minus_1_exact": frac(m2 - 1),
        },
        "quadrature": {
            "h1": h1,
            "h1_quadpack_abs_error_estimate": h1_err,
            "h1_elliptic_check": h1_elliptic,
            "h1_elliptic_quadpack_abs_error_estimate": h1_elliptic_err,
            "alpha_root": alpha,
            "root_function_abs_error_estimate": root_integral_err,
            "root_residual": root_residual - 1,
        },
    }


def main() -> None:
    antipodal_checks = check_antipodal_pair()
    smooth = summarize("smooth_phi_z_plus_epsilon_tanh_z", SMOOTH_ETA, Q(1))
    leaky = summarize("leaky_relu", LEAKY_ETA, LEAKY_A)
    smooth_upper = Q(smooth["analytic_certificate"]["h1_upper_exact"])
    # Directional K = eta |e.X| ||X|| (7+2|Y|), Y~N(0,1).
    # E|e.X| ||X|| <= sqrt(E[(e.X)^2 ||X||^2])=sqrt(d+2)=2,
    # E|Y| <= sqrt(E Y^2)=1. Hence EK <= eta * 2 * 9 exactly.
    ek_upper = SMOOTH_ETA * 2 * 9
    smooth_average_contraction_upper = smooth_upper + SMOOTH_EPS * ek_upper
    assert smooth_average_contraction_upper < 1
    smooth["analytic_certificate"].update({
        "epsilon": frac(SMOOTH_EPS),
        "E_K_upper_exact": frac(ek_upper),
        "average_distance_factor_upper_exact": frac(smooth_average_contraction_upper),
        "average_distance_factor_upper_decimal": float(smooth_average_contraction_upper),
        "strict_margin_lower_exact": frac(1 - smooth_average_contraction_upper),
    })
    output = {
        "method": "Exact Fraction moments and Cauchy bound; scipy QUADPACK angular-hypergeometric radial quadrature (non-rigorous estimates)",
        "quadrature_t_max": T_MAX,
        "antipodal_exact_fraction_examples": antipodal_checks,
        "smooth": smooth,
        "leaky": leaky,
    }
    target = Path(__file__).with_name("a14_results.json")
    target.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
    print(json.dumps(output, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
