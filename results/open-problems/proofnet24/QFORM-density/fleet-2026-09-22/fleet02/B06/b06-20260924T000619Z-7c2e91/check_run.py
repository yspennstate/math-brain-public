import numpy as np
from math import sqrt

rng=np.random.default_rng(260924)
max_det=max_frame=max_e2_rel=0.0
count=0
for _ in range(1000):
    m=8
    E=rng.normal(size=(2,m))
    G=E@E.T
    if np.linalg.det(G)<1e-5:
        continue
    T=rng.normal(size=(2,2)); T=(T+T.T)/2
    if abs(np.linalg.det(T))<1e-5:
        continue
    d=rng.normal(size=m)
    h=int(rng.integers(m))
    eh=E[:,h]
    s=d[h]+eh@T@eh
    if abs(s)<1e-5:
        continue
    Th=T-np.outer(T@eh,T@eh)/s
    max_det=max(max_det,abs(np.linalg.det(Th)-np.linalg.det(T)*d[h]/s))
    alpha=eh@np.linalg.inv(G)@eh
    J=[j for j in range(m) if j!=h]
    Wh=np.linalg.det(E[:,J]@E[:,J].T)
    max_frame=max(max_frame,abs(Wh-np.linalg.det(G)*(1-alpha)))
    rng.shuffle(J)
    I=J[:len(J)//2]; K=J[len(J)//2:]
    M=E[:,I].T@Th@E[:,K]
    sv=np.linalg.svd(M,compute_uv=False)
    z=(sv[0]*sv[1])**2
    WI=np.linalg.det(E[:,I]@E[:,I].T)
    WK=np.linalg.det(E[:,K]@E[:,K].T)
    rhs=np.linalg.det(Th)**2*WI*WK
    if abs(rhs)>1e-12:
        max_e2_rel=max(max_e2_rel,abs(z-rhs)/abs(rhs))
    count += 1

print('random_instances',count)
print('max_det_transfer_abs_error',max_det)
print('max_frame_delete_abs_error',max_frame)
print('max_e2_factor_relative_error',max_e2_rel)

# Exact route-obstruction prototype, represented numerically for sanity checking.
r=1/sqrt(2)
H=np.array([[0.,1.],[1.,0.]])
E=np.array([[r,.5,0.],[r,0.,.5]])
T=np.diag([1.,-1.])
qdiag=np.diag(E.T@T@E)
D=np.diag(-qdiag)
S=D+E.T@T@E
C=S+E.T@H@E
A=np.block([[H,E],[E.T,C]])
G=E@E.T
alpha=E[:,0]@np.linalg.inv(G)@E[:,0]
W=np.linalg.det(G)
Wh=np.linalg.det(E[:,1:]@E[:,1:].T)
B=A[np.ix_([0,2,3],[0,2,3])]
print('prototype_alpha_h',alpha)
print('prototype_W',W)
print('prototype_W_delete_h',Wh)
print('prototype_S_diagonal',np.diag(S))
print('prototype_rank_A',np.linalg.matrix_rank(A,tol=1e-10))
print('prototype_B_eigenvalues',np.linalg.eigvalsh(B))
print('prototype_scaled4_A_eigenvalues',np.linalg.eigvalsh(4*A))
