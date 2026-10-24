# Checks of Proposition 3.16. (1) Algebra: for random frames, cross terms, linear terms and conditioning values X_R, the
# hub value x*(t) = (s - lambda V^2 - 2 L <q, X'> - <b, X'>)/(2t), computed with X_i = (t - beta - L_R)/w_i, equals
# alpha/(2t) + c_0 - sigma t/2 with sigma = lambda v_i^2/w_i^2 + 2 q_i/w_i (fit on five values of t, then compared at
# two more), and |u_R|^2 = 1 + v_i^2/w_i^2. (2) The conditional bound: for comb laws on X_i and a rough hub law, the
# exact conditional density of Q at s given X_R (quadrature over X_i) is at most
# 1/2 + |w_i|^{-1} (3.5 log(1 + 2/|alpha|) + 0.5 log(1 + 2|sigma|)).
import math
import numpy as np
rng = np.random.default_rng(316)

def frame(m):
    Qf, _ = np.linalg.qr(rng.standard_normal((m, 2)))
    return Qf[:, 0], Qf[:, 1]

worst_fit = 0.0; worst_u = 0.0; worst_ratio = 0.0; cases = 0
for trial in range(400):
    m = int(rng.integers(3, 9)); w, v = frame(m)
    q = rng.standard_normal(m) * rng.choice([0.01, 0.3, 1.0]); b = rng.standard_normal(m)
    lam = rng.choice([-1, 1]) * rng.uniform(0.5, 3); beta = rng.uniform(-1, 1); s = rng.uniform(-2, 2)
    i = int(np.argmax(np.abs(w))); R = [j for j in range(m) if j != i]
    XR = rng.uniform(-2, 2, m - 1)
    LR = w[R] @ XR
    def xstar(t):
        Xi = (t - beta - LR) / w[i]
        X = np.empty(m); X[i] = Xi; X[R] = XR
        L, V = w @ X, v @ X
        return (s - lam * V ** 2 - 2 * L * (q @ X) - b @ X) / (2 * t)
    ts = np.array([0.1, 0.23, -0.37, 0.61, -0.88])
    A = np.stack([1 / (2 * ts), np.ones_like(ts), -ts / 2], axis=1)
    coef, *_ = np.linalg.lstsq(A, np.array([xstar(t) for t in ts]), rcond=None)
    alpha, c0, sigma = coef
    for t in (0.05, -0.5):
        worst_fit = max(worst_fit, abs(alpha / (2 * t) + c0 - sigma * t / 2 - xstar(t)) / (1 + abs(xstar(t))))
    worst_fit = max(worst_fit, abs(sigma - (lam * v[i] ** 2 / w[i] ** 2 + 2 * q[i] / w[i])) / (1 + abs(sigma)))
    uR = v[R] - (v[i] / w[i]) * w[R]
    worst_u = max(worst_u, abs(uR @ uR - (1 + v[i] ** 2 / w[i] ** 2)))
    # (2) exact conditional density at s: X_i uniform on T teeth of width 1/T, hub rough (random unit-measure union of cells)
    T = int(rng.integers(1, 6)); teeth = np.sort(rng.uniform(-3, 3, T)) if T > 1 else np.array([-0.5])
    cell = rng.choice([0.05, 0.2]); ncell = int(round(2 / cell)); hub_cells = rng.choice(ncell, ncell // 2, replace=False)
    def fh(x):
        k = np.floor((x + 1) / cell).astype(int)
        return np.isin(k, hub_cells) & (x >= -1) & (x < 1)
    xi = (teeth[:, None] + (np.arange(4000)[None, :] + 0.5) / (4000 * T)).ravel()   # quadrature nodes, weight 1/(4000 T)
    t = w[i] * xi + LR + beta
    Xall = np.empty((len(xi), m)); Xall[:, i] = xi; Xall[:, R] = XR
    L, V = Xall @ w, Xall @ v
    xs = (s - lam * V ** 2 - 2 * L * (Xall @ q) - Xall @ b) / (2 * t)
    dens = np.sum(fh(xs) / (2 * np.abs(t))) / (4000 * T)
    bound = 0.5 + (3.5 * math.log(1 + 2 / abs(alpha)) + 0.5 * math.log(1 + 2 * abs(sigma))) / abs(w[i])
    worst_ratio = max(worst_ratio, dens / bound); cases += 1
print("algebra: largest relative misfit %.2e over %d cases (sigma formula and the form alpha/(2t) + c0 - sigma t/2)" % (worst_fit, cases))
print("|u_R|^2 - (1 + v_i^2/w_i^2): largest %.2e" % worst_u)
print("conditional density / conditional bound: largest %.3f" % worst_ratio)
