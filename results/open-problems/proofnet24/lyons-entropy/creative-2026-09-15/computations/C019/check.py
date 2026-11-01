#!/usr/bin/env python3
"""C019: numerical checks of proved identities, not a concavity proof.

Run: python computations/C019/check.py
Only writes results.json in this script's own directory.
"""
from pathlib import Path
import itertools
import json
import math

import numpy as np


def real(x):
    if abs(np.imag(x)) > 2e-10:
        raise AssertionError(f"Unexpected imaginary residue: {x}")
    return float(np.real(x))


def support_frame(u):
    columns = []
    for e in np.eye(3, dtype=complex):
        v = e - u * np.vdot(u, e)
        for w in columns:
            v -= w * np.vdot(w, v)
        if np.linalg.norm(v) > 1e-10:
            columns.append(v / np.linalg.norm(v))
        if len(columns) == 2:
            break
    U = np.column_stack(columns)
    assert np.linalg.norm(U.conj().T @ U - np.eye(2)) < 1e-13
    assert np.linalg.norm(U.conj().T @ u) < 1e-13
    return U


def hermitian_basis(n):
    out = []
    for i in range(n):
        A = np.zeros((n, n), complex)
        A[i, i] = 1
        out.append(A)
    for i in range(n):
        for j in range(i + 1, n):
            A = np.zeros((n, n), complex)
            A[i, j] = A[j, i] = 1 / math.sqrt(2)
            out.append(A)
            A = np.zeros((n, n), complex)
            A[i, j] = 1j / math.sqrt(2)
            A[j, i] = -1j / math.sqrt(2)
            out.append(A)
    return out


def adapted_basis(u, U):
    # Order: one normal, four mixing, four supported tangent modes.
    basis = [np.outer(u, u.conj())]
    for w in U.T:
        V = np.outer(w, u.conj())
        basis.append((V + V.conj().T) / math.sqrt(2))
        basis.append(1j * (V - V.conj().T) / math.sqrt(2))
    basis += [U @ B @ U.conj().T for B in hermitian_basis(2)]
    gram = [[real(np.trace(A @ B)) for B in basis] for A in basis]
    assert np.linalg.norm(np.array(gram) - np.eye(9)) < 1e-12
    return basis


def regular_hessian(K, basis):
    """Seven-atom regular form (8), using polynomial det derivatives."""
    H = np.zeros((len(basis), len(basis)))
    min_atom = 1.0
    for flags in itertools.product((False, True), repeat=3):
        if all(flags):
            continue
        V = K - np.diag([0 if bit else 1 for bit in flags])
        sign = (-1) ** (3 - sum(flags))
        p = sign * real(np.linalg.det(V))
        if p <= 0:
            raise AssertionError(f"Nonpositive regular atom: {p}")
        min_atom = min(min_atom, p)
        trV = real(np.trace(V))
        adj = V @ V - trV * V
        adj += ((trV * trV - real(np.trace(V @ V))) / 2) * np.eye(3)
        g = np.array([sign * real(np.trace(adj @ A)) for A in basis])
        h = np.zeros_like(H)
        for i, A in enumerate(basis):
            trA = real(np.trace(A))
            for j, B in enumerate(basis):
                trB = real(np.trace(B))
                h[i, j] = sign * (
                    trV * (trA * trB - real(np.trace(A @ B)))
                    - trA * real(np.trace(V @ B))
                    - trB * real(np.trace(V @ A))
                    + real(np.trace(V @ (A @ B + B @ A)))
                )
        H -= np.outer(g, g) / p + math.log(p) * h
    return (H + H.T) / 2, min_atom


def decomposition(u, U, basis):
    # Use the exact intended adapted coordinates. Projecting back in floating
    # point would leak O(machine epsilon) tangent components into the normal
    # coordinate, which is then multiplied by 1/eps for the smallest eps values.
    assert len(basis) == 9
    a = np.zeros(9)
    a[0] = 1
    v = np.zeros((9, 2), complex)
    for k in range(2):
        v[1 + 2 * k, k] = 1 / math.sqrt(2)
        v[2 + 2 * k, k] = 1j / math.sqrt(2)
    B = np.zeros((9, 2, 2), complex)
    B[5:] = hermitian_basis(2)
    assert max(abs(real(np.vdot(u, A @ u)) - a[i]) for i, A in enumerate(basis)) < 1e-13
    assert max(np.linalg.norm(U.conj().T @ A @ u - v[i]) for i, A in enumerate(basis)) < 1e-13
    assert max(np.linalg.norm(U.conj().T @ A @ U - B[i]) for i, A in enumerate(basis)) < 1e-13
    return a, v, B


