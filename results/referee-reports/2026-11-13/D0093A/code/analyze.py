#!/usr/bin/env python3
"""Audit raw counts; summarize independent runs and plot their finite-size behavior."""
import os
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
os.chdir(ROOT)
for name in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS',
             'VECLIB_MAXIMUM_THREADS','NUMEXPR_NUM_THREADS']:
    os.environ[name]='1'
os.environ['MPLCONFIGDIR']=str(ROOT/'data'/'matplotlib_cache')
os.environ['XDG_CACHE_HOME']=str(ROOT/'data'/'cache')
assert os.getpriority(os.PRIO_PROCESS,0)>=10
import collections
import csv
import hashlib
import json
import math
import statistics
import sys

def quantile(values,p):
    v=sorted(values)
    i=(len(v)-1)*p
    a=math.floor(i);b=math.ceil(i)
    return v[a]+(v[b]-v[a])*(i-a)

rows=list(csv.DictReader(open('data/runs.csv')))
by=collections.defaultdict(list)
seeds=set()
for row in rows:
    n=int(row['n']);density=float(row['density']);lam=float(row['lambda'])
    assert density<lam/(1+lam)
    seed=int(row['seed']);assert seed not in seeds;seeds.add(seed)
    t=int(row['T'])
    assert int(row['jumps'])+int(row['sleep_success'])+int(row['sleep_failure'])==t
    assert int(row['finished'])==1
    assert int(row['sleep_success'])>=int(row['initial_mass'])
    assert 0<=int(row['max_odometer'])<=t
    assert abs(float(row['T_over_n'])-t/n)<1e-7
    counts=[int(row['sites_ge_'+str(k)]) for k in [1,2,5,10,20,50,100,200,500,1000]]
    assert n>=counts[0] and all(a>=b for a,b in zip(counts,counts[1:]))
    by[(density,lam,n)].append(row)

summaries=[]
tails=[]
site_tails=[]
for (density,lam,n),rr in sorted(by.items()):
    v=[int(r['T'])/n for r in rr]
    mean=statistics.mean(v);sd=statistics.stdev(v);se=sd/math.sqrt(len(v))
    summaries.append(dict(density=density,lambda_=lam,n=n,repetitions=len(v),
                          mean_T_over_n=mean,sd_T_over_n=sd,se_mean=se,
                          mean_ci95_low=mean-1.96*se,mean_ci95_high=mean+1.96*se,
                          median=quantile(v,.5),q90=quantile(v,.90),q95=quantile(v,.95),
                          q99=quantile(v,.99),maximum=max(v),
                          largest_site_odometer=max(int(r['max_odometer']) for r in rr),
                          unfinished=sum(int(r['finished'])!=1 for r in rr)))
    for cutoff in [.25,.3,.5,1,1.5,2,3,4,5,10,20,50,75,100,200,250,300,500,1000,2000]:
        count=sum(x>cutoff for x in v)
        tails.append(dict(density=density,lambda_=lam,n=n,cutoff_T_over_n=cutoff,
                          exceedances=count,repetitions=len(v),fraction=count/len(v)))
    for cutoff in [1,2,5,10,20,50,100,200,500,1000]:
        count=sum(int(r['sites_ge_'+str(cutoff)]) for r in rr)
        site_tails.append(dict(density=density,lambda_=lam,n=n,cutoff_site_odometer=cutoff,
                               sites_ge=count,total_sites=n*len(v),fraction=count/(n*len(v))))

