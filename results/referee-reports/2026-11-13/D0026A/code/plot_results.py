#!/usr/bin/env python3
import os
os.environ['XDG_CACHE_HOME']=str(__import__('pathlib').Path('data/cache').resolve())
os.environ.update(MPLCONFIGDIR=str(__import__('pathlib').Path('data/mplconfig').resolve()),OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1',VECLIB_MAXIMUM_THREADS='1')
import csv
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
fig,axes=plt.subplots(2,4,figsize=(14,6),constrained_layout=True)
for j,q in enumerate([.1,.3,.6,.85]):
 for mode,label,color in [(0,'single seed','#2364aa'),(1,'sparse + seed','#ba4b32')]:
  rows=list(csv.DictReader(open(f'data/q{q:g}_mode{mode}.csv')))
  ts=[float(r['time']) for r in rows if float(r['time'])>0];rr=[r for r in rows if float(r['time'])>0]
  axes[0,j].errorbar(ts,[float(r['infect0'])-q for r in rr],yerr=[1.96*float(r['infect0_se']) for r in rr],label=label,color=color,marker='.',lw=1,capsize=2)
  key='right_front' if mode==0 else 'ever_right'
  axes[1,j].plot(ts,[float(r[key]) for r in rr],label='current R, seed' if mode==0 else 'connected visited reach, sparse',color=color,marker='.',lw=1)
 axes[0,j].axhline(0,color='black',lw=.7);axes[0,j].set_xscale('log');axes[0,j].set_title(f'q={q}');axes[0,j].set_xlabel('time');axes[1,j].set_xlabel('time')
axes[0,0].set_ylabel('P(infection at 0) − q\n(pointwise 95% error bars)');axes[1,0].set_ylabel('rightward extent');axes[0,0].legend(fontsize=8);axes[1,0].legend(fontsize=7)
fig.suptitle('FA-1f: 2,000 independent paths per q and initial law; evidence only')
fig.savefig('data/fa1f_results.svg');plt.close(fig)
