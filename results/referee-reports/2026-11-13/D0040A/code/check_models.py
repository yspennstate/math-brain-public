#!/usr/bin/env python3
"""Small-matrix Monte Carlo for D0040; evidence, not a proof.
Run from project root: python3 code/check_models.py
All numerical thread pools are capped at one before importing numpy/scipy.
"""
import os
for name in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'VECLIB_MAXIMUM_THREADS',
             'MKL_NUM_THREADS', 'NUMEXPR_NUM_THREADS', 'BLIS_NUM_THREADS'):
    os.environ[name] = '1'
import json, csv, time, resource, platform, hashlib
from pathlib import Path
import numpy as np
import scipy
from scipy import stats, special

ROOT = Path(__file__).resolve().parents[1]
SEED = 400020261113
SAMPLES = 30000
NMAX = 4
rng = np.random.default_rng(SEED)
checks, moments, failures, raw = [], [], [], {}
t0 = time.monotonic()

def ks_one(x, dist, kind, beta, a, n):
    result = stats.kstest(x, dist.cdf)
    checks.append(dict(model='laguerre',kind=kind,beta=beta,a=a,n=n,
                       statistic=float(result.statistic),p=float(result.pvalue)))

def bidiag(d, ell):
    size = d.shape[1]
    out = np.zeros((len(d),size,size))
    ii = np.arange(size)
    out[:,ii,ii] = d
    if size>1:
        out[:,ii[1:],ii[:-1]] = ell
    return out

def kn_jacobi(n, beta, p, q, samples):
    """KN Theorem 2, affinely moved to (0,1), weight x^p(1-x)^q.
    Their B(s,t) on (-1,1) equals 2*Beta(t,s)-1.
    """
    alpha = {-1: np.full(samples,-1.),2*n-1:np.full(samples,-1.)}
    for k in range(2*n-1):
        if k%2==0:
            s=(2*n-k-2)*beta/4 + q+1
            t=(2*n-k-2)*beta/4 + p+1
        else:
            s=(2*n-k-3)*beta/4 + p+q+2
            t=(2*n-k-1)*beta/4
        alpha[k] = 2*rng.beta(t,s,samples)-1
    J = np.zeros((samples,n,n))
    for k in range(n):
        diag=(1-alpha[2*k-1])*alpha[2*k]
        if k>0:
            diag -= (1+alpha[2*k-1])*alpha[2*k-2]
        J[:,k,k]=diag
        if k<n-1:
            off=np.sqrt((1-alpha[2*k-1])*(1-alpha[2*k]**2)*(1+alpha[2*k+1]))
            J[:,k,k+1]=off
            J[:,k+1,k]=off
    return (J+2*np.eye(n))/4

max_nesting_error = 0.
max_interlace_violation = 0.
for beta in (0.5,1.,2.,4.):
    for a in (-0.25,1.5):
        theta=beta/2
        d=np.sqrt(rng.chisquare(beta*(a+np.arange(1,NMAX+1)),size=(SAMPLES,NMAX))/beta)
        ell=np.sqrt(rng.chisquare(beta*np.arange(1,NMAX),size=(SAMPLES,NMAX-1))/beta)
        B=bidiag(d,ell)
        L=B @ B.transpose(0,2,1)
        previous=None
        eigs={}
        for n in range(1,NMAX+1):
            Ln=L[:,:n,:n]
            Bn=B[:,:n,:n]
            max_nesting_error=max(max_nesting_error,float(np.max(np.abs(Ln-Bn@Bn.transpose(0,2,1)))))
            ev=np.linalg.eigvalsh(Ln)
            eigs[n]=ev
            if previous is not None:
                max_interlace_violation=max(max_interlace_violation,float(np.max(ev[:,:-1]-previous)),float(np.max(previous-ev[:,1:])))
            previous=ev
            trace=ev.sum(axis=1)
            ks_one(trace,stats.gamma(theta*n*(n+a),scale=2/beta),'trace_exact_gamma',beta,a,n)
            # Use the entry determinant to avoid losing tiny eigenvalues at beta=0.5.
            logdet=2*np.log(d[:,:n]).sum(axis=1)
            target=float(np.sum(special.digamma(theta*(a+np.arange(1,n+1))))+n*np.log(2/beta))
            var=float(np.sum(special.polygamma(1,theta*(a+np.arange(1,n+1)))))
            z=(float(logdet.mean())-target)/np.sqrt(var/SAMPLES)
            moments.append(dict(beta=beta,a=a,n=n,logdet_mean=float(logdet.mean()),target=target,z=float(z),
                                trace_mean=float(trace.mean()),trace_target=n*(n+a)))
            raw[f'lag_beta{beta}_a{a}_n{n}']=ev
            if n>=3:
                # Independent standard decreasing DE model; not the truncated candidate.
                dd=np.sqrt(rng.chisquare(beta*(a+n-np.arange(n)),size=(SAMPLES,n))/beta)
                ee=np.sqrt(rng.chisquare(beta*(n-np.arange(1,n)),size=(SAMPLES,n-1))/beta)
                BB=bidiag(dd,ee)
                ref=np.linalg.eigvalsh(BB@BB.transpose(0,2,1))
                for j in range(n):
                    res=stats.ks_2samp(ev[:,j],ref[:,j])
                    checks.append(dict(model='laguerre',kind=f'eigenvalue_{j+1}_vs_DE',beta=beta,a=a,n=n,
                                       statistic=float(res.statistic),p=float(res.pvalue)))
        ev=eigs[2]
        trace=ev.sum(axis=1)
        u=((ev[:,1]-ev[:,0])/trace)**2
        target_u=stats.beta((beta+1)/2,theta*(a+1))
        ks_one(u,target_u,'n2_gap_ratio_exact_beta',beta,a,2)
        pit_t=stats.gamma(theta*2*(2+a),scale=2/beta).cdf(trace)
        pit_u=target_u.cdf(u)
        counts=np.histogram2d(pit_t,pit_u,bins=[np.linspace(0,1,6)]*2)[0].ravel()
        res=stats.chisquare(counts,np.full(25,SAMPLES/25))
        checks.append(dict(model='laguerre',kind='n2_joint_PIT_5x5',beta=beta,a=a,n=2,
                           statistic=float(res.statistic),p=float(res.pvalue)))

