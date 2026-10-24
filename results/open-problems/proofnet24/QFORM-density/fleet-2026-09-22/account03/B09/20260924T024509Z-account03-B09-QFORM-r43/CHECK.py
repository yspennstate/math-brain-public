import numpy as np, math

rng=np.random.default_rng(20260924)
max_abs=0.0
checked=0

for trial in range(200):
    Q,_=np.linalg.qr(rng.normal(size=(3,3)))
    R,_=np.linalg.qr(rng.normal(size=(7,2)))
    s1=0.5+1.5*rng.random()
    s2=0.5+1.5*rng.random()
    C=Q[:,:2]@np.diag([s1,s2])@R.T
    n=Q[:,2]
    Delta=s1*s2

    H=rng.normal(size=(3,3))
    P=(H+H.T)/2
    P[np.diag_indices(3)] += np.array([1.5,2.0,2.5])
    a=P@n

    for i in range(3):
        d=P[i,i]
        if abs(d)<0.05:
            continue
        K=[j for j in range(3) if j!=i]
        M=C[K,:]-np.outer(P[K,i]/d,C[i,:])
        Z2=np.linalg.det(M@M.T)
        rhs=Delta**2*(a[i]/d)**2
        max_abs=max(max_abs,abs(Z2-rhs))
        checked += 1

assert max_abs < 1e-9, max_abs

C=np.array([[1.,0.],[0.,1.],[-1.,-1.]])
Delta=np.prod(np.linalg.svd(C,compute_uv=False))
n=np.array([1.,1.,1.])/math.sqrt(3)

P=2*np.eye(3)
a=P@n
A0=np.linalg.norm(a)
V=Delta**2*A0**2
Raniso=A0**2/Delta
A=np.block([[P,C],[C.T,np.zeros((2,2))]])
evals_pos=np.linalg.eigvalsh(A)
new_bound=2**(11/4)*(Delta*abs(P[0,0]*a[0]))**(-1/4)

P0=np.ones((3,3))-np.eye(3)
a0=P0@n
A0z=np.linalg.norm(a0)
Vz=Delta**2*A0z**2
Az=np.block([[P0,C],[C.T,np.zeros((2,2))]])
evals_zero=np.linalg.eigvalsh(Az)
forced=A0z/(2*math.sqrt(6))

partner=3*6**(-1/3)
route_const=2**(11/4)*6**0.25

print(f"random identities checked = {checked}")
print(f"max absolute Schur-area error = {max_abs:.3e}")
print(f"Delta regression = {Delta:.15f}")
print(f"A0 regression = {A0:.15f}")
print(f"V regression = {V:.15f}")
print(f"R_aniso regression = {Raniso:.15f}")
print("positive-pivot spectrum =", np.array2string(evals_pos, precision=12))
print(f"new nonphysical-kernel bound = {new_bound:.15f}")
print("zero-diagonal spectrum =", np.array2string(evals_zero, precision=12))
print(f"zero-diagonal V = {Vz:.15f}")
print(f"forced offdiagonal threshold = {forced:.15f}")
print(f"actual offdiagonal = {P0[0,1]:.15f}")
print(f"high-anisotropy routing constant = {route_const:.15f}")
print(f"account04/B09 partner bound = {partner:.15f}")
print("ALL CHECKS PASSED")
