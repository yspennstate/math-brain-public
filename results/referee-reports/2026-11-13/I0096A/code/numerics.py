"""Finite candidate search for I0096. No numerical value is a proof.

All subsets are enumerated; singular values use float64 LAPACK SVD.
Run python3 code/numerics.py [enumerate|optimize|summarize].
The process inherits nice >=10, uses a single BLAS thread, and batches at 2048.
"""
import os
for name in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS', 'VECLIB_MAXIMUM_THREADS', 'NUMEXPR_NUM_THREADS'):
    os.environ[name] = '1'
import csv
import itertools
import json
import math
from pathlib import Path
import platform
import resource
import sys
import time
import numpy as np
import scipy
from scipy import linalg, optimize
from threadpoolctl import threadpool_info, threadpool_limits

threadpool_limits(limits=1)
root = Path(__file__).resolve().parents[1]
out = root/'data'
out.mkdir(exist_ok=True)
priority = os.getpriority(os.PRIO_PROCESS, 0)
if priority < 10:
    os.nice(10-priority)

def normalize_rows(a):
    return a / np.linalg.norm(a, axis=1, keepdims=True)

def harmonic(m):
    """Real form of consecutive complex Fourier frequencies, including even m."""
    n = 2*m-1
    t = 2*np.pi*np.arange(n)/n
    cols = [np.ones(n)/np.sqrt(m)] if m % 2 else []
    fs = np.arange(1,(m+1)//2) if m % 2 else np.arange(m//2)+.5
    for f in fs:
        cols.extend([np.sqrt(2/m)*np.cos(f*t), np.sqrt(2/m)*np.sin(f*t)])
    return np.array(cols).T

def make_candidates(m):
    n=2*m-1
    rng=np.random.default_rng(960000+m)
    yield 'harmonic', harmonic(m)
    x=np.linspace(-1,1,n)
    yield 'vandermonde', normalize_rows(np.vander(x,m,increasing=True))
    for trial in range(3):
        g=rng.standard_normal((n,m))
        yield f'gaussian_unit_{trial}',normalize_rows(g)
        q=np.linalg.qr(g)[0]
        yield f'haar_scaled_{trial}',q/np.linalg.norm(q,axis=1).max()
    q=np.linalg.qr(rng.standard_normal((m,m)))[0]
    yield 'two_bases',np.vstack([np.eye(m),q[:m-1]])
    h=np.eye(m+1)-np.ones((m+1,m+1))/(m+1)
    q=np.linalg.qr(h[:,:m])[0]*np.sqrt((m+1)/m)
    yield 'simplex_plus',np.vstack([q,normalize_rows(rng.standard_normal((m-2,m)))])

def omega(a, batch=2048, detailed=False):
    n,m=a.shape
    iterator=iter(itertools.combinations(range(n),m))
    best=float('inf'); witness=None; seen=0
    while True:
        sub=list(itertools.islice(iterator,batch))
        if not sub: break
        idx=np.array(sub,dtype=np.int16)
        sv=np.linalg.svd(a[idx],compute_uv=False)[:,-1]
        i=int(np.argmin(sv))
        if float(sv[i])<best:
            best=float(sv[i]); witness=sub[i]
        seen+=len(sub)
    assert seen==math.comb(n,m)
    if not detailed:return best
    s=a[list(witness)]
    u,svals,vh=linalg.svd(s,lapack_driver='gesvd')
    check=float(svals[-1])
    residual=float(np.linalg.norm(s@vh[-1]-check*u[:,-1]))
    return best,{'witness_zero_based':list(witness),'subsets':seen,'gesvd_value':check,
                'svd_residual':residual,'max_row_norm':float(np.linalg.norm(a,axis=1).max()),
                'frame_condition':float(np.linalg.cond(a))}

def record(a,m,family,stage,elapsed,extra=None):
    evaluation_start=time.monotonic()
    value,detail=omega(a,detailed=True)
    elapsed+=time.monotonic()-evaluation_start
    safe=family.replace('/','_')
    filename=f'{stage}_m{m:02}_{safe}.csv'
    np.savetxt(out/filename,a,delimiter=',',fmt='%.18e')
    row={'m':m,'family':family,'stage':stage,'omega':value,'matrix_file':filename,
         'base':value**(1/m) if value>0 else 0,'decay_per_dimension':-math.log(value)/m if value>0 else None,
         'elapsed_seconds':elapsed,**detail,**(extra or {})}
    with (out/'numerics.jsonl').open('a') as f:f.write(json.dumps(row)+'\n')
    print(json.dumps({k:row[k] for k in ('m','family','stage','omega','elapsed_seconds')}),flush=True)
    return row

def enumerate_all():
    done=set()
    if (out/'numerics.jsonl').exists():
        done={(r['m'],r['family'],r['stage']) for r in map(json.loads,(out/'numerics.jsonl').read_text().splitlines())}
    for m in range(2,13):
        for family,a in make_candidates(m):
            if (m,family,'enumeration') in done:continue
            start=time.monotonic()
            record(a,m,family,'enumeration',time.monotonic()-start)

def optimize_small():
    rows=list(map(json.loads,(out/'numerics.jsonl').read_text().splitlines()))
    opt_round=int(os.environ.get('I0096_OPT_ROUND','0'))
    max_m=int(os.environ.get('I0096_OPT_MAX_M','9'))
    for m in range(2,max_m+1):
        if opt_round and m<5:continue
        n=2*m-1
        subsets=np.array(list(itertools.combinations(range(n),m)),dtype=int)
        candidates=sorted([r for r in rows if r['m']==m],key=lambda r:-r['omega'])
        trials=1 if opt_round else 6 if m<=4 else 3 if m<=6 else 1
        for trial in range(trials):
            family=f'slsqp_r{opt_round}_{trial}' if opt_round else f'slsqp_{trial}'
            if any(r['m']==m and r['family']==family and r['stage']=='optimization' for r in rows):continue
            a=np.loadtxt(out/candidates[trial%len(candidates)]['matrix_file'],delimiter=',')
            a=normalize_rows(a)
            initial=omega(a)
            state={}
            def calc(z):
                if 'z' in state and np.array_equal(state['z'],z):return state['v'],state['j']
                b=z[:-1].reshape(n,m)
                u,s,vh=np.linalg.svd(b[subsets],full_matrices=False)
                vals=s[:,-1]-z[-1]
                jac=np.zeros((len(subsets),n*m+1))
                grad=u[:,:,-1,None]*vh[:,-1,None,:]
                for i in range(m):
                    for j in range(m):jac[np.arange(len(subsets)),subsets[:,i]*m+j]=grad[:,i,j]
                jac[:,-1]=-1
                state.update(z=z.copy(),v=vals,j=jac)
                return vals,jac
            def eq(z):return np.sum(z[:-1].reshape(n,m)**2,axis=1)-1
            def eqjac(z):
                j=np.zeros((n,n*m+1))
                for i in range(n):j[i,i*m:(i+1)*m]=2*z[i*m:(i+1)*m]
                return j
            start=time.monotonic()
            z0=np.r_[a.ravel(),initial*.99]
            objjac=np.r_[np.zeros(n*m),-1.]
            result=optimize.minimize(lambda z:-z[-1],z0,jac=lambda z:objjac,method='SLSQP',
                constraints=[{'type':'eq','fun':eq,'jac':eqjac},
                             {'type':'ineq','fun':lambda z:calc(z)[0],'jac':lambda z:calc(z)[1]}],
                options={'maxiter':140,'ftol':2e-10,'disp':False})
            b=normalize_rows(result.x[:-1].reshape(n,m))
            if omega(b)<initial:b=a
            row=record(b,m,family,'optimization',time.monotonic()-start,
                       {'initial_omega':initial,'success':bool(result.success),'message':str(result.message),
                        'iterations':int(result.nit),'epigraph_t':float(result.x[-1]),
                        'raw_equality_violation':float(np.max(np.abs(eq(result.x))))})
            rows.append(row)

def summarize():
    rows=list(map(json.loads,(out/'numerics.jsonl').read_text().splitlines()))
    best=[]
    for m in sorted(set(r['m'] for r in rows)):
        b=max((r for r in rows if r['m']==m),key=lambda r:r['omega']);best.append(b)
    with (out/'best.csv').open('w') as f:
        keys=['m','omega','base','decay_per_dimension','family','stage','subsets','frame_condition','matrix_file']
        w=csv.DictWriter(f,fieldnames=keys,extrasaction='ignore');w.writeheader();w.writerows(best)
    fit={}
    for lo,hi in [(2,7),(2,9),(3,7),(8,12),(2,12)]:
        b=[r for r in best if lo<=r['m']<=hi]
        x=np.array([r['m'] for r in b]);y=np.log([r['omega'] for r in b])
        slope,intercept=np.polyfit(x,y,1)
        fit[f'{lo}-{hi}']={'slope':float(slope),'fitted_base':float(np.exp(slope)),
                            'intercept':float(intercept),'warning':'Different search effort by dimension; no asymptotic inference.'}
    (out/'fits.json').write_text(json.dumps(fit,indent=2))
    print((out/'best.csv').read_text())
    print(json.dumps(fit,indent=2))

if __name__=='__main__':
    meta={'numpy':np.__version__,'scipy':scipy.__version__,'platform':platform.platform(),
          'nice':os.getpriority(os.PRIO_PROCESS,0),'threadpools':threadpool_info(),
          'batch':2048,'seed_formula':'960000+m','float':'float64',
          'rss_bytes_at_start':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}
    (out/'numerics_environment.json').write_text(json.dumps(meta,indent=2))
    {'enumerate':enumerate_all,'optimize':optimize_small,'summarize':summarize}[sys.argv[1] if len(sys.argv)>1 else 'enumerate']()
