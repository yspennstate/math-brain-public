#!/usr/bin/env python3
"""Estimate heuristic variances and paired search sensitivity, not optimal variance."""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','VECLIB_MAXIMUM_THREADS','MKL_NUM_THREADS'):
    os.environ[key]='1'
import csv
import json
import math
from pathlib import Path
import statistics
import numpy as np
from scipy.stats import chi2

ROOT=Path(__file__).resolve().parents[1]
os.environ['MPLCONFIGDIR']=str(ROOT/'data'/'matplotlib_cache')
os.environ['XDG_CACHE_HOME']=str(ROOT/'data'/'cache')
(ROOT/'data'/'matplotlib_cache').mkdir(exist_ok=True)
(ROOT/'data'/'cache').mkdir(exist_ok=True)
RNG=np.random.Generator(np.random.PCG64(300099123))

def read(name):
    with (ROOT/'data'/name).open() as f:return list(csv.DictReader(f))

def bootstrap_variance(x,reps=5000):
    x=np.asarray(x);samples=x[RNG.integers(len(x),size=(reps,len(x)))]
    vv=samples.var(axis=1,ddof=1)
    return float(vv.std(ddof=1)),[float(v) for v in np.quantile(vv,[0.025,0.975])]

def main():
    raw=read('torus_samples.csv');cal=read('calibration.csv')
    main_rows=[];pair_rows=[]
    for n in sorted({int(r['n']) for r in raw}):
        rows=[r for r in raw if int(r['n'])==n]
        assert len({int(r['index']) for r in rows})==len(rows)
        x=np.array([float(r['best']) for r in rows])
        base=np.array([min(float(r['base1']),float(r['base2'])) for r in rows])
        v=float(x.var(ddof=1));v_other=statistics.variance(map(float,x))
        assert abs(v-v_other)<1e-12
        se,ci=bootstrap_variance(x)
        startdiff=np.array([float(r['best1'])-float(r['best2']) for r in rows])
        out={'n':n,'samples':len(x),'mean_length':float(x.mean()),
             'mean_div_sqrt_n':float(x.mean()/np.sqrt(n)),
             'variance':v,'variance_second_method':v_other,
             'bootstrap_se':se,'bootstrap_95_percentile':ci,
             'variance20_epochs':float(base.var(ddof=1)),
             'mean20_to80_improvement':float((base-x).mean()),
             'half_mean_squared_start_difference':float(np.mean(startdiff**2)/2),
             'mean_2nearest_lower_bound':float(np.mean([float(r['lower_bound']) for r in rows])),
             'cap_hits':sum(int(r['cap_hits']) for r in rows),
             'solver_seconds':sum(float(r['seconds']) for r in rows),
             'max_python_rss_bytes':max(float(r['python_peak_rss_bytes']) for r in rows),
             'max_child_rss_bytes':max(float(r['child_peak_rss_bytes']) for r in rows),
             'nice_values':sorted({int(r['nice']) for r in rows})}
        main_rows.append(out)
        pairs=[r for r in cal if int(r['n'])==n]
        if len(pairs)>1:
            weak=np.array([float(r['baseline80']) for r in pairs])
            strong=np.array([float(r['combined']) for r in pairs])
            for row,ww in zip(pairs,weak):
                mainrow=next((r for r in rows if int(r['index'])==int(row['index'])),None)
                if mainrow is not None:assert abs(float(mainrow['best'])-ww)<1e-9
            delta=weak-strong
            idx=RNG.integers(len(pairs),size=(10000,len(pairs)))
            diff=strong[idx].var(axis=1,ddof=1)-weak[idx].var(axis=1,ddof=1)
            variance_delta=float(delta.var(ddof=1))
            covariance=float(np.cov(strong,delta,ddof=1)[0,1])
            assert abs(float(weak.var(ddof=1)-strong.var(ddof=1))-variance_delta-2*covariance)<1e-10
            bounds=[]
            for r in pairs:
                if r['hk_lower']:
                    lower=float(r['hk_lower']);upper=float(r['combined'])
                    bounds.append({'index':int(r['index']),'lower':lower,'upper':upper,
                                   'relative_gap_bound':upper/lower-1,
                                   'baseline_gap_bound':float(r['baseline80'])/lower-1})
            pair_rows.append({'n':n,'samples':len(pairs),'mean_improvement':float(delta.mean()),
                              'improvement_sd':float(delta.std(ddof=1)),
                              'relative_mean_improvement':float(delta.mean()/weak.mean()),
                              'variance_baseline80':float(weak.var(ddof=1)),
                              'variance_combined320':float(strong.var(ddof=1)),
                              'paired_variance_change':float(strong.var(ddof=1)-weak.var(ddof=1)),
                              'paired_variance_change_bootstrap_95':[float(z) for z in np.quantile(diff,[.025,.975])],
                              'variance_improvement':variance_delta,
                              'covariance_strong_improvement':covariance,
                              'lower_bound_checks':bounds})
    values=np.array([r['variance'] for r in main_rows]);errors=np.array([r['bootstrap_se'] for r in main_rows])
    weights=1/errors**2;constant=float(np.sum(weights*values)/np.sum(weights))
    stat=float(np.sum(weights*(values-constant)**2));df=len(main_rows)-1
    design=np.column_stack((np.ones(len(main_rows)),np.log10([r['n'] for r in main_rows])))
    cov=np.linalg.inv(design.T@(weights[:,None]*design));fit=cov@(design.T@(weights*values))
    out={'main':main_rows,'calibration':pair_rows,
         'descriptive_constant_fit':{'constant':constant,'se':float(1/np.sqrt(weights.sum())),
                                     'chi_square':stat,'df':df,'p':float(chi2.sf(stat,df))},
         'descriptive_log10_slope':{'slope':float(fit[1]),'se':float(np.sqrt(cov[1,1]))},
         'interpretation':'All variances are heuristic tour variances. Bootstrap intervals exclude solver bias. Fits are descriptive over the tested sizes.'}
    (ROOT/'data'/'analysis.json').write_text(json.dumps(out,indent=2))
    with (ROOT/'data'/'variance_summary.csv').open('w') as f:
        keys=['n','samples','mean_div_sqrt_n','variance','bootstrap_se','variance20_epochs','mean20_to80_improvement','half_mean_squared_start_difference']
        writer=csv.DictWriter(f,fieldnames=keys);writer.writeheader()
        writer.writerows({k:r[k] for k in keys} for r in main_rows)
    print(json.dumps(out,indent=2))
    # Plot only original numerical results: no paper images or scans.
    try:
        import matplotlib
        matplotlib.use('Agg')
        import matplotlib.pyplot as plt
        n=np.array([r['n'] for r in main_rows])
        fig,axes=plt.subplots(1,2,figsize=(10,4),layout='constrained')
        axes[0].errorbar(n,values,yerr=1.96*errors,fmt='o-',label='80 epochs, best of 2 starts')
        axes[0].plot(n,[r['variance20_epochs'] for r in main_rows],'s--',label='20-epoch checkpoint')
        axes[0].set(xscale='log',xlabel='Number of points n',ylabel='Sample variance of heuristic length')
        axes[0].legend(fontsize=8);axes[0].grid(alpha=.2)
        axes[1].plot(n,[r['mean_div_sqrt_n'] for r in main_rows],'o-')
        axes[1].set(xscale='log',xlabel='Number of points n',ylabel='Mean heuristic length / sqrt(n)')
        axes[1].grid(alpha=.2)
        fig.suptitle('Flat unit torus: heuristic tours; bars show sampling uncertainty only')
        fig.savefig(ROOT/'data'/'variance_trend.svg')
        plt.close(fig)
    except ImportError:
        print('matplotlib unavailable; numeric artifacts saved')

if __name__=='__main__':main()
