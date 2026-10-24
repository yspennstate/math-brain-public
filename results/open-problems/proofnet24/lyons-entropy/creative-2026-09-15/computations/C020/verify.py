#!/usr/bin/env python3
"""C020: exact constants and independent full-Hermitian Hessian diagnostics.

The proof is agents/C020.md. Numerical experiments are supplementary only.
The determinant routine below uses the six permutation terms, not matrix
inverses or the frozen-log Hessian formula.
"""
from fractions import Fraction as F
from itertools import combinations, permutations
from pathlib import Path
import json
import math
import numpy as np


PERMS = [(p, (-1) ** sum(p[i] > p[j] for i in range(3)
                         for j in range(i + 1, 3)))
         for p in permutations(range(3))]
EDGES = [(1, 2), (2, 0), (0, 1)]  # edge i is opposite vertex i


def determinant_taylor(Q, A):
    """Coefficients of det(Q+t*A), by explicit permutation multiplication."""
    out = [0j] * 4
    for p, sign in PERMS:
        coeff = [1 + 0j]
        for i in range(3):
            q, a = Q[i, p[i]], A[i, p[i]]
            nxt = [0j] * (len(coeff) + 1)
            for k, v in enumerate(coeff):
                nxt[k] += v * q
                nxt[k + 1] += v * a
            coeff = nxt
        for k, v in enumerate(coeff):
            out[k] += sign * v
    return np.real_if_close(np.array(out), tol=1000).real


def hermitian_basis():
    out = []
    for i in range(3):
        A = np.zeros((3, 3), complex)
        A[i, i] = 1
        out.append(A)
    for i, j in EDGES:
        for value in [1, 1j]:
            A = np.zeros((3, 3), complex)
            A[i, j] = value
            A[j, i] = np.conjugate(value)
            out.append(A)
    return out


BASIS = hermitian_basis()


def det_hessian(Q):
    diagonal = [2 * determinant_taylor(Q, A)[2] for A in BASIS]
    H = np.diag(diagonal)
    for i, j in combinations(range(9), 2):
        both = 2 * determinant_taylor(Q, BASIS[i] + BASIS[j])[2]
        H[i, j] = H[j, i] = (both - diagonal[i] - diagonal[j]) / 2
    return H


def compute(K):
    masses, gradients, atom_hessians = [], [], []
    for mask in range(8):
        Q = K.copy()
        size = mask.bit_count()
        for i in range(3):
            if not (mask >> i) & 1:
                Q[i, i] -= 1
        sign = (-1) ** (3 - size)
        masses.append(sign * determinant_taylor(Q, BASIS[0])[0])
        gradients.append([sign * determinant_taylor(Q, A)[1] for A in BASIS])
        atom_hessians.append(sign * det_hessian(Q))
    p = np.array(masses)
    assert np.min(p) > 0
    Dp = np.array(gradients)
    D2p = np.array(atom_hessians)
    fisher = Dp.T @ (Dp / p[:, None])
    H = -fisher - np.einsum('s,sij->ij', np.log(p), D2p)
    f = -np.log(p)
    tau = sum((-1) ** (3 - mask.bit_count()) * f[mask] for mask in range(8))
    pair = []
    for i, j in EDGES:
        pair.append(f[(1 << i) | (1 << j)] - f[1 << i] - f[1 << j] + f[0])
    M = np.diag(pair).astype(complex) + tau * K
    m = np.diag(M).real
    frozen = det_hessian(M)
    claimed_penalty = np.diag([2 / 19] * 3 +
                              [3 / 7 * m[i] for i in range(3) for _ in range(2)])
    return {
        'atom_sum_error': float(abs(p.sum() - 1)),
        'hessian_identity_error': float(np.max(np.abs(H + fisher - frozen))),
        'max_hessian_eigenvalue': float(np.linalg.eigvalsh(H)[-1]),
        'max_bound_remainder_eigenvalue': float(np.linalg.eigvalsh(H + claimed_penalty)[-1]),
        'tau': float(tau),
        'M_diagonal': m.tolist(),
        'minimum_atom': float(p.min()),
    }


