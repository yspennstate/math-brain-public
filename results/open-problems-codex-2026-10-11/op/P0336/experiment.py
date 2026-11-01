import numpy as np, scipy, scipy.optimize, json, time
from pathlib import Path
rng=np.random.default_rng(336)
out=[]
for n in [100,300,1000,2000]:
 for rep in range(4):
  a=rng.random((n,2)); b=rng.random((n,2)); b[:,0]+=2
  d=b[None,:,0]-a[:,None,0]; h=b[None,:,1]-a[:,None,1]
  c=h*h/(np.sqrt(d*d+h*h)+d)
  i,j=scipy.optimize.linear_sum_assignment(c)
  xx=a[:,0]; yy=b[j,0]-2; hv=b[j,1]-a[:,1]
  r={'n':n,'rep':rep,'horizontal_corr':float(np.corrcoef(xx,yy)[0,1]),'translation_mse':float(np.mean((xx-yy)**2)),'reflection_mse':float(np.mean((xx+yy-1)**2)),'vertical_mse':float(np.mean(hv*hv)),'n_excess':float(n*np.mean(c[i,j])),'mean_dx':float(np.mean(b[j,0]-xx))}
  out.append(r); print(json.dumps(r),flush=True)
Path('numerics.json').write_text(json.dumps(out,indent=2),encoding='utf8')
