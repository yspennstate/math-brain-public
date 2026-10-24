try:
    import psutil; psutil.Process().nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
except Exception:
    pass
import numpy as np
rng = np.random.default_rng(7)
def randframe(n, r):
    Q,_ = np.linalg.qr(rng.standard_normal((n, r))); return Q
# (1) discriminant matrix N = alpha alpha^T - a B for coordinate j of A = R M R^T (rank r)
worst = {}
for trial in range(2000):
    r = rng.integers(1, 5); n = rng.integers(r+2, 12)
    R = randframe(n, r); M = rng.standard_normal((r, r)); M = M + M.T
    if trial % 3 == 0:   # make coordinate 0 heavy by mixing e_0 into the frame
        R[:, 0] = 0.9*np.eye(n)[:,0] + 0.1*R[:,0]; R,_ = np.linalg.qr(R)
    A = R @ M @ R.T; j = 0
    a = A[j, j]; alpha = np.delete(A[:, j], j); B = np.delete(np.delete(A, j, 0), j, 1)
    N = np.outer(alpha, alpha) - a*B
    ev = np.linalg.eigvalsh(N); ev = ev[np.abs(ev) > 1e-9*max(1, np.abs(ev).max())]
    lj = R[j] @ R[j]
    lam = np.linalg.eigvalsh(M)
    if r == 2:
        err = abs(ev.sum() - (-np.linalg.det(M)*lj)) if len(ev) else abs(-np.linalg.det(M)*lj)
        worst['r2 trace=-detM*l'] = max(worst.get('r2 trace=-detM*l',0), err)
        worst['r2 rank<=1'] = max(worst.get('r2 rank<=1',0), max(0, len(ev)-1))
    if r == 3:
        # rotate so rho_j = sqrt(l) e_3 : build orthonormal O with last column rho_j/|rho_j|
        rho = R[j]; u = rho/np.linalg.norm(rho)
        O,_ = np.linalg.qr(np.column_stack([rng.standard_normal((3,2)), u]))
        O[:, 2] = u if O[:,2] @ u > 0 else -u
        O,_ = np.linalg.qr(O); 
        if O[:,2] @ u < 0: O[:,2] *= -1
        Mr = O.T @ M @ O
        c = Mr[:2, 2]; P = Mr[:2,:2]
        pred_det = lj * a * np.linalg.det(M)
        pred_tr = lj * (c @ c - Mr[2,2]*np.trace(P))
        if len(ev) == 2:
            worst['r3 det'] = max(worst.get('r3 det',0), abs(np.prod(ev) - pred_det)/(1+abs(pred_det)))
            worst['r3 tr'] = max(worst.get('r3 tr',0), abs(ev.sum() - pred_tr)/(1+abs(pred_tr)))
        worst['r3 a=l*M33'] = max(worst.get('r3 a=l*M33',0), abs(a - lj*Mr[2,2]))
print('discriminant identities, max errors:', worst, flush=True)
# (2) (M^{-1})_{33} = -p'/(kappa^2) at M_33 = 0, with M = [[p,q,k],[q,s,0],[k,0,0]], p' = p - q^2/s
e = 0
for _ in range(1000):
    p,q,s,k = rng.standard_normal(4)*3
    M = np.array([[p,q,k],[q,s,0],[k,0,0.]])
    if abs(np.linalg.det(M)) < 1e-6: continue
    e = max(e, abs(np.linalg.inv(M)[2,2] - (-(p - q*q/s)/k**2)))
    e = max(e, abs(np.linalg.inv(M)[1,1] - 1/s))
print('(M^-1)_33 = -p\'/k^2 and (M^-1)_22 = 1/s at M_33=0: max err', e, flush=True)
# (3) interlacing: principal k-block of an r x r M with norm < 1 and all |eig(M)| >= 1 forces 2k <= r
viol = 0
for _ in range(20000):
    r = rng.integers(2, 7); k = rng.integers(1, r+1)
    # random M with a small principal k-block: M = [[S, C],[C^T, T]], ||S|| < 1
    S = rng.standard_normal((k,k)); S = (S+S.T); S *= 0.9*rng.random()/max(1e-9, np.abs(np.linalg.eigvalsh(S)).max())
    C = rng.standard_normal((k, r-k))*rng.exponential(3)
    T = rng.standard_normal((r-k, r-k))*rng.exponential(3); T = T + T.T
    M = np.block([[S, C],[C.T, T]])
    ev = np.linalg.eigvalsh(M)
    if np.all(np.abs(ev) >= 1) and 2*k > r: viol += 1
print('interlacing violations (should be 0):', viol, flush=True)
