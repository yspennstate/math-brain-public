"""Binary lognormal smoothing iterations. Evidence only; no continuum inference.

The heavy-tailed-seed iterate is simulated exactly in law, conditional on the
Gaussian tree, by positive-stable additivity. Spatial checks use explicit marks.
"""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','VECLIB_MAXIMUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):
    os.environ[key]='1'
import argparse, csv, datetime, json, math, pathlib, resource, time
import numpy as np
ROOT=pathlib.Path(__file__).resolve().parents[1]
L2=math.log(2); ALPHA=.6; GAMMAS=[math.sqrt(.5),math.sqrt(2)]


def stable(rng, alpha, size):
    """Kanter variable with E exp(-q S)=exp(-q**alpha), 0<alpha<1."""
    u=rng.uniform(np.finfo(float).eps,math.pi-np.finfo(float).eps,size)
    e=rng.exponential(1,size)
    log_s=(np.log(np.sin(alpha*u))-np.log(np.sin(u))/alpha
        +(1-alpha)/alpha*(np.log(np.sin((1-alpha)*u))-np.log(e)))
    return np.exp(log_s)


def tree(rng,nrep,depth,batch=4):
    checkpoints=sorted(set([2,4,8,12,16,depth]) & set(range(1,depth+1)))
    result={n:{'sub':[],'crit':[],'derivative_x':[],'bounded_sub':[],'bounded_crit':[]} for n in checkpoints}
    for first in range(0,nrep,batch):
        b=min(batch,nrep-first); x=np.zeros((b,1))
        for n in range(1,depth+1):
            x=np.repeat(x,2,axis=1)
            x += rng.normal(0,math.sqrt(L2),size=x.shape)
            if n in result:
                t=n*L2
                for g,label in zip(GAMMAS,['sub','crit']):
                    w=np.exp(g*x-(g*g/2+1)*t)
                    result[n][label].extend(w.sum(axis=1).tolist())
                    result[n]['bounded_'+label].extend(np.exp((g*x-(g*g/2+1)*t)/ALPHA).sum(axis=1).tolist())
                    if label=='crit':
                        result[n]['derivative_x'].extend(((g*t-x)*w).sum(axis=1).tolist())
    return {n:{k:np.array(v) for k,v in d.items()} for n,d in result.items()}


def bounded_stats(x,q):
    y=np.exp(-q*x); return float(y.mean()),float(y.std(ddof=1)/math.sqrt(len(y)))


