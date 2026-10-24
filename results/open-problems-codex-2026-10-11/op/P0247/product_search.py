from compute import law
from pathlib import Path
import json,numpy as np,time
p=Path(__file__).parent;out=[];start=time.monotonic()
for m,k,kind in [(3,2,'thickened'),(4,2,'thickened'),(5,2,'thickened'),(6,2,'thickened'),(4,3,'thickened'),(3,4,'thickened'),(4,3,'cartesian'),(6,2,'cartesian')]:
 if time.monotonic()-start>180:break
 n=m*k;adj=[]
 for x in range(n):
  a,b=divmod(x,k)
  if kind=='thickened':neighbors=[((a+s)%m)*k+j for s in [-1,1] for j in range(k)]
  else:neighbors=[((a+s)%m)*k+b for s in [-1,1]]+[a*k+j for j in range(k) if j!=b]
  adj.append(sorted(set(neighbors)))
 v,res=law(adj)
 row=dict(m=m,k=k,kind=kind,n=n,law=v.tolist(),tv=float(abs(v-1/n).sum()/2),projection_law=v.reshape(m,k).sum(axis=1).tolist(),residual=res,sum_error=float(abs(v.sum()-1)))
 out.append(row);p.joinpath('product_search.json').write_text(json.dumps(out,indent=2),encoding='utf-8');print(json.dumps(row),flush=True)
