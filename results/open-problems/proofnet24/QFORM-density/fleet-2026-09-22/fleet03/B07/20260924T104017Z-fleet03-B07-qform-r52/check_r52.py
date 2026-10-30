"""Deterministic regression checker for fleet03/B07 QFORM r52.

Finite computations are regression evidence only.  The proof is the exact
A^2/Weyl/Cauchy--Binet argument in REPORT.md.
"""
import math
import numpy as np

SEED = 5207
rng = np.random.default_rng(SEED)

def sv(M):
    return np.linalg.svd(M, compute_uv=False)

def e2_gram(M):
    x = sv(M) ** 2
    return 0.5 * ((x.sum()) ** 2 - (x * x).sum())

def row_e2_marginals(M):
    z = e2_gram(M)
    m = M.shape[0]
    if z <= 1e-14:
        return z, np.zeros(m)
    G = M @ M.T
    # Sum of squared 2x2 minors containing row h equals
    # G_hh tr(G) - (G^2)_hh.
    numer = np.diag(G) * np.trace(G) - np.diag(G @ G)
    return z, numer / z

ladder_viol = 0
min_slack = [float('inf')] * 3
for _ in range(900):
    n = int(rng.integers(6, 17))
    Z = rng.normal(size=(n, n))
    Q, _ = np.linalg.qr(Z)
    lam = rng.normal(scale=2.0, size=n)
    lam[:3] = np.array([1.0, -1.3, 1.7]) * rng.choice([-1,1], size=3)
    A = Q @ np.diag(lam) @ Q.T
    U = Q[:, :3]
    m = int(rng.integers(2, n))
    I = np.sort(rng.choice(n, size=m, replace=False))
    Ic = np.setdiff1d(np.arange(n), I)
    B = A[np.ix_(I,I)]
    D = A[np.ix_(I,Ic)]
    a = np.linalg.eigvalsh(U[I,:].T @ U[I,:])[0]
    sb = np.pad(sv(B), (0, max(0,3-min(B.shape))), constant_values=0)[:3]
    sd = np.pad(sv(D), (0, max(0,3-min(D.shape))), constant_values=0)[:3]
    rhs = [max(0.0, a-sb[0]**2), max(0.0, a-sb[1]**2), max(0.0, a-sb[2]**2)]
    lhs = [sd[2]**2, sd[1]**2, sd[0]**2]
    for j in range(3):
        slack = lhs[j]-rhs[j]
        min_slack[j] = min(min_slack[j], slack)
        if slack < -2e-10:
            ladder_viol += 1

max_sum_err = 0.0
max_del_err = 0.0
for _ in range(500):
    m = int(rng.integers(3, 12)); p = int(rng.integers(2, 12))
    M = rng.normal(size=(m,p))
    z, alpha = row_e2_marginals(M)
    if z <= 1e-12: continue
    max_sum_err = max(max_sum_err, abs(alpha.sum()-2.0))
    for h in range(m):
        zm = e2_gram(np.delete(M,h,axis=0))
        max_del_err = max(max_del_err, abs(zm-z*(1-alpha[h]))/max(1.0,z))

C3 = 3 * 2**(4/3) * math.e**(1/3)
d = 1/math.sqrt(8)
print(f"seed={SEED}")
print(f"ladder_tests=900 violations={ladder_viol} min_slacks={min_slack}")
print(f"e2_tests=500 max_sum_alpha_error={max_sum_err:.3e} max_relative_deletion_error={max_del_err:.3e}")
print(f"C3={C3:.15f}")
print(f"d={d:.15f}")
print(f"C3_sqrt8={C3*math.sqrt(8):.15f}")
print(f"sqrt1023_over64={math.sqrt(1023)/64:.15f}")
print(f"mixed12_RhZ={1/(2048*895):.15e}")
print(f"mixed12_coeffZ={1/(2048*895**2):.15e}")
print(f"mixed21_starZ={1023/(1048576*895):.15e}")
assert ladder_viol == 0
assert max_sum_err < 1e-10
assert max_del_err < 1e-10
print("STATUS=PASS")
