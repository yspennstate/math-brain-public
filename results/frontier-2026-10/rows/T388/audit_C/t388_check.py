"""T388 review, part 1: an independent check of the offline partial-trace claim (source: T388_partial_trace_d2.md
in the row folder). Written from the model's definition, not from t388.py.

Model: x = S(z + beta g u), z ~ N(0, I_d), g = +-1, S = (I + beta^2 u u^T)^(-1/2), so Cov x = I and
cum4(x) = kappa u^(x4), kappa = -2 beta^4/(1+beta^2)^2.
Statistic: M_n = (1/n) sum a_i x_i x_i^T, a = |x|^2 - d - 2. E M_n = kappa u u^T (exact).
M_n + (d+2) I is the FOBI matrix (1/n) sum |x|^2 x x^T of Cardoso (1989): same eigenvectors.

Prediction tested here (not in the source): with n/d large the centred noise M_n - kappa u u^T behaves like a Wigner
matrix whose off-diagonal entries have variance v/n, v = E[a^2 x_j^2 x_k^2] (j != k, estimated from the sample).
With sigma^2 = d v/n the noise edge is 2 sigma; the bottom eigenvector separates when |kappa| > sigma (BBP), with
overlap^2 = 1 - sigma^2/kappa^2 and bottom eigenvalue kappa + sigma^2/kappa. Since v ~ 2d, sigma^2 ~ 2/c at n = c d^2,
so the threshold is c* ~ 2/kappa^2 = 8 at beta = 1 and the overlap depends on c alone.
usage: python t388_check.py -> t388_check.json
"""
import json, math
import numpy as np

beta = 1.0
kappa = -2 * beta ** 4 / (1 + beta ** 2) ** 2
B = 50000
out = []
for d in [16, 32, 64]:
    for c in [4.0, 8.0, 16.0, 32.0, 128.0]:
        n = int(c * d * d)
        for seed in range(4):
            rng = np.random.default_rng(1000 * d + 10 * int(c) + seed)
            u = rng.standard_normal(d); u /= np.linalg.norm(u)
            s = 1 / math.sqrt(1 + beta ** 2)
            M = np.zeros((d, d)); v_num = 0.0; done = 0
            while done < n:
                b = min(B, n - done)
                y = rng.standard_normal((b, d)) + beta * rng.choice([-1.0, 1.0], size=b)[:, None] * u
                p = y @ u
                x = y + (s - 1) * p[:, None] * u          # S y
                q = (x * x).sum(1)
                a = q - d - 2
                M += (x * a[:, None]).T @ x
                # off-diagonal entry variance: a^2 * sum_{j != k} x_j^2 x_k^2 / (d(d-1))
                v_num += float((a * a * (q * q - (x ** 4).sum(1))).sum()) / (d * (d - 1))
                done += b
            M /= n; v = v_num / n
            N = M - kappa * np.outer(u, u)
            noise = float(np.abs(np.linalg.eigvalsh(N)).max())
            ev, V = np.linalg.eigh(M)
            sig2 = d * v / n
            ov_pred = math.sqrt(max(0.0, 1 - sig2 / kappa ** 2))
            lam_pred = kappa + sig2 / kappa if sig2 < kappa ** 2 else -2 * math.sqrt(sig2)
            out.append({"d": d, "c": c, "n": n, "seed": seed, "v_over_2d": v / (2 * d), "noise_norm": noise,
                        "edge_pred": 2 * math.sqrt(sig2), "src_pred": 2 * math.sqrt(2) * d / math.sqrt(n),
                        "overlap": float(abs(V[:, 0] @ u)), "overlap_pred": ov_pred,
                        "lam_min": float(ev[0]), "lam_pred": lam_pred, "lam_2": float(ev[1])})
        rs = [r for r in out if r["d"] == d and r["c"] == c]
        f = lambda k: np.mean([r[k] for r in rs])
        print(f"d {d:3d} c {c:6.1f}  v/2d {f('v_over_2d'):.3f}  noise {f('noise_norm'):.3f} edge {f('edge_pred'):.3f} "
              f"(src {f('src_pred'):.3f})  overlap {f('overlap'):.3f} pred {f('overlap_pred'):.3f}  "
              f"lam_min {f('lam_min'):+.3f} pred {f('lam_pred'):+.3f}", flush=True)
json.dump(out, open("t388_check.json", "w"), indent=1)
