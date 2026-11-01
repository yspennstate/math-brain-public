"""Optimize h with bounded conditional increments only before f is determined."""
import numpy as np,json,pathlib,time,itertools
from scipy.sparse import coo_matrix
from scipy.optimize import linprog
def value(bits):
 if len(bits)==1:return bits[0]
 m=len(bits)//3
 return int(sum(value(bits[i*m:(i+1)*m]) for i in range(3))>=2)
P=pathlib.Path(__file__).parent;start=time.monotonic();results=[]
for k in (1,2):
 n=3**k;N=1<<n;f=np.array([2*value(tuple((x>>j)&1 for j in range(n)))-1 for x in range(N)])
 rr=[];cc=[];vv=[];row=0;histories=0
 for s in itertools.product(range(3),repeat=n):
  base=sum((1<<j) for j,a in enumerate(s) if a==1);unknown=sum((1<<j) for j,a in enumerate(s) if a==2)
  if f[base]==f[base|unknown]:continue
  histories+=1
  if histories%1024==0 and time.monotonic()-start>180:raise RuntimeError('bounded LP construction cap')
  m=unknown.bit_count();xs=[];sub=unknown
  while True:
   xs.append(base|sub)
   if sub==0:break
   sub=(sub-1)&unknown
  for j,a in enumerate(s):
   if a!=2:continue
   for sign in (1.,-1.):
    for x in xs:
     rr.append(row);cc.append(x);vv.append(sign*(1. if x&(1<<j) else -1.)/(1<<m))
    row+=1
 A=coo_matrix((vv,(rr,cc)),shape=(row,N)).tocsr();del rr,cc,vv
 res=linprog(-f/N,A_ub=A,b_ub=np.ones(row),bounds=[(0.,0.)]+[(None,None)]*(N-1),method='highs',options={'time_limit':45})
 assert res.success,res.message
 optimum=-res.fun;assert abs(optimum-(1.5**k))<1e-8
 r=dict(k=k,variables=N,undetermined_histories=histories,constraints=row,nonzeros=A.nnz,optimum=optimum,expected=1.5**k,max_constraint_violation=float(max(A@res.x-1)),seconds=time.monotonic()-start)
 results.append(r);(P/'relaxed_transport_lp.json').write_text(json.dumps(results,indent=2),encoding='utf8');print(r,flush=True)
