"""Descriptive finite-size fits with conditional bootstrap intervals; no proof claims."""
import os
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
os.environ['MPLCONFIGDIR']=str(ROOT/'data'/'matplotlib-cache')
os.environ['XDG_CACHE_HOME']=str(ROOT/'data'/'cache')
from simulate import governor
import csv,json,math
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def main():
    governor()
    data=ROOT/'data'
    with (data/'summary.csv').open() as f: summary=list(csv.DictReader(f))
    with (data/'trials.csv').open() as f: trials=list(csv.DictReader(f))
    families=list(dict.fromkeys(r['family'] for r in summary))
    rng=np.random.default_rng(601113)
    fits=[]
    fig,axes=plt.subplots(2,4,figsize=(15,8),constrained_layout=True)
    for family,ax in zip(families,axes.flat):
        rows=sorted((r for r in summary if r['family']==family),key=lambda x:int(x['n']))
        x=np.array([float(r['n']) for r in rows]);y=np.array([float(r['median']) for r in rows])
        lo=np.array([float(r['q10']) for r in rows]);hi=np.array([float(r['q90']) for r in rows])
        logx=np.log(x);coef=np.polyfit(logx,np.log(y),1)
        pred=np.exp(np.polyval(coef,logx))
        r2=1-np.sum((np.log(y)-np.log(pred))**2)/np.sum((np.log(y)-np.log(y).mean())**2)
        groups=[np.array([float(t['largest']) for t in trials if t['family']==family and int(t['n'])==int(n)]) for n in x]
        bs=[]
        for _ in range(1000):
            med=np.array([np.median(rng.choice(g,len(g),replace=True)) for g in groups])
            bs.append(float(np.polyfit(logx,np.log(med),1)[0]))
        boot=np.quantile(bs,[.025,.975])
        lc=np.polyfit(logx,y,1);lp=np.polyval(lc,logx)
        row={'family':family,'host_sizes':len(x),'min_n':int(x[0]),'max_n':int(x[-1]),
             'power_exponent':float(coef[0]),'power_prefactor':float(np.exp(coef[1])),
             'bootstrap_95_low':float(boot[0]),'bootstrap_95_high':float(boot[1]),
             'log_space_r2':float(r2),'power_original_scale_rmse':float(np.sqrt(np.mean((pred-y)**2))),
             'affine_log_slope':float(lc[0]),'affine_log_intercept':float(lc[1]),
             'affine_log_original_scale_rmse':float(np.sqrt(np.mean((lp-y)**2))),
             'largest_n_median':float(y[-1]),'largest_n_q10':float(lo[-1]),'largest_n_q90':float(hi[-1])}
        fits.append(row)
        ax.errorbar(x,y,yerr=[y-lo,hi-y],fmt='o',capsize=3,label='median; 10–90%')
        ax.plot(x,pred,'--',label=f'power fit: {coef[0]:.3f}')
        ax.set_xscale('log');ax.set_yscale('log');ax.set_title(family.replace('_',' '),fontsize=10)
        ax.set_xlabel('host vertices n');ax.set_ylabel('largest component');ax.grid(alpha=.2);ax.legend(fontsize=8)
    axes.flat[-1].axis('off')
    axes.flat[-1].text(0,1,'Exact Bernoulli bond percolation\n40 trials per host\nError bars: empirical 10–90%\n\nPower fits describe finite sizes.\nThey do not establish asymptotic exponents.\n\nε = 0.2 except near-regular ε = 0.1',va='top',fontsize=12)
    fig.suptitle('G0010 simulation evidence',fontsize=16)
    fig.savefig(data/'scaling.svg');plt.close(fig)
    with (data/'fits.csv').open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(fits[0]));w.writeheader();w.writerows(fits)
    (data/'fit_notes.txt').write_text(
      'Fits use all available sizes, including small graphs, and log median L1 versus log n.\n'
      'Bootstrap: 1000 independent resamples of the 40 percolation realizations at each fixed host.\n'
      'Intervals measure conditional Monte Carlo variability only. They exclude host randomness,\n'
      'systematic finite-size bias, and uncertainty in any asymptotic power-law model.\n'
      'The near-regular constructions have very small proven exponents; these simulations\n'
      'cannot distinguish their eventual polynomial behavior from slow polylogarithmic growth.\n'
      'Each planted-hub host is fixed for its 40 repeats; seeds and adjacency hashes are in hosts.json.\n')
    print(json.dumps(fits,indent=2))

if __name__=='__main__':main()
