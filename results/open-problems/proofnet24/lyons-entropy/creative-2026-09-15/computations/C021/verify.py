"""Reproduce C021's unequal-replacement identities and affine-kernel example.

The analytic proofs are in agents/C021.md. These finite floating-point checks
are corroboration, and the parity obstruction is also evaluated symbolically.
"""

import json
from pathlib import Path

import numpy as np
import sympy as sp


ROOT = Path(__file__).resolve().parent
RNG = np.random.default_rng(2102120260915)


def bits(n):
    return ((np.arange(1 << n)[:, None] >> np.arange(n)) & 1).astype(int)


def replace(p, i, mean):
    masks = np.arange(len(p))
    low = masks & ~(1 << i)
    total = p[low] + p[low | (1 << i)]
    return total * np.where((masks >> i) & 1, mean, 1 - mean)


def product_mu(means):
    x = bits(len(means))
    return np.prod(np.where(x, means, 1 - means), axis=1)


def channel(p, means, eta, sites):
    p = p.copy()
    for i, e in zip(sites, eta):
        p = e * p + (1 - e) * replace(p, i, means[i])
    return p


def stats(p, means, sites):
    qs = [replace(p, i, means[i]) for i in sites]
    ds = [p - q for q in qs]
    js = np.array([np.sum(d * np.log(p / q)) for d, q in zip(ds, qs)])
    chis = np.array([np.sum(d * d / p) for d in ds])
    es = np.zeros((len(sites), len(sites)))
    for a, (q, d) in enumerate(zip(qs, ds)):
        r = np.log(p / q)
        for b, j in enumerate(sites):
            if a == b:
                continue
            u = replace(p, j, means[j]) - p
            v = replace(q, j, means[j]) - q
            es[a, b] = -np.sum(
                u * (r + 1 - q / p) + v * (-r + 1 - p / q)
            )
    return js, chis, es, np.array(ds)


def direct_replacement_derivatives(p, means, sites, eta):
    mu = product_mu(means)
    log_ratio = np.log(p / mu)
    ds = np.array([p - replace(p, i, means[i]) for i in sites])
    dp = ds / eta[:, None]
    grad = dp @ log_ratio
    hess = (dp / p) @ dp.T
    for a, i in enumerate(sites):
        for b, j in enumerate(sites):
            if a != b:
                dpij = (ds[a] - replace(ds[a], j, means[j])) / (eta[a] * eta[b])
                hess[a, b] += dpij @ log_ratio
    return grad, hess


def dpp_atoms(K, A=None):
    n = len(K)
    eye = np.eye(n)
    probabilities, first, second = [], [], []
    for x in bits(n):
        M = np.where(x[None, :] == 1, K, eye - K)
        p = float(np.linalg.det(M).real)
        probabilities.append(p)
        if A is not None:
            V = A * (2 * x - 1)[None, :]
            R = np.linalg.solve(M, V)
            tr = np.trace(R)
            first.append(float((p * tr).real))
            second.append(float((p * (tr * tr - np.trace(R @ R))).real))
    p = np.array(probabilities)
    if A is None:
        return p
    return p, np.array(first), np.array(second)


def kernel_with_f(K, m, f):
    out = K.copy()
    out[:m, m:] = f[:, None] * K[:m, m:]
    out[m:, :m] = out[:m, m:].conj().T
    return out


def entropy(p):
    return float(-np.sum(p * np.log(p)))


def hessian_from_atoms(p, dp, ddp):
    return float(-np.sum(dp * dp / p) - np.sum(ddp * np.log(p)))


def channel_checks():
    max_grad_error = max_hess_error = max_symmetry_error = 0.0
    min_first = min_diag = min_mixed = float("inf")
    count = 180
    for trial in range(count):
        n = 2 + trial % 5
        p0 = RNG.gamma(0.8, 1.0, size=1 << n)
        p0 /= p0.sum()
        means = p0 @ bits(n)
        sites = list(range(n))
        eta = RNG.uniform(0.2, 0.9, n)
        p = channel(p0, means, eta, sites)
        js, chis, es, _ = stats(p, means, sites)
        grad, hess = direct_replacement_derivatives(p, means, sites, eta)
        predicted = es / eta[:, None] / eta[None, :]
        np.fill_diagonal(predicted, chis / eta**2)
        max_grad_error = max(max_grad_error, float(np.max(np.abs(grad - js / eta))))
        max_hess_error = max(max_hess_error, float(np.max(np.abs(hess - predicted))))
        max_symmetry_error = max(max_symmetry_error, float(np.max(np.abs(es - es.T))))
        min_first = min(min_first, float(np.min(grad)))
        min_diag = min(min_diag, float(np.min(np.diag(hess))))
        min_mixed = min(min_mixed, float(np.min(hess[~np.eye(n, dtype=bool)])))
    assert max_grad_error < 2e-12
    assert max_hess_error < 2e-12
    assert max_symmetry_error < 2e-12
    assert min(min_first, min_diag, min_mixed) > -2e-12
    return dict(
        trials=count,
        max_gradient_identity_error=max_grad_error,
        max_hessian_identity_error=max_hess_error,
        max_cross_dissipation_asymmetry=max_symmetry_error,
        minimum_first_partial=min_first,
        minimum_diagonal_second_partial=min_diag,
        minimum_mixed_second_partial=min_mixed,
    )


