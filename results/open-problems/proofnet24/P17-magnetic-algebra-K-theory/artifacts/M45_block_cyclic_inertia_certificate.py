#!/usr/bin/env python3
"""ProofNet24 P17 M45 structural certificate checker.

Supports the exact algebraic claims:
  P17-M45-SPARSE-HERMITIAN-LINEARIZATION-INERTIA-41
  P17-M45-CYCLIC-BLOCK-SCHUR-INERTIA-41

The script is a finite sanity checker, not the proof and not a magnetic-gap
certificate.  It verifies on deterministic small Hermitian block-cyclic examples:

1. For H(B) = [[0,B*],[B,0]] and t>0 away from singular values,
       nu_-(H(B)-tI) = N + #{s_j(B)<t}.

2. For a Hermitian cyclic block-tridiagonal matrix M=T+U W U*, where T is
   the open chain and W is the invertible wrap block, Haynsworth/Schur
   complement additivity gives
       nu_-(M) = nu_-(T) + nu_+(W^{-1}+U*T^{-1}U) - nu_+(W^{-1}).
   In the P17 wrap geometry nu_+(W^{-1})=m.

3. The open-chain inertia is the sum of the inertias of the block Schur pivots
       S_0=D_0,
       S_k=D_k-E_{k-1} S_{k-1}^{-1} E_{k-1}*.

For the actual doubled P17 target the dimensions are L=306, m=148,
L*m=45288, and the wrap correction is only 2m=296 dimensional.

No floating result from this script is promoted to a spectral theorem.
"""

from __future__ import annotations

import numpy as np


def inertia(a: np.ndarray, tol: float = 1e-10) -> tuple[int, int, int]:
    ev = np.linalg.eigvalsh(a)
    return (
        int(np.count_nonzero(ev > tol)),
        int(np.count_nonzero(ev < -tol)),
        int(np.count_nonzero(np.abs(ev) <= tol)),
    )


def linearization_test(seed: int) -> None:
    rng = np.random.default_rng(seed)
    n = 7
    b = rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n))
    s = np.linalg.svd(b, compute_uv=False)
    # Pick a threshold strictly between two ordered singular values.
    ss = np.sort(s)
    t = float((ss[2] + ss[3]) / 2)
    h = np.block(
        [
            [np.zeros((n, n), dtype=complex), b.conj().T],
            [b, np.zeros((n, n), dtype=complex)],
        ]
    )
    neg = inertia(h - t * np.eye(2 * n))[1]
    expected = n + int(np.count_nonzero(s < t))
    assert neg == expected, (seed, neg, expected)


def block_cyclic_test(seed: int) -> None:
    rng = np.random.default_rng(seed)
    l = 5
    m = 3

    ds: list[np.ndarray] = []
    for k in range(l):
        x = rng.normal(size=(m, m)) + 1j * rng.normal(size=(m, m))
        d = (x + x.conj().T) / 2 + (2.5 + 0.2 * k) * np.eye(m)
        ds.append(d)

    es: list[np.ndarray] = []
    for k in range(l - 1):
        z = (0.18 + 0.03 * k) + 1j * (0.02 + 0.01 * k)
        es.append(z * np.eye(m))

    n = l * m
    t_open = np.zeros((n, n), dtype=complex)
    for k, d in enumerate(ds):
        sl = slice(k * m, (k + 1) * m)
        t_open[sl, sl] = d
    for k, e in enumerate(es):
        sl0 = slice(k * m, (k + 1) * m)
        sl1 = slice((k + 1) * m, (k + 2) * m)
        t_open[sl1, sl0] = e
        t_open[sl0, sl1] = e.conj().T

    q = 0.21 + 0.13j
    u = np.zeros((n, 2 * m), dtype=complex)
    u[0:m, 0:m] = np.eye(m)
    u[(l - 1) * m : l * m, m : 2 * m] = np.eye(m)
    w = np.block(
        [
            [np.zeros((m, m), dtype=complex), np.conj(q) * np.eye(m)],
            [q * np.eye(m), np.zeros((m, m), dtype=complex)],
        ]
    )
    full = t_open + u @ w @ u.conj().T

    # Open-chain block LDL/Schur recursion.
    pivots: list[np.ndarray] = [ds[0].copy()]
    for k, e in enumerate(es):
        prev = pivots[-1]
        pivots.append(ds[k + 1] - e @ np.linalg.solve(prev, e.conj().T))

    open_neg_from_pivots = sum(inertia(s)[1] for s in pivots)
    open_neg_direct = inertia(t_open)[1]
    assert open_neg_from_pivots == open_neg_direct

    schur = np.linalg.inv(w) + u.conj().T @ np.linalg.solve(t_open, u)
    predicted_neg = open_neg_direct + inertia(schur)[0] - inertia(np.linalg.inv(w))[0]
    direct_neg = inertia(full)[1]
    assert predicted_neg == direct_neg, (seed, predicted_neg, direct_neg)
    assert inertia(np.linalg.inv(w))[0] == m

    # Determinant/nonsingularity companion identity, checked numerically.
    sign_f, log_f = np.linalg.slogdet(full)
    sign_t, log_t = np.linalg.slogdet(t_open)
    sign_w, log_w = np.linalg.slogdet(w)
    sign_s, log_s = np.linalg.slogdet(schur)
    lhs = sign_f * np.exp(log_f)
    rhs = sign_t * sign_w * sign_s * np.exp(log_t + log_w + log_s)
    rel = abs(lhs - rhs) / max(1.0, abs(lhs), abs(rhs))
    assert rel < 1e-8, rel


def main() -> None:
    for seed in range(10):
        linearization_test(seed)
        block_cyclic_test(seed)

    l_actual = 306
    m_actual = 148
    print("M45 structural checks: PASS")
    print(f"actual doubled layers L={l_actual}")
    print(f"slice size m={m_actual}")
    print(f"full Hermitian dimension L*m={l_actual*m_actual}")
    print(f"wrap correction dimension 2m={2*m_actual}")
    print("No magnetic gap is claimed by this checker.")


if __name__ == "__main__":
    main()