def write_csv(path,entries):
    with open(path,'w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(entries[0]));w.writeheader();w.writerows(entries)
write_csv('data/summary.csv',summaries)
write_csv('data/upper_tails.csv',tails)
write_csv('data/site_tails.csv',site_tails)

checks=[]
for (density,lam) in sorted({(d,l) for d,l,n in by}):
    rr=[r for (d,l,n),values in by.items() if d==density and l==lam for r in values]
    expected=density*sum(int(r['n']) for r in rr)
    observed=sum(int(r['initial_mass']) for r in rr)
    mass_z=(observed-expected)/math.sqrt(expected)
    t=sum(int(r['T']) for r in rr);j=sum(int(r['jumps']) for r in rr)
    q=1/(1+lam)
    # A stopped-instruction martingale diagnostic, not a proof or exact normal test.
    jump_z=(j-q*t)/math.sqrt(t*q*(1-q))
    checks.append(dict(density=density,lambda_=lam,mass_z=mass_z,
                       jump_instruction_martingale_z=jump_z))
    assert abs(mass_z)<6 and abs(jump_z)<6
(ROOT/'data'/'audit.json').write_text(json.dumps(dict(rows=len(rows),unique_seeds=len(seeds),
    all_counts_consistent=True,all_completed=True,diagnostics=checks,
    raw_csv_sha256=hashlib.sha256((ROOT/'data'/'runs.csv').read_bytes()).hexdigest()),indent=2)+'\n')

lookup={(s['density'],s['lambda_'],s['n']):s for s in summaries}
lines=['| ζ | λ | mean T/n, n=1,000 | mean T/n, n=100,000 (SE) | empirical q95, n=100,000 | max T/n, n=100,000 | mean ratio, large/small |',
       '|---:|---:|---:|---:|---:|---:|---:|']
for density,lam in sorted({(d,l) for d,l,n in by}):
    a=lookup[(density,lam,1000)];b=lookup[(density,lam,100000)]
    lines.append(f"| {density:g} | {lam:g} | {a['mean_T_over_n']:.4f} | {b['mean_T_over_n']:.4f} ({b['se_mean']:.4f}) | {b['q95']:.4f} | {b['maximum']:.4f} | {b['mean_T_over_n']/a['mean_T_over_n']:.3f} |")
(ROOT/'data'/'report_table.txt').write_text('\n'.join(lines)+'\n')

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
params=sorted({(d,l) for d,l,n in by})
fig,axs=plt.subplots(4,2,figsize=(11,12),layout='constrained')
for ax,(density,lam) in zip(axs.flat,params):
    ss=sorted([s for s in summaries if s['density']==density and s['lambda_']==lam],key=lambda s:s['n'])
    ns=[s['n'] for s in ss]
    ax.errorbar(ns,[s['mean_T_over_n'] for s in ss],
                yerr=[1.96*s['se_mean'] for s in ss],label='mean, approximate 95% CI',marker='o',capsize=3)
    ax.plot(ns,[s['q95'] for s in ss],label='empirical 95th percentile',marker='s',linestyle='--')
    ax.set_xscale('log');ax.set_title(f'density {density:g}, sleep rate {lam:g}')
    ax.set_xlabel('cycle sites n');ax.set_ylabel('instructions / site (T/n)')
    ax.grid(alpha=.2)
axs.flat[-1].axis('off')
handles,labels=axs.flat[0].get_legend_handles_labels()
axs.flat[-1].legend(handles,labels,loc='center')
fig.suptitle('ARW on the cycle: Poisson initial particles, all instruction attempts counted')
fig.savefig('data/size_scaling.svg')
if '--preview' in sys.argv:
    fig.savefig('data/size_scaling_preview.png',dpi=100)
plt.close(fig)
fig,ax=plt.subplots(figsize=(8,5),layout='constrained')
for density,lam in params:
    ss=sorted([s for s in summaries if s['density']==density and s['lambda_']==lam],key=lambda s:s['n'])
    base=ss[0]['mean_T_over_n']
    ax.plot([s['n'] for s in ss],[s['mean_T_over_n']/base for s in ss],marker='o',
            label=f'density {density:g}, sleep {lam:g}')
ns=[1000,3000,10000,30000,100000]
ax.plot(ns,[math.log(n)/math.log(1000) for n in ns],color='black',linestyle=':',label='pure log(n) growth, normalized')
ax.axhline(1,color='gray',linestyle='--',linewidth=.7)
ax.set_xscale('log');ax.set_xlabel('cycle sites n')
ax.set_ylabel('mean(T/n), relative to n = 1000')
ax.set_title('Finite-size comparison; this does not decide an asymptotic theorem')
ax.grid(alpha=.2);ax.legend(fontsize=8)
fig.savefig('data/normalized_scaling.svg')
plt.close(fig)
print('\n'.join(lines))
print('Audited',len(rows),'independent runs; raw-count diagnostics saved in data/audit.json')
