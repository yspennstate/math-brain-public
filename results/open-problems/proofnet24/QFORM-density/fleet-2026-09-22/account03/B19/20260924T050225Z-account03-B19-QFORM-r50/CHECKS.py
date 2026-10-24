import math
import numpy as np

SEED = 20260924
TRIALS = 5000
tau = 2.0**-16
s2_floor = 1.0/64.0
robust_floor = 1.0/256.0 - tau
star_floor = 1.0/128.0 - tau
C_R2 = 3.929131770449763

rng = np.random.default_rng(SEED)
counts = {"robust": 0, "starR": 0, "starC": 0}
violations = []
min_robust_ratio = float("inf")
min_star_ratio = float("inf")

for trial in range(TRIALS):
    m = int(rng.integers(4, 25))
    n = int(rng.integers(4, 25))

    U, _ = np.linalg.qr(rng.normal(size=(m, 2)))
    V, _ = np.linalg.qr(rng.normal(size=(n, 2)))
    s2 = s2_floor * (1.0 + 5.0*rng.random())
    s1 = s2 * (1.0 + 8.0*rng.random())
    N2 = U @ np.diag([s1, s2]) @ V.T

    F = rng.normal(size=(m, n))
    F *= (0.9*tau*rng.random()) / (np.linalg.norm(F, "fro") + 1e-300)
    N = N2 + F

    # Recompute the ACTUAL top-two SVD truncation.
    ua, sv, vta = np.linalg.svd(N, full_matrices=False)
    if sv[1] < s2_floor:
        N *= (1.001*s2_floor/sv[1])
        ua, sv, vta = np.linalg.svd(N, full_matrices=False)

    # If needed, reduce only the actual tail singular values so the live tail gate holds.
    if np.linalg.norm(sv[2:]) >= tau:
        ss = sv.copy()
        tailnorm = np.linalg.norm(ss[2:])
        if tailnorm > 0:
            ss[2:] *= (0.9*tau/tailnorm)
        N = ua @ np.diag(ss) @ vta
        sv = ss

    U = ua[:, :2]
    V = vta[:2, :].T
    N2 = U @ np.diag(sv[:2]) @ V.T
    F = N - N2
    tailnorm = np.linalg.norm(F, "fro")

    levR = np.sum(U*U, axis=1)
    levC = np.sum(V*V, axis=1)
    HR = np.where(levR > 0.5)[0]
    HC = np.where(levC > 0.5)[0]
    LR = np.where(levR <= 0.5)[0]
    LC = np.where(levC <= 0.5)[0]

    GR = U[LR].T @ U[LR]
    GC = V[LC].T @ V[LC]
    lmR = np.linalg.eigvalsh(GR)[0]
    lmC = np.linalg.eigvalsh(GC)[0]

    if lmR >= 0.25 - 1e-12 and lmC >= 0.25 - 1e-12:
        counts["robust"] += 1
        M = N[np.ix_(LR, LC)]
        sm = np.linalg.svd(M, compute_uv=False)
        actual = sm[1]
        instance_bound = sv[1]*math.sqrt(max(lmR, 0.0))*math.sqrt(max(lmC, 0.0)) - tailnorm
        if instance_bound > 0:
            min_robust_ratio = min(min_robust_ratio, actual/instance_bound)
        if actual + 1e-10 < robust_floor:
            violations.append(("robust", trial, actual, robust_floor))
    else:
        if lmR < 0.25:
            counts["starR"] += 1
            if len(HR) == 0:
                violations.append(("empty-HR", trial, lmR))
            else:
                actual = max(np.linalg.norm(N[HR, :], axis=1))
                instance_bound = sv[1]/2.0 - tailnorm
                if instance_bound > 0:
                    min_star_ratio = min(min_star_ratio, actual/instance_bound)
                if actual + 1e-10 < star_floor:
                    violations.append(("starR", trial, actual, star_floor))
        if lmC < 0.25:
            counts["starC"] += 1
            if len(HC) == 0:
                violations.append(("empty-HC", trial, lmC))
            else:
                actual = max(np.linalg.norm(N[:, HC], axis=0))
                instance_bound = sv[1]/2.0 - tailnorm
                if instance_bound > 0:
                    min_star_ratio = min(min_star_ratio, actual/instance_bound)
                if actual + 1e-10 < star_floor:
                    violations.append(("starC", trial, actual, star_floor))

H14 = C_R2 * robust_floor**(-0.25)
interval_coeff = H14 / (2.0**0.25)
partner_48 = 34.0*math.sqrt(1.0 + 48.0*math.log(2.0))

print("QFORM_B19_R50_HEAVY6_PEEL_CHECK")
print("trials", TRIALS)
print("counts", counts)
print("violations", len(violations))
print("robust_floor", repr(robust_floor))
print("star_floor", repr(star_floor))
print("H_1/4_bound", repr(H14))
print("interval_delta_1/4_coeff", repr(interval_coeff))
print("partner_Dres_2^-48_bound", repr(partner_48))
print("min_actual_over_instance_robust_bound", repr(min_robust_ratio))
print("min_actual_over_instance_star_bound", repr(min_star_ratio))
assert not violations
print("QFORM_B19_R50_HEAVY6_PEEL_CHECK_PASS")
