"""Alternating best responses for the laws in the hub families (multilinearity: the best response of coordinate i is
the indicator of the top measure-one superlevel set of g_i(x) = p(s | X_i = x)).
Q = a X_h^2 + 2 X_h (L + beta) + lam V^2 + eps X'^T W X', n1 leaves.
 - hub: g_h estimated by the weighted histogram of the E1 roots (weight 1/|2 a x + 2T|), no f_h factor;
 - leaf j: g_j(y) = E[ window density at s | X_j = y ] by substituting X_j -> y (T, R are affine/quadratic in y).
Random multi-interval starts for all laws.  After each round s is re-chosen as the argmax of the window density."""
try:
    import psutil; psutil.Process().nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
except Exception:
    pass
import numpy as np, sys, time
from lib import *
n1 = int(sys.argv[1]); M = int(sys.argv[2]); seed = int(sys.argv[3]); epsn = float(sys.argv[4]); a = float(sys.argv[5])
rounds = int(sys.argv[6]) if len(sys.argv) > 6 else 3
rng = np.random.default_rng(seed); t0 = time.time()
B, _ = np.linalg.qr(rng.normal(size=(n1, 2))); w, v = B.T
G = rng.normal(size=(n1, n1)); Wg = G + G.T; Wg /= np.abs(np.linalg.eigvalsh(Wg)).max()
Wm = (epsn/np.sqrt(n1))*Wg
lam = 1.0; delta = 0.003
grid = np.linspace(-3, 3, 241); gb = grid[1] - grid[0]
edges_h = np.linspace(-4, 4, 401)


def rand_law():
    k = rng.integers(1, 5)
    for _ in range(100):
        c = np.sort(rng.uniform(-2.5, 2.5, k)); ws = rng.dirichlet(np.ones(k))
        a_ = c - ws/2; b_ = c + ws/2
        if np.all(a_[1:] >= b_[:-1]): return PWLaw(a_, b_)
    return U()


def TR(Xp):
    return Xp @ w, lam*(Xp @ v)**2 + np.einsum('ij,ij->i', Xp @ Wm, Xp)


def window_curve(laws, fh, svals, Mloc):
    Xp = sample_X(laws, Mloc, rng); T, R = TR(Xp)
    acc = np.zeros(len(svals))
    for c0 in range(0, Mloc, 10000):
        acc += hub_window_values(a, T[c0:c0+10000], R[c0:c0+10000], svals, fh, delta).sum(0)
    return acc/(Mloc*2*delta)


for start in range(3):
    laws = [U()]*n1 if start == 0 else [rand_law() for _ in range(n1)]
    fh = U() if start == 0 else rand_law()
    sv = np.linspace(-0.6, 0.6, 121)
    pw = window_curve(laws, fh, sv, M); s = sv[int(np.argmax(pw))]
    hist = [round(pw.max(), 4)]
    for rd in range(rounds):
        # hub best response
        Xp = sample_X(laws, M, rng); T, R = TR(Xp)
        if abs(a) < 1e-15:
            x = (s - R)/(2*T); wt = 1/(2*np.abs(T)); xs = [x]; wts = [wt]
        else:
            disc = T*T - a*(R - s); ok = disc > 0; sq = np.sqrt(np.where(ok, disc, 0))
            xs = [(-T + sq)/a, (-T - sq)/a]; wts = [np.where(ok, 1/(2*np.maximum(sq, 1e-300)), 0.0)]*2
        gh = np.zeros(len(edges_h) - 1)
        for x, wt in zip(xs, wts):
            gh += np.histogram(x, bins=edges_h, weights=wt)[0]
        gh /= (M*(edges_h[1] - edges_h[0]))
        fh = top_set_law(smooth(gh, 2), edges_h)
        # leaf best responses (Jacobi, all leaves from one sample)
        Xp = sample_X(laws, M//4, rng); T, R = TR(Xp); Vv = Xp @ v; WX = Xp @ Wm
        new = []
        for j in range(n1):
            dy = grid[None, :] - Xp[:, j:j+1]                         # (m, G)
            Tj = T[:, None] + w[j]*dy
            Rj = R[:, None] + lam*(2*Vv[:, None]*v[j]*dy + v[j]**2*dy*dy) + 2*WX[:, j:j+1]*dy + Wm[j, j]*dy*dy
            gj = np.zeros(len(grid))
            for gi in range(len(grid)):
                gj[gi] = hub_window_values(a, Tj[:, gi], Rj[:, gi], [s], fh, delta)[:, 0].mean()/(2*delta)
            e = np.concatenate([grid - gb/2, [grid[-1] + gb/2]])
            new.append(top_set_law(smooth(gj, 1), e))
        laws = new
        pw = window_curve(laws, fh, sv, M); s = sv[int(np.argmax(pw))]
        hist.append(round(pw.max(), 4))
        print(f"  start {start} round {rd}: window max {pw.max():.4f} at s={s:+.3f}; hub law {fh.desc(3)}; leaf0 {laws[0].desc(3)}; "
              f"leaf1 {laws[1].desc(3)}  t={time.time()-t0:.0f}", flush=True)
    print(f"n1={n1} eps*sqrt(n)={epsn} a={a} start {start}: trajectory {hist}", flush=True)