# A concrete negative control: reverse a fixed-size KN Jacobi model, then truncate.
p,q=0.3,1.1
for beta in (0.5,1.,2.,4.):
    J=kn_jacobi(4,beta,p,q,SAMPLES)
    K=J[:,::-1,::-1]
    scalar=K[:,0,0]
    true=J[:,0:1,0:1]  # Not a target n=1 draw; generate that separately below.
    target=stats.beta(p+1,q+1)
    res=stats.kstest(scalar,target.cdf)
    expected_bad=0.5+(p-q)/(2*(p+q+2+beta))
    se=float(scalar.std(ddof=1)/np.sqrt(SAMPLES))
    failures.append(dict(model='reversed_KN_Jacobi',beta=beta,p=p,q=q,
                         observed_mean=float(scalar.mean()),candidate_mean=expected_bad,
                         target_mean=float(target.mean()),mean_se=se,
                         statistic=float(res.statistic),pvalue=float(res.pvalue)))
    # Verify the direct 1x1 target model independently; affinely mapped KN has beta law.
    direct=kn_jacobi(1,beta,p,q,SAMPLES)[:,0,0]
    result=stats.kstest(direct,target.cdf)
    checks.append(dict(model='direct_KN_Jacobi',kind='n1_exact_beta',beta=beta,a=None,n=1,
                       statistic=float(result.statistic),p=float(result.pvalue)))
    raw[f'jacobi_reversed_beta{beta}']=scalar

# Family-wise correction only for the positive-model checks. Negative controls are separate.
pvals=np.array([c['p'] for c in checks])
order=np.argsort(pvals)
adjusted=np.maximum.accumulate((len(pvals)-np.arange(len(pvals)))*pvals[order]).clip(0,1)
for i,adj in zip(order,adjusted): checks[int(i)]['holm_p']=float(adj)
meta=dict(seed=SEED,samples_per_case=SAMPLES,nmax=NMAX,betas=[0.5,1,2,4],a_values=[-0.25,1.5],
          python=platform.python_version(),numpy=np.__version__,scipy=scipy.__version__,
          niceness=os.getpriority(os.PRIO_PROCESS,0),threads={k:os.environ[k] for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','VECLIB_MAXIMUM_THREADS')},
          elapsed_seconds=time.monotonic()-t0,peak_rss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
          max_nesting_error=max_nesting_error,max_interlace_violation=max_interlace_violation,
          positive_tests=len(checks),holm_rejections_005=sum(c['holm_p']<0.05 for c in checks),
          min_raw_p=float(pvals.min()),max_abs_logdet_z=max(abs(m['z']) for m in moments),
          code_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
(ROOT/'data'/'checks.json').write_text(json.dumps(dict(metadata=meta,positive_checks=checks,moments=moments,negative_controls=failures),indent=2)+'\n')
np.savez_compressed(ROOT/'data'/'samples.npz',**raw)
for filename, rows in [('positive_checks.csv',checks),('moments.csv',moments),('negative_controls.csv',failures)]:
    with (ROOT/'data'/filename).open('w',newline='') as f:
        writer=csv.DictWriter(f,fieldnames=rows[0].keys());writer.writeheader();writer.writerows(rows)
print(json.dumps(meta,indent=2))
print(json.dumps(failures,indent=2))
