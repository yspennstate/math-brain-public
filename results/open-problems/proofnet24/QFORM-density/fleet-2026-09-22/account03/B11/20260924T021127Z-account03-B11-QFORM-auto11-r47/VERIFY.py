import math
import numpy as np

Q0 = 63/64
DELTA0 = 1/8
M0 = 1/4
PAIR_CONST = 128*math.sqrt(2)/math.sqrt(Q0*DELTA0)

rng = np.random.default_rng(20260924021127)
max_T_error = 0.0
max_rank_tail = 0.0
max_sparse_forbidden = 0.0
max_sigma_error = 0.0
max_lambda_error = 0.0
min_partial_eig = 1.0
max_partial_eig = 0.0
max_partner_ratio = 0.0
frames_checked = 0
attempts = 0

while frames_checked < 120 and attempts < 2000:
    attempts += 1
    n = 1200
    X = rng.normal(size=(n, 3))
    Q, _ = np.linalg.qr(X)
    t, y, z = Q[:, 0], Q[:, 1], Q[:, 2]
    rho = y*y + z*z
    if rho.max() >= DELTA0:
        continue

    kappa, d, e, c = 1.7, 0.4, -0.3, 1.2
    M = np.array([[0.0, kappa, 0.0],
                  [kappa, d, e],
                  [0.0, e, c]])
    eigM = np.linalg.eigvalsh(M)
    assert eigM[0] < 0 < eigM[1]

    q = Q0
    U = np.column_stack([math.sqrt(1-q)*t, y, z])
    ri = np.array([math.sqrt(q), 0.0, 0.0])
    assert np.linalg.norm(U.T @ U + np.outer(ri,ri) - np.eye(3)) < 1e-12

    # Find one partition satisfying the deterministic paving conclusion.
    S = np.column_stack([y,z])
    mask = None
    GL = None
    for _ in range(5000):
        m = rng.random(n) < 0.5
        G = S[m].T @ S[m]
        ev = np.linalg.eigvalsh(G)
        if ev[0] >= M0 and ev[1] <= 1-M0:
            mask, GL = m, G
            break
    assert mask is not None
    GR = np.eye(2) - GL
    evL = np.linalg.eigvalsh(GL)
    evR = np.linalg.eigvalsh(GR)
    min_partial_eig = min(min_partial_eig, evL[0], evR[0])
    max_partial_eig = max(max_partial_eig, evL[1], evR[1])

    L = np.where(mask)[0]
    R = np.where(~mask)[0]
    cL = U[L] @ M @ ri
    rR = ri @ M @ U[R].T
    N = U[L] @ M @ U[R].T

    def pperp(v):
        return np.eye(v.size) - np.outer(v,v)/(v@v)

    C = pperp(cL) @ N @ pperp(rR)
    sv = np.linalg.svd(C, compute_uv=False)
    max_rank_tail = max(max_rank_tail, float(sv[1] if len(sv)>1 else 0.0))

    DL = float(np.linalg.det(GL))
    DR = float(np.linalg.det(GR))
    Tgeom = float((cL@cL)*(rR@rR)*(np.linalg.norm(C,'fro')**2))
    rhs = float(q*q*(np.linalg.det(M)**2)*DL*DR)
    max_T_error = max(max_T_error, abs(Tgeom-rhs))

    # Sparse 3x3 bank crossing and exact one-sided puncture coefficients.
    yL,yR = y[L],y[R]
    zL,zR = z[L],z[R]
    tL,tR = t[L],t[R]
    eL = yL/np.linalg.norm(yL)
    eR = yR/np.linalg.norm(yR)
    zpL = zL-(eL@zL)*eL
    zpR = zR-(eR@zR)*eR
    vL = zpL/np.linalg.norm(zpL)
    vR = zpR/np.linalg.norm(zpR)
    tauL = tL-(eL@tL)*eL-(vL@tL)*vL
    tauR = tR-(eR@tR)*eR-(vR@tR)*vR
    if np.linalg.norm(tauL)>1e-12 and np.linalg.norm(tauR)>1e-12:
        wL = tauL/np.linalg.norm(tauL)
        wR = tauR/np.linalg.norm(tauR)
        BL = np.column_stack([eL,vL,wL])
        BR = np.column_stack([eR,vR,wR])
        B = BL.T @ N @ BR
        forbidden = max(abs(B[1,2]),abs(B[2,1]),abs(B[2,2]))
        max_sparse_forbidden = max(max_sparse_forbidden, forbidden)
        sigma_pred = c*np.linalg.norm(zpL)*np.linalg.norm(zpR)
        lamR_pred = kappa*math.sqrt(1-q)*np.linalg.norm(yL)*np.linalg.norm(tauR)
        lamL_pred = kappa*math.sqrt(1-q)*np.linalg.norm(yR)*np.linalg.norm(tauL)
        max_sigma_error = max(max_sigma_error, abs(B[1,1]-sigma_pred))
        max_lambda_error = max(max_lambda_error,
                               abs(B[0,2]-lamR_pred),
                               abs(B[2,0]-lamL_pred))
        # Determinant-one shears clear star--transverse entries without touching punctures.
        a = B[0,1]/B[1,1]
        b = B[1,0]/B[1,1]
        SL = np.eye(3); SL[1,0] = -a
        SR = np.eye(3); SR[1,0] = -b
        Bp = SL.T @ B @ SR
        max_sparse_forbidden = max(max_sparse_forbidden,
                                   abs(Bp[0,1]),abs(Bp[1,0]),
                                   abs(Bp[1,2]),abs(Bp[2,1]),abs(Bp[2,2]))

    # Direct account04/B11 extension-mass ratio for a random leaf.
    j = int(rng.integers(0,n))
    uj = np.array([y[j],z[j]])
    denom = float(uj@uj)
    if denom > 1e-14:
        ratios=[]
        for k in range(n):
            cross = y[j]*z[k]-z[j]*y[k]
            ratios.append((cross*cross)/denom)
        max_partner_ratio = max(max_partner_ratio, max(ratios))
        assert max(ratios) <= float(rho.max()) + 1e-12

    # Deterministic second-moment estimate behind the paving lemma.
    lhs = 0.25*float(np.sum(rho*rho))
    assert lhs <= DELTA0/2 + 1e-12

    frames_checked += 1

assert frames_checked == 120
assert max_T_error < 1e-10
assert max_rank_tail < 1e-10
assert max_sparse_forbidden < 1e-10
assert max_sigma_error < 1e-10
assert max_lambda_error < 1e-10
assert PAIR_CONST < 517
assert max_partner_ratio <= DELTA0 + 1e-12

print(f'frames_checked={frames_checked}')
print(f'attempts={attempts}')
print(f'max_Tgeom_identity_abs_error={max_T_error:.3e}')
print(f'max_effective_crossing_second_singular={max_rank_tail:.3e}')
print(f'max_sparse_forbidden_entry={max_sparse_forbidden:.3e}')
print(f'max_sigma_formula_error={max_sigma_error:.3e}')
print(f'max_lambda_formula_error={max_lambda_error:.3e}')
print(f'min_observed_partial_gram_eigenvalue={min_partial_eig:.12f}')
print(f'max_observed_partial_gram_eigenvalue={max_partial_eig:.12f}')
print(f'max_observed_extension_ratio={max_partner_ratio:.12f}')
print(f'delta0={DELTA0:.12f}')
print(f'm0={M0:.12f}')
print(f'paid_pair_constant={PAIR_CONST:.12f}')
print('QFORM_B11_R47_SPARSE_CROSSING_CHECK_PASS')
