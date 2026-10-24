"""Reproduce the balanced four-site path theorem and its CMI obstruction.

The proof is in agents/C026.md. Random checks are corroboration only.
The final CMI-curvature sign is certified with rational log bounds.
"""

from fractions import Fraction as Q
import json
from math import atanh, exp, log, log1p, tanh
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parent
RNG = np.random.default_rng(2602620260915)
BITS = ((np.arange(16)[:, None] >> np.arange(4)) & 1).astype(int)
SPINS = 2 * BITS - 1
U = SPINS[:, 0] * SPINS[:, 2]
V = SPINS[:, 2] * SPINS[:, 3]
W = SPINS[:, 1] * SPINS[:, 3]


def kernel(u, v, w):
    K = np.eye(4, dtype=complex) / 2
    K[0, 2], K[1, 3], K[2, 3] = u, v, w
    K[2, 0], K[3, 1], K[3, 2] = np.conj(u), np.conj(v), np.conj(w)
    return K


def dpp_atoms(K, A):
    p, dp, ddp = [], [], []
    for x in BITS:
        M = np.where(x[None, :] == 1, K, np.eye(4) - K)
        prob = float(np.linalg.det(M).real)
        R = np.linalg.solve(M, A * (2 * x - 1)[None, :])
        tr = np.trace(R)
        p.append(prob)
        dp.append(float((prob * tr).real))
        ddp.append(float((prob * (tr * tr - np.trace(R @ R))).real))
    return np.array(p), np.array(dp), np.array(ddp)


def marginal(p, sites):
    masks = sum(BITS[:, i] << j for j, i in enumerate(sites))
    return np.bincount(masks, weights=p, minlength=1 << len(sites))


def entropy(p):
    return float(-np.sum(p * np.log(p)))


def curvature(p, dp, ddp):
    return float(-np.sum(dp * dp / p) - np.sum(ddp * np.log(p)))


def cmi(p):
    return (
        entropy(marginal(p, [0, 2, 3]))
        + entropy(marginal(p, [1, 2, 3]))
        - entropy(marginal(p, [2, 3]))
        - entropy(p)
    )


def phi(x):
    return ((1 + x) * log1p(x) + (1 - x) * log1p(-x)) / 2


def log_A(m, x):
    z = m * atanh(x)
    log_cosh = abs(z) + log1p(exp(-2 * abs(z))) - log(2)
    return -m * log1p(-x * x) / 2 + log_cosh


def log_A_derivatives(m, x):
    t = tanh(m * atanh(x))
    d = 1 - x * x
    first = m * (x + t) / d
    second = m * (1 + x * x + 2 * x * t + m * (1 - t * t)) / d**2
    return first, second


def series(a, b, c, da, dc, dda, ddc):
    """Exact-series value, CMI, and the nonnegative curvature decomposition."""
    deficit = phi(a) + phi(c)
    conditional_mi = 0.0
    baseline_curvature = da * da / (1 - a * a) + atanh(a) * dda
    baseline_curvature += dc * dc / (1 - c * c) + atanh(c) * ddc
    squares_curvature = 0.0
    last = None
    for k in range(1, 1001):
        m = 2 * k - 1
        la, lc = log_A(m, a), log_A(m, c)
        term = exp(2 * k * log(b) - log(2 * k * (2 * k - 1)) + la + lc)
        lpa, lppa = log_A_derivatives(m, a)
        lpc, lppc = log_A_derivatives(m, c)
        squared = (lpa * da + lpc * dc) ** 2
        diagonal = lppa * da * da + lpa * dda + lppc * dc * dc + lpc * ddc
        contribution = term * (squared + diagonal)
        assert min(term, squared, diagonal, contribution) >= 0
        deficit += term
        conditional_mi += term * (-np.expm1(-la)) * (-np.expm1(-lc))
        squares_curvature += contribution
        last = max(term, contribution)
        if k > 12 and last < 1e-17:
            break
    else:
        raise AssertionError("The verification series did not converge.")
    return deficit, conditional_mi, baseline_curvature + squares_curvature, k


def replace(p, i):
    masks = np.arange(16)
    lo = masks & ~(1 << i)
    return (p[lo] + p[lo | (1 << i)]) / 2


def channel_stats(p):
    chi, jeffreys = [], []
    for i in [0, 1]:
        q = replace(p, i)
        d = p - q
        chi.append(float(np.sum(d * d / p)))
        jeffreys.append(float(np.sum(d * np.log(p / q))))
    q = replace(p, 0)
    r = np.log(p / q)
    u = replace(p, 1) - p
    v = replace(q, 1) - q
    cross = -float(np.sum(u * (r + 1 - q / p) + v * (-r + 1 - p / q)))
    return chi, jeffreys, cross


