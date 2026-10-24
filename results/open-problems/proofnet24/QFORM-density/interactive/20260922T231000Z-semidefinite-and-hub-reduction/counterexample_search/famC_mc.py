"""Family (c): two hubs with a nonzero hub block B and a remainder.
Q = a1 X1^2 + 2 kap X1 X2 + a2 X2^2 + 2 X1 T1 + 2 X2 T2 + R,  T_i = <w_i, X'> + beta_i,  R = lam V^2 + eps X'^T W X'.
w2 = cos(th) w1 + sin(th) u  (overlap of the hub rows).  Hub laws uniform on [-1/2,1/2]; leaves uniform.
Exact window estimator in X1 (delta = .004), Gauss-Legendre (24 nodes) in X2, Monte Carlo over the leaves."""
try:
    import psutil; psutil.Process().nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
except Exception:
    pass
import numpy as np, sys, time
from lib import *

n1 = int(sys.argv[1]); N = int(sys.argv[2]); seed = int(sys.argv[3])
rng = np.random.default_rng(seed)
B, _ = np.linalg.qr(rng.normal(size=(n1, 5))); w1, u, v, z1, z2 = B.T
G = rng.normal(size=(n1, n1)); Wg = (G + G.T); Wg /= np.abs(np.linalg.eigvalsh(Wg)).max()
fh = U()
gx, gw = np.polynomial.legendre.leggauss(12); x2n = gx/2; x2w = gw/2      # nodes on [-1/2,1/2], weights sum 1
Xp = rng.uniform(-0.5, 0.5, (N, n1))
P1 = Xp @ w1; PU = Xp @ u; PV = Xp @ v; QW = np.einsum('ij,ij->i', Xp @ Wg, Xp)
sv = np.linspace(-0.4, 0.4, 81); delta = 0.004
t0 = time.time()


def Fconf(th, a1, a2, kap, lam, epsn, b1=0.0, b2=0.0):
    w2 = np.cos(th)*w1 + np.sin(th)*u
    T1 = P1 + b1; T2 = np.cos(th)*P1 + np.sin(th)*PU + b2
    eps = epsn/np.sqrt(n1)
    R = lam*PV*PV + eps*QW
    acc = np.zeros(len(sv))
    for c0 in range(0, N, 5000):
        sl = slice(c0, c0+5000)
        for x2, wt in zip(x2n, x2w):
            acc += wt*hub_window_values(a1, T1[sl] + kap*x2, a2*x2*x2 + 2*x2*T2[sl] + R[sl], sv, fh, delta).sum(0)
    pw = acc/(N*2*delta)
    n = n1 + 2
    A = np.zeros((n, n)); A[0, 0] = a1; A[1, 1] = a2; A[0, 1] = A[1, 0] = kap
    A[0, 2:] = w1; A[2:, 0] = w1; A[1, 2:] = w2; A[2:, 1] = w2
    A[2:, 2:] = lam*np.outer(v, v) + eps*Wg
    m3 = mu3(A)
    j = int(np.argmax(pw))
    return m3*pw[j], pw[j], sv[j], m3


confs = []
for th in (np.pi/2, np.pi/6):
    for (a1, a2, kap) in ((0, 0, 0), (0, 0, 0.03), (0, 0, 0.1), (0, 0, 0.3), (0.1, -0.1, 0), (0.1, 0.1, 0), (0.1, 0, 0), (0.1, -0.1, 0.1), (0.3, 0, 0), (0.3, 0.3, 0.3)):
        for (lam, epsn) in ((0.0, 0.0), (1.0, 0.0)):
            confs.append((th, a1, a2, kap, lam, epsn))
for (a1, a2, kap) in ((0, 0, 0), (0, 0, 0.1), (0.1, -0.1, 0.1)):
    for (lam, epsn) in ((1.0, 0.3), (-1.0, 0.0), (1.0, 1.0)):
        confs.append((np.pi/2, a1, a2, kap, lam, epsn))
    confs.append((np.pi/18, a1, a2, kap, 1.0, 0.0))
res = []
for c in confs:
    F, pw, s, m3 = Fconf(*c)
    res.append((F,) + c + (s, m3))
    print(f"th={np.degrees(c[0]):5.1f} a1={c[1]:+.2f} a2={c[2]:+.2f} kap={c[3]:.2f} lam={c[4]:+.0f} eps*sqrt(n)={c[5]:.1f}: "
          f"max window-density {pw:.4f} at s={s:+.3f}  mu3={m3:.3f}  F={F:.4f}  t={time.time()-t0:.0f}", flush=True)
res.sort(key=lambda r: -r[0])
print("TOP6:", [tuple(np.round(r, 3)) for r in res[:6]], flush=True)
