try:
    import psutil; psutil.Process().nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
except Exception:
    pass
# Aligned-curvature family (examples E2 and its 3-eigenvalue completion):
#   Q = a Xh^2 + 2 Xh t + sigma t^2 + lam V^2 + lam2 U^2,  t = L + beta, L, V, U independent spread linear forms.
# D_H = |1 - a sigma|.  lam2 = 0: only two large eigenvalues (expect log(1/D_H) growth, factor ~ sqrt|a|, hyperbolic case).
# lam2 != 0: three large eigenvalues (W^2 sigma, lam, lam2): the conjecture predicts a bound uniform in D_H.
import numpy as np, time, sys
sys.path.insert(0, '.')
from hublib import *
rng = np.random.default_rng(21)
m = 30
wL = np.ones(m)/np.sqrt(m); wV = np.ones(m)/np.sqrt(m); wU = np.ones(m)/np.sqrt(m)
N = 250000
law = uniform_law(); fh = uniform_law()
def samp_factory(sigma, lam, lam2):
    def samp(r):
        L = r.random((N, m)) @ wL - 0.5*np.sqrt(m)
        V = r.random((N, m)) @ wV - 0.5*np.sqrt(m)
        U = r.random((N, m)) @ wU - 0.5*np.sqrt(m)
        return L, (lam*V*V + lam2*U*U, L)   # sigma t^2 added below (needs beta)
    return samp
t0 = time.time()
def run(a, sigma, lam, lam2, beta, sgrid, chunks):
    def samp(r):
        L, (Rb, _) = samp_factory(sigma, lam, lam2)(r)
        t = L + beta
        return L, Rb + sigma*t*t
    d = density_on_grid(a, beta, samp, fh, sgrid, chunks, rng)
    j = int(np.argmax(d))
    return sgrid[j], d[j]
a = 0.2
for lam2 in [0.0, 1.0, -1.0]:
    for DH in [1.0, 0.3, 0.1, 0.03, 0.01, 0.003]:
        sigma = (1 - DH)/a     # D_H = 1 - a sigma
        for lam in [-1.0]:
            # the singular value of the (a, sigma) block form is at 0 when beta = 0; scan around 0 finely
            sg = np.concatenate([np.linspace(-0.3, 0.3, 25), np.linspace(-0.02, 0.02, 9)])
            s1, dmax = run(a, sigma, lam, lam2, 0.0, np.unique(sg), 2)
            print("lam2 %4.1f  D_H %6.3f  sigma %7.3f  a %.2f lam %.1f : max_s p_Q = %.3f at s = %.3f   t=%.0fs"
                  % (lam2, DH, sigma, a, lam, dmax, s1, time.time() - t0), flush=True)