def exact_constants():
    eta = F(2, 7)
    z = 3 * eta ** 2 + 2 * eta ** 3
    t = z / (2 - z)
    log_upper = 2 * (t + t ** 3 / (3 * (1 - t * t)))
    assert z == F(100, 343)
    assert t == F(50, 293)
    assert log_upper < F(7, 20)
    c = 1 - 2 * eta
    C = F(7, 5)
    frozen_upper = C * (2 + 2 * eta ** 2 / c)
    fisher_lower = 4 / (1 + 2 * eta ** 2)
    assert frozen_upper == F(10, 3)
    assert fisher_lower == F(196, 57)
    assert fisher_lower - frozen_upper == F(2, 19)
    return {k: str(v) for k, v in {
        'edge_ratio': eta, 'relative_atom_error': z,
        'atanh_parameter': t, 'rational_log_upper': log_upper,
        'log_upper_gap': F(7, 20) - log_upper,
        'frozen_diagonal_bound': frozen_upper,
        'fisher_diagonal_bound': fisher_lower,
        'diagonal_curvature_margin': fisher_lower - frozen_upper,
        'off_diagonal_coefficient': c,
    }.items()}


def exact_witness():
    """All eight masses are rational when real/imaginary entries are rational."""
    d = F(2, 5)
    # K23=2/25, K31=(3+4i)/100, K12=1/10.
    radii = [F(4, 625), F(1, 400), F(1, 100)]
    cycle_twice_real = F(3, 6250)
    p = []
    for mask in range(8):
        a = [d if (mask >> i) & 1 else d - 1 for i in range(3)]
        det = a[0] * a[1] * a[2] - sum(a[i] * radii[i] for i in range(3))
        det += cycle_twice_real
        p.append((-1) ** (3 - mask.bit_count()) * det)
    assert sum(p) == 1 and min(p) > 0
    even = math.prod(p[mask] for mask in range(8) if mask.bit_count() % 2 == 0)
    odd = math.prod(p[mask] for mask in range(8) if mask.bit_count() % 2 == 1)
    assert even != odd  # equivalent to tau != 0
    assert max(radii) <= (F(2, 7) * d) ** 2
    return {
        'masses_mask_order': [str(v) for v in p],
        'parity_product_ratio': str(even / odd),
        'tau_is_nonzero_exactly': True,
        'real_cycle_product': str(cycle_twice_real / 2),
    }


def main():
    K = np.array([[.4, .1, .03 - .04j],
                  [.1, .4, .08], [.03 + .04j, .08, .4]], complex)
    results = {
        'status': 'Exact arithmetic proves constants; finite Hessian runs are diagnostics.',
        'exact_constants': exact_constants(),
        'exact_outside_families_witness': exact_witness(),
        'witness_diagnostics': compute(K),
    }
    rng = np.random.default_rng(20260915020)
    cases = []
    # Include extreme common diagonals, unbalanced magnitudes, missing edges,
    # saturated radii, arbitrary phases, and general interior examples.
    for index in range(160):
        d = [1e-4, .01, .2, .4, .5, .6, .8, .99, .9999][index % 9]
        mu = min(d, 1 - d)
        magnitudes = (2 / 7) * mu * rng.random(3)
        if index % 4 == 0:
            magnitudes[index % 3] = 0
        if index % 7 == 0:
            magnitudes[(index + 1) % 3] *= 1e-5
        if index % 11 == 0:
            magnitudes[:] = (2 / 7) * mu
        phases = rng.uniform(-math.pi, math.pi, 3)
        K = d * np.eye(3, dtype=complex)
        for (i, j), radius, phase in zip(EDGES, magnitudes, phases):
            K[i, j] = radius * np.exp(1j * phase)
            K[j, i] = np.conjugate(K[i, j])
        case = compute(K)
        case['common_diagonal'] = d
        cases.append(case)
    max_remainder = max(c['max_bound_remainder_eigenvalue'] for c in cases)
    max_identity_error = max(c['hessian_identity_error'] for c in cases)
    assert max_remainder < 1e-8
    assert max_identity_error < 1e-8
    results['diagnostic_summary'] = {
        'sample_count': len(cases),
        'max_bound_remainder_eigenvalue': max_remainder,
        'max_hessian_identity_error': max_identity_error,
        'max_atom_sum_error': max(c['atom_sum_error'] for c in cases),
        'all_claimed_bounds_pass_numerical_tolerance': True,
    }
    path = Path(__file__).with_name('verification_results.json')
    path.write_text(json.dumps(results, indent=2) + '\n')
    print(json.dumps(results, indent=2))


if __name__ == '__main__':
    main()
