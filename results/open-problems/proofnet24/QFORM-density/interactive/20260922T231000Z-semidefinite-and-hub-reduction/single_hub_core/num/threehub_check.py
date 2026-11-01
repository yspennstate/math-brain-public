import numpy as np
rng = np.random.default_rng(7)
N = 4_000_000
def comb(n, teeth, gap):
    k = rng.integers(0, teeth, n); u = rng.random(n) / teeth
    return k * gap + u
def peak(Q, widths=(0.02, 0.01, 0.005)):
    out = []
    for w in widths:
        lo, hi = np.percentile(Q, 0.01), np.percentile(Q, 99.99)
        bins = np.arange(lo, hi + w, w)
        h, _ = np.histogram(Q, bins=bins)
        out.append(h.max() / (N * w))
    return out
def run(name, lawH, lawX, B, M, Rfun):
    XH = np.stack([lawH() for _ in range(3)], 1)
    Xp = np.stack([lawX() for _ in range(M.shape[1])], 1)
    L = Xp @ M.T
    Q = np.einsum('ni,ij,nj->n', XH, B, XH) + 2 * np.einsum('ni,ni->n', XH, L) + Rfun(Xp, L)
    s = np.linalg.svd(M, compute_uv=False)
    bound = 3 * np.sqrt(2) * np.prod(s[:3]) ** (-1/3)
    print(f"{name:34s} peak(w=.02,.01,.005) = " + ", ".join(f"{p:.3f}" for p in peak(Q)) + f"   bound {bound:.2f}")
U = lambda: rng.random(N)
C = lambda: comb(N, 8, 5.0)
M = np.eye(3)
B1 = np.array([[0,1,0],[1,0,0],[0,0,0.]])
run("unif, B swap, R=2L1L2", U, U, B1, M, lambda X, L: 2*L[:,0]*L[:,1])
B2 = np.diag([1.0, 1.0, -1.0])
Binv = np.linalg.inv(B2)
run("unif, Schur-matched indefinite", U, U, B2, M, lambda X, L: np.einsum('ni,ij,nj->n', L, Binv, L))
run("comb light, Schur-matched", U, C, B2, M, lambda X, L: np.einsum('ni,ij,nj->n', L, Binv, L))
run("comb all, Schur-matched", C, C, B2, M, lambda X, L: np.einsum('ni,ij,nj->n', L, Binv, L))
run("unif, B=0, R=-sum L^2 ... wild", U, U, np.zeros((3,3)), M, lambda X, L: 30*np.sin(X[:,0]*X[:,1]) - (L**2).sum(1))
run("unif, B small, R=0", U, U, 0.01*B2, M, lambda X, L: 0*L[:,0])
print("done")
