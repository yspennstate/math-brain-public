"""Small independent checks. Floating point evidence, never an asymptotic proof."""
import os
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','VECLIB_MAXIMUM_THREADS','MKL_NUM_THREADS'):os.environ[k]='1'
import numpy as np
import csv,json,resource
from fractions import Fraction as Q
from pathlib import Path
assert os.getpriority(os.PRIO_PROCESS,0)>=10
root=Path(__file__).resolve().parents[1]
rng=np.random.default_rng(103)
rows=[]; checks=[]
for p in [101,257,509,1009,2017,4093,10009]:
 assert p%4==1 and all(p%d for d in range(2,int(p**.5)+1))
 chi=np.full(p,-1,dtype=np.int64);chi[0]=0
 chi[(np.arange(1,p,dtype=np.int64)**2)%p]=1
 residues=np.flatnonzero(chi==1)
 L=int(p**(17/32));j=np.arange(L)
 T=chi[(j[:,None]-j[None,:])%p]
 E=T/np.sqrt(p)
 phi=np.vstack([np.ones(L)/np.sqrt(p),np.sqrt(2/p)*np.exp(-2j*np.pi*np.outer(residues,j)/p)])
 # einsum keeps the direct construction independent of the character formula.
 gram=np.einsum('ri,rj->ij',phi.conj(),phi)
 error=float(np.max(np.abs(gram-np.eye(L)-E)));assert error<1e-11
 e=np.linalg.eigvalsh(E);norm=max(abs(e));cond=np.sqrt((1+e[-1])/(1+e[0]))
 bordered=np.zeros((L+1,L+1));bordered[:L,:L]=E;bordered[-1,:L]=bordered[:L,-1]=1/np.sqrt(p)
 eb=np.linalg.eigvalsh(bordered);bnorm=max(abs(eb));bcond=np.sqrt((1+eb[-1])/(1+eb[0]))
 assert bnorm<=norm+np.sqrt(L/p)+1e-12
 assert abs(np.linalg.norm(np.abs(bordered),2)-L/np.sqrt(p))<1e-11
 # Fourier integral: degree at most 2(L-1), so this trapezoid quadrature is exact algebraically.
 z=rng.normal(size=L)+1j*rng.normal(size=L);z/=np.linalg.norm(z)
 theta=np.arange(4*L)/(4*L);hs=np.arange(1,L)
 symbol=2*np.real(np.einsum('h,ht->t',chi[hs],np.exp(2j*np.pi*hs[:,None]*theta)))
 P=np.einsum('j,jt->t',z,np.exp(2j*np.pi*j[:,None]*theta))
 qerr=abs(np.einsum('i,ij,j->',z.conj(),T,z)-np.mean(symbol*abs(P)**2));assert qerr<1e-10
 # Independent row-energy identity and block-Abel inequality with actual short sums.
 u=np.einsum('j,nj->n',z,np.exp(-2j*np.pi*np.outer(np.arange(p),j)/p));w=abs(u)**2
 weighted=np.dot(chi,w)/p
 assert abs(weighted-np.einsum('i,ij,j->',z.conj(),E,z))<1e-11
 variation=float(np.sum(np.abs(np.roll(w,-1)-w)))
 assert variation<=4*np.pi*(L-1)*np.linalg.norm(z)**2+1e-9
 blocks=np.array_split(np.arange(p),L);Kmin=min(map(len,blocks));Kmax=max(map(len,blocks))
 partial_max=max(np.max(np.abs(np.cumsum(chi[b]))) for b in blocks)
 abel_actual=partial_max*sum(w[b[-1]]+np.sum(np.abs(np.diff(w[b]))) for b in blocks)/p
 abstract=partial_max*(1/Kmin+8*np.pi*(L-1)/p)*np.linalg.norm(z)**2
 assert abs(weighted)<=abel_actual+1e-10 and abel_actual<=abstract+1e-10
 # Affine labels, both residue and nonresidue step, including modular wraparound.
 for d in [2,int(np.flatnonzero(chi==-1)[0])]:
  labels=(p-2+d*j)%p
  assert len(set(labels))==L
  assert np.array_equal(chi[(labels[:,None]-labels[None,:])%p],chi[d]*T)
 rows.append({'p':p,'L':L,'finite_norm':float(norm),'bordered_norm':float(bnorm),'finite_condition':float(cond),'bordered_condition':float(bcond),'direct_gram_error':error,'quadrature_error':float(qerr)})
 checks.append({'p':p,'L':L,'row_energy_error':float(abs(weighted-np.einsum('i,ij,j->',z.conj(),E,z))),'variation':variation,'block_abel_actual':float(abel_actual),'abstract_abel_bound':float(abstract)})
 print(rows[-1],flush=True)
rho=Q(1,32)
assert Q(2,3)*Q(9,16)-Q(3,8)==0
assert Q(2,3)*(-rho)+rho/3==-rho/3
assert (Q(9,16)-rho)/2-Q(5,16)==-Q(1,32)-rho/2
with (root/'data'/'interval_checks.csv').open('w') as f:
 writer=csv.DictWriter(f,fieldnames=list(rows[0]));writer.writeheader();writer.writerows(rows)
(root/'data'/'verification.json').write_text(json.dumps({'nice':os.getpriority(os.PRIO_PROCESS,0),'threads':1,'peak_rss_bytes':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,'rows':rows,'block_checks':checks,'exponents':'exact fractions passed'},indent=2))
