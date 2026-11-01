"""Floating-point locator for the exact certificate; no proof claims."""
import json
from pathlib import Path
import numpy as np
from scipy.linalg import eigvalsh
from search import data,best_tree
rng=np.random.default_rng(659151)
out=Path(__file__).resolve().parent
best=-100
for it in range(4000):
 B=rng.integers(-6,7,size=(4,4));B[2]=B[1]+B[3]
 d=int(rng.integers(3,70));eps=1e-6
 L=(B@B.T+eps*np.eye(4))/d;K=np.linalg.solve(np.eye(4)+L,L)
 if np.linalg.eigvalsh(K)[1]<.001:continue
 try:p,s,R,F,F2,Fc=data(K)
 except (np.linalg.LinAlgError,ValueError):continue
 e2=eigvalsh(F2-R)[0];ec=eigvalsh(Fc-R)[0];ef=eigvalsh(F-R)[0]
 if e2<-.1 and ec<-.01 and ef>.03:
  et,tree=best_tree(p,s,R)
  print('candidate',it,'full',ef,'degree2',e2,'count',ec,'tree',et,flush=True)
  if et>best:
   best=et
   root,child,grand,leaves,FT=tree
   rec=dict(B=B.tolist(),d=d,eps=eps,K=K.tolist(),ef=ef,e2=e2,ec=ec,et=et,root=root,child=child,grand=grand,leaves=leaves)
   (out/'rank3_candidate.json').write_text(json.dumps(rec,indent=2))
   if et>.04:break
 if it%100==0:print('progress',it,e2,ec,flush=True)
