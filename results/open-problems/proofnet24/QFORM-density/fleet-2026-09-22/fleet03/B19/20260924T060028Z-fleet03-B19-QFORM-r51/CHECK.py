import math
import numpy as np

rng = np.random.default_rng(260925)
tau = 2.0**-16
s_gate = 1.0/64.0
eta = 2.0/7.0
g = 4.0/7.0
T = 6000

robust = fail_r = fail_c = violations = 0
min_robust_ratio = float('inf')
min_star_ratio = float('inf')
max_normalized_light_leverage = 0.0
max_heavy_r = max_heavy_c = 0

for _ in range(T):
    m = int(rng.integers(6, 55))
    n = int(rng.integers(6, 55))
    Qr, _ = np.linalg.qr(rng.normal(size=(m, m)))
    Qc, _ = np.linalg.qr(rng.normal(size=(n, n)))
    s2 = s_gate + float(rng.random())*0.12
    s1 = s2 + float(rng.random())*0.25
    r = min(m, n)
    sing = np.zeros(r)
    sing[:2] = [s1, s2]
    if r > 2:
        tv = rng.random(r-2)
        tv = tv/np.linalg.norm(tv)*(tau*float(rng.uniform(0.05, 0.999)))
        sing[2:] = np.sort(tv)[::-1]

    N = Qr[:, :r] @ np.diag(sing) @ Qc[:, :r].T
    U = Qr[:, :2]
    V = Qc[:, :2]
    N2 = U @ np.diag([s1, s2]) @ V.T
    tail = np.linalg.norm(N-N2, 'fro')

    lev_r = np.sum(U*U, axis=1)
    lev_c = np.sum(V*V, axis=1)
    HR = np.where(lev_r > eta)[0]
    HC = np.where(lev_c > eta)[0]
    max_heavy_r = max(max_heavy_r, len(HR))
    max_heavy_c = max(max_heavy_c, len(HC))
    HRset, HCset = set(HR), set(HC)
    LR = np.array([i for i in range(m) if i not in HRset], dtype=int)
    LC = np.array([j for j in range(n) if j not in HCset], dtype=int)

    GR = U[LR].T @ U[LR]
    GC = V[LC].T @ V[LC]
    lr = np.linalg.eigvalsh(GR)[0] if len(LR) else 0.0
    lc = np.linalg.eigvalsh(GC)[0] if len(LC) else 0.0

    if lr >= g and lc >= g:
        robust += 1
        M = N[np.ix_(LR, LC)]
        actual = np.linalg.svd(M, compute_uv=False)[1]
        claimed_instance = s2*math.sqrt(lr*lc) - tail
        if actual + 1e-12 < claimed_instance:
            violations += 1
        min_robust_ratio = min(min_robust_ratio, actual/claimed_instance)

        invR = np.linalg.inv(GR)
        invC = np.linalg.inv(GC)
        whitened_r = np.einsum('ij,jk,ik->i', U[LR], invR, U[LR])
        whitened_c = np.einsum('ij,jk,ik->i', V[LC], invC, V[LC])
        observed = max(whitened_r.max(initial=0.0), whitened_c.max(initial=0.0))
        max_normalized_light_leverage = max(max_normalized_light_leverage, float(observed))
        if observed > 0.5 + 1e-10:
            violations += 1
    else:
        if lr < g:
            fail_r += 1
            actual = np.linalg.norm(N[HR, :], axis=1).max()
            claimed_instance = s2*math.sqrt((1.0-lr)/len(HR)) - tail
            if actual + 1e-12 < claimed_instance:
                violations += 1
            min_star_ratio = min(min_star_ratio, actual/claimed_instance)
        if lc < g:
            fail_c += 1
            actual = np.linalg.norm(N[:, HC], axis=0).max()
            claimed_instance = s2*math.sqrt((1.0-lc)/len(HC)) - tail
            if actual + 1e-12 < claimed_instance:
                violations += 1
            min_star_ratio = min(min_star_ratio, actual/claimed_instance)

print('tests', T)
print('robust', robust)
print('R-failure tests', fail_r)
print('C-failure tests', fail_c)
print('violations', violations)
print('max heavy R', max_heavy_r)
print('max heavy C', max_heavy_c)
print('min robust actual/instance-bound ratio', min_robust_ratio)
print('min star actual/instance-bound ratio', min_star_ratio)
print('max normalized light leverage', max_normalized_light_leverage)
print('universal robust sigma2 lower', 4.0/(7.0*64.0)-tau)
print('universal star lower', 1.0/(64.0*math.sqrt(14.0))-tau)
print('QFORM_B19_R51_BL_COMPATIBLE_PEEL_CHECK_PASS' if violations == 0 else 'FAIL')
