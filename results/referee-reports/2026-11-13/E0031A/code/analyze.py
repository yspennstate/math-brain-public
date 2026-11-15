#!/usr/bin/env python3
"""Stratified nonparametric bootstrap; finite-size trends only, never a proof."""
import csv,json,os,math
from pathlib import Path
from collections import defaultdict
os.environ['MPLCONFIGDIR']=str(Path('data/matplotlib_cache').resolve())
os.environ['XDG_CACHE_HOME']=str(Path('data/fontconfig_cache').resolve())
for k in ['OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','VECLIB_MAXIMUM_THREADS']:os.environ[k]='1'
assert os.getpriority(os.PRIO_PROCESS,0)>=10
import numpy as np
B=4000
rng=np.random.default_rng(31001399)
groups=defaultdict(list)
with Path('data/samples.csv').open() as f:
 for r in csv.DictReader(f):groups[int(r['d']),int(r['n'])].append(float(r['length']))
summary=[];boot={}
for (d,n),ls in sorted(groups.items()):
 x=np.array(ls);m=len(x)
 if m<50:continue
 v=float(np.var(x,ddof=1))
 # Process bootstrap in small batches, avoiding a large memory allocation.
 vs=[]
 for offset in range(0,B,100):
  a=x[rng.integers(0,m,size=(min(100,B-offset),m))]
  vs.extend(np.var(a,axis=1,ddof=1))
 vs=np.array(vs)
 assert np.all(np.isfinite(vs)) and np.all(vs>0)
 boot[d,n]=vs
 lo,hi=np.quantile(vs,[.025,.975]);power=1-2/d
 summary.append({'d':d,'n':n,'samples':m,'mean':float(x.mean()),'variance':v,'var_ci_low':float(lo),'var_ci_high':float(hi),'variance_over_target_power':v/n**power,'normalized_ci_low':float(lo/n**power),'normalized_ci_high':float(hi/n**power)})
with Path('data/summary.csv').open('w') as f:
 w=csv.DictWriter(f,fieldnames=list(summary[0]));w.writeheader();w.writerows(summary)
slopes=[]
for d in sorted({r['d'] for r in summary}):
 for min_n in [32,256]:
  rows=[r for r in summary if r['d']==d and r['n']>=min_n]
  if len(rows)<3:continue
  logn=np.log([r['n'] for r in rows]);z=logn-logn.mean();den=float(np.sum(z*z))
  slope=float(np.sum(z*np.log([r['variance'] for r in rows]))/den)
  bs=np.sum(z[:,None]*np.array([np.log(boot[d,r['n']]) for r in rows]),axis=0)/den
  assert np.all(np.isfinite(bs))
  low,high=np.quantile(bs,[.025,.975])
  slopes.append({'d':d,'min_n':min_n,'max_n':max(r['n'] for r in rows),'loglog_slope':slope,'bootstrap_ci_low':float(low),'bootstrap_ci_high':float(high),'target_exponent':1-2/d})
Path('data/trends.json').write_text(json.dumps({'bootstrap_replicates':B,'bootstrap_seed':31001399,'method':'percentile nonparametric independent within each (d,n); ordinary least squares of log variance on log n','slopes':slopes},indent=2)+'\n')
lines=['| d | n | samples | sample variance | 95% bootstrap interval | variance / n^(1-2/d) |','|---:|---:|---:|---:|---:|---:|']
for r in summary:lines.append(f"| {r['d']} | {r['n']} | {r['samples']} | {r['variance']:.6g} | [{r['var_ci_low']:.6g}, {r['var_ci_high']:.6g}] | {r['variance_over_target_power']:.6g} |")
Path('data/numerical_table.md').write_text('\n'.join(lines)+'\n')
try:
 import matplotlib
 matplotlib.use('Agg')
 import matplotlib.pyplot as plt
 fig,ax=plt.subplots(1,2,figsize=(10,4),layout='constrained')
 for d in sorted({r['d'] for r in summary}):
  rows=[r for r in summary if r['d']==d];ns=np.array([r['n'] for r in rows]);vs=np.array([r['variance'] for r in rows]);lo=np.array([r['var_ci_low'] for r in rows]);hi=np.array([r['var_ci_high'] for r in rows]);p=1-2/d
  ax[0].errorbar(ns,vs,yerr=[vs-lo,hi-vs],marker='o',capsize=2,label=f'd={d}')
  ax[1].errorbar(ns,vs/ns**p,yerr=[(vs-lo)/ns**p,(hi-vs)/ns**p],marker='o',capsize=2,label=f'd={d}')
 ax[0].set(xscale='log',yscale='log',xlabel='Number of points n',ylabel='Sample variance of total length',title='Complete-graph one-colour matching')
 ax[1].set(xscale='log',xlabel='Number of points n',ylabel='Variance divided by n^(1−2/d)',title='Target normalization (evidence only)')
 for a in ax:a.grid(alpha=.2);a.legend()
 fig.savefig('data/variance.svg');plt.close(fig)
except ImportError:pass
print(json.dumps({'samples':sum(map(len,groups.values())),'groups':len(summary),'slopes':slopes},indent=2))
