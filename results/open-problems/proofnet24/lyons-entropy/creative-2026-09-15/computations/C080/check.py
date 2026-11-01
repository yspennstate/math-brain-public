"""C080 exact-identity and normal-form diagnostics; no numerical proof claims.

Run from the campaign root with: python computations/C080/check.py
The singular atoms are evaluated by their exact low-rank formulas, so tiny
endpoint eigenvalues are not reconstructed from rounded determinants.
"""
import json
import math
from pathlib import Path

import numpy as np


rng = np.random.default_rng(20260915)
w = np.array([1, 1, 1, 0], dtype=complex) / math.sqrt(3)
T = np.column_stack((
    np.array([1, -1, 0, 0]) / math.sqrt(2),
    np.array([1, 1, -2, 0]) / math.sqrt(6),
)).astype(complex)
M = np.array([[.37, .04 + .07j], [.04 - .07j, .61]])
N = np.eye(2) - M
mi, ni = np.linalg.inv(M), np.linalg.inv(N)
d, d0 = np.linalg.det(M).real, np.linalg.det(N).real


def hermitian_form(fun, basis):
    diagonal = np.array([fun(A) for A in basis])
    H = np.diag(diagonal)
    for i in range(len(basis)):
        for j in range(i):
            H[i, j] = H[j, i] = (
                fun(basis[i] + basis[j]) - diagonal[i] - diagonal[j]
            ) / 2
    return (H + H.T) / 2


def determinant_jets(D, A, sign=1):
    p = sign * np.linalg.det(D).real
    R = np.linalg.solve(D, A)
    tr = np.trace(R).real
    return p, p * tr, p * (tr * tr - np.trace(R @ R).real)


def atom_jets(K, A, mask):
    D = K - np.diag([0 if mask >> i & 1 else 1 for i in range(4)])
    return determinant_jets(D, A, (-1) ** (4 - mask.bit_count()))


def entropy_jet(jet):
    p, g, f = jet
    assert p > 0
    return -g * g / p - f * math.log(p)


