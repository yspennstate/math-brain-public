"""The coordinator's experiment: do bumpy / lattice-tuned laws (which inflate the Fourier L^1 norm of aligned twists,
twist agent N2/N13, and make |psi(s0)| ~ 1) raise the ACTUAL density in hub + aligned-twist families?
Q = 2 X_h (L + beta) + lam V^2 + kap L^2 [+ kap2 L V] [+ eps X'^T W X'],  hub law uniform[-1/2,1/2].
Exact window estimator (hub integrated, delta = .004) over a data-driven s-grid; F = mu_3 * max.
Setup 1: n1 = 4 leaves, w = (1,1,1,1)/2, v = (1,-1,1,-1)/2, leaves = N bumps (uniform, width 1/N, height 1) at base-N
         positions a_{i,q} = q N^(i-1) D / w_i, D = 8 N/|kap|  (the N13 construction, bumps -> boxes).
Setup 2: n1 = 50 spread w, v; leaves = N boxes of width 1/N at random positions in [-R/2, R/2] (R = 1 is uniform).
Setup 3: n1 = 50; leaves = M boxes of width 1/M at spacing Delta (lattice-tuned: psi(2 pi/Delta) ~ 1)."""
try:
    import psutil; psutil.Process().nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
except Exception:
    pass
import numpy as np, sys, time
from lib import *

setup = int(sys.argv[1]); N_s = int(sys.argv[2]); seed = int(sys.argv[3])
rng = np.random.default_rng(seed)
fh = U(); delta = 0.004
t0 = time.time()


def boxes(centers, width):
    c = np.sort(np.asarray(centers, float))
    return PWLaw(c - width/2, c + width/2)


def Fvalue(laws, w, v, lam, kap, kap2=0.0, epsW=None, beta=0.0, ns=241):
    n1 = len(w)
    Xp = sample_X(laws, N_s, rng)
    L = Xp @ w; V = Xp @ v
    R = lam*V*V + kap*L*L + kap2*L*V
    if epsW is not None:
        R = R + np.einsum('ij,ij->i', Xp @ epsW, Xp)
    T = L + beta
    Qs = 2*rng.uniform(-0.5, 0.5, N_s)*T + R
    lo, hi = np.quantile(Qs, [0.005, 0.995])
    sv = np.unique(np.concatenate([np.linspace(lo, hi, ns), np.linspace(-0.3, 0.3, 61)]))
    acc = np.zeros(len(sv))
    for c0 in range(0, N_s, 5000):
        acc += hub_window_values(0.0, T[c0:c0+5000], R[c0:c0+5000], sv, fh, delta).sum(0)
    pw = acc/(N_s*2*delta)
    A = np.zeros((n1+1, n1+1)); A[0, 1:] = w; A[1:, 0] = w
    A[1:, 1:] = lam*np.outer(v, v) + kap*np.outer(w, w) + kap2*(np.outer(w, v) + np.outer(v, w))/2
    if epsW is not None: A[1:, 1:] += epsW
    m3 = mu3(A); j = int(np.argmax(pw))
    return m3*pw[j], pw[j], sv[j], m3, np.std(L), np.std(V)


if setup == 1:
    w = np.ones(4)/2; v = np.array([1, -1, 1, -1])/2.0
    print("uniform leaves:", [round(x, 4) for x in Fvalue([U()]*4, w, v, 1.0, 1.0)[:4]], flush=True)
    for kap in (1.0, 0.3):
        for N in (2, 3, 4):
            D = 8*N/abs(kap)
            laws = [boxes([q*N**i*D/w[i] for q in range(N)], 1.0/N) for i in range(4)]
            for lam in (1.0, -1.0):
                F, pw, s, m3, sL, sV = Fvalue(laws, w, v, lam, kap)
                Fu = Fvalue([U()]*4, w, v, lam, kap)[0]
                print(f"setup1 kap={kap} N={N} lam={lam:+.0f} D={D:.1f}: bumpy F={F:.5f} (max window-density {pw:.5f} at s={s:.2f}, "
                      f"sd L={sL:.1f}, sd V={sV:.1f})   uniform-leaf F={Fu:.4f}  t={time.time()-t0:.0f}", flush=True)
elif setup == 2:
    n1 = 50
    B, _ = np.linalg.qr(rng.normal(size=(n1, 2))); w, v = B.T
    for kap in (0.1, 1.0):
        for N in (2, 4, 8):
            for Rr in ((1.0, 1.5, 2.0, 4.0, 16.0) if N == 4 else (2.0,)):
                laws = []
                for i in range(n1):
                    if Rr == 1.0:
                        laws.append(U()); continue
                    # N disjoint boxes of width 1/N at random positions in [-R/2, R/2] (rejection for disjointness)
                    for _ in range(1000):
                        c = np.sort(rng.uniform(-Rr/2 + 0.5/N, Rr/2 - 0.5/N, N))
                        if np.all(np.diff(c) >= 1.0/N): break
                    else:
                        c = np.linspace(-Rr/2 + 0.5/N, Rr/2 - 0.5/N, N)
                    laws.append(boxes(c, 1.0/N))
                F, pw, s, m3, sL, sV = Fvalue(laws, w, v, 1.0, kap)
                print(f"setup2 kap={kap} N={N} R={Rr}: F={F:.4f} (window-density {pw:.4f} at s={s:+.3f}, mu3={m3:.3f}, sd L={sL:.3f}) t={time.time()-t0:.0f}", flush=True)
elif setup == 3:
    n1 = 50
    B, _ = np.linalg.qr(rng.normal(size=(n1, 2))); w, v = B.T
    G = rng.normal(size=(n1, n1)); Wg = (G + G.T); Wg /= np.abs(np.linalg.eigvalsh(Wg)).max()
    for M in (4, 8):
        for Dl in (1.0/M, 1.25/M, 1.5/M, 2.0/M, 1.0, 2.0):
            laws = [boxes(np.arange(M)*Dl - (M-1)*Dl/2, 1.0/M)]*n1
            for (kap, epsn) in ((0.0, 0.0), (0.3, 0.0), (1.0, 0.0), (0.3, 0.3)):
                F, pw, s, m3, sL, sV = Fvalue(laws, w, v, 1.0, kap, epsW=(epsn/np.sqrt(n1))*Wg if epsn > 0 else None)
                print(f"setup3 M={M} spacing={Dl:.3f} (psi(2pi/spacing) ~ 1) kap={kap} eps*sqrt(n)={epsn}: F={F:.4f} "
                      f"(window {pw:.4f} at s={s:+.3f}, mu3={m3:.3f}, sd L={sL:.3f}) t={time.time()-t0:.0f}", flush=True)
