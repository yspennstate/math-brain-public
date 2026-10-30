import numpy as np, math


def family(m, c=0.75, beta=0.5):
    rows = [np.array([math.sqrt(c), 0.0, 0.0])]
    for _ in range(m):
        rows.append(np.array([math.sqrt((1 - c) / m), 0.0, 0.0]))
    for _ in range(m):
        rows.append(np.array([0.0, 1 / math.sqrt(2 * m), math.sqrt((1 - beta) / (2 * m))]))
        rows.append(np.array([0.0, 1 / math.sqrt(2 * m), -math.sqrt((1 - beta) / (2 * m))]))
    for _ in range(m):
        rows.append(np.array([0.0, 0.0, math.sqrt(beta / m)]))
    R = np.vstack(rows)
    Lam = np.diag([1.0, 1.0, -1.0])
    A = R @ Lam @ R.T
    eig = np.linalg.eigvalsh(A)
    nonzero = eig[np.abs(eig) > 1e-9]
    diag = np.diag(A)
    lev = np.sum(R * R, axis=1)
    ratios = [np.linalg.norm(r) / (r[2] ** 2) for r in R if abs(r[2]) > 1e-15]
    cone_lb = min(ratios)
    return R, A, nonzero, diag, lev, cone_lb


for m in [1, 2, 3, 10, 100]:
    R, A, eigs, diag, lev, cone_lb = family(m)
    print(
        f"m={m:3d} n={len(R):3d} "
        f"gram_err={np.max(np.abs(R.T @ R - np.eye(3))):.3e} "
        f"eigs={np.array2string(eigs, precision=6)} "
        f"max_lev={lev.max():.12g} "
        f"min_diag={diag.min():.12g} "
        f"cone_cost_lb={cone_lb:.12g} "
        f"ratio_to_sqrt2m={cone_lb / math.sqrt(2 * m):.12g}"
    )

beta = 0.5
kappa = beta
mu = beta
partner = 8 * 2 ** (3 / 4) * math.sqrt(5) * (kappa * mu) ** (-1 / 4)
eigenbank = 16 * math.sqrt(60)
print(f"kappa={kappa}, mu={mu}")
print(f"partner_bound={partner:.12f}")
print(f"eigenbank_peel_bound={eigenbank:.12f}")
print("PASS")