def setup(z, V):
    U = np.column_stack((z, w, V))
    assert np.linalg.norm(U.conj().T @ U - np.eye(4)) < 2e-14
    v4 = V[3, :]
    s = abs(z[3]) ** 2
    shift = v4.conj() / z[3].conjugate()
    F0 = T.conj().T @ (np.outer(z, z.conj()) + V @ N @ V.conj().T) @ T
    D0 = np.linalg.det(F0).real

    def kernel(e, h):
        return e * np.outer(z, z.conj()) + (1 - h) * np.outer(w, w.conj()) + V @ M @ V.conj().T

    def unpack(A):
        return A[0, 0].real, A[1, 1].real, A[0, 1], A[2:, 0], A[2:, 1], A[2:, 2:]

    def singular(e, h, A):
        a, b, u, x, y, B = unpack(A)
        t = np.trace(mi @ B).real
        t0 = np.trace(ni @ B).real
        db = np.linalg.det(B).real
        q = e * (1 - h) * d
        qg = d * ((1 - h) * a + e * b + e * (1 - h) * t)
        qf = 2 * d * (
            a * b + (1 - h) * a * t + e * b * t - abs(u) ** 2
            - (1 - h) * np.vdot(x, mi @ x).real
            - e * np.vdot(y, mi @ y).real
        ) + 2 * e * (1 - h) * db
        q0 = h * (1 - e) * d0
        q0g = -d0 * (h * a + (1 - e) * b + h * (1 - e) * t0)
        q0f = 2 * d0 * (
            a * b + h * a * t0 + (1 - e) * b * t0 - abs(u) ** 2
            - h * np.vdot(x, ni @ x).real
            - (1 - e) * np.vdot(y, ni @ y).real
        ) + 2 * h * (1 - e) * db

        Am = U @ A @ U.conj().T
        F = T.conj().T @ ((1 - e) * np.outer(z, z.conj()) + V @ N @ V.conj().T) @ T
        fi = np.linalg.inv(F)
        D = np.linalg.det(F).real
        C = T.conj().T @ Am @ T
        f = T.conj().T @ Am @ w
        tF = np.trace(fi @ C).real
        R = h * D
        Rg = -D * (b + h * tF)
        Rf = 2 * D * (b * tF - np.vdot(f, fi @ f).real) + 2 * h * np.linalg.det(C).real
        theta = (1 - e) * d0 / D
        thetag = theta * (-a / (1 - e) - t0 + tF)
        split = -R * thetag * thetag / (theta * (1 - theta)) - q0f * math.log(theta) - (Rf - q0f) * math.log1p(-theta)
        return (q, qg, qf), (q0, q0g, q0f), (R, Rg, Rf), split

    def regular(e, h, A):
        K, Am = kernel(e, h), U @ A @ U.conj().T
        return sum(entropy_jet(atom_jets(K, Am, mask)) for mask in range(16) if mask not in (0, 8, 15))

    def grouped(e, h, A):
        q, q0, R, split = singular(e, h, A)
        return regular(e, h, A) + entropy_jet(q) + entropy_jet(R) + split

    def parameter_matrix(p, e=math.exp(-1), h=math.exp(-1), scaled=True):
        Le, Lh = -math.log(e), -math.log(h)
        a = p[0] * (math.sqrt(e) if scaled else 1)
        b = p[1] * (math.sqrt(h) if scaled else 1)
        u = complex(p[2], p[3]) / (math.sqrt(Le) if scaled else 1)
        x = np.array([complex(p[4], p[5]), complex(p[6], p[7])]) / (math.sqrt(Le) if scaled else 1)
        r = np.array([complex(p[8], p[9]), complex(p[10], p[11])]) / (math.sqrt(Lh) if scaled else 1)
        y = shift * u + r
        B = np.array([[p[12], complex(p[14], p[15]) / math.sqrt(2)], [complex(p[14], -p[15]) / math.sqrt(2), p[13]]])
        A = np.zeros((4, 4), dtype=complex)
        A[0, 0], A[1, 1], A[0, 1], A[1, 0] = a, b, u, u.conjugate()
        A[2:, 0], A[0, 2:] = x, x.conj()
        A[2:, 1], A[1, 2:] = y, y.conj()
        A[2:, 2:] = B
        return A

    parameter_basis = np.eye(16)
    active_basis = [parameter_matrix(p, scaled=False) for p in parameter_basis[12:]]
    face = hermitian_form(lambda A: regular(0, 0, A), active_basis)

    def principal(p):
        chi = complex(p[2], p[3])
        xi = np.array([complex(p[4], p[5]), complex(p[6], p[7])])
        upsilon = np.array([complex(p[8], p[9]), complex(p[10], p[11])])
        f = T.conj().T @ V @ upsilon
        return (
            -d * p[0] ** 2 - D0 * p[1] ** 2 - 2 * d * abs(chi) ** 2
            - 2 * d * np.vdot(xi, mi @ xi).real
            - 2 * D0 * np.vdot(f, np.linalg.solve(F0, f)).real
            + p[12:] @ face @ p[12:]
        )

    limit = hermitian_form(principal, list(parameter_basis))
    max_jet_error = 0.0
    max_grouping_error = 0.0
    for e, h in [(.07, .12), (.17, .03)]:
        K = kernel(e, h)
        for _ in range(12):
            A = parameter_matrix(rng.normal(size=16), scaled=False)
            Am = U @ A @ U.conj().T
            q, q0, R, split = singular(e, h, A)
            direct = [atom_jets(K, Am, 15), atom_jets(K, Am, 0), determinant_jets((np.eye(4) - K)[:3, :3], -Am[:3, :3])]
            for actual, expected in zip((q, q0, R), direct):
                max_jet_error = max(max_jet_error, max(abs(a - b) for a, b in zip(actual, expected)))
            q4 = tuple(a - b for a, b in zip(R, q0))
            max_jet_error = max(max_jet_error, max(abs(a - b) for a, b in zip(q4, atom_jets(K, Am, 8))))
            raw = sum(entropy_jet(atom_jets(K, Am, mask)) for mask in range(16))
            max_grouping_error = max(max_grouping_error, abs(raw - grouped(e, h, A)))

    K0 = kernel(0, 0)
    probs = {mask: atom_jets(K0, np.eye(4), mask)[0] for mask in range(16) if mask not in (0, 8, 15)}
    H_a = -sum(abs(t) ** 2 * math.log(abs(t) ** 2) for t in w if abs(t) > 1e-14)
    H_b = -sum(abs(t) ** 2 * math.log(abs(t) ** 2) for t in z)
    Lambda = -math.log(d * d0) + H_a + H_b
    active_minors = []
    for i in range(4):
        for j in range(i):
            edge = w[i] * V[j, :] - w[j] * V[i, :]
            Lambda += np.vdot(edge, edge).real * math.log(probs[(1 << i) + (1 << j)])
            active_minors.append(abs(np.linalg.det(V[[i, j], :])) ** 2)
    gaps = []
    for k in range(3):
        others = [i for i in range(3) if i != k]
        gaps.append(math.log(probs[(1 << k) + (1 << others[0])] * probs[(1 << k) + (1 << others[1])] / (probs[1 << k] * probs[7])))
    triangle_bound = s * sum(abs(w[k]) ** 2 * gaps[k] for k in range(3))
    universal_bound = 3 * s * min(abs(w[:3]) ** 2) * math.log(4 / 3)

    rows = []
    for pe, ph in [(3, 3), (6, 6), (12, 12), (60, 60), (3, 60), (6, 120), (12, 240), (60, 3), (120, 6), (240, 12)]:
        e, h = 10.0 ** (-pe), 10.0 ** (-ph)
        bs = [parameter_matrix(p, e, h) for p in parameter_basis]
        H = hermitian_form(lambda A: grouped(e, h, A), bs)
        rows.append({
            "epsilon": f"1e-{pe}", "eta": f"1e-{ph}",
            "maximum_scaled_hessian_eigenvalue": float(np.linalg.eigvalsh(H)[-1]),
            "operator_norm_error_from_limit": float(np.linalg.norm(H - limit, 2)),
        })

    assert max_jet_error < 1e-10
    assert max_grouping_error < 1e-9
    assert Lambda >= triangle_bound - 1e-12 >= universal_bound - 1e-12
    assert sum(gaps) >= 3 * math.log(4 / 3) - 1e-12
    assert np.linalg.eigvalsh(face)[-1] < 0
    assert all(row["maximum_scaled_hessian_eigenvalue"] < 0 for row in rows)
    return {
        "z": [[float(t.real), float(t.imag)] for t in z],
        "min_active_minor_square": float(min(active_minors)),
        "min_regular_boundary_atom": float(min(probs.values())),
        "maximum_jet_absolute_error": max_jet_error,
        "maximum_grouping_absolute_error": max_grouping_error,
        "Lambda": float(Lambda),
        "triangle_weighted_bound": float(triangle_bound),
        "explicit_strictness_bound": float(universal_bound),
        "sum_triangle_log_gaps": float(sum(gaps)),
        "maximum_active_face_hessian_eigenvalue": float(np.linalg.eigvalsh(face)[-1]),
        "maximum_limit_form_eigenvalue": float(np.linalg.eigvalsh(limit)[-1]),
        "samples": rows,
    }


examples = {
    "zero_active_minor": (
        np.array([1, 1, -2, 2], dtype=complex) / math.sqrt(10),
        np.column_stack((np.array([1, -1, 0, 0]) / math.sqrt(2), np.array([1, 1, -2, -3]) / math.sqrt(15))).astype(complex),
    ),
    "all_active_minors_positive": (
        np.array([1, 2, -3, 4], dtype=complex) / math.sqrt(30),
        np.column_stack((np.array([5, -4, -1, 0]) / math.sqrt(42), np.array([2, 4, -6, -7]) / math.sqrt(105))).astype(complex),
    ),
}
results = {"status": "Floating-point identity and convergence diagnostics only. The theorem is proved analytically.", "examples": {name: setup(*frame) for name, frame in examples.items()}}
Path(__file__).with_name("results.json").write_text(json.dumps(results, indent=2) + "\n")
print(json.dumps(results, indent=2))
