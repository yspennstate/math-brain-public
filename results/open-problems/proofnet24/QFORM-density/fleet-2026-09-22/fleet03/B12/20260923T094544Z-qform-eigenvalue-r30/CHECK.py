import json, math
import numpy as np

SEED = 20260923094544
rng = np.random.default_rng(SEED)

def ell(r):
    return (math.sqrt(r*r + 4.0) - r) / 2.0

def kth_sv(A, j):
    sv = np.linalg.svd(A, compute_uv=False)
    return float(sv[j-1]) if j <= len(sv) else 0.0

# Random checks of s_3(H) >= mu*ell(rho)^2 - s_{k+1}(B_Q).
N = 10000
viol = 0
min_margin = float('inf')
min_ratio = float('inf')
for _ in range(N):
    top = int(rng.integers(1, 5))
    k = int(rng.integers(0, 4))
    p = 2*k + 3 + int(rng.integers(0, 4))
    q = int(rng.integers(0, 6))
    mu = float(rng.uniform(0.25, 3.0))

    signs = np.where(rng.random(p) < 0.5, -1.0, 1.0)
    mags = mu * (1.0 + rng.uniform(0.0, 5.0, size=p))
    Dp = np.diag(signs * mags)

    vals_q = rng.normal(0.0, 10.0, size=q) if q else np.empty(0)
    if q and rng.random() < 0.3:
        vals_q[int(rng.integers(0, q))] = 0.0
    Dq = np.diag(vals_q)

    C = rng.normal(size=(top, top))
    C = (C + C.T) / 2.0
    Bp = rng.normal(size=(top, p)) * rng.uniform(0.05, 3.0)
    Bq = (rng.normal(size=(top, q)) * 10.0**rng.uniform(-2.0, 3.0)
          if q else np.zeros((top, 0)))

    rho = np.linalg.norm(Bp @ np.linalg.inv(Dp), 2)
    g = mu * ell(rho)**2
    eps = kth_sv(Bq, k+1)

    H = np.block([
        [C,    Bp,                   Bq],
        [Bp.T, Dp,                   np.zeros((p, q))],
        [Bq.T, np.zeros((q, p)),     Dq],
    ])
    lhs = kth_sv(H, 3)
    rhs = g - eps
    margin = lhs - rhs
    min_margin = min(min_margin, margin)
    min_ratio = min(min_ratio, lhs/g)
    if margin < -1e-9:
        viol += 1
        break

# Explicit arbitrary-magnitude rank-two leakage family.
def explicit_s3(amp):
    top, p, q = 3, 7, 2
    C = np.array([[0.2,-0.1,0.3],[-0.1,-4.0,1.2],[0.3,1.2,7.0]])
    Dp = np.diag([2,-2,2,-2,2,-2,2])
    Dq = np.array([[1e6,-3e5],[-3e5,-1e-7]])
    Bp = np.zeros((top,p))
    Bq = amp*np.array([[1,2],[3,-1],[-4,5]], dtype=float)
    H = np.block([
        [C,    Bp,                Bq],
        [Bp.T, Dp,                np.zeros((p,q))],
        [Bq.T, np.zeros((q,p)),   Dq],
    ])
    return kth_sv(H, 3)

amps = [1e-6, 1.0, 1e3, 1e6]
explicit = {str(a): explicit_s3(a) for a in amps}

# Check s_3(B) >= s_{K+1}(BQ), used by the volume alternative.
M = 5000
cross_viol = 0
cross_min_margin = float('inf')
for _ in range(M):
    top = int(rng.integers(3, 8))
    d = int(rng.integers(7, 15))
    A = rng.normal(size=(d,d))
    O, _ = np.linalg.qr(A)
    rp = int(rng.integers(7, d+1))
    P = O[:,:rp] @ O[:,:rp].T
    Q = np.eye(d) - P
    B = rng.normal(size=(top,d))
    K = (rp - 3)//2
    eps = kth_sv(B @ Q, K+1)
    margin = kth_sv(B, 3) - eps
    cross_min_margin = min(cross_min_margin, margin)
    if margin < -1e-9:
        cross_viol += 1
        break

result = {
    'seed': SEED,
    'rank_budget_trials': N,
    'rank_budget_violations': viol,
    'rank_budget_min_margin': min_margin,
    'rank_budget_min_s3_over_g': min_ratio,
    'explicit_rank2_leakage_s3': explicit,
    'm12_density_constant_when_g2': math.sqrt(72.0*math.pi),
    'volume_branch_coefficient_48sqrt3e_over5': 48.0*math.sqrt(3.0)*math.e/5.0,
    'cross_monotonicity_trials': M,
    'cross_monotonicity_violations': cross_viol,
    'cross_monotonicity_min_margin': cross_min_margin,
}
print(json.dumps(result, indent=2, sort_keys=True))