def full_hessian(u, U, J2, eps, basis):
    J = U @ J2 @ U.conj().T
    K = J + eps * np.outer(u, u.conj())
    H, min_atom = regular_hessian(K, basis)
    d = real(np.linalg.det(J2))
    invJ = np.linalg.inv(J2)
    a, v, B = decomposition(u, U, basis)
    t = np.array([real(np.trace(invJ @ b)) for b in B])
    grad = d * a + eps * d * t
    hess = np.empty_like(H)
    for i in range(9):
        for j in range(9):
            det2hess = (
                real(np.trace(B[i])) * real(np.trace(B[j]))
                - real(np.trace(B[i] @ B[j]))
            )
            hess[i, j] = d * (
                a[i] * t[j] + a[j] * t[i]
                - 2 * float(np.real(np.vdot(v[i], invJ @ v[j])))
            ) + eps * det2hess
    p = eps * d
    H -= np.outer(grad, grad) / p + math.log(p) * hess
    return (H + H.T) / 2, min_atom


def predicted_limit(u, U, J2, basis):
    J = U @ J2 @ U.conj().T
    tangent, min_atom = regular_hessian(J, basis[5:])
    limit = np.zeros((9, 9))
    d = real(np.linalg.det(J2))
    invJ = np.linalg.inv(J2)
    _, v, _ = decomposition(u, U, basis)
    limit[0, 0] = -d
    for i in range(1, 5):
        for j in range(1, 5):
            limit[i, j] = -2 * d * float(np.real(np.vdot(v[i], invJ @ v[j])))
    limit[5:, 5:] = tangent
    return limit, tangent, min_atom


def analytic_isotropic_tangent(u, U, s, basis):
    q = np.abs(u) ** 2
    r = 1 - q
    lam = float(np.sum(r * np.log(r) - q * np.log(q)))
    T = np.empty((4, 4))
    for i, A in enumerate(basis[5:]):
        for j, B in enumerate(basis[5:]):
            diagonal_fisher = sum(
                real(A[k, k]) * real(B[k, k]) / r[k] for k in range(3)
            ) / (s * (1 - s))
            T[i, j] = -diagonal_fisher + lam * (
                real(np.trace(A)) * real(np.trace(B))
                - real(np.trace(A @ B))
            )
    return T, lam


def main():
    q = np.array([1 / 2, 1 / 3, 1 / 6])
    phases = np.array([0.0, 0.31, -0.77])
    u = np.sqrt(q) * np.exp(1j * phases)
    U = support_frame(u)
    basis = adapted_basis(u, U)
    s = 0.37
    isotropic = s * np.eye(2)
    perturbation = np.array([[0.03, 0.02 + 0.01j], [0.02 - 0.01j, -0.02]])
    cases = [("isotropic_nonexchangeable", isotropic),
             ("unequal_surviving_eigenvalues", isotropic + perturbation)]
    records = []
    for name, J2 in cases:
        limit, tangent, min_atom = predicted_limit(u, U, J2, basis)
        row = {
            "case": name,
            "surviving_eigenvalues": np.linalg.eigvalsh(J2).tolist(),
            "minimum_regular_boundary_atom": min_atom,
            "tangent_eigenvalues": np.linalg.eigvalsh(tangent).tolist(),
            "limit_eigenvalues": np.linalg.eigvalsh(limit).tolist(),
            "epsilon_sweep": [],
        }
        if name.startswith("isotropic"):
            T_exact, lam = analytic_isotropic_tangent(u, U, s, basis)
            discrepancy = float(np.linalg.norm(T_exact - tangent, ord=2))
            assert discrepancy < 5e-12
            assert np.linalg.eigvalsh(tangent)[-1] <= -lam + 1e-12
            row["lambda_q"] = lam
            row["q_product_lower_bound"] = float(np.prod(q))
            row["tangent_formula_operator_error"] = discrepancy
        for eps in [1e-2, 1e-4, 1e-8, 1e-16, 1e-32]:
            H, atom_min = full_hessian(u, U, J2, eps, basis)
            L = math.log(1 / eps)
            scales = np.array([math.sqrt(eps)] + [1 / math.sqrt(L)] * 4 + [1.0] * 4)
            scaled = H * np.outer(scales, scales)
            error = float(np.linalg.norm(scaled - limit, ord=2))
            max_scaled = float(np.linalg.eigvalsh(scaled)[-1])
            row["epsilon_sweep"].append({
                "epsilon": eps,
                "scaled_normal_form_operator_error": error,
                "maximum_scaled_hessian_eigenvalue": max_scaled,
                "minimum_regular_atom": atom_min,
            })
            assert max_scaled < 0
        assert row["epsilon_sweep"][-1]["scaled_normal_form_operator_error"] < row["epsilon_sweep"][0]["scaled_normal_form_operator_error"]
        records.append(row)
    output = {
        "status": "PASS: numerical identity and asymptotic checks only",
        "q": q.tolist(),
        "phases": phases.tolist(),
        "notes": [
            "All Hessians are with respect to affine Hermitian K directions.",
            "The full atom is evaluated analytically, including its derivatives.",
            "Scaled Hessian negativity is numerically equivalent by congruence to full Hessian negativity.",
            "Finite numerical checks do not prove the uniform theorem or the general conjecture.",
        ],
        "cases": records,
    }
    path = Path(__file__).with_name("results.json")
    path.write_text(json.dumps(output, indent=2) + "\n")
    print(json.dumps(output, indent=2))


if __name__ == "__main__":
    main()
