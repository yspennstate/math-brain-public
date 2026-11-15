"""Independent scalar/statistical and objective-gradient audit of the saved result."""
import os
for key in ['OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','VECLIB_MAXIMUM_THREADS']:os.environ[key]='1'
import csv,json,statistics,math,hashlib
from pathlib import Path
import numpy as np
from scipy.special import logsumexp
from experiments import shifts,objective,hardloss,signal
ROOT=Path(__file__).resolve().parents[1]
rows=list(csv.DictReader((ROOT/'data/recovery.csv').open()))
assert len(rows)==672
assert len({(r['suite'],r['L'],r['sigma'],r['n'],r['rep'],r['seed']) for r in rows})==168
assert all(math.isfinite(float(r['relative_squared_error'])) and float(r['relative_squared_error'])>=0 for r in rows)
values={}
for n in [200,2000,20000]:
 for sigma in ['0.5','1.5']:
  for method in ['marginal','quasi_raw','quasi_post_power','quasi_constrained']:
   v=[float(r['relative_squared_error']) for r in rows if r['L']=='5' and r['sigma']==sigma and r['n']==str(n) and r['method']==method]
   values[f'{sigma}/{n}/{method}']=statistics.median(v)
# Independent scalar log-log regression, avoiding numpy.polyfit.
mr=list(csv.DictReader((ROOT/'data/moment_scaling.csv').open()))
by={s:[float(r['squared_error']) for r in mr if float(r['sigma'])==s] for s in [2,3,4,6]}
x=[math.log(s) for s in by];y=[math.log(statistics.mean(v)) for v in by.values()]
xm,ym=statistics.mean(x),statistics.mean(y)
slope=sum((a-xm)*(b-ym) for a,b in zip(x,y))/sum((a-xm)**2 for a in x)
assert abs(slope-json.loads((ROOT/'data/summary.json').read_text())['moment_loglog_slope_sigma_ge_2'])<1e-12
# Independent centered finite differences of the exact marginal objective.
rg=np.random.default_rng(57999);Y=rg.normal(size=(41,7));theta=rg.normal(size=7);sigma=1.3
C=np.einsum('ij,kj->ik',Y,shifts(theta))/sigma**2
W=np.exp(C-logsumexp(C,axis=1,keepdims=True))
A=np.einsum('ik,ij->kj',W,Y)/len(Y)
grad=(theta-sum(np.roll(A[s],-s) for s in range(7)))/sigma**2
finite=[]
for j in range(7):
 h=np.zeros(7);h[j]=1e-5
 finite.append((objective(Y,theta+h,sigma)-objective(Y,theta-h,sigma))/(2e-5))
assert np.max(np.abs(grad-finite))<1e-8
# One scalar direct mixture evaluation, with Gaussian constants removed in the same way.
z=[]
for row in Y:
 vals=[sum(float(row[j])*float(np.roll(theta,s)[j]) for j in range(7))/sigma**2 for s in range(7)]
 a=max(vals);z.append(a+math.log(sum(math.exp(v-a) for v in vals)))
direct=sum(float(v*v) for v in theta)/(2*sigma**2)-statistics.mean(z)+math.log(7)
assert abs(direct-objective(Y,theta,sigma))<1e-12
# Every retained source is text, including control-character cleanup after PDF extraction.
for p in (ROOT/'sources').iterdir():
 assert p.suffix in ['.txt','.json']
 assert not p.read_bytes().startswith(b'%PDF')
 p.read_text()
metadata={'dataset_count':168,'fit_count':672,'independent_slope':slope,'marginal_gradient_max_error':float(np.max(np.abs(grad-finite))),'direct_objective_error':abs(direct-objective(Y,theta,sigma)),'selected_medians':values,'source_text_check':'all retained source files decode as text; no PDF signatures'}
(ROOT/'data/final_audit.json').write_text(json.dumps(metadata,indent=2)+'\n')
print({k:v for k,v in metadata.items() if k!='selected_medians'})
