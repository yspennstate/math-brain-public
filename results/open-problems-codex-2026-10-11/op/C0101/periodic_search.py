"""Bounded finite-period witness search. Feasibility is exact-checked;
solver infeasibility is only evidence. Never infer global maximality."""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import numpy as np,json,time
from scipy.optimize import milp,Bounds,LinearConstraint
R=Path(__file__).parent
start=time.time();points=list(product(range(2),repeat=3));lookup={x:i for i,x in enumerate(points)}
L=np.zeros((8,8),dtype=int)
for x,i in lookup.items():
 L[i,i]-=6
 for j in range(3):
  for s in [-1,1]:
   y=list(x);y[j]=(y[j]+s)%2;L[i,lookup[tuple(y)]]+=1
def q(A,x):return sum(F(A[i][j],2)*x[i]*x[j] for i in range(3) for j in range(3))
def solve(A,phase):
 c=[]
 for x in points:
  k=F(0)
  for j in range(3):
   for s in [-1,1]:
    y=list(x);y[j]+=s;res=tuple(v%2 for v in y)
    off=q(A,y)-q(A,res)+sum(phase[j]*(y[j]-res[j]) for j in range(3))
    assert off.denominator==1
    k+=off
  c.append(int(k))
 low=np.full(8,-np.inf);high=np.full(8,np.inf);low[0]=high[0]=0
 result=milp(np.zeros(8),integrality=np.ones(8),bounds=Bounds(low,high),constraints=LinearConstraint(L,np.full(8,-np.inf),5-np.array(c)),options={'time_limit':1})
 rec={'A':[[str(v) for v in row] for row in A],'linear_phase':[str(v) for v in phase],'solver_status':int(result.status),'trace':str(sum(A[i][i] for i in range(3))),'separable_criterion':sum(-(-A[i][i].numerator//A[i][i].denominator) for i in range(3))<=5 if all(A[i][j]==0 for i in range(3) for j in range(3) if i!=j) else None}
 if result.x is not None:
  z=[round(float(v)) for v in result.x]
  heights=[sum(int(L[i,j])*z[j] for j in range(8))+c[i] for i in range(8)]
  assert max(heights)<=5
  rec.update(witness_values=z,laplacian_values=heights,exact_verified=True)
 return rec
cases=[]
# diagonal half-integral curvatures near the trace ceiling; then genuine mixed terms
for a,b,c in [(F(3,2),F(3,2),F(3,2)),(F(1),F(3,2),F(2)),(F(1,2),F(1,2),F(7,2)),(F(1),F(1),F(3)),(F(0),F(0),F(5)),(F(1,2),F(3,2),F(5,2))]:
 cases.append([[a,F(0),F(0)],[F(0),b,F(0)],[F(0),F(0),c]])
for u,v,w in product([F(0),F(1,2)],repeat=3):
 cases.append([[F(1),u,v],[u,F(1),w],[v,w,F(2)]])
out={'period':2,'dimension':3,'threshold':5,'bounds_on_g_in_fundamental_cell':'unbounded, gauge g(0)=0','cases':[solve(A,phase) for A in cases for phase in product([F(0),F(-1,2)],repeat=3)],'elapsed_seconds':time.time()-start}
(R/'periodic_phase_results.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print('cases',len(out['cases']),'feasible',sum(x.get('exact_verified',False) for x in out['cases']),'seconds',out['elapsed_seconds'],flush=True)
