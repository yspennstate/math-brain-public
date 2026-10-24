"""Test the stronger linear-operator form of capped Hall at one fixed W."""
import itertools,json
from pathlib import Path
import numpy as np
from capped_probe import frame,PAIRS,TRIPLES,INC

Q=frame(); W=Q[:,:2]; V=Q[:,2:]
vp=list(itertools.combinations(range(4),2))
Z=np.array([[np.linalg.det(V[np.ix_(p,ij)]) for ij in vp] for p in PAIRS])
TS=[np.array([[np.linalg.det(np.column_stack((V[:,i],V[:,j],W[:,s]))[list(m)]) for i,j in vp] for m in TRIPLES]) for s in range(2)]
effects=sum(np.einsum('mi,mj->mij',T.conj(),T) for T in TS)
zeffects=np.einsum('pi,pj->pij',Z.conj(),Z)
worst={'minimum_eigenvalue':1.0}
violations=0
for start in range(0,1<<20,8192):
 masks=np.arange(start,min(start+8192,1<<20),dtype=np.uint32)
 bits=((masks[:,None]>>np.arange(20))&1).astype(float)
 A=np.einsum('bp,pij->bij',np.minimum(bits@INC,2),zeffects)-np.einsum('bm,mij->bij',bits,effects)
 ev=np.linalg.eigvalsh(A)
 k=int(np.argmin(ev[:,0]))
 if ev[k,0]<worst['minimum_eigenvalue']:
  mask=int(masks[k]); F=[TRIPLES[i] for i in range(20) if mask>>i&1]
  worst={'minimum_eigenvalue':float(ev[k,0]),'mask':mask,'family':F,'eigenvalues':ev[k].tolist()}
 violations+=int(np.sum(ev[:,0]<-1e-9))
out={'worst':worst,'violations':violations}
print(json.dumps(out,indent=2)); Path(__file__).with_name('psd_probe_output.json').write_text(json.dumps(out,indent=2)+'\n')
