import math
import numpy as np

beta=(3/16)*math.sqrt(3/5)
router=3*2**(7/6)*6**(1/6)*beta**(-2/3)*8**(1/3)
aligned=12*2**(-1/3)
transverse=3*2**(11/6)

def sylvester(n):
    H=np.array([[1.0]])
    while H.shape[0] < n:
        H=np.block([[H,H],[H,-H]])
    return H/math.sqrt(n)

m=8
H=sylvester(m)
u,v,w,z=H[:,0],H[:,1],H[:,2],H[:,4]
C=np.outer(u,u)
Balign=np.outer(u,u)+np.outer(v,v)
Aalign=np.block([[C,Balign],[Balign,C]])
ev=np.linalg.eigvalsh(Aalign)
nz=ev[np.abs(ev)>1e-10]
assert np.allclose(nz,[-1,1,2],atol=1e-12)
vals,vec=np.linalg.eigh(Aalign)
R=vec[:,np.abs(vals)>=1-1e-10]
lev=np.sum(R*R,axis=1)
assert abs(np.max(lev)-3/(2*m))<1e-12

J1=np.where(z>0)[0]
J0=np.where(z<0)[0]
M_align=np.stack([u,v])
MJ=M_align[:,J1]
Pi=MJ.T@np.linalg.inv(MJ@MJ.T)@MJ
Calign_cross=np.outer(u[J0],u[J1])@(np.eye(len(J1))-Pi)
assert np.linalg.norm(Calign_cross,'fro')<1e-12

Btrans=np.outer(v,v)+np.outer(w,w)
Atrans=np.block([[C,Btrans],[Btrans,C]])
evt=np.linalg.eigvalsh(Atrans)
nzt=evt[np.abs(evt)>1e-10]
assert np.allclose(nzt,[-1,-1,1,1,1,1],atol=1e-12)
M=np.stack([v,w])
MJ=M[:,J1]
S=math.sqrt(np.linalg.det(MJ@MJ.T))
Pi=MJ.T@np.linalg.inv(MJ@MJ.T)@MJ
Cproj=np.outer(u[J0],u[J1])@(np.eye(len(J1))-Pi)
F=np.linalg.norm(Cproj,'fro')
marg=np.sum(Cproj*Cproj,axis=1)/(F*F)
assert abs(S-.5)<1e-12
assert abs(F-.5)<1e-12
assert np.max(np.abs(marg-.25))<1e-12
assert abs(transverse - 3*2**(7/6)*(S*F)**(-1/3))<1e-12

print(f"beta={beta:.15f}")
print(f"router_constant={router:.12f}")
print(f"aligned_fixed_source_constant={aligned:.12f}")
print(f"transverse_gc_constant={transverse:.12f}")
print(f"m8_max_large_eigenspace_leverage={np.max(lev):.12f}")
print(f"m8_aligned_projected_F={np.linalg.norm(Calign_cross,'fro'):.12e}")
print(f"m8_transverse_S={S:.12f}")
print(f"m8_transverse_F={F:.12f}")
print(f"m8_transverse_max_row_marginal={np.max(marg):.12f}")
print("QFORM_B08_173735_CHECK_PASS")
