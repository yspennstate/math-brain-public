# Derrida-Retaux recursion in tilted coordinates r_k = m^k P(X=k), so no entry is tiny relative to the
# quantities that drive criticality.  Sum of m copies: tilted law R = r * r * ... (plain convolution).
# Then r'_0 = R_0 + R_1/m and r'_k = R_{k+1}/m (k >= 1).  Checks Theorem 1.1's conclusions:
# E[X^r]/q -> M_r(m), conditional TV -> 0, E[s^X|X>0] -> (m-1)s/(m-s), and the Lemma 2.1 identities.
import numpy as np, sys
from numpy.fft import rfft, irfft

def run(m, r0, K, N, report):
    L = 1
    while L < m * (K + 1): L *= 2
    r = np.zeros(K + 1); r[:len(r0)] = r0
    k = np.arange(K + 1)
    w = float(m) ** (-k.astype(float))            # p_k = r_k m^{-k}
    pi = np.where(k > 0, (m - 1) * w, 0.0)
    M1 = (k * pi).sum(); M2 = (k * k * pi).sum()
    rows = []
    for n in range(N + 1):
        p = r * w
        q = 1 - p[0]
        if n in report:
            mu = (k * p).sum(); e2 = (k * k * p).sum()
            nu = p[1:] / q
            tv = 0.5 * np.abs(nu - pi[1:]).sum()
            s = 1.5
            gfs = ((s / m) ** k * r)[1:].sum() / q
            Gm = r.sum()
            crit = (m - 1) * (k * r).sum() - Gm
            print(f"n={n:5d} n2q={n*n*q:8.5f} EX/q={mu/q:.5f}({M1:.5f}) EX2/q={e2/q:.5f}({M2:.5f}) "
                  f"TV={tv:.5f} E[1.5^X|>0]={gfs:.5f}({(m-1)*s/(m-s):.5f}) n(Gm-1)={n*(Gm-1):.4f} "
                  f"critdefect={crit:.2e} tailtilt={r[-K//10:].sum():.2e}", flush=True)
        if n == N: break
        R = np.convolve(r, r) if m == 2 else np.convolve(np.convolve(r, r), r)
        new = np.zeros(K + 1)
        new[0] = R[0] + R[1] / m
        new[1:] = R[2:K + 2] / m
        r = new / (new * w).sum()   # total mass M -> M^m doubles rounding error each step; renormalise
    return r

m = 2
# critical law on {0,2}, P(2) = 1/5: tilted r_0 = 0.8, r_2 = 0.2*4
print("K=3000"); run(m, [0.8, 0.0, 0.8], 3000, 3000, {10, 100, 300, 1000, 2000, 3000})
print("K=6000"); run(m, [0.8, 0.0, 0.8], 6000, 3000, {1000, 3000})
