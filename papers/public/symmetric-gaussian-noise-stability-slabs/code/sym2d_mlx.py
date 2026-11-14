"""In R^2: search symmetric sets A = -A in R^2 of Gaussian measure a for maximal noise stability
P(X in A, Y in A), from many random symmetric starts, and compare with the best cylinder (ball, strip, complements).
Grid [-L, L]^2, N cells per axis. With K1[i,j] = P(X1 in I_i, Y1 in I_j), Stab(f) = sum f * (K1 f K1).
K1 is PSD, so Frank-Wolfe with full step (take cells by (K1 f K1) / w up to mass a, then symmetrize) never lowers Stab.
Search on the GPU in float32 (MLX); every reported value is recomputed in float64 with numpy."""
import math, sys, time, json
import numpy as np
import mlx.core as mx

L, N, Q = 6.5, int(sys.argv[2]) if len(sys.argv) > 2 else 256, 6
edges = np.linspace(-L, L, N + 1)
gx, gw = np.polynomial.legendre.leggauss(Q)
_erfc = np.frompyfunc(math.erfc, 1, 1)
ndtr = lambda z: np.asarray(0.5 * _erfc(-np.asarray(z, float) / math.sqrt(2)), dtype=float)

def kernel1(rho):
    s = math.sqrt(1 - rho * rho)
    lo, hi = edges[:-1], edges[1:]
    xs = (lo + hi)[:, None] / 2 + (hi - lo)[:, None] / 2 * gx[None, :]
    wx = (hi - lo)[:, None] / 2 * gw[None, :] * np.exp(-xs ** 2 / 2) / math.sqrt(2 * math.pi)
    e = edges.copy(); e[0], e[-1] = -40, 40                     # outer cells absorb the tails in y
    c = ndtr((e[None, :] - rho * xs.ravel()[:, None]) / s)
    K = (wx.ravel()[:, None] * np.diff(c, axis=1)).reshape(N, Q, N).sum(1)
    return (K + K.T) / 2

w1 = ndtr(edges[1:]) - ndtr(edges[:-1]); w1[0] += ndtr(-L); w1[-1] += ndtr(-L)
W2 = np.outer(w1, w1)
xc = (edges[:-1] + edges[1:]) / 2
X1, X2 = np.meshgrid(xc, xc, indexing='ij')

def stab64(K, f):
    return float((f * (K @ f @ K)).sum())

def fw(K, F, a, iters=300):
    Km = mx.array(K.astype(np.float32)); Wf = mx.array(W2.ravel().astype(np.float32))
    W2m = mx.array(W2.astype(np.float32))
    F = mx.array(F.astype(np.float32)); B = F.shape[0]
    for it in range(iters):
        g = (Km @ F @ Km) / W2m
        order = mx.argsort(-g.reshape(B, -1), axis=1)
        ws = mx.take(Wf, order)
        cw = mx.cumsum(ws, axis=1)
        take = (cw <= a).astype(mx.float32)
        k = mx.sum(take, axis=1).astype(mx.int32)
        prev = mx.where(k > 0, mx.take_along_axis(cw, mx.maximum(k - 1, 0)[:, None], axis=1)[:, 0], 0.0)
        nxt = mx.take_along_axis(ws, mx.minimum(k, N * N - 1)[:, None], axis=1)[:, 0]
        frac = mx.clip((a - prev) / nxt, 0, 1)
        pos = mx.arange(N * N)[None, :]
        vals = take + mx.where(pos == k[:, None], frac[:, None], 0.0)
        G = mx.put_along_axis(mx.zeros((B, N * N)), order, vals, axis=1).reshape(B, N, N)
        G = (G + G[:, ::-1, ::-1]) / 2
        d = mx.max(mx.abs(G - F)).item()
        F = G
        if d < 1e-6:
            break
    return np.array(F).astype(np.float64), it

def fw64(K, f, a, iters=60):
    """float64 Frank-Wolfe polish of one set (numpy, CPU)."""
    w = W2.ravel()
    for _ in range(iters):
        g = (K @ f @ K).ravel() / w
        o = np.argsort(-g, kind='stable')
        cw = np.cumsum(w[o]); k = int((cw <= a).sum())
        G = np.zeros(N * N); G[o[:k]] = 1
        if k < N * N:
            G[o[k]] = (a - (cw[k - 1] if k else 0.0)) / w[o[k]]
        G = G.reshape(N, N); G = (G + G[::-1, ::-1]) / 2
        if np.abs(G - f).max() < 1e-12:
            return G
        f = G
    return f

def mass_fix(f, a):                      # float64 mass check
    return float((f * W2).sum()) - a

def cyl_starts(a):
    from math import log, sqrt
    out = {}
    r = sqrt(-2 * log(1 - a)); out['ball'] = (X1 ** 2 + X2 ** 2 <= r * r).astype(float)
    rc = sqrt(-2 * log(a)); out['ball_c'] = (X1 ** 2 + X2 ** 2 >= rc * rc).astype(float)
    lo, hi = 0, 40
    for _ in range(100):
        m = (lo + hi) / 2
        if math.erf(m / math.sqrt(2)) < a: lo = m
        else: hi = m
    out['strip'] = (np.abs(X1) <= lo).astype(float)
    lo2, hi2 = 0, 40
    for _ in range(100):
        m = (lo2 + hi2) / 2
        if math.erf(m / math.sqrt(2)) < 1 - a: lo2 = m
        else: hi2 = m
    out['strip_c'] = (np.abs(X1) >= lo2).astype(float)
    return out

