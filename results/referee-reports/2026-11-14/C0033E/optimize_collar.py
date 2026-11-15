"""Finite local/global optimization on a precisely specified spectral collar.

lambda_min=exp(-L), lambda_max=1-exp(-b L), b in [.12,1].
Middle eigenvalue lies between them. Six optimization coordinates cover
three orientation angles, one phase, b, and the middle spectral parameter.
This is a search, not a certified minimum.
"""
import os
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):os.environ[k]='1'
import json,time,math,resource
from pathlib import Path
import mpmath as mp
import numpy as np
from scipy.optimize import differential_evolution,minimize
from mp_core import *

OUT=Path('data/collar_optimization.json')
def build(x,L):
    angles=[mp.atan(mp.exp(mp.mpf(str(v)))) for v in x[:3]]
    phase=mp.mpf(str(x[3]));b=mp.mpf(str(x[4]));mid=mp.mpf(str(x[5]))
    u=rotation(1,2,angles[2])*rotation(0,2,angles[1],phase)*rotation(0,1,angles[0])
    lo=mp.exp(-L);hi=1-mp.exp(-b*L);t=lo+(hi-lo)/(1+mp.exp(-mid))
    q=u*mp.diag([lo,t,hi])*u.H
    return (q+q.H)/2

def main():
    start=time.monotonic();out=dict(seed=33506,runs=[])
    def save():
        out['seconds']=time.monotonic()-start;out['peak_rss_mib']=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/2**20
        tmp=OUT.with_suffix('.tmp');tmp.write_text(json.dumps(out,indent=2)+'\n');tmp.replace(OUT)
    for L in (20,60,150,400):
        mp.mp.dps=100+int(2.5*L/math.log(10))
        row=dict(L=L,precision=mp.mp.dps,evaluations=0,rejected=0,best=None,starts=[]);out['runs'].append(row)
        bounds=[(-.8*L,.8*L)]*3+[(-math.pi,math.pi),(.12,1),(-.9*L,.9*L)]
        def objective(x):
            row['evaluations']+=1
            if any(v<lo or v>hi for v,(lo,hi) in zip(x,bounds)):
                row['rejected']+=1;return 2+sum(max(lo-v,v-hi,0)**2 for v,(lo,hi) in zip(x,bounds))
            try:
                q=build(x,L);ev=evaluate(q)
                if row['best'] is None or ev['margin']<mp.mpf(row['best']['margin']):
                    row['best']=strings(dict(**ev,x=list(map(float,x)),coordinates=coordinates(q)),70)
                if ev['margin']<0:save();raise RuntimeError('negative margin found')
                if row['evaluations']%100==0:save()
                return float(ev['margin'])
            except (ArithmeticError,ValueError,ZeroDivisionError):row['rejected']+=1;return 2
        de=differential_evolution(objective,bounds,seed=33506+L,workers=1,popsize=8,maxiter=22,polish=False,tol=1e-9)
        row['de']=dict(success=bool(de.success),message=str(de.message),evaluations=int(de.nfev))
        for initial in (de.x, np.array([0,-.5*L,0,0,1,.3*L]),np.array([-.5*L,0,0,math.pi,1,0])):
            local=minimize(objective,initial,method='Nelder-Mead',options=dict(maxfev=900,xatol=1e-7,fatol=1e-12))
            row['starts'].append(dict(success=bool(local.success),message=str(local.message),evaluations=int(local.nfev)))
        print('L',L,'evals',row['evaluations'],'best',row['best']['margin'],'scaled',row['best']['scaled'],flush=True);save()
    save()
if __name__=='__main__':main()
