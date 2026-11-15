"""Produce a standalone scientific figure from the saved CSV files."""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):
    os.environ[key]='1'
from pathlib import Path
import csv
from collections import defaultdict
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
ROOT=Path(__file__).resolve().parents[1]
D=defaultdict(float)
for r in csv.DictReader((ROOT/'data/sampled_correlations.csv').open()):
    if r['window']=='512':
        key=(r['model'],int(r['gap']))
        D[key]=max(D[key],float(r['correlation']))
fig,ax=plt.subplots(1,2,figsize=(11,4.2),layout='constrained')
ns=[1,2,4,8,16,32,64]
for model,label in [('ar07','AR(0.7)'),('difference_ar07','Differenced AR(0.7)'),
                    ('difference','Differenced white noise'),('cusp','Cusp |1-z|'),
                    ('step','Positive step density'),('white_plus_atom','White noise + atom')]:
    ax[0].plot(ns,[D[(model,n)] for n in ns],marker='o',ms=3,label=label)
ax[0].set(xscale='log',xlabel='Separation n',ylabel='Largest sampled canonical correlation',
          title='Window 512: lower bounds from specified supports',ylim=(-.025,1.03))
ax[0].legend(fontsize=7,loc='upper right')
for n in (1,8,128):
    rows=[r for r in csv.DictReader((ROOT/'data/cusp_block_sums.csv').open()) if int(r['gap'])==n]
    ax[1].plot([int(r['block_length']) for r in rows],
               [float(r['absolute_correlation']) for r in rows],marker='o',ms=3,label=f'Fixed gap n={n}')
ax[1].axhline(.5,ls='--',c='black',lw=1,label='Proved block-sum limit 1/2')
ax[1].set(xscale='log',xlabel='Length L of each block',ylabel='Absolute block-sum correlation',
          title='Cusp density: increasing the window reveals dependence',ylim=(0,.54))
ax[1].legend(fontsize=8)
for a in ax:
    a.grid(alpha=.22)
fig.savefig(ROOT/'data/correlations.svg')
fig.savefig(ROOT/'data/correlations.png',dpi=150)
print('Saved data/correlations.svg')
