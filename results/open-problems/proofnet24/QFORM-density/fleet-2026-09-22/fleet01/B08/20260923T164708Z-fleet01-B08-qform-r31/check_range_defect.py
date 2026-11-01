import math
import numpy as np

SEED = 31082026
TRIALS = 2500
rng = np.random.default_rng(SEED)

checked = 0
min_slack = float("inf")
for trial in range(TRIALS):
    n = 16
    Z = rng.normal(size=(n, n))
    Q, _ = np.linalg.qr(Z)
    R = Q[:, :3]
    lam = (1 + 2*rng.random(3))*rng.choice([-1, 1], 3)
    comp = 4*rng.normal(size=n-3)
    if trial % 7 == 0:
        comp[0] = rng.choice([-1, 1])*100
    A = R @ np.diag(lam) @ R.T + Q[:, 3:] @ np.diag(comp) @ Q[:, 3:].T

    for _ in range(40):
        mask = rng.random(n) < 0.5
        I = np.where(mask)[0]
        J = np.where(~mask)[0]
        if len(I) < 3 or len(J) < 3:
            continue
        GI = R[I].T @ R[I]
        alpha = np.linalg.eigvalsh(GI)[0]
        if alpha < 0.08:
            continue

        C = A[np.ix_(I, I)]
        B = A[np.ix_(I, J)]
        ec, Uc = np.linalg.eigh(C)
        idx = np.argmax(np.abs(ec))
        mu = ec[idx]
        r = Uc[:, idx]
        sC = np.linalg.svd(C, compute_uv=False)
        s2C = sC[1]
        Ub, sB, _ = np.linalg.svd(B, full_matrices=False)
        U = Ub[:, :2]
        d = np.linalg.norm(r - U @ (U.T @ r))
        rho = np.linalg.norm(R[I].T @ r)
        s3B = sB[2] if len(sB) >= 3 else 0.0

        lhs = math.sqrt(alpha) * min(abs(lam))
        rhs = abs(mu)*rho*d + s2C + s3B
        slack = rhs - lhs
        min_slack = min(min_slack, slack)
        if slack < -1e-8:
            raise AssertionError((trial, lhs, rhs, slack))
        checked += 1
        break

alpha = 3/8
c = math.sqrt(3/20)
delta = 3/math.sqrt(40)
eta = math.sqrt(alpha) - c
kappa_half = c*delta*(0.5**2)/(2*math.sqrt(c*c*(0.5**2)+4*delta*delta))

print("QFORM_B08_R31_RANGE_DEFECT_CHECK_PASS")
print("seed", SEED)
print("checked", checked)
print("min_slack", min_slack)
print("eta", eta)
print("near_aligned_density_constant", 12*math.sqrt(math.e)/eta)
print("near_aligned_star_constant", eta/(2*math.sqrt(6)))
print("delta", delta)
print("kappa_half_new", kappa_half)
print("partner_residual_half", kappa_half/16)
print("partner_density_half", 23/kappa_half)
print("orthogonal_residual", c/64)
print("orthogonal_density", 92/c)
