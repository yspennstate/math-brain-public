import numpy as np
from itertools import combinations

def atoms(K):
 m=np.ones(8)
 for s in range(1,8):
  I=[i for i in range(3) if s>>i&1];m[s]=np.linalg.det(K[np.ix_(I,I)]).real
 p=m.copy()
 for i in range(3):
  for s in range(8):
   if not (s>>i&1):p[s]-=p[s|1<<i]
 return p

def data(K):
 p=atoms(K);a=K.diagonal().real
 c=np.log([p[2]*p[4]/(p[0]*p[6]),p[1]*p[4]/(p[0]*p[5]),p[1]*p[2]/(p[0]*p[3])])
 tau=np.log(p[0]*p[3]*p[5]*p[6]/(p[1]*p[2]*p[4]*p[7]));M=np.diag(c)+tau*K
 es=[]
 for i,j in [(1,2),(2,0),(0,1)]:
  for z in [1,1j]:
   A=np.zeros((3,3),complex);A[i,j]=z;A[j,i]=np.conj(z);es.append(A)
 def ad(A):
  return A@A-np.trace(A)*A+0.5*(np.trace(A)**2-np.trace(A@A))*np.eye(3)
 def f(A):return -2*np.trace(M@ad(A)).real
 F=np.zeros((6,6));J=np.zeros((8,6))
 for i,A in enumerate(es):
  F[i,i]=f(A)
  for j,B in enumerate(es[:i]):F[i,j]=F[j,i]=(f(A+B)-f(A)-f(B))/2
  # exact cubic central derivative with +/- 1 and 2 evaluations
  J[:,i]=(8*(atoms(K+A)-atoms(K-A))-(atoms(K+2*A)-atoms(K-2*A)))/12
 return p,tau,F,J

if __name__=='__main__':
 rng=np.random.default_rng(9531);wings=0;fails=0;worst=0;fail=None
 for k in range(200):
  Z=rng.normal(size=(3,3))+1j*rng.normal(size=(3,3));U=np.linalg.qr(Z)[0]
  ev=np.array([10**rng.uniform(-14,-7),rng.uniform(.05,.95),rng.uniform(.05,.95)])
  K=U@np.diag(ev)@U.conj().T;p,tau,F,J=data(K)
  if np.linalg.eigvalsh(F)[0]>=-1e-8:continue
  wings+=1;s=7 if tau>0 else 0;Q=F+np.outer(J[s],J[s])/(p[s]*(1-p[s]));e=np.linalg.eigvalsh(Q)[0]
  if e < -1e-7:
   fails+=1
   if e<worst:worst=e;fail=(K,p,tau,e)
 print('wings',wings,'failures',fails,'worst',worst)
 if fail is not None:print(fail)
