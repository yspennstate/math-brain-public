import numpy as np
import math

N=64
idx=np.arange(N)
chi1=np.where(((idx>>0)&1)==0,1.0,-1.0)
chi2=np.where(((idx>>1)&1)==0,1.0,-1.0)
chi3=np.where(((idx>>2)&1)==0,1.0,-1.0)
V=np.column_stack([np.ones(N),chi1,chi2])/math.sqrt(N)
assert np.max(np.abs(V.T@V-np.eye(3))) < 1e-13
A=V@V.T
ev=np.linalg.eigvalsh(A)
assert np.allclose(ev[-3:],np.ones(3),atol=1e-12)
assert np.max(np.abs(ev[:-3])) < 1e-12

J=np.where(chi3>0)[0]
I=np.where(chi3<0)[0]
GJ=V[J].T@V[J]
GI=V[I].T@V[I]
assert np.allclose(GJ,.5*np.eye(3),atol=1e-13)
assert np.allclose(GI,.5*np.eye(3),atol=1e-13)
B=A[np.ix_(J,I)]
sv=np.linalg.svd(B,compute_uv=False)
assert np.allclose(sv[:3],.5*np.ones(3),atol=1e-12)
assert sv[3] < 1e-12
Z3=np.prod(sv[:3]**2)
assert abs(Z3-1/64)<1e-13
U,s,VT=np.linalg.svd(B,full_matrices=False)
marg=np.sum(U[:,:3]**2,axis=1)
assert np.max(np.abs(marg-3/32)) < 1e-12

patterns={}
for i in range(N):
    patterns.setdefault((int(chi1[i]),int(chi2[i])),[]).append(i)
R=[patterns[(1,1)][0],patterns[(1,-1)][0],patterns[(-1,1)][0]]
C=[patterns[(1,1)][1],patterns[(1,-1)][1],patterns[(-1,1)][1]]
assert set(R).isdisjoint(C)
K=A[np.ix_(R,C)]
detK=abs(np.linalg.det(K))
assert abs(detK-16/N**3)<1e-15

c_diff=24*math.sqrt(2*math.e)
c_fork=48*math.sqrt(2*math.e)/math.sqrt(3)
c_walsh=12*math.sqrt(2*math.e)
c_partner=3*detK**(-1/3)
c_tau=c_diff/.75

print(f"frame_orth_error={np.max(np.abs(V.T@V-np.eye(3))):.3e}")
print(f"target_top_eigenvalues={ev[-3:]}")
print(f"GJ_diag={np.diag(GJ)} GI_diag={np.diag(GI)}")
print(f"cross_singular_values={sv[:3]}")
print(f"Z3={Z3:.15f}")
print(f"row_marginal_minmax=({marg.min():.15f},{marg.max():.15f})")
print(f"partner_det={detK:.15e}")
print(f"C_diffuse={c_diff:.12f}")
print(f"C_fork={c_fork:.12f}")
print(f"C_walsh={c_walsh:.12f}")
print(f"C_partner_N64={c_partner:.12f}")
print(f"C_diffuse_tau_quarter={c_tau:.12f}")
print("ALL CHECKS PASSED")
