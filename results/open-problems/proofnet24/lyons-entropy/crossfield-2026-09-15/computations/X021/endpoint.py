import numpy as np
from geometry import atoms, data, coordinates, matrix

BASES=[matrix(np.eye(9)[j]) for j in range(9)]

def quad(fn):
 q=np.zeros((9,9)); q[np.diag_indices(9)]=[fn(e) for e in BASES]
 for i in range(9):
  for j in range(i):q[i,j]=q[j,i]=(fn(BASES[i]+BASES[j])-q[i,i]-q[j,j])/2
 return q

def details(K):
 d=data(K); M=d['M']; p=d['p']; IA=[]; End=[]; Marg=[]
 eye=np.eye(3)
 atom_scores=[]
 for mask in range(8):
  C=np.column_stack([K[:,j] if mask>>j&1 else (eye-K)[:,j] for j in range(3)])
  inv=np.linalg.inv(C)
  atom_scores.append(np.array([np.trace(inv@np.column_stack([A[:,j] if mask>>j&1 else -A[:,j] for j in range(3)])).real for A in BASES]))
 atom_scores=np.array(atom_scores)
 FI=atom_scores.T@(p[:,None]*atom_scores)
 E=np.zeros((9,9)); D=np.zeros((9,9))
 for k in range(3):
  a=K[k,k].real
  D[k,k]=1/(a*(1-a))
  for s in [0,1]:
   v=np.zeros(9);v[k]=s/a-(1-s)/(1-a)
   for rs in [0,1]:
    mask=sum((s if j==k else rs)<<j for j in range(3))
    score=atom_scores[mask]-v
    E+=p[mask]*np.outer(score,score)
 def curvature(A):
  adj=A@A-np.trace(A)*A+(np.trace(A)**2-np.trace(A@A))/2*np.eye(3)
  return 2*np.trace(M@adj).real
 R=quad(curvature)
 q=D+E-3*R
 return dict(d=d,E=E,D=D,FI=FI,R=R,Q=q,ev=np.linalg.eigvalsh(q),evfull=np.linalg.eigvalsh(FI-R))

if __name__=='__main__':
 Ks=[np.array([[.2,.1,.05],[.1,.6,.1],[.05,.1,.8]],complex),np.array([[.2,.1,.05j],[.1,.6,.1],[-.05j,.1,.8]],complex),np.array([[.5,.1,0],[.1,.22,.1],[0,.1,.8]],complex)]
 for K in Ks:
  r=details(K)
  print('K=',K,'Q eigenvalues=',r['ev'],'full=',r['evfull'])
 rng=np.random.default_rng(21)
 worst=100;fail=0
 for i in range(100):
  z=rng.normal(size=(3,3))+1j*rng.normal(size=(3,3));u=np.linalg.qr(z)[0]
  eig=rng.uniform(.001,.999,size=3);K=(u*eig)@u.conj().T
  r=details(K);v=r['ev'][0]
  if v<worst:worst=v;W=K
  if v< -1e-7:fail+=1
 print('100 diagnostic kernels: worst=',worst,'fail=',fail,'K=',W)
# Stress just the endpoint certificate on approaching boundary eigenvalues.
if __name__=='__main__':
 worst=100;fail=0
 for i in range(100):
  z=rng.normal(size=(3,3))+1j*rng.normal(size=(3,3));u=np.linalg.qr(z)[0]
  eig=np.array([10**rng.uniform(-7,-1),rng.uniform(.01,.99),1-10**rng.uniform(-7,-1)]);K=(u*eig)@u.conj().T
  r=details(K);v=r['ev'][0]
  if v<worst:worst=v;W=K
  if v< -1e-7:fail+=1
 print('100 boundary diagnostics: worst=',worst,'fail=',fail,'K=',W)
