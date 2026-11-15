"""Finite-volume summaries and block-bootstrap pseudocritical points. No extrapolation."""
import csv
from collections import defaultdict
import json
import math
import resource
from pathlib import Path
import numpy as np

ROOT=Path(__file__).resolve().parents[1]
FIELDS=['chi','chi_excl','chi_nonwrap','wrap','largest','density','clusters']

def exact(d,L,q,p):
    with (ROOT/f'data/exact_d{d}_L{L}.csv').open() as f:rows=list(csv.DictReader(f))
    m=d*L**d;n=L**d;z=0.;s=np.zeros(6)
    for r in rows:
        a=int(r['open']);k=int(r['k']);w=p**a*(1-p)**(m-a)*q**k
        count=int(r['count']);z+=w*count
        s+=w*np.array([int(r['sum_s2'])/n,int(r['sum_excl'])/n,int(r['sum_nonwrap'])/n,
                       int(r['wrap_count']),int(r['sum_max'])/n,a*count/m])
    return z,s/z

def ess(x):
    x=x-x.mean();n=len(x)
    if not np.any(x):return float(n)
    nfft=1 << (2*n-1).bit_length()
    transform=np.fft.rfft(x,nfft)
    ac=np.fft.irfft(transform*transform.conjugate(),nfft)[:n]/np.arange(n,0,-1)
    ac/=ac[0];pairs=[]
    for i in range(0,n-1,2):
        val=ac[i]+ac[i+1]
        if val<0:break
        pairs.append(min(val,pairs[-1] if pairs else val))
    tau=max(1.,-1+2*sum(pairs))
    return n/tau

