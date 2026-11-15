"""Summarize independent fields, finite-range slopes and their uncertainty."""
import os
for _var in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS',
             'VECLIB_MAXIMUM_THREADS','NUMEXPR_NUM_THREADS']:
    os.environ[_var]='1'
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
os.environ['MPLCONFIGDIR']=str(ROOT/'data'/'.mplconfig')
os.environ['XDG_CACHE_HOME']=str(ROOT/'data'/'.cache')
import csv
import json
import numpy as np
from scipy.stats import skew, kurtosis, norm
from scipy.optimize import curve_fit
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def read(path):
    return np.genfromtxt(path,delimiter=',',names=True)

s=read(ROOT/'data'/'samples_main.csv')
if (ROOT/'data'/'metadata_calibration.json').exists():
    metadata=json.loads((ROOT/'data'/'metadata_calibration.json').read_text())
    if 'finished' in metadata:
        s=np.concatenate([s,read(ROOT/'data'/'samples_calibration.csv')])
e=read(ROOT/'data'/'exact_means.csv')
lams=np.unique(s['lambda'])
rng=np.random.default_rng(2026111303)
summ=[];fits=[]
for lam in lams:
    for N in np.unique(s['N']):
        z=s[(s['lambda']==lam)&(s['N']==N)]
        x=z['X'];y=z['Y'];d=x-y;L=np.log(N)
        ex=e[(e['lambda']==lam)&(e['N']==N)]['EX'][0]
        summ.append(dict(N=int(N),**{'lambda':lam},n=len(z),mean=float(x.mean()),
            mean_se=float(x.std(ddof=1)/np.sqrt(len(z))),variance=float(x.var(ddof=1)),
            exact_mean=float(ex),mean_z_score=float((x.mean()-ex)/(x.std(ddof=1)/np.sqrt(len(z)))),
            skewness=float(skew(x,bias=False)),excess_kurtosis=float(kurtosis(x,bias=False)),
            q05=float(np.quantile(x,.05)),q50=float(np.median(x)),q95=float(np.quantile(x,.95)),
            RMSE_X_Y=float(np.mean(d*d)**.5),scaled_RMSE=float(L*np.mean(d*d)**.5),
            D_mean=float(z['D'].mean()),D_sd=float(z['D'].std(ddof=1)),
            D_skewness=float(skew(z['D'],bias=False)),Q_mean=float(z['Q'].mean()),
            RMSE_D_Q=float(np.mean((z['D']-z['Q'])**2)**.5)))
    # Exclude grids with fewer than 60 fields. Slopes are descriptive finite-N
    # fits, not estimators with an established limiting distribution.
    ns=np.array([256,512,1024,2048])
    groups=[s[(s['lambda']==lam)&(s['N']==N)] for N in ns]
    loglog=np.log(np.log(ns))
    rmse=np.array([np.mean((z['X']-z['Y'])**2)**.5 for z in groups])
    bias=np.array([e[(e['lambda']==lam)&(e['N']==N)]['m'][0]-
                   e[(e['lambda']==lam)&(e['N']==N)]['EX'][0] for N in ns])
    exponent=-np.polyfit(loglog,np.log(rmse),1)[0]
    slopes=[]
    for b in range(500):
        rr=[]
        for z in groups:
            d=(z['X']-z['Y'])[rng.integers(0,len(z),len(z))]
            rr.append(np.mean(d*d)**.5)
        slopes.append(-np.polyfit(loglog,np.log(rr),1)[0])
    fits.append(dict(**{'lambda':float(lam)},N_range=ns.tolist(),
                     effective_RMSE_log_exponent=float(exponent),
                     bootstrap_percentiles=np.quantile(slopes,[.025,.975]).tolist(),
                     exact_bias_effective_log_exponent=float(-np.polyfit(loglog,np.log(bias),1)[0]),
                     caution='descriptive finite-range fit; rare-tail uncertainty not captured by bootstrap'))
with (ROOT/'data'/'summary.csv').open('w',newline='') as f:
    wr=csv.DictWriter(f,fieldnames=summ[0].keys());wr.writeheader();wr.writerows(summ)
(ROOT/'data'/'fits.json').write_text(json.dumps(fits,indent=2)+'\n')
print('fits',json.dumps(fits,indent=2))
for z in summ:
    if z['N'] in [512,2048]:print(z)

plt.rcParams.update({'font.size':10,'svg.fonttype':'none'})
fig,axs=plt.subplots(2,2,figsize=(10,7),constrained_layout=True)
for lam,ax in zip(lams,axs.flat):
    z=e[e['lambda']==lam]
    B=z['B'][0]
    ax.plot(np.log(z['N']),z['log_bias'],'o-',label=r'$\log N\,(E X_N-m)$')
    ax.axhline(B,color='black',ls='--',label=r'$B_\lambda$')
    ax.set(title=rf'$\lambda={lam:g}$',xlabel=r'$\log N$',ylabel='scaled mean bias')
    ax.legend(fontsize=8)
fig.savefig(ROOT/'data'/'mean_bias.svg');plt.close(fig)

fig,axs=plt.subplots(1,2,figsize=(10,4),constrained_layout=True)
for lam in lams:
    z=[v for v in summ if v['lambda']==lam and v['N']<=2048]
    axs[0].loglog([np.log(v['N']) for v in z],[v['RMSE_X_Y'] for v in z],'o-',label=f'{lam:g}')
    axs[1].plot([np.log(v['N']) for v in z],[v['scaled_RMSE'] for v in z],'o-',label=f'{lam:g}')
axs[0].set(xlabel=r'$\log N$',ylabel='RMSE of count minus lattice chaos')
axs[1].set(xlabel=r'$\log N$',ylabel=r'$\log N$ times RMSE')
for ax in axs:ax.legend(title=r'$\lambda$');ax.grid(alpha=.2)
fig.savefig(ROOT/'data'/'comparison_rate.svg');plt.close(fig)

fig,axs=plt.subplots(2,2,figsize=(10,7),constrained_layout=True)
for lam,ax in zip(lams,axs.flat):
    for N in [128,512,2048]:
        x=np.sort(s[(s['lambda']==lam)&(s['N']==N)]['X'])
        ax.step(x,np.arange(1,len(x)+1)/len(x),where='post',label=f'N={N}')
    ax.set(title=rf'$\lambda={lam:g}$',xlabel='normalized level-set size',ylabel='empirical CDF',xscale='log')
    ax.legend(fontsize=8);ax.grid(alpha=.2)
fig.savefig(ROOT/'data'/'level_size_ecdf.svg');plt.close(fig)

fig,axs=plt.subplots(1,2,figsize=(10,4),constrained_layout=True)
for lam,ax in zip([.2,.4],axs):
    z=s[(s['lambda']==lam)&(s['N']==512)]['D']
    z=(z-z.mean())/z.std(ddof=1)
    ax.plot(norm.ppf((np.arange(len(z))+.5)/len(z)),np.sort(z),'.')
    ax.plot([-3,3],[-3,3],'k--')
    ax.set(title=rf'$\lambda={lam:g}, N=512$',xlabel='standard Gaussian quantile',ylabel='standardized lattice residual quantile')
fig.savefig(ROOT/'data'/'residual_qq.svg');plt.close(fig)
