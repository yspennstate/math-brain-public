"""Trajectory-level uncertainty and finite-time decay fits; no asymptotic inference."""
import os
for key in ['OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','VECLIB_MAXIMUM_THREADS','MKL_NUM_THREADS']:
    os.environ[key]='1'
from pathlib import Path
os.environ["MPLCONFIGDIR"]=str(Path(__file__).resolve().parents[1]/"data"/"mpl_cache")
os.environ["XDG_CACHE_HOME"]=str(Path(__file__).resolve().parents[1]/"data"/"cache")
import csv, json, math
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
ROOT=Path(__file__).resolve().parents[1]

def load(path):
    x=np.genfromtxt(path,delimiter=',',names=True)
    reps=np.unique(x['rep']).astype(int);times=np.unique(x['time'])
    values={k:x[k].reshape(len(reps),len(times)) for k in x.dtype.names[2:]}
    assert np.all(x['rep'].reshape(len(reps),-1)==reps[:,None])
    assert np.all(x['time'].reshape(len(reps),-1)==times)
    return times,values

def fit(times, samples, equilibrium, q, seed, interval=None):
    mean=samples.mean(0);se=samples.std(0,ddof=1)/np.sqrt(len(samples));diff=mean-equilibrium
    # Time intervals fixed before examining the numerical values.
    lo,hi=interval if interval is not None else ((8,60) if q<0.5 else (1,12))
    sign=np.sign(diff[np.where(times>=lo)[0][0]])
    mask=(times>=lo)&(times<=hi)&(sign*diff>4*se)
    tt=times[mask];dd=sign*diff[mask]
    if len(tt)<4: return {'status':'too few points','n_points':len(tt)}
    A=np.column_stack([np.ones(len(tt)),-tt]);y=np.log(dd)
    coef=np.linalg.lstsq(A,y,rcond=None)[0]
    pred=A@coef
    r2=1-np.sum((y-pred)**2)/np.sum((y-y.mean())**2)
    rng=np.random.default_rng(seed);slopes=[]
    # Resample full trajectories to preserve correlation between observation times.
    for _ in range(400):
        boot=samples[rng.integers(0,len(samples),len(samples))][:,mask].mean(0)
        residual=sign*(boot-equilibrium)
        if np.all(residual>0): slopes.append(float(np.linalg.lstsq(A,np.log(residual),rcond=None)[0][1]))
    beta_grid=np.linspace(0.25,1.75,301);loss=[];beta_coef=[]
    for beta in beta_grid:
        design=np.column_stack([np.ones(len(tt)),-tt**beta])
        b=np.linalg.lstsq(design,y,rcond=None)[0]
        loss.append(float(np.sum((y-design@b)**2)));beta_coef.append(b)
    best=int(np.argmin(loss))
    return {'status':'fit','observable':'infection indicator','fit_interval_requested':[lo,hi],
            'times_used':tt.tolist(),'n_points':len(tt),'sign':float(sign),
            'exp_rate':float(coef[1]),'exp_amplitude':float(np.exp(coef[0])),
            'rate_bootstrap_95_percentile':np.percentile(slopes,[2.5,97.5]).tolist(),
            'bootstrap_successful':len(slopes),'log_fit_R2':float(r2),
            'free_beta_logfit':float(beta_grid[best]),'free_beta_grid':[0.25,1.75],
            'exp_log_RSS':float(np.sum((y-pred)**2)),'free_beta_log_RSS':loss[best],
            'warning':'Finite time descriptive fits, correlated times, data-based 4-SE mask; no asymptotic conclusion.'}

