#!/usr/bin/env python3
"""Finite diagnostics for account03/B11 fixed-multiplicity audit.

This is not a proof. It checks the Schur pointwise singular-value inequality
and recomputes constants used in the audit.
"""
import math
import numpy as np

SEED = 20260924
rng = np.random.default_rng(SEED)

def schur(A, k):
    B = A[:k, :k]
    C = A[:k, k:]
    D = A[k:, k:]
    return D - C.T @ np.linalg.solve(B, C)

def svals_sym(A):
    return np.sort(np.abs(np.linalg.eigvalsh(A)))[::-1]

def check_random():
    nonsingular_cases = 0
    singular_cases = 0
    max_excess_nonsingular = 0.0
    max_excess_singular = 0.0
    max_constructed_zero = 0.0

    for n in range(3, 10):
        for k in range(1, min(4, n)):
            for _ in range(300):
                R = rng.normal(size=(n, n))
                A = (R + R.T) / 2
                A[:k, :k] += np.diag(np.arange(1, k + 1) * 0.7 + 2.0)
                S = schur(A, k)
                sa, ss = svals_sym(A), svals_sym(S)
                for j in range(n-k):
                    max_excess_nonsingular = max(
                        max_excess_nonsingular, float(sa[j+k] - ss[j])
                    )
                nonsingular_cases += 1

    for n in range(4, 10):
        for k in range(1, min(4, n)):
            m = n-k
            for _ in range(150):
                R = rng.normal(size=(k, k))
                B = R @ R.T + np.eye(k)
                C = rng.normal(size=(k, m))
                T = rng.normal(size=(m, m))
                S = (T + T.T) / 2
                vals, U = np.linalg.eigh(S)
                vals[0] = 0.0
                S = U @ np.diag(vals) @ U.T
                D = S + C.T @ np.linalg.solve(B, C)
                A = np.block([[B, C], [C.T, D]])
                sa, ss = svals_sym(A), svals_sym(S)
                max_constructed_zero = max(max_constructed_zero, float(sa[-1]))
                for j in range(m):
                    max_excess_singular = max(
                        max_excess_singular, float(sa[j+k] - ss[j])
                    )
                singular_cases += 1

    return (nonsingular_cases, singular_cases,
            max_excess_nonsingular, max_excess_singular, max_constructed_zero)

def main():
    ns, sg, ex_ns, ex_sg, zerr = check_random()
    print("QFORM_B11_FIXEDMULT_SCHUR_VERIFY")
    print(f"seed={SEED}")
    print(f"nonsingular_cases={ns}")
    print(f"singular_cases={sg}")
    print(f"max_excess_nonsingular={ex_ns:.17g}")
    print(f"max_excess_singular={ex_sg:.17g}")
    print(f"max_abs_smallest_eigenvalue_constructed_singular={zerr:.17g}")
    print(f"no_pivot_k3_full_half_upper={12*math.sqrt(80*math.e):.15f}")
    print(f"no_pivot_k5_density_upper={800*math.e:.15f}")
    print(f"scalar_pivot_H={10*(20+12*math.log(16)):.15f}")
    print(f"definite_pair_H={40*math.pi:.15f}")
    print(f"main_indefinite_pair={10*(10+5*math.log(16))+1/math.e:.15f}")
    print(f"leverage_half_order3_density={480*math.sqrt(2)*math.e:.15f}")
    assert ex_ns <= 1e-10
    assert ex_sg <= 1e-10
    print("QFORM_B11_FIXEDMULT_SCHUR_VERIFY_PASS")

if __name__ == "__main__":
    main()
