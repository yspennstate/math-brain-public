"""T262 one-layer check of the joint generator (agent A, 19 Oct): at theta = phi/n, n * Var dlog theta (pred 2),
n * Var dlog|h|^2 (pred 5), n * Cov (pred -2), n * E dlog theta (pred -1 - phi/(3 pi)), n * E dlog|h|^2 (pred -5/2)."""
import numpy as np
rng = np.random.default_rng(7)
for n in (400, 1600):
    for phi in (2.0, 10.0):
        th = phi / n; R = 20000 if n == 400 else 5000; dt, dh = [], []
        for _ in range(R // 1000):
            g = rng.standard_normal((1000, n)); gp = rng.standard_normal((1000, n))
            h1 = np.maximum(g, 0) * np.sqrt(2 / n); h2 = np.maximum(np.cos(th) * g + np.sin(th) * gp, 0) * np.sqrt(2 / n)
            n1 = np.linalg.norm(h1, axis=1); n2 = np.linalg.norm(h2, axis=1); u1 = h1 / n1[:, None]; u2 = h2 / n2[:, None]
            t2 = 2 * np.arctan2(np.linalg.norm(u1 - u2, axis=1), np.linalg.norm(u1 + u2, axis=1))
            dt.append(np.log(t2 / th)); dh.append(2 * np.log(n1))
        dt = np.concatenate(dt); dh = np.concatenate(dh); C = np.cov(dt, dh)
        print(f"n {n} phi {phi:4.1f}: nVar dlogth {n*C[0,0]:.2f} (2)  nVar dlog|h|^2 {n*C[1,1]:.2f} (5)  nCov {n*C[0,1]:+.2f} (-2)  "
              f"nE dlogth {n*dt.mean():+.2f} ({-1-phi/(3*np.pi):+.2f})  nE dlog|h|^2 {n*dh.mean():+.2f} (-2.50)", flush=True)
