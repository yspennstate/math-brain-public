#!/usr/bin/env python3
"""Summarize independent-path Euler evidence; bootstrap entire paths across times."""
import os
for key in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS','NUMEXPR_NUM_THREADS']:
    os.environ[key]='1'
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
os.environ['MPLCONFIGDIR']=str(ROOT/'data'/'mplconfig')
os.environ['XDG_CACHE_HOME']=str(ROOT/'data'/'cache')
import csv
import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def read(path):
    with path.open() as f:
        return [{k:(v if k=='kernel' else float(v)) for k,v in row.items()} for row in csv.DictReader(f)]

def summarize(rows):
    result=[]
    for name in sorted({r['kernel'] for r in rows}):
        for t in sorted({r['t'] for r in rows}):
            group=[r for r in rows if r['kernel']==name and r['t']==t]
            xs=np.array([r['x'] for r in group])
            n=len(xs)
            result.append(dict(kernel=name,t=t,n=n,rms=float(np.sqrt(np.mean(xs**2))),
                mean_abs=float(np.mean(np.abs(xs))),mean_speed=float(xs.mean()/t),
                mean_abs_speed=float(np.abs(xs).mean()/t),rms_speed=float(np.sqrt(np.mean(xs**2))/t),
                mean_drift_energy_per_t=float(np.mean([r['drift_energy']/t for r in group])),
                msd_standard_error=float(np.std(xs**2,ddof=1)/np.sqrt(n))))
    return result

def write_csv(name,rows):
    with (ROOT/'data'/name).open('w') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0])); w.writeheader();w.writerows(rows)

def exponents(rows,lo,hi,bootstrap=2000):
    rng=np.random.default_rng(129)
    results=[]
    for name in sorted({r['kernel'] for r in rows}):
        times=sorted({r['t'] for r in rows if lo<=r['t']<=hi})
        seeds=sorted({r['seed'] for r in rows if r['kernel']==name})
        lookup={(r['seed'],r['t']):r['x'] for r in rows if r['kernel']==name}
        x=np.array([[lookup[s,t] for t in times] for s in seeds])
        z=np.log(np.array(times)); zc=z-z.mean()
        slope=lambda rms:float(np.log(rms)@zc/(zc@zc))
        beta=slope(np.sqrt(np.mean(x*x,axis=0)))
        samples=[]
        for _ in range(bootstrap):
            idx=rng.integers(0,len(seeds),size=len(seeds))
            samples.append(slope(np.sqrt(np.mean(x[idx]**2,axis=0))))
        ci=np.quantile(samples,[.025,.975])
        results.append(dict(kernel=name,t_min=lo,t_max=hi,rms_exponent=beta,
                            bootstrap_025=float(ci[0]),bootstrap_975=float(ci[1]),
                            independent_paths=len(seeds),bootstrap_resamples=bootstrap,
                            numerical_flag=('exclude_stiff_Euler' if any(
                                (r.get('max_negative_slope_dt',0)>2 or r['drift_step_over_dx']*r['dx']>.25)
                                for r in rows if r['kernel']==name) else 'finite_time_only')))
    return results

