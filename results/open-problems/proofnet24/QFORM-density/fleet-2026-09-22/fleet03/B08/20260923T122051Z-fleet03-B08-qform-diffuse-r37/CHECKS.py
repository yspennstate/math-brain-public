import math
import numpy as np


def C(h, r):
    d = 2*h + r
    assert d > 2
    return 4*d/(d-2) * 2**(-2*h/d)

print('C_11', C(1,1))
print('C_12', C(1,2))
print('C_20', C(2,0))
print('C_30', C(3,0))
partner = (2**(4/3)+1)*math.sqrt(3)*2**(1/4)
print('partner', partner)

assert abs(C(1,1) - 3*4**(2/3)) < 1e-13
assert abs(C(1,2) - 4*math.sqrt(2)) < 1e-13
assert abs(C(2,0) - 4) < 1e-13
assert abs(C(3,0) - 3) < 1e-13
assert partner < 7.251

# Seeded regression of the exact shear/leverage identity.
rng = np.random.default_rng(20260923)
max_lev_err = 0.0
max_det_rel_err = 0.0
ntests = 0
for r in [0,1,2,3]:
    for h in [1,2,3]:
        m = h + r + 5
        for _ in range(100):
            if r:
                Z = rng.normal(size=(m,r))
                S, _ = np.linalg.qr(Z)
                S = S[:, :r]
            else:
                S = np.zeros((m,0))
            Cmat = rng.normal(size=(m,h))
            Cperp = Cmat - S @ (S.T @ Cmat)
            G = Cperp.T @ Cperp
            if np.linalg.eigvalsh(G).min() < 1e-9:
                continue
            A = S.T @ Cmat
            Gamma = np.block([
                [Cmat.T @ Cmat, Cmat.T @ S],
                [S.T @ Cmat, np.eye(r)]
            ]) if r else Cmat.T @ Cmat
            invGamma = np.linalg.inv(Gamma)
            invG = np.linalg.inv(G)
            for i in range(m):
                w = np.r_[Cmat[i], S[i]]
                lev1 = float(w @ invGamma @ w)
                lev2 = float(Cperp[i] @ invG @ Cperp[i] + S[i] @ S[i])
                max_lev_err = max(max_lev_err, abs(lev1-lev2))
            det1 = float(np.linalg.det(Gamma))
            det2 = float(np.linalg.det(G))
            max_det_rel_err = max(max_det_rel_err, abs(det1-det2)/max(1.0,abs(det2)))
            ntests += 1

print('identity_tests', ntests)
print('max_leverage_error', max_lev_err)
print('max_det_relative_error', max_det_rel_err)
assert max_lev_err < 1e-10
assert max_det_rel_err < 1e-10

# Explicit anisotropic m-arm family.  C has m copies of each arm coefficient.
for m in [2,3,8,32]:
    for R in [3.0,10.0,1000.0]:
        L0 = 1.7
        Cmat = np.zeros((2*m,2))
        Cmat[:m,0] = L0*R/math.sqrt(m)
        Cmat[m:,1] = L0/R/math.sqrt(m)
        G = Cmat.T @ Cmat
        detG = float(np.linalg.det(G))
        lev = np.einsum('ij,jk,ik->i', Cmat, np.linalg.inv(G), Cmat)
        assert abs(detG-L0**4) < 1e-8 * max(1.0,L0**4)
        assert np.max(np.abs(lev-1/m)) < 1e-12
        s = np.linalg.svd(Cmat, compute_uv=False)
        assert abs(s[0]*s[1]-L0**2) < 1e-10
print('anisotropic_family_checks PASS')
print('QFORM_B08_R37_CHECK_PASS')
