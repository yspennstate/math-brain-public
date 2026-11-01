import json
import math
import numpy as np

SEED = 20260924101039
rng = np.random.default_rng(SEED)


def sv_desc(M):
    return np.linalg.svd(M, compute_uv=False)


def random_orthogonal(n):
    Q, R = np.linalg.qr(rng.normal(size=(n, n)))
    d = np.sign(np.diag(R))
    d[d == 0] = 1
    return Q * d


clip_trials = 10_000
clip_violations = 0
min_sv_margin = float("inf")
min_psd_eig = float("inf")

for _ in range(clip_trials):
    n = int(rng.integers(6, 15))
    m = int(rng.integers(5, n + 1))
    U = random_orthogonal(n)
    lam = rng.normal(size=n) * np.exp(rng.uniform(-2, 2, size=n))
    frac = rng.random(n)
    mu = frac * np.abs(lam) * rng.choice([-1.0, 1.0], size=n)

    A = (U * lam) @ U.T
    B = (U * mu) @ U.T
    idx = np.sort(rng.choice(n, size=m, replace=False))
    P = np.eye(n)[:, idx]

    sa = sv_desc(A @ P)
    sb = sv_desc(B @ P)
    margin = float(np.min(sa - sb))
    min_sv_margin = min(min_sv_margin, margin)

    psd = A @ A - B @ B
    mineig = float(np.linalg.eigvalsh((psd + psd.T) / 2).min())
    min_psd_eig = min(min_psd_eig, mineig)

    if margin < -1e-9 or mineig < -1e-8:
        clip_violations += 1

# Literal fleet04/B12-r8-compatible baseline.
n = 18
m = 6
jdim = 12
C = np.diag([4.0, 4.0, 0.0, 0.0, 0.0, 0.0])
X = np.zeros((m, jdim))
for r in range(2, 6):
    X[r, r - 2] = 2.0
X[0, 4] = 2.0
X[1, 5] = 2.0
D = np.zeros((jdim, jdim))
Bstar = np.block([[C, X], [X.T, D]])
P = np.eye(n)[:, :m]
base_singular_values = sv_desc(Bstar @ P)
evals, U = np.linalg.eigh(Bstar)

partner_g = (math.sqrt(17.0) - 1.0) / 2.0
inflate_trials = 10_000
inflate_violations = 0
min_final_s6 = float("inf")
min_exact_margin = float("inf")

for _ in range(inflate_trials):
    extra = np.exp(rng.uniform(-8, 8, size=n)) * rng.random(n)
    mags = np.abs(evals) + extra
    signs = rng.choice([-1.0, 1.0], size=n)
    lam = signs * mags
    A = (U * lam) @ U.T
    s6 = float(sv_desc(A @ P)[-1])
    min_final_s6 = min(min_final_s6, s6)
    min_exact_margin = min(min_exact_margin, s6 - float(base_singular_values[-1]))
    if s6 + 1e-9 < base_singular_values[-1]:
        inflate_violations += 1

K3 = 3 * 2 ** (4 / 3) * math.e ** (1 / 3)
five_mode_numerator_m6 = math.sqrt(144 * math.pi + K3 ** 2)

result = {
    "seed": SEED,
    "spectral_clipping_trials": clip_trials,
    "spectral_clipping_violations": clip_violations,
    "minimum_singular_value_margin": min_sv_margin,
    "minimum_numerical_eigenvalue_A2_minus_B2": min_psd_eig,
    "partner_baseline_singular_values": base_singular_values.tolist(),
    "partner_bound_g": partner_g,
    "partner_inflation_trials": inflate_trials,
    "partner_inflation_violations": inflate_violations,
    "minimum_final_s6": min_final_s6,
    "minimum_exact_baseline_margin": min_exact_margin,
    "K3": K3,
    "five_mode_numerator_m6": five_mode_numerator_m6,
    "density_cap_partner_bound_no_residual": five_mode_numerator_m6 / partner_g,
    "density_cap_partner_bound_residual_1_over_20": five_mode_numerator_m6 / (partner_g - 0.05),
    "density_cap_exact_baseline": five_mode_numerator_m6 / 2.0,
    "baseline_eigenvalues": evals.tolist(),
    "note": "Finite floating-point sanity checks only; analytic proofs are in REPORT.md."
}

print(json.dumps(result, indent=2))
