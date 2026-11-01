"""Explicit refutation of T1-sharp for REAL orthonormal leaves (3 variables: selector x in {+-1}^2, data y).
A_1 = {x = (1,1)} (p_1 = 1/4), A_2 = rest.  G_1 = cos e - sin e * y,  G_2 = sin e + cos e * y  (orthonormal).
F = 1_{A_1}(x) G_1(y) + 1_{A_2}(x) G_2(y)  (real, E F^2 = 1).  Compare H(Fhat^2) with
H(p) + sum_k p_k [H(q_k) + H(Ghat_k^2)]."""
import numpy as np
from fei_lib import fwht_float
def H(p):
    p = np.asarray(p).ravel(); p = p[p > 1e-300]; return float(-(p*np.log2(p)).sum())
lab = np.array([0, 1, 1, 1])                # index 0 = x=(1,1)
p = np.array([0.25, 0.75])
q = []
for k in range(2):
    ak = (lab == k).astype(float); q.append((fwht_float(ak)/4)**2/p[k])
for e in (0.02, 0.05, 0.1, 0.2, 0.3):
    G = [np.array([np.cos(e) - np.sin(e), np.cos(e) + np.sin(e)]),     # values at y=+1 (index0), y=-1 (index1)
         np.array([np.sin(e) + np.cos(e), np.sin(e) - np.cos(e)])]
    Fx = np.empty(8)
    for yi in range(2):
        for xi in range(4):
            Fx[xi + 4*yi] = G[lab[xi]][yi]
    assert abs(np.mean(Fx**2) - 1) < 1e-12 and abs(np.mean(G[0]*G[1])) < 1e-12
    lhs = H((fwht_float(Fx)/8)**2)
    rhs = H(p) + sum(p[k]*(H(q[k]) + H((fwht_float(G[k])/2)**2)) for k in range(2))
    print('eps=%.2f  H(F)=%.6f  T1-sharp bound=%.6f  gap=%+.6f   T1 bound (with 2H(p))=%.6f' % (e, lhs, rhs, lhs-rhs, rhs + H(p)))
