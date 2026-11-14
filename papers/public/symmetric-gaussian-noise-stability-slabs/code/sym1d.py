"""Dimension 1: among symmetric A in R with gamma(A) = a, is noise stability
P(X in A, Y in A) maximized by a centred interval or its complement, for every rho in (0,1)?
Discretize [0, L] into N cells; a symmetric set is a 0/1 vector on cells (each cell stands for +-cell).
M[i,j] = P(X in +-I_i, Y in +-I_j) (Gauss-Legendre in x, exact normal cdf in y). Stab = f^T M f, M is PSD,
so Frank-Wolfe with full step (greedy by (Mf)_i / W_i up to mass a) increases Stab monotonically.
Random symmetric starts; compare the best local maximum with the exact interval / complement values."""
import sys, time
import numpy as np
import math
_erfc = np.frompyfunc(math.erfc, 1, 1)

def ndtr(z):
    z = np.asarray(z, dtype=float)
    return (0.5 * _erfc(-z / math.sqrt(2))).astype(float)

def gamma_inv_sym(a):
    lo, hi = 0.0, 40.0                               # t with P(|Z| <= t) = a
    for _ in range(200):
        mid = (lo + hi) / 2
        if math.erf(mid / math.sqrt(2)) < a: lo = mid
        else: hi = mid
    return (lo + hi) / 2

L, N, Q = 7.0, 1400, 6
edges = np.linspace(0, L, N + 1)
gx, gw = np.polynomial.legendre.leggauss(Q)

def kernel(rho):
    s = np.sqrt(1 - rho * rho)
    lo, hi = edges[:-1], edges[1:]
    xs = (lo[:, None] + hi[:, None]) / 2 + (hi - lo)[:, None] / 2 * gx[None, :]       # N x Q
    wx = (hi - lo)[:, None] / 2 * gw[None, :] * np.exp(-xs ** 2 / 2) / np.sqrt(2 * np.pi)
    x = xs.ravel(); w = wx.ravel()
    def strip(sign):   # P(Y in sign * I_j | x) for all j, as (NQ x N)
        e = sign * edges
        c = ndtr((e[None, :] - rho * x[:, None]) / s)
        return np.abs(np.diff(c, axis=1))
    P = strip(1) + strip(-1)                         # Y in +-I_j
    Mh = (w[:, None] * P).reshape(N, Q, N).sum(1)    # X in +I_i
    M = 2 * Mh                                       # X in +-I_i (symmetry)
    return (M + M.T) / 2

W = 2 * (ndtr(edges[1:]) - ndtr(edges[:-1]))

def fw(M, F, a, iters=200):
    for _ in range(iters):
        g = (F @ M) / W
        order = np.argsort(-g, axis=1)
        cw = np.cumsum(W[order], axis=1)
        take = cw <= a + 1e-15
        G = np.zeros_like(F)
        np.put_along_axis(G, order, take.astype(float), axis=1)
        # fractional last cell to hit mass a exactly
        k = take.sum(1)
        rem = a - np.where(k > 0, cw[np.arange(len(F)), np.maximum(k - 1, 0)], 0) * (k > 0)
        idx = order[np.arange(len(F)), np.minimum(k, N - 1)]
        G[np.arange(len(F)), idx] += np.clip(rem / W[idx], 0, 1)
        if np.abs(G - F).max() < 1e-12:
            break
        F = G
    return F, np.einsum('ki,ij,kj->k', F, M, F)

def exact_interval(a, rho):
    t = gamma_inv_sym(a)                             # gamma([-t,t]) = a
    s = math.sqrt(1 - rho * rho)
    x, w = np.polynomial.legendre.leggauss(400)
    x = t * x; w = t * w
    phi = np.exp(-x ** 2 / 2) / math.sqrt(2 * math.pi)
    return float((w * phi * (ndtr((t - rho * x) / s) - ndtr((-t - rho * x) / s))).sum())

def exact_best(a, rho):
    I = exact_interval(a, rho)
    C = 2 * a - 1 + exact_interval(1 - a, rho)      # complement of the interval of measure 1-a
    return I, C

if __name__ == '__main__':
    rng = np.random.default_rng(int(sys.argv[1]) if len(sys.argv) > 1 else 0)
    K = 300
    rhos = [0.05, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.95]
    As = [0.02, 0.05, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.95, 0.98]
    t0 = time.time(); worst = (-1, None)
    for rho in rhos:
        M = kernel(rho)
        for a in As:
            I, C = exact_best(a, rho)
            # starts: random symmetric sets of varied block structure, plus interval / complement
            F = np.zeros((K, N))
            for k in range(K):
                blocks = rng.integers(2, 40)
                cut = np.sort(rng.choice(N, blocks, replace=False))
                lab = rng.integers(0, 2, blocks + 1)
                F[k] = np.repeat(lab, np.diff(np.r_[0, cut, N]))
            F[0] = 0; F[0][:N // 2] = 1
            F[1] = 0; F[1][N // 2:] = 1
            F, val = fw(M, F, a)
            # discretised interval / complement values for a like-for-like comparison
            Fi = np.zeros((2, N)); Fi[0][:N // 2] = 1; Fi[1][N // 2:] = 1
            _, vi = fw(M, Fi, a, iters=50)
            ref = vi.max()
            k = int(val.argmax())
            gap = val[k] / ref - 1
            sw = np.abs(np.diff(F[k])).sum() // 1
            print(f"rho={rho:.2f} a={a:.2f} best={val[k]:.10f} disc_ref={ref:.10f} exact I={I:.10f} C={C:.10f} "
                  f"rel_gap={gap:.2e} switches={int(sw)}", flush=True)
            if gap > worst[0]:
                worst = (gap, rho, a, F[k].round(3)[::20].tolist())
    print('largest relative gap:', worst[:3], f'({time.time() - t0:.0f}s)')
    if worst[0] > 1e-8:
        print('best set (every 20th cell of [0,L]):', worst[3])
