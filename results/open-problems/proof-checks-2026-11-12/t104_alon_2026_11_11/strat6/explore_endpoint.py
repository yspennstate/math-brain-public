"""NUMERICAL: diagnostics for the extreme-u-pair endpoint polynomial."""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):
    os.environ[key]='1'
import sys
sys.path.insert(0,'STRAT5')
import numpy as np
from stratum import BASIS
rng=np.random.default_rng(13110323)
U=np.linalg.qr(rng.normal(size=(100000,4,2)))[0]
U=np.einsum('ij,njk->nik',BASIS,U)
u,w=U[:,:,0],U[:,:,1]
A,B,C=(u**4).sum(1),(w**4).sum(1),(u*u*w*w).sum(1)
d,e,f,h=(u**3).sum(1),(u*u*w).sum(1),(u*w*w).sum(1),(w**3).sum(1)
lo,hi=np.argmin(u,axis=1),np.argmax(u,axis=1)
k=1+20*w[np.arange(len(U)),lo]*w[np.arange(len(U)),hi]
p=-u[np.arange(len(U)),lo]*u[np.arange(len(U)),hi]
Lu,Lw=14/9*(A+C-.2),14/9*(B+C-.2)
P=58/45-40*A/9-34*C/9+8*d*d/3+2*e*e/3+2*d*f
R=58/45-40*B/9-34*C/9+8*h*h/3+2*f*f/3+2*h*e
Q=2/9*(A+B-.4)-8*C/9+10/3*(e*e+f*f)+2*d*f+2*h*e
for r in [.12,.15,.2,.25,.3,.4,.6,1]:
    E=4.5*((20*p-1-r*k)*(Lu+r*Lw)+2*(P+r*Q+r*r*R))
    ix=E.argmin()
    print('NUMERICAL: r',r,'minimum',E[ix],'frame',U[ix].tolist(),flush=True)
