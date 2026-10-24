#!/usr/bin/env python3
from math import exp, factorial, log, sqrt
import numpy as np
from scipy.linalg import expm


def tv(mu, nu):
    return 0.5 * np.abs(mu - nu).sum()


def k4_kernel():
    A = np.ones((4, 4)) - np.eye(4)
    return A / 3.0


def poisson_common_clock_kernel(P, t, cutoff=120):
    n = P.shape[0]
    out = np.zeros((n * n, n * n))
    Pm = np.eye(n)
    for m in range(cutoff + 1):
        if m > 0:
            Pm = Pm @ P
        w = exp(-t) * (t ** m) / factorial(m)
        out += w * np.kron(Pm, Pm)
    return out


def check():
    # Exact constants for the degree-six, tensor-square application.
    d = 6
    k = 2
    D = d ** k
    rho = 2 * sqrt(d - 1) / d
    gap_lower = 1 - rho
    center_coeff_log5N = d / (k * (d - 2))
    Qball = (d - 1) ** k
    beta = 0.5 * (1 - log(Qball) / log(D - 1))

    assert D == 36
    assert abs(rho - sqrt(5) / 3) < 1e-15
    assert abs(gap_lower - (3 - sqrt(5)) / 3) < 1e-15
    assert abs(center_coeff_log5N - 0.75) < 1e-15
    assert Qball == 25
    assert D - 1 == 35
    assert beta > 0

    # Finite exact-structure sanity check on K4.  Its tensor square has kernel
    # P tensor P.  Salez continuous time is a single Poisson clock shared by
    # the two coordinates, not a product of independent CT semigroups.
    P = k4_kernel()
    n = P.shape[0]
    Q = np.kron(P, P)
    I = np.eye(n * n)
    pi = np.ones(n) / n
    pi2 = np.ones(n * n) / (n * n)

    evP = np.linalg.eigvalsh(P)
    evQ = np.linalg.eigvalsh(Q)
    products = np.sort(np.array([x * y for x in evP for y in evP]))
    assert np.max(np.abs(np.sort(evQ) - products)) < 1e-12

    for t in [0.2, 0.9, 2.5, 5.0]:
        H_direct = expm(t * (Q - I))
        H_clock = poisson_common_clock_kernel(P, t, cutoff=120)
        assert np.max(np.abs(H_direct - H_clock)) < 2e-12

        H_base = expm(t * (P - np.eye(n)))
        row = H_direct[0].reshape(n, n)
        marg0 = row.sum(axis=1)
        marg1 = row.sum(axis=0)
        assert np.max(np.abs(marg0 - H_base[0])) < 2e-12
        assert np.max(np.abs(marg1 - H_base[0])) < 2e-12

        d_tensor = tv(H_direct[0], pi2)
        d_base_ct = tv(H_base[0], pi)
        assert d_tensor + 1e-12 >= d_base_ct

        m0 = max(0, int(np.floor(t)))
        p_lt = sum(exp(-t) * (t ** m) / factorial(m) for m in range(m0))
        Pm0 = np.linalg.matrix_power(P, m0)
        d_disc = max(tv(Pm0[x], pi) for x in range(n))
        upper = p_lt + k * d_disc
        assert d_tensor <= upper + 1e-12

    print("SYNCHRONOUS_TENSOR_EXACT_CONSTANTS")
    print(f"d={d} k={k} output_degree={D}")
    print(f"ramanujan_abs_rho=sqrt(5)/3={rho:.15f}")
    print(f"gap_lower=(3-sqrt(5))/3={gap_lower:.15f}")
    print("cutoff_center=(3/4) log_5 N")
    print("cutoff_window=O(sqrt(log N))")
    print(f"ball_growth_base={Qball} LRE_benchmark_base={D-1}")
    print(f"non_LRE_beta={beta:.15f}")
    print("K4_TENSOR_SPECTRUM_PASS")
    print("COMMON_POISSON_CLOCK_IDENTITY_PASS")
    print("MARGINAL_SOURCE_CT_IDENTITY_PASS")
    print("TV_SANDWICH_FINITE_SANITY_PASS")
    print("ALL_EXACT_AND_SANITY_CHECKS_PASS")


if __name__ == "__main__":
    check()
