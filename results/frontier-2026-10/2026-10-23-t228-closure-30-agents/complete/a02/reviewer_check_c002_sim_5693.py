"""Independent check of T336-w727-C002 v1: build the attention layers as literal Q,K,V matrices and run them (claude-5693aca3)."""
import numpy as np, math
rng = np.random.default_rng(7)
relu = lambda x: np.maximum(x, 0)

def build_and_run(Z, y, q, n, s, B, R, eps):
    p = Z.shape[1] if len(Z) else q.shape[0]
    t = len(Z); N = n + 1
    # registers
    o = {}
    for i, nm in enumerate(["zc", "zq", "qbar", "w", "u", "wold", "uold"]):
        o[nm] = slice(i * p, (i + 1) * p)
    Y, ONE, MO, VO = 7 * p, 7 * p + 1, 7 * p + 2, 7 * p + 3
    D = 7 * p + 4
    H = np.zeros((N, D)); H[:, ONE] = 1; H[:, VO] = s
    for i in range(t):
        H[i, o["zc"]] = Z[i]; H[i, Y] = y[i]
    H[t, o["zq"]] = q
    def layer(H, heads):
        out = H.copy()
        for Q, K, V in heads:
            S = relu((H @ Q.T) @ (H @ K.T).T)  # S[i,j]=relu(<Q h_i, K h_j>)
            out += S @ (H @ V.T) / N
        return out
    def E(rows, cols, vals, shape=(D, D)):
        M = np.zeros(shape)
        for r, c, v in zip(rows, cols, vals): M[r, c] += v
        return M
    idx = lambda nm: list(range(D))[o[nm]]
    # broadcast
    Qb = E([0], [ONE], [1]); Kb = E([0], [ONE], [1])
    Vb = E(idx("qbar"), idx("zq"), [N] * p)
    H = layer(H, [(Qb, Kb, Vb)])
    nplus = max(1, n); L = s + nplus * R**2; kap = L / s; M = n * R**2 * B / s
    delta = min(0.5, s / (2 * R**2), math.sqrt(s * eps) / (1 + M), s * math.sqrt(eps) / R**2)
    T = math.ceil(math.sqrt(kap) / 2 * math.log(2 / delta))
    c, d = (L + s) / 2, (L - s) / 2; a = c / d
    Cheb = [1.0, a]
    for j in range(T + 2): Cheb.append(2 * a * Cheb[-1] - Cheb[-2])
    for j in range(T):
        eta = 1 / c if j == 0 else 2 * Cheb[j] / (d * Cheb[j + 1])
        beta = 0.0 if j == 0 else Cheb[j - 1] / Cheb[j + 1]
        # head1/2: Q=(w,one) K=(-zc,y) placed in first p+1 coords
        Q1 = E(list(range(p)) + [p], idx("w") + [ONE], [1] * (p + 1))
        K1 = E(list(range(p)) + [p], idx("zc") + [Y], [-1] * p + [1])
        V1 = E(idx("w"), idx("zc"), [N * eta] * p)
        Q2, V2 = -Q1, -V1
        Q3 = E(list(range(p)), idx("u"), [1] * p); K3 = E(list(range(p)), idx("zc"), [1] * p)
        V3 = E(idx("u"), idx("zc"), [-N * eta] * p)
        Q4, V4 = -Q3, -V3
        V5 = np.zeros((D, D))
        for k in range(p):
            w, wo, u, uo, qb = idx("w")[k], idx("wold")[k], idx("u")[k], idx("uold")[k], idx("qbar")[k]
            V5[w, w] += beta - eta * s; V5[w, wo] += -beta
            V5[u, u] += beta - eta * s; V5[u, uo] += -beta; V5[u, qb] += eta
            V5[wo, w] += 1; V5[wo, wo] += -1
            V5[uo, u] += 1; V5[uo, uo] += -1
        H = layer(H, [(Q1, K1, V1), (Q2, K1, V2), (Q3, K3, V3), (Q4, K3, V4), (Qb, Kb, V5)])
    Qr = E(list(range(p)), idx("qbar"), [1] * p); Kw = E(list(range(p)), idx("w"), [1] * p); Ku = E(list(range(p)), idx("u"), [1] * p)
    Vm = E([MO], [ONE], [1]); Vv = E([VO], [ONE], [s])
    H = layer(H, [(Qr, Kw, Vm), (-Qr, Kw, -Vm), (Qr, Ku, Vv), (-Qr, Ku, -Vv)])
    return H[t, MO], H[t, VO], T

worst = 0; cases = 0
for trial in range(400):
    p = int(rng.integers(1, 5)); n = int(rng.integers(0, 40)); t = int(rng.integers(0, n + 1))
    s = float(10 ** rng.uniform(-1.5, 1)); B = float(rng.uniform(0, 3)); R = float(10 ** rng.uniform(-0.5, 0.7)); eps = float(10 ** rng.uniform(-6, -1))
    def feat():
        v = rng.normal(size=p); return v / np.linalg.norm(v) * R * rng.uniform(0, 1) ** 0.3
    Z = np.array([feat() for _ in range(t)]).reshape(t, p)
    y = rng.uniform(-B, B, size=t) * (rng.random() < 0.5 or 1) ; y = np.sign(y) * B if rng.random() < 0.3 else y
    q = feat()
    A = s * np.eye(p) + Z.T @ Z; b = Z.T @ y
    m = q @ np.linalg.solve(A, b); v = s + s * q @ np.linalg.solve(A, q)
    mh, vh, T = build_and_run(Z, y, q, n, s, B, R, eps)
    kl = 0.5 * (math.log(vh / v) + (v + (m - mh) ** 2) / vh - 1)
    ratio = kl / eps; worst = max(worst, ratio); cases += 1
    assert vh >= s - 1e-12, (vh, s)
print("cases", cases, "max KL/eps", worst)