def random_checks():
    errors = dict(atom=0.0, entropy_series=0.0, cmi_series=0.0,
                  curvature_series=0.0, fisher_identities=0.0)
    largest_hpp = -float("inf")
    least_excess_fisher_eigenvalue = float("inf")
    least_cross_bound_slack = float("inf")
    maximum_terms = 0
    opposite_radial_signs = 0
    trials = 240
    for _ in range(trials):
        a, c = RNG.uniform(0.05, 0.70, 2)
        b = RNG.uniform(0.15, 0.85) * (1 - a) * (1 - c)
        phases = np.exp(1j * RNG.uniform(-np.pi, np.pi, 3))
        u, v, w = np.sqrt([a, c, b]) * phases / 2
        du, dv = (RNG.normal(size=2) + 1j * RNG.normal(size=2)) / 5
        K = kernel(u, v, w)
        A = kernel(du, dv, 0) - np.eye(4) / 2
        p, dp, ddp = dpp_atoms(K, A)
        predicted_atoms = ((1 - a * U) * (1 - c * W) - b * V) / 16
        da, dc = 8 * np.real(np.conj(u) * du), 8 * np.real(np.conj(v) * dv)
        dda, ddc = 8 * abs(du) ** 2, 8 * abs(dv) ** 2
        deficit, cmi_value, positive_curvature, terms = series(a, b, c, da, dc, dda, ddc)
        direct_hpp = curvature(p, dp, ddp)
        errors["atom"] = max(errors["atom"], float(np.max(abs(p - predicted_atoms))))
        errors["entropy_series"] = max(errors["entropy_series"], abs(4 * log(2) - deficit - entropy(p)))
        errors["cmi_series"] = max(errors["cmi_series"], abs(cmi_value - cmi(p)))
        errors["curvature_series"] = max(errors["curvature_series"], abs(direct_hpp + positive_curvature))
        largest_hpp = max(largest_hpp, direct_hpp)
        maximum_terms = max(maximum_terms, terms)
        opposite_radial_signs += da * dc < 0

        pa = -U * (1 - c * W) / 16
        pc = -W * (1 - a * U) / 16
        pac = U * W / 16
        faa, fcc = np.sum(pa * pa / p), np.sum(pc * pc / p)
        fac = np.sum(pa * pc / p) + np.sum(pac * np.log(p))
        chi, js, cross = channel_stats(p)
        errors["fisher_identities"] = max(
            errors["fisher_identities"],
            abs(chi[0] - a * a * faa), abs(chi[1] - c * c * fcc), abs(cross - a * c * fac),
        )
        remainder_hessian = np.array([[faa - 1 / (1 - a * a), fac],
                                      [fac, fcc - 1 / (1 - c * c)]])
        least_excess_fisher_eigenvalue = min(
            least_excess_fisher_eigenvalue, float(np.linalg.eigvalsh(remainder_hessian)[0]))
        remainder_chi = [chi[0] - a * a / (1 - a * a), chi[1] - c * c / (1 - c * c)]
        least_cross_bound_slack = min(least_cross_bound_slack, remainder_chi[0] * remainder_chi[1] - cross * cross)
    assert max(errors.values()) < 3e-11, errors
    assert largest_hpp < 0
    assert least_excess_fisher_eigenvalue > 0
    assert least_cross_bound_slack > 0
    return dict(trials=trials, opposite_radial_sign_trials=int(opposite_radial_signs),
                maximum_identity_errors=errors, largest_entropy_curvature=largest_hpp,
                least_excess_fisher_eigenvalue=least_excess_fisher_eigenvalue,
                least_strong_cross_bound_slack=least_cross_bound_slack,
                maximum_series_terms=maximum_terms)


def log_bounds(x, terms=24):
    """Rational lower/upper bounds, using range-reduced atanh series."""
    exponent = 0
    y = x
    while y < 1:
        y *= 2
        exponent -= 1
    while y >= 2:
        y /= 2
        exponent += 1

    def reduced(z):
        r = (z - 1) / (z + 1)
        lower = 2 * sum((r ** (2 * k + 1) / (2 * k + 1) for k in range(terms)), Q(0))
        tail = 2 * r ** (2 * terms + 1) / ((2 * terms + 1) * (1 - r * r))
        return lower, lower + tail

    lo, hi = reduced(y)
    lo2, hi2 = reduced(Q(2))
    if exponent >= 0:
        return lo + exponent * lo2, hi + exponent * hi2
    return lo + exponent * hi2, hi + exponent * lo2


