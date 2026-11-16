import json
import numpy as np
from stratum import *
rng=np.random.default_rng(20261113)
errs=np.zeros(3); mineig=1; minweight=1; maxgap=0
for k in range(5000):
    U=frame(rng.uniform(-np.pi,np.pi,5))
    r=10**rng.uniform(-5,0) if k%2 else rng.uniform(.001,1)
    a=tmax(r,U)*rng.uniform(.001,1)
    b=a*r
    x=closed(a,b,U); y=direct(a,b,U); z=pair_terms(a,b,U)
    errs=np.maximum(errs,[max(abs(x-y)),max(abs(x-z)),abs(ratio(x)-ratio(y))])
    lam,G,Pi,L,weights=matrices(a,b,U)
    ev=np.linalg.eigvalsh(L)
    assert min(weights)>-1e-14
    assert max(abs(ev[-2:]-lam))<2e-14
    assert abs(ev[-3]-(lam-b))<2e-14
    assert b>0 and ev[-3]<lam
    assert abs(sum(weights)-1)<2e-14
    mineig=min(mineig,ev[0]); minweight=min(minweight,min(weights)); maxgap=max(maxgap,abs(ev[-1]-ev[-2]))
print(json.dumps(dict(samples=5000,max_abs_closed_vs_trace=float(errs[0]),max_abs_closed_vs_pair=float(errs[1]),max_ratio_discrepancy=float(errs[2]),min_eigenvalue=float(mineig),min_weight=float(minweight),max_top_split=float(maxgap)),indent=2))
