"""Audit the simulations against exact trap probabilities and summarize paths."""
import os
if os.getpriority(os.PRIO_PROCESS, 0) < 10:
    os.setpriority(os.PRIO_PROCESS, 0, 10)
os.environ.update(OMP_NUM_THREADS="1", OPENBLAS_NUM_THREADS="1",
                  MKL_NUM_THREADS="1", VECLIB_MAXIMUM_THREADS="1",
                  XDG_CACHE_HOME=str(__import__('pathlib').Path(__file__).resolve().parents[1]/'data'/'cache'),
                  MPLCONFIGDIR=str(__import__('pathlib').Path(__file__).resolve().parents[1]/'data'/'mplconfig'))
import csv
import json
import math
from pathlib import Path
import statistics

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"


def rows(name):
    with (DATA/name).open() as f:
        return list(csv.DictReader(f))


def main():
    parameters = {r['config']: r for r in rows('parameters.csv')}
    paths, traps = rows('paths.csv'), rows('traps.csv')
    for r in paths:
        n, x, y = (int(r[k]) for k in ('n','x','y'))
        assert abs(x)+abs(y) <= n
        assert (x+y-n) % 2 == 0
        assert 1 <= int(r['visited_sites']) <= n
        assert int(r['max_completed_run']) <= n
        assert int(r['censored_final_run']) <= n
    summary=[]
    for cfg in parameters:
        for n in sorted({int(r['n']) for r in paths if r['config']==cfg}):
            group=[r for r in paths if r['config']==cfg and int(r['n'])==n]
            vx=[float(r['vx']) for r in group]
            vy=[float(r['vy']) for r in group]
            summary.append(dict(config=cfg,n=n,replicates=len(vx),
                mean_vx=statistics.mean(vx),median_vx=statistics.median(vx),
                se_vx=statistics.stdev(vx)/len(vx)**.5,
                min_vx=min(vx),max_vx=max(vx),mean_vy=statistics.mean(vy),
                median_max_completed_run=statistics.median(int(r['max_completed_run']) for r in group),
                max_censored_run=max(int(r['censored_final_run']) for r in group)))
    with (DATA/'speed_summary.csv').open('w') as f:
        w=csv.DictWriter(f,fieldnames=list(summary[0]));w.writeheader();w.writerows(summary)
    checked=[]
    max_z=0.0
    for r in traps:
        p=parameters[r['config']]
        a=[float(p[k]) for k in ('a_plus_x','a_plus_y','a_minus_x','a_minus_y')]
        A=sum(a);axis=int(r['axis']);m=int(r['threshold'])//2
        assert 2*m==int(r['threshold'])
        # P(T > 2m) = E[(omega(0,e)*omega(e,0))**m].
        log_probability=math.fsum([2*math.lgamma(A),math.lgamma(a[axis]+m),
            math.lgamma(a[axis+2]+m),-math.lgamma(a[axis]),
            -math.lgamma(a[axis+2]),-2*math.lgamma(A+m)])
        probability=math.exp(log_probability)
        N=int(r['samples']);observed=int(r['exceedances']);expected=N*probability
        z=(observed-expected)/math.sqrt(N*probability*(1-probability))
        if expected>=10 and N-expected>=10:
            max_z=max(max_z,abs(z))
        checked.append(dict(config=r['config'],threshold=r['threshold'],
            exact_probability=probability,empirical_probability=observed/N,
            observed=observed,expected=expected,z=z))
    assert max_z<6, f'Trap sampler disagrees with exact distribution: {max_z}'
    with (DATA/'trap_checks.csv').open('w') as f:
        w=csv.DictWriter(f,fieldnames=list(checked[0]));w.writeheader();w.writerows(checked)
    # Second evaluation of the exact probability by a product, independent of lgamma.
    for cfg,p in parameters.items():
        a=[float(p[k]) for k in ('a_plus_x','a_plus_y','a_minus_x','a_minus_y')]
        A=sum(a);axis=0 if a[0]+a[2]>=a[1]+a[3] else 1
        for m in (1,2,5,50,500):
            product=math.prod((a[axis]+j)*(a[axis+2]+j)/(A+j)**2 for j in range(m))
            lg=math.exp(math.fsum([2*math.lgamma(A),math.lgamma(a[axis]+m),
                math.lgamma(a[axis+2]+m),-math.lgamma(a[axis]),
                -math.lgamma(a[axis+2]),-2*math.lgamma(A+m)]))
            assert math.isclose(product,lg,rel_tol=2e-11)
        assert math.isclose(2*A-max(a[0]+a[2],a[1]+a[3]),float(p['kappa']),rel_tol=1e-14)
    final_n=max(r['n'] for r in summary)
    lines=['Finite-time velocities; independent environments and trajectories per replicate.',
           'Mean +/- one standard error describes sampling variability, not asymptotic speed.',
           f'Largest absolute trap binomial z-score with expected count >=10: {max_z:.4f}',
           'Exact probabilities separately checked by finite products.',
           f'Inherited nice: {os.getpriority(os.PRIO_PROCESS,0)}', '']
    for s in summary:
        if s['n']==final_n:
            lines.append(f"{s['config']}: n={s['n']}, mean vx={s['mean_vx']:.7f}, "
                f"SE={s['se_vx']:.7f}, median={s['median_vx']:.7f}, "
                f"range=[{s['min_vx']:.7f},{s['max_vx']:.7f}], "
                f"median longest completed alternating run={s['median_max_completed_run']}, "
                f"max right-censored final run={s['max_censored_run']}")
    (DATA/'checks.txt').write_text('\n'.join(lines)+'\n')
    print('\n'.join(lines))
    slopes=[]
    for cfg,p in parameters.items():
        group=[r for r in checked if r['config']==cfg and
               int(r['threshold'])>=100 and r['observed']>=50]
        if len(group)<3: continue
        xs=[math.log(int(r['threshold'])) for r in group]
        def exponent(field):
            ys=[math.log(r[field]) for r in group]
            mx,my=statistics.mean(xs),statistics.mean(ys)
            return -sum((x-mx)*(y-my) for x,y in zip(xs,ys))/sum((x-mx)**2 for x in xs)
        slopes.append(dict(config=cfg,kappa=float(p['kappa']),points=len(xs),
            t_min=min(int(r['threshold']) for r in group),
            t_max=max(int(r['threshold']) for r in group),
            empirical_exponent=exponent('empirical_probability'),
            exact_finite_range_exponent=exponent('exact_probability')))
    with (DATA/'trap_slopes.csv').open('w') as f:
        w=csv.DictWriter(f,fieldnames=list(slopes[0]));w.writeheader();w.writerows(slopes)
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    fig,axs=plt.subplots(1,2,figsize=(11,4.4))
    palette=plt.rcParams['axes.prop_cycle'].by_key()['color']
    for index,cfg in enumerate(parameters):
        if not cfg.startswith('horizontal'):continue
        color=palette[index % len(palette)]
        group=[s for s in summary if s['config']==cfg]
        k=float(parameters[cfg]['kappa'])
        axs[0].errorbar([r['n'] for r in group],[r['mean_vx'] for r in group],
                        yerr=[r['se_vx'] for r in group],label=f'kappa={k:g}',marker='o',capsize=2,color=color)
        group=[r for r in checked if r['config']==cfg and r['observed']>=10]
        axs[1].loglog([int(r['threshold']) for r in group],
                        [r['empirical_probability'] for r in group],'o',label=f'kappa={k:g}',color=color)
        axs[1].loglog([int(r['threshold']) for r in group],
                        [r['exact_probability'] for r in group],'-',alpha=.8,color=color)
    axs[0].set_xscale('log');axs[0].set_xlabel('steps n');axs[0].set_ylabel('mean X_n.x / n (one SE)')
    axs[0].set_title('Finite-time velocity, 24 independent runs')
    axs[1].set_xlabel('two-site exit time t');axs[1].set_ylabel('P(T > t)')
    axs[1].set_title('Fresh traps: samples (points), exact law (lines)')
    for ax in axs: ax.legend(fontsize=7);ax.grid(alpha=.2)
    fig.tight_layout();fig.savefig(DATA/'evidence.png',dpi=160)


if __name__=='__main__':main()
