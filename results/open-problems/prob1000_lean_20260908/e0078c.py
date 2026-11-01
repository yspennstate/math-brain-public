"""Conjecture 4.2 on 'wide-block' cycles: m states clockwise at rate r, a block of k consecutive
states carries rate L each (per-visit exposure L/r small, per-lap exposure E = kL/r moderate).
Direct check of the source's (14): (pi-alpha) e^{Ct} 1 >= 0 for all t."""
import numpy as np
from scipy.linalg import expm
def run(m, k, L, r=1.0, n=400, periods=2.0):
    Q = np.zeros((m,m))
    for i in range(m): Q[i,(i+1)%m] = r
    np.fill_diagonal(Q, -r)
    lam = np.zeros(m); lam[:k] = L
    pi = np.full(m, 1.0/m); ls = pi@lam; al = pi*lam/ls
    C = Q - np.diag(lam); one = np.ones(m); T = m/r
    ts = np.linspace(T/n, periods*T, n)
    vals = np.array([(pi-al)@expm(C*t)@one for t in ts])
    S = np.array([pi@expm(C*t)@one for t in ts])
    i = np.argmin(vals/S)
    return vals[i], ts[i]/T, S[i], (vals/S)[i], k*L/r
for (m,k,L) in [(64,32,0.25),(64,32,0.5),(128,64,0.125),(128,64,0.25),(200,100,0.1),(200,100,0.2),(256,128,0.1)]:
    v,tp,S,rel,E = run(m,k,L)
    print(f"m={m:3d} k={k:3d} L={L:.3f} E={E:5.1f}: min (pi-alpha)e^Ct1 = {v:+.3e} at {tp:.2f} periods, S={S:.3e}, rel = 1-hazard/lam* = {rel:+.4f}")
