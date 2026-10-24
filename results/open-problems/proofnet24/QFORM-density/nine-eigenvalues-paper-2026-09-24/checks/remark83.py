"""Remark 8.3: the second crossing volume alone does not bound the density.

Q = (X1+Y1)^2 - (X2+Y2)^2 with X1, X2, Y1, Y2 independent uniform on [-1/2, 1/2]; for I = {X1, X2}, J = {Y1, Y2}
the cross block is diag(1, -1), so E_2 = 1. The density of Q near 0 grows like log(1/|z|): the mass in a window of
width h around 0, divided by h, should track log(1/h) plus a constant.
"""
import json

import numpy as np

rng = np.random.default_rng(83)
N = 20_000_000
X = rng.uniform(-0.5, 0.5, (N, 4)).astype(np.float32)
Q = (X[:, 0] + X[:, 2]) ** 2 - (X[:, 1] + X[:, 3]) ** 2
rows = []
for h in [1e-1, 1e-2, 1e-3, 1e-4]:
    d = float(np.mean(np.abs(Q) < h / 2) / h)
    rows.append({"bin": h, "density_near_0": d, "log_1_over_h": float(np.log(1 / h))})
    print(rows[-1])
diffs = [r["density_near_0"] - r["log_1_over_h"] for r in rows]
print("density - log(1/h):", [round(x, 3) for x in diffs])
json.dump({"N": N, "rows": rows}, open("results_remark83.json", "w", encoding="utf-8"), indent=1)
