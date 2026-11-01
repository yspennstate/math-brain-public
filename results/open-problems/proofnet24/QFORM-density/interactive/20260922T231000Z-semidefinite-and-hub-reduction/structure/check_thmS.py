try:
    import psutil; psutil.Process().nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
except Exception:
    pass
import numpy as np
from itertools import combinations
rng = np.random.default_rng(1)

def marginals(M, k=3):
    # volume-sampling I-marginals alpha_i = sum_m p_m u_m(i)^2, p_m = s_m^2 e_{k-1}(s^2_{-m}) / e_k(s^2)
    Uu, s, Vt = np.linalg.svd(M, full_matrices=False)
    x = s**2
    def esym(v, j):
        e = np.zeros(j+1); e[0] = 1.0
        for t in v:
            e[1:] = e[1:] + t*e[:-1]
        return e[j]
    ek = esym(x, k)
    p = np.array([x[m]*esym(np.delete(x, m), k-1)/ek for m in range(len(x))])
    return (Uu**2) @ p, p

def brute_marginals(M, k=3):
    I, J = M.shape
    num = np.zeros(I); Z = 0.0
    for S in combinations(range(I), k):
        for T in combinations(range(J), k):
            d = np.linalg.det(M[np.ix_(S, T)])**2
            Z += d
            num[list(S)] += d
    return num/Z

# 1. marginal formula vs brute force, and the bound alpha_i <= 3||m_i||^2 / T3, T3 = sum_{j>=3} s_j^2
worst = 0.0; worst_bound = 0.0
for trial in range(20):
    I, J = rng.integers(4, 7), rng.integers(4, 7)
    M = rng.standard_normal((I, J)) * rng.uniform(0.1, 3, size=(I, 1))
    a1, _ = marginals(M); a2 = brute_marginals(M)
    worst = max(worst, np.max(np.abs(a1-a2)))
    s = np.linalg.svd(M, compute_uv=False)
    T3 = np.sum(s[2:]**2)
    bnd = 3*np.sum(M**2, axis=1)/T3
    worst_bound = max(worst_bound, np.max(a2/np.minimum(bnd, 1e300)))
print("marginal formula max error:", worst, flush=True)
print("max alpha_i / (3||m_i||^2/T3):", worst_bound, "(must be <= 1)", flush=True)

# 2. the identity 4 Phi = (I+Delta) Lambda (I-Delta) - U^T D R D U
n = 60
A = rng.standard_normal((n, n)); A = (A + A.T)/np.sqrt(2*n)
w, V = np.linalg.eigh(A)
U = V[:, :3]; Lam = np.diag(w[:3]); Rm = A - U @ Lam @ U.T
eps = rng.choice([-1, 1], size=n); xi = (1+eps)/2
Iset = np.where(xi == 1)[0]; Jset = np.where(xi == 0)[0]
Phi = U[Iset].T @ A[np.ix_(Iset, Jset)] @ U[Jset]
Delta = U.T @ np.diag(eps) @ U
rhs = (np.eye(3)+Delta) @ Lam @ (np.eye(3)-Delta) - U.T @ np.diag(eps) @ Rm @ np.diag(eps) @ U
print("identity error:", np.max(np.abs(4*Phi - rhs)), flush=True)

# 3. Theorem S test: matrices with 3 eigenvalues of modulus >= 1 and small rows, several remainders
def make(n, kind, eta_target):
    Q, _ = np.linalg.qr(rng.standard_normal((n, n)))
    U = Q[:, :3]
    lam = np.array([1.0, -1.0, 1.0]) if kind != 'big' else np.array([1.0, 40.0, -3.0])
    B = U @ np.diag(lam) @ U.T
    if kind == 'noise':
        W = rng.standard_normal((n, n)); W = (W+W.T)/np.sqrt(2*n)
        P = np.eye(n) - U @ U.T
        R = P @ W @ P * 0.9 / np.linalg.norm(P @ W @ P, 2)
    elif kind == 'cancel':
        # remainder chosen to cancel the diagonal of the big part as much as possible (zero diagonal of M)
        P = np.eye(n) - U @ U.T
        R = -P @ np.diag(np.diag(B)) @ P
    else:
        R = np.zeros((n, n))
    M = B + R
    return M, U

for kind in ['plain', 'noise', 'cancel', 'big']:
    for n in [200, 800]:
        M, U = make(n, kind, 0.05)
        eta = np.max(np.linalg.norm(M, axis=1))
        s3s = []; amax = []
        for t in range(40):
            xi = rng.integers(0, 2, size=n)
            Iset = np.where(xi == 1)[0]; Jset = np.where(xi == 0)[0]
            B = M[np.ix_(Iset, Jset)]
            s = np.linalg.svd(B, compute_uv=False)
            s3s.append(s[2])
            a, _ = marginals(B)
            amax.append(a.max())
        s3s = np.array(s3s); amax = np.array(amax)
        print(f"{kind:7s} n={n:4d} max row norm={eta:.3f}  s3 median={np.median(s3s):.3f} min={s3s.min():.3f}"
              f"  max marginal median={np.median(amax):.3f} max={amax.max():.3f}", flush=True)
