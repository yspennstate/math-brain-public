"""Summarize independent runs, without treating simulation errors as proofs."""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):
    os.environ[key]='1'
import csv,json,sys
from pathlib import Path
import numpy as np
from scipy.optimize import brentq
from density import flux_density
ROOT=Path(__file__).resolve().parents[1]
rows=list(csv.DictReader((ROOT/'referee_data/monte_carlo.csv').open()))
result=[]
for r in (.1,5.,20.):
    a=[x for x in rows if float(x['r'])==r]
    t=np.array([float(x['time']) for x in a]);g=np.array([float(x['log_growth']) for x in a])
    estimate=g.sum()/t.sum()
    # Delta-method batch variance for the ratio of accumulated rewards/time.
    z=g-estimate*t
    se=np.std(z,ddof=1)/(np.sqrt(len(z))*np.mean(t))
    reps=[]
    for rep in range(3):
        b=[x for x in a if int(x['replicate'])==rep]
        reps.append(sum(float(x['log_growth']) for x in b)/sum(float(x['time']) for x in b))
    result.append(dict(r=r,cycles=sum(int(x['cycles']) for x in a),blocks=len(a),
                       exponent=estimate,block_se=se,replicates=reps,total_time=float(t.sum()),
                       density=flux_density(r)['exponent']))
grid=list(csv.DictReader((ROOT/'referee_data/grid.csv').open()))
brackets=[]
for a,b in zip(grid,grid[1:]):
    if float(a['exponent'])*float(b['exponent'])<0:
        lo,hi=float(a['r']),float(b['r'])
        root=brentq(lambda r:flux_density(r)['exponent'],lo,hi,xtol=2e-11)
        brackets.append(dict(bracket=[lo,hi],root=root))
data=dict(monte_carlo=result,grid=dict(count=len(grid),range=[float(grid[0]['r']),float(grid[-1]['r'])],
                                     sampled_sign_changes=brackets),
          limits=dict(slow=.25,fast=float(-.75+np.sqrt(3)/2)),
          sanity_rates=[flux_density(r) for r in (.0001,.001,.01,100.,1000.)])
(ROOT/'referee_data/summary.json').write_text(json.dumps(data,indent=2)+'\n')
print(json.dumps(data,indent=2))
