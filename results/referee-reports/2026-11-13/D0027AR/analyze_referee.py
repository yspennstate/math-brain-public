"""Summarise independent batches, retain signed bias, and fit fixed later windows."""
import os
from pathlib import Path
ROOT=Path(__file__).resolve().parent
os.environ.update(OMP_NUM_THREADS='1', OPENBLAS_NUM_THREADS='1',
                  VECLIB_MAXIMUM_THREADS='1', MKL_NUM_THREADS='1',
                  MPLCONFIGDIR=str(ROOT/'data'/'mpl'), XDG_CACHE_HOME=str(ROOT/'data'/'cache'))
import csv
import json
import math
import resource
import numpy as np
from scipy.optimize import least_squares
from scipy.stats import chi2
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

WINDOWS={'055':[24,32,40,48,64], '060':[20,24,32,40,48], '075':[8,10,12,16,20]}
fits={}
summary=[]
fig,axes=plt.subplots(3,2,figsize=(11,10),layout='constrained')

for row,(tag,window) in enumerate(WINDOWS.items()):
    q=int(tag)/100
    records=list(csv.DictReader((ROOT/'data'/f'confirm_q{tag}.csv').open()))
    batches=sorted({int(r['batch']) for r in records})
    times=np.array(sorted({float(r['time']) for r in records}))
    assert batches==list(range(100)), 'Confirmation run not finished'
    lookup={(int(r['batch']),float(r['time'])):int(r['origin_infected'])/int(r['n']) for r in records}
    Y=np.array([[lookup[b,t] for t in times] for b in batches])
    counts={int(r['n']) for r in records}
    assert len(counts)==1
    N=counts.pop()*len(batches)
    means=Y.mean(axis=0)
    bias=means-q
    se=np.sqrt(means*(1-means)/N)
    for t,mean,d,e in zip(times,means,bias,se):
        summary.append(dict(q=q,n=N,time=t,mean=mean,signed_bias=d,abs_bias=abs(d),se=e))
    indices=np.array([int(np.flatnonzero(times==t)[0]) for t in window])
    chosen=bias[indices]
    assert (chosen<0).all(), 'Retain crossing instead of fitting log(abs) blindly'
    tfit=times[indices]
    X=np.column_stack([np.ones(len(indices)),-tfit])
    coef=np.linalg.lstsq(X,np.log(-chosen),rcond=None)[0]
    residual=np.log(-chosen)-X@coef
    r2=1-float(residual@residual/np.sum((np.log(-chosen)-np.log(-chosen).mean())**2))
    rng=np.random.default_rng(891011+int(q*100))
    boot=[]; rejected=0
    for _ in range(2000):
        d=Y[rng.integers(0,len(batches),len(batches))][:,indices].mean(axis=0)-q
        if (d<0).all(): boot.append(np.linalg.lstsq(X,np.log(-d),rcond=None)[0][1])
        else: rejected+=1
    # A separate correlated-error check of the exact single-exponential shape.
    cov=np.cov(Y[:,indices],rowvar=False,ddof=1)/len(batches)
    lower=np.linalg.cholesky(cov)
    def whitened(z):
        prediction=-np.exp(z[0]-np.exp(z[1])*tfit)
        return np.linalg.solve(lower,prediction-chosen)
    gls=least_squares(whitened,[coef[0],math.log(coef[1])])
    chi_sq=float(gls.fun@gls.fun)
    df=len(indices)-2
    info=dict(q=q,n=N,seed=int(records[0]['seed']),times=window,
              signed_bias=chosen.tolist(),se=se[indices].tolist(),
              ols_c=float(coef[1]),ols_A=float(np.exp(coef[0])),log_r2=r2,
              batch_bootstrap_95=np.quantile(boot,[.025,.975]).tolist(),
              bootstrap_draws=2000,bootstrap_rejected=rejected,
              exact_shape_gls_c=float(np.exp(gls.x[1])),exact_shape_gls_chisq=chi_sq,
              exact_shape_gls_df=df,exact_shape_gls_approx_p=float(chi2.sf(chi_sq,df)))
    fits[tag]=info
    ax=axes[row,0]
    ax.errorbar(times,bias,yerr=1.96*se,fmt='o-',ms=3,lw=1,capsize=2)
    ax.axhline(0,color='black',lw=.7)
    ax.set_yscale('symlog',linthresh=.001)
    ax.set(title=f'q={q:g}: signed bias',xlabel='time',ylabel='E[origin infected] - q')
    ax=axes[row,1]
    resolved=np.abs(bias)>3*se
    ax.semilogy(times[resolved],np.abs(bias[resolved]),'o',ms=4,label='resolved (>3 SE)')
    unresolved=~resolved
    ax.semilogy(times[unresolved],np.maximum(np.abs(bias[unresolved]),1e-6),'o',
                markerfacecolor='none',color='grey',ms=4,label='below 3 SE')
    ax.errorbar(tfit,-chosen,yerr=1.96*se[indices],fmt='s',ms=4,color='tab:orange',capsize=2)
    grid=np.linspace(tfit[0],tfit[-1],150)
    ax.semilogy(grid,np.exp(coef[0]-coef[1]*grid),'-',color='tab:orange',
                label=f'fixed-window fit: c={coef[1]:.4f}')
    ax.axhline(3*math.sqrt(q*(1-q)/N),color='grey',ls=':',lw=1)
    ax.set(title=f'q={q:g}: absolute bias',xlabel='time',ylabel='absolute deviation',ylim=(1e-5,1))
    ax.legend(fontsize=8,loc='upper right')
    for ax in axes[row]:ax.grid(alpha=.2)

with (ROOT/'data'/'summary.csv').open('w') as stream:
    writer=csv.DictWriter(stream,fieldnames=list(summary[0]));writer.writeheader();writer.writerows(summary)
metadata=dict(fits=fits,peak_rss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
              interpretation='Fixed finite-time windows; bootstrap intervals describe Monte Carlo uncertainty only.')
(ROOT/'data'/'fits.json').write_text(json.dumps(metadata,indent=2)+'\n')
fig.suptitle('FA-1f from one infection at 0: independent confirmation runs, 5 million paths per q')
fig.savefig(ROOT/'data'/'referee_decay.svg')
print(json.dumps(metadata,indent=2))
