"""Referee check of the two-cell reduction behind SEL-15 and SEL-8 (NOTES 5.2):
for two cells (h, -h), p = (p1, p2), orthogonal Boolean leaves G1, G2,
  H(F) - [H(p) + sum_k p_k (H(q_k) + H(G_k))] = sum_T R_T [h(cos^2(t_T + alpha)) - h(cos^2 t_T)] - h(p1),
with c(T) = (sqrt p1 G1hat(T), sqrt p2 G2hat(T))/sqrt(R_T) = (cos t_T, sin t_T), sin^2 alpha = p1.
Also: sum_T R_T m_T = 2 p1 p2 (m_T = mass of nu_T off the empty set), and the bent point flip relation to X009:
H(S|T)/delta -> log2(1/delta) + 1/ln2 and I(X;Y)/delta -> 2/ln2.
"""
import math
import numpy as np
from rlib import wht, ent, h2

rng = np.random.default_rng(5)


def orth_partner(G, rng):
    D = len(G)
    flip = np.zeros(D, dtype=bool)
    flip[rng.choice(D, size=D // 2, replace=False)] = True
    return np.where(flip, -G, G)


worst_id = 0.0
worst_m = 0.0
for trial in range(3000):
    a = int(rng.integers(1, 6)); n = int(rng.integers(1, 6))
    N, Dn = 1 << a, 1 << n
    lab = (rng.random(N) < rng.uniform(0.05, 0.95)).astype(np.int64)
    if lab.sum() in (0, N):
        continue
    G1 = rng.choice([-1, 1], size=Dn).astype(np.int64)
    G2 = orth_partner(G1, rng)
    L = lab                                   # cell 1 = label 0, cell 2 = label 1
    F = np.where(L[None, :] == 0, G1[:, None], G2[:, None]).reshape(-1)   # [y, x] -> x + N y
    W = wht(F).astype(np.float64) / (N * Dn)
    P = W ** 2
    HF = float(ent(P))
    p1 = float(np.mean(L == 0)); p2 = 1 - p1
    a1 = (L == 0).astype(np.int64)
    A1 = wht(a1).astype(np.float64) / N
    A2 = wht(1 - a1).astype(np.float64) / N
    q1 = A1 ** 2 / p1; q2 = A2 ** 2 / p2
    g1 = wht(G1).astype(np.float64) / Dn; g2 = wht(G2).astype(np.float64) / Dn
    C010 = float(h2(p1)) + p1 * (float(ent(q1)) + float(ent(g1 ** 2))) + p2 * (float(ent(q2)) + float(ent(g2 ** 2)))
    R = p1 * g1 ** 2 + p2 * g2 ** 2
    alpha = math.asin(math.sqrt(p1))
    rhs = 0.0
    msum = 0.0
    Pm = P.reshape(Dn, N)
    for T in range(Dn):
        if R[T] <= 0:
            continue
        c1 = math.sqrt(p1) * g1[T] / math.sqrt(R[T]); c2 = math.sqrt(p2) * g2[T] / math.sqrt(R[T])
        t = math.atan2(c2, c1)
        mT = math.cos(t + alpha) ** 2
        rhs += R[T] * (float(h2(mT)) - float(h2(math.cos(t) ** 2)))
        # direct: mass of nu_T off the empty selector set
        mdir = 1 - Pm[T, 0] / R[T]
        worst_m = max(worst_m, abs(mdir - mT))
        msum += R[T] * mT
    rhs -= float(h2(p1))
    worst_id = max(worst_id, abs((HF - C010) - rhs), abs(msum - 2 * p1 * p2))
print("two-cell reduction identity: max |LHS - RHS| = %.2e ; max |m_T(direct) - cos^2(t+alpha)| = %.2e" % (worst_id, worst_m))

# X009 relation for the bent point flip
LN2 = math.log(2)
for m in (8, 12, 16):
    idx = np.arange(1 << m)
    s = np.zeros(1 << m, dtype=np.int64)
    for k in range(0, m, 2):
        s ^= ((idx >> k) & 1) & ((idx >> (k + 1)) & 1)
    b = 1 - 2 * s; bp = b.copy(); bp[0] = -bp[0]
    F = np.empty(1 << (m + 1), dtype=np.int64); F[0::2] = b; F[1::2] = bp
    P = (wht(F).astype(np.float64) / (1 << (m + 1))) ** 2
    HF = float(ent(P))
    R = P.reshape(1 << m, 2).sum(axis=1)
    HST = HF - float(ent(R))
    Hb = float(ent((wht(b).astype(np.float64) / (1 << m)) ** 2)); Hbp = float(ent((wht(bp).astype(np.float64) / (1 << m)) ** 2))
    IXY = (HF - (Hb + Hbp) / 2) - HST
    d = 2.0 ** -m
    print("m=%2d  H(S|T)/delta = %.6f (log2(1/delta)+1/ln2 = %.6f)   I(X;Y)/delta = %.6f (2/ln2 = %.6f)" % (
        m, HST / d, m + 1 / LN2, IXY / d, 2 / LN2))
