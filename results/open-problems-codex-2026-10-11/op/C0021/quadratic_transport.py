"""Exact finite quadratic transport optimum using an assignment and integer dual certificate."""
import pathlib,json,time
import numpy as np
from scipy.optimize import linear_sum_assignment
from fractions import Fraction
P=pathlib.Path(__file__).parent;start=time.monotonic();results=[]
def f(x):
 if len(x)==1:return x[0]
 m=len(x)//3;return int(sum(f(x[i*m:(i+1)*m]) for i in range(3))>=2)
for k in (1,2):
 n=3**k;lo=[];hi=[]
 for x in range(1<<n):
  (hi if f(tuple((x>>j)&1 for j in range(n))) else lo).append(x)
 N=len(lo);assert N==len(hi)
 cost=np.array([[(x^y).bit_count()**2 for y in hi] for x in lo],dtype=np.int64)
 ii,jj=linear_sum_assignment(cost);assert np.array_equal(ii,np.arange(N));assert sorted(jj.tolist())==list(range(N))
 assigned=cost[ii,jj];v=np.zeros(N,dtype=np.int64)
 # Exact difference-constraint dual reconstruction. No floating LP dual is trusted.
 for it in range(N):
  nextv=np.minimum(v,(v[jj,None]+cost-assigned[:,None]).min(axis=0))
  if np.array_equal(v,nextv):break
  v=nextv
 else:raise RuntimeError('No finite feasible assignment dual found')
 u=assigned-v[jj]
 slack=cost-u[:,None]-v[None,:]
 assert np.all(slack>=0)
 primal=int(assigned.sum());dual=int(u.sum()+v.sum());assert primal==dual
 cert=dict(k=k,bits=n,low=lo,high=hi,assignment=jj.tolist(),row_potentials=u.tolist(),column_potentials=v.tolist(),total_cost=primal,dual_sum=dual)
 (P/f'quadratic_transport_certificate_{k}.json').write_text(json.dumps(cert),encoding='utf8')
 mean=Fraction(primal,N);r=dict(k=k,class_size=N,squared_transport_cost=str(mean),decimal=float(mean),min_integer_dual_slack=int(slack.min()),dual_rounds=it+1,seconds=time.monotonic()-start)
 results.append(r);(P/'quadratic_transport_results.json').write_text(json.dumps(results,indent=2),encoding='utf8');print(r,flush=True)
