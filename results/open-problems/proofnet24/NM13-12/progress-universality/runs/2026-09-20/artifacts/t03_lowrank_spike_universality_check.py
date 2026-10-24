#!/usr/bin/env python3
import numpy as np

L = 6.30297437506
U = 12.78437096216
KAPPA = -1.0

def sqrtm_psd(S):
    w, V = np.linalg.eigh(S)
    return (V * np.sqrt(w)) @ V.T

def invsqrtm_pd(S):
    w, V = np.linalg.eigh(S)
    return (V * (1.0/np.sqrt(w))) @ V.T

def check_general_covariance_sandwich(seed=17, trials=200):
    rng = np.random.default_rng(seed)
    worst_lower = 1e9
    worst_upper = 1e9
    for _ in range(trials):
        N = 7
        M = 11
        G = rng.standard_normal((M, N))
        Q, _ = np.linalg.qr(rng.standard_normal((N, N)))
        eigs = np.linspace(0.7, 2.3, N)
        S = Q @ np.diag(eigs) @ Q.T
        Sh = sqrtm_psd(S)
        Sih = invsqrtm_pd(S)
        a = np.sqrt(eigs.min())
        b = np.sqrt(eigs.max())

        for _j in range(100):
            z = rng.standard_normal(N)
            z /= np.linalg.norm(z)

            if np.min(G @ z) >= KAPPA / b:
                x = Sih @ z
                x /= np.linalg.norm(x)
                margin = np.min(G @ (Sh @ x) - KAPPA)
                worst_lower = min(worst_lower, margin)
                assert margin >= -1e-10

            x = rng.standard_normal(N)
            x /= np.linalg.norm(x)
            y = Sh @ x
            if np.min(G @ y) >= KAPPA:
                z2 = y / np.linalg.norm(y)
                margin = np.min(G @ z2 - KAPPA / a)
                worst_upper = min(worst_upper, margin)
                assert margin >= -1e-10
    return worst_lower, worst_upper

def check_low_rank_kernel_lift(seed=23, trials=100):
    rng = np.random.default_rng(seed)
    max_err = 0.0
    min_eig = 1e9
    for _ in range(trials):
        N = 12
        r = 4
        M = 15
        U0, _ = np.linalg.qr(rng.standard_normal((N, r)))
        theta = np.exp(rng.uniform(-2.0, 8.0, size=r))
        B = U0 @ np.diag(theta) @ U0.T
        S = np.eye(N) + B
        w, V = np.linalg.eigh(S)
        min_eig = min(min_eig, w.min())
        Sh = sqrtm_psd(S)

        wb, Vb = np.linalg.eigh(B)
        Q = Vb[:, :N-r]
        err_kernel = np.linalg.norm(B @ Q, ord=2)
        err_fixed = np.linalg.norm(Sh @ Q - Q, ord=2)
        max_err = max(max_err, err_kernel, err_fixed)

        G = rng.standard_normal((M, N))
        z = rng.standard_normal(N-r)
        z /= np.linalg.norm(z)
        lhs = G @ (Sh @ (Q @ z))
        rhs = (G @ Q) @ z
        err = np.max(np.abs(lhs-rhs))
        max_err = max(max_err, err)
        assert err < 1e-8
    return max_err, min_eig

def main():
    wl, wu = check_general_covariance_sandwich()
    err, mineig = check_low_rank_kernel_lift()

    print("GENERAL_COVARIANCE_SANDWICH_SANITY")
    print(f"worst_observed_lower_inclusion_slack={wl:.6e}")
    print(f"worst_observed_upper_inclusion_slack={wu:.6e}")
    print("LOW_RANK_KERNEL_LIFT_SANITY")
    print(f"max_kernel_or_identity_error={err:.6e}")
    print(f"min_observed_lambda_min_IplusB={mineig:.12f}")

    print("T03_TRANSFERRED_BRACKETS")
    print(f"rho=0.000 lower={L:.11f} upper={U:.11f} width={U-L:.11f}")
    for rho in (0.01,0.05,0.10,0.20,0.50):
        lower=(1-rho)*L
        print(f"rho={rho:.3f} lower={lower:.11f} upper={U:.11f} width={U-lower:.11f}")

    N = 1000
    r = int(round(N**(2/3)))
    theta = np.exp(20.0)
    rho = r/N
    print("CONCRETE_DIVERGING_SPIKE_EXAMPLE")
    print(f"N={N} rank={r} rank_fraction={rho:.6f}")
    print(f"theta=exp(20)={theta:.6e}")
    print("lambda_min=1 exactly; lambda_max=1+theta; operator_norm_diverges if theta_N->infinity")
    print("if rank_N=o(N), asymptotic bracket remains exactly the isotropic current bracket")
    print("ALL_CHECKS_PASS")

if __name__ == "__main__":
    main()
