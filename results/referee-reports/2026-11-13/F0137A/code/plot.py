#!/usr/bin/env python3
"""Standalone vector plots of this run's numerical data, never source-page images."""
import os
from pathlib import Path
root=Path(__file__).resolve().parents[1]
os.environ['MPLCONFIGDIR']=str(root/'data/mpl_config')
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
if os.getpriority(os.PRIO_PROCESS,0)<10:os.setpriority(os.PRIO_PROCESS,0,10)
import csv
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

names=['d2_moderate','d3_moderate','d2_trapping','d3_trapping']
rows=list(csv.DictReader((root/'data/slab_intervals.csv').open()))
fig,axes=plt.subplots(2,2,figsize=(10,7),constrained_layout=True)
for ax,name in zip(axes.flat,names):
    a=[x for x in rows if x['model']==name]
    L=np.array([int(x['L']) for x in a]);lo=np.array([float(x['q95_lower']) for x in a]);hi=np.array([float(x['q95_upper']) for x in a])
    ax.fill_between(L,np.maximum(lo,1e-5),hi,color='#4682b4',alpha=.25,label='95% interval incl. censoring')
    observed=np.array([float(x['p_back_by_cap']) for x in a]);upper=np.array([float(x['p_not_front_by_cap']) for x in a])
    ax.plot(L,np.maximum(observed,1e-5),'o-',label='backward by time cap')
    if any(int(x['censored']) for x in a):ax.plot(L,upper,'s--',label='not forward by time cap')
    ax.set(title=name,xlabel='slab half-width L',ylabel='backward exit probability',yscale='log',ylim=(1e-4,1))
    ax.grid(alpha=.2);ax.legend(fontsize=7)
fig.suptitle('RWDE slab exits: finite-scale evidence; zero counts are not zero probabilities')
fig.savefig(root/'data/slab_exits.svg');plt.close(fig)

rows=list(csv.DictReader((root/'data/renewal_tail_lower_bounds.csv').open()))
fig,axes=plt.subplots(2,2,figsize=(10,7),constrained_layout=True)
for ax,name in zip(axes.flat,names):
    for H in (10000,30000,100000):
        a=[x for x in rows if x['model']==name and int(x['horizon'])==H]
        ax.plot([int(x['t']) for x in a],[float(x['proxy_tail']) for x in a],'o-',label=f'horizon {H:,}')
    ax.set(title=name,xlabel='time t',ylabel='P(finite-horizon proxy > t)',xscale='log',yscale='log',ylim=(.001,1))
    ax.grid(alpha=.2);ax.legend(fontsize=7)
fig.suptitle('Provisional regeneration tails: lower bounds for the actual tails')
fig.savefig(root/'data/renewal_proxies.svg');plt.close(fig)
