"""Gibbs bounds for E with level-conditioned product references, exact normalizers:
  paper-type:   theta_k(i) = max(sigma_i^2 min(1,(k/Lam_i)^a), 4 pi_i)          (pi_i global inclusion prob.)
  level-dep.:   theta_k(i) = max(sigma_i^2 min(1,(k/Lam_i)^a), c pi_i^(k))      (pi_i^(k) inclusion prob. inside level k)
Both are upper bounds for E (Gibbs). Report bound/I. Brute force over 2^n sets (n <= 16)."""
import numpy as np, math, sys
from biased import ltf_table, g_transform, sigma2_vector, popcount_vector
def esym(vals, kmax):
    e = np.zeros(kmax + 1); e[0] = 1.0
    for v in vals: e[1:] = e[1:] + v * e[:-1]
    return e
def bounds(T, q, w, a=1.2, c=4.0):
    q = np.asarray(q, float); n = len(q)
    g = g_transform(T, q); s2 = sigma2_vector(q); k = popcount_vector(n); P = s2 * g * g
    sig = 4 * q * (1 - q); V = P[k > 0].sum(); I = (k * P).sum()
    idx = np.arange(2 ** n); member = ((idx[:, None] >> np.arange(n)) & 1).astype(bool)
    pi = (P[:, None] * member).sum(0) / V
    order = np.argsort(-np.asarray(w), kind='stable'); Lam = np.zeros(n); acc = 0.0
    for i in order: Lam[i] = acc; acc += sig[i]
    E = float(np.sum((P * np.log(np.where(P > 0, s2 / np.where(P > 0, P, 1), 1)))[k > 0]))
    Bp = 0.0; Bl = 0.0
    for kk in range(1, n + 1):
        sel = (k == kk) & (P > 0); Wk = P[sel].sum()
        if Wk <= 0: continue
        rankw = sig * np.minimum(1.0, (kk / np.maximum(Lam, 1e-300)) ** a)
        pik = (P[sel][:, None] * member[sel]).sum(0) / Wk
        for which, th in ((0, np.maximum(rankw, 4 * pi)), (1, np.maximum(rankw, c * pik))):
            th = np.maximum(th, 1e-300)
            Zk = esym(th, kk)[kk]
            cost = (P[sel][:, None] * member[sel] * np.log(sig / th)[None, :]).sum()
            val = Wk * math.log(Zk / Wk) + cost
            if which == 0: Bp += val
            else: Bl += val
    return E / I, Bp / I, Bl / I
if __name__ == '__main__':
    print('T_s family (x=1/s, p=x/50):')
    for s in (4, 8, 12):
        x = 1.0 / s; p = x / 50; a2 = p ** s; ph = a2 * (1 - x) / (x + a2 * (1 - x))
        w = [s] + [1] * s
        print('  s=%d  E/I=%.3f  paper-ref B/I=%.3f  level-dep B/I=%.3f' % ((s,) + bounds(ltf_table(w, s), [ph] + [p] * s, w)), flush=True)
    print('three-class family OR(y0, AND(s lights, [Z >= t])) as 1[W y0 + L + cZ >= s + c t]:')
    for (s, N, t) in ((4, 8, 5), (6, 8, 5), (8, 7, 4), (10, 5, 3)):
        x = 1.0 / s; p = x / 50; qz = 0.5
        from math import comb
        PM = sum(comb(N, j) * 0.5 ** N for j in range(t, N + 1))
        a2 = p ** s * PM; ph = a2 * (1 - x) / (x + a2 * (1 - x))
        cz = 1.0 / (N + 1); W0 = s + cz * t + 1
        w = [W0] + [1.0] * s + [cz] * N; th = s + cz * t
        T = ltf_table(w, th)
        q = [ph] + [p] * s + [qz] * N
        print('  s=%d N=%d t=%d  E/I=%.3f  paper-ref B/I=%.3f  level-dep B/I=%.3f' % ((s, N, t) + bounds(T, q, w)), flush=True)
