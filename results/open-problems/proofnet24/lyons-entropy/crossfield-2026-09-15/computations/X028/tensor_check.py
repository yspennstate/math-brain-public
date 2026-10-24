"""Finite deterministic self-checks of the proposed tensor-power form."""
import importlib.util,json
from pathlib import Path
import numpy as np
spec=importlib.util.spec_from_file_location('probe','computations/X016/probe.py');m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
I=np.eye(3);om=np.exp(2j*np.pi/3);F=np.array([[om**(i*j) for j in range(3)] for i in range(3)])/np.sqrt(3)
z=np.array([0,1,1j,-1+.5j,2-1j,.5+.75j]);generic=m.parseval(np.column_stack((np.ones(6),z,z*z)))
frames=[('generic',generic),('two_bases',np.vstack((I,F))/np.sqrt(2)),('block',m.parseval(np.array([[1,0,0],[0,1,0],[0,0,1],[1,1,0],[1,1j,0]],complex)))]
out=[]
for label,v in frames:
 t=np.sum(abs(v)**2,axis=1);n=v/np.sqrt(t)[:,None];lam=abs(n@n.conj().T)**2;np.fill_diagonal(lam,1.)
 fv=m.qmat(lambda a:sum(t*np.real(np.einsum('ij,jk,ik->i',n,a,n.conj()))**2))
 row={'frame':label,'tp':[]}
 for k in [1,2,3,4,8,16,32]:
  def qk(a):
   na=n@a@n.conj().T;x=np.real(np.diag(na));return .5*np.sum(t[:,None]*t[None,:]*lam**k*(x[:,None]*x[None,:]-abs(na)**2)).real
  Q=m.qmat(qk);gap=fv/(k+1)-Q;val,vec=np.linalg.eigh(gap)
  row['tp'].append({'k':k,'min_gap':val[0].item(),'max_Q':np.linalg.eigvalsh(Q)[-1].item()})
 out.append(row)
Path('computations/X028/tensor_results.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
