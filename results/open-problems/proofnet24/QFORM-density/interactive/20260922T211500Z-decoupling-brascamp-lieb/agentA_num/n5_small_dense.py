try:
    import psutil; psutil.Process().nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
except Exception:
    pass
import numpy as np, itertools
rng = np.random.default_rng(5)
def maxdens(q, h=0.01):
    lo, hi = np.quantile(q, [1e-5, 1-1e-5]); c, _ = np.histogram(q, bins=np.arange(lo, hi+h, h))
    return c.max()/(len(q)*h)
# (d) n=3 bounded-dimensional cores: random search over shifted-uniform laws (density 1 on [c_i-1/2, c_i+1/2])
r = np.ones(3)/np.sqrt(3); A1 = np.eye(3) - 2*np.outer(r, r)          # eigenvalues 1,1,-1, all 2x2 blocks indefinite
A2 = np.ones((3, 3)) - np.eye(3)                                     # zero diagonal: eigenvalues 2,-1,-1
for name, A in [("I-2rr^T", A1), ("J-I (zero diag)", A2)]:
    best = (0, None)
    for trial in range(40):
        c = rng.uniform(-1.0, 1.0, 3) if trial else np.zeros(3)
        X = rng.uniform(-0.5, 0.5, (1_000_000, 3)) + c
        d = maxdens(np.einsum('bi,ij,bj->b', X, A, X))
        if d > best[0]: best = (d, c)
    print(f"(d) {name}: max histogram density over 40 shifted-uniform laws = {best[0]:.3f} at shifts {np.round(best[1],2)}")
# (e) Theorem D on dense examples: Z = e_3(M^T M), marginals, bound 6 sqrt(e) Z^{-1/6}
def esym(x, k):
    E = np.zeros(k+1); E[0] = 1
    for v in x:
        for j in range(k, 0, -1): E[j] += E[j-1]*v
    return E[k]
def thmD(A, I, J):
    M = A[np.ix_(I, J)]; U, s, _ = np.linalg.svd(M, full_matrices=False); s2 = s**2; e3 = esym(s2, 3)
    p = np.array([s2[m]*esym(np.delete(s2, m), 2)/e3 for m in range(len(s2))])
    return e3, ((U**2) @ p).max()
n = 30
O, _ = np.linalg.qr(rng.standard_normal((n, n)))
examples = {"orthogonal-conjugated signs (all |eig|=1)": O @ np.diag(rng.choice([-1.0, 1.0], n)) @ O.T}
R = O[:, :3]; base = R @ np.diag([1.0, 1.0, -1.0]) @ R.T
W = rng.standard_normal((n, n)); W = (W+W.T)/np.sqrt(2*n)
for eps in [0.0, 0.05, 0.2]:
    examples[f"spread rank 3 + {eps}*Wigner"] = base + eps*W
perm = rng.permutation(n); I, J = perm[:n//2], perm[n//2:]
for name, A in examples.items():
    Z, amax = thmD(A, I, J)
    X = rng.uniform(-0.5, 0.5, (1_000_000, n))
    d = maxdens(np.einsum('bi,ij,bj->b', X, A, X))
    print(f"(e) {name}: Z={Z:.4g}, max marginal={amax:.3f}, Thm D bound={6*np.sqrt(np.e)*Z**(-1/6):.2f}, empirical max density={d:.3f}")
