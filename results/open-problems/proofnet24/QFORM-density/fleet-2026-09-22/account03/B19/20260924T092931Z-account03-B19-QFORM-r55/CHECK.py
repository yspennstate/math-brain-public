import numpy as np

SEED = 20260924092931
TAU = 2.0**-16
SIGMA = 4089.0/458752.0
THETA = TAU/SIGMA
rng = np.random.default_rng(SEED)


def frame(m, r=2):
    q, _ = np.linalg.qr(rng.normal(size=(m, r)))
    return q[:, :r]


def e3(B):
    s = np.linalg.svd(B, compute_uv=False)
    x = s*s
    ans = 0.0
    for i in range(len(x)):
        for j in range(i+1, len(x)):
            for k in range(j+1, len(x)):
                ans += x[i]*x[j]*x[k]
    return ans


accepted = 0
lev_viol = 0
e3_viol = 0
min_ratio = float('inf')
max_lev_excess = -float('inf')
max_projection_distance = 0.0

for _ in range(2500):
    m, n = 20, 19
    U0 = frame(m)
    V0 = frame(n)
    if np.max(np.sum(U0*U0, axis=1)) > 0.5:
        continue
    if np.max(np.sum(V0*V0, axis=1)) > 0.5:
        continue

    s2 = 1.0/112.0 + rng.random()*0.015
    s1 = s2 + rng.random()*0.03
    M0 = U0 @ np.diag([s1, s2]) @ V0.T

    F = rng.normal(size=(m, n))
    op = np.linalg.svd(F, compute_uv=False)[0]
    F *= rng.uniform(0.0, 0.999)*TAU/op
    M = M0 + F

    Uh, sh, _ = np.linalg.svd(M, full_matrices=False)
    U2 = Uh[:, :2]
    P0 = U0 @ U0.T
    P = U2 @ U2.T
    pdist = np.linalg.norm(P-P0, 2)
    max_projection_distance = max(max_projection_distance, pdist)

    maxlev = np.max(np.diag(P))
    excess = maxlev - (0.5 + THETA)
    max_lev_excess = max(max_lev_excess, excess)
    if excess > 1e-10:
        lev_viol += 1

    X = rng.normal(size=(m, m))
    D = (X + X.T)/2.0
    for j in rng.choice(m, 3, replace=False):
        keep = np.arange(m) != j
        d = D[keep, j]
        Us = U2[keep, :]
        coeff = np.linalg.lstsq(Us, d, rcond=None)[0]
        rho = np.linalg.norm(d - Us @ coeff)
        B = np.column_stack([M[keep, :], d])
        E3 = e3(B)
        ell = np.sum(U2[j, :]**2)
        rhs = (sh[0]*sh[1])**2 * (1.0-ell) * rho**2
        if rhs > 1e-25:
            ratio = E3/rhs
            min_ratio = min(min_ratio, ratio)
            if E3 < rhs*(1.0-1e-8):
                e3_viol += 1

    accepted += 1

print('QFORM_B19_R55_CHECK_PASS' if lev_viol == 0 and e3_viol == 0 else 'QFORM_B19_R55_CHECK_FAIL')
print('accepted_instances', accepted)
print('deleted_columns_tested', 3*accepted)
print('leverage_bound_violations', lev_viol)
print('E3_bound_violations', e3_viol)
print('minimum_E3_over_exact_contribution', min_ratio)
print('maximum_actual_plane_leverage_excess_over_bound', max_lev_excess)
print('maximum_projection_distance', max_projection_distance)
print('theoretical_theta', THETA)
