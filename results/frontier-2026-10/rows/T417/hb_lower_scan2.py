"""T417 (agent A, 18 Oct): per-delta sup of R(mu') for mu' in [1 - delta/4, 2] (explicit choice, worst diagonal noise, c = 1/4).
If sup over mu' >= 1 - delta/4 of the secular sum stays below 1, no secular root lies above 1 - delta/4."""
import numpy as np
for delta in [0.5, 0.2, 0.1, 0.03, 0.01, 0.003, 0.001, 0.0003]:
    beta = (1 - delta / 2) ** 2; out = []
    for mu in [1 - delta / 4, 1 - delta / 8, 1, 1 + delta, 1.1, 1.5, 2.0]:
        w = 0.0
        for s in np.concatenate([np.linspace(0.25, 4, 300), np.geomspace(4, 1 / delta ** 2, 300)]):
            x = s * delta ** 2; k = 1 + beta - x
            for eps in [0.0, 0.25 * delta * x]:
                M = np.array([[k * k + eps, -2 * beta * k, beta ** 2], [k, -beta, 0], [1, 0, 0]])
                p = np.linalg.det(mu * np.eye(3) - M)
                w = max(w, mu * (mu + beta) * x / p * delta if p > 0 else np.inf)
        out.append(w)
    print(f"delta {delta:<7} sup R at mu = 1-d/4, 1-d/8, 1, 1+d, 1.1, 1.5, 2: " + " ".join(f"{v:.3f}" for v in out))
