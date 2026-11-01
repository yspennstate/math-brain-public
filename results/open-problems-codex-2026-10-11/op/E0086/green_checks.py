from pathlib import Path
import numpy as np,json
from scipy.sparse import coo_matrix
from scipy.sparse.linalg import spsolve
out=[]
for R in [5,10,20]:
 pts=[(x,y) for x in range(-R,R+1) for y in range(-R,R+1) if x*x+y*y<=R*R];ind={p:i for i,p in enumerate(pts)};dim=len(pts);rows=[];cols=[];vals=[]
 for p,i in ind.items():
  rows.append(i);cols.append(i);vals.append(1.)
  x,y=p
  for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
   q=(x+dx,y+dy)
   if q in ind:rows.append(i);cols.append(ind[q]);vals.append(-.25)
 A=coo_matrix((vals,(rows,cols)),shape=(dim,dim)).tocsr();i0=ind[(0,0)];rhs=np.zeros(dim);rhs[i0]=1;col0=spsolve(A,rhs)
 for h in [(1,0),(2,0),(3,1)]:
  ih=ind[h];rhs=np.zeros(dim);rhs[ih]=1;colh=spsolve(A,rhs);schur=col0[i0]-colh[i0]*col0[ih]/colh[ih]
  keep=np.array([i for i in range(dim) if i!=ih]);B=A[keep,:][:,keep];k0=int(np.where(keep==i0)[0][0]);rhs=np.zeros(len(keep));rhs[k0]=1;direct=spsolve(B,rhs)[k0]
  error=abs(schur-direct);symerror=abs(colh[i0]-col0[ih]);assert error<1e-10 and symerror<1e-10 and direct>=1
  out.append({'R':R,'h':h,'states':dim,'schur':float(schur),'direct_killed_green':float(direct),'error':float(error),'symmetry_error':float(symerror)})
Path('green_checks.json').write_text(json.dumps(out,indent=2));print('nine sparse Green checks passed; max error',max(r['error'] for r in out))
