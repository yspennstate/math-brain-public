import math
import numpy as np

h=9/16
q=2*h
kbar=5/2
C=2*math.sqrt(math.e)*(kbar/(kbar-2*q))*q**-0.5
C_exact=(40/3)*math.sqrt(2*math.e)
assert abs(C-C_exact)<1e-12
CJ=C_exact*(125/76)**(1/5)
print(f"h={h:.12g} q={q:.12g}")
print(f"C_mixed={C:.15f}")
print(f"C_router={CJ:.15f}")

beta=(3/16)*math.sqrt(3/5)
zs=[beta,beta/(14400**(1/6)),(beta/120)/(225**(1/6))]
for idx,z in enumerate(zs):
    paid=CJ/z
    packet=(19/500)*z**6
    pscale=packet**(1/6)
    print(f"k={idx} zeta/L={z:.15g} new_paid_coeff={paid:.15f} double_packet/L^6={packet:.15e} sixthroot/L={pscale:.15g}")

for m in [2,5,20]:
    U=np.zeros((m+2,3));V=np.zeros((m+2,3))
    U[0]=[1,0,0]; U[1]=[0,1,0]; U[2:,2]=1/math.sqrt(m)
    V[0]=[1,0,0]; V[1]=[0,0,1]; V[2:,1]=1/math.sqrt(m)
    assert np.max(np.abs(U.T@U-np.eye(3)))<1e-12
    assert np.max(np.abs(V.T@V-np.eye(3)))<1e-12
    M=U@V.T
    s=np.linalg.svd(M,compute_uv=False)
    assert np.max(np.abs(s[:3]-1))<1e-12
    assert abs(np.linalg.det(M[:2,:2]))<1e-12
    vals=[]
    for i in range(2,m+2):
        for j in range(2,m+2):
            vals.append(np.linalg.det(M[np.ix_([0,1,i],[0,1,j])]))
    assert max(abs(abs(v)-1/m) for v in vals)<1e-12
    assert abs(sum(v*v for v in vals)-1)<1e-10
    A=np.block([[np.zeros_like(M), M],[M.T,np.zeros_like(M)]])
    ev=np.linalg.eigvalsh(A)
    large=sorted([round(abs(x),12) for x in ev if abs(x)>1e-8])
    assert large==[1.0]*6
    print(f"stress m={m}: singulars={s[:3].tolist()} anchor_det=0 max_minor={max(abs(v) for v in vals):.12g} packet={sum(v*v for v in vals):.12g}")

g=np.array([.5,.5,.5,.5])
r=np.array([.5,-.5,.5,-.5])
assert abs(g@r)<1e-12 and abs(np.linalg.norm(g)-1)<1e-12 and abs(np.linalg.norm(r)-1)<1e-12
A=np.zeros((5,5))
A[0,1:]=g; A[1:,0]=g
A[1:,1:]=np.outer(r,r)
ev=np.linalg.eigvalsh(A)
nz=sorted([round(float(x),12) for x in ev if abs(x)>1e-8])
assert nz==[-1.0,1.0,1.0]
lev=g*g+r*r
assert np.max(lev)<=.5+1e-12
mf=3*4**(2/3)
print(f"MF target eigenvalues={nz} max_leaf_leverage={lev.max():.12g} density_bound={mf:.15f}")
print(f"stress_holder_bound={3*2**(1/3):.15f}")
print("QFORM_B08_R22_CHECK_PASS")
