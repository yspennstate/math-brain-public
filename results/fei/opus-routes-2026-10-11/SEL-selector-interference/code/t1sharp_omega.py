"""beta -> 1 limit of two-cell T1-sharp (NOTES 5.3): Phi = eps*Omega + O(eps^2 log 1/eps) with p_2 = eps,
Omega = 4 H(V) - 4 A + H(G1) - H(G2) - 4, V = (G1-G2)/2, A = sum_T G1hat(T) Vhat(T) log2(1/G1hat(T)^2),
H(.) unnormalised.  Vectorised: spectra of all tables precomputed with the Hadamard matrix."""
import numpy as np
def Hun(P):
    with np.errstate(divide='ignore', invalid='ignore'):
        return np.where(P > 0, -P*np.log2(np.where(P > 0, P, 1)), 0.0).sum(axis=-1)
for n in (2, 3, 4):
    N = 1 << n
    codes = np.arange(1 << N, dtype=np.int64)
    tabs = (1 - 2*((codes[:, None] >> np.arange(N)[None, :]) & 1)).astype(np.int8)
    x = np.arange(N)
    Hm = np.array([[(-1)**bin(xx & S).count('1') for S in range(N)] for xx in x], dtype=np.float64)
    spec = tabs.astype(np.float64) @ Hm / N
    Hspec = Hun(spec**2)
    with np.errstate(divide='ignore'):
        L = np.where(spec**2 > 0, np.log2(1/np.where(spec**2 > 0, spec**2, 1)), 0.0)
    rng = np.random.default_rng(1)
    idx1 = np.arange(len(tabs)) if n <= 3 else rng.choice(len(tabs), size=2500, replace=False)
    best = (-np.inf, None, None)
    for i in idx1:
        dots = tabs.astype(np.int32) @ tabs[i].astype(np.int32)
        J = np.where(dots == 0)[0]
        if len(J) == 0: continue
        Vh = (spec[i][None, :] - spec[J]) / 2
        om = 4*Hun(Vh**2) - 4*(spec[i][None, :]*Vh*L[i][None, :]).sum(axis=1) + Hspec[i] - Hspec[J] - 4
        k = int(np.argmax(om))
        if om[k] > best[0]: best = (om[k], int(i), int(J[k]))
    print('n=%d max Omega = %.6e  G1 code %d  G2 code %d' % (n, best[0], best[1], best[2]), flush=True)
