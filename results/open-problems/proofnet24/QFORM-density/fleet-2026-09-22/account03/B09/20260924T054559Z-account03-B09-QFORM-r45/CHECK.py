import itertools
import math
import numpy as np

SEED=4509
rng=np.random.default_rng(SEED)
C44=15.059181790788745

def packet_identity(P,C):
    T=float(np.linalg.det(P@P.T+C@C.T))
    detP=float(np.linalg.det(P))
    gs=[]
    for k in range(3):
        H=[i for i in range(3) if i!=k]
        B=P[np.ix_(H,H)]
        p=P[H,k]
        adj=np.array([[B[1,1],-B[0,1]],[-B[1,0],B[0,0]]])
        g=np.linalg.det(B)*C[k,:]-p@adj@C[H,:]
        gs.append(g)
    G=sum(float(g@g) for g in gs)
    W=0.0
    for r,s in itertools.combinations(range(C.shape[1]),2):
        w=np.cross(C[:,r],C[:,s])
        W+=float((P@w)@(P@w))
    return T,detP*detP+G+W,detP,G,W,gs

max_rel=0.0
max_minor=0.0
for _ in range(200):
    M=rng.standard_normal((3,3)); P=(M+M.T)/2
    U=rng.standard_normal((3,2)); V=rng.standard_normal((2,7)); C=U@V
    T,R,detP,G,W,gs=packet_identity(P,C)
    max_rel=max(max_rel,abs(T-R)/(1+abs(T)))
    for k in range(3):
        H=[i for i in range(3) if i!=k]
        for j in range(C.shape[1]):
            minor=np.linalg.det(np.column_stack([P[:,H[0]],P[:,H[1]],C[:,j]]))
            max_minor=max(max_minor,abs(abs(minor)-abs(gs[k][j])))
assert max_rel<1e-12
assert max_minor<1e-12

# Target-valid aggregate-pair regression.
P=np.array([[0.,1,1],[1,0,1],[1,1,0]])
C=.5*np.array([[1.,0],[0,1],[0,0]])
A=np.block([[P,C],[C.T,np.zeros((2,2))]])
eig=np.linalg.eigvalsh(A)
assert np.sum(np.abs(eig)>=1-1e-12)>=3
T,R,detP,G,W,gs=packet_identity(P,C)
D=[detP*detP+float(g@g) for g in gs]
kappa=[]
for k in range(3):
    H=[i for i in range(3) if i!=k]
    B=P[np.ix_(H,H)]
    assert np.linalg.det(B)<0
    kappa.append(float(np.min(np.abs(np.linalg.eigvalsh(B)))))
Rpair=sum(kappa[k]**2*D[k] for k in range(3))
bound=C44*3**(1/8)*Rpair**(-1/8)
assert abs(T-5.625)<1e-12
assert abs(Rpair-13.5)<1e-12
assert abs(bound-12.478138789189643)<1e-12

# Pair-resource forcing counterexample.
S=np.array([[1.,1,1],[1,1,-1],[1,-1,1]])
P2=2*S
C2=.5*np.array([[1.,0],[0,1],[0,0]])
A2=np.block([[P2,C2],[C2.T,np.zeros((2,2))]])
eig2=np.linalg.eigvalsh(A2)
assert np.sum(np.abs(eig2)>=1-1e-12)>=3
pairdets=[]
for k in range(3):
    H=[i for i in range(3) if i!=k]
    pairdets.append(float(np.linalg.det(P2[np.ix_(H,H)])))
assert max(abs(x) for x in pairdets)<1e-12

# Designated partner theorem numerical application.
K=np.diag([2.,1.,1.])
Apart=np.block([[np.zeros((3,3)),K],[K,np.zeros((3,3))]])
eigp=np.linalg.eigvalsh(Apart)
partner_bound=3*np.linalg.det(K)**(-1/3)
assert np.sum(np.abs(eigp)>=1-1e-12)==6
assert abs(partner_bound-2.3811015779522995)<1e-12

print(f'seed={SEED}')
print('random_rank2_packets=200')
print(f'max_relative_cauchy_binet_error={max_rel:.16e}')
print(f'max_abs_polynomial_minor_error={max_minor:.16e}')
print(f'regression_spectrum={eig.tolist()}')
print(f'regression_T={T:.15f}')
print(f'regression_R_pair={Rpair:.15f}')
print(f'regression_density_bound={bound:.15f}')
print(f'nogo_spectrum_eps_half={eig2.tolist()}')
print(f'nogo_all_principal_pair_determinants={pairdets}')
print(f'partner_spectrum={eigp.tolist()}')
print(f'partner_density_bound={partner_bound:.15f}')
print('ALL_ASSERTIONS_PASSED')
