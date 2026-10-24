import math
import numpy as np

SEED = 20260924
TRIALS = 60000
rng = np.random.default_rng(SEED)

pivot_branch = 0
pair_branch = 0
violations = 0
min_pair_ratio = float("inf")
max_schur_det_relerr = 0.0
max_interlace_err = 0.0

for k in range(TRIALS):
    z = rng.normal(size=(3, 3))
    u, _ = np.linalg.qr(z)
    mags = np.exp(rng.uniform(-1.0, 3.0, size=3))
    if k % 2 == 0:
        vals = np.array([-mags[0], mags[1], mags[2]])
        majority = +1
    else:
        vals = np.array([mags[0], -mags[1], -mags[2]])
        majority = -1
    C = u @ np.diag(vals) @ u.T
    lam = np.linalg.eigvalsh(C)
    s = float(np.min(np.abs(lam)))
    d = np.diag(C)

    has_majority_pivot = (np.max(d) >= s/3) if majority == 1 else (np.min(d) <= -s/3)
    if has_majority_pivot:
        pivot_branch += 1
        continue

    pair_branch += 1
    for deleted in range(3):
        I = [j for j in range(3) if j != deleted]
        B = C[np.ix_(I, I)]
        mu = np.linalg.eigvalsh(B)
        interlace_err = max(
            lam[0] - mu[0],
            mu[0] - lam[1],
            lam[1] - mu[1],
            mu[1] - lam[2],
            0.0,
        )
        max_interlace_err = max(max_interlace_err, interlace_err)
        kappa = float(np.min(np.abs(mu)))
        min_pair_ratio = min(min_pair_ratio, kappa/s)
        if not (mu[0] < 0 < mu[1] and kappa >= s/3 - 1e-10):
            violations += 1

        r = C[I, deleted]
        delta = C[deleted, deleted] - r @ np.linalg.solve(B, r)
        lhs = np.linalg.det(C)
        rhs = np.linalg.det(B) * delta
        relerr = abs(lhs-rhs)/max(1.0, abs(lhs))
        max_schur_det_relerr = max(max_schur_det_relerr, relerr)

# Exact one-dimensional tube formula behind the logarithmic averaging lemma.
def tube_measure(xi, rho):
    lo = max(0.0, xi-rho)
    hi = xi+rho
    if hi <= 0:
        return 0.0
    return 2.0*(math.sqrt(hi)-math.sqrt(lo))

max_tube_ratio = 0.0
for rho in np.logspace(-10, 4, 180):
    for q in np.linspace(-2.0, 20.0, 1200):
        ratio = tube_measure(q*rho, rho)/math.sqrt(rho)
        max_tube_ratio = max(max_tube_ratio, ratio)

C_pivot = 4 * 22**(3/4) * 3**(1/4)
C_log = 8 * 6**(1/4)

print(f"seed={SEED}; trials={TRIALS}")
print(f"pivot_branch={pivot_branch}; pair_branch={pair_branch}")
print(f"violations={violations}")
print(f"min_observed_pair_kappa_over_s={min_pair_ratio:.15f}; theorem_threshold={1/3:.15f}")
print(f"max_interlace_error={max_interlace_err:.3e}")
print(f"max_schur_det_relative_error={max_schur_det_relerr:.3e}")
print(f"max_grid_tube_measure_over_sqrt_rho={max_tube_ratio:.15f}; exact_bound={2*math.sqrt(2):.15f}")
print(f"pivot_branch_constant={C_pivot:.15f}")
print(f"log_average_branch_constant={C_log:.15f}")
assert violations == 0
assert max_interlace_err < 1e-10
assert max_schur_det_relerr < 1e-10
assert max_tube_ratio <= 2*math.sqrt(2) + 1e-12
print("QFORM_B11_R56_LOCALIZED_INDEFINITE_CHECK_PASS")
