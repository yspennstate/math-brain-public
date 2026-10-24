try:
    import psutil; psutil.Process().nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
except Exception:
    pass
# Check: rank-3 forms with a heavy row h and an OUTSIDE linear term beta*<u,X>.
# Exact estimator: condition on X_{-h}, Q = a x^2 + 2 M x + C in x = X_h, p(s) = E sum_roots f_h(x)/|2ax+2M|.
# Compared with a histogram of direct samples; then sup_s over a grid, for several beta.
import numpy as np
rng = np.random.default_rng(7)

def make(n, lh, sig, rng, timelike=False):
    # rows: heavy row r_h with |r_h|^2 = lh, rest spread; columns orthonormal
    G = rng.standard_normal((n - 1, 3)); Qm, _ = np.linalg.qr(G)
    rh_dir = np.array([1.0, 0.0, 0.0]) if not timelike else np.array([0.0, 0.0, 1.0])
    rh = np.sqrt(lh) * rh_dir
    # columns: c_k = [rh_k ; sqrt(1 - rh_k^2) * Qm[:,k]]  -> orthonormal because Qm orthonormal and rh along one axis
    R = np.zeros((n, 3)); R[0] = rh
    for k in range(3):
        R[1:, k] = np.sqrt(1 - rh[k] ** 2) * Qm[:, k]
    L = np.diag(sig).astype(float)
    # outside direction u orthogonal to columns of R
    u = rng.standard_normal(n); u -= R @ (R.T @ u); u /= np.linalg.norm(u)
    return R, L, u

def exact_density(R, L, u, beta, y0, svals, N, rng, law='unif'):
    n = R.shape[0]
    Xr = rng.uniform(-0.5, 0.5, size=(N, n - 1)) if law == 'unif' else sample_spread(N, n - 1, rng)
    r = R[0]; Rr = R[1:]
    D = Xr @ Rr - y0
    LD = D @ L
    a = r @ L @ r
    M = LD @ r + beta * u[0] / 2
    C = np.einsum('ij,ij->i', D, LD) + beta * (Xr @ u[1:])
    out = []
    for s in svals:
        c = C - s
        disc = M * M - a * c
        ok = disc > 0
        sq = np.sqrt(np.where(ok, disc, 0))
        q = -(M + np.where(M >= 0, 1.0, -1.0) * sq)
        vals = np.zeros(N)
        for x in (q / a, c / np.where(q == 0, 1e-300, q)):
            gg = np.abs(2 * a * x + 2 * M)
            inside = ok & (np.abs(x) <= 0.5) & (gg > 0)
            vals += np.where(inside, 1.0 / np.where(gg > 0, gg, 1), 0)
        out.append(vals.mean())
    return np.array(out)

def hist_density(R, L, u, beta, y0, svals, N, rng, width=0.02):
    n = R.shape[0]
    X = rng.uniform(-0.5, 0.5, size=(N, n))
    Y = X @ R - y0
    Qv = np.einsum('ij,jk,ik->i', Y, L, Y) + beta * (X @ u)
    return np.array([np.mean(np.abs(Qv - s) <= width / 2) / width for s in svals])

n = 30
for (lh, sig, tl) in [(0.9, (1, 1, 1), False), (0.99, (1, 1, 1), False), (0.9, (1, 1, -1), False), (0.9, (1, 1, -1), True)]:
    R, L, u = make(n, lh, sig, rng, timelike=tl)
    y0 = rng.normal(0, 0.3, 3)
    for beta in [0.0, 1.0, 5.0]:
        sv = np.array([-0.5, 0.1, 0.4, 1.0])
        e = exact_density(R, L, u, beta, y0, sv, 400000, rng)
        h = hist_density(R, L, u, beta, y0, sv, 2000000, rng)
        print(f"l_h={lh} sig={sig} timelike_heavy={tl} beta={beta:4.1f}  exact {np.round(e,3)}  hist {np.round(h,3)}", flush=True)
    grid = np.linspace(-3, 3, 121)
    for beta in [0.0, 0.3, 1.0, 3.0, 10.0]:
        e = exact_density(R, L, u, beta, y0, grid, 200000, rng)
        print(f"   sup over s in [-3,3], beta={beta:5.1f}: {e.max():.3f} at s={grid[e.argmax()]:+.2f}", flush=True)