def main():
    p=argparse.ArgumentParser();p.add_argument('--seed',type=int,default=20261113)
    p.add_argument('--replicates',type=int,default=512);p.add_argument('--depth',type=int,default=18)
    args=p.parse_args();start=time.monotonic()
    if os.getpriority(os.PRIO_PROCESS,0)<10:
        raise RuntimeError('Process must already run at nice >=10')
    # The arrays are much smaller; enforce an additional hard process limit.
    soft,hard=resource.getrlimit(resource.RLIMIT_AS)
    cap=3*1024**3
    if hard!=resource.RLIM_INFINITY: cap=min(cap,hard)
    cap_applied=False
    try:
        resource.setrlimit(resource.RLIMIT_AS,(cap,hard))
        cap_applied=True
    except (ValueError,OSError):
        # macOS may reject RLIMIT_AS. Largest tree arrays are bounded explicitly:
        # batch <=4, depth <=18, spatial replicates=128 and depth <=16.
        pass
    if args.depth>18 or args.replicates>2048:
        raise ValueError('This modest experiment is capped at depth 18 and 2048 roots')
    rng=np.random.default_rng(args.seed);controls=tree(rng,args.replicates,args.depth)
    rows=[];samples={}
    with (ROOT/'data'/f'controls_{args.seed}.csv').open('w') as f:
        writer=csv.writer(f);writer.writerow(['depth','root','subcritical_mass','critical_mass','critical_derivative_x','bounded_dual','bounded_frozen'])
        for n,v in controls.items():
            for i in range(args.replicates): writer.writerow([n,i,v['sub'][i],v['crit'][i],v['derivative_x'][i],v['bounded_sub'][i],v['bounded_crit'][i]])
    for n,vals in controls.items():
        for label in ['sub','crit']:
            for alpha in [1.,ALPHA]:
                regime=('standard' if label=='sub' else 'critical') if alpha==1 else ('dual' if label=='sub' else 'frozen')
                s=np.ones(args.replicates) if alpha==1 else stable(rng,alpha,args.replicates)
                raw=vals[label]**(1/alpha)*s
                scale=1. if label=='sub' else (n*L2)**(1/(2*alpha))
                normalized=scale*raw
                forms=[('raw',raw),('normalized',normalized)]
                if alpha<1:
                    bounded=vals['bounded_'+label]
                    forms.append(('bounded_seed',bounded))
                    if label=='crit': forms.append(('bounded_seed_frozen_normalized',(n*L2)**(3/(2*alpha))*bounded))
                for form,x in forms:
                    d=dict(seed=args.seed,regime=regime,alpha=alpha,gamma2=.5 if label=='sub' else 2.,depth=n,form=form,
                           median=float(np.median(x)),q25=float(np.quantile(x,.25)),q75=float(np.quantile(x,.75)))
                    for q in [.25,1.,4.]:
                        m,se=bounded_stats(x,q);d[f'laplace_{q}']=m;d[f'se_{q}']=se
                        if form in ['raw','normalized']:
                            cscale=scale if form=='normalized' else 1.
                            conditional=np.exp(-(q*cscale)**alpha*vals[label])
                            d[f'conditional_laplace_{q}']=float(conditional.mean())
                            d[f'conditional_se_{q}']=float(conditional.std(ddof=1)/math.sqrt(len(conditional)))
                        else:
                            d[f'conditional_laplace_{q}']=''
                            d[f'conditional_se_{q}']=''
                    rows.append(d)
                if n==args.depth: samples[regime]=normalized
    out=ROOT/'data'/f'cascade_{args.seed}.csv'
    with out.open('w') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
    # Independent empirical terminal samples for a one-step fixed-point diagnostic.
    # These are resamples of a finite-depth approximation, not exact limiting laws.
    residual=[];ncheck=30000
    for regime,x in samples.items():
        alpha=1. if regime in ['standard','critical'] else ALPHA
        g=GAMMAS[0] if regime in ['standard','dual'] else GAMMAS[1]
        gnorm=rng.normal(0,math.sqrt(L2),(ncheck,2))
        weights=np.exp((g*gnorm-(g*g/2+1)*L2)/alpha)
        transformed=(weights*rng.choice(x,size=(ncheck,2))).sum(axis=1)
        # Original SE records finite terminal sample uncertainty; it is not a CI
        # for the correlated difference of the two empirical transforms.
        for q in [.25,1.,4.]:
            orig,se=bounded_stats(x,q);one,one_se=bounded_stats(transformed,q)
            residual.append(dict(regime=regime,q=q,original=orig,one_step=one,residual=one-orig,
                                 original_se=se,conditional_resampling_se=one_se))
    with (ROOT/'data'/f'fixed_point_residual_{args.seed}.csv').open('w') as f:
        w=csv.DictWriter(f,fieldnames=list(residual[0]));w.writeheader();w.writerows(residual)
    # Explicit stable leaves on a separate set of spatial trees. For alpha<1,
    # E sum cellmass^2 / totalmass^2 =1-alpha+alpha*sum controlprob^2.
    spatial=[];srep=128
    for n in [8,12,16]:
        x=np.zeros((srep,1))
        for j in range(n):
            x=np.repeat(x,2,axis=1);x+=rng.normal(0,math.sqrt(L2),x.shape)
        for label,g in zip(['sub','crit'],GAMMAS):
            log_w=g*x-(g*g/2+1)*n*L2
            w=np.exp(log_w);prob=w/w.sum(axis=1)[:,None]
            diffuse_ipr=(prob**2).sum(axis=1)
            mark=stable(rng,ALPHA,w.shape)
            masses=np.exp(log_w/ALPHA)*mark
            massprob=masses/masses.sum(axis=1)[:,None]
            ipr=(massprob**2).sum(axis=1)
            spatial.append(dict(depth=n,control=label,replicates=srep,
                diffuse_ipr_mean=float(diffuse_ipr.mean()),stable_cell_ipr_mean=float(ipr.mean()),
                stable_cell_ipr_se=float(ipr.std(ddof=1)/math.sqrt(srep)),
                exact_expected_stable_ipr=float(1-ALPHA+ALPHA*diffuse_ipr.mean())))
        del x,w,prob,mark,masses,massprob
    with (ROOT/'data'/f'spatial_{args.seed}.csv').open('w') as f:
        w=csv.DictWriter(f,fieldnames=list(spatial[0]));w.writeheader();w.writerows(spatial)
    # Check stable sampler using bounded observables, not an infinite sample mean.
    s=stable(rng,ALPHA,200000);stable_check=[]
    for q in [.25,1.,4.]:
        m,se=bounded_stats(s,q);stable_check.append(dict(q=q,empirical=m,se=se,exact=math.exp(-q**ALPHA)))
    d=controls[args.depth]['derivative_x']
    diagnostics=dict(seed=args.seed,replicates=args.replicates,depth=args.depth,
        alpha=ALPHA,gamma2=[.5,2.],stable_sampler=stable_check,
        critical_derivative_x_median=float(np.median(d)),critical_derivative_negative_fraction=float((d<0).mean()),
        seneta_heyde_median=float(np.median(math.sqrt(args.depth*L2)*controls[args.depth]['crit'])),
        derivative_converted_median=float(math.sqrt(2/math.pi)*np.median(d)),
        nice=os.getpriority(os.PRIO_PROCESS,0),threads={k:os.environ[k] for k in ['OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','VECLIB_MAXIMUM_THREADS']},
        address_space_cap_requested_bytes=cap,address_space_cap_applied=cap_applied,peak_rss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
        seconds=time.monotonic()-start,utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
        caveats=['Finite-depth critical convergence is slow.','Residual errors share a finite empirical terminal sample.',
                 'The chosen bounded-seed dual iteration collapses; critical regimes require renormalization.',
                 'Stable-seeded mass iteration uses exact conditional stable additivity.','No continuum inference.'])
    (ROOT/'data'/f'diagnostics_{args.seed}.json').write_text(json.dumps(diagnostics,indent=2)+'\n')
    print(json.dumps(diagnostics,indent=2))

if __name__=='__main__':main()
