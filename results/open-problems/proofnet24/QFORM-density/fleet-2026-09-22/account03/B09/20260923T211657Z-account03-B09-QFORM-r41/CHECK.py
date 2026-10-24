import math
import numpy as np

C_LOCAL = 5*6**(3/5)*2**(-13/10)
C_GROUP = 5*6**(3/5)*2**(-9/10)
print(f"C_LOCAL={C_LOCAL:.15f}")
print(f"C_GROUP={C_GROUP:.15f}")


def stress(m):
    P = np.array([[0.,0.,1.],[0.,0.,0.],[1.,0.,0.]])
    C = np.zeros((3,m))
    C[0,:m//2] = math.sqrt(2/m)
    C[1,m//2:] = math.sqrt(2/m)
    A = np.block([[P,C],[C.T,np.zeros((m,m))]])
    ev = np.linalg.eigvalsh(A)
    sv = np.linalg.svd(C,compute_uv=False)
    Delta = sv[0]*sv[1]
    n = np.array([0.,0.,1.])
    a = P@n
    V1 = 0.0
    currencies = []
    for r in range(m):
        for s in range(r+1,m):
            w = np.cross(C[:,r],C[:,s])
            V1 += np.linalg.norm(P@w)**2
            if np.linalg.norm(w)>1e-14:
                currencies.append(np.linalg.norm(w)*np.linalg.norm(P@w))
    return ev, Delta, np.linalg.norm(a), V1, max(currencies)

for m in [8,32,128]:
    ev, Delta, anorm, V1, cur = stress(m)
    nz = ev[np.abs(ev)>1e-9]
    local = C_LOCAL*cur**(-1/5)
    print(f"stress m={m}: nonzero_eigs={np.array2string(nz,precision=9)}, Delta={Delta:.15f}, ||Pn||={anorm:.15f}, V1={V1:.15f}, max_packet_currency={cur:.15f}, best_single_packet_bound={local:.12f}, grouped_bound={C_GROUP:.12f}")

rng = np.random.default_rng(20260923)
errs = []
orthoerrs = []
for _ in range(100):
    M = rng.normal(size=(3,3))
    Q,_ = np.linalg.qr(M)
    n = Q[:,0]
    E = Q[:,1:]
    m = int(rng.integers(3,10))
    B = rng.normal(size=(2,m))
    while np.linalg.matrix_rank(B)<2:
        B = rng.normal(size=(2,m))
    C = E@B
    P0 = rng.normal(size=(3,3))
    P = (P0+P0.T)/2
    sv = np.linalg.svd(C,compute_uv=False)
    Delta = sv[0]*sv[1]
    V1 = 0.0
    for r in range(m):
        for s in range(r+1,m):
            w = np.cross(C[:,r],C[:,s])
            V1 += np.linalg.norm(P@w)**2
    rhs = Delta**2*np.linalg.norm(P@n)**2
    errs.append(abs(V1-rhs)/max(1.0,abs(rhs)))

    BB = E.T@C
    lam,U = np.linalg.eigh(BB@BB.T)
    L0 = U@np.diag(np.sqrt(lam))@U.T
    R = BB.T@np.linalg.inv(L0)
    orthoerrs.append(np.linalg.norm(R.T@R-np.eye(2)))

print(f"100_random_tests: max_V1_identity_relative_error={max(errs):.3e}, max_R_orthonormality_error={max(orthoerrs):.3e}")

Apart = np.block([[np.zeros((3,3)),np.eye(3)],[np.eye(3),np.zeros((3,3))]])
print(f"partner_regression: eigenvalues={np.array2string(np.linalg.eigvalsh(Apart),precision=3)}, det_cross={np.linalg.det(np.eye(3)):.1f}, partner_bound=3.000000000000")
