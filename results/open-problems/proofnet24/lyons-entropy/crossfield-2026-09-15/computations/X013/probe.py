import numpy as np
from scipy.optimize import minimize_scalar


def atoms(K):
 n=len(K); ret=[]
 for mask in range(1<<n):
  Q=K-np.diag([int(not(mask>>i&1)) for i in range(n)])
  p=np.linalg.det(Q).real*(-1)**(n-mask.bit_count())
  ret.append((p,np.linalg.inv(Q)))
 return ret

def fi(data,A,B=None):
 if B is None:B=A
 return sum(p*np.trace(Y@A).real*np.trace(Y@B).real for p,Y in data)

def case(c):
 K=np.array([[.1,c,.004,.004],[c,.4,.008,-.004],[.004,.008,.5,.003j],[.004,-.004,-.003j,.65]],dtype=complex)
 A=np.diag([1,-1,.05,-.05])
 data=atoms(K)
 L=np.linalg.solve(np.eye(4)-K,K)
 Delta=-np.linalg.slogdet(L)[1]+np.log(np.diag(L).real).sum()
 JA=fi(data,A); spec=fi(data,np.diag([1,1,.05,.05]))
 def D(z):
  return np.array([[np.cosh(z),np.sinh(z),0,0],[np.sinh(z),np.cosh(z),0,0],[0,0,.05,0],[0,0,0,.05]])
 res=minimize_scalar(lambda z:fi(data,D(z)),bounds=(-1,1),method='bounded')
 beta=res.fun
 Hminus=JA+sum(p*np.log(p)*((np.trace(Y@A).real)**2-np.trace(Y@A@Y@A).real) for p,Y in data)
 return dict(c=c,Delta=Delta,JA=JA,spec=spec,beta=beta,z=res.x,old=(1+Delta/4)*JA-Delta*spec,new=(1+Delta/4)*JA-Delta*beta,actual=Hminus)

if __name__=='__main__':
 for c in [.132,.134,.136,.138,.14]:print(case(c))
