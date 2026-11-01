import itertools
import numpy as np

rng = np.random.default_rng(2026092407)
max_minor = 0.0
max_frame = 0.0
max_sing = 0.0
max_fro = 0.0
trials = 500
used = 0

for _ in range(trials):
    m = int(rng.integers(3, 9))
    tau = float(rng.normal())
    if abs(tau) < 0.1:
        tau = 0.75 if tau >= 0 else -0.75
    ell = rng.normal(size=2)
    ell /= np.linalg.norm(ell)
    B = tau * np.outer(ell, ell)
    U = rng.normal(size=(m, 2))
    C = rng.normal(size=(m, m))
    C = (C + C.T) / 2
    A = np.block([[B, U.T], [U, C]])

    if abs(A[1, 1]) > abs(A[0, 0]):
        perm = [1, 0] + list(range(2, m + 2))
        A = A[np.ix_(perm, perm)]

    B = A[:2, :2]
    U = A[2:, :2]
    C = A[2:, 2:]
    a, c = B[0, 0], B[0, 1]
    if abs(a) < 1e-11:
        continue
    used += 1

    kappa = c / a
    u, v = U[:, 0], U[:, 1]
    w = v - kappa * u
    S = C - np.outer(u, u) / a

    pairs = list(itertools.combinations(range(m), 2))
    E = np.zeros((m, len(pairs)))
    for j, (r, s) in enumerate(pairs):
        E[r, j] = w[s]
        E[s, j] = -w[r]

    F = np.zeros((len(pairs), len(pairs)))
    for ii, R in enumerate(pairs):
        for jj, T in enumerate(pairs):
            rows = [0, 1, R[0] + 2, R[1] + 2]
            cols = [0, 1, T[0] + 2, T[1] + 2]
            F[ii, jj] = np.linalg.det(A[np.ix_(rows, cols)])

    F_formula = -a * E.T @ S @ E
    max_minor = max(max_minor, float(np.max(np.abs(F - F_formula))))

    W = float(w @ w)
    if W <= 1e-12:
        continue
    P = np.eye(m) - np.outer(w, w) / W
    max_frame = max(max_frame, float(np.linalg.norm(E @ E.T - W * P, "fro")))

    sv_F = np.linalg.svd(F, compute_uv=False)
    sv_T = np.linalg.svd(P @ S @ P, compute_uv=False)
    lhs = np.sort(sv_F)[::-1][:m]
    if len(lhs) < m:
        lhs = np.pad(lhs, (0, m - len(lhs)))
    rhs = np.sort(abs(a) * W * sv_T)[::-1]
    max_sing = max(max_sing, float(np.max(np.abs(lhs - rhs))))
    max_fro = max(
        max_fro,
        abs(float(np.linalg.norm(F, "fro") - abs(a) * W * np.linalg.norm(P @ S @ P, "fro"))),
    )

pstar = 1.19876993884320
print(f"trials_attempted={trials}")
print(f"trials_used={used}")
print(f"max_minor_matrix_abs_error={max_minor:.17g}")
print(f"max_frame_fro_error={max_frame:.17g}")
print(f"max_singular_value_abs_error={max_sing:.17g}")
print(f"max_fro_identity_abs_error={max_fro:.17g}")
print(f"pstar2={pstar*pstar:.17g}")
print(f"pstar2_over_24={pstar*pstar/24:.17g}")
print(f"pstar2_over_48={pstar*pstar/48:.17g}")
print("STATUS=PASS")
