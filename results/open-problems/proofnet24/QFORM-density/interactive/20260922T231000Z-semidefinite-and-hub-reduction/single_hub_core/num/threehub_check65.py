import numpy as np
rng = np.random.default_rng(11)
N = 3_000_000
m = 12
J = np.arange(0, 8); I = np.arange(8, 12)
# partners on all coordinates (M_I != 0 allowed), transverse square straddling, dense twist
Wp = rng.standard_normal((2, m)); Wp = np.linalg.qr(Wp.T)[0].T  # 2 orthonormal partner rows
v = rng.standard_normal(m); v -= Wp.T @ (Wp @ v); v /= np.linalg.norm(v)
def comb(n, teeth, gap):
    k = rng.integers(0, teeth, n); u = rng.random(n) / teeth
    return k * gap + u
def peak(Q, w):
    lo, hi = np.percentile(Q, 0.005), np.percentile(Q, 99.995)
    h, _ = np.histogram(Q, bins=np.arange(lo, hi + w, w))
    return h.max() / (N * w)
for eps, law, lam in [(0.0, "unif", 1.0), (0.5, "unif", 1.0), (2.0, "unif", 1.0), (0.5, "comb", 1.0), (2.0, "comb", 1.0), (0.5, "comb", 0.2)]:
    W = rng.standard_normal((m, m)); W = (W + W.T) / 2; np.fill_diagonal(W, 0); W /= np.linalg.norm(W)
    A = lam * np.outer(v, v) + eps * W
    MJ = Wp[:, J]
    s = np.linalg.svd(MJ, compute_uv=False)
    P = MJ.T @ np.linalg.pinv(MJ @ MJ.T) @ MJ          # projection onto row space of M_J
    C = A[np.ix_(I, J)] @ (np.eye(len(J)) - P)
    F = np.linalg.norm(C); lev = (np.linalg.norm(C, axis=1) ** 2).max() / F ** 2
    bound = 5.35 * (s[0] * s[1] * F) ** (-1/3)
    X = np.stack([ (rng.random(N) if law == "unif" else comb(N, 6, 4.0)) for _ in range(m)], 1)
    XH = np.stack([rng.random(N), rng.random(N)], 1)
    B = np.array([[0.3, 1.0], [1.0, -0.2]])
    L = X @ Wp.T
    Q = np.einsum('ni,ij,nj->n', XH, B, XH) + 2 * (XH * L).sum(1) + np.einsum('ni,ij,nj->n', X, A, X)
    print(f"eps={eps} law={law} lam={lam}: F={F:.3f} max row share={lev:.2f} s'={s[0]:.2f},{s[1]:.2f} "
          f"peak(.02)={peak(Q,.02):.3f} peak(.005)={peak(Q,.005):.3f}  bound {bound:.2f}", flush=True)
