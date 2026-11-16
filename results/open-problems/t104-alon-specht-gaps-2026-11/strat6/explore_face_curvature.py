"""NUMERICAL: test the proposed second face reduction in fixed-frame (a,b)."""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):
    os.environ[key]='1'
import numpy as np
import json
import sys
sys.path.insert(0,'STRAT5')
from stratum import BASIS,IJ
rng=np.random.default_rng(13110329)
F=np.linalg.qr(rng.normal(size=(100000,4,2)))[0]
F=np.einsum('ij,njk->nik',BASIS,F)
u,w=F[:,:,0],F[:,:,1]
A,B,C=(u**4).sum(1),(w**4).sum(1),(u*u*w*w).sum(1)
d,e,f,h=(u**3).sum(1),(u*u*w).sum(1),(u*w*w).sum(1),(w**3).sum(1)
P=58/45-40*A/9-34*C/9+8*d*d/3+2*e*e/3+2*d*f
R=58/45-40*B/9-34*C/9+8*h*h/3+2*f*f/3+2*h*e
Q=2/9*(A+B-.4)-8*C/9+10/3*(e*e+f*f)+2*d*f+2*h*e
cs=.05+u[:,IJ[0]]*u[:,IJ[1]]
ds=.05+w[:,IJ[0]]*w[:,IJ[1]]
r=rng.uniform(.12,1,len(F))
c=cs+r[:,None]*ds
ends=np.where(c<0,-.1/np.minimum(c,-1e-15),np.inf)
edge=ends.argmin(1)
a=ends[np.arange(len(F)),edge]
cc=cs[np.arange(len(F)),edge]
dd=ds[np.arange(len(F)),edge]
curv=P*dd*dd-Q*cc*dd+R*cc*cc
valid=a<2/(3-r)-1e-10
positive=valid & (curv>1e-12)
print('NUMERICAL: zero endpoints',int(valid.sum()),'positive tangent curvature',int(positive.sum()))
if positive.any():
 ix=np.where(positive)[0][0]
 out=dict(frame=F[ix].tolist(),r=float(r[ix]),a=float(a[ix]),edge=int(edge[ix]),curvature=float(curv[ix]))
 print('NUMERICAL:',out)
 with open('positive_face_curvature.json','w') as fp:json.dump(out,fp,indent=2)