def main():
    fig,axes=plt.subplots(2,2,figsize=(10,7),sharex='col')
    summary=[];fits={}
    for qi,q in enumerate([0.25,0.65]):
        for li,law in enumerate(['renewal','hmm']):
            path=ROOT/'data'/f'{law}_q{int(q*100):03d}.csv'
            t,vals=load(path);n=len(vals['density']);label=f'{law}, q={q}'
            for observable,eq in [('density',q),('pair',q*q),('origin',q),('origin_pair',q*q)]:
                m=vals[observable].mean(0);se=vals[observable].std(0,ddof=1)/np.sqrt(n)
                summary.extend([dict(law=law,q=q,n=n,time=float(tt),observable=observable,mean=float(mm),
                                     equilibrium=eq,difference=float(mm-eq),se=float(ss))
                                for tt,mm,ss in zip(t,m,se)])
            fit_result=fit(t,vals['density'],q,q,271100+10*qi+li);fits[label]=fit_result
            m=vals['density'].mean(0);se=vals['density'].std(0,ddof=1)/np.sqrt(n)
            ax=axes[0,qi];ax.errorbar(t,m-q,yerr=1.96*se,marker='o',markersize=3,capsize=2,label=law,color=f'C{li}')
            bx=axes[1,qi];mask=np.abs(m-q)>4*se
            bx.errorbar(t[mask],np.abs(m[mask]-q),yerr=1.96*se[mask],marker='o',markersize=3,capsize=2,label=law,color=f'C{li}')
            if fit_result['status']=='fit':
                tt=np.array(fit_result['times_used']);bx.plot(tt,fit_result['exp_amplitude']*np.exp(-fit_result['exp_rate']*tt),'--',color=f'C{li}')
        axes[0,qi].axhline(0,color='black',lw=.8);axes[0,qi].set_title(f'q = {q}')
        axes[0,qi].set_ylabel('Mean infection indicator minus q');axes[0,qi].legend()
        axes[1,qi].set_yscale('log');axes[1,qi].set_xlabel('Time (rate-one site clocks)')
        axes[1,qi].set_ylabel('Absolute deviation, >4 SE only');axes[1,qi].legend()
    fig.suptitle('FA-1f: correlated initial laws, 1,000 independent trajectories each')
    fig.tight_layout();fig.savefig(ROOT/'data'/'decay.png',dpi=160);plt.close(fig)
    with (ROOT/'data'/'summary.csv').open('w') as f:
        w=csv.DictWriter(f,fieldnames=list(summary[0]));w.writeheader();w.writerows(summary)
    (ROOT/'data'/'fits.json').write_text(json.dumps(fits,indent=2))
    checks={}
    for q in [.25,.65]:
        t,values=load(ROOT/'data'/f'equilibrium_q{int(q*100):03d}.csv')
        checks[str(q)]={}
        for observable,eq in [('density',q),('pair',q*q),('origin',q),('origin_pair',q*q)]:
            mean=values[observable].mean(0);se=values[observable].std(0,ddof=1)/np.sqrt(len(values[observable]))
            checks[str(q)][observable]={'max_abs_z':float(np.max(np.abs(mean-eq)/se)),
                                      'final_mean':float(mean[-1]),'final_se':float(se[-1])}
    # Exact gap formulas for the two stationary infinite initial laws.
    D=np.diag([.98,.62]);T=np.array([[.97,.03],[.03,.97]]);alpha=np.array([.5,.5]);one=np.ones(2)
    gaps=[]
    for r in range(21):
        length=2*r+1
        hmm=float(alpha@D@np.linalg.matrix_power(T@D,length-1)@one)
        renewal=.8*.75**(length-1)
        gaps.append({'radius':r,'renewal_empty_gap_probability':renewal,'hmm_empty_gap_probability':hmm})
    with (ROOT/'data'/'initial_gap_probabilities.csv').open('w') as f:
        w=csv.DictWriter(f,fieldnames=list(gaps[0]));w.writeheader();w.writerows(gaps)
    checks['hmm_gap_matrix_spectral_radius']=float(max(abs(np.linalg.eigvals(T@D))))
    # In finite simulations, observe the middle 256 of 1024 spins, buffer >=384.
    # Sum_{n>=384} (120)^n/n! <= first term / (1-120/385).
    log_path=384*math.log(120)-math.lgamma(385)-math.log1p(-120/385)
    checks['finite_boundary']={'tmax':60,'buffer_steps':384,'path_bound_per_observed_site':math.exp(log_path),
                               'bound_union_256_sites':256*math.exp(log_path)}
    (ROOT/'data'/'checks.json').write_text(json.dumps(checks,indent=2))
    print(json.dumps(fits,indent=2));print('Checks',json.dumps(checks,indent=2))

if __name__=="__main__":
    main()
