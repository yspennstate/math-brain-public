"""Family (b): hub with small diagonal a plus a dense remainder,
Q = a X_h^2 + 2 X_h (L + beta) + lam V^2 + eps X'^T W X'  (uniform laws), exact window estimator (delta .004)."""
try:
    import psutil; psutil.Process().nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
except Exception: pass
import numpy as np, sys, time
from lib import *
n1 = int(sys.argv[1]); N = int(sys.argv[2]); seed = int(sys.argv[3])
AS = [float(x) for x in sys.argv[4].split(',')]
EPSN = [float(x) for x in sys.argv[5].split(',')]
types = sys.argv[6].split(',')
LAMS = [float(x) for x in sys.argv[7].split(',')] if len(sys.argv) > 7 else [1.0, -1.0]
BETAS = [float(x) for x in sys.argv[8].split(',')] if len(sys.argv) > 8 else [0.0]
rng = np.random.default_rng(seed)
B, _ = np.linalg.qr(rng.normal(size=(n1, 6))); w, v, u1, u2, u3, u4 = B.T
def normed(W): W = (W + W.T)/2; return W/np.abs(np.linalg.eigvalsh(W)).max()
def wig():
    G = rng.normal(size=(n1, n1)); return normed(G + G.T)
def make(tp):
    if tp == 'wig': return wig()
    if tp == 'lr': return normed(np.outer(u1, u1) - np.outer(u2, u2) + 0.5*(np.outer(w, u1) + np.outer(u1, w)) + 0.5*(np.outer(v, u2) + np.outer(u2, v)))
    if tp == 'comp':
        P = np.eye(n1) - np.outer(w, w) - np.outer(v, v); return normed(P @ wig() @ P)
    if tp == 'sgn': return normed(np.outer(np.sign(w), np.sign(v)) + np.outer(np.sign(v), np.sign(w)))
    if tp == 'ww': return normed(np.outer(w, w))
    if tp == 'wu': return normed(np.outer(w, u1) + np.outer(u1, w))
    raise ValueError(tp)
fh = U()
t0 = time.time()
Xp = rng.uniform(-0.5, 0.5, (N, n1)); L = Xp @ w; V = Xp @ v
sv = np.linspace(-0.6, 0.6, 121); delta = 0.004
def scan(a, R, T):
    acc = np.zeros(len(sv))
    for c0 in range(0, N, 10000):
        acc += hub_window_values(a, T[c0:c0+10000], R[c0:c0+10000], sv, fh, delta).sum(0)
    return acc/(N*2*delta)
res = []
Wm = {tp: make(tp) for tp in types}
QWs = {tp: np.einsum('ij,ij->i', Xp @ Wm[tp], Xp) for tp in types}
def mu3full(a, lam, eps, W):
    A = np.zeros((n1+1, n1+1)); A[0, 0] = a; A[0, 1:] = w; A[1:, 0] = w; A[1:, 1:] = lam*np.outer(v, v) + eps*W
    return mu3(A)
for lam in LAMS:
    for a in AS:
        for tp in types:
            for en in EPSN:
                for beta in BETAS:
                    eps = en/np.sqrt(n1)
                    R = lam*V*V + eps*QWs[tp]
                    pw = scan(a, R, L + beta)
                    j = int(np.argmax(pw))
                    m3 = mu3full(a, lam, eps, Wm[tp])
                    res.append((lam, a, tp, en, beta, m3*pw[j], sv[j]))
                    print(f"n1={n1} lam={lam:+.0f} a={a:+.3f} W={tp:4s} eps*sqrt(n)={en:4.2f} beta={beta:+.2f}  max_s window-density={pw[j]:.4f} at s={sv[j]:+.3f} mu3={m3:.3f} F={m3*pw[j]:.4f}  t={time.time()-t0:.0f}", flush=True)
res.sort(key=lambda r: -r[5])
print("TOP8:", [(r[0], r[1], r[2], r[3], r[4], round(r[5], 4), round(r[6], 3)) for r in res[:8]], flush=True)