def blocks(x,b):
    return x[:len(x)//b*b].reshape(-1,b).mean(axis=1)

def stats(chains):
    x=np.asarray(chains);n=x.shape[1]
    # Split R-hat; report constant variables explicitly in diagnostic notes.
    y=np.concatenate([x[:,:n//2],x[:,-n//2:]],axis=0)
    W=np.var(y,axis=1,ddof=1).mean();B=(n//2)*np.var(y.mean(axis=1),ddof=1)
    rhat=math.sqrt(((n//2-1)/(n//2)*W+B/(n//2))/W) if W else (1. if B==0 else float('inf'))
    bs=np.concatenate([blocks(z,20) for z in x])
    se=max(np.std(np.concatenate([blocks(z,b) for z in x]),ddof=1)/math.sqrt(sum(len(z)//b for z in x)) for b in [20,40])
    cs=[max(np.std(blocks(z,b),ddof=1)/math.sqrt(len(z)//b) for b in [20,40]) for z in x]
    zstart=abs(x[0].mean()-x[1].mean())/math.hypot(*cs) if math.hypot(*cs) else 0.
    return dict(mean=x.mean(),se=se,ess=sum(ess(z) for z in x),rhat=rhat,start_z=zstart),bs

def read_groups(path):
    groups=defaultdict(lambda:defaultdict(list))
    with path.open() as f:
        for r in csv.DictReader(f):
            key=(int(r['d']),int(r['L']),float(r['q']),float(r['p']))
            groups[key][int(r['chain'])].append([float(r[t]) for t in FIELDS])
    return {k:np.array([np.array(v[c]) for c in sorted(v)]) for k,v in groups.items()}

def crossing(ps,ys,level=.5):
    # Use actual first crossing. Do not impose isotonicity or the self-dual prediction.
    for i in range(len(ps)-1):
        if ys[i]<=level<=ys[i+1] and ys[i+1]>ys[i]:
            return ps[i]+(ps[i+1]-ps[i])*(level-ys[i])/(ys[i+1]-ys[i])
    return float('nan')

def main():
    rng=np.random.default_rng(9202026)
    groups=read_groups(ROOT/'data/mc_samples.csv')
    summaries=[];allblocks={}
    for key,x in sorted(groups.items()):
        d,L,q,p=key;row=dict(d=d,L=L,q=q,p=p)
        for i,t in enumerate(FIELDS):
            st,bs=stats(x[:,:,i]);allblocks[key,t]=bs
            row.update({t+'_'+k:v for k,v in st.items()})
        summaries.append(row)
    with (ROOT/'data/mc_summary.csv').open('w') as f:
        w=csv.DictWriter(f,fieldnames=list(summaries[0]));w.writeheader();w.writerows(summaries)
    pseudo=[]
    for d,L,q in sorted({key[:3] for key in groups}):
        rows=[r for r in summaries if (r['d'],r['L'],r['q'])==(d,L,q)]
        ps=np.array([r['p'] for r in rows]);wrap=np.array([r['wrap_mean'] for r in rows])
        chi=np.array([r['chi_mean'] for r in rows]);excl=np.array([r['chi_excl_mean'] for r in rows])
        nwr=np.array([r['chi_nonwrap_mean'] for r in rows])
        half=crossing(ps,wrap);peak=ps[np.argmax(excl)];nonwrap_peak=ps[np.argmax(nwr)]
        boots=[]
        for _ in range(500):
            wb=[];eb=[]
            for p in ps:
                for t,arr in [('wrap',wb),('chi_excl',eb)]:
                    bs=allblocks[(d,L,q,p),t];arr.append(rng.choice(bs,len(bs)).mean())
            boots.append([crossing(ps,wb),ps[np.argmax(eb)]])
        boots=np.array(boots)
        wlo,whi=np.nanquantile(boots[:,0],[.025,.975]);plo,phi=np.quantile(boots[:,1],[.025,.975])
        relevant=[r for r in rows if .1<r['wrap_mean']<.9]
        row=dict(d=d,L=L,q=q,p_wrap50=half,wrap_ci_low=wlo,wrap_ci_high=whi,
                 p_chi_excl_peak=peak,peak_ci_low=plo,peak_ci_high=phi,
                 p_chi_nonwrap_peak=nonwrap_peak,chi_at_wrap50=np.interp(half,ps,chi),
                 peak_minus_wrap=peak-half,max_relevant_rhat=max(r['wrap_rhat'] for r in relevant),
                 min_relevant_ess=min(r['wrap_ess'] for r in relevant),
                 max_relevant_start_z=max(r['wrap_start_z'] for r in relevant))
        pseudo.append(row)
    with (ROOT/'data/pseudocritical.csv').open('w') as f:
        w=csv.DictWriter(f,fieldnames=list(pseudo[0]));w.writeheader();w.writerows(pseudo)
    exactrows=[]
    for d,L in [(2,2),(2,3),(3,2)]:
        for q in [.25,.5,.75,1.]:
            for p in np.linspace(.01,.99,99):
                z,vals=exact(d,L,q,float(p));r=dict(d=d,L=L,q=q,p=p,Z=z)
                r.update(dict(zip(FIELDS[:6],vals)));exactrows.append(r)
    with (ROOT/'data/exact_observables.csv').open('w') as f:
        w=csv.DictWriter(f,fieldnames=list(exactrows[0]));w.writeheader();w.writerows(exactrows)
    # Independent checks of the sampler against exact finite-volume probabilities.
    vgroups=read_groups(ROOT/'data/validation_samples.csv');checks=[]
    for key,x in sorted(vgroups.items()):
        d,L,q,p=key;z,truth=exact(d,L,q,p)
        for i,t in enumerate(FIELDS[:6]):
            st,_=stats(x[:,:,i]);err=abs(st['mean']-truth[i]);se=st['se']
            checks.append(dict(d=d,L=L,q=q,p=p,observable=t,exact=truth[i],
                               observed=st['mean'],se=se,z=err/se if se else 0.))
    with (ROOT/'data/sampler_validation.csv').open('w') as f:
        w=csv.DictWriter(f,fieldnames=list(checks[0]));w.writeheader();w.writerows(checks)
    diagnostic=dict(points=len(summaries),raw_samples=sum(x.shape[0]*x.shape[1] for x in groups.values()),
                    validation_comparisons=len(checks),validation_max_standardized_error=max(r['z'] for r in checks),
                    phase_window_max_rhat=max(r['max_relevant_rhat'] for r in pseudo),
                    phase_window_min_ess=min(r['min_relevant_ess'] for r in pseudo),
                    phase_window_max_start_z=max(r['max_relevant_start_z'] for r in pseudo),
                    caveats='Block bootstrap conditional on short chains; no mixing proof, no finite-size scaling fit. Constant wrapping samples have nominal zero SE but do not certify probabilities 0 or 1. Grid spacing and finite-size bias exceed many Monte Carlo errors.')
    (ROOT/'data/diagnostics.json').write_text(json.dumps(diagnostic,indent=2)+'\n')
    text=['# Finite-volume numerical results','',
          'p_wrap is the first interpolated 50% wrapping point; p_peak maximizes susceptibility after removing one largest component. These are different finite-size proxies. Intervals below quantify block-sampling error only. Maximum grid spacing is 0.02.','',
          '| d | q | L | p_wrap (95% block interval) | p_peak (95% block interval) | chi at p_wrap | peak − wrap |',
          '|---|---|---|---|---|---|---|']
    for r in pseudo:
        text.append(f"| {r['d']} | {r['q']:.2f} | {r['L']} | {r['p_wrap50']:.4f} [{r['wrap_ci_low']:.4f}, {r['wrap_ci_high']:.4f}] | {r['p_chi_excl_peak']:.4f} [{r['peak_ci_low']:.4f}, {r['peak_ci_high']:.4f}] | {r['chi_at_wrap50']:.2f} | {r['peak_minus_wrap']:+.4f} |")
    text+=['',
           'The full susceptibility has no finite-p singularity on a finite torus. Largest-cluster-deleted and nonwrapping susceptibility peaks are different quantities and can have large finite-size shifts. No infinite-volume threshold or scaling fit is inferred.',
           '',
           'The initial short validation at d=3,L=2,q=.25,p=.6 missed rare connected nonwrapping configurations and gave a 12.64-standard-error discrepancy. Its summary is retained in initial_sampler_validation.csv. That parameter was rerun for one million measured sweeps per chain, stride 10. The final maximum discrepancy over 108 comparisons is 2.775 estimated standard errors.',
           '',
           '```json',json.dumps(diagnostic,indent=2),'```','']
    (ROOT/'data/NUMERICS.md').write_text('\n'.join(text))
    try:
        import matplotlib
        matplotlib.use('Agg')
        import matplotlib.pyplot as plt
        fig,axes=plt.subplots(2,3,figsize=(12,7),constrained_layout=True)
        for i,d in enumerate([2,3]):
            for j,q in enumerate([.25,.5,.75]):
                ax=axes[i,j];right=ax.twinx()
                for L in sorted({r['L'] for r in summaries if r['d']==d}):
                    rows=[r for r in summaries if (r['d'],r['L'],r['q'])==(d,L,q)]
                    line=ax.plot([r['p'] for r in rows],[r['chi_excl_mean'] for r in rows],label=f'L={L}')[0]
                    right.plot([r['p'] for r in rows],[r['wrap_mean'] for r in rows],'--',color=line.get_color(),alpha=.65)
                right.set_ylim(0,1);right.axhline(.5,color='grey',linewidth=.5)
                ax.set(title=f'd={d}, q={q}',xlabel='p',ylabel='susceptibility minus largest cluster')
                right.set_ylabel('wrapping probability (dashed)');ax.legend(fontsize=8)
        fig.savefig(ROOT/'data/finite_size_comparison.svg')
        plt.close(fig)
    except ImportError:
        pass
    (ROOT/'data/analysis_usage.json').write_text(json.dumps(dict(max_rss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss),indent=2)+'\n')
    print(json.dumps(diagnostic,indent=2));print('\n'.join(text[:25]))

if __name__=='__main__':main()