def random_starts(rng, B, a):
    F = np.zeros((B, N, N))
    for b in range(B):
        kind = b % 4
        if kind == 0:                     # random low-frequency field, symmetrized
            h = np.zeros((N, N))
            for _ in range(rng.integers(3, 12)):
                kx, ky = rng.normal(0, 1.2, 2); ph = rng.uniform(0, 2 * np.pi)
                h += rng.normal() * np.cos(kx * X1 + ky * X2 + ph)
        elif kind == 1:                   # random radial-angular field
            R = np.hypot(X1, X2); T = np.arctan2(X2, X1)
            h = sum(rng.normal() * np.cos(m * T + rng.uniform(0, 6.3)) * np.cos(rng.uniform(0.3, 3) * R)
                    for m in range(0, 7, 2))
        elif kind == 2:                   # random symmetric union of ellipses and strips
            h = np.zeros((N, N))
            for _ in range(rng.integers(1, 4)):
                A = rng.normal(size=(2, 2)); S = A @ A.T + 0.1 * np.eye(2)
                q = S[0, 0] * X1 ** 2 + 2 * S[0, 1] * X1 * X2 + S[1, 1] * X2 ** 2
                h = np.maximum(h, np.exp(-q * rng.uniform(0.2, 2)))
            if rng.random() < 0.5: h = -h
        else:                             # white noise, smoothed a little
            h = rng.normal(size=(N, N))
            for _ in range(rng.integers(1, 20)):
                h = (h + np.roll(h, 1, 0) + np.roll(h, -1, 0) + np.roll(h, 1, 1) + np.roll(h, -1, 1)) / 5
        h = h + h[::-1, ::-1]
        o = np.argsort(-(h.ravel()))
        cw = np.cumsum(W2.ravel()[o])
        f = np.zeros(N * N); f[o[cw <= a]] = 1
        F[b] = f.reshape(N, N)
    return F

if __name__ == '__main__':
    EXACT = json.load(open('exact_cyl.json'))
    seed = int(sys.argv[1]) if len(sys.argv) > 1 else 0
    rng = np.random.default_rng(seed)
    rhos = [0.1, 0.3, 0.5, 0.7, 0.9]
    As = [0.05, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.95]
    B = int(sys.argv[3]) if len(sys.argv) > 3 else 128
    t0 = time.time()
    for rho in rhos:
        K = kernel1(rho)
        for a in As:
            cs = cyl_starts(a)
            Fc, _ = fw(K, np.stack(list(cs.values())), a, iters=100)
            Fc = np.stack([fw64(K, f, a) for f in Fc])
            cv = {n: stab64(K, Fc[i]) for i, n in enumerate(cs)}
            cbest = max(cv, key=cv.get)
            F, its = fw(K, random_starts(rng, B, a), a)
            v32 = np.array([float((f * (K @ f @ K)).sum()) for f in F])
            top = np.argsort(-v32)[:6]
            for t in top:
                F[t] = fw64(K, F[t], a)
            vals = np.full(len(F), -1.0); vals[top] = [stab64(K, F[t]) for t in top]
            k = int(vals.argmax())
            ex = EXACT[f'{rho}_{a}']; ebest = max(ex.values())
            derr = abs(ex[cbest] - cv[cbest])            # discretization error of the winning cylinder
            gap = vals[k] / cv[cbest] - 1
            egap = vals[k] - ebest                       # vs the exact continuum cylinder optimum
            flag = 'CANDIDATE' if egap > 3 * derr + 1e-9 and gap > 1e-6 else ''
            # nearest cylinder to the best random-start set, by symmetric-difference mass
            sd = {n: float((np.abs(F[k] - Fc[i]) * W2).sum()) for i, n in enumerate(cs)}
            # also allow 90-degree rotation of the strips (the grid has two axis strips)
            for i, n in enumerate(cs):
                if 'strip' in n:
                    sd[n + '_rot'] = float((np.abs(F[k] - Fc[i].T) * W2).sum())
            near = min(sd, key=sd.get)
            nwin = int((v32 > cv[cbest] * (1 + 1e-4)).sum())
            print(f"rho={rho} a={a} cyl_best={cbest} {cv[cbest]:.10f} search_best={vals[k]:.10f} rel_gap={gap:+.2e} "
                  f"n_above_cyl={nwin}/{B} nearest={near} symdiff={sd[near]:.2e} mass_err={mass_fix(F[k], a):.1e} "
                  f"iters={its} exact_cyl={ebest:.10f} disc_err={derr:.1e} gap_vs_exact={egap:+.2e} {flag} ({time.time() - t0:.0f}s)", flush=True)
            if gap > 1e-6:
                np.save(f"best_rho{rho}_a{a}_s{seed}.npy", F[k].astype(np.float32))
    print('done', f'{time.time() - t0:.0f}s')
