"""Conjecture 4.2 test on 'lighthouse' cycles: m states, clockwise rate r, arrivals only in state 0 at rate L.
Direct check of the source's form (14): (pi - alpha) e^{Ct} 1 >= 0 for all t."""
import numpy as np
from scipy.linalg import expm
def check(m, r, L, tmax_periods=2.5, n=600):
    Q = np.zeros((m,m))
    for i in range(m): Q[i,(i+1)%m] = r
    np.fill_diagonal(Q, -r)
    lam = np.zeros(m); lam[0] = L
    pi = np.full(m, 1.0/m); ls = pi@lam; al = pi*lam/ls
    C = Q - np.diag(lam); one = np.ones(m)
    T = m/r                       # mean period
    ts = np.linspace(1e-3, tmax_periods*T, n)
    vals = np.array([(pi-al)@expm(C*t)@one for t in ts])
    S = np.array([pi@expm(C*t)@one for t in ts])
    i = np.argmin(vals)
    return vals[i], ts[i]/T, S[i], vals.min()/S[i]
for m in [4, 8, 16, 32, 64]:
    for L in [1.0, 5.0, 20.0]:
        v, tper, S, rel = check(m, 1.0, L)
        print(f"m={m:3d} r=1 L={L:5.1f}: min (pi-alpha)e^Ct 1 = {v:+.3e} at t = {tper:.2f} periods, S(t)={S:.3e}, relative {rel:+.3e}")
