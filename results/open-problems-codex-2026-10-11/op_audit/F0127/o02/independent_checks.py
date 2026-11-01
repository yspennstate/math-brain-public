from pathlib import Path
import numpy as np
from scipy.linalg import expm
from fractions import Fraction
out=[]
def check(name,nu):
 n=len(nu); Q=(nu-np.eye(n))/2
 ev=np.linalg.eigvalsh(-Q)[1:]; K=sum(1/ev); rel=1/ev[0]
 # Independently solve the killed pair-chain backward equations.
 pair=np.kron(Q,np.eye(n))+np.kron(np.eye(n),Q)
 off=[i*n+j for i in range(n) for j in range(n) if i!=j]
 times=np.linalg.solve(-pair[np.ix_(off,off)],np.ones(len(off)))
 mean=times.sum()/n**2
 # Independently solve singleton-target hitting equations.
 target_means=[]
 for o in range(n):
  keep=[i for i in range(n) if i!=o]
  target_means.append(np.linalg.solve(-Q[np.ix_(keep,keep)],np.ones(n-1)).sum()/n)
 # Direct occupancy CTMC: transitions move one occupied walker; landing on
 # an occupied vertex removes its original location, implementing coalescence.
 masks=[s for s in range(1,1<<n) if s.bit_count()>1];idx={s:i for i,s in enumerate(masks)}
 A=np.zeros((len(masks),len(masks)))
 for s in masks:
  for i in range(n):
   if not (s>>i)&1:continue
   for j in range(n):
    if i==j or Q[i,j]==0:continue
    t=(s & ~(1<<i)) | (1<<j); rate=Q[i,j]
    A[idx[s],idx[s]]-=rate
    if t in idx:A[idx[s],idx[t]]+=rate
 coal=np.linalg.solve(-A,np.ones(len(masks)))[idx[(1<<n)-1]]
 bound=rel*max(1,np.log(4*mean/rel))
 density=max(abs(expm(bound*Q)*n-np.ones((n,n))).ravel())
 assert abs(mean-K/2)<1e-9,(name,mean,K)
 assert max(abs(np.array(target_means)-K))<1e-9
 assert density<=.5+1e-10
 out.append(f'{name}: n={n}, pair_mean={mean:.12g}, spectral_K/2={K/2:.12g}, target_mean={target_means[0]:.12g}, coal_mean={coal:.12g}, coal/meet={coal/mean:.12g}, density_at_Hermon_bound={density:.12g}; PASS')
for n in range(2,9):
 nu=(np.ones((n,n))-np.eye(n))/(n-1);check('complete',nu)
for n in range(3,9):
 nu=np.zeros((n,n))
 for i in range(n):nu[i,(i+1)%n]+=.5;nu[i,(i-1)%n]+=.5
 check('cycle',nu)
for n in [5,6,7,8]:
 nu=np.zeros((n,n))
 for i in range(n):
  for d,w in [(1,.35),(-1,.35),(2,.15),(-2,.15)]:nu[i,(i+d)%n]+=w
 check('weighted circulant',nu)
for n in range(2,101):
 meet=Fraction(n-1,n)*Fraction(n-1)
 coal=sum((Fraction(n-1)*Fraction(2,k*(k-1)) for k in range(2,n+1)),Fraction(0))
 assert coal==2*meet
out.append('Exact Fraction complete-graph identities n=2,...,100: PASS')
Path('independent_checks.txt').write_text('\n'.join(out)+'\n',encoding='utf-8')
print('\n'.join(out))
