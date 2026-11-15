"""Plot empirical CRT-scaled height/width CDFs; no paper imagery."""
import os
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):
    os.environ[k]='1'
import csv,pathlib
ROOT=pathlib.Path(__file__).resolve().parents[1]
cache=ROOT/'data'/'plot_cache'
cache.mkdir(exist_ok=True)
os.environ['MPLCONFIGDIR']=str(cache)
os.environ['XDG_CACHE_HOME']=str(cache)
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from simulate_ou_conditioned import excursion_max_cdf,audit_priority
audit_priority()
fig,axes=plt.subplots(1,2,figsize=(10,4),sharey=True)
x=np.linspace(.5,2.3,500)
for ax,stat,label in zip(axes,('height','width'),('Scaled height','Scaled width')):
    ax.plot(x,excursion_max_cdf(x),color='black',lw=1.8,label='CRT maximum excursion')
    for prefix,name,color in [('ou_poisson','Poisson (300 trees)','#2266aa'),('ou','Binomial (150 trees)','#b26422')]:
        with (ROOT/f'data/{prefix}_conditioned_raw.csv').open() as f:
            vals=np.sort([float(r[stat+'_scaled']) for r in csv.DictReader(f) if int(r['n'])==100000])
        ax.step(vals,np.arange(1,len(vals)+1)/len(vals),where='post',label=name,color=color,lw=1.2)
    ax.set_xlabel(label);ax.set_xlim(.5,2.3);ax.grid(alpha=.2)
axes[0].set_ylabel('Cumulative probability');axes[1].legend(frameon=False,fontsize=8,loc='lower right')
fig.suptitle('Exact size-conditioned OU-marked branching trees, n = 100,000')
fig.tight_layout();fig.savefig(ROOT/'data/crt_comparison.svg');plt.close(fig)
print('Saved data/crt_comparison.svg')
