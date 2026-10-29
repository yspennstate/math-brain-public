"""Audit 2 of NOTE 'c(n d) in closed form' (agent A, 20 Oct 2026).
(1) Exact finite-n slot formulas for k, Q, cb (derived by hand from the permutation moments E Z_l Z_m = -z2/(n-1),
    E b_k Z_l^2 = -E[bZ^2]/(n-1), E b_k Z_l Z_m = 2 E[bZ^2]/((n-1)(n-2)), infinite history), averaged over the slot p,
    against the NOTE's continuum integrands at fixed s = n d as n grows.
(2) Monte Carlo of the cubic term at x = 0: d E[b_k (Z_k + W)^3] (current epoch) against 3 E[bZ] z2 avg[k Qc],
    Qc = (1 - e^-2t)/2 - (1 - e^-t)^2/s, the current-epoch part of Q. The M W0^2 cross term is what turns Z_k into k Z_k.
Argv: mode 'slots' or 'mc'."""
import sys, numpy as np
from scipy.integrate import quad
def cont(s):
    q = np.tanh(s/2); e = np.exp
    k = lambda t: 1 - (1 - e(-t))/s
    Q = lambda t: 0.5 - (1 - e(-t))**2/s - e(-2*t)*q/s
    Qc = lambda t: (1 - e(-2*t))/2 - (1 - e(-t))**2/s
    cb = lambda t: 1 - 2*(1 - e(-t))/s - (1 - e(-2*t))/(2*s) + 2*(1 - e(-t))**2/s**2
    av = lambda f: quad(f, 0, s, limit=400)[0]/s
    return dict(K=av(k), Q=av(Q), cb=av(cb), kQ=av(lambda t: k(t)*Q(t)), kQc=av(lambda t: k(t)*Qc(t)))
def slots(n, s):
    d = s/n; b2 = 1 - d; j = np.arange(1, n)
    w = b2**j; S1 = np.concatenate([[0], np.cumsum(w)]); S2 = np.concatenate([[0], np.cumsum(w**2)])   # current-epoch lags 1..p
    k = 1 - S1/(n - 1)
    def pvar(a1, a2): return a2*n/(n - 1) - a1**2/(n - 1)       # Var of a permutation sum / z2, weights with sums a1, a2
    p = np.arange(n); E1 = b2**p; Ep = b2**n                    # earlier epochs: weights b2^(p+1+m n + i), i = 0..n-1
    a1 = (1 - b2**n)/(1 - b2) * b2**(p + 1); a2 = (1 - b2**(2*n))/(1 - b2**2) * b2**(2*(p + 1))
    fut = pvar(a1, a2)/(1 - Ep**2) * 1.0                          # sum over earlier epochs m >= 0: factor 1/(1 - b2^(2n))
    cur = 1 + pvar(S1, S2) + 2*(-S1/(n - 1)) + 0               # Var(Z_k + W)/z2: lag 0, W, cross 2 sum w E Z_k Z_l
    cur = (1 + S2*n/(n - 1) - S1**2/(n - 1)) - 2*S1/(n - 1)       # same thing written out
    Q = d*(cur + fut)
    cb = 1 - 2*S1/(n - 1) - S2/(n - 1) + 2*(S1**2 - S2)/((n - 1)*(n - 2))
    return dict(K=k.mean(), Q=Q.mean(), cb=cb.mean(), kQ=(k*Q).mean())
mode = sys.argv[1]
if mode == 'slots':
    for s in (0.5, 2, 5, 20):
        c = cont(s); print("s %g continuum   K %.6f Qbar %.6f cb %.6f kQ %.6f" % (s, c['K'], c['Q'], c['cb'], c['kQ']))
        for n in (100, 1000, 10000, 100000):
            e = slots(n, s); print("      n %6d  K %.6f Qbar %.6f cb %.6f kQ %.6f   max rel diff %.2e" % (n, e['K'], e['Q'], e['cb'], e['kQ'],
                  max(abs(e[x]/c[x] - 1) for x in ('K', 'Q', 'cb', 'kQ'))), flush=True)
else:
    rng = np.random.default_rng(23); C = int(sys.argv[3])
    for n in map(int, sys.argv[2].split(',')):
        for s in (2.0, 5.0, 20.0):
            d = s/n; b2 = 1 - d; m = n//10; b = np.array([9.0]*m + [-1.0]*(n - m))
            Z = b**2; Z -= Z.mean(); EbZ = np.mean(b*Z); z2 = np.mean(Z**2)
            acc = np.zeros(C); perm = np.argsort(rng.random((C, n)), axis=1).astype(np.int32); W = np.zeros(C)
            for p in range(n):
                kk = perm[:, p]
                if p: W = b2*(Z[perm[:, p-1]] + W)
                acc += b[kk]*(Z[kk] + W)**3
            E = d*acc/n; pred = 3*EbZ*z2*cont(s)['kQc']
            print("n %d s %g: d E[b(Z_k+W)^3] %.4g +- %.2g | 3 E[bZ] z2 avg[k Qc] %.4g | ratio %.4f +- %.4f" % (n, s, E.mean(),
                  E.std(ddof=1)/np.sqrt(C), pred, E.mean()/pred, E.std(ddof=1)/np.sqrt(C)/pred), flush=True)
