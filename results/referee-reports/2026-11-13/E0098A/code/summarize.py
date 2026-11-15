"""Compute groupwise evidence and a standalone scientific CDF figure."""
import os
for key in ('OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','OMP_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):
    os.environ[key]='1'
import collections
import csv
import json
from pathlib import Path
import math

import numpy as np
from scipy.stats import kstest

ROOT=Path(__file__).resolve().parents[1]
RATE=math.sqrt(2/math.pi)
rows=list(csv.DictReader((ROOT/'data/main_samples.csv').open()))
groups=collections.defaultdict(list)
for row in rows:
    groups[(row['ensemble'],int(row['n']),row['region'])].append(row)
summary=[]
for (ensemble,n,region),items in sorted(groups.items()):
    values=np.array([float(row['scaled_min']) for row in items])
    test=kstest(values,'expon',args=(0,1/RATE))
    result=dict(ensemble=ensemble,n=n,region=region,samples=len(items),
        mean=float(values.mean()),mean_se=float(values.std(ddof=1)/math.sqrt(len(values))),
        median=float(np.median(values)),q90=float(np.quantile(values,.9)),
        empirical_cdf_t1=float(np.mean(values<=1)),empirical_cdf_t2=float(np.mean(values<=2)),
        ks_distance=float(test.statistic),ks_pvalue=float(test.pvalue),
        dkw_95=float(math.sqrt(math.log(40)/(2*len(values)))),
        simultaneous_dkw_95=float(math.sqrt(math.log(2*len(groups)/.05)/(2*len(values)))),
        minimum_observed=float(values.min()),
        max_residual=max(float(row['residual_l2']) for row in items),
        max_norm_error=max(float(row['norm_error']) for row in items))
    for t in (1,2):
        counts=np.array([int(row[f'count_t{t}']) for row in items])
        result[f'count_t{t}_mean']=float(counts.mean())
        result[f'count_t{t}_second_factorial_moment']=float((counts*(counts-1)).mean())
    summary.append(result)
with (ROOT/'data/summary.csv').open('w',newline='') as stream:
    writer=csv.DictWriter(stream,fieldnames=list(summary[0]))
    writer.writeheader()
    writer.writerows(summary)
audit={'matrix_count':len(rows)//3,'eigenvector_count':len(rows),'groups':len(groups),
       'rate':RATE,'predicted_mean':1/RATE,'predicted_median':math.log(2)/RATE,
       'max_residual':max(float(row['residual_l2']) for row in rows),
       'max_norm_error':max(float(row['norm_error']) for row in rows),
       'exact_float_zero_minima':sum(float(row['scaled_min'])==0 for row in rows),
       'nonfinite_statistic_count':sum(not math.isfinite(float(row['scaled_min'])) for row in rows),
       'familywise_05_rejections':sum(row['ks_pvalue']<.05/len(summary) for row in summary),
       'pointwise_05_rejections':sum(row['ks_pvalue']<.05 for row in summary)}
(ROOT/'data/numerical_audit.json').write_text(json.dumps(audit,indent=2))
print(json.dumps(audit,indent=2))
for row in summary:
    if row['n'] in (1024,2048):
        print(row['ensemble'],row['n'],row['region'],row['samples'],
              'mean',round(row['mean'],4),'KS',round(row['ks_distance'],4),'p',round(row['ks_pvalue'],4))

# This is a figure of our simulation data, not an image of source material.
os.environ['MPLCONFIGDIR']=str(ROOT/'data'/'.matplotlib')
os.environ['XDG_CACHE_HOME']=str(ROOT/'data'/'.cache')
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
fig,axes=plt.subplots(2,3,figsize=(12,6.8),sharex=True,sharey=True)
grid=np.linspace(0,5,500)
colors={'goe':'#3566a8','rademacher':'#bf5b30','bernoulli_p010':'#34845b'}
for i,n in enumerate((512,2048)):
    for j,region in enumerate(('lower_edge','bulk','upper_edge')):
        ax=axes[i,j]
        ax.plot(grid,1-np.exp(-RATE*grid),color='black',ls='--',lw=1.5,label='Exponential prediction')
        for ensemble,color in colors.items():
            values=np.sort([float(row['scaled_min']) for row in groups[(ensemble,n,region)]])
            ax.step(np.r_[0,values],np.r_[0,np.arange(1,len(values)+1)/len(values)],
                    where='post',color=color,lw=1,label=f'{ensemble} (m={len(values)})')
        ax.set_title(f'n={n}, {region.replace("_"," ")}')
        ax.set_xlim(0,5)
        ax.set_ylim(0,1)
        ax.grid(alpha=.15)
        if i==1: ax.set_xlabel(r'$n^{3/2}\min_k|v_j(k)|$')
        if j==0: ax.set_ylabel('Empirical cumulative probability')
axes[0,0].legend(fontsize=7,loc='lower right')
fig.tight_layout()
fig.savefig(ROOT/'data/minimum_cdf.svg')
fig.savefig(ROOT/'data/minimum_cdf.png',dpi=120)
plt.close(fig)
