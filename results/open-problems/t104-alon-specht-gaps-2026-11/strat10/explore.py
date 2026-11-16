"""NUMERICAL: exploratory thresholds only, not certificates."""
import os
for k in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):os.environ[k]='1'
import sys
sys.dont_write_bytecode=True
sys.path.insert(0,'../STRAT6')
from moment_bounds import vertices
import numpy as np
from scipy.optimize import brentq

def bound(a,r,v):
    A,B,C=map(float,v);F=A+r*B+(1+r)*C
    c=max(0,(1-10*r-2*r*r)/3)
    return 9/80+a*(11*F-2*(1+r))/8+a*a*((100*(1+r)*F-1600*(A+r*r*B)-1280*(1+r*r)*C-640*r*C+415*(1+r*r)-66*r)/320-c*C)
if __name__=='__main__':
    print('NUMERICAL: process priority',os.getpriority(os.PRIO_PROCESS,0))
    for enhanced in (False,True):
        vs=vertices(enhanced)
        roots=[]
        for r in np.linspace(0,1,1001):
            g=lambda a:min(bound(a,r,v) for v in vs)
            root=brentq(g,0,2) if g(2)<0 else 2
            roots.append((root,r))
        print('NUMERICAL: enhanced',enhanced,'vertices',len(vs),'worst',min(roots))
        for r in (0,.1,.2,.4,.6,.8,1):
            print('NUMERICAL: ratio',r,'scale',brentq(lambda a:min(bound(a,r,v) for v in vs),0,2))
