import numpy as np, math


def family(m):
    R = [np.array([1.0, 0.0, 0.0])]
    for _ in range(m):
        R.append(np.array([0.0, 1 / math.sqrt(2 * m), 1 / (2 * math.sqrt(m))]))
        R.append(np.array([0.0, 1 / math.sqrt(2 * m), -1 / (2 * math.sqrt(m))]))
    for _ in range(m):
        R.append(np.array([0.0, 0.0, 1 / math.sqrt(2 * m)]))
    R = np.vstack(R)
    Lam = np.diag([1.0, 1.0, -1.0])
    A = R @ Lam @ R.T
    evals = np.linalg.eigvalsh(A)
    nonzero = evals[np.abs(evals) > 1e-9]
    diag = np.diag(A)
    ratios = []
    for r in R:
        if r[2] != 0:
            ratios.append(np.linalg.norm(r) / (r[2] ** 2))
    cone_lb = min(ratios)
    return R, A, nonzero, diag, cone_lb


for m in [1, 2, 3, 10, 100]:
    R, A, eigs, diag, cone_lb = family(m)
    print(
        f"m={m:3d} n={len(R):3d} "
        f"gram_err={np.max(np.abs(R.T @ R - np.eye(3))):.3e} "
        f"eigs={np.array2string(eigs, precision=6)} "
        f"min_diag={diag.min():.6g} "
        f"cone_cost_lb={cone_lb:.12g} "
        f"ratio_to_sqrt2m={cone_lb / math.sqrt(2 * m):.12g}"
    )

kappa = 0.5
mu = 0.5
partner = 8 * 2 ** (3 / 4) * math.sqrt(5) * (kappa * mu) ** (-1 / 4)
onesheet = math.pi * math.sqrt(2)
print(f"kappa={kappa}, mu={mu}")
print(f"partner_bound={partner:.12f}")
print(f"one_sheet_bound={onesheet:.12f}")
print("PASS")
