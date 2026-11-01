import numpy as np
import json
from pathlib import Path
rng=np.random.default_rng(4040)
results=[]
for beta,a in [(0.3,-0.8),(1.,0.),(2.,2.),(4.,0.5)]:
 n=5; samples=10000
 d=np.sqrt(rng.chisquare(beta*(a+np.arange(1,n+1)),size=(samples,n))/beta)
 c=np.sqrt(rng.chisquare(beta*np.arange(1,n),size=(samples,n-1))/beta)
 errors=[]; gaps=[]; traces=[]
 for k in range(samples):
  B=np.diag(d[k])+np.diag(c[k],-1)
  J=B@B.T
  R=np.eye(n)[::-1]
  L=R@B.T@R
  errors.append(np.max(np.abs(np.linalg.eigvalsh(J)-np.linalg.eigvalsh(L@L.T))))
  ev=np.linalg.eigvalsh(J); prev=np.linalg.eigvalsh(J[:-1,:-1])
  gaps.append(min(np.min(prev-ev[:-1]),np.min(ev[1:]-prev)))
  assert np.allclose(J[:-1,:-1],B[:-1,:-1]@B[:-1,:-1].T)
  traces.append(np.trace(J))
 target=n*(a+n); se=np.sqrt(2*target/(beta*samples))
 results.append(dict(beta=beta,a=a,n=n,samples=samples,max_spectral_error=float(max(errors)),min_interlacing_gap=float(min(gaps)),trace_mean=float(np.mean(traces)),trace_target=target,trace_standard_error=se,z_score=float((np.mean(traces)-target)/se)))
Path('numerical_checks.json').write_text(json.dumps(results,indent=2),encoding='utf-8')
print(json.dumps(results,indent=2))
