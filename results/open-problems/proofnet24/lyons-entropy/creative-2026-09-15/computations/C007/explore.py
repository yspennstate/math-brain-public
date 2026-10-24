import numpy as np

def randk(rng,n=2):
 z=rng.normal(size=(n,n))+1j*rng.normal(size=(n,n)); q,_=np.linalg.qr(z)
 ev=rng.beta(.6,.6,size=n); ev=np.clip(ev,1e-5,1-1e-5)
 return (q*ev)@q.conj().T

def atoms(A):
 a=A[0,0].real;b=A[1,1].real;r=a*b-abs(A[0,1])**2
 return np.array([1-a-b+r,a-r,b-r,r])

def dp(A,Q):
 a=A[0,0].real;b=A[1,1].real;c=A[0,1];u=Q[0,0].real;v=Q[1,1].real;w=Q[0,1]
 r=u*b+a*v-2*(c.conjugate()*w).real
 return np.array([-u-v+r,u-r,v-r,r])

def fisher(A,Q):
 p=atoms(A);v=dp(A,Q);return np.dot(v/p,v)

def fish_der(A,Q,E):
 p=atoms(A);v=dp(A,Q);pe=dp(A,E)
 h=(Q[0,0]*E[1,1]+Q[1,1]*E[0,0]-2*(Q[0,1].conjugate()*E[0,1]).real).real
 dv=h*np.array([1,-1,-1,1]);return np.sum(2*v*dv/p-v*v*pe/p**2)

rng=np.random.default_rng(700720260915)
best=(float('inf'),None)
for it in range(250000):
 A=randk(rng);B=randk(rng)
 u=rng.normal(size=2)+1j*rng.normal(size=2);u/=np.linalg.norm(u);Q=np.outer(u,u.conjugate())
 f=fisher(A,Q);d=2*f+fish_der(A,Q,A-B);val=d/f
 if val<best[0]:
  best=val,(A,B,Q,f,d)
 if val<-.1:
  print('FOUND',it,val, flush=True);break
print(best[0]);
for x in best[1]:print(x)
np.savez('/workspace/scratch/f042dae27852/creative-lyons-20260915/computations/C007/fisher_search.npz',A=best[1][0],B=best[1][1],Q=best[1][2],f=best[1][3],d=best[1][4])
