import numpy as np
from scipy.optimize import linprog
from itertools import combinations
import json, time, sys

def setup(n=6,r=2):
 levels=[list(combinations(range(n),k)) for k in [r,r+1,r+2]]
 sets=sum(levels,[]); lookup={s:k for k,s in enumerate(sets)}
 diamonds=[(s,tuple(j)) for s in levels[0] for j in combinations([i for i in range(n) if i not in s],2)]
 D=np.zeros((len(sets),len(diamonds)))
 for k,(s,j) in enumerate(diamonds):
  D[lookup[s],k]=1;D[lookup[tuple(sorted(s+j))],k]=1
  for i in j: D[lookup[tuple(sorted(s+(i,)))],k]=-1
 return levels,diamonds,D

def laws(Q,r=2):
 n=Q.shape[0]; levels,diamonds,D=setup(n,r)
 p=[]
 for k,ls in enumerate(levels):
  if k==1:
   p.append(np.array([abs(np.linalg.det(Q[np.ix_(s,list(range(r))+[r])]))**2+abs(np.linalg.det(Q[np.ix_(s,list(range(r))+[r+1])]))**2 for s in ls]))
  else: p.append(np.array([abs(np.linalg.det(Q[np.ix_(s,list(range(r+k)))]))**2 for s in ls]))
 return p,np.concatenate([p[0],-p[1],p[2]])

def scan(count=1000,complex_=False,seed=4004):
 rng=np.random.default_rng(seed); levels,diamonds,D=setup(); worst=0
 st=time.time()
 for k in range(count):
  G=rng.normal(size=(6,6))+(1j*rng.normal(size=(6,6)) if complex_ else 0)
  Q=np.linalg.qr(G)[0];p,b=laws(Q)
  result=linprog(np.zeros(len(diamonds)),A_eq=D,b_eq=b,bounds=(0,None),method='highs')
  if not result.success:
   print('FAILED',k,result.message,flush=True);np.savez('creative-lyons-20260915/computations/C004/failed.npz',Q=Q,b=b);return
  if k%100==0:print(k,'OK',time.time()-st,flush=True)
 print('ALL FEASIBLE',count,complex_,flush=True)

if __name__=='__main__':scan(int(sys.argv[1]) if len(sys.argv)>1 else 1000,'complex' in sys.argv)
