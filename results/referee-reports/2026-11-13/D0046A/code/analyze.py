#!/usr/bin/env python3
import os
for key in ['OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','VECLIB_MAXIMUM_THREADS','NUMEXPR_NUM_THREADS']:
    os.environ[key]='1'
os.environ['MPLCONFIGDIR']=str(__import__('pathlib').Path(__file__).resolve().parents[1]/'data'/'mplconfig')
import csv,json,pathlib
cache_path=pathlib.Path(__file__).resolve().parents[1]/'data'/'cache'
cache_path.mkdir(exist_ok=True)
os.environ['XDG_CACHE_HOME']=str(cache_path)
import numpy as np
from collections import defaultdict
ROOT=pathlib.Path(__file__).resolve().parents[1]
rng=np.random.default_rng(464646)

samples=defaultdict(dict)
with (ROOT/'data'/'edge_samples.csv').open() as f:
    for r in csv.DictReader(f):
        key=(r['model'],int(r['n']),int(r['eigenvalue_rank']))
        rep=int(r['rep']);s=float(r['s'])
        samples[key].setdefault(rep,{})[s]=float(r['edge_value'])
summary=[]
for (model,n,rank),reps in sorted(samples.items()):
    paths=np.array([[reps[i][s] for s in [0.,.25,1.,3.]] for i in sorted(reps)])
    for col,lag in enumerate([.25,1.,3.],1):
        x,y=paths[:,0],paths[:,col];delta2=(y-x)**2
        correlation=float(np.corrcoef(x,y)[0,1]);m=len(x)
        bootstrap=[]
        for _ in range(500):
            ix=rng.integers(m,size=m)
            bootstrap.append(float(np.corrcoef(x[ix],y[ix])[0,1]))
        lo,hi=np.quantile(bootstrap,[.025,.975])
        summary.append(dict(model=model,n=n,rank=rank,lag_s=lag,reps=m,
                            correlation=correlation,correlation_ci_low=float(lo),correlation_ci_high=float(hi),
                            mean_squared_increment=float(delta2.mean()),
                            mean_squared_increment_se=float(delta2.std(ddof=1)/np.sqrt(m)),
                            mean_initial=float(x.mean()),variance_initial=float(x.var(ddof=1)),
                            mean_at_lag=float(y.mean()),variance_at_lag=float(y.var(ddof=1))))
with (ROOT/'data'/'summary.csv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=list(summary[0]));w.writeheader();w.writerows(summary)
energy=defaultdict(list)
with (ROOT/'data'/'edge_energies.csv').open() as f:
    for r in csv.DictReader(f):energy[(int(r['n']),int(r['eigenvalue_rank']))].append((float(r['ipr']),float(r['gamma'])))
with (ROOT/'data'/'energy_summary.csv').open('w',newline='') as f:
    w=csv.writer(f);w.writerow(['n','rank','reps','mean_ipr','mean_gamma','gamma_se'])
    for (n,j),rows in sorted(energy.items()):
        a=np.array(rows);w.writerow([n,j,len(a),*a.mean(axis=0),a[:,1].std(ddof=1)/np.sqrt(len(a))])
lines=['Two-time numerical evidence (independent ensembles; 95% percentile bootstrap CIs, 500 resamples).',
       'Lags use s=n^(1/3)*t for rate-one OU; standard Airy time is 2s.',
       'The n=2048 Hermitian BM sample has only 12 replicates and is a pilot, not an asymptotic estimate.','']
for r in summary:
    if r['rank']==1 and r['lag_s']==1:
        lines.append(f"{r['model']:20s} n={r['n']:4d} R={r['reps']:4d} corr={r['correlation']:.4f} CI=[{r['correlation_ci_low']:.4f},{r['correlation_ci_high']:.4f}] MSD={r['mean_squared_increment']:.4f} +/- {r['mean_squared_increment_se']:.4f}")
(ROOT/'data'/'SUMMARY.txt').write_text('\n'.join(lines)+'\n')
print('\n'.join(lines))

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
fig,axes=plt.subplots(1,2,figsize=(10,4.2),constrained_layout=True)
colors={'hermitian_bm':'#16629c','independent_tri_ou':'#c04b2a'}
labels={'hermitian_bm':'Hermitian Brownian motion (normalized)','independent_tri_ou':'Independent tridiagonal OU'}
for model in colors:
    sub=[r for r in summary if r['model']==model and r['rank']==1 and r['lag_s']==1]
    ns=np.array([r['n'] for r in sub]);cs=np.array([r['correlation'] for r in sub])
    err=np.array([[r['correlation']-r['correlation_ci_low'] for r in sub],
                  [r['correlation_ci_high']-r['correlation'] for r in sub]])
    # Sampling can put a percentile interval to one side of the point estimate;
    # draw interval segments directly rather than forcing nonnegative error lengths.
    axes[0].vlines(ns,[r['correlation_ci_low'] for r in sub],[r['correlation_ci_high'] for r in sub],color=colors[model],alpha=.6)
    axes[0].plot(ns,cs,'o-',color=colors[model],label=labels[model])
    axes[1].errorbar(ns,[r['mean_squared_increment'] for r in sub],
                     yerr=[1.96*r['mean_squared_increment_se'] for r in sub],fmt='o-',color=colors[model])
for ax in axes:
    ax.set_xscale('log',base=2);ax.set_xlabel('Matrix size n');ax.grid(alpha=.2)
axes[0].set_ylabel('Top eigenvalue correlation');axes[0].set_ylim(-.25,1.03)
axes[0].legend(fontsize=8,loc='lower left')
axes[1].set_ylabel('Mean squared edge increment')
fig.suptitle('Two-time edge statistics at lag s=1 (standard Airy lag 2)\nn=2048 dense data: 12 replicates only',fontsize=11)
fig.savefig(ROOT/'data'/'edge_comparison.svg')
plt.close(fig)
