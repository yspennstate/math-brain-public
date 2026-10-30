import numpy as np

rng = np.random.default_rng(330823)
g = 0.5
tau = g / 48.0
counts = {"localized": 0, "diffuse": 0, "violations": 0}
min_loc_margin = float("inf")
max_lev = 0.0
min_dist_ratio = float("inf")

for m in [300, 500, 1000]:
    for _ in range(500):
        Z = rng.normal(size=(m, 3))
        W, _ = np.linalg.qr(Z)
        row = np.sum(W * W, axis=1)
        H = row > tau
        WT = W[~H]
        G = WT.T @ WT
        evals = np.linalg.eigvalsh(G)

        if evals[0] < g:
            counts["localized"] += 1
            WH = W[H]
            top = np.linalg.eigvalsh(WH.T @ WH)[-1]
            min_loc_margin = min(min_loc_margin, float(top - (1.0 - g)))
            if not top > 1.0 - g - 1e-12:
                counts["violations"] += 1
        else:
            counts["diffuse"] += 1
            Gi = np.linalg.inv(G)
            lev = np.einsum("ij,jk,ik->i", WT, Gi, WT)
            max_lev = max(max_lev, float(lev.max(initial=0.0)))
            if lev.max(initial=0.0) > 1.0 / 48.0 + 1e-10:
                counts["violations"] += 1

            d = float(rng.uniform(0.5, 1.0))
            theta = float(rng.uniform(0.0, 2.0 * np.pi))
            a = np.sqrt(1.0 - d * d) * np.array([np.cos(theta), np.sin(theta)])
            z = np.r_[d, a]
            rT = WT @ z
            U = WT[:, 1:3]
            GU = U.T @ U
            proj = U @ np.linalg.solve(GU, U.T @ rT)
            dist = np.linalg.norm(rT - proj)
            ratio = float(dist / (d * np.sqrt(g)))
            min_dist_ratio = min(min_dist_ratio, ratio)
            if dist < d * np.sqrt(g) - 1e-10:
                counts["violations"] += 1
            if np.dot(rT, rT) < g - 1e-10:
                counts["violations"] += 1

print("QFORM_B08_R33_HEAVY_PEEL_CHECK")
print("frames", sum(counts.values()) - counts["violations"])
print("localized", counts["localized"])
print("diffuse", counts["diffuse"])
print("violations", counts["violations"])
print("min_localization_margin", min_loc_margin)
print("max_restricted_leverage", max_lev)
print("one_over_48", 1.0 / 48.0)
print("min_transverse_ratio", min_dist_ratio)
print("QFORM_B08_R33_HEAVY_PEEL_CHECK_PASS" if counts["violations"] == 0 else "QFORM_B08_R33_HEAVY_PEEL_CHECK_FAIL")
