import json
import numpy as np
from itertools import product

basis=[]
for i in range(3):
 A=np.zeros((3,3),complex); A[i,i]=1; basis.append(A)
for i,j in [(0,1),(0,2),(1,2)]:
 A=np.zeros((3,3),complex); A[i,j]=A[j,i]=1/np.sqrt(2); basis.append(A)
 A=np.zeros((3,3),complex); A[i,j]=1j/np.sqrt(2); A[j,i]=-1j/np.sqrt(2); basis.append(A)
basis=np.array(basis)
def coord(A): return np.einsum('iab,ba->i',basis,A).real
def adj2(A): return np.trace(A)*np.eye(2)-A

def data(K):
 p=[]
 for bits in product([0,1],repeat=3):
  S=np.array(bits,dtype=bool)
  J=K-np.diag(~S)
  p.append(((-1)**sum(~S)*np.linalg.det(J)).real)
 p=np.array(p)
 assert p.min()>0
 f=-np.log(p)
 c=np.array([f[3]-f[2]-f[1]+f[0],f[5]-f[4]-f[1]+f[0],f[6]-f[4]-f[2]+f[0]])
 tau=f[7]-f[3]-f[5]-f[6]+f[1]+f[2]+f[4]-f[0]
 M=np.diag(c)+tau*K
 delta=np.linalg.det(M).real
 Q=np.zeros((9,9))
 endpoint=[]
 for k in range(3):
  a=K[k,k].real;b=1-a
  ek=np.eye(3)[:,k]
  d=coord(np.outer(ek,ek)); Q+=np.outer(d,d)/(a*b)
  R=[j for j in range(3) if j!=k]
  v=K[R,k]
  for s in [0,1]:
   r=a-(1-s);pi=a if s else b
   V=np.eye(3)[:,R].astype(complex); V[k,:]=-v.conj()/r
   J=K[np.ix_(R,R)]-np.outer(v,v.conj())/r
   for F in [J,np.eye(2)-J]:
    P=np.sqrt(pi)*V@adj2(F)@V.conj().T/np.sqrt(np.linalg.det(F).real)
    endpoint.append(P)
    z=coord(P);Q+=np.outer(z,z)
 W=np.empty((9,9))
 Mi=np.linalg.inv(M)
 for i,A in enumerate(basis):
  for j,B in enumerate(basis): W[i,j]=3*delta*np.trace(Mi@A@Mi@B).real
 W+=Q
 ell=coord(Mi)
 ray=np.linalg.solve(W,ell)
 A=np.einsum('i,iab->ab',ray,basis)
 A/=np.trace(Mi@A).real
 return {'K_eigenvalues':np.linalg.eigvalsh(K).tolist(),'M_eigenvalues':np.linalg.eigvalsh(M).tolist(),'optimizer_eigenvalues':np.linalg.eigvalsh(A).tolist(),'endpoint_scalar':float(3*delta*ell@ray),'optimizer':[[[z.real,z.imag] for z in row] for row in A]}

cases={}
for c in [-1,-61/1861,0,1]:
 z=c+1j*np.sqrt(1-c*c)
 K=np.array([[.43,.245*z,.275],[.245*z.conjugate(),.41,.19],[.275,.19,.65]])
 cases['C014_'+str(c)]=data(K)
K=.5*np.eye(3)+.25j*np.array([[0,1,-1],[-1,0,1],[1,-1,0]])
cases['X021_balanced']=data(K)
K=np.array([[.2,.1,.05j],[.1,.6,.1],[-.05j,.1,.8]])
cases['X021_unequal']=data(K)
for t in [.001,.01,.1,1,10,100]:
 # A deterministic odds deformation of the unequal-phase example.
 L=K@np.linalg.inv(np.eye(3)-K)
 Kt=t*L@np.linalg.inv(np.eye(3)+t*L)
 cases['odds_scale_'+str(t)]=data(Kt)
print(json.dumps(cases,indent=2))
