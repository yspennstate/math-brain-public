#!/usr/bin/env python3
"""Independent small-box quenched averaging against exact urn enumeration."""
import os
os.environ['OPENBLAS_NUM_THREADS']='1'
os.environ['OMP_NUM_THREADS']='1'
os.environ['VECLIB_MAXIMUM_THREADS']='1'
if os.getpriority(os.PRIO_PROCESS,0)<10:os.setpriority(os.PRIO_PROCESS,0,10)
import json, math
from pathlib import Path
import numpy as np
from fractions import Fraction as F

root=Path(__file__).resolve().parents[1]
exact=json.loads((root/'data/finite_certificate_checks.json').read_text())
rng=np.random.default_rng(13799881)
n=50000
points=[(x,y) for x in (-1,0,1) for y in (-1,0,1)]
index={x:i for i,x in enumerate(points)}
env=rng.dirichlet([.55,.5,.5,.5],size=(n,9))
P=np.zeros((n,9,9));f=np.zeros((n,9))
for i,x in enumerate(points):
    for j,e in enumerate(((1,0),(0,1),(-1,0),(0,-1))):
        y=(x[0]+e[0],x[1]+e[1])
        if y in index:P[:,i,index[y]]=env[:,i,j]
        elif y[0]>=2:f[:,i]=env[:,i,j]
dist=np.zeros((n,9));dist[:,index[(0,0)]]=1
front=np.zeros(n);rows=[]
for k in range(1,9):
    front+=np.sum(dist*f,axis=1)
    dist=np.einsum('ni,nij->nj',dist,P)
    if k%2==0:
        e=next(x for x in exact['examples'] if x['N']==k and x['L']==2)
        target=float(F(e['front']));value=float(front.mean());se=float(front.std(ddof=1)/math.sqrt(n))
        rows.append({'N':k,'exact_front':target,'quenched_MC_front':value,'MC_SE':se,'z':(value-target)/se})
        assert abs(value-target)<5*se
(root/'data/independent_checks.json').write_text(json.dumps(rows,indent=2))
print(json.dumps(rows,indent=2))
