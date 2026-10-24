import numpy as np
from scipy.sparse import lil_matrix
from scipy.sparse.linalg import spsolve, expm_multiply
from pathlib import Path
import json,time
# Exact finite generator, floating-point stationary probabilities (NOT certified).
# Each vertex of {-1,0,1}^2 recovers at 1 and is infected at lambda times
# its occupied internal neighbors plus its external neighbors (always occupied).
pts=[(x,y) for y in [-1,0,1] for x in [-1,0,1]]
index={p:i for i,p in enumerate(pts)}
n=9;N=1<<n
nbr=[];ext=[]
for x,y in pts:
 ns=[(x+1,y),(x-1,y),(x,y+1),(x,y-1)]
 nbr.append([index[p] for p in ns if p in index]);ext.append(sum(p not in index for p in ns))
center=index[(0,0)]
boundary=set(range(n))-{center}
def crossing(s):
 if not s>>center&1:return False
 return any(s>>j&1 for j in nbr[center])
def generator(lam):
 Q=lil_matrix((N,N),dtype=float)
 for s in range(N):
  total=0.
  for i in range(n):
   rate=1. if s>>i&1 else lam*(ext[i]+sum(s>>j&1 for j in nbr[i]))
   if rate:Q[s,s^(1<<i)]=rate;total+=rate
  Q[s,s]=-total
 return Q.tocsr()
results=[]
for lam in [0.05,0.125,0.25,0.4,0.5]:
 t=time.time();Q=generator(lam)
 A=Q.T.tolil();b=np.zeros(N);A[-1,:]=np.ones(N);b[-1]=1
 pi=spsolve(A.tocsr(),b)
 assert np.min(pi)>-1e-12
 assert abs(pi.sum()-1)<1e-11
 residual=float(np.max(np.abs(Q.T@pi)))
 f=np.array([crossing(s) for s in range(N)],float)
 dens=np.array([s>>center&1 for s in range(N)],float)
 p=float(pi@f);rho=float(pi@dens)
 initial=np.zeros(N);initial[-1]=1
 transient=[]
 for T in [1.,5.,20.]:
  mu=expm_multiply(Q.T*T,initial)
  val=float(mu@f);assert val>=p-1e-10
  transient.append({'time':T,'crossing_probability':val})
 rec={'lambda':lam,'stationary_annulus_crossing':p,'stationary_center_density':rho,'stationary_residual_infinity':residual,'threshold':1/19683,'finite_time_from_full':transient,'seconds':time.time()-t,'states':N}
 results.append(rec);print(json.dumps(rec),flush=True)
Path('wired_results.json').write_text(json.dumps({'description':'Numerical evidence only; 3x3 infected-boundary box, L=1 in d=2','results':results},indent=2),encoding='utf8')
