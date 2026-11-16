#!/usr/bin/env python3
"""Numerical checks of Lemma 2.1 (conditional variance) and Lemma 3.1 (lattice sum).

Lemma 2.1: for one coordinate of the slice t -> B(s, t), a Brownian motion with
variance rate s, and pairs (u_j, v_j) in I x J with I = [0, 1], J = [2, 3], the
conditional variance of W(v) - W(u) given the earlier differences W(v_j) - W(u_j)
is at least the Brownian bridge variance given the anchors, which is at least
(s/2)(rho_U(u) + rho_V(v)). Endpoints are drawn from a grid of mesh 1/16, so
repeated endpoints and endpoints on the anchors occur often.

Lemma 3.1: the lattice sum divided by (k+2)^2 r^4 delta^-2 (1 + log2(1/delta))
stays bounded as delta decreases.

These checks are not part of the proof. Usage: python code/check_lemmas.py
(writes data/lemma_checks.json relative to the repository root).
"""
import json
import pathlib

import numpy as np

ROOT = pathlib.Path(__file__).resolve().parent.parent
rng = np.random.default_rng(17017)


def bridge_variance(x, anchors):
    """Variance at x of a unit-rate Brownian bridge between the anchors adjacent to x."""
    if np.min(np.abs(anchors - x)) < 1e-12:
        return 0.0
    left = max(a for a in anchors if a < x)
    right = min(a for a in anchors if a > x)
    return (x - left) * (right - x) / (right - left)


margins = []
for k in range(1, 9):              # k earlier pairs, then one new pair
    for _ in range(120):
        u = rng.integers(0, 17, k + 1) / 16
        v = 2 + rng.integers(0, 17, k + 1) / 16
        s = float(rng.uniform(0.5, 2.0))
        # Cov(W(v_i) - W(u_i), W(v_j) - W(u_j)) = s |[u_i, v_i] cap [u_j, v_j]|
        cov = s * np.maximum(0.0, np.minimum(v[:, None], v[None, :]) - np.maximum(u[:, None], u[None, :]))
        prev = cov[:-1, :-1]
        cond_var = float(cov[-1, -1] - cov[-1, :-1] @ np.linalg.pinv(prev, rcond=1e-12) @ cov[:-1, -1])
        anchors_u = np.r_[0.0, 1.0, u[:-1]]
        anchors_v = np.r_[2.0, 3.0, v[:-1]]
        rho = float(np.min(np.abs(anchors_u - u[-1])) + np.min(np.abs(anchors_v - v[-1])))
        bridge = s * (bridge_variance(u[-1], anchors_u) + bridge_variance(v[-1], anchors_v))
        bound = s * rho / 2
        assert cond_var + 1e-9 >= bridge >= bound - 1e-12, (k, cond_var, bridge, bound)
        margins.append(cond_var - bound)

lattice = []
for n in (4, 6, 8, 10):
    delta = 2.0 ** (-n)
    for alpha in (0.3, 0.4, 0.49):  # r = delta^alpha, so delta <= r^2 <= 1
        r = delta ** alpha
        grid = np.arange(2 ** n + 1) * delta
        for k in (0, 1, 3, 7):
            au = np.r_[0.0, 1.0, rng.choice(grid, k)]
            av = np.r_[2.0, 3.0, 2 + rng.choice(grid, k)]
            du = np.min(np.abs(grid[:, None] - au), axis=1)
            dv = np.min(np.abs((2 + grid)[:, None] - av), axis=1)
            total = float(np.sum(r ** 4 / (r ** 2 + du[:, None] + dv[None, :]) ** 2))
            norm = (k + 2) ** 2 * r ** 4 * delta ** (-2) * (1 + n)
            lattice.append({"n": n, "alpha": alpha, "k": k, "normalized_sum": total / norm})

out = {
    "seed": 17017,
    "variance_cases": len(margins),
    "smallest_conditional_variance_minus_bound": min(margins),
    "largest_normalized_lattice_sum": max(x["normalized_sum"] for x in lattice),
    "lattice_cases": lattice,
}
(ROOT / "data").mkdir(exist_ok=True)
(ROOT / "data" / "lemma_checks.json").write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
print(json.dumps({key: val for key, val in out.items() if key != "lattice_cases"}, indent=2))
