"""T238 target 2: the alpha window for a quadratic-activation student, via the exact matrix ODE.
Student alpha m^-1 sum_j a_j (w_j . x)^2 with +- pairs sharing w_j(0) ~ N(0, I/d), m -> infinity, gradient flow on the
empirical square loss. Each w_j moves by a linear ODE w' = -/+ G w with G = (1/n) sum_i r_i x_i x_i^T, so the predictor
is x^T M x with M = P - Q, P' = -(G P + P G), Q' = +(G Q + Q G), P(0) = Q(0) = c I, c proportional to alpha / d
(time rescaled by alpha, as in Chizat-Oyallon-Bach). Lazy limit (c -> infinity): M' = -4 c G, which converges to the
minimum-Frobenius interpolant M_lin. Teacher y = (v . x)^2, |v| = 1, n samples.
Runs the multiplicative flow to train MSE < tol and reports, on 2000 test points:
test MSE / Var y, and |f - f_lin|^2 / Var y (distance to the linearized predictor).
usage: python3 window.py d n seed"""
import sys
import numpy as np

d, n, seed = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
rng = np.random.default_rng(seed)
v = rng.standard_normal(d); v /= np.linalg.norm(v)
X = rng.standard_normal((n, d)); y = (X @ v) ** 2
Xt = rng.standard_normal((2000, d)); yt = (Xt @ v) ** 2
F = np.einsum("ni,nj->nij", X, X).reshape(n, -1)
m_lin = np.linalg.lstsq(F, y, rcond=None)[0].reshape(d, d); m_lin = (m_lin + m_lin.T) / 2
Lf = np.linalg.eigvalsh(F @ F.T / n).max()
pred = lambda Mx, Z: np.einsum("ni,ij,nj->n", Z, Mx, Z)
f_lin = pred(m_lin, Xt); vy = yt.var()
ev = np.sort(np.abs(np.linalg.eigvalsh(m_lin)))[::-1]
print("d %d n %d n/d^2 %.3f seed %d | lazy limit (min-Frobenius): test %.4f | M_lin top eig %.3f, bulk median %.4f, bulk rms %.4f" % (
    d, n, n / d ** 2, seed, ((f_lin - yt) ** 2).mean() / vy, ev[0], np.median(ev[1:]), np.sqrt((ev[1:] ** 2).mean())))
cs = [float(s) for s in sys.argv[4].split(",")] if len(sys.argv) > 4 else [1e-6, 1e-4, 1e-3, 1e-2, 3e-2, 0.1, 0.3, 1, 3, 10, 100]
for c in cs:
    P = c * np.eye(d); Q = c * np.eye(d)
    steps = 0
    while True:
        M = P - Q
        r = pred(M, X) - y
        tr = (r ** 2).mean()
        if tr < 1e-10 or steps > 400000:
            break
        G = (X * r[:, None]).T @ X / n
        lam = np.abs(np.linalg.eigvalsh(G)).max()
        scale = np.linalg.eigvalsh(P + Q).max()
        eta = min(0.2 / (lam + 1e-12), 0.4 / (2 * scale * Lf))  # Lf: top eigenvalue of the feature Gram F F^T / n
        A = np.eye(d) - eta * G; B = np.eye(d) + eta * G
        P = A @ P @ A; Q = B @ Q @ B
        steps += 1
    M = P - Q; f = pred(M, Xt)
    sv = np.sort(np.abs(np.linalg.eigvalsh(M)))[::-1]
    print("c %8.0e (alpha ~ c d = %8.2e) | steps %6d train %.1e | test %.4f | dist to lazy %.4f | top eigs %.3f %.3f %.3f" % (
        c, c * d, steps, tr, ((f - yt) ** 2).mean() / vy, ((f - f_lin) ** 2).mean() / vy, sv[0], sv[1], sv[2]), flush=True)
