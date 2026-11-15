"""Read saved PMFs; recompute diagnostics without BLAS dot products."""
from common import log,memory_check
import json,csv,resource
import numpy as np
mom=np.load('moments.npz')['moments'];summary={}
for k,name in enumerate(('S','C','QC')):
    with open(f'pmf/{name}/offsets.json') as f:offset=json.load(f)
    worst=np.zeros(4);worst_mass=0.;finite=True
    for n in range(2,len(offset)):
        p=np.load(f'pmf/{name}/{n:03}.npy');lo=offset[n]
        x=np.arange(lo,lo+len(p),dtype=float);mu=float(np.sum(p*x));d=x-mu
        vals=np.array([mu,*[float(np.sum(p*d**r)) for r in (2,3,4)]])
        rel=abs(vals-mom[n,k])/np.maximum(1,abs(mom[n,k]));worst=np.maximum(worst,rel)
        worst_mass=max(worst_mass,abs(float(np.sum(p))-1));finite=finite and bool(np.all(np.isfinite(p)) and np.all(p>=0))
        if n==200:summary[name]={'n':n,'min':lo,'max':lo+len(p)-1,'moments':list(map(float,vals))}
        memory_check()
    summary[name].update(worst_relative_moment_errors=worst.tolist(),worst_mass_error=worst_mass,all_finite_nonnegative=finite)
with open('pmf_audit.json','w') as f:json.dump(summary,f,indent=2)
log('Independent saved-PMF audit: '+json.dumps(summary)+'; audit RSS bytes='+str(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss))
