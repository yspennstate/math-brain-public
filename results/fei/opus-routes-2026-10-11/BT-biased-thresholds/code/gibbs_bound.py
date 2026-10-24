"""Exact-normalizer Gibbs bound with the paper's reference adapted to weighted thresholds:
   theta_k(i) = max( sigma_i^2 min(1, (k/Lambda_i)^a), 4 pi_i ),  Lambda_i = sigma-mass of strictly heavier coords,
   B(f) = sum_k [ W_k ln(e_k(theta_k)/W_k) + sum_{|S|=k} P(S) sum_{i in S} ln(sigma_i^2/theta_k(i)) ]  >= E(f).
Reports B/I and E/I, and the version with the paper's normalizer bound ln Z_k <= k + 4m (B_loose)."""
import numpy as np, math, sys, time
from biased import ltf_table, g_transform, sigma2_vector, popcount_vector
def esym(vals, kmax):
    e = np.zeros(kmax + 1); e[0] = 1.0
    for v in vals:
        e[1:] = e[1:] + v * e[:-1]
    return e
def gibbs(T, q, w, a=2.0):
    q = np.asarray(q, float); n = len(q)
    g = g_transform(T, q); s2 = sigma2_vector(q); k = popcount_vector(n)
    P = s2 * g * g
    sig = 4 * q * (1 - q)
    V = P[k > 0].sum(); I = (k * P).sum()
    if V < 1e-300: return None
    idx = np.arange(2 ** n)
    member = ((idx[:, None] >> np.arange(n)) & 1).astype(bool)
    pi = (P[:, None] * member).sum(0) / V          # pi_i = I_i / V
    order = np.argsort(-np.asarray(w), kind='stable')
    Lam = np.zeros(n); acc = 0.0
    for i in order:
        Lam[i] = acc; acc += sig[i]
    B = 0.0; Bl = 0.0; E = 0.0; m = I / V
    for kk in range(1, n + 1):
        sel = (k == kk) & (P > 0)
        Wk = P[sel].sum()
        if Wk <= 0: continue
        th = np.maximum(sig * np.minimum(1.0, np.where(Lam > 0, (kk / np.maximum(Lam, 1e-300)) ** a, 1.0)), 4 * pi)
        th = np.maximum(th, 1e-300)
        Zk = esym(th, kk)[kk]
        cost = (P[sel][:, None] * member[sel] * np.log(sig / th)[None, :]).sum()
        B += Wk * math.log(Zk / Wk) + cost
        Bl += Wk * (kk + 4 * m + math.log(1 / Wk)) + cost   # paper's ln Z_k <= k + 4m
        E += (P[sel] * np.log(s2[sel] / P[sel])).sum()
    return dict(B_over_I=B / I, Bloose_over_I=Bl / I, E_over_I=E / I)
if __name__ == '__main__':
    for s in (4, 6, 8, 10, 12):
        x = 1.0 / s; p = x / 50; a2 = p ** s; ph = a2 * (1 - x) / (x + a2 * (1 - x))
        w = [s] + [1] * s
        T = ltf_table(w, s)
        r = gibbs(T, [ph] + [p] * s, w)
        print('T_s s=%d  exact-normalizer B/I=%.3f  paper-normalizer B/I=%.3f  true E/I=%.3f' % (s, r['B_over_I'], r['Bloose_over_I'], r['E_over_I']), flush=True)
