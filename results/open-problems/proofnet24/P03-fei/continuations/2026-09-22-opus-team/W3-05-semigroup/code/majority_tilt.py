"""Majority: exact level spectrum (closed form) and the tilted-law quantities for large n.

For odd n, m = (n-1)/2 and odd k, |Maj_n^(S)| = C(m,(k-1)/2) C(n-1,m) / (C(n-1,k-1) 2^{n-1}) for |S| = k,
and 0 for even k.  All quantities are computed in log space (nats).

Output (logs/majority_tilt.log):
  (1) H/I and -dH(q_t)/dt at t = 0 against E_0|S| = I and against Var_0|S|;
  (2) at fixed t in {0.25, 0.5, 1.0}: Z_t, E_t|S|, Var_t|S| converge as n grows while -dH/dt grows like 2 log(n) Var_t
      (the scalar-state no-go theorem);
  (3) the unnormalized flux G(t) against M(t) = sum |S|^2 e^{-2t|S|} w and the KKL rate Kr(t);
  (4) the escort-tilt Gibbs bound log sum_S theta^{|S|} w(S)^alpha against I.
"""
import math, sys
import numpy as np
from fei_core import lowprio

lowprio()


def lgC(a, b):
    return math.lgamma(a + 1) - math.lgamma(b + 1) - math.lgamma(a - b + 1)


def maj_levels(n):
    m = (n - 1) // 2
    ks, lw, lcount = [], [], []
    for k in range(1, n + 1, 2):
        la = lgC(m, (k - 1) // 2) + lgC(n - 1, m) - lgC(n - 1, k - 1) - (n - 1) * math.log(2)
        ks.append(k)
        lw.append(2 * la)            # log of the per-set weight a_k^2
        lcount.append(lgC(n, k))     # log C(n,k)
    ks = np.array(ks, float); lw = np.array(lw); lc = np.array(lcount)
    W = np.exp(lw + lc)              # level weights
    return ks, lw, lc, W


def tilt_stats(ks, lw, lc, W, t):
    e = np.log(W) - 2 * t * ks
    mx = e.max()
    pi = np.exp(e - mx); Zs = pi.sum(); pi /= Zs
    logZ = math.log(Zs) + mx
    L = -lw                          # log(1/w(S)) for S at level k
    E = float((pi * ks).sum()); V = float((pi * (ks - E) ** 2).sum())
    EL = float((pi * L).sum())
    cov = float((pi * (ks - E) * (L - EL)).sum())
    mdH = 2 * cov + 4 * t * V
    # entropy of q_t: level entropy + within-level uniform entropy log C(n,k)
    Hq = float(-(pi[pi > 0] * np.log(pi[pi > 0])).sum() + (pi * lc).sum())
    return dict(logZ=logZ, Z=math.exp(logZ), E=E, V=V, mdH=mdH, cov=cov, Hq=Hq)


def main():
    out = []
    P = lambda *a: out.append(' '.join(str(x) for x in a))
    P("# Majority, exact level spectrum; entropies in nats")
    P("# n  I  H/I(bits)  [-dH/dt]_0  ratio_to_E0  ratio_to_Var0  H(q_inf)")
    for n in [11, 21, 51, 101, 201, 401, 801, 1601, 3201]:
        ks, lw, lc, W = maj_levels(n)
        I = float((W * ks).sum()); H = float((W * (-lw)).sum())
        s0 = tilt_stats(ks, lw, lc, W, 0.0)
        P(n, round(I, 5), round(H / I / math.log(2), 5), round(s0['mdH'], 4), round(s0['mdH'] / I, 4),
          round(s0['mdH'] / s0['V'], 4), round(math.log(n), 4))
    P("")
    P("# fixed t: (Z_t, E_t, Var_t) converge in n; -dH/dt / Var_t grows like 2 log n")
    P("# t n Z_t E_t Var_t -dH/dt ratio(-dH/dt / Var_t) 2*log(n)")
    for t in [0.25, 0.5, 1.0]:
        for n in [101, 1001, 10001, 100001]:
            ks, lw, lc, W = maj_levels(n)
            s = tilt_stats(ks, lw, lc, W, t)
            P(t, n, round(s['Z'], 6), round(s['E'], 6), round(s['V'], 6), round(s['mdH'], 4),
              round(s['mdH'] / s['V'], 4), round(2 * math.log(n), 4))
    P("")
    P("# unnormalized flux at fixed t: G(t)=sum|S|e^{-2t|S|}w L_S, M(t)=sum|S|^2 e^{-2t|S|} w, Kr(t)=sum_S w e^{-2t|S|} sum_{i in S} log(1/Inf_i)")
    P("# t n G M Kr G/M G/(M+Kr)")
    for t in [0.5, 1.0]:
        for n in [101, 1001, 10001, 100001]:
            ks, lw, lc, W = maj_levels(n)
            I = float((W * ks).sum()); inf = I / n
            dec = W * np.exp(-2 * t * ks)
            G = float((ks * dec * (-lw)).sum()); M = float((ks ** 2 * dec).sum())
            Kr = float((ks * dec).sum()) * math.log(1 / inf)
            P(t, n, round(G, 6), round(M, 6), round(Kr, 6), round(G / M, 4), round(G / (M + Kr), 4))
    P("")
    P("# escort-tilt Gibbs: H <= [I log(1/theta) + log sum theta^{|S|} w^alpha]/(1-alpha); report log-sum / I")
    P("# alpha theta n I logsum logsum/I")
    for alpha in [0.5, 0.9]:
        for theta in [0.5, 0.9]:
            for n in [101, 1001, 10001]:
                ks, lw, lc, W = maj_levels(n)
                I = float((W * ks).sum())
                terms = lc + alpha * lw + ks * math.log(theta)
                mx = terms.max(); ls = mx + math.log(np.exp(terms - mx).sum())
                P(alpha, theta, n, round(I, 3), round(ls, 3), round(ls / I, 4))
    txt = '\n'.join(out)
    print(txt)
    with open('../logs/majority_tilt.log', 'w') as fh:
        fh.write(txt + '\n')


if __name__ == '__main__':
    main()
