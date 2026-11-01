import numpy as np,json
from pathlib import Path
exec(Path(__file__).with_name('explore_levels.py').read_text().split('out={}')[0])
x=np.arange(32); t=[(x>>j)&1 for j in range(5)]
f=1-2*(((t[3]==t[0]*t[1])&(t[4]==t[0]*t[2])).astype(np.int64))
W=fwht(f)[0]; bands={}
for m in sorted(set(abs(W))-{0}):
 vals=fwht(np.where(abs(W)==m,W,0))[0]
 bands[str(m)]={'count':int(np.sum(abs(W)==m)),'physical_values': sorted(set((vals/32).tolist()))}
I=int(sum(int(z)**2 * j.bit_count() for j,z in enumerate(W)))/1024
H=-sum((z/32)**2*np.log2((z/32)**2) for z in W if z)
print(json.dumps({'W':W.tolist(),'bands':bands,'I':I,'H':H,'ratio':H/I},indent=2))
