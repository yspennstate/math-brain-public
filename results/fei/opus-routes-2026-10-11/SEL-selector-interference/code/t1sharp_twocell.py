"""Two-cell T1-sharp reduces (NOTES 5.3) to: for orthogonal Boolean G1,G2 (U=(G1+G2)/2, V=(G1-G2)/2) and beta in (-1,1),
 Phi_beta = (1-beta^2) H(V) + H(U+beta V) - p1 H(G1) - p2 H(G2) - R(p) <= 0,  p1=(1+beta)/2,
 H(.) of an unnormalised coefficient vector = sum c^2 log(1/c^2).  Exhaustive n=3, random n=4,5.  Vectorised."""
import itertools, numpy as np
from fei_lib import fwht_float
def Hun(M):   # rows = vectors of Fourier coefficients
    P = M**2
    with np.errstate(divide='ignore', invalid='ignore'):
        L = np.where(P > 0, -P*np.log2(np.where(P > 0, P, 1)), 0.0)
    return L.sum(axis=1)
def batch(G1, G2, n, betas):
    N = 1 << n
    A = np.array([fwht_float(g) for g in G1]) / N; B = np.array([fwht_float(g) for g in G2]) / N
    Uh, Vh = (A + B)/2, (A - B)/2
    HG1, HG2, HV = Hun(A), Hun(B), Hun(Vh)
    worst = np.full(len(G1), -np.inf); arg = np.zeros(len(G1))
    for be in betas:
        p1, p2 = (1+be)/2, (1-be)/2
        R = 4*p1*p2 + 2*p1**2*np.log2(1/p1) + 2*p2**2*np.log2(1/p2)
        val = (1-be**2)*HV + Hun(Uh + be*Vh) - p1*HG1 - p2*HG2 - R
        upd = val > worst; worst[upd] = val[upd]; arg[upd] = be
    return worst, arg
betas = np.concatenate([np.linspace(-0.999, 0.999, 401)])
# n = 3 exhaustive
n = 3; N = 8
tabs = np.array([[1 - 2*((c >> i) & 1) for i in range(N)] for c in range(1 << N)])
G1, G2 = [], []
for i in range(len(tabs)):
    for j in range(len(tabs)):
        if int(tabs[i] @ tabs[j]) == 0: G1.append(tabs[i]); G2.append(tabs[j])
w, b = batch(np.array(G1), np.array(G2), n, betas)
k = int(np.argmax(w)); print('n=3 pairs', len(G1), ' max Phi', w[k], ' beta', b[k], G1[k], G2[k])
rng = np.random.default_rng(9)
for n in (4, 5):
    N = 1 << n; best = (-np.inf, None)
    for rep in range(40):
        g1 = rng.choice([-1, 1], size=(4000, N)); g2 = rng.choice([-1, 1], size=(4000, N))
        ok = (np.einsum('ij,ij->i', g1, g2) == 0)
        w, b = batch(g1[ok], g2[ok], n, betas[::4])
        k = int(np.argmax(w))
        if w[k] > best[0]: best = (w[k], b[k])
    print('n=%d random max Phi' % n, best)
