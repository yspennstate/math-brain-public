#!/usr/bin/env python3
"""Additional independent checks of boundary estimates and comparison arguments.
No imports or data from src, or from referee_audit.py.
"""
import json
from math import log, sqrt
from pathlib import Path
from datetime import datetime
import os
os.environ.setdefault('OPENBLAS_NUM_THREADS','1')
import numpy as np
import mpmath as mp

mp.mp.dps=50
z=float(mp.zeta(2)); b=float(mp.euler/mp.zeta(2)+mp.zeta(3)/mp.zeta(2)**2)
N=8000
h=np.zeros(1000001); h[1:]=np.cumsum(1/np.arange(1,len(h),dtype=float))
signed=np.zeros(N+1); oscillating=np.zeros(N+1)
barriermax=(0,0); dmax=(0,0); signedrows={}
for n in range(2,N+1):
    i=np.arange(1,n,dtype=float); j=n-i; L=log(n)
    q=n/(2*h[n-1]*i*j)
    A=np.sum(-np.log(i/n)/(n-i))
    B=np.sum(np.log(i/n)**2/(n-i))
    defect=n/h[n-1]*((2*L*A-B)/(2*z)+b*A)
    dv=np.sum(q*(np.sqrt(i)+np.sqrt(j)-sqrt(n)))
    assert dv>0
    ratio=abs(n-defect)/dv
    if ratio>barriermax[0]:barriermax=(float(ratio),n)
    dtoll=2*np.sum(q*np.minimum(i,j))
    ddefect=2*log(2)/z*n/h[n-1]*A
    if abs(dtoll-ddefect)>dmax[0]:dmax=(float(abs(dtoll-ddefect)),n)
    signed[n]=np.sum(q*(signed[1:n]+signed[n-1:0:-1]))-3*n*n*L*L/h[n-1]
    oscillating[n]=np.sum(q*(oscillating[1:n]+oscillating[n-1:0:-1]))+(-1)**n*n*n/h[n-1]
    if n in (100,1000,8000):
        signedrows[str(n)]={'negative_A_ratio':float(signed[n]/(n*n*L*L)),'signed_O_ratio':float(oscillating[n]/(n*n)),'S_defect_residual':float(n-defect),'barrier_defect':float(dv),'D_residual':float(dtoll-ddefect)}

counterexample=[]
for power in (2,4,8,16):
    x=mp.mpf(10)**(-power); y=1-x
    actual=abs((x*x*mp.log(x)+y*y*mp.log(y))/(2*x*y))
    claimed=x*abs(mp.log(x))+y*abs(mp.log(y))
    counterexample.append({'x':str(x),'actual_log_correction_integrand':str(actual),'stated_bound_shapes_sum':str(claimed),'ratio':str(actual/claimed)})

nonuniform={}
for n in (1000,10000,100000,1000000):
    p=1/log(n); x=np.arange(1,n,dtype=float)/n; y=1-x
    val=np.sum((1-x**p-y**p)/(2*x*y))/n
    target=float(mp.digamma(p)+mp.euler)
    nonuniform[str(n)]={'p':p,'defect_over_psi':float(val/target),'scaled_defect':float(val),'psi':target}

overview={}
for n in (10,100,1000,1000000):
    r=n//2
    ej=n/h[n-1]*(h[n-1]-h[r]+1/n)
    overview[str(n)]={'c_over_n':float(1-2*ej/n),'g_over_n2':float(1-2*(n-1)/(n*h[n-1]))}

out={'scope':'Finite computations do not prove asymptotics or uniform parameter estimates.', 'signed_transfer':signedrows,'max_S_residual_over_barrier':barriermax,'max_D_residual':dmax,'endpoint_counterexample_p2_j1':counterexample,'parameter_nonuniformity_p_1_over_log_n':nonuniform,'overview_toll_ratios':overview}
Path('referee_boundaries.json').write_text(json.dumps(out,indent=2)+'\n')
with Path('LOG.md').open('a') as f:
    f.write('\n- '+datetime.now().astimezone().isoformat(timespec='seconds')+': Completed signed-toll, barrier and endpoint-bound attacks (referee_boundaries.py). Literal endpoint bound at original line 179 fails for p=2,j=1; adding x^(j-1) repairs it. Fixed-parameter Riemann convergence is distinct from uniformity as p approaches zero.\n')
print(json.dumps(out,indent=2))
