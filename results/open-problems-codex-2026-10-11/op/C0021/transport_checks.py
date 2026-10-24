"""Bounded independent LP and explicit monotone-bijection checks."""
import pathlib,json,time
from fractions import Fraction
P=pathlib.Path(__file__).parent;start=time.monotonic()
LOW_TO_HIGH={0:7,1:5,2:3,4:6}
def value(bits):
 if len(bits)==1:return bits[0]
 m=len(bits)//3
 return int(sum(value(bits[i*m:(i+1)*m]) for i in range(3))>=2)
def transport(bits):
 assert value(bits)==0
 if len(bits)==1:return (1,)
 m=len(bits)//3;children=[bits[i*m:(i+1)*m] for i in range(3)]
 pattern=sum(value(b)<<i for i,b in enumerate(children));target=LOW_TO_HIGH[pattern]
 return sum((transport(b) if not (pattern>>i)&1 and (target>>i)&1 else b for i,b in enumerate(children)),())
out={'date':'2026-10-12','explicit_coupling':[],'lp':[]}
for k in (0,1,2):
 n=3**k;seen=set();total=0;count=0
 for mask in range(1<<n):
  bits=tuple((mask>>i)&1 for i in range(n))
  if value(bits):continue
  y=transport(bits);assert value(y)==1 and all(a<=b for a,b in zip(bits,y))
  assert y not in seen;seen.add(y);count+=1;total+=sum(a!=b for a,b in zip(bits,y))
 assert count==(1<<(n-1));mean=Fraction(total,count);assert mean==Fraction(3,2)**k
 out['explicit_coupling'].append(dict(k=k,inputs_checked=count,mean_distance=str(mean),bijective=True,monotone=True))
 (P/'transport_checks.json').write_text(json.dumps(out,indent=2),encoding='utf8')
try:
 import numpy as np
 from scipy.optimize import linprog
 from scipy.sparse import coo_matrix
 for k in (1,2):
  n=3**k;N=1<<n;fs=np.array([2*value(tuple((mask>>i)&1 for i in range(n)))-1 for mask in range(N)])
  rows=[];cols=[];coeff=[];r=0
  for x in range(N):
   for j in range(n):
    if x&(1<<j):continue
    y=x|(1<<j)
    for s in (1,-1):
     rows.extend([r,r]);cols.extend([y,x]);coeff.extend([s,-s]);r+=1
  A=coo_matrix((coeff,(rows,cols)),shape=(r,N)).tocsr()
  res=linprog(-fs/N,A_ub=A,b_ub=np.full(r,2.),bounds=[(0.,0.)]+[(None,None)]*(N-1),method='highs',options={'time_limit':45})
  assert res.success,res.message
  optimum=-res.fun;influence=float(Fraction(3,2)**k);assert abs(optimum-influence)<1e-8
  out['lp'].append(dict(k=k,variables=N,constraints=r,optimum=optimum,predicted=influence,max_edge_violation=float(max(A@res.x-2))))
  (P/'transport_checks.json').write_text(json.dumps(out,indent=2),encoding='utf8')
except ImportError as e:out['lp_unavailable']=str(e)
out['seconds']=time.monotonic()-start
(P/'transport_checks.json').write_text(json.dumps(out,indent=2),encoding='utf8');print(json.dumps(out,indent=2))
