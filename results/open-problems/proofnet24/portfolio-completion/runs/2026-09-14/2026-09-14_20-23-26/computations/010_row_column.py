"""Checks for Agent 010's proved row/column entropy-concavity lemma.

These floating-point checks verify formulas on selected examples; the proof is
in agents/010.md. They do not establish the full Lyons conjecture.
Run from the research-session root:
    python computations/010_row_column.py
"""

import itertools
import json

import numpy as np

from dpp_core import atom_matrices, direction_derivatives, random_contraction


def conditional_odds_gradient(K):
    """Distinguished coordinate is 0; return Q, g, complementary atom masses."""
    mats, _ = atom_matrices(K)
    p = np.linalg.det(mats).real
    half = len(p) // 2
    g = np.log(p[:half] / p[half:])
    C = K[1:, 1:]
    rest_mats, rest_signs = atom_matrices(C)
    r = np.linalg.det(rest_mats).real
    N = rest_mats * rest_signs[:, None, :]
    Q = np.einsum("s,sij->ij", r * g, np.linalg.inv(N))
    return (Q + Q.conj().T) / 2, g, r


def compound2(A):
    ix = np.array(list(itertools.combinations(range(len(A)), 2)))
    return (
        A[ix[:, 0, None], ix[None, :, 0]]
        * A[ix[:, 1, None], ix[None, :, 1]]
        - A[ix[:, 0, None], ix[None, :, 1]]
        * A[ix[:, 1, None], ix[None, :, 0]]
    )


def n3_supermodular_operator(K):
    mats, _ = atom_matrices(K)
    p = np.linalg.det(mats).real
    f = -np.log(p)
    bits = list(itertools.product([0, 1], repeat=3))
    f_by_set = {
        frozenset(i for i, b in enumerate(s) if b): value
        for s, value in zip(bits, f)
    }
    c = {}
    for size in range(4):
        for S_tuple in itertools.combinations(range(3), size):
            S = frozenset(S_tuple)
            c[S] = sum(
                (-1) ** (len(S) - len(T)) * f_by_set[T]
                for T in f_by_set
                if T <= S
            )
    D = np.diag([c[frozenset(S)] for S in itertools.combinations(range(3), 2)])
    # This extends polynomially to singular K, although these examples are interior.
    CK = np.linalg.det(K).real * compound2(np.linalg.inv(K))
    T = D + c[frozenset(range(3))] * CK
    return (T + T.conj().T) / 2


def main():
    rng = np.random.default_rng(20260914010)
    row_checks = []
    for n in (2, 3, 4, 5, 6):
        max_identity_error = 0.0
        minimum_Q_eigenvalue = float("inf")
        maximum_H2 = -float("inf")
        minimum_g_increment = float("inf")
        for _ in range(80):
            K = random_contraction(rng, n, complex_case=True)
            v = rng.normal(size=n - 1) + 1j * rng.normal(size=n - 1)
            A = np.zeros_like(K)
            A[0, 0] = rng.normal()
            A[1:, 0] = v
            A[0, 1:] = v.conj()
            Q, g, _ = conditional_odds_gradient(K)
            derivative = direction_derivatives(K, A)
            predicted_curvature = -2 * np.vdot(v, Q @ v).real
            max_identity_error = max(
                max_identity_error,
                abs(derivative["curvature"] - predicted_curvature),
            )
            minimum_Q_eigenvalue = min(
                minimum_Q_eigenvalue, float(np.linalg.eigvalsh(Q)[0])
            )
            maximum_H2 = max(maximum_H2, derivative["H2"])
            for mask in range(len(g)):
                for shift in range(n - 1):
                    if not mask & (1 << shift):
                        minimum_g_increment = min(
                            minimum_g_increment,
                            float(g[mask | (1 << shift)] - g[mask]),
                        )
        row_checks.append(
            dict(
                n=n,
                examples=80,
                maximum_curvature_identity_error=max_identity_error,
                minimum_Q_eigenvalue=minimum_Q_eigenvalue,
                minimum_discrete_g_increment=minimum_g_increment,
                maximum_entropy_second_derivative=maximum_H2,
            )
        )

    n3_error = 0.0
    n3_min_eigenvalue = float("inf")
    n3_max_H2 = -float("inf")
    for _ in range(200):
        K = random_contraction(rng, 3, complex_case=True)
        G = rng.normal(size=(3, 3)) + 1j * rng.normal(size=(3, 3))
        U, _ = np.linalg.qr(G)
        A = U @ np.diag([rng.uniform(0.2, 2), -rng.uniform(0.2, 2), 0]) @ U.conj().T
        T = n3_supermodular_operator(K)
        derivative = direction_derivatives(K, A)
        predicted = 2 * np.trace(T @ compound2(A)).real
        n3_error = max(n3_error, abs(predicted - derivative["curvature"]))
        n3_min_eigenvalue = min(n3_min_eigenvalue, float(np.linalg.eigvalsh(T)[0]))
        n3_max_H2 = max(n3_max_H2, derivative["H2"])

    K = np.array([[0.5, 0.25], [0.25, 0.5]])
    obstruction = direction_derivatives(K, np.eye(2))
    result = dict(
        seed=20260914010,
        row_column_checks=row_checks,
        n3_indefinite_rank_two_checks=dict(
            examples=200,
            maximum_curvature_identity_error=n3_error,
            minimum_operator_eigenvalue=n3_min_eigenvalue,
            maximum_entropy_second_derivative=n3_max_H2,
        ),
        positive_curvature_obstruction=dict(
            curvature=obstruction["curvature"],
            exact_curvature="4 log(5/3)",
            fisher=obstruction["fisher"],
            exact_fisher="32/3",
            H2=obstruction["H2"],
        ),
    )
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
