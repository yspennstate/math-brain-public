import numpy as np

rng = np.random.default_rng(2026092301)
viol = 0
cases = 0
min_margin = float("inf")

for m in range(4, 11):
    for k in range(1, min(4, m - 3) + 1):
        for _ in range(300):
            kappa = 2.0
            delta = 0.15

            Z = rng.standard_normal((m, m))
            B0 = kappa * np.eye(m) + (Z @ Z.T) / (10 * m)

            Z = rng.standard_normal((m, m))
            R = (Z + Z.T) / 2
            ev = np.linalg.eigvalsh(R)
            neg = sorted((-x for x in ev if x < 0), reverse=True)
            beta = neg[k] if len(neg) > k else 0.0
            if beta > 1.2:
                R *= 1.2 / beta
                ev = np.linalg.eigvalsh(R)
                neg = sorted((-x for x in ev if x < 0), reverse=True)
                beta = neg[k] if len(neg) > k else 0.0

            Z = rng.standard_normal((m, m))
            T = (Z + Z.T) / 2
            op = np.max(np.abs(np.linalg.eigvalsh(T)))
            if op > 0:
                T *= delta / op

            L = kappa - delta - beta
            if L <= 1e-8:
                continue

            B = B0 + R + T
            w = np.linalg.eigvalsh(B)[::-1]
            count = int(np.sum(w >= L - 1e-8))
            cases += 1
            if count < m - k:
                viol += 1
            min_margin = min(min_margin, float(w[m-k-1] - L))

print(f"cases={cases}")
print(f"violations={viol}")
print(f"minimum_threshold_margin={min_margin:.15g}")
assert viol == 0
