"""Independent checks of the proved certificates and the failed PSD extension."""
import os
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):os.environ[k]='1'
import json,itertools,time,resource
from pathlib import Path
import numpy as np,mpmath as mp
from dpp import *
rng=np.random.default_rng(33350);rows={};start=time.time()
def adj(a):return a@a-np.trace(a)*a+((np.trace(a)**2-np.trace(a@a))/2)*np.eye(3)
maxerr=0;minr=1e9;maxstarerr=0;minmon=1e9;maxchain=0
for it in range(300):
 q=random_kernel(rng,3,True,'uniform');p,m=probabilities(q);f=np.log(p)
 l=np.array([np.log(p[2]*p[4]/(p[0]*p[6])),np.log(p[1]*p[4]/(p[0]*p[5])),np.log(p[1]*p[2]/(p[0]*p[3]))])
 gamma=f[7]-f[3]-f[5]-f[6]+f[1]+f[2]+f[4]-f[0];r=np.diag(l)-gamma*q
 minr=min(minr,np.linalg.eigvalsh(r)[0]);a=rng.normal(size=(3,3))+1j*rng.normal(size=(3,3));a=(a+a.conj().T)/2
 c=np.einsum('sij,jk->sik',np.linalg.inv(m),a);tr=np.trace(c,axis1=1,axis2=2).real;tr2=np.einsum('sij,sji->s',c,c).real
 dd=-np.sum(p*tr*tr)+2*np.trace(adj(a)@r).real;maxerr=max(maxerr,abs(dd-stats(q,a)[1]))
rows['three_point']={'trials':300,'max_curvature_identity_error':float(maxerr),'min_certificate_eigenvalue':float(minr)}
for n in (3,4,5,6):
 errs=[];chain=[];mgs=[]
 for it in range(100):
  q=random_kernel(rng,n,True,'uniform');c=q[1:,1:];v=q[1:,0];aa=q[0,0].real
  pi,mm=probabilities(c);iv=np.linalg.inv(mm);qt=aa-np.einsum('i,sij,j->s',v.conj(),iv,v).real
  hp=np.log((1-qt)/qt);g=np.einsum('s,sij->ij',pi*hp,iv);mgs.append(np.linalg.eigvalsh(g)[0])
  w=rng.normal(size=n-1)+1j*rng.normal(size=n-1);alpha=rng.normal();a=np.zeros((n,n),complex);a[0,0]=alpha;a[1:,0]=w;a[0,1:]=w.conj()
  qp=alpha-2*np.einsum('i,sij,j->s',w.conj(),iv,v).real
  value=-np.sum(pi*qp*qp/(qt*(1-qt)))-2*np.vdot(w,g@w).real
  errs.append(abs(value-stats(q,a)[1]));hc=stats(c)[0];hcond=hc-np.sum(pi*(qt*np.log(qt)+(1-qt)*np.log(1-qt)));chain.append(abs(hcond-stats(q)[0]))
 rows['star_n%d'%n]=dict(trials=100,max_curvature_identity_error=float(max(errs)),max_chain_rule_error=float(max(chain)),min_monotonicity_matrix_eigenvalue=float(min(mgs)))
# High precision obstruction to a globally PSD exterior matrix.
rows['wedge_obstruction']={}
for n in (5,6,8):
 z=np.load('data/wedge_n%d.npz'%n);results={}
 for dps in (110,160):
  with mp.workdps(dps):
   q=mp_matrix(z['Q']);w=[mp.mpc(str(t.real),str(t.imag)) for t in z['v']];ix=list(itertools.combinations(range(n),2));value=mp.mpc(0);mass=mp.mpf(0);minp=mp.mpf(1)
   for s in range(1<<n):
    b=q.copy()
    for i in range(n):
     if not s>>i&1:b[i,i]-=1
    p=mp.re(mp.det(b))*(-1)**(n-s.bit_count());assert p>0;mass+=p;minp=min(minp,p);iv=b**-1
    v=mp.fsum(mp.conj(w[k])*(iv[i,a]*iv[j,bb]-iv[i,bb]*iv[j,a])*w[l] for k,(i,j) in enumerate(ix) for l,(a,bb) in enumerate(ix))
    value-=p*mp.log(p)*v
   value/=mp.fsum(abs(t)**2 for t in w)
   eig,_=mp.eighe(q,eigvals_only=False)
   results[str(dps)]=dict(rayleigh=mp.nstr(mp.re(value),dps-5),imaginary_residual=mp.nstr(abs(mp.im(value)),8),mass=mp.nstr(mass,10),min_atom=mp.nstr(minp,15),min_eigenvalue=mp.nstr(eig[0],15),max_eigenvalue=mp.nstr(eig[n-1],15))
 skew=np.zeros((n,n),complex)
 for k,(i,j) in enumerate(ix):skew[i,j]=z['v'][k];skew[j,i]=-z['v'][k]
 results['vector_skew_rank']=int(np.linalg.matrix_rank(skew))
 with mp.workdps(160):
  ww={ij:mp.mpc(str(z['v'][k].real),str(z['v'][k].imag)) for k,ij in enumerate(ix)}
  plucker=ww[(0,1)]*ww[(2,3)]-ww[(0,2)]*ww[(1,3)]+ww[(0,3)]*ww[(1,2)]
  results['nonzero_plucker_relation_abs']=mp.nstr(abs(plucker),100)
 rows['wedge_obstruction'][str(n)]=results
 print('wedge',n,results['160']['rayleigh'][:60],flush=True)
# Saved commuting optimized directions: decimal entry matrices, with commutator residual.
rows['commuting_mp']=[]
for n in (3,4,6):
 z=np.load('data/commuting_opt_n%d.npz'%n);q=z['Q'];a=z['A']
 row=dict(n=n,double_score=float(z['value']),commutator_norm=float(np.linalg.norm(q@a-a@q)))
 for dps in (110,160):row[str(dps)]=mp_stats(q,a,dps=dps)
 rows['commuting_mp'].append(row);print('commuting',n,row['160']['second'][:60],flush=True)
rows['elapsed_seconds']=time.time()-start;rows['peak_rss_bytes']=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
Path('data/certificate_audit.json').write_text(json.dumps(rows,indent=2)+'\n')
print(json.dumps({k:v for k,v in rows.items() if k not in ('wedge_obstruction','commuting_mp')},indent=2),flush=True)
