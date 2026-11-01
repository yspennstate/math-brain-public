"""T262 Target 3 (agent A, 20 Oct): critical tanh (W ~ N(0, 1/n), no bias), two inputs at angle theta0, q0 = 1.
Prediction. Small q: E tanh u tanh v = q12 (1 - 2q + 5q^2 + (2/3) q^2 c^2) + ..., so the infinite-width correlation moves only by
O(q^2) per layer; with q_l ~ 1/(2l) the total is summable and c_l -> c_inf(theta0) < 1 (no degeneration, unlike ReLU). At L = t n the
network is linear to leading order, the 2 x 2 Gram is a Wishart chain, and the Fisher z = atanh(c) of each layer's sample correlation
moves by c/(2n) in mean and 1/n in variance. Limit: dz = (1/2) tanh z ds + dB, z_0 = atanh(c_inf).
Net: exact reduction (rotation invariance) - given layer l, the next preactivations are n iid pairs with covariance Gram/n.
usage: python tanh_two_input.py n1,n2 reps theta0"""
import sys, numpy as np
try:
    import psutil; psutil.Process().nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
except Exception:
    pass
ns = [int(v) for v in sys.argv[1].split(",")]; R = int(sys.argv[2]); th0 = float(sys.argv[3])
ts = [0.25, 0.5, 1.0, 2.0]; qs = [0.1, 0.25, 0.5, 0.75, 0.9]
# infinite-width map by 2-D Gauss-Hermite
xg, wg = np.polynomial.hermite_e.hermegauss(60); wg = wg / wg.sum()
X, Y = np.meshgrid(xg, xg, indexing='ij'); Wt = np.outer(wg, wg)
q1 = q2 = 1.0; c = np.cos(th0); cl = {}
for l in range(1, 20001):
    a, b = np.sqrt(q1), np.sqrt(q2)
    u = a * X; v = b * (c * X + np.sqrt(1 - c * c) * Y)
    tu, tv = np.tanh(u), np.tanh(v)
    q1n, q2n, q12 = (Wt * tu * tu).sum(), (Wt * tv * tv).sum(), (Wt * tu * tv).sum()
    q1, q2 = q1n, q2n; c = q12 / np.sqrt(q1 * q2)
    if l in (1, 2, 5, 10, 100, 1000, 5000, 10000, 20000): cl[l] = c
print("infinite-width c_l:", " ".join(f"l {k}: {v:.6f}" for k, v in cl.items()), flush=True)
cinf = 2 * cl[20000] - cl[10000]  # the remainder decays like 1/l
print(f"c_inf (Richardson on 10k/20k) {cinf:.6f}, theta_inf {np.arccos(cinf):.6f}", flush=True); z0 = np.arctanh(cinf)
# the limit diffusion
rng = np.random.default_rng(2620); P, m = 50000, 2000; z = np.full(P, z0); s = 0.0; ds = 2.0 / m; lim = {}
for j in range(m):
    z = z + 0.5 * np.tanh(z) * ds + np.sqrt(ds) * rng.standard_normal(P); s += ds
    for t in ts:
        if abs(s - t) < ds / 2: lim[t] = np.quantile(z, qs), z.mean(), z.std()
for t in ts:
    qq, mu, sd = lim[t]; print(f"limit t {t}: z quantiles " + " ".join(f"{v:.3f}" for v in qq) + f" | mean {mu:.3f} sd {sd:.3f}", flush=True)
for n in ns:
    x1 = np.ones((R, n)) * 0; g = rng.standard_normal((R, n)); gp = rng.standard_normal((R, n))
    # layer-0 inputs: |x|^2 = n (q0 = 1), angle th0
    x1 = g / np.linalg.norm(g, axis=1, keepdims=True) * np.sqrt(n)
    e = gp - (gp * x1).sum(1, keepdims=True) / n * x1; e = e / np.linalg.norm(e, axis=1, keepdims=True) * np.sqrt(n)
    x2 = np.cos(th0) * x1 + np.sin(th0) * e
    Ls = {int(round(t * n)): t for t in ts}
    for l in range(1, max(Ls) + 1):
        A = (x1 * x1).sum(1) / n; B = (x2 * x2).sum(1) / n; C = (x1 * x2).sum(1) / n
        cc = np.clip(C / np.sqrt(A * B), -1, 1)
        g = rng.standard_normal((R, n)); gp = rng.standard_normal((R, n))
        x1 = np.tanh(np.sqrt(A)[:, None] * g)
        x2 = np.tanh(np.sqrt(B)[:, None] * (cc[:, None] * g + np.sqrt(1 - cc * cc)[:, None] * gp))
        if l in Ls:
            A = (x1 * x1).sum(1); B = (x2 * x2).sum(1); C = (x1 * x2).sum(1)
            zz = np.arctanh(np.clip(C / np.sqrt(A * B), -1 + 1e-15, 1 - 1e-15))
            print(f"net n {n} t {Ls[l]}: z quantiles " + " ".join(f"{v:.3f}" for v in np.quantile(zz, qs)) +
                  f" | mean {zz.mean():.3f} sd {zz.std():.3f} (se {zz.std() / np.sqrt(R):.3f}) | median q {np.median(A / n):.2e}", flush=True)
