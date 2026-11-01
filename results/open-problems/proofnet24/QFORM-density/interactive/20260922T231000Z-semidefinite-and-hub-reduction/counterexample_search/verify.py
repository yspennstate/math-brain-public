"""Second, independent estimator (E2, fibre identity over all coordinates) for the headline values found by E1 /
window scans / quadrature.  Each case prints both numbers."""
try:
    import psutil; psutil.Process().nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
except Exception:
    pass
import numpy as np, sys, time
from lib import *
case = sys.argv[1]; N = int(sys.argv[2])
t0 = time.time()
if case == 'star':
    n1 = 100; rng = np.random.default_rng(100 + n1)
    B, _ = np.linalg.qr(rng.normal(size=(n1, 2))); w, v = B.T
    A = np.zeros((n1+1, n1+1)); A[0, 1:] = w; A[1:, 0] = w; A[1:, 1:] = np.outer(v, v)
    sv = [0.0, 0.002, 0.004]
    m, se = fibre_density_v(A, [U()]*(n1+1), sv, N=N, rng=np.random.default_rng(5))
    print(f"star n1=100 E2: {np.round(m,4)} +- {np.round(se,4)}  (E1 exact at s=.002: 3.5449 +- .0165; p(0) 3.4770 +- .0195)  t={time.time()-t0:.0f}", flush=True)
elif case == 'wig':
    n1 = 50; rng = np.random.default_rng(3)
    B, _ = np.linalg.qr(rng.normal(size=(n1, 6))); w, v = B.T[:2]
    G = rng.normal(size=(n1, n1)); W = (G + G.T); W /= np.abs(np.linalg.eigvalsh(W)).max()
    eps = 0.3/np.sqrt(n1)
    A = np.zeros((n1+1, n1+1)); A[0, 1:] = w; A[1:, 0] = w; A[1:, 1:] = np.outer(v, v) + eps*W
    sv = [0.0, 0.01, 0.02, 0.03]
    m1, s1 = hub_density(A, [U()]*(n1+1), 0, sv, N=4*N, rng=np.random.default_rng(8))
    m2, s2 = fibre_density_v(A, [U()]*(n1+1), sv, N=N, rng=np.random.default_rng(9))
    print(f"star+eps W (Wigner, eps sqrt n = .3), n1=50: E1 {np.round(m1,4)} +- {np.round(s1,4)} | E2 {np.round(m2,4)} +- {np.round(s2,4)}  mu3={mu3(A):.4f} t={time.time()-t0:.0f}", flush=True)
elif case == 'diag':
    n1 = 100; rng = np.random.default_rng(7)
    B, _ = np.linalg.qr(rng.normal(size=(n1, 6))); w, v = B.T[:2]
    a = 0.1
    A = np.zeros((n1+1, n1+1)); A[0, 0] = a; A[0, 1:] = w; A[1:, 0] = w; A[1:, 1:] = np.outer(v, v)
    sv = [-0.01, 0.0, 0.01, 0.02]
    m1, s1 = hub_density(A, [U()]*(n1+1), 0, sv, N=4*N, rng=np.random.default_rng(8))
    m2, s2 = fibre_density_v(A, [U()]*(n1+1), sv, N=N, rng=np.random.default_rng(9))
    print(f"hub diag a=.1 + rank one, n1=100: E1 {np.round(m1,4)} +- {np.round(s1,4)} | E2 {np.round(m2,4)} +- {np.round(s2,4)}  mu3={mu3(A):.4f} t={time.time()-t0:.0f}", flush=True)
elif case == 'semi':
    # best two-sheet configuration of famE_opt (start 2) realised as an actual product measure with n coordinates
    from famE_semi import density
    rho = np.array([-0.441, 0.062, 0.105]); lam = np.array([1.0, 1.0, -1.002]); b = np.array([-0.116, -0.055, 0.111]); c0 = 0.009
    sv = [-0.0031, -0.01, -0.03]
    pq = density(sv, rho, lam, b, c0, nx=32)
    print(f"semi-Gaussian quadrature: {np.round(pq,4)}", flush=True)
    for n in (40, 160):
        rng = np.random.default_rng(n)
        Qp, _ = np.linalg.qr(rng.normal(size=(n-1, 3)))
        C = np.eye(3) - np.outer(rho, rho); ev, EV = np.linalg.eigh(C); Ch = EV @ np.diag(np.sqrt(ev)) @ EV.T
        R = np.vstack([rho, Qp @ Ch])                       # n x 3, R^T R = I, first row rho
        A = R @ np.diag(lam) @ R.T; bb = R @ b; bb[0] += c0
        m2, s2 = fibre_density_v(A, [U()]*n, sv, N=N, b=bb, rng=np.random.default_rng(3))
        print(f"product measure n={n}: E2 {np.round(m2,4)} +- {np.round(s2,4)}   (R^T R - I max {np.abs(R.T @ R - np.eye(3)).max():.1e}) t={time.time()-t0:.0f}", flush=True)
