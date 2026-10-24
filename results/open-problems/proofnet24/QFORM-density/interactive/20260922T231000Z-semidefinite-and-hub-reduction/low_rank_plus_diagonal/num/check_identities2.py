try:
    import psutil; psutil.Process().nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
except Exception:
    pass
import numpy as np
rng = np.random.default_rng(8)
def randframe(n, r):
    Q,_ = np.linalg.qr(rng.standard_normal((n, r))); return Q
def basis_with_last(u):
    G = np.column_stack([u, rng.standard_normal((3,2))]); Q,_ = np.linalg.qr(G)
    if Q[:,0] @ u < 0: Q[:,0] *= -1
    return np.column_stack([Q[:,1], Q[:,2], Q[:,0]])
w = {}
for trial in range(3000):
    n = rng.integers(5, 12); R = randframe(n, 3)
    if trial % 2 == 0:
        R[:,0] = 0.95*np.eye(n)[:,0] + 0.05*R[:,0]; R,_ = np.linalg.qr(R)
    M = rng.standard_normal((3,3))*3; M = M + M.T
    A = R @ M @ R.T; j = 0
    a = A[j,j]; alpha = np.delete(A[:,j], j); B = np.delete(np.delete(A,j,0),j,1)
    N = np.outer(alpha, alpha) - a*B
    ev = np.linalg.eigvalsh(N); ev = ev[np.abs(ev) > 1e-9*max(1,np.abs(ev).max())]
    rho = R[j]; lj = rho @ rho; u = rho/np.sqrt(lj)
    O = basis_with_last(u); Mr = O.T @ M @ O
    c = Mr[:2,2]; P = Mr[:2,:2]
    w['a=l*M33'] = max(w.get('a=l*M33',0), abs(a - lj*Mr[2,2]))
    if len(ev) == 2:
        w['det'] = max(w.get('det',0), abs(np.prod(ev) - lj*a*np.linalg.det(M))/(1+abs(lj*a*np.linalg.det(M))))
        w['tr'] = max(w.get('tr',0), abs(ev.sum() - lj*(c@c - Mr[2,2]*np.trace(P)))/(1+abs(ev.sum())))
    # also check: rows of R in the rotated frame vanish at j in coords 1,2
    Rr = R @ O
    w['rot rows'] = max(w.get('rot rows',0), abs(Rr[j,0]) + abs(Rr[j,1]))
print(w, flush=True)
