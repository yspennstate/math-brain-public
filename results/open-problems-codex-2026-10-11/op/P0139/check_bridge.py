"""Small Monte Carlo normalization check and exact polygon BV translation."""
import json
from pathlib import Path
import numpy as np

seed=13906
rng=np.random.default_rng(seed)
trials=4000
steps=512
u=np.linspace(0.0,1.0,steps+1)
increments=rng.normal(size=(trials,steps,2))/np.sqrt(steps)
B=np.concatenate([np.zeros((trials,1,2)),np.cumsum(increments,axis=1)],axis=1)
W=B-u[None,:,None]*B[:,-1:,:]

def wedge(x,y):
    return x[...,0]*y[...,1]-x[...,1]*y[...,0]

AB=0.5*np.sum(wedge(B[:,:-1,:],B[:,1:,:]),axis=1)
AW=0.5*np.sum(wedge(W[:,:-1,:],W[:,1:,:]),axis=1)
integral=np.sum(wedge((B[:,:-1,:]+B[:,1:,:])/2,B[:,-1:,:]),axis=1)/steps
error=float(np.max(np.abs(AW-(AB-integral))))
assert error<1e-12
second=float(np.mean(AW**2))
standard_error=float(np.std(AW**2,ddof=1)/np.sqrt(trials))
assert abs(second-1/12)<5*standard_error+1/steps
out={'seed':seed,'trials':trials,'steps':steps,
     'polygon_translation_max_error':error,
     'bridge_area_second_moment_estimate':second,
     'continuum_theoretical_second_moment':1/12,
     'estimated_standard_error':standard_error,
     'mean_area':float(np.mean(AW)),
     'qualification':'Finite polygon samples check normalization and BV translation, not the infinite-loop summability theorem.'}
Path('bridge_checks.json').write_text(json.dumps(out,indent=2),encoding='utf8')
print(json.dumps(out,indent=2))
