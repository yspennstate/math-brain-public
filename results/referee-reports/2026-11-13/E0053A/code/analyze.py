#!/usr/bin/env python3
"""Paired sampling CIs and finite-size sensitivity, with no optimizer-error claim."""
import os
for k in ['OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','VECLIB_MAXIMUM_THREADS','MKL_NUM_THREADS']:os.environ[k]='1'
import collections,csv,json,math,pathlib
os.environ['MPLCONFIGDIR']=str(pathlib.Path(__file__).resolve().parents[1]/'data'/'mplconfig')
os.environ['XDG_CACHE_HOME']=str(pathlib.Path(__file__).resolve().parents[1]/'data'/'cache')
import numpy as np
from scipy.stats import t
ROOT=pathlib.Path(__file__).resolve().parents[1];DATA=ROOT/'data'
def read(mode):
    p=DATA/f'{mode}.jsonl'
    return [json.loads(l) for l in p.read_text().splitlines()] if p.exists() else []
def summarize(rows,mode):
    groups=collections.defaultdict(list)
    for r in rows:groups[(r['d'],r['n'])].append(r)
    result=[]
    for (d,n),rr in sorted(groups.items()):
        a=np.array([[r['min']/n,r['max']/n,(r['min']+r['max'])/n-d/2] for r in rr]);means=a.mean(axis=0)
        ses=a.std(axis=0,ddof=1)/len(rr)**.5 if len(rr)>1 else np.full(3,np.nan)
        ci=t.ppf(.975,len(rr)-1)*ses if len(rr)>1 else np.full(3,np.nan)
        ci=np.where(ses>0,ci,np.nan)
        result.append(dict(mode=mode,d=d,n=n,samples=len(rr),**{name:float(means[j]) for j,name in enumerate(['min_mean','max_mean','delta_mean'])},**{name:float(ses[j]) for j,name in enumerate(['min_se','max_se','delta_se'])},**{name:(float(ci[j]) if np.isfinite(ci[j]) else None) for j,name in enumerate(['min_ci95_half','max_ci95_half','delta_ci95_half'])}))
    return result

def fit(rows,mode):
    rng=np.random.default_rng(530053)
    result=[]
    for d in [3,4,5]:
      for nmin in [128,256,512,1024]:
        groups=collections.defaultdict(list)
        for r in rows:
            if r['d']==d and r['n']>=nmin:groups[r['n']].append(r)
        groups={n:rr for n,rr in groups.items() if len(rr)>=2}
        ns=np.array(sorted(groups),dtype=float)
        if len(ns)<4:continue
        # Bootstrap paired min/max observations within each fixed graph-size group.
        bootstrap=[];means=[];ses=[]
        for n in ns:
            rr=groups[int(n)];arr=np.array([[r['min']/n,r['max']/n,(r['min']+r['max'])/n-d/2] for r in rr])
            means.append(arr.mean(axis=0));ses.append(arr.std(axis=0,ddof=1)/len(arr)**.5)
            bootstrap.append(arr[rng.integers(0,len(arr),size=(1000,len(arr)))].mean(axis=1))
        means=np.array(means);ses=np.array(ses);boots=np.array(bootstrap)
        for powers in [(.5,),(2/3,),(.85,),(1.,),(2/3,1.)]:
            X=np.column_stack([np.ones(len(ns)),*[ns**(-p) for p in powers]])
            for j,metric in enumerate(['min','max','delta']):
                # One crossing-edge parity step is two edges; avoid infinite weight
                # for a zero sample variance, and never pretend that it is exact.
                sig=np.maximum(ses[:,j],1/ns/np.sqrt([len(groups[int(n)]) for n in ns]))
                weighted=X/sig[:,None];inverse=np.linalg.pinv(weighted)
                beta=np.sum(inverse*(means[:,j]/sig)[None,:],axis=1)
                estimates=np.sum((inverse[0]/sig)[:,None]*boots[:,:,j],axis=0)
                assert np.all(np.isfinite(estimates))
                low,high=np.quantile(estimates,[.025,.975])
                chi2=float(np.sum(((means[:,j]-np.sum(X*beta[None,:],axis=1))/sig)**2))
                result.append(dict(mode=mode,d=d,nmin=nmin,nmax=int(ns[-1]),sizes=len(ns),metric=metric,powers=list(powers),limit=float(beta[0]),bootstrap95_low=float(low),bootstrap95_high=float(high),chi2=chi2,dof=len(ns)-X.shape[1]))
    return result

