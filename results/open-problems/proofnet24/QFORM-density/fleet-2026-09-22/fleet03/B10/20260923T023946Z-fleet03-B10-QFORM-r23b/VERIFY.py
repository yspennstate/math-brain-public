import itertools
import numpy as np

rng = np.random.default_rng(20260923)
max_error = 0.0
small_d_cases = 0

for n in (6, 7, 10, 20):
    for _ in range(30):
        z = rng.normal(size=(n, 3))
        r, _ = np.linalg.qr(z)
        r = r[:, :3]
        triples = list(itertools.combinations(range(n), 3))
        weights = {}
        for s in triples:
            weights[s] = float(np.linalg.det(r[list(s), :]) ** 2)

        total = sum(weights.values())
        d_direct = 0.0
        for s, ws in weights.items():
            ss = set(s)
            for t, wt in weights.items():
                if ss.isdisjoint(t):
                    d_direct += ws * wt

        d_gram = 0.0
        best = None
        for s, ws in weights.items():
            g = r[list(s), :].T @ r[list(s), :]
            complement_det = float(np.linalg.det(np.eye(3) - g))
            d_gram += ws * complement_det
            if ws > 1e-15 and (best is None or complement_det < best[0]):
                best = (complement_det, s, g)

        max_error = max(max_error, abs(total - 1.0), abs(d_direct - d_gram))

        if d_direct < 1.0 / 64.0:
            small_d_cases += 1
            value, s, g = best
            leverage = np.sum(r * r, axis=1)
            assert value <= d_direct + 1e-10
            assert np.linalg.eigvalsh(g).max() + 1e-10 >= 1.0 - d_direct ** (1.0 / 3.0)
            assert max(leverage[i] for i in s) + 1e-10 >= (1.0 - d_direct ** (1.0 / 3.0)) / 3.0

print(f"max_identity_error={max_error:.17g}")
print(f"small_d_cases={small_d_cases}")
print("STATUS=PASS")
