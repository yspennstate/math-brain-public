# Independent check: top Lyapunov exponent of dX/dt = A_{I_t} X, I_t flips 0<->1 at rate r.
# Angle theta in [0,pi), upwind finite-volume CTMC on (state, cell); lambda = E_pi[u^T A_i u].
import numpy as np, scipy.sparse as sp, scipy.sparse.linalg as sla, sys
A = [np.array([[-0.75,-1.0],[1.0,-0.75]]), np.diag([1.25,-2.75])]
def lam(r, N):
    h = np.pi/N; th = (np.arange(N)+0.5)*h
    c, s = np.cos(th), np.sin(th)
    rows, cols, vals = [], [], []
    f = []
    for i, M in enumerate(A):
        # theta' = u_perp^T M u, radial = u^T M u, u=(c,s), u_perp=(-s,c)
        v = -s*(M[0,0]*c+M[0,1]*s) + c*(M[1,0]*c+M[1,1]*s)
        f.append(c*(M[0,0]*c+M[0,1]*s) + s*(M[1,0]*c+M[1,1]*s))
        # face velocities at k+1/2 for upwind: use velocity at face
        tf = (np.arange(N)+1.0)*h; cf, sf = np.cos(tf), np.sin(tf)
        vf = -sf*(M[0,0]*cf+M[0,1]*sf) + cf*(M[1,0]*cf+M[1,1]*sf)
        k = np.arange(N); kp = (k+1) % N
        up = np.maximum(vf,0)/h; dn = np.maximum(-vf,0)/h
        # k -> k+1 at rate up[k]; k+1 -> k at rate dn[k]
        rows += list(i*N+k); cols += list(i*N+kp); vals += list(up)
        rows += list(i*N+kp); cols += list(i*N+k); vals += list(dn)
        rows += list(i*N+k); cols += list((1-i)*N+k); vals += [r]*N
    Q = sp.csr_matrix((vals,(rows,cols)), shape=(2*N,2*N))
    Q = Q - sp.diags(np.asarray(Q.sum(axis=1)).ravel())
    QT = Q.T.tocoo(); m = QT.row != 0; QT = sp.coo_matrix((np.r_[QT.data[m], np.ones(2*N)], (np.r_[QT.row[m], np.zeros(2*N,int)], np.r_[QT.col[m], np.arange(2*N)])), shape=(2*N,2*N)); b = np.zeros(2*N); b[0] = 1.0
    p = sla.spsolve(QT.tocsc(), b)
    return float(p[:N]@f[0] + p[N:]@f[1])
for r in [1.0, 2.0, 5.0, 10.0, 20.0, 100.0]:
    print(r, ["%.5f" % lam(r, N) for N in (2000, 8000)], flush=True)
