import numpy as np, json, itertools, time
from pathlib import Path
ROOT=Path(__file__).parent
def law(adj):
 n=len(adj); full=(1<<n)-1
 P=np.zeros((n,n))
 for x,a in enumerate(adj):P[x,a]=1/len(a)
 dp={}; max_residual=0.
 for size in range(n-1,0,-1):
  for S in itertools.combinations(range(n),size):
   mask=sum(1<<x for x in S)
   if size==n-1:
    F=np.zeros((n,n));F[:,next(x for x in range(n) if not(mask>>x&1))]=1
   else:
    rhs=np.zeros((size,n))
    for i,x in enumerate(S):
     for y in adj[x]:
      if not(mask>>y&1):rhs[i]+=P[x,y]*dp[mask|(1<<y)][y]
    A=np.eye(size)-P[np.ix_(S,S)]
    sol=np.linalg.solve(A,rhs)
    max_residual=max(max_residual,float(np.max(abs(A@sol-rhs))))
    F=np.zeros((n,n));F[list(S)]=sol
   dp[mask]=F
 k=dp[1][0]
 return k, max_residual
def circulant(n,steps):return [sorted({(x+s)%n for s in steps}|{(x-s)%n for s in steps}) for x in range(n)]
cases=[]
for n in range(3,11):cases.append((f'C{n}',circulant(n,[1])))
for n in [4,6,8,10]:cases.append((f'K{n}',[[y for y in range(n) if y!=x] for x in range(n)]))
for m in [2,3,4,5]:cases.append((f'K{m},{m}',[list(range(m,2*m)) if x<m else list(range(m)) for x in range(2*m)]))
for n in [6,8,10]:cases.append((f'Circulant({n};1,2)',circulant(n,[1,2])))
cases.append(('cube3',[[x^(1<<i) for i in range(3)] for x in range(8)]))
for m in [3,4,5]:cases.append((f'prism{m}',[[(x//m)*m+(x+1)%m,(x//m)*m+(x-1)%m,(x+m)%(2*m)] for x in range(2*m)]))
if __name__=='__main__':
 out=[]
 for name,adj in cases:
  k,res=law(adj);n=len(adj)
  row=dict(graph=name,n=n,law=k.tolist(),tv=float(abs(k-1/n).sum()/2),residual=res,sum_error=float(abs(k.sum()-1)),min_probability=float(k.min()))
  if name.startswith('C') and not name.startswith('Circulant'):row['cycle_formula_error']=float(max(abs(k[1:]-1/(n-1))))
  out.append(row);print(json.dumps(row),flush=True)
  ROOT.joinpath('computations.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
