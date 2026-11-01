"""E0018 (Malrieu, Open question 3): can the instability set in the jump rate r be a union of several intervals?
Planar switched system x' = A_{I_t} x, I_t two-state, symmetric rate r.  Write A_i = -a_i I + B_i, B_i traceless.
The angular process depends only on B_i, so L(r) = G(r) - (a_0+a_1)/2 with G the exponent of the traceless pair.
Question <=> can G(r) have two humps separated by a dip?  G via the stationary law of (theta, I) on [0,pi)x{0,1},
computed by an upwind finite-volume discretisation of the generator (sparse null vector)."""
import numpy as np, scipy.sparse as sp, scipy.sparse.linalg as spl, sys, time
def angular(B, th):
    (a11,a12),(a21,a22) = B
    c, s = np.cos(th), np.sin(th)
    f = a21*c*c - a12*s*s + (a22-a11)*s*c          # theta'
    g = a11*c*c + a22*s*s + (a12+a21)*s*c          # radial growth <B u,u>
    return f, g
def G_of_r(B0, B1, r, N=600):
    h = np.pi/N; edges = np.arange(N+1)*h; cent = edges[:-1] + h/2
    rows=[]; cols=[]; vals=[]
    def add(i,j,v): rows.append(i); cols.append(j); vals.append(v)
    for i,B in enumerate((B0,B1)):
        fe,_ = angular(B, edges[:-1])              # velocity at left edge of each cell
        for j in range(N):
            k = i*N + j
            fl = fe[j]; fr = fe[(j+1)%N]           # left / right edge velocities
            # right edge: if fr>0 mass flows j -> j+1 at rate fr/h ; if fr<0 flows j+1 -> j
            if fr > 0: add(k, i*N+(j+1)%N, fr/h)
            if fl < 0: add(k, i*N+(j-1)%N, -fl/h)
            add(k, (1-i)*N + j, r)
    Q = sp.csr_matrix((vals,(rows,cols)), shape=(2*N,2*N))
    d = np.asarray(Q.sum(axis=1)).ravel()
    Q = Q - sp.diags(d)
    # stationary p: p Q = 0, sum p = 1  -> solve Q^T p = 0 with one row replaced
    A = Q.T.tolil(); A[0,:] = 1.0; b = np.zeros(2*N); b[0] = 1.0
    p = spl.spsolve(A.tocsr(), b)
    G = 0.0
    for i,B in enumerate((B0,B1)):
        _, g = angular(B, cent); G += p[i*N:(i+1)*N] @ g
    return G
if __name__ == "__main__":
    # validation on the survey's example (nilpotent pair): G peaks ~0.2 near r ~ 4.6, G -> 0 at both ends
    B0 = np.array([[0.,1.],[0.,0.]]); B1 = np.array([[0.,0.],[-1.,0.]])
    for r in [0.5, 1, 2, 3, 4, 4.6, 5, 6, 8, 12, 20, 50]:
        print(f"r={r:5.1f}  G={G_of_r(B0,B1,r):.4f}   (N=600)   N=2400: {G_of_r(B0,B1,r,2400):.4f}")
