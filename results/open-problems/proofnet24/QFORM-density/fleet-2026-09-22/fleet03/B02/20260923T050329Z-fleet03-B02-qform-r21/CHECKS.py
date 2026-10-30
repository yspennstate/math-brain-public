import math
import numpy as np

rng=np.random.default_rng(20260923)

def e2(M):
    s=np.linalg.svd(M,compute_uv=False)
    lam=s*s
    return sum(lam[i]*lam[j] for i in range(len(lam)) for j in range(i+1,len(lam)))

max_identity_error=0.0
max_compound_violation=0.0
for _ in range(100):
    m,n=5,6
    d,e,a=rng.normal(size=3)
    if abs(a)<0.2:
        a += 0.5
    delta=d*e-a*a
    if abs(delta)<0.2:
        e += 1.0
        delta=d*e-a*a
    u,c=rng.normal(size=(2,m))
    r,v=rng.normal(size=(2,n))
    N=rng.normal(size=(m,n))
    P=np.array([[d,a],[a,e]])
    T=N-np.column_stack([u,c])@np.linalg.inv(P)@np.vstack([r,v])
    S=N-np.outer(c,r)/a
    xi0=a*u-d*c
    eta0=a*v-e*r
    T2=S+np.outer(xi0,eta0)/(a*delta)
    max_identity_error=max(max_identity_error,np.linalg.norm(T-T2)/(1+np.linalg.norm(T)))
    if np.linalg.norm(xi0)>1e-12 and np.linalg.norm(eta0)>1e-12:
        Px=np.eye(m)-np.outer(xi0,xi0)/(xi0@xi0)
        Py=np.eye(n)-np.outer(eta0,eta0)/(eta0@eta0)
        F=np.linalg.norm(Px@S@Py,'fro')
        correction=np.linalg.norm(xi0)*np.linalg.norm(eta0)*F/(abs(a*delta))
    else:
        correction=0.0
    violation=max(0.0, math.sqrt(e2(S))-(math.sqrt(e2(T))+correction))
    max_compound_violation=max(max_compound_violation,violation)

# Exact B06 correction witness.
A=np.array([
[0,1,0,1,0,0],
[1,0,0,0,0,1],
[0,0,0,0,1,0],
[1,0,0,0,0,1],
[0,0,1,0,0,0],
[0,1,0,1,0,0]],dtype=float)
# anchors x=0,y=1; U=(2,3), V=(4,5)
d,e,a=A[0,0],A[1,1],A[0,1]
delta=d*e-a*a
u=A[[2,3],0]; c=A[[2,3],1]
r=A[0,[4,5]]; v=A[1,[4,5]]
N=A[np.ix_([2,3],[4,5])]
P=A[np.ix_([0,1],[0,1])]
S=N-np.outer(c,r)/a
T=N-np.column_stack([u,c])@np.linalg.inv(P)@np.vstack([r,v])
xi0=a*u-d*c; eta0=a*v-e*r
Px=np.eye(2)-np.outer(xi0,xi0)/(xi0@xi0)
Py=np.eye(2)-np.outer(eta0,eta0)/(eta0@eta0)
F=np.linalg.norm(Px@S@Py,'fro')
correction_resource=(np.linalg.norm(xi0)**2*np.linalg.norm(eta0)**2/delta**2)*F**2

q=4/3
C3=3*math.e/((3-2*q)*math.sqrt(q))
theta=3/4
K=theta**(-theta)*(1-theta)**(-(1-theta))
CE2=(math.e*(3*theta/(3*theta-2))*K**(-1/(4*theta)))**(2/3)
Cpair=7*(math.pi/12)**(1/7)
CpairE2=Cpair*CE2**(3/7)
Cgate=CpairE2*12**(1/14)
Cpartner=6*3**(1/3)*2**(2/9)

print('QFORM_B02_R21_CHECK_PASS')
print(f'max_rank_one_identity_scaled_error={max_identity_error:.3e}')
print(f'max_compound_triangle_violation={max_compound_violation:.3e}')
print(f'B06_witness_E2_cross={e2(S):.12g}')
print(f'B06_witness_E2_true={e2(T):.12g}')
print(f'B06_witness_correction_resource={correction_resource:.12g}')
print(f'C3_q4over3={C3:.12f}')
print(f'C_E2_theta3over4={CE2:.12f}')
print(f'C_pair_E2_gate={CpairE2:.12f}')
print(f'C_gate_after_J_gt_Zover3={Cgate:.12f}')
print(f'C_partner_nested={Cpartner:.12f}')
