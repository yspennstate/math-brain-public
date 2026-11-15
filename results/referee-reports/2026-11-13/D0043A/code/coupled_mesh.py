"""Coupled weighted-Brownian mesh and boundary checks for S_beta,1."""
import os
for key in ['OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','VECLIB_MAXIMUM_THREADS','MKL_NUM_THREADS']:
    os.environ[key]='1'
import json,resource
from pathlib import Path
import numpy as np
from models import profile,bottom

assert os.getpriority(os.PRIO_PROCESS,0)>=10
rng=np.random.default_rng(431303);output=[]
for beta in [1,2,4]:
    differences=[];boundaries=[]
    for draw in range(96):
        h=.0125;n=10240;t=h*np.arange(1,n+1)
        d,e,_=profile(n,beta,rng,noise='gaussian',h=h)
        dw=(d-2/h**2-t**(1/3))*h
        fine=bottom(d,e)
        hc=2*h;tc=t[1::2]
        dc=2/hc**2+tc**(1/3)+dw.reshape(-1,2).sum(axis=1)/hc
        coarse=bottom(dc,np.full(len(dc)-1,-1/hc**2))
        short=bottom(d[:n//2],e[:n//2-1])
        differences.append(coarse-fine);boundaries.append(short-fine)
    differences=np.array(differences);boundaries=np.array(boundaries)
    output.append(dict(beta=beta,draws=96,h_fine=h,h_coarse=hc,L_long=128,L_short=64,
        mesh_mean=differences.mean(axis=0).tolist(),mesh_rms=np.sqrt(np.mean(differences**2,axis=0)).tolist(),
        boundary_max=np.max(abs(boundaries),axis=0).tolist()))
print(json.dumps(output,indent=2))
Path('data/coupled_mesh.json').write_text(json.dumps(output,indent=2)+'\n')
print('maxrss_bytes',resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
