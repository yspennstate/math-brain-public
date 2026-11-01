import math
import numpy as np

SEED = 2026092410
TRIALS = 1000
rng = np.random.default_rng(SEED)

g = 0.5 - 1.0/(4.0*math.sqrt(2.0))
mu = 1.0/16.0
alpha = mu*(1.0-g)/g
analytic_leverage_ceiling = mu + (math.sqrt(alpha)+0.25)**2
m0 = math.sqrt(47.0/48.0)
eta = 2.0**-20
beta0 = 4.0*math.sqrt(2.0)*eta
s_exact = g*m0
C_cross = 6.0**(4.0/3.0)*s_exact**(-2.0/3.0)*eta**(-1.0/3.0)
C_schur = 4.0*math.sqrt(6.0)*((1.0/64.0)*beta0*m0)**(-1.0/3.0)

max_py = 0.0
max_orth = 0.0
max_rw = 0.0
max_det_rel = 0.0
max_leverage = 0.0
accepted = 0

while accepted < TRIALS:
    m = 240
    Z = rng.normal(size=(m,2))
    V, _ = np.linalg.qr(Z)
    rowlev = np.sum(V*V,axis=1)
    if rowlev.max() > mu:
        continue

    cut = None
    for _ in range(50):
        mask = rng.random(m) < 0.5
        G = V[mask].T @ V[mask]
        H = np.eye(2)-G
        if min(np.linalg.eigvalsh(G).min(),np.linalg.eigvalsh(H).min()) >= g:
            cut = mask
            break
    if cut is None:
        continue
    mask = cut

    delta = rng.normal(size=2)
    w = np.zeros(m)
    w[mask] = V[mask] @ (H @ delta)
    w[~mask] = -V[~mask] @ (G @ delta)
    wnorm = np.linalg.norm(w)
    if wnorm == 0:
        continue

    r = np.zeros(m)
    for idx, sub in ((mask,V[mask]),(~mask,V[~mask])):
        z = rng.normal(size=idx.sum())
        z -= sub @ np.linalg.solve(sub.T@sub,sub.T@z)
        r[idx] = z
    r *= (0.15*wnorm/np.linalg.norm(r))

    u = r+w
    beta = np.linalg.norm(u)
    e = np.linalg.norm(r)
    if not beta > 4.0*e:
        continue

    max_py = max(max_py,abs(beta**2-(e**2+delta@(G@H)@delta)))
    max_orth = max(max_orth,np.linalg.norm(V.T@w),np.linalg.norm(V.T@r),np.linalg.norm(V.T@u))
    max_rw = max(max_rw,abs(r@w))
    max_leverage = max(max_leverage,np.max(rowlev+(u*u)/(beta*beta)))

    Lam = np.diag([
        rng.choice([-1.0,1.0])*(0.5+3.0*rng.random()),
        rng.choice([-1.0,1.0])*(0.5+3.0*rng.random())
    ])
    c = rng.normal(size=2)
    a = rng.choice([-1.0,1.0])*(0.5+3.0*rng.random())
    q = np.r_[c,beta]
    D = np.zeros((3,3)); D[:2,:2] = Lam
    M = D - np.outer(q,q)/a
    lhs = np.linalg.det(M)
    rhs = -(beta*beta/a)*np.linalg.det(Lam)
    max_det_rel = max(max_det_rel,abs(lhs-rhs)/max(1.0,abs(rhs)))
    accepted += 1

print('QFORM_B08_R52_CHECK_PASS')
print('seed',SEED)
print('trials',accepted)
print('max_pythagoras_error',repr(max_py))
print('max_orthogonality_norm',repr(max_orth))
print('max_abs_r_dot_w',repr(max_rw))
print('max_schur_det_relative_error',repr(max_det_rel))
print('max_sampled_threeframe_row_leverage',repr(max_leverage))
print('analytic_threeframe_leverage_ceiling',repr(analytic_leverage_ceiling))
print('g',repr(g))
print('alpha',repr(alpha))
print('m0',repr(m0))
print('exact_crossing_scale',repr(s_exact))
print('eta',repr(eta))
print('beta0',repr(beta0))
print('C_cross',repr(C_cross))
print('C_schur',repr(C_schur))
