"""Numerical checks of the exact identities and the rank lemma (float; identities to ~1e-12)."""
import numpy as np, math, sys
from biased import ltf_table, g_transform, sigma2_vector, popcount_vector, law_vector
rng = np.random.default_rng(11)
def h(x): return 0.0 if x <= 0 or x >= 1 else -(x*math.log(x)+(1-x)*math.log(1-x))
worst_rank = 0; maxerr = [0, 0, 0]; worstW = -1e9
for trial in range(400):
    n = int(rng.integers(2, 10))
    w = np.sort(np.exp(rng.normal(0, 1.2, n)))[::-1]          # decreasing: order = desirability
    th = rng.random() * w.sum(); T = ltf_table(w, th)
    if T.min() == T.max(): continue
    q = 1 / (1 + np.exp(-rng.normal(0, 2.5, n)))
    g = g_transform(T, q); s2 = sigma2_vector(q); k = popcount_vector(n); P = s2 * g * g
    sig = 4 * q * (1 - q); idx = np.arange(2 ** n)
    E = float(np.sum((P * np.log(np.where(P > 0, s2 / np.where(P > 0, P, 1), 1)))[k > 0]))
    I = float(np.sum(k * P)); V = float(np.sum(P[k > 0])); Delta = I - V
    # (1) least-element decomposition: last element = max index (lightest)
    Edec = 0.0; Ddec = 0.0
    for i in range(n):
        sets = [S for S in range(1, 2 ** n) if (S >> i) & 1 and (S >> (i + 1)) == 0]
        for S in sets:
            if P[S] > 0:
                Edec += P[S] * math.log(s2[S] / P[S])
            Ddec += (bin(S).count('1') - 1) * P[S]
    maxerr[0] = max(maxerr[0], abs(Edec - E), abs(Ddec - Delta))
    # (2) DTC identity for A = {T=1}
    p = law_vector(q); alpha = p[T == 1].sum()
    pa = np.where(T == 1, p, 0) / alpha
    H = -np.sum(pa[pa > 0] * np.log(pa[pa > 0]))
    Y = (idx[:, None] >> np.arange(n)) & 1
    c = np.zeros(n); Hc = 0.0
    for i in range(n):
        fl = idx ^ (1 << i)
        piv_on = (Y[:, i] == 1) & (T == 1) & (T[fl] == 0)
        c[i] = pa[piv_on].sum()
        Hc += (1 - c[i]) * h(q[i])
    DTC = H - Hc
    maxerr[1] = max(maxerr[1], abs(math.log(1 / alpha) - (np.sum(c * np.log(1 / q)) - DTC)))
    if DTC < -1e-10: print('NEGATIVE DTC', DTC)
    # (3) rank lemma: E_{nu_i} ln^+(Lambda_i/(|B cap U_i|+1)) <= 3 + ln 4, U_i = {0..i-1}
    for i in range(n):
        Lam = sig[:i].sum(); Ii = sum(P[S] for S in range(2 ** n) if (S >> i) & 1)
        if Ii <= 0: continue
        tot = 0.0
        for S in range(2 ** n):
            if (S >> i) & 1 and P[S] > 0:
                kk = bin(S & ((1 << i) - 1)).count('1')
                tot += P[S] * max(0.0, math.log(max(Lam, 1e-300) / (kk + 1)))
        worst_rank = max(worst_rank, tot / Ii)
    # (4) Theorem W:  E <= V ln(1/V) + 9.21 I
    worstW = max(worstW, (E - V * math.log(1 / V)) / I)
print('identity errors (least-element, DTC):', maxerr[:2])
print('max rank functional:', worst_rank, ' bound 3+ln4 =', 3 + math.log(4))
print('max (E - V ln(1/V))/I:', worstW, ' bound A0 = 9.21')
