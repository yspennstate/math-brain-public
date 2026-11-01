"""Family (a) at finite n with product (uniform) laws: Q = 2 X_h (L + beta) + lam V^2 + eps X'^T W X', ||W|| = 1.
Common random numbers per n1: L, V and Q_W = X'^T W X' computed once per W type; all eps values reuse them.
Scan: exact window estimator (delta = 0.004) on an s-grid; exact E1 (delta -> 0) at the argmax with fresh samples.
Reports F = mu_3(A) * max_s p(s)."""
try:
    import psutil; psutil.Process().nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
except Exception: pass
import numpy as np, sys, time
from lib import *
n1 = int(sys.argv[1]); N = int(sys.argv[2]); lam = float(sys.argv[3]); seed = int(sys.argv[4])
types = sys.argv[5].split(',') if len(sys.argv) > 5 else ['wig', 'wv', 'ww', 'vv', 'lr', 'lrn', 'comp', 'sgn', 'hadam']
EPSN = [0.0, 0.01, 0.03, 0.1, 0.3, 1.0, 3.0]
rng = np.random.default_rng(seed)
B, _ = np.linalg.qr(rng.normal(size=(n1, 6))); w, v, u1, u2, u3, u4 = B.T
def normed(W): W = (W + W.T)/2; return W/np.abs(np.linalg.eigvalsh(W)).max()
def wig():
    G = rng.normal(size=(n1, n1)); return normed(G + G.T)
def make(tp):
    if tp == 'wig': return wig()
    if tp == 'wv': return normed(np.outer(w, v) + np.outer(v, w))
    if tp == 'ww': return normed(np.outer(w, w))
    if tp == 'vv': return normed(np.outer(v, v))
    if tp == 'lr': return normed(np.outer(u1, u1) - np.outer(u2, u2) + 0.5*(np.outer(w, u1) + np.outer(u1, w)) + 0.5*(np.outer(v, u2) + np.outer(u2, v)))
    if tp == 'lrn': return normed(make('lr') + 0.3*wig())
    if tp == 'comp':
        P = np.eye(n1) - np.outer(w, w) - np.outer(v, v); return normed(P @ wig() @ P)
    if tp == 'sgn': return normed(np.outer(np.sign(w), np.sign(v)) + np.outer(np.sign(v), np.sign(w)))
    if tp == 'hadam':
        k = int(np.log2(n1)); H = np.array([[1.0]])
        for _ in range(int(np.ceil(np.log2(n1)))): H = np.block([[H, H], [H, -H]])
        H = H[:n1, :n1]; return normed(H + H.T)
    raise ValueError(tp)
fh = U()
t0 = time.time()
# common samples for the scan
Xp = rng.uniform(-0.5, 0.5, (N, n1))
L = Xp @ w; V = Xp @ v
sv = np.linspace(-0.6, 0.6, 121); delta = 0.004
def scan(R, T):
    acc = np.zeros(len(sv))
    for c0 in range(0, N, 10000):
        acc += hub_window_values(0.0, T[c0:c0+10000], R[c0:c0+10000], sv, fh, delta).sum(0)
    return acc/(N*2*delta)
res = []
for tp in types:
    W = make(tp); QW = np.einsum('ij,ij->i', Xp @ W, Xp)
    for en in EPSN:
        if tp != types[0] and en == 0.0: continue
        eps = en/np.sqrt(n1)
        A = np.zeros((n1+1, n1+1)); A[0, 1:] = w; A[1:, 0] = w; A[1:, 1:] = lam*np.outer(v, v) + eps*W
        m3 = mu3(A)
        R = lam*V*V + eps*QW
        pw = scan(R, L)
        j = int(np.argmax(pw))
        res.append((tp, en, m3, pw[j], sv[j], m3*pw[j]))
        print(f"n1={n1} lam={lam:+.0f} W={tp:5s} eps*sqrt(n)={en:5.2f} mu3={m3:.3f}  max_s window-density={pw[j]:.4f} at s={sv[j]:+.3f}  F={m3*pw[j]:.4f}  t={time.time()-t0:.0f}", flush=True)
res.sort(key=lambda r: -r[5])
print("TOP5:", [(r[0], r[1], round(r[5], 4), round(r[4], 3)) for r in res[:5]], flush=True)
