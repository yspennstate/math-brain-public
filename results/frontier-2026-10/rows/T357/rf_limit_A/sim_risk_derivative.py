"""T357 (agent A, 20 Oct 2026): independent check of lam_risk at finite n by direct simulation of the Gaussian-equivalent
design, to decide between risk_gap_coefficient.py and the rf_cgmt.py fixed point (they disagree by 1.5-2x at large alpha).
u = mu1 F x + mus xi (x ~ N(0, I_d), xi ~ N(0, I_N)), y ~ Bernoulli(sig(beta x_1)), w_hat = ridge logistic fit (no intercept).
Exact at every n: dR(w_hat_lam)/dlam = -grad R(w_hat) . (Hh + lam)^{-1} w_hat, with the population gradient in closed form
grad R(w) = Vh(|w|_Sig) Sig w - kappa m (Stein; Vh(q) = E sig'(q g)). The zero of its mean over reps is lam_risk.
argv: beta alpha psi d reps [seed]   (F as rf_ridge_inf.py with its seed argument, 100 = rf_cgmt.py's F)"""
import sys, math
import numpy as np
beta, alpha, psi = map(float, sys.argv[1:4]); d, reps = int(sys.argv[4]), int(sys.argv[5])
seed = int(sys.argv[6]) if len(sys.argv) > 6 else 100
sig = lambda t: 0.5 * (1 + np.tanh(t / 2))
hx, hw = np.polynomial.hermite_e.hermegauss(120); hw = hw / hw.sum()
mu1 = (hw * (1 - np.tanh(hx) ** 2)).sum(); mus2 = (hw * np.tanh(hx) ** 2).sum() - mu1 ** 2
kap = (hw * sig(beta * hx) * hx).sum()
N = int(psi * d); n = int(alpha * d)
F = np.random.default_rng(seed).standard_normal((N, d)) / math.sqrt(d)
Sig = mu1 ** 2 * F @ F.T + mus2 * np.eye(N); m = mu1 * F[:, 0]
Vh = lambda q: (hw * sig(q * hx) * (1 - sig(q * hx))).sum()
def gradR(w):
    q = math.sqrt(w @ Sig @ w); return Vh(q) * (Sig @ w) - kap * m
lams = np.array([0.25, 0.5, 0.75, 1.0, 1.25]) / alpha * 0.08
print(__doc__); print(f"beta {beta} alpha {alpha} N {N} d {d} n {n} reps {reps} seed {seed}; lam grid {lams}")
rng = np.random.default_rng(12345)
acc = np.zeros((reps, len(lams)))
for r in range(reps):
    x = rng.standard_normal((n, d)); U = mu1 * x @ F.T + math.sqrt(mus2) * rng.standard_normal((n, N))
    y = (rng.random(n) < sig(beta * x[:, 0])).astype(float); del x
    w = np.zeros(N)
    for j, lam in enumerate(lams[::-1]):                 # warm start from the largest lam
        for _ in range(30):
            z = U @ w; p = sig(z); g = U.T @ (p - y) / n + lam * w
            Hh = (U * (p * (1 - p))[:, None]).T @ U / n
            step = np.linalg.solve(Hh + lam * np.eye(N), g); w -= step
            if np.abs(step).max() < 1e-12: break
        z = U @ w; p = sig(z); Hh = (U * (p * (1 - p))[:, None]).T @ U / n
        acc[r, len(lams) - 1 - j] = -gradR(w) @ np.linalg.solve(Hh + lam * np.eye(N), w)
    if (r + 1) % 10 == 0 or r + 1 == reps:
        mu_ = acc[:r + 1].mean(0); se = acc[:r + 1].std(0, ddof=1) / math.sqrt(r + 1) if r else np.zeros(len(lams))
        sl, ic = np.polyfit(lams, mu_, 1)
        print(f"  reps {r + 1}: mean dR/dlam " + " ".join(f"{a:+.4e}({b:.1e})" for a, b in zip(mu_, se))
              + f"  -> linear zero lam_risk {-ic / sl:.4e}  alpha*lam_risk {-ic / sl * alpha:.4f}", flush=True)
