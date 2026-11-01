import math,json
import numpy as np
from scipy.stats import binom
from pathlib import Path
out={}
# Deterministic real-valued generating-function recursion, no simulation used as proof.
rows=[]
for b in [5,9,25]:
 for h in [80,160,320,640]:
  p=1/(b*math.cos(math.pi/(h+2)));mu=b*p;t=1/(128*h*h);x=t;maxratio=0
  for k in range(h):
   x=t+b*math.log1p(p*math.expm1(x));maxratio=max(maxratio,x/((k+2)/(64*h*h)))
  rows.append(dict(b=b,h=h,mu=mu,log_mgf=x,upper=1/(32*h),max_induction_ratio=maxratio))
out['mgf']=rows
# Check every possible band population at j<=35, then sample larger bands.
rows=[]
for b in [5,9,25]:
 minprob=1.;arg=None;cnt=0
 for j in range(8,81):
  values=range(j*j,4*j*j+1) if j<=35 else np.unique(np.linspace(j*j,4*j*j,120,dtype=int))
  for z in values:
   z=int(z);a=max(z,(j+1)**2);end=a+math.isqrt(z)
   assert j*j<=z<=4*j*j
   assert a>= (j+1)**2 and end<=4*(j+1)**2
   prob=binom.sf(a-1,b*z,1/b)-binom.sf(end,b*z,1/b)
   if prob<minprob:minprob=float(prob);arg=[j,z,a,end]
   cnt+=1
 rows.append(dict(b=b,windows=cnt,min_probability=minprob,argmin=arg,proved_lower=math.exp(-30)/8))
out['binomial_windows']=rows
# Direct check of finite-tree spectral formula with sparse adjacency.
from scipy.sparse import coo_matrix
from scipy.sparse.linalg import eigsh
rows=[]
for b,h in [(5,2),(5,4),(9,3)]:
 n=(b**(h+1)-1)//(b-1);v=np.arange(1,n);par=(v-1)//b
 A=coo_matrix((np.ones(2*(n-1)),(np.concatenate([v,par]),np.concatenate([par,v]))),shape=(n,n)).tocsr()
 lam=float(eigsh(A,k=1,which='LA',return_eigenvectors=False)[0]);exact=2*math.sqrt(b)*math.cos(math.pi/(h+2))
 rows.append(dict(b=b,h=h,n=n,computed=lam,formula=exact,absolute_error=abs(lam-exact)))
out['spectral']=rows
Path('numerical_checks.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print('MGF max ratio:',max(x['max_induction_ratio'] for x in out['mgf']))
print('Band minima:',rows if False else out['binomial_windows'])
print('Spectral errors:',out['spectral'])
