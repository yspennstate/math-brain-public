# Shifted Fourier witnesses.  With U ~ mu_n and Z = frac(2U),
#   W_n(k) = E[(-1)^{floor 2U} e^{-4 pi i k U}] = (2/(pi i)) sum_{m odd} [ conj(hatmu(2^n(m-2k))) - hatmu(2^n(m+2k)) ] / m,
# and |phi| = 1 gives the Fourier lower bound  E[u_n^2] >= |W_n(k)|^2  for every integer k.
import numpy as np, sys
KMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 40001
NMAX = int(sys.argv[2]) if len(sys.argv) > 2 else 9
KS   = int(sys.argv[3]) if len(sys.argv) > 3 else 6
def hat_mu(xi, terms=4000):
    xi = np.asarray(xi, dtype=np.float64); out = np.ones(xi.shape, dtype=np.complex128); a = xi/3.0
    for _ in range(terms):
        out *= (1 + np.exp(-2j*np.pi*a))/2; a = a*(2.0/3.0)
        if np.max(np.abs(a)) < 1e-16: break
    return out
ms = np.arange(1, KMAX+1, 2, dtype=np.float64)
meas = {0:2.1284e-01, 1:4.0394e-03, 2:1.1676e-03, 3:9.9085e-05, 4:2.7003e-05, 5:2.6079e-05,
        6:1.8968e-07, 7:2.3292e-08, 8:1.7489e-08, 9:9.5067e-09}
print("n | best k | |W_n(k)|^2 (Fourier lower bound) | measured E[u_n^2] | share")
for n in range(NMAX+1):
    p = 2.0**n; best = (0.0, None)
    for k in range(0, KS+1):
        A = np.conj(hat_mu(p*(ms - 2*k))); B = hat_mu(p*(ms + 2*k))
        W = (2/(np.pi*1j))*np.sum((A - B)/ms)
        v = abs(W)**2
        if v > best[0]: best = (v, k)
    m = meas.get(n)
    print(f"n={n}: k={best[1]}  |W|^2={best[0]:.4e}   Eu2={m:.4e}   share={best[0]/m:.4f}" if m else f"n={n}: k={best[1]} |W|^2={best[0]:.4e}")
