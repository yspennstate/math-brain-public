import math
import numpy as np

eps=0.1
h=0.5
a=1/(2*math.sqrt(2))
beta=a*np.array([1.,1.,-1.,-1.])
gamma=a*np.array([1.,-1.,1.,-1.])
u=np.ones(4)/2
p=math.sqrt(0.5-2*eps**2)
alphaJ=p*beta+eps*u
alphaK=-p*beta+eps*u
RJ=np.column_stack([alphaJ,beta,gamma])
RK=np.column_stack([alphaK,beta,gamma])
r0=np.array([[math.sqrt(h),0.,0.]])
R=np.vstack([r0,RJ,RK])
M=np.array([[0.,1.,0.],[1.,0.,0.],[0.,0.,1.]])
A=R@M@R.T
C=RJ@M@RK.T
V=np.column_stack([beta,gamma])
coefJ=np.linalg.solve(V.T@V,V.T@alphaJ)
coefK=np.linalg.solve(V.T@V,V.T@alphaK)
etaJ=alphaJ-V@coefJ
etaK=alphaK-V@coefK
B=A[np.ix_([0,1,2],[0,1,2])]
C0=3*2**(2/3)
print('eps',eps)
print('p',repr(p))
print('||R^T R-I||',repr(float(np.linalg.norm(R.T@R-np.eye(3)))))
print('eig(A)',[float(x) for x in np.linalg.eigvalsh(A)])
print('S_J',RJ[:,1:].T@RJ[:,1:])
print('||eta_J||',repr(float(np.linalg.norm(etaJ))))
print('||eta_K||',repr(float(np.linalg.norm(etaK))))
print('eta_J dot beta,gamma',repr(float(etaJ@beta)),repr(float(etaJ@gamma)))
print('cross singular values',[float(x) for x in np.linalg.svd(C,compute_uv=False)])
print('det principal triple',repr(float(np.linalg.det(B))))
print('partner bound',repr(float(C0*abs(np.linalg.det(B))**(-1/3))))
