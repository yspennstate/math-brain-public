import json, numpy as np
from pathlib import Path
# imports avoid executing exploratory enumeration
exec(Path(__file__).with_name('explore_levels.py').read_text().split('out={}')[0])
out={}
for n in range(1,5):
 N=1<<n;tt=1-2*((np.arange(1<<N,dtype=np.int64)[:,None]>>np.arange(N)[None,:])&1); ww=fwht(tt); absw=abs(ww)
 mask=np.all((absw&(absw-1))==0,axis=1); W=ww[mask]; noninteger=np.zeros(len(W),dtype=bool); witnesses=[]
 for r in range(n+1):
  part=np.where(abs(W)==1<<r,W,0); vals=fwht(part); fail=np.any(vals%N!=0,axis=1);noninteger|=fail
  if fail.any():
   j=int(np.flatnonzero(fail)[0]);witnesses.append({'r':r,'W':W[j].tolist(),'band_numer':vals[j].tolist()})
 out[n]={'pure_power_count':len(W),'bad_count':int(noninteger.sum()),'witnesses':witnesses[:1]}
print(json.dumps(out,indent=2))
