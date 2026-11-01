"""T417 (agent A, 18 Oct 2026): toward a proof of the heavy-ball lower bound.
(1) Check: rho = max(largest block radius, largest real root of the secular function above it) on random points.
(2) For the explicit choice (sqrt beta = 1 - delta/2, eta = delta^2/(4 h_min)) and mu = 1 - delta/4, scan the per-mode ratio
    R = [mu (mu+beta) eta h / p(mu)] * delta,  so that the secular sum = (eta/B) sum_j h_j R_j / delta <= sup R * eta tr H/(B delta) <= sup R * c,
    and the block radii, over s = eta h / delta^2 in [1/4, 1/delta^2] and delta in (0, 1).
    The diagonal noise eta^2 h^2/B is at most c delta eta h for the explicit choice, so the scan uses that worst case (c = 1/4)."""
import numpy as np
from hb_ms_secular import full


def Mj(k, hj, eta, beta, B):
    return np.array([[k * k + eta ** 2 / B * hj * hj, -2 * beta * k, beta ** 2], [k, -beta, 0], [1, 0, 0]])


rng = np.random.default_rng(9); bad = 0
for t in range(1500):
    d = int(rng.integers(2, 10)); h = np.sort(rng.uniform(0.01, 1, d))[::-1]; B = int(rng.integers(1, 50))
    beta = rng.uniform(0, 0.99); eta = rng.uniform(0, 2 * (1 + beta) / h[0])
    rho = max(abs(np.linalg.eigvals(full(h, eta, beta, B)))); kb = 1 + beta - eta * h
    blk = max(max(abs(np.linalg.eigvals(Mj(k, hj, eta, beta, B)))) for k, hj in zip(kb, h))
    grid = np.linspace(blk + 1e-9, max(rho, blk) + 2, 200001)

    def f(mu):
        tot = 0.0
        for k, hj in zip(kb, h):
            tot += eta ** 2 / B * hj ** 2 * mu * (mu + beta) / np.linalg.det(mu * np.eye(3) - Mj(k, hj, eta, beta, B))
        return 1 - tot
    lo, hi = blk + 1e-12, 50.0
    root = blk
    if f(lo + 1e-9) < 0:   # secular function negative just above the blocks -> a root lies above
        a, b = lo + 1e-9, hi
        for _ in range(200):
            m = (a + b) / 2
            if f(m) < 0: a = m
            else: b = m
        root = b
    if abs(max(blk, root) - rho) > 1e-6 * max(1, rho): bad += 1
print(f"(1) rho == max(block radius, top secular root) on {1500 - bad}/1500")
worst = 0.0; wblk = 0.0
for delta in [0.5, 0.2, 0.1, 0.03, 0.01, 0.003, 0.001]:
    beta = (1 - delta / 2) ** 2; mu = 1 - delta / 4
    for s in np.concatenate([np.linspace(0.25, 4, 400), np.geomspace(4, 1 / delta ** 2, 400)]):
        x = s * delta ** 2  # x = eta h
        k = 1 + beta - x
        for eps in [0.0, 0.25 * delta * x]:   # eta^2 h^2/B <= c delta eta h with c = 1/4 (from delta <= 4 c B h_min/tr H)
            M = np.array([[k * k + eps, -2 * beta * k, beta ** 2], [k, -beta, 0], [1, 0, 0]])
            p = np.linalg.det(mu * np.eye(3) - M); br = max(abs(np.linalg.eigvals(M)))
            wblk = max(wblk, br / mu)
            if p > 0: worst = max(worst, mu * (mu + beta) * x / p * delta)
            else: worst = np.inf
print(f"(2) sup R = {worst:.4f} (secular sum at mu=1-delta/4 <= sup R * c); max block radius / mu = {wblk:.4f}")
