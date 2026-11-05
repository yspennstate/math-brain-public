"""T388 review, part 2a: is the source's 16x gap between one-pass Oja and offline FOBI a property of streaming, or of
its step rule? (source ff4dc32f, t388_oja.py: eta = 2 log n/(|kappa| n) constant, uniform random start).

Same data stream, several step rules run side by side on it, plus the offline FOBI eigenvector of the same samples.
Oja on the signed matrices A_i = -a_i x_i x_i^T (top eigenvector of E A = |kappa| u u^T, gap |kappa|):
    w <- normalize(w + eta_t A_i w)
Variance proxy (computed, not assumed): V = ||E[(A - EA)^2]|| ~ E[a^2 |x|^2 x_j^2] = 2(d+2)^2 + 8(d+2) for the
Gaussian part (size-biasing x_j^2 makes |x|^2 a chi-square on d+2 dof).
Rules: src = source constant step; dec(alpha, beta) = alpha/(|kappa| (beta + t)) as in Jain et al. 2016 (1602.06929),
beta in units of V/kappa^2.
usage: python t388_oja_check.py -> t388_oja_check.json
"""
import json, math
import numpy as np

beta_m = 1.0
kappa = -2 * beta_m ** 4 / (1 + beta_m ** 2) ** 2
d = 32
V = 2 * (d + 2) ** 2 + 8 * (d + 2)
B0 = V / kappa ** 2
RULES = [("src", None, None), ("dec a1 b1", 1.0, 1.0), ("dec a2 b1", 2.0, 1.0), ("dec a2 b4", 2.0, 4.0),
         ("dec a4 b4", 4.0, 4.0)]
out = []
for c in [32.0, 128.0, 512.0]:
    n = int(c * d * d)
    for seed in range(3):
        rng = np.random.default_rng(77 + 1000 * int(c) + seed)
        u = rng.standard_normal(d); u /= np.linalg.norm(u)
        s = 1 / math.sqrt(1 + beta_m ** 2)
        y = rng.standard_normal((n, d)) + beta_m * rng.choice([-1.0, 1.0], size=n)[:, None] * u
        X = y + (s - 1) * (y @ u)[:, None] * u
        a = (X * X).sum(1) - d - 2
        M = (X * a[:, None]).T @ X / n
        off = float(abs(np.linalg.eigh(M)[1][:, 0] @ u))
        w0 = rng.standard_normal(d); w0 /= np.linalg.norm(w0)
        W = np.tile(w0, (len(RULES), 1))
        t = np.arange(n, dtype=float)
        etas = np.empty((len(RULES), n))
        for k, (_, al, be) in enumerate(RULES):
            etas[k] = 2 * math.log(n) / (abs(kappa) * n) if al is None else al / (abs(kappa) * (be * B0 + t))
        for i in range(n):
            xi = X[i]
            W += (etas[:, i] * (-a[i]) * (W @ xi))[:, None] * xi
            W /= np.linalg.norm(W, axis=1)[:, None]
        ov = [float(abs(W[k] @ u)) for k in range(len(RULES))]
        out.append({"c": c, "n": n, "seed": seed, "offline": off, "oja": dict(zip([r[0] for r in RULES], ov))})
        print(f"c {c:5.0f} seed {seed}  offline {off:.3f}  " + "  ".join(f"{r[0]} {o:.3f}" for r, o in zip(RULES, ov)),
              flush=True)
json.dump({"d": d, "V": V, "V_over_kappa2": B0, "runs": out}, open("t388_oja_check.json", "w"), indent=1)
