"""Independent check of T255 section 13 (Cor 4.3, m >= 3): generator of Y = a^-q + |w|^2 + M psi^p, psi = (tr X + 1)/a, on the
corner region D, built from scratch: drift b (section 1) + b_res (paper Thm 3.2), covariance written entrywise -
  c-part and MLP part: (c + 2 gamma^2)(V_ac V_bd + V_ad V_bc);
  attention N-part: k^2 (V_ac Q_bd + V_ad Q_bc + V_bc Q_ad + V_bd Q_ac), Q = V P V P V  (from L(dN K + K dN^T)L^T, K = L^T P L);
exact sympy gradient/Hessian of Y in the upper-triangle entries. No code from lyapY_mlp.py / gen.py. Reports max LY/(|W|^2 Y)."""
import sys, random, json
import sympy as sp
from mpmath import mp, mpf, sqrt, acos, pi, matrix
mp.dps = 110


def build(m, q, p, M, old=False):
    idx = [(i, j) for i in range(m) for j in range(i, m)]
    s = {ij: sp.Symbol(f"v{ij[0]}{ij[1]}") for ij in idx}
    V = sp.Matrix(m, m, lambda i, j: s[(min(i, j), max(i, j))])
    a = V[0, 0]; w2 = sum(V[i, 0] ** 2 for i in range(1, m)) / a ** 2
    trX = sum(V[i, i] for i in range(1, m)) - sum(V[i, 0] ** 2 for i in range(1, m)) / a
    Y = a ** (-q) + w2 + M * ((trX / a) if old else ((trX + 1) / a)) ** p
    syms = [s[ij] for ij in idx]
    g = [sp.diff(Y, x) for x in syms]
    H = [[sp.diff(gi, x) for x in syms] for gi in g]
    f = sp.lambdify(syms, [Y, g, H], "mpmath")
    return idx, f


def gen(V, m, g2, tau0, Delta):
    P = matrix(m, m)
    for i in range(m):
        for j in range(m): P[i, j] = (1 if i == j else 0) - mpf(1) / m
    W = P * V * P; W2 = sum(W[i, j] ** 2 for i in range(m) for j in range(m))
    v = [V[i, i] for i in range(m)]; trW = sum(W[i, i] for i in range(m))
    D = matrix([W[i, i] - trW / m for i in range(m)])
    VD = V * D
    b = matrix(m, m)
    for i in range(m):
        for j in range(m):
            b[i, j] = (g2 / tau0 ** 2) * (V[i, j] * W2 / m ** 2 + (v[i] * VD[j] + VD[i] * v[j]) / (2 * m))
            if i != j:
                rho = V[i, j] / sqrt(V[i, i] * V[j, j])
                nu = Delta / (2 * pi) * (sqrt(1 - rho ** 2) - rho * acos(rho))
                b[i, j] += g2 * nu * sqrt(V[i, i] * V[j, j])
    c = g2 * (2 - g2); k = g2 / (m * tau0); Q = V * P * V * P * V
    return b, W2, (c + 2 * g2), k, Q


def LY(V, m, g2, tau0, Delta, idx, f):
    b, W2, cl, k, Q = gen(V, m, g2, tau0, Delta)
    Y, g, H = f(*[V[i, j] for (i, j) in idx])
    drift = sum(g[r] * b[i, j] for r, (i, j) in enumerate(idx))
    qv = 0
    for r, (a_, b_) in enumerate(idx):
        for t, (c_, d_) in enumerate(idx):
            cov = cl * (V[a_, c_] * V[b_, d_] + V[a_, d_] * V[b_, c_]) + \
                k ** 2 * (V[a_, c_] * Q[b_, d_] + V[a_, d_] * Q[b_, c_] + V[b_, c_] * Q[a_, d_] + V[b_, d_] * Q[a_, c_])
            qv += H[r][t] * cov
    return (drift + qv / 2) / (W2 * Y)


def sample(m, rng, delta=0.05, amin=2, amax=10, phimin=-40):
    a = mpf(10) ** rng.uniform(amin, amax)
    w = [rng.gauss(0, 1) for _ in range(m - 1)]; nw = sum(x * x for x in w) ** 0.5
    rw = delta * rng.random() ** 0.5 * (rng.random() if rng.random() < 0.3 else 1)
    w = [mpf(x) / nw * rw for x in w]
    if rng.random() < 0.2: w = [mpf(0)] * (m - 1)
    A = matrix(m - 1, m - 1)
    for i in range(m - 1):
        for j in range(m - 1): A[i, j] = rng.gauss(0, 1)
    X = A * A.T + matrix(m - 1, m - 1) * 0
    if rng.random() < 0.3:  # near-degenerate shapes
        for i in range(m - 1): X[i, i] += mpf(10) ** rng.uniform(-12, 0)
    trX = sum(X[i, i] for i in range(m - 1))
    phi = mpf(10) ** rng.uniform(phimin, mp.log10(delta))
    X = X * (phi * a / trX)
    V = matrix(m, m); V[0, 0] = a
    for i in range(1, m):
        V[i, 0] = V[0, i] = a * w[i - 1]
        for j in range(1, m): V[i, j] = X[i - 1, j - 1] + a * w[i - 1] * w[j - 1]
    return V


if __name__ == "__main__":
    rng = random.Random(int(sys.argv[1]) if len(sys.argv) > 1 else 20261017)
    out = []
    for m, g2, Delta in ((3, 1, 1), (3, 0.5, 1), (3, 1, 4), (4, 1, 1), (4, 0.3, 4), (5, 1, 1), (3, 0.1, 1), (6, 1, 2)):
        for old in (False, True):
            idx, f = build(m, sp.Rational(1, 10), sp.Rational(1, 10), 10, old)
            worst = None
            for _ in range(150):
                V = sample(m, rng)
                r = LY(V, m, mpf(g2), mpf(1), mpf(Delta), idx, f)
                if worst is None or r > worst[0]:
                    worst = (r, float(V[0, 0]), float(sum(V[i, i] for i in range(1, m)) / V[0, 0]))
            rec = {"m": m, "g2": g2, "Delta": Delta, "Y": "old" if old else "new", "max_ratio": mp.nstr(worst[0], 4),
                   "at_a": worst[1], "at_trVpp_over_a": worst[2]}
            print(json.dumps(rec), flush=True); out.append(rec)
