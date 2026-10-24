"""H0020 (Neri-Pinto arXiv:2607.07309, Remark 3.7): is lambda_max(symm(C_p J_p (R^T - lambda I) C_p^T)) < 0 for p = d-1 (or p = d)
for every tenable, irreducible generalized Polya urn with balance lambda?  C_{d-1} = [I_{d-1} | -1] ((d-1) x d), J_{d-1} = diag(1,..,1,0).
Equivalently: for every mean-zero w in R^d, sum_{i<d} w_i (w(R - lambda I))_i <= -A sum_{i<d} w_i^2 with A > 0.
Random search over integer replacement matrices with nonnegative off-diagonal entries, rows summing to lambda, diagonal >= 0 or negative
(tenable if the divisibility holds - we only need a witness; we then check tenability of the witness by hand)."""
import numpy as np, itertools, sys
rng = np.random.default_rng(int(sys.argv[1]) if len(sys.argv) > 1 else 0)
def lam_max(R, lam, p):
    d = R.shape[0]
    if p == d:
        C = np.eye(d); J = np.eye(d)
    else:
        C = np.hstack([np.eye(d - 1), -np.ones((d - 1, 1))]); J = np.diag([1.0] * (d - 1) + [0.0])
    M = C @ J @ (R.T - lam * np.eye(d)) @ C.T
    return np.max(np.linalg.eigvalsh((M + M.T) / 2))
def irreducible(R):
    d = R.shape[0]; A = (R > 0).astype(int); np.fill_diagonal(A, 1)
    return np.all(np.linalg.matrix_power(A, d) > 0)
best = (-np.inf, None)
for t in range(int(sys.argv[2]) if len(sys.argv) > 2 else 200000):
    d = rng.integers(3, 6); lam = int(rng.integers(1, 7))
    R = np.zeros((d, d), dtype=int)
    for i in range(d):
        # choose off-diagonal nonneg integers, then diagonal = lam - offsum (may be negative: allowed if tenable)
        off = rng.integers(0, lam + 3, size=d - 1) * (rng.random(d - 1) < rng.uniform(0.3, 1.0))
        R[i, [j for j in range(d) if j != i]] = off
        R[i, i] = lam - off.sum()
    if not irreducible(R): continue
    if np.any(R[~np.eye(d, dtype=bool)] < 0): continue
    v = lam_max(R.astype(float), lam, d - 1)
    if v > best[0]: best = (v, R.copy())
print("max over trials of lambda_max (p = d-1):", best[0])
print("witness R =\n", best[1])
R = best[1]; d = R.shape[0]; lam = R.sum(1)[0]
print("row sums:", R.sum(1), " p=d value:", lam_max(R.astype(float), lam, d))
