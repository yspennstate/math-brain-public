"""Independent finite-matrix check at beta=1; not Mo contour evaluation."""
import os
os.environ.update(OMP_NUM_THREADS='1',OPENBLAS_NUM_THREADS='1',VECLIB_MAXIMUM_THREADS='1')
import numpy as np
from scipy.linalg import eigh_tridiagonal
from pathlib import Path
import csv,time,json,resource
assert os.getpriority(os.PRIO_PROCESS,0)>=10
root=Path(__file__).resolve().parents[1]
lookup={(float(r['t']),float(r['w'])):float(r['pde_n2400']) for r in csv.DictReader((root/'data/pde_comparison.csv').open()) if r['beta']=='1' and r['w']!='inf'}
rng=np.random.default_rng(410013)
rows=[];start=time.time();trials=2500
for N in [256,1024,262144]:
 M=N+1
 keep=N if N<=1024 else int(np.ceil(20*N**(1/3)))
 counts={w:np.zeros(15,dtype=int) for w in [-2.,0.,2.]}
 ts=np.arange(-4.,3.01,.5)
 for trial in range(trials):
  diagchi=rng.chisquare(M-np.arange(keep))
  subchi=np.zeros(keep)
  subchi[:min(keep,N-1)]=rng.chisquare(N-1-np.arange(min(keep,N-1)))
  diag=diagchi+subchi
  off=np.sqrt(subchi[:-1]*diagchi[1:])
  for w in counts:
   ell=2-w*(4/N)**(1/3)
   d=diag.copy();d[0]+=(ell-1)*diagchi[0]
   largest=eigh_tridiagonal(d,off,select='i',select_range=(keep-1,keep-1),check_finite=False,eigvals_only=True)[0]/M
   scaled=(largest-4)*(N/4)**(2/3)
   counts[w]+=scaled<=ts
 for w in counts:
  for t,k in zip(ts,counts[w]):
   phat=float(k/trials);p=lookup[(float(t),w)]
   rows.append({'N':N,'M':M,'retained_rows':keep,'trials':trials,'t':t,'w':w,'matrix_cdf':phat,'pde':p,'difference':phat-p,'binomial_standard_error':float(np.sqrt(phat*(1-phat)/trials)),'is_Mo_evaluation':False})
 print('N',N,'elapsed_seconds',round(time.time()-start,2),flush=True)
with (root/'data/wishart_comparison.csv').open('w') as f:
 writer=csv.DictWriter(f,fieldnames=rows[0]);writer.writeheader();writer.writerows(rows)
summary={'seed':410013,'trials_per_N_per_w':trials,'N':[256,1024,262144],'w':[-2,0,2],'grid_points':len(rows),'seconds':time.time()-start,'maxrss_bytes_macos':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,'max_discrepancy_by_N':{str(n):max(abs(r['difference']) for r in rows if r['N']==n) for n in [256,1024,262144]},'not_a_Mo_formula_evaluation':True,'truncation_not_rigorously_bounded':True}
(root/'data/wishart_summary.json').write_text(json.dumps(summary,indent=2));print(json.dumps(summary,indent=2))