def affine_checks():
    max_atom_error = max_curvature_error = 0.0
    max_curvature = -float("inf")
    count = 120
    for trial in range(count):
        n = 4 + trial % 4
        m = 2 + trial % (n - 2)
        means = RNG.uniform(0.3, 0.7, n)
        V = RNG.normal(size=(n, n)) + 1j * RNG.normal(size=(n, n))
        V = (V + V.conj().T) / 2
        np.fill_diagonal(V, 0)
        V[:m, :m] = 0
        V *= 0.8 * min(np.min(means), np.min(1 - means)) / np.linalg.norm(V, 2)
        K = np.diag(means) + V
        starts = RNG.uniform(0.15, 0.7, m)
        slopes = RNG.uniform(0.05, 0.95, m) * (1 - starts)
        t = RNG.uniform(0.15, 0.85)
        f = starts + t * slopes
        Kt = kernel_with_f(K, m, f)
        A = np.zeros_like(K)
        A[:m, m:] = slopes[:, None] * K[:m, m:]
        A[m:, :m] = A[:m, m:].conj().T
        p, dp, ddp = dpp_atoms(Kt, A)
        pc = channel(dpp_atoms(K), means, f**2, list(range(m)))
        js, chis, es, _ = stats(p, means, list(range(m)))
        u = slopes / f
        predicted = -float(np.sum((4 * chis + 2 * js) * u * u) + 4 * u @ es @ u)
        actual = hessian_from_atoms(p, dp, ddp)
        max_atom_error = max(max_atom_error, float(np.max(np.abs(p - pc))))
        max_curvature_error = max(max_curvature_error, abs(predicted - actual))
        max_curvature = max(max_curvature, actual)
    assert max_atom_error < 2e-12
    assert max_curvature_error < 2e-11
    assert max_curvature < 0
    return dict(
        trials=count,
        max_atom_identity_error=max_atom_error,
        max_affine_curvature_identity_error=max_curvature_error,
        maximum_sampled_entropy_curvature=max_curvature,
    )


def exact_six_site_example():
    integer_B = sp.Matrix([[3, 1, 0], [0, 2, 1], [1, 0, 2]])
    outside = sp.Matrix([[0, 1, 2], [1, 0, -1], [2, -1, 0]])
    exact_K = sp.eye(6) / 2
    exact_K[:3, 3:] = integer_B / 40
    exact_K[3:, :3] = integer_B.T / 40
    exact_K[3:, 3:] += outside / 40
    exact_slopes = sp.diag(sp.Rational(3, 4), sp.Rational(1, 2), sp.Rational(1, 4))
    exact_A = sp.zeros(6)
    exact_A[:3, 3:] = exact_slopes * integer_B / 40
    exact_A[3:, :3] = exact_A[:3, 3:].T
    assert integer_B.det() == 13
    assert exact_A.rank() == 6
    rows = [sum(abs(exact_K[i, j]) for j in range(6) if i != j) for i in range(6)]
    assert max(rows) == sp.Rational(7, 40)
    K = np.array(exact_K).astype(float)
    A = np.array(exact_A).astype(float)
    starts = np.array([0.25, 0.5, 0.75])
    slopes = np.array([0.75, 0.5, 0.25])
    values = []
    for t in [0.0, 0.25, 0.5, 0.75, 1.0]:
        p, dp, ddp = dpp_atoms(kernel_with_f(K, 3, starts + t * slopes), A)
        values.append(dict(t=t, entropy=entropy(p), curvature=hessian_from_atoms(p, dp, ddp)))
    return dict(
        determinant_integer_B=str(integer_B.det()),
        exact_direction_rank=int(exact_A.rank()),
        direction_inertia=[3, 3, 0],
        maximal_offdiagonal_row_sum=str(max(rows)),
        spectral_enclosure=["13/40", "27/40"],
        sampled_values=values,
        midpoint_entropy_gap=values[2]["entropy"] - (values[0]["entropy"] + values[4]["entropy"]) / 2,
    )


def parity_obstruction():
    t, e = sp.symbols("t e", real=True)
    r = e * (1 - t * t) ** 2 / 16
    phi = ((1 + r) * sp.log(1 + r) + (1 - r) * sp.log(1 - r)) / 2
    hdd = sp.simplify(-sp.diff(phi, t, 2).subs(t, 0))
    expected = e * (sp.log(1 + e / 16) - sp.log(1 - e / 16)) / 8
    assert sp.simplify(hdd - expected) == 0
    n = 3
    x = bits(n)
    epsilon = 0.5
    p = (1 + epsilon * (-1.0) ** np.sum(x, axis=1)) / 8
    means = p @ x
    p0 = channel(p, means, np.array([0.25, 0.25]), [0, 1])
    js, chis, es, _ = stats(p0, means, [0, 1])
    u = np.array([1.0, -1.0])
    curvature = -float(np.sum((4 * chis + 2 * js) * u * u) + 4 * u @ es @ u)
    exact_value = float(hdd.subs(e, sp.Rational(1, 2)))
    assert abs(curvature - exact_value) < 1e-14
    assert exact_value > 0
    selected_marginal = [float(sum(p[mask] for mask in range(8) if mask & 3 == pair)) for pair in range(4)]
    assert selected_marginal == [0.25] * 4
    return dict(
        selected_pair_marginal=selected_marginal,
        exact_entropy_curvature="(epsilon/4) * atanh(epsilon/16)",
        epsilon_half_curvature=exact_value,
        predicted_curvature=curvature,
        symbolic_expression=str(hdd),
        note="A channel obstruction; this parity law cannot be a nonproduct DPP.",
    )


if __name__ == "__main__":
    results = dict(
        seed=2102120260915,
        replacement=channel_checks(),
        affine_dpp=affine_checks(),
        six_site=exact_six_site_example(),
        parity=parity_obstruction(),
    )
    (ROOT / "results.json").write_text(json.dumps(results, indent=2) + "\n")
    print(json.dumps(results, indent=2))