def exact_atoms(a, b, c):
    """At t=0 for a(t)=a(1+t)^2, c(t)=c(1-t)^2."""
    p, dp, ddp = [], [], []
    for uu, vv, ww in zip(U, V, W):
        uu, vv, ww = int(uu), int(vv), int(ww)
        p.append(((1 - a * uu) * (1 - c * ww) - b * vv) / 16)
        dp.append((-2 * a * uu * (1 - c * ww) + 2 * c * ww * (1 - a * uu)) / 16)
        ddp.append((-2 * a * uu * (1 - c * ww) - 2 * c * ww * (1 - a * uu)
                    - 8 * a * c * uu * ww) / 16)
    return p, dp, ddp


def exact_marginal(values, sites):
    out = [Q(0)] * (1 << len(sites))
    for mask, value in enumerate(values):
        outmask = sum(((mask >> i) & 1) << j for j, i in enumerate(sites))
        out[outmask] += value
    return out


def exact_hessian_bounds(p, dp, ddp):
    rational = -sum((d * d / x for x, d in zip(p, dp)), Q(0))
    lo, hi = rational, rational
    for x, dd in zip(p, ddp):
        xl, xh = log_bounds(x)
        coefficient = -dd
        if coefficient >= 0:
            lo += coefficient * xl
            hi += coefficient * xh
        else:
            lo += coefficient * xh
            hi += coefficient * xl
    return lo, hi


def exact_cmi_obstruction():
    a, b, c = Q(1, 16), Q(16, 25), Q(1, 16)
    assert (1 - a) * (1 - c) > b
    arrays = exact_atoms(a, b, c)
    full = exact_hessian_bounds(*arrays)
    t1 = exact_hessian_bounds(*(exact_marginal(x, [0, 2, 3]) for x in arrays))
    t2 = exact_hessian_bounds(*(exact_marginal(x, [1, 2, 3]) for x in arrays))
    clo, chi = t1[0] + t2[0] - full[1], t1[1] + t2[1] - full[0]
    assert chi < 0
    assert -Q(3, 10000) < clo < chi < -Q(2, 10000)
    assert full[1] < 0
    return dict(a=str(a), b=str(b), c=str(c),
                cmi_second_derivative_lower=str(clo), cmi_second_derivative_upper=str(chi),
                cmi_second_derivative_decimal=[float(clo), float(chi)],
                entropy_second_derivative_decimal=[float(full[0]), float(full[1])],
                exact_simple_sign_certificate="-3/10000 < CMI''(0) < -2/10000",
                series_terms_per_log=24)


def affine_example():
    def at(t):
        u, v, w = (1 + t) / 8, (2 - t) / 8, 2 / 5
        K = kernel(u, v, w)
        A = kernel(1 / 8, -1 / 8, 0) - np.eye(4) / 2
        p, dp, ddp = dpp_atoms(K, A)
        return dict(t=t, entropy=entropy(p), entropy_curvature=curvature(p, dp, ddp),
                    kernel_eigenvalues=np.linalg.eigvalsh(K).tolist())
    values = [at(t) for t in [0, 0.25, 0.5, 0.75, 1]]
    assert all(v["entropy_curvature"] < 0 for v in values)
    midpoint_gap = values[2]["entropy"] - (values[0]["entropy"] + values[-1]["entropy"]) / 2
    A = kernel(1 / 8, -1 / 8, 0) - np.eye(4) / 2
    return dict(outer_edges="u(t)=(1+t)/8; v(t)=(2-t)/8", middle_edge="w=2/5",
                samples=values, midpoint_entropy_gap=midpoint_gap,
                direction_eigenvalues=np.linalg.eigvalsh(A).tolist(),
                minimum_endpoint_contraction_determinant="101/1600")


if __name__ == "__main__":
    results = dict(random_checks=random_checks(), affine_example=affine_example(),
                   exact_conditional_mi_obstruction=exact_cmi_obstruction())
    (ROOT / "results.json").write_text(json.dumps(results, indent=2) + "\n")
    compact = json.loads(json.dumps(results))
    for key in ["cmi_second_derivative_lower", "cmi_second_derivative_upper"]:
        compact["exact_conditional_mi_obstruction"].pop(key)
    print(json.dumps(compact, indent=2))
