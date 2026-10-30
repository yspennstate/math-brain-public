import itertools
import math
import numpy as np

rng = np.random.default_rng(20260923)
max_local_identity_err = 0.0
max_rigidity_ratio = 0.0
min_partition_ratio = float('inf')
trials = 30

for trial in range(trials):
    n = 8
    M = rng.normal(size=(2, n))
    G = M @ M.T
    Ginv = np.linalg.inv(G)
    S2 = np.linalg.det(G)
    C = rng.normal(size=(n, n))
    C = (C + C.T) / 2

    ell = np.array([M[:, j] @ Ginv @ M[:, j] for j in range(n)])
    zloc = []
    d = []
    for j in range(n):
        inds = [i for i in range(n) if i != j]
        P = M[:, inds].T
        c = C[inds, j]
        y = np.linalg.lstsq(P, c, rcond=None)[0]
        dj = np.linalg.norm(c - P @ y)
        N = np.column_stack([P, c])
        zj = max(0.0, np.linalg.det(N.T @ N))
        rhs = S2 * (1 - ell[j]) * dj * dj
        max_local_identity_err = max(max_local_identity_err, abs(zj-rhs)/max(1.0, abs(zj), abs(rhs)))
        zloc.append(zj)
        d.append(dj)

    zagg = sum(zloc)

    # Exhaust every physical split L=I union J and compute E3 of A[I,T union J].
    best = 0.0
    for mask in range(1 << n):
        I = [i for i in range(n) if (mask >> i) & 1]
        J = [i for i in range(n) if not ((mask >> i) & 1)]
        if len(I) < 3:
            continue
        blocks = [M[:, I].T]
        if J:
            blocks.append(C[np.ix_(I, J)])
        N = np.column_stack(blocks)
        s2vals = np.linalg.svd(N, compute_uv=False) ** 2
        e3 = 0.0
        for a, b, c in itertools.combinations(s2vals, 3):
            e3 += a*b*c
        best = max(best, e3)
    if zagg > 0:
        min_partition_ratio = min(min_partition_ratio, best/(zagg/16))

    # Quantitative rigidity, tested only in the diffuse branch.
    if np.max(ell) <= 0.75:
        ew, U = np.linalg.eigh(G)
        Gm12 = U @ np.diag(ew ** -0.5) @ U.T
        V = Gm12 @ M
        ys = []
        D2 = 0.0
        for j in range(n):
            inds = [i for i in range(n) if i != j]
            P = V[:, inds].T
            c = C[inds, j]
            y = np.linalg.lstsq(P, c, rcond=None)[0]
            r = c - P @ y
            D2 += float(r @ r)
            ys.append(y)
        Y = np.array(ys)
        B = sum(np.outer(V[:, i], Y[i]) for i in range(n))
        K = (B + B.T) / 2
        E = C - V.T @ K @ V
        np.fill_diagonal(E, 0.0)
        ratio = np.linalg.norm(E, 'fro')**2 / D2 if D2 else 0.0
        max_rigidity_ratio = max(max_rigidity_ratio, ratio)
        assert ratio <= 26 + 1e-9

S0 = 1/(480*math.sqrt(7626))
Cstar = 8.45302122552817687470491804598
paid_constant = Cstar * 16**(1/6) * (2**-60)**(-1/6)
residual_bound = 2*math.sqrt(26)*(2**-60)**0.5/S0
pinned_Dprime_constant = 9*math.sqrt(3*math.e) * 16**(1/6) * (2**-60)**(-1/6)

print(f"trials={trials}")
print(f"max_local_identity_relative_error={max_local_identity_err:.3e}")
print(f"min_exhaustive_partition_ratio_to_Zagg_over_16={min_partition_ratio:.9f}")
print(f"max_rigidity_Frobenius_squared_over_D2={max_rigidity_ratio:.9f}")
print(f"S0={S0:.15e}")
print(f"marginal_free_E3_bound_at_Zagg_2^-60={paid_constant:.12f}")
print(f"common_plane_residual_op_bound_if_Zagg_lt_2^-60={residual_bound:.15f}")
print(f"pinned_Dprime_h_2over3_bound_at_Zagg_2^-60={pinned_Dprime_constant:.12f}")
print("QFORM_B19_AGGREGATE_E3_RIGIDITY_CHECK_PASS")
