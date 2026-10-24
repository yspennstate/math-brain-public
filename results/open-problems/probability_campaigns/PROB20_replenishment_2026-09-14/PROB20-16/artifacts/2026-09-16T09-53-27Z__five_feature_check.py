import numpy as np

SEED=20260916
rng=np.random.default_rng(SEED)

# Hermitian coordinate basis: three diagonals, then Re/Im for 12,13,23.
def hbasis():
    E=[]
    for i in range(3):
        A=np.zeros((3,3),complex); A[i,i]=1; E.append(A)
    for i,j in [(0,1),(0,2),(1,2)]:
        A=np.zeros((3,3),complex); A[i,j]=A[j,i]=1; E.append(A)
        A=np.zeros((3,3),complex); A[i,j]=1j; A[j,i]=-1j; E.append(A)
    return E
BASIS=hbasis()

def adj3(A):
    return A@A-np.trace(A)*A+0.5*(np.trace(A)**2-np.trace(A@A))*np.eye(3,dtype=complex)

def atoms(K):
    p=np.zeros(8)
    for mask in range(8):
        Q=K.copy()
        for i in range(3):
            if not ((mask>>i)&1): Q[i,i]-=1
        p[mask]=(((-1)**(3-mask.bit_count()))*np.linalg.det(Q)).real
    return p

def atom_derivs(K,A):
    q=np.zeros(8)
    for mask in range(8):
        Q=K.copy()
        for i in range(3):
            if not ((mask>>i)&1): Q[i,i]-=1
        sg=(-1)**(3-mask.bit_count())
        q[mask]=(sg*np.linalg.det(Q)*np.trace(np.linalg.solve(Q,A))).real
    return q

def ctM(K,p):
    c=np.array([
        np.log(p[2]*p[4]/(p[0]*p[6])),
        np.log(p[1]*p[4]/(p[0]*p[5])),
        np.log(p[1]*p[2]/(p[0]*p[3]))])
    tau=np.log(p[0]*p[3]*p[5]*p[6]/(p[1]*p[2]*p[4]*p[7]))
    M=np.diag(c)+tau*K
    return c,tau,M

def features():
    return np.array([[(mask>>i)&1 for i in range(3)]+[float(mask==0),float(mask==7)] for mask in range(8)],float)
Z=features()

def cov_features(p):
    m=p@Z
    return np.einsum('s,si,sj->ij',p,Z,Z)-np.outer(m,m)

def feature_covectors(K):
    H=[]
    for i in range(3):
        A=np.zeros((3,3),complex); A[i,i]=1; H.append(A)
    H.append(-adj3(np.eye(3)-K))
    H.append(adj3(K))
    return H

def fi5_direct(p,q):
    S=cov_features(p); dz=q@Z
    return float(dz@np.linalg.solve(S,dz))

def fi5_middle(p,q):
    p0,p7=p[0],p[7]; r=1-p0-p7
    q0,q7=q[0],q[7]; qM=-(q0+q7)
    u=np.array([p[1<<i] for i in range(3)])
    v=np.array([p[7^(1<<i)] for i in range(3)])
    du=np.array([q[1<<i] for i in range(3)])
    dv=np.array([q[7^(1<<i)] for i in range(3)])
    h=(u+v)/r; k=(u-v)/r
    dotk=((du-dv)-k*qM)/r
    S=np.diag(h)-np.outer(k,k)
    cat=q0*q0/p0+q7*q7/p7+qM*qM/r
    return float(cat+r*dotk@np.linalg.solve(S,dotk))

def frozen(K,M,A):
    return float((-2*np.trace(M@adj3(A))).real)

def matrices(K):
    p=atoms(K); c,tau,M=ctM(K,p); delta=float(np.linalg.det(M).real)
    Sig=cov_features(p); H=feature_covectors(K)
    C=np.empty((5,5))
    for i in range(5):
        for j in range(5):
            C[i,j]=(np.trace(M@H[i]@M@H[j]).real
                    -0.5*np.trace(M@H[i]).real*np.trace(M@H[j]).real)
    # Matrix of Q5=FI5+frozen in 9D basis, built directly.
    L=np.empty((5,9))
    for a,h in enumerate(H):
        for j,E in enumerate(BASIS): L[a,j]=np.trace(h@E).real
    Qfi=L.T@np.linalg.solve(Sig,L)
    Qfr=np.empty((9,9))
    for i,E in enumerate(BASIS):
        Qfr[i,i]=frozen(K,M,E)
        for j in range(i):
            val=(frozen(K,M,E+BASIS[j])-Qfr[i,i]-Qfr[j,j])/2
            Qfr[i,j]=Qfr[j,i]=val
    return p,c,tau,M,delta,Sig,C,Qfi+Qfr,L,Qfr

def randK():
    Zm=rng.normal(size=(3,3))+1j*rng.normal(size=(3,3)); U,_=np.linalg.qr(Zm)
    x=rng.uniform(-8,8,3); ev=1/(1+np.exp(-x))
    return U@np.diag(ev)@U.conj().T

max_formula=0.; min_full_minus_proj=1e100
min_q5=1e100; min_det_ratio=1e100; min_kernel_f=1e100
accepted=0
for _ in range(20000):
    K=randK(); p=atoms(K)
    if p.min()<1e-11: continue
    accepted+=1
    p,c,tau,M,delta,Sig,C,Q5,L,Qfr=matrices(K)
    evC=np.linalg.eigvalsh(C)
    assert (evC<0).sum()==1 and (evC>0).sum()==4
    ratio=np.linalg.det(C+delta*Sig)/np.linalg.det(C)
    min_det_ratio=min(min_det_ratio,ratio)
    min_q5=min(min_q5,np.linalg.eigvalsh(Q5)[0])
    coeff=rng.normal(size=9); A=sum(x*E for x,E in zip(coeff,BASIS))
    q=atom_derivs(K,A)
    f5=fi5_direct(p,q); f5m=fi5_middle(p,q)
    max_formula=max(max_formula,abs(f5-f5m))
    full=float(np.sum(q*q/p))
    min_full_minus_proj=min(min_full_minus_proj,full-f5)
    _,_,Vh=np.linalg.svd(L)
    N=Vh[5:].T
    Fk=N.T@Qfr@N
    min_kernel_f=min(min_kernel_f,np.linalg.eigvalsh(Fk)[0])

print('status=PASS_DIAGNOSTIC')
print('seed=',SEED)
print('accepted_broad_kernels=',accepted)
print('max_abs_direct_vs_middle_FI5=',repr(max_formula))
print('min_full_FI_minus_FI5=',repr(min_full_minus_proj))
print('min_frozen_on_five_feature_kernel=',repr(min_kernel_f))
print('min_eigenvalue_FI5_plus_frozen=',repr(min_q5))
print('min_det_ratio_det(C5+deltaSigma)/det(C5)=',repr(min_det_ratio))
print('universal_FI5_certificate_proved=False')