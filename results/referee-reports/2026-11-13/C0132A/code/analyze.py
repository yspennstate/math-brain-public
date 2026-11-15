"""Summaries, paired bootstrap intervals and a standalone scientific figure."""
import csv
import json
import math
from pathlib import Path
import statistics
import numpy as np

root=Path(__file__).resolve().parents[1]
rng=np.random.default_rng(1322026)
summary=[]; growth=[]; columns=[]

def wilson(k,n):
    z=1.959963984540054;p=k/n;den=1+z*z/n
    center=(p+z*z/(2*n))/den
    half=z*math.sqrt(p*(1-p)/n+z*z/(4*n*n))/den
    return max(0,center-half),min(1,center+half)

def mean_se(x):
    x=np.array(x,dtype=float)
    return x.mean(),x.std(ddof=1)/math.sqrt(len(x))

for d1 in (1,2):
    rows=list(csv.DictReader((root/f'data/m{d1}1.csv').open()))
    by={}
    for r in rows: by.setdefault(int(r['n']),[]).append(r)
    indices=rng.integers(0,128,size=(4000,128))
    previous=None
    for n,rs in sorted(by.items()):
        rs.sort(key=lambda r:int(r['seed']))
        assert len(rs)==128 and [int(r['seed']) for r in rs]==list(range(128))
        for r in rs:
            assert int(r['first_departures'])+int(r['revisit_departures'])==n
            assert int(r['range'])-int(r['first_departures']) in (0,1)
            assert (int(r['last_origin'])>n//2)==bool(int(r['window_hit']))
            assert (int(r['window_visits'])>0)==bool(int(r['window_hit']))
        vals=lambda key:[float(r[key]) for r in rs]
        ranges=np.array(vals('range'))
        rmean,rse=mean_se(ranges)
        k=sum(int(r['window_hit']) for r in rs);ci=wilson(k,len(rs))
        visits,vse=mean_se(vals('origin_returns'))
        wvis,wse=mean_se(vals('window_visits'))
        row=dict(d1=d1,d2=1,n=n,seeds=len(rs),range_mean=rmean,range_se=rse,
                 range_median=float(np.median(ranges)),late_hit_seeds=k,late_hit_probability=k/len(rs),
                 late_wilson_low=ci[0],late_wilson_high=ci[1],returns_mean=visits,returns_se=vse,
                 window_visits_mean=wvis,window_visits_se=wse,window_occupancy=wvis/(n-n//2),
                 endpoint_origin_seeds=sum(int(r['endpoint_origin']) for r in rs))
        summary.append(row)
        if previous:
            pn,pr=previous
            alpha=math.log(rmean/pr.mean())/math.log(n/pn)
            boot=np.log(ranges[indices].mean(axis=1)/pr[indices].mean(axis=1))/math.log(n/pn)
            low,high=np.quantile(boot,[.025,.975])
            growth.append(dict(d1=d1,d2=1,from_n=pn,to_n=n,alpha=alpha,
                               bootstrap_low=float(low),bootstrap_high=float(high)))
        previous=(n,ranges)
        entries=sum(vals('column_entries'))
        columns.append(dict(d1=d1,d2=1,n=n,entries_mean=entries/128,
                            zero_q_fraction=sum(vals('column_zero_q'))/entries,
                            q_sum_mean=statistics.mean(vals('column_q_sum')),
                            completed_successes_mean=statistics.mean(vals('column_successes')),
                            component_width_mean=statistics.mean([int(r['column_hi'])-int(r['column_lo'])+1 for r in rs]),
                            column_sites_mean=statistics.mean(vals('column_sites'))))

for name,data in [('summary',summary),('growth',growth),('columns',columns)]:
    with (root/f'data/{name}.csv').open('w') as f:
        w=csv.DictWriter(f,fieldnames=list(data[0]));w.writeheader();w.writerows(data)

independent=[]
ir=list(csv.DictReader((root/'data/independent.csv').open()))
for d1 in (1,2):
    for n in (10000,100000,1000000):
        rows=[r for r in ir if int(r['d1'])==d1 and int(r['n'])==n]
        assert len(rows)==16
        mean,se=mean_se([int(r['range']) for r in rows])
        independent.append(dict(d1=d1,d2=1,n=n,seeds=16,range_mean=mean,range_se=se))
with (root/'data/independent_summary.csv').open('w') as f:
    w=csv.DictWriter(f,fieldnames=list(independent[0]));w.writeheader();w.writerows(independent)

text=['| Case | n | Mean range ± SE | Origin visits ± SE | Late-return seeds | Late-return probability (95% Wilson) |',
      '|---|---:|---:|---:|---:|---:|']
for r in summary:
    text.append(f"| M({r['d1']},1) | {r['n']:,} | {r['range_mean']:,.1f} ± {r['range_se']:,.1f} | {r['returns_mean']:.3f} ± {r['returns_se']:.3f} | {r['late_hit_seeds']}/128 | {r['late_hit_probability']:.4f} ({r['late_wilson_low']:.4f}, {r['late_wilson_high']:.4f}) |")
text+=['','| Case | Interval | Effective range exponent | Paired bootstrap 95% interval |',
       '|---|---:|---:|---:|']
for r in growth:
    text.append(f"| M({r['d1']},1) | {r['from_n']:,}–{r['to_n']:,} | {r['alpha']:.4f} | ({r['bootstrap_low']:.4f}, {r['bootstrap_high']:.4f}) |")
text+=['','| Case | n | Mean column entries | Fraction with q=0 | Mean Q | Mean completed successes | Mean origin-component size |',
       '|---|---:|---:|---:|---:|---:|---:|']
for r in columns:
    if r['n']<100000:continue
    text.append(f"| M({r['d1']},1) | {r['n']:,} | {r['entries_mean']:.2f} | {r['zero_q_fraction']:.4f} | {r['q_sum_mean']:.4f} | {r['completed_successes_mean']:.4f} | {r['component_width_mean']:.2f} |")
(root/'data/tables.md').write_text('\n'.join(text)+'\n')

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
fig,axes=plt.subplots(1,3,figsize=(13,3.7),layout='constrained')
for d1,color in [(1,'#2864aa'),(2,'#b54a2b')]:
    rs=[r for r in summary if r['d1']==d1]
    n=np.array([r['n'] for r in rs]);means=np.array([r['range_mean'] for r in rs]);se=np.array([r['range_se'] for r in rs])
    axes[0].plot(n,means,'o-',color=color,label=f'M({d1},1)')
    axes[0].fill_between(n,means-1.96*se,means+1.96*se,color=color,alpha=.18)
    axes[1].plot(n,means/n,'o-',color=color)
    p=np.array([r['late_hit_probability'] for r in rs])
    lo=np.array([r['late_wilson_low'] for r in rs]);hi=np.array([r['late_wilson_high'] for r in rs])
    axes[2].errorbar(n,p,yerr=[p-lo,hi-p],fmt='o-',capsize=3,color=color)
axes[0].set(xscale='log',yscale='log',xlabel='Steps n',ylabel='Mean distinct vertices');axes[0].legend(frameon=False)
axes[1].set(xscale='log',xlabel='Steps n',ylabel='Mean range / n')
axes[2].set(xscale='log',xlabel='Steps n',ylabel='P(origin hit in (n/2,n])',ylim=(-.005,.16))
for ax in axes:ax.grid(alpha=.2)
fig.savefig(root/'data/range_returns.png',dpi=180)
fig.savefig(root/'data/range_returns.svg')
print('\n'.join(text))
print('All 1280 simulation checkpoint rows passed consistency checks.')
