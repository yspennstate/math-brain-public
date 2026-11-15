"""Independent finite-state checks, proof diagnostics, and simulation summaries."""
import os
os.environ.setdefault('XDG_CACHE_HOME', os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'data', 'cache'))
os.environ.setdefault('MPLCONFIGDIR', os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'data', 'mplconfig'))
for key in ['OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS']:
    os.environ[key]='1'
if os.getpriority(os.PRIO_PROCESS,0)<10:
    os.setpriority(os.PRIO_PROCESS,0,10)
import csv
import itertools
import json
import math
import resource
import time
import warnings
from pathlib import Path
import numpy as np
from scipy.linalg import expm
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

ROOT=Path(__file__).resolve().parents[1]
DATA=ROOT/'data'

def independent_checks():
    rates=np.array([.3,.55,.9]); N=4
    states=[x for x in itertools.product(range(N+1),repeat=3) if sum(x)==N]
    ix={x:i for i,x in enumerate(states)}
    Q=np.zeros((len(states),len(states)))
    for state,i in ix.items():
        for k in range(3):
            if state[k]:
                target=list(state); target[k]-=1; target[(k+1)%3]+=1
                Q[i,ix[tuple(target)]]+=rates[k]
                Q[i,i]-=rates[k]
    weights=np.array([np.prod(rates**(-np.array(x))) for x in states]); weights/=weights.sum()
    balance=float(abs(weights@Q).max())
    # Enumerate the independent geometric construction, conditioned on bulk <= N.
    q=rates[0]/rates[1:]
    geometric=np.array([np.prod((1-q)*q**np.array(x[1:])) for x in states]);geometric/=geometric.sum()
    geom_error=float(abs(geometric-weights).max())
    # A positive Poisson series checks the matrix exponential independently.
    rate=float(-Q.diagonal().min())
    P=np.eye(len(states))+Q/rate
    term=np.eye(len(states))[ix[(2,1,1)]]
    weight=math.exp(-20*rate)
    expected=weight*term
    weight_sum=weight
    for k in range(1,240):
        term=term@P;weight*=20*rate/k
        expected+=weight*term;weight_sum+=weight
    assert abs(weight_sum-1)<1e-13 and abs(expected.sum()-1)<1e-13
    with warnings.catch_warnings(record=True) as warning_list:
        warnings.simplefilter('always')
        matrix_expected=expm(20*Q)[ix[(2,1,1)]]
    assert np.all(np.isfinite(matrix_expected))
    matrix_error=float(abs(expected-matrix_expected).max())
    assert matrix_error<1e-12
    rows=list(csv.DictReader((DATA/'tiny_endpoints.csv').open()))
    empirical=np.array([next(int(row['count']) for row in rows if tuple(int(row[f'n{k}']) for k in range(3))==x) for x in states])/50000
    tv=float(abs(empirical-expected).sum()/2)
    z=np.abs(empirical-expected)/np.sqrt(np.maximum(expected*(1-expected),1e-12)/50000)
    assert balance<1e-12 and geom_error<1e-12
    assert z.max()<6, (z.max(),tv)
    result=dict(states=len(states),trajectories=50000,time=20,stationary_balance_max_error=balance,
                geometric_representation_max_error=geom_error,transient_TV_error=tv,max_standardized_error=float(z.max()),
                poisson_series_vs_matrix_exponential_max_error=matrix_error,
                matrix_exponential_warnings=[str(w.message) for w in warning_list])
    (DATA/'verification.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result),flush=True)

def proof_diagnostics():
    rng=np.random.default_rng(481102)
    rows=[];c=.3;s=.7
    for kappa in [1.5,2.,3.]:
        rho_c=c*kappa/(s*(kappa-1))
        for L in [64,256,1024,4096]:
            for rep in range(300):
                rates=c+s*rng.random(L)**(1/kappa)
                order=np.argsort(rates);i=order[0]
                mask=np.arange(L)!=i
                X=rng.geometric(1-rates[i]/rates[mask])-1
                N=round((rho_c+2)*L)
                rows.append(dict(kappa=kappa,L=L,rep=rep,rho_c=rho_c,bulk_density=X.sum()/L,
                                 bulk_max=X.max()/L,reject=int(X.sum()>N),
                                 min_scaled=L**(1/kappa)*(rates[i]-c)/s,
                                 gap=rates[order[1]]-rates[i]))
    with (DATA/'bulk_diagnostics.csv').open('w') as f:
        w=csv.DictWriter(f,fieldnames=rows[0]);w.writeheader();w.writerows(rows)
    out=[]
    for kappa in [1.5,2.,3.]:
        for L in [64,256,1024,4096]:
            group=[r for r in rows if r['kappa']==kappa and r['L']==L]
            b=np.array([r['bulk_density'] for r in group])
            out.append(dict(kappa=kappa,L=L,replicates=len(group),rho_c=group[0]['rho_c'],
                            median_bulk=float(np.median(b)),q10_bulk=float(np.quantile(b,.1)),q90_bulk=float(np.quantile(b,.9)),
                            rejection_probability=float(np.mean([r['reject'] for r in group]))))
    (DATA/'bulk_summary.json').write_text(json.dumps(out,indent=2)+'\n')

def analyze():
    rows=list(csv.DictReader((DATA/'dynamics.csv').open()))
    for r in rows:
        for k in r:r[k]=float(r[k])
        assert r['N']==r['total']
    # Verify raw snapshots and all rank-based measurements independently of C++.
    rates_by_run={}
    for r in csv.DictReader((DATA/'rates.csv').open()):
        rates_by_run.setdefault(int(r['run']),[]).append(float(r['rate']))
    snapshots=[json.loads(x) for x in (DATA/'states.jsonl').read_text().splitlines()]
    assert len(snapshots)==len(rows)
    for snap,r in zip(snapshots,rows):
        n=np.array(snap['eta']);rates=np.array(rates_by_run[snap['run']]);order=np.argsort(rates)
        assert n.sum()==r['N'] and n.min()>=0
        assert n[order[0]]==r['slowest_mass']
        assert n[order[:5]].sum()==r['top5_mass']
        assert n[order[:10]].sum()==r['top10_mass']
        ranks=np.empty(len(rates),dtype=int);ranks[order]=np.arange(1,len(rates)+1)
        assert int(n.argmax())==r['max_index']
        assert n.max()==r['max_mass'] and ranks[n.argmax()]==r['max_rate_rank']
        slow=rates<=.3+.7*len(rates)**(-1/(2*r['kappa']))
        assert slow.sum()==r['slowset_count'] and n[slow].sum()==r['slowset_mass']
        baseline=(.3/(rates[slow]-.3)).sum()
        excess=(n[slow].sum()-baseline)/(r['N']-r['rho_c']*len(rates))
        assert abs(excess-r['slowset_excess_estimate'])<1e-11
    result=[]
    for kappa in [1.5,2.,3.]:
        for L in [128,384]:
            for tau in sorted(set(r['tau'] for r in rows)):
                group=[r for r in rows if r['kappa']==kappa and r['L']==L and r['tau']==tau]
                denom=[r['N']-r['rho_c']*L for r in group]
                result.append(dict(kappa=kappa,L=L,tau=tau,replicates=len(group),
                    slowest_over_excess_mean=float(np.mean([r['slowest_mass']/d for r,d in zip(group,denom)])),
                    slowest_over_excess_median=float(np.median([r['slowest_mass']/d for r,d in zip(group,denom)])),
                    max_at_min_rate=float(np.mean([r['max_rate_rank']==1 for r in group])),
                    max_at_top5_rate=float(np.mean([r['max_rate_rank']<=5 for r in group])),
                    slowset_excess_estimate=float(np.mean([r['slowset_excess_estimate'] for r in group])),
                    bulk_density=float(np.mean([r['bulk_density'] for r in group]))))
    (DATA/'dynamics_summary.json').write_text(json.dumps(result,indent=2)+'\n')
    fig,axes=plt.subplots(1,3,figsize=(12,3.4),layout='constrained')
    for ax,kappa in zip(axes,[1.5,2.,3.]):
        for L in [128,384]:
            group=[r for r in result if r['kappa']==kappa and r['L']==L and r['tau']>0]
            ax.plot([r['tau'] for r in group],[r['slowest_over_excess_mean'] for r in group],'-o',ms=3,label=f'L={L}')
        ax.axhline(1,color='0.6',lw=1,ls='--');ax.set_xscale('log')
        ax.set_title(f'Rate-tail exponent kappa={kappa:g}')
        ax.set_xlabel('t / L^(1+1/kappa)');ax.set_ylabel('Mean mass at slowest / excess');ax.legend()
    fig.savefig(DATA/'concentration.svg');plt.close(fig)
    # A spatial profile from one specified path, without selecting for successful condensation.
    run=12;chosen=[x for x in snapshots if x['run']==run and x['tau'] in [0,.1,1,4]]
    rates=np.array(rates_by_run[run]);order=np.argsort(rates)
    fig,axes=plt.subplots(4,1,figsize=(10,7),sharex=True,layout='constrained')
    for ax,snap in zip(axes,chosen):
        ax.bar(range(len(rates)),snap['eta'],width=1,color='#415a77')
        for i in order[:5]:ax.axvline(i,color='#c65d3b',lw=.7,alpha=.7)
        ax.set_ylabel('Particles');ax.set_title(f'run={run}, tau={snap["tau"]:g}')
    axes[-1].set_xlabel('Site; red lines mark the five slowest service rates')
    fig.savefig(DATA/'profile.svg');plt.close(fig)
    print('Final dynamic summaries:',json.dumps([r for r in result if r['tau']==4]),flush=True)

if __name__=='__main__':
    started=time.perf_counter()
    independent_checks();proof_diagnostics();analyze()
    (DATA/'resources.json').write_text(json.dumps(dict(elapsed_seconds=time.perf_counter()-started,
        max_rss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
        nice=os.getpriority(os.PRIO_PROCESS,0),numerical_threads=1),indent=2)+'\n')
