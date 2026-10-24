import numpy as np,json
from explore_derivative import fwht,entropy
out=[]
for n in range(1,5):
 N=1<<n; hs=[]
 for start in range(0,1<<N,512):
  codes=np.arange(start,min(start+512,1<<N),dtype=np.int64)
  fs=1-2*((codes[:,None]>>np.arange(N))&1)
  a=fwht(fs)/N; hs.extend(entropy(a*a).tolist())
 c=fwht(np.array(hs))/(1<<N)
 summary={}
 for j in range(N+1):
  ids=np.array([u for u in range(1<<N) if u.bit_count()==j]); vals=c[ids]
  nz=vals[np.abs(vals)>1e-9]
  if len(nz):summary[j]={'min':float(nz.min()),'max':float(nz.max()),'positive':int((nz>0).sum()),'negative':int((nz<0).sum())}
 out.append({'n':n,'coefficient_by_order':summary})
print(json.dumps(out,indent=2))
