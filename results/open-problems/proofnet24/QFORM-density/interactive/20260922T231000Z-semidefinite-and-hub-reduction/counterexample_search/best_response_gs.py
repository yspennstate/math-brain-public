"""Gauss-Seidel alternating best responses (one coordinate at a time, fresh samples for each update) for
Q = a X_h^2 + 2 X_h (L + beta) + lam V^2 + eps X'^T W X'.  The Jacobi version (best_response.py) overshoots: every
leaf's partial density is nearly monotone in its own shift, so simultaneous top-set jumps compound (documented).
g_j is estimated with the exact window estimator by substituting X_j -> y on a grid; g_h by the E1 root histogram."""
try:
    import psutil; psutil.Process().nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
except Exception: pass
import numpy as np, sys, time
from lib import *
n1 = int(sys.argv[1]); M = int(sys.argv[2]); seed = int(sys.argv[3]); epsn = float(sys.argv[4]); a = float(sys.argv[5])
rounds = int(sys.argv[6]); nstarts = int(sys.argv[7])
rng = np.random.default_rng(seed); t0 = time.time()
B, _ = np.linalg.qr(rng.normal(size=(n1, 2))); w, v = B.T
G = rng.normal(size=(n1, n1)); Wg = G + G.T; Wg /= np.abs(np.linalg.eigvalsh(Wg)).max(); Wm = (epsn/np.sqrt(n1))*Wg
lam = 1.0; delta = 0.003
grid = np.linspace(-2, 2, 161); gb = grid[1] - grid[0]; eg = np.concatenate([grid - gb/2, [grid[-1] + gb/2]])
edges_h = np.linspace(-3, 3, 301)
def rand_law():
    k = rng.integers(1, 4)
    for _ in range(200):
        c = np.sort(rng.uniform(-1.0, 1.0, k)); ws = rng.dirichlet(np.ones(k))
        a_ = c - ws/2; b_ = c + ws/2
        if np.all(a_[1:] >= b_[:-1]): return PWLaw(a_, b_)
    return U()
def TR(Xp): return Xp @ w, lam*(Xp @ v)**2 + np.einsum('ij,ij->i', Xp @ Wm, Xp)
def curve(laws, fh, sv, Ml):
    Xp = sample_X(laws, Ml, rng); T, R = TR(Xp); acc = np.zeros(len(sv))
    for c0 in range(0, Ml, 10000):
        acc += hub_window_values(a, T[c0:c0+10000], R[c0:c0+10000], sv, fh, delta).sum(0)
    return acc/(Ml*2*delta)
sv = np.linspace(-0.5, 0.5, 101)
for st in range(nstarts):
    laws = [U()]*n1 if st == 0 else [rand_law() for _ in range(n1)]; fh = U() if st == 0 else rand_law()
    pw = curve(laws, fh, sv, M); s = sv[int(np.argmax(pw))]; traj = [round(pw.max(), 4)]
    for rd in range(rounds):
        # hub
        Xp = sample_X(laws, M, rng); T, R = TR(Xp)
        if abs(a) < 1e-15:
            gh = np.histogram((s - R)/(2*T), bins=edges_h, weights=1/(2*np.abs(T)))[0]
        else:
            disc = T*T - a*(R - s); ok = disc > 0; sq = np.sqrt(np.where(ok, disc, 0)); wt = np.where(ok, 1/(2*np.maximum(sq, 1e-300)), 0)
            gh = np.histogram((-T + sq)/a, bins=edges_h, weights=wt)[0] + np.histogram((-T - sq)/a, bins=edges_h, weights=wt)[0]
        fh = top_set_law(smooth(gh/(M*(edges_h[1]-edges_h[0])), 2), edges_h)
        # leaves, one at a time
        for j in range(n1):
            Xp = sample_X(laws, M//3, rng); T, R = TR(Xp); Vv = Xp @ v; WX = Xp @ Wm
            dy = grid[None, :] - Xp[:, j:j+1]
            Tj = T[:, None] + w[j]*dy
            Rj = R[:, None] + lam*(2*Vv[:, None]*v[j]*dy + v[j]**2*dy*dy) + 2*(WX[:, j:j+1] - Wm[j, j]*Xp[:, j:j+1])*dy + Wm[j, j]*(grid[None, :]**2 - Xp[:, j:j+1]**2) - 0*dy
            # exact update of eps x^T W x when x_j -> y:  2 y (W x)_{-j}  + W_jj y^2  minus the old terms
            gj = np.array([hub_window_values(a, Tj[:, g], Rj[:, g], [s], fh, delta)[:, 0].mean() for g in range(len(grid))])/(2*delta)
            laws = laws[:j] + [top_set_law(smooth(gj, 1), eg)] + laws[j+1:]
        pw = curve(laws, fh, sv, M); s = sv[int(np.argmax(pw))]; traj.append(round(pw.max(), 4))
        print(f"  start {st} round {rd}: window max {pw.max():.4f} at s={s:+.3f}; hub {fh.desc(3)}; leaf0 {laws[0].desc(3)}; leaf1 {laws[1].desc(3)} t={time.time()-t0:.0f}", flush=True)
    print(f"n1={n1} eps*sqrt(n)={epsn} a={a} start {st}: trajectory {traj}", flush=True)
