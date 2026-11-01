import numpy as np
from itertools import product
bs=[]
for k in range(2):
 A=np.zeros((2,2),complex);A[k,k]=1;bs.append(A)
A=np.array([[0,1],[1,0]],complex)/np.sqrt(2);bs.append(A)
A=np.array([[0,1j],[-1j,0]],complex)/np.sqrt(2);bs.append(A)
def prob(K):
 d=np.linalg.det(K).real;a=K[0,0].real;b=K[1,1].real
 return np.array([1-a-b+d,a-d,b-d,d])
def jets(K,C):
 D=(np.trace(K)*np.trace(C)-np.trace(K@C)).real
 a=C[0,0].real;b=C[1,1].real
 return np.array([-a-b+D,a-D,b-D,D])
def hess(K):
 p=prob(K);gs=np.array([jets(K,C) for C in bs]).T
 lam=np.log(p[1]*p[2]/p[0]/p[3]);J=np.zeros((4,4));J[0,1]=J[1,0]=.5;J[2,2]=J[3,3]=-.5
 return gs.T@np.diag(1/p)@gs-2*lam*J
rng=np.random.default_rng(7501)
worst=(1e10,None)
for t in range(1000):
 Z=rng.normal(size=(2,2))+1j*rng.normal(size=(2,2));Q=np.linalg.qr(Z)[0]
 K=Q@np.diag(rng.uniform(.1,.7,size=2))@Q.conj().T
 u=rng.normal(size=2)+1j*rng.normal(size=2);u*=.2/np.linalg.norm(u);D=np.outer(u,u.conj())
 eps=1e-3
 H2=(hess(K+eps*D)+hess(K-eps*D)-2*hess(K))/(eps*eps)
 mi=np.linalg.eigvalsh(H2)[0]
 if mi<worst[0]:worst=mi,(K,D,H2)
print('rankone metric convexity minimum',worst[0]);print(worst[1])
