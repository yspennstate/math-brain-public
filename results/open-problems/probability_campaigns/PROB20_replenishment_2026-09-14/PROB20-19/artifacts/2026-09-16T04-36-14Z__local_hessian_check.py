#!/usr/bin/env python3
"""Reproducibility checks for PROB20-19 local Hessian theorem.

This is supporting numerical self-review, not a proof.
Checks:
  1) conditional folded-angle curvature formula against finite differences;
  2) negative population-direction evidence for every Givens pair in a fixed
     simple spectrum using a sign-symmetrized common-random-number bank;
  3) mixed Hessian entries numerically vanish in exponential coordinates.
"""
import itertools
import numpy as np
from scipy.integrate import quad
from scipy.linalg import expm


def normalizer(kappa: float) -> float:
    return quad(
        lambda u: np.cosh(kappa * np.cos(2.0 * u)),
        -np.pi / 4.0,
        np.pi / 4.0,
        epsabs=1e-12,
        limit=300,
    )[0]


def conditional_J(theta: float, s: float, tau: float, kappa: float) -> float:
    z = normalizer(kappa)

    def integrand(u: float) -> float:
        h = max(0.0, 0.5 * s * (1.0 + np.cos(2.0 * u)) - tau)
        q_shift = np.cosh(kappa * np.cos(2.0 * (u + theta))) / z
        return h * q_shift

    return quad(
        integrand,
        -np.pi / 4.0,
        np.pi / 4.0,
        epsabs=1e-11,
        limit=300,
    )[0]


def conditional_Jpp_formula(s: float, tau: float, kappa: float) -> float:
    z = normalizer(kappa)

    def integrand(u: float) -> float:
        active = 0.5 * s * (1.0 + np.cos(2.0 * u)) > tau
        if not active:
            return 0.0
        return np.sin(2.0 * u) ** 2 * np.sinh(kappa * np.cos(2.0 * u))

    val = quad(
        integrand,
        0.0,
        np.pi / 4.0,
        epsabs=1e-11,
        limit=300,
    )[0]
    return -4.0 * s * kappa * val / z


def Eij(p: int, i: int, j: int) -> np.ndarray:
    E = np.zeros((p, p))
    E[i, j] = 1.0
    E[j, i] = -1.0
    return E


def main() -> None:
    print("=== conditional curvature identity ===")
    cases = [
        (2.3, 0.7, 0.8),
        (1.1, 0.9, 2.0),
        (3.0, 1.4, 0.3),
        (2.0, 0.4, 1.7),
    ]
    h = 2e-4
    max_abs_err = 0.0
    for s, tau, kappa in cases:
        fd = (
            conditional_J(h, s, tau, kappa)
            - 2.0 * conditional_J(0.0, s, tau, kappa)
            + conditional_J(-h, s, tau, kappa)
        ) / h**2
        exact = conditional_Jpp_formula(s, tau, kappa)
        err = abs(fd - exact)
        max_abs_err = max(max_abs_err, err)
        print(
            f"s={s:.3g} tau={tau:.3g} kappa={kappa:.3g} "
            f"finite_diff={fd:.12g} formula={exact:.12g} abs_err={err:.3e}"
        )
        assert exact < 0.0
    assert max_abs_err < 5e-6

    print("\n=== sign-symmetrized full-objective bank ===")
    p, d = 4, 2
    lam = np.array([5.0, 3.0, 1.7, 0.8])
    rng = np.random.default_rng(20260916)
    base = rng.standard_normal((32768, p)) * np.sqrt(lam)
    signs = np.array(list(itertools.product([-1.0, 1.0], repeat=p)))
    X = (base[:, None, :] * signs[None, :, :]).reshape(-1, p)

    def objective(U: np.ndarray) -> float:
        Y = X @ U.T
        sq = Y * Y
        return float(np.mean(np.partition(sq, -d, axis=1)[:, -d:].sum(axis=1)))

    pairs = list(itertools.combinations(range(p), 2))
    Es = [Eij(p, i, j) for i, j in pairs]
    F0 = objective(np.eye(p))
    h2 = 0.05
    curvatures = []
    for pair, E in zip(pairs, Es):
        fp = objective(expm(h2 * E))
        fm = objective(expm(-h2 * E))
        curv = (fp - 2.0 * F0 + fm) / h2**2
        curvatures.append(curv)
        print(f"pair={pair} centered_curvature={curv:.9g}")
        assert curv < 0.0

    print("\n=== mixed Hessian entries ===")
    h3 = 0.02
    max_mix = 0.0
    for a in range(len(Es)):
        for b in range(a + 1, len(Es)):
            Ea, Eb = Es[a], Es[b]
            pp = objective(expm(h3 * (Ea + Eb)))
            pm = objective(expm(h3 * (Ea - Eb)))
            mp = objective(expm(h3 * (-Ea + Eb)))
            mm = objective(expm(-h3 * (Ea + Eb)))
            mix = (pp - pm - mp + mm) / (4.0 * h3**2)
            max_mix = max(max_mix, abs(mix))
            print(f"pairs={pairs[a]},{pairs[b]} mixed={mix:.3e}")
    assert max_mix < 2e-8

    print("\nPASS")
    print(f"conditional_max_abs_error={max_abs_err:.3e}")
    print(f"largest_mixed_abs={max_mix:.3e}")
    print(f"least_negative_pair_curvature={max(curvatures):.9g}")
    print(f"samples_after_sign_symmetrization={len(X)}")


if __name__ == "__main__":
    main()
