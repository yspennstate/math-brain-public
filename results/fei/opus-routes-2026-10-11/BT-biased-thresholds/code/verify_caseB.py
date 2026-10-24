"""Adversarial numeric check of the deterministic inequalities used in Theorem 6.1, Case B, for EVERY
coordinate 0 of random thresholds under random (also extreme) biases:
  (a) E_{>=2}(f) <= 4[(1-q0)E(U)+q0 E(V')] + 8.25[(1-q0)Var U + q0 Var V']
  (b) sum_{j!=0} I_j(f) = (1-q0) I(U) + q0 I(V')
  (c) rho_j <= eps/(q_j(1-q_j)),  eps = 1 - rho_0."""
import numpy as np, math
from biased import ltf_table, g_transform, sigma2_vector, popcount_vector
rng = np.random.default_rng(5)
def stats(T, q):
    n = len(q); g = g_transform(T, q); s2 = sigma2_vector(q); k = popcount_vector(n); P = s2 * g * g
    with np.errstate(divide='ignore', invalid='ignore'):
        lg = np.where(P > 0, np.log(np.where(P > 0, s2 / P, 1)), 0)
    E = float((P * lg)[k > 0].sum()); E2 = float((P * lg)[k >= 2].sum())
    I = float((k * P).sum()); V = float(P[k > 0].sum())
    idx = np.arange(2 ** n); Ii = np.array([P[((idx >> i) & 1) == 1].sum() for i in range(n)])
    return E, E2, I, V, Ii, g
worst_a = -1e9; worst_b = 0; worst_c = -1e9; cnt = 0
for trial in range(1500):
    n = int(rng.integers(3, 10))
    w = np.exp(rng.normal(0, 1.3, n)); th = rng.random() * w.sum(); T = ltf_table(w, th)
    if T.min() == T.max(): continue
    q = 1 / (1 + np.exp(-rng.normal(0, 3.5, n)))
    E, E2, I, V, Ii, g = stats(T, q)
    rho = np.array([g[1 << i] for i in range(n)])
    for z in range(n):
        Tr = T.reshape(-1, 2, 2 ** z)
        u = Tr[:, 0, :].reshape(-1); v = 1 - Tr[:, 1, :].reshape(-1)
        qr = np.delete(q, z)
        EU, _, IU, VU, _, _ = stats(u, qr) if u.min() != u.max() else (0, 0, 0, 0, None, None)
        EV, _, IV, VV, _, _ = stats(v, qr) if v.min() != v.max() else (0, 0, 0, 0, None, None)
        rhs = 4 * ((1 - q[z]) * EU + q[z] * EV) + 8.25 * ((1 - q[z]) * VU + q[z] * VV)
        worst_a = max(worst_a, E2 - rhs)
        worst_b = max(worst_b, abs(Ii.sum() - Ii[z] - ((1 - q[z]) * IU + q[z] * IV)))
        eps = 1 - rho[z]
        for j in range(n):
            if j != z:
                worst_c = max(worst_c, rho[j] - eps / (q[j] * (1 - q[j])))
        cnt += 1
print('cases', cnt)
print('(a) max E2 - rhs (must be <= 0):', worst_a)
print('(b) max |identity error|:', worst_b)
print('(c) max rho_j - eps/(q_j(1-q_j)) (must be <= 0):', worst_c)
