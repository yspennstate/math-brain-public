import itertools
import math
import numpy as np


def hadamard(n):
    H = np.array([[1.0]])
    while H.shape[0] < n:
        H = np.block([[H, H], [H, -H]])
    return H


def stability_trial(rng, N=9):
    C = rng.normal(size=(N, 2))
    w, V = np.linalg.eigh(C.T @ C)
    C = C @ (V @ np.diag(w ** -0.5) @ V.T)

    D = rng.normal(size=(N, N))
    D = (D + D.T) / 2

    ell = np.sum(C * C, axis=1)
    q = float(np.max(ell))
    gamma2 = 0.0

    for k in range(N):
        mask = np.arange(N) != k
        Cm = C[mask, :]
        d = D[k, mask]
        m = np.linalg.solve(Cm.T @ Cm, Cm.T @ d)
        e = d - Cm @ m
        delta2 = float(e @ e)
        gamma2 += float(np.linalg.det(Cm.T @ Cm)) * delta2

    # Exact Frobenius distance to C Sym_2 C^T + diagonal:
    # diagonal is free, so least-squares only on i<j and double the residual.
    rows = []
    rhs = []
    for i in range(N):
        for j in range(i + 1, N):
            ci, cj = C[i], C[j]
            rows.append([
                ci[0] * cj[0],
                ci[0] * cj[1] + ci[1] * cj[0],
                ci[1] * cj[1],
            ])
            rhs.append(D[i, j])
    X = np.asarray(rows)
    y = np.asarray(rhs)
    par = np.linalg.lstsq(X, y, rcond=None)[0]
    dist = math.sqrt(2.0) * float(np.linalg.norm(y - X @ par))

    lower = math.sqrt(gamma2)
    upper = math.sqrt(2.0) / math.sqrt(1.0 - q) * math.sqrt(gamma2)
    assert lower <= dist + 1e-10
    assert dist <= upper + 1e-10
    return lower / dist, dist / upper


def main():
    rng = np.random.default_rng(20260923)
    lower_ratios = []
    upper_ratios = []
    for _ in range(100):
        a, b = stability_trial(rng)
        lower_ratios.append(a)
        upper_ratios.append(b)

    N = 256
    H = hadamard(N)
    C = H[:, 0:2] / math.sqrt(N)
    u = H[:, 2] / math.sqrt(N)

    assert np.allclose(C.T @ C, np.eye(2))
    assert np.allclose(C.T @ u, 0)
    assert np.isclose(np.linalg.norm(u), 1)

    A = np.zeros((N + 2, N + 2))
    A[0:2, 2:] = C.T
    A[2:, 0:2] = C
    A[2:, 2:] = np.outer(u, u)

    eig = np.linalg.eigvalsh(A)
    large = eig[np.abs(eig) >= 1 - 1e-10]
    assert np.allclose(large, np.array([-1.0, -1.0, 1.0, 1.0, 1.0]), atol=1e-9)

    max_diag = float(np.max(np.abs(np.diag(A))))
    max_pair_det = 0.0
    for i in range(N + 2):
        for j in range(i + 1, N + 2):
            det = A[i, i] * A[j, j] - A[i, j] ** 2
            max_pair_det = max(max_pair_det, abs(float(det)))
    assert max_diag == 1 / N
    assert max_pair_det == 1 / N
    assert max_diag < 1 / 128
    assert max_pair_det < 1 / 128

    gamma2 = (N - 3) / N ** 2
    gamma = math.sqrt(gamma2)
    gamma_total_sq = N * gamma2

    # Recompute one singleton augmentation directly.
    k = 0
    mask = np.arange(N) != k
    Cm = C[mask, :]
    d = u[k] * u[mask]
    m = np.linalg.solve(Cm.T @ Cm, Cm.T @ d)
    e = d - Cm @ m
    gamma_direct = math.sqrt(np.linalg.det(Cm.T @ Cm)) * np.linalg.norm(e)
    assert abs(gamma_direct - gamma) < 1e-12

    rho_lower = 1 - 9 / N
    r23_bound = 5 * math.e / 3 * rho_lower ** (-1 / 5)
    singleton_grouped_bound = 3 * math.e * gamma ** (-1 / 3)

    W = np.column_stack([C, u])
    sign_rows = np.unique(np.round(W * math.sqrt(N), 12), axis=0)
    max_sign_det = 0.0
    for comb in itertools.combinations(range(len(sign_rows)), 3):
        max_sign_det = max(max_sign_det, abs(float(np.linalg.det(sign_rows[list(comb), :]))))
    assert abs(max_sign_det - 4.0) < 1e-12
    partner_max_minor = max_sign_det / N ** 2
    partner_bound = 3 * partner_max_minor ** (-1 / 3)

    print(f"random_trials=100 lower_ratio_max={max(lower_ratios):.12f} upper_ratio_max={max(upper_ratios):.12f}")
    print(f"N={N}")
    print(f"large_spectrum={large.tolist()}")
    print(f"max_diag={max_diag:.15f}")
    print(f"max_pair_det={max_pair_det:.15f}")
    print(f"gamma_single={gamma:.15f}")
    print(f"gamma_total_sq={gamma_total_sq:.15f}")
    print(f"rho_lower={rho_lower:.15f}")
    print(f"r23_bound={r23_bound:.15f}")
    print(f"partner_max_minor={partner_max_minor:.15e}")
    print(f"partner_bound={partner_bound:.15f}")
    print(f"singleton_grouped_bound={singleton_grouped_bound:.15f}")


if __name__ == "__main__":
    main()
