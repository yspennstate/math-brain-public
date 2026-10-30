import numpy as np

rng = np.random.default_rng(20260924075625)
max_det = 0.0
max_schur = 0.0
max_slope = 0.0

for _ in range(10000):
    G = rng.normal(size=(3, 3))
    O, _ = np.linalg.qr(G)
    mu_p = 10.0 ** rng.uniform(-1.0, 1.0)
    mu_m = -(10.0 ** rng.uniform(-1.0, 1.0))
    F = O @ np.diag([mu_p, mu_m, 0.0]) @ O.T
    v = O[:, 2]
    i = int(np.argmax(np.abs(v)))
    I = [j for j in range(3) if j != i]
    P = F[np.ix_(I, I)]
    r = F[I, i]
    a = F[i, i]

    D = abs(np.linalg.det(P))
    kappa_F = abs(mu_p * mu_m)
    det_err = abs(D - kappa_F * v[i] ** 2) / (1.0 + D + kappa_F)
    max_det = max(max_det, det_err)

    schur = a - r @ np.linalg.solve(P, r)
    schur_err = abs(schur) / (1.0 + abs(a) + np.linalg.norm(r))
    max_schur = max(max_schur, schur_err)

    b = rng.normal(size=3)
    c = b[I]
    d = b[i]
    gamma = d - c @ np.linalg.solve(P, r)
    beta = v @ b
    slope_err = abs(gamma - beta / v[i]) / (1.0 + abs(gamma) + abs(beta / v[i]))
    max_slope = max(max_slope, slope_err)

print("QFORM_B06_R54_CHECK_PASS")
print("max_normalized_det_identity_error", max_det)
print("max_normalized_zero_schur_error", max_schur)
print("max_normalized_null_slope_error", max_slope)
