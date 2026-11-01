"""C006: determinant Hessian versus the product-resampling KL identity.

Run with Python 3 and numpy. The random checks supplement the analytic proof;
the two-mode obstruction is also checked with exact Fraction arithmetic.
"""

from fractions import Fraction as F
import json
from pathlib import Path

import numpy as np


def entropy(p):
    p = np.asarray(p, float)
    return float(-np.dot(p[p > 0], np.log(p[p > 0])))


def reset(p, i, d):
    q = np.zeros_like(p)
    bit = 1 << i
    for x in range(len(p)):
        if x & bit == 0:
            mass = p[x] + p[x | bit]
            q[x] = (1 - d) * mass
            q[x | bit] = d * mass
    return q


def noise(p, eta, diagonal):
    q = p.copy()
    for i, d in enumerate(diagonal):
        q = eta * q + (1 - eta) * reset(q, i, d)
    return q


def atoms_and_derivatives(kernel, direction):
    n = len(kernel)
    eye = np.eye(n)
    p = np.empty(1 << n)
    v = np.empty_like(p)
    w = np.empty_like(p)
    for x in range(1 << n):
        selected = np.array([(x >> j) & 1 for j in range(n)], dtype=bool)
        matrix = np.where(selected[None, :], kernel, eye - kernel)
        tangent = direction * (2 * selected - 1)[None, :]
        value = np.linalg.det(matrix).real
        ratio = np.linalg.solve(matrix, tangent)
        trace = np.trace(ratio)
        p[x] = value
        v[x] = (value * trace).real
        w[x] = (value * (trace * trace - np.trace(ratio @ ratio))).real
    return p, v, w


def jeffreys_derivative(p, q, u, v):
    ratio_log = np.log(p / q)
    return float(np.dot(u, ratio_log + 1 - q / p)
                 + np.dot(v, -ratio_log + 1 - p / q))


def decomposition(p, diagonal):
    n = len(diagonal)
    resets = [reset(p, i, d) for i, d in enumerate(diagonal)]
    chi = sum(float(np.sum((p - q) ** 2 / p)) for q in resets)
    cross = []
    for i, q in enumerate(resets):
        for j, d in enumerate(diagonal):
            if i != j:
                u = resets[j] - p
                v = reset(q, j, d) - q
                cross.append(-jeffreys_derivative(p, q, u, v))
    return chi, sum(cross), min(cross, default=0.0)


def random_verification():
    rng = np.random.default_rng(600620260915)
    max_atom_error = 0.0
    max_hessian_error = 0.0
    minimum_cross_dissipation = float("inf")
    maximum_hessian = -float("inf")
    samples = 0
    for n in range(2, 7):
        for _ in range(32):
            z = rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n))
            unitary, _ = np.linalg.qr(z)
            kernel = (unitary * rng.uniform(.12, .88, n)) @ unitary.conj().T
            diagonal = rng.uniform(.12, .88, n)
            target = np.diag(diagonal)
            eta = rng.uniform(.08, .92)
            direction = kernel - target
            at = target + eta * direction
            p, v, w = atoms_and_derivatives(at, direction)
            original, _, _ = atoms_and_derivatives(kernel, np.zeros_like(kernel))
            max_atom_error = max(max_atom_error,
                                 float(np.max(np.abs(p - noise(original, eta, diagonal)))))
            hessian = -float(np.sum(v * v / p) + np.dot(w, np.log(p)))
            chi, cross, min_cross = decomposition(p, diagonal)
            error = abs(-eta * eta * hessian - chi - cross)
            max_hessian_error = max(max_hessian_error, error)
            minimum_cross_dissipation = min(minimum_cross_dissipation, min_cross)
            maximum_hessian = max(maximum_hessian, hessian)
            samples += 1
    assert max_atom_error < 1e-12
    assert max_hessian_error < 1e-10
    assert minimum_cross_dissipation > -1e-12
    assert maximum_hessian < 0
    return dict(samples=samples, dimensions=list(range(2, 7)),
                max_atom_error=max_atom_error,
                max_hessian_identity_error=max_hessian_error,
                minimum_cross_dissipation=minimum_cross_dissipation,
                maximum_entropy_hessian=maximum_hessian)


def two_mode(a, c):
    return [(1 - a) ** 2 - c ** 2,
            a * (1 - a) + c ** 2,
            a * (1 - a) + c ** 2,
            a ** 2 - c ** 2]


def exact_obstruction():
    center = two_mode(F(1, 2), F(1, 4))
    minus = two_mode(F(3, 8), F(1, 4))
    plus = two_mode(F(5, 8), F(1, 4))
    mixture = [(a + b) / 2 for a, b in zip(minus, plus)]
    assert center == [F(3, 16), F(5, 16), F(5, 16), F(3, 16)]
    assert mixture == [F(13, 64), F(19, 64), F(19, 64), F(13, 64)]
    assert center[0] < mixture[0] < F(1, 4)
    fisher = F(32, 3)
    acceleration = 4 * np.log(3 / 5)
    hessian = -float(fisher) - acceleration
    center_eigenvalues = [F(3, 16), F(3, 16), F(9, 16), F(1, 16)]
    mixture_eigenvalues = [F(13, 64), F(13, 64), F(35, 64), F(3, 64)]
    assert sum(center_eigenvalues) == sum(mixture_eigenvalues) == 1
    return {
        "center_atoms": list(map(str, center)),
        "minus_atoms": list(map(str, minus)),
        "plus_atoms": list(map(str, plus)),
        "mixture_atoms": list(map(str, mixture)),
        "measured_mixture_minus_gaussian_entropy": entropy(mixture) - entropy(center),
        "quantum_gaussian_minus_mixture_entropy": entropy(center_eigenvalues)
                                                   - entropy(mixture_eigenvalues),
        "lyons_midpoint_gap": entropy(center) - .5 * (entropy(minus) + entropy(plus)),
        "classical_and_quantum_fisher": str(fisher),
        "acceleration_log_pairing": float(acceleration),
        "measured_entropy_hessian": hessian,
        "coherence_entropy_hessian": -float(acceleration),
    }


if __name__ == "__main__":
    result = {"random_determinant_checks": random_verification(),
              "exact_two_mode_certificate": exact_obstruction()}
    path = Path(__file__).with_name("results.json")
    path.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))
