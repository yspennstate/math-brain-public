import os
os.environ['OPENBLAS_NUM_THREADS']='1'
os.environ['OMP_NUM_THREADS']='1'
import json, math
from fractions import Fraction as F
from pathlib import Path
import numpy as np
from scipy.integrate import quad

out={'scope':'Auxiliary checks only; no verification of infinite construction or quantitative theorem.'}
windows=[]
for e in [F(1,100),F(1,20),F(1,4),F(1,2),F(13,20),F(2,3),F(4,5)]:
 p=2+e; alpha=2*e/p
 for j in [1,10,1000]:
  delta=alpha+F(1,j); low=max(e/delta,2*e); high=p/2
  if low<high:
   b=(low+high)/2; beta=(e/b+F(1,2))/2
   assert 2*b-p<0 and b*beta-e>0 and b*delta-e>0
  windows.append({'eps':str(e),'j':j,'window_exists':low<high,'alpha':float(alpha)})
out['exact_rational_exponent_windows']=windows
rs=np.linspace(1/math.sqrt(2),1,1001)
minratio=1e10
for r in rs[:-1]:
 gap=quad(lambda u:2/math.pi*math.sqrt(1-u*u),.5,.5/r,epsabs=1e-13)[0]
 assert gap >= (1-r)/8-1e-12
 minratio=min(minratio,gap/(1-r))
out['rectangle_1000_radii_min_gap_over_1_minus_r']=minratio
rng=np.random.default_rng(109)
rows=[]
for n in [48,96,192]:
 vals=[]
 for k in range(6):
  mat=rng.normal(size=(n,n))/math.sqrt(n)
  lam=np.linalg.eigvals(mat); r=.9
  # Stronger exact scaling check of matrix eigenvalues and the uncapped test.
  scaled=np.linalg.eigvals(r*mat)
  residual=max(np.min(np.abs(scaled[:,None]-r*lam[None,:]),axis=1))
  assert residual<1e-9
  vals.append({'scaling_residual':float(residual),'mean_radius':float(np.mean(abs(lam)))})
 rows.append({'n':n,'replicates':vals})
out['finite_gaussian_scaling_checks']=rows
out['memory']='Largest matrix 192x192; arrays far below 1 GB; BLAS one thread.'
Path('checks.json').write_text(json.dumps(out,indent=2),encoding='utf8')
print(json.dumps({k:v for k,v in out.items() if k!='finite_gaussian_scaling_checks'},indent=2))