def main():
    main=read(ROOT/'data'/'main.csv')
    summary=summarize(main); write_csv('summary.csv',summary)
    exp=exponents(main,256,8192);write_csv('exponents.csv',exp)
    exp_late=exponents(main,1024,8192);write_csv('exponents_late.csv',exp_late)
    checks=dict(rows=len(main),max_cached_vs_direct_force_error=max(r['force_check_error'] for r in main),
                max_occupation_mass_error=max(r['mass_check_error'] for r in main),
                max_drift_step_over_dx=max(r['drift_step_over_dx'] for r in main),
                max_brownian_control_error=max(abs(r['x']-r['brownian']) for r in main if r['kernel']=='zero'))
    assert checks['max_cached_vs_direct_force_error']<1e-7
    assert checks['max_occupation_mass_error']<1e-7
    assert checks['max_brownian_control_error']==0
    (ROOT/'data'/'numerical_checks.json').write_text(json.dumps(checks,indent=2)+'\n')
    fig,axes=plt.subplots(1,2,figsize=(11,4.4))
    for name in sorted({r['kernel'] for r in summary}):
        g=[r for r in summary if r['kernel']==name]
        ts=np.array([r['t'] for r in g]);rms=np.array([r['rms'] for r in g])
        label=name+' (stiff Euler)' if name in ['bump','annular'] else name
        axes[0].loglog(ts,rms,'o-',label=label,markersize=3)
        axes[1].loglog(ts,rms/ts,'o-',label=label,markersize=3)
    ts=np.array([16.,8192.])
    axes[0].loglog(ts,ts**(2/3),'k--',lw=1,label='t^(2/3) reference')
    axes[0].set(xlabel='time',ylabel='ensemble RMS displacement',title='Finite-time Euler evidence (48 paths per kernel)')
    axes[1].set(xlabel='time',ylabel='RMS displacement / time',title='Scaled displacement')
    for a in axes:a.grid(alpha=.2,which='both')
    axes[0].legend(fontsize=8)
    fig.tight_layout();fig.savefig(ROOT/'data'/'growth.png',dpi=160);plt.close(fig)
    refinements=[]
    for filename in ['refine_coarse.csv','refine_space.csv','refine_fine.csv']:
        path=ROOT/'data'/filename
        if not path.exists():continue
        raw=read(path)
        if len(raw)!=6*32*7: continue
        out=summarize(raw)
        write_csv(filename.replace('.csv','_summary.csv'),out)
        for r in out:
            if r['t']==1024:
                r=dict(r,run=filename,dt=raw[0]['dt'],dx=raw[0]['dx']);refinements.append(r)
    if refinements:write_csv('refinement_summary.csv',refinements)
    extra={}
    for filename in ['main_fine.csv','stiff_refine.csv','annular_short.csv']:
        path=ROOT/'data'/filename
        if not path.exists():continue
        raw=read(path)
        counts={'main_fine.csv':5*64*10,'stiff_refine.csv':2*32*7,'annular_short.csv':1*32*5}
        if len(raw)!=counts[filename]:continue
        ss=summarize(raw);write_csv(filename.replace('.csv','_summary.csv'),ss)
        horizon=max(r['t'] for r in raw)
        extra[filename]=dict(final=[r for r in ss if r['t']==horizon],
            max_negative_slope_dt={name:max(r['max_negative_slope_dt'] for r in raw if r['kernel']==name)
                                   for name in sorted({r['kernel'] for r in raw})},
            max_drift_step={name:max(r['drift_step_over_dx']*r['dx'] for r in raw if r['kernel']==name)
                                   for name in sorted({r['kernel'] for r in raw})})
        if filename=='main_fine.csv':
            write_csv('main_fine_exponents.csv',exponents(raw,256,8192))
            write_csv('main_fine_exponents_late.csv',exponents(raw,1024,8192))
            fig,axes=plt.subplots(1,2,figsize=(11,4.4))
            for name in sorted({r['kernel'] for r in ss}):
                if name=='bump':continue
                g=[r for r in ss if r['kernel']==name]
                ts=np.array([r['t'] for r in g]);rms=np.array([r['rms'] for r in g])
                axes[0].loglog(ts,rms,'o-',label=name,markersize=3)
                axes[1].loglog(ts,rms/ts,'o-',label=name,markersize=3)
            ts=np.array([16.,8192.]);axes[0].loglog(ts,ts**(2/3),'k--',lw=1,label='t^(2/3) reference')
            axes[0].set(xlabel='time',ylabel='ensemble RMS displacement',title='Finer Euler mesh (64 paths per kernel)')
            axes[1].set(xlabel='time',ylabel='RMS displacement / time',title='Scaled displacement')
            for a in axes:a.grid(alpha=.2,which='both')
            axes[0].legend(fontsize=8);fig.tight_layout()
            fig.savefig(ROOT/'data'/'growth_fine.png',dpi=160);plt.close(fig)
    (ROOT/'data'/'extra_checks.json').write_text(json.dumps(extra,indent=2)+'\n')
    print(json.dumps(dict(checks=checks,exponents=exp,final=[r for r in summary if r['t']==8192],
                          refinements=refinements,extra=extra),indent=2))

if __name__=='__main__':main()