def main():
    allrows={mode:read(mode) for mode in ['small','large','deep','sa']};summary=[];fits=[]
    main_by={(r['d'],r['n'],r['instance']):r for r in allrows['large']}
    pooled=[]
    for r in allrows['deep']:
        old=main_by.get((r['d'],r['n'],r['instance']))
        if old:
            pooled.append(dict(d=r['d'],n=r['n'],instance=r['instance'],min=min(old['min'],r['min']),max=max(old['max'],r['max']),main_trace=old['trace'],deep_trace=r['trace']))
    allrows['pooled']=pooled
    (DATA/'pooled.jsonl').write_text(''.join(json.dumps(r)+'\n' for r in pooled))
    for mode,rows in allrows.items():
        summary+=summarize(rows,mode)
        if mode in ['large','deep','pooled']:
            fits+=fit(rows,mode)
            for cap in [1024,2048,4096]:
                if rows and max(r['n'] for r in rows)>cap:
                    fits+=fit([r for r in rows if r['n']<=cap],mode+'_window')
    (DATA/'summary.json').write_text(json.dumps(summary,indent=2)+'\n');(DATA/'fits.json').write_text(json.dumps(fits,indent=2)+'\n')
    if summary:
        with (DATA/'summary.csv').open('w') as f:
            w=csv.DictWriter(f,fieldnames=list(summary[0]));w.writeheader();w.writerows(summary)
    # Matched graph comparisons measure an observed budget effect, not a bound
    # on the remaining gap to the unknown optima.
    main_by={(r['d'],r['n'],r['instance']):r for r in allrows['large']};comparisons=[]
    for mode in ['deep','sa']:
      grouped=collections.defaultdict(list)
      for r in allrows[mode]:
        old=main_by.get((r['d'],r['n'],r['instance']))
        if old:
            n=r['n'];new_min=min(old['min'],r['min']);new_max=max(old['max'],r['max'])
            grouped[(r['d'],n)].append([(old['min']-new_min)/n,(new_max-old['max'])/n,((new_min+new_max)-(old['min']+old['max']))/n])
      for (d,n),a in sorted(grouped.items()):
        arr=np.array(a);comparisons.append(dict(mode=mode,d=d,n=n,samples=len(a),mean_min_improvement=float(arr[:,0].mean()),mean_max_improvement=float(arr[:,1].mean()),mean_delta_shift=float(arr[:,2].mean()),largest_individual_endpoint_change=float(abs(arr[:,:2]).max())))
    (DATA/'budget_comparisons.json').write_text(json.dumps(comparisons,indent=2)+'\n')
    # Standalone research plot, suitable for export.
    import matplotlib;matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    fig,axes=plt.subplots(2,3,figsize=(12,7),sharex='col')
    for j,d in enumerate([3,4,5]):
        for mode,color,marker in [('large','#2166ac','o'),('pooled','#b2182b','s'),('sa','#636363','^')]:
            rr=[r for r in summary if r['d']==d and r['mode']==mode]
            if not rr:continue
            ns=[r['n'] for r in rr]
            axes[0,j].errorbar(ns,[r['min_mean'] for r in rr],yerr=[r['min_ci95_half'] if r['min_ci95_half'] is not None else np.nan for r in rr],label=mode+' MinBis',color=color,marker=marker,ms=3,lw=1)
            axes[0,j].errorbar(ns,[d/2-r['max_mean'] for r in rr],yerr=[r['max_ci95_half'] if r['max_ci95_half'] is not None else np.nan for r in rr],label=mode+' d/2-MaxBis',color=color,marker=marker,ms=3,lw=1,ls='--',alpha=.65)
            axes[1,j].errorbar(ns,[r['delta_mean'] for r in rr],yerr=[r['delta_ci95_half'] if r['delta_ci95_half'] is not None else np.nan for r in rr],label=mode,color=color,marker=marker,ms=3,lw=1)
        axes[0,j].set_title(f'd = {d}');axes[1,j].axhline(0,color='black',lw=.8);axes[1,j].set_xlabel('n')
        axes[0,j].set_xscale('log',base=2);axes[1,j].set_xscale('log',base=2)
        axes[0,j].grid(alpha=.2);axes[1,j].grid(alpha=.2)
    axes[0,0].set_ylabel('Cut density / complementary density');axes[1,0].set_ylabel('(best max + best min)/n - d/2')
    axes[0,2].legend(fontsize=7);axes[1,2].legend(fontsize=8)
    fig.suptitle('Heuristic bisections: 95% sampling intervals; optimization error excluded',fontsize=12);fig.tight_layout()
    fig.savefig(DATA/'bisections.pdf');fig.savefig(DATA/'bisections.png',dpi=160);plt.close(fig)
    def fmt(x):return 'not estimable' if x is None else f'{x:.7f}'
    lines=['# Numerical tables','', 'Intervals below are Student-t 95% sampling intervals for algorithm outputs. They do not include optimization bias. Identical observations give an unestimable interval, not evidence of zero population variance.','', '| mode | d | n | graphs | best MinBis/n | best MaxBis/n | sum/n-d/2 |','|---|---:|---:|---:|---:|---:|---:|']
    for r in summary:
        lines.append(f"| {r['mode']} | {r['d']} | {r['n']} | {r['samples']} | {r['min_mean']:.7f} ± {fmt(r['min_ci95_half'])} | {r['max_mean']:.7f} ± {fmt(r['max_ci95_half'])} | {r['delta_mean']:+.7f} ± {fmt(r['delta_ci95_half'])} |")
    (DATA/'NUMERICS.md').write_text('\n'.join(lines)+'\n')
    print('summaries',len(summary),'fits',len(fits),'budget comparisons',len(comparisons))
if __name__=='__main__':main()
