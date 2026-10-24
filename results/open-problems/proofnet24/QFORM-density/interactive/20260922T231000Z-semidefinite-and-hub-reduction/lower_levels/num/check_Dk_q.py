try:
    import psutil; psutil.Process().nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
except Exception:
    pass
import numpy as np
rng = np.random.default_rng(11)
def psi_u(s):
    s = np.asarray(s, float); out = np.ones_like(s); nz = np.abs(s) > 1e-12
    out[nz] = np.sin(s[nz]/2)/(s[nz]/2); return out
def e2(l): s = l.sum(); return 0.5*(s*s - (l*l).sum())
def marg1(A): r = (A**2).sum(1); return r/r.sum()
def marg2(A):
    G = A @ A.T; return (np.diag(G)*np.trace(G) - np.diag(G @ G))/e2(np.linalg.eigvalsh(G))
def EFq(A, t, q, N=100000):
    nI, nJ = A.shape
    W = rng.uniform(-.5, .5, (N, nJ)) - rng.uniform(-.5, .5, (N, nJ))
    Y = W @ A.T
    F = np.ones(N)
    for i in range(nI): F *= np.abs(psi_u(2*t*Y[:, i]))
    return (F**q).mean()
# D_1 at q = 3/2: block with one row carrying ~0.7 of the Frobenius mass
A = 0.05*rng.normal(size=(12, 12)); A[0, :] = rng.normal(size=12)*0.35
m1 = marg1(A); print("D1: max row share", m1.max().round(3), flush=True)
q = 1.5; Z = (A**2).sum(); worst = 0
for t in [1, 3, 10, 30, 100]:
    worst = max(worst, EFq(A, t, q)/(np.exp(0.5)*(2*np.pi/t)*q**-0.5*Z**-0.5))
print("D1 q=1.5: max ratio E F^q / bound =", round(worst, 4), flush=True)
# D_2 at q = 1.2: huge rank-one + O(1) second direction, marginals should be <= 0.6
n = 14
x = rng.normal(size=n); x /= np.linalg.norm(x); y = rng.normal(size=n); y /= np.linalg.norm(y)
u2 = rng.normal(size=n); u2 -= (u2 @ x)*x; u2 /= np.linalg.norm(u2)
v2 = rng.normal(size=n); v2 -= (v2 @ y)*y; v2 /= np.linalg.norm(v2)
A2 = 20*np.outer(x, y) + 1.0*np.outer(u2, v2) + 0.05*rng.normal(size=(n, n))
m2 = marg2(A2); print("D2: max 2-marginal", m2.max().round(3), flush=True)
q = 1.2; Z2 = e2(np.linalg.svd(A2, compute_uv=False)**2); worst = 0
for t in [1, 3, 10, 30]:
    worst = max(worst, EFq(A2, t, q)/(np.e*(2*np.pi/t)**2/q*Z2**-0.5))
print("D2 q=1.2: max ratio E F^q / bound =", round(worst, 4), flush=True)
