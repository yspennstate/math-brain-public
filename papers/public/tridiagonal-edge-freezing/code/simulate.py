#!/usr/bin/env python3
"""Exact Gaussian/Bessel transitions; no Euler discretization of singular SDEs."""
import os
for key in ['OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','VECLIB_MAXIMUM_THREADS','NUMEXPR_NUM_THREADS','BLIS_NUM_THREADS']:
    os.environ[key] = '1'
import argparse, csv, json, math, pathlib, resource, time
import numpy as np
from scipy.linalg import eigh, eigh_tridiagonal
from threadpoolctl import threadpool_limits, threadpool_info

ROOT = pathlib.Path(__file__).resolve().parents[1]
GOVERNOR = pathlib.Path(os.environ.get('COMPUTE_STATE_FILE', 'compute_state.json'))
LAGS = np.array([0., .25, 1., 3.])

def check_resources():
    niceness = os.getpriority(os.PRIO_PROCESS, 0)
    if niceness < 10 and os.environ.get('REQUIRE_NICE') == '1':
        raise RuntimeError(f'REQUIRE_NICE=1 needs nice >= 10, found {niceness}')
    if GOVERNOR.exists():
        state = json.loads(GOVERNOR.read_text())
        if state.get('status') == 'distress':
            raise RuntimeError('Compute governor distress: stopping with current CSV preserved')
    peak = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    if peak > 3.5e9:
        raise RuntimeError('Memory guard at 3.5 GB')

def gue(rng, n):
    # Real/imaginary parts of Z have variance 1/2. Hermitization produces
    # diagonal variance 1 and E|G_ij|^2=1, as in equation (2.1) of the paper.
    z = (rng.standard_normal((n,n)) + 1j*rng.standard_normal((n,n))) / math.sqrt(2)
    return (z + z.conj().T) / math.sqrt(2)

def dense_path(rng, n):
    b = gue(rng, n)                 # B(1); subsequently B(u) is literal Hermitian BM.
    previous_u = 1.
    path = []
    for s in LAGS:
        u = math.exp(2*s/n**(1/3))
        if u > previous_u:
            b += math.sqrt(u-previous_u) * gue(rng, n)
        eigenvalues = eigh(b, eigvals_only=True, subset_by_index=[n-2,n-1],
                          check_finite=False, driver='evr')[::-1]
        path.append((eigenvalues/math.sqrt(u)-2*math.sqrt(n))*n**(1/6))
        previous_u = u
    return np.array(path), None

def tri_path(rng, n):
    df = 2*np.arange(n-1,0,-1)
    a = rng.standard_normal(n)
    q = rng.chisquare(df)           # q=2*b^2, a vector of squared OU radii.
    path = []
    energy = None
    previous_s = 0.
    for s in LAGS:
        if s > previous_s:
            dt = (s-previous_s)/n**(1/3)
            rho = math.exp(-dt)
            noisevar = -math.expm1(-2*dt)
            a = rho*a + math.sqrt(noisevar)*rng.standard_normal(n)
            q = noisevar*rng.noncentral_chisquare(df, rho*rho*q/noisevar)
        off = np.sqrt(q/2)
        if s == 0:
            ev, vectors = eigh_tridiagonal(a,off,select='i',select_range=(n-2,n-1),
                                          check_finite=False)
            vectors = vectors[:,::-1]
            p = vectors*vectors
            ipr = np.sum(p*p,axis=0)
            gamma = ipr+2*np.sum(p[:-1]*p[1:],axis=0)
            energy = (ipr,gamma)
        else:
            ev = eigh_tridiagonal(a,off,select='i',select_range=(n-2,n-1),
                                  check_finite=False,eigvals_only=True)
        path.append((ev[::-1]-2*math.sqrt(n))*n**(1/6))
        previous_s = s
    return np.array(path), energy

def main():
    p=argparse.ArgumentParser()
    p.add_argument('--pilot',action='store_true')
    args=p.parse_args()
    check_resources()
    dense_counts={64:1500,128:1000,256:600,512:240,1024:64,2048:12}
    tri_counts={n:2000 for n in dense_counts}
    if args.pilot:
        dense_counts={32:4};tri_counts={32:4}
    tag='pilot' if args.pilot else 'edge'
    samples=ROOT/'data'/f'{tag}_samples.csv'
    energies=ROOT/'data'/f'{tag}_energies.csv'
    start=time.perf_counter()
    metadata={'seed':4620261113,'lags_s':LAGS.tolist(),'clock':'t=s*n^(-1/3), u=exp(2*t)',
              'normalization':'GUE diag variance 1, E|off|^2=1; edge n^(1/6)*(lambda-2*sqrt(n))',
              'nice':os.getpriority(os.PRIO_PROCESS,0),'threads_requested':1,
              'threadpools':threadpool_info(),'dense_reps':dense_counts,'tri_reps':tri_counts}
    with samples.open('w',newline='') as f, energies.open('w',newline='') as g:
        writer=csv.writer(f); ew=csv.writer(g)
        writer.writerow(['model','n','rep','s','eigenvalue_rank','edge_value'])
        ew.writerow(['n','rep','eigenvalue_rank','ipr','gamma'])
        for model,counts,fn,stream in [('hermitian_bm',dense_counts,dense_path,0),('independent_tri_ou',tri_counts,tri_path,1)]:
            for n,reps in counts.items():
                if n>2048:raise RuntimeError('Matrix-size memory guard')
                check_resources()
                rng=np.random.default_rng(np.random.SeedSequence([metadata['seed'],stream,n]))
                stage=time.perf_counter()
                for rep in range(reps):
                    if rep%50==0:check_resources()
                    path, energy=fn(rng,n)
                    for s,row in zip(LAGS,path):
                        for j,value in enumerate(row,1):writer.writerow([model,n,rep,s,j,float(value)])
                    if energy is not None:
                        for j in range(2):ew.writerow([n,rep,j+1,float(energy[0][j]),float(energy[1][j])])
                    if rep%50==0:f.flush();g.flush()
                f.flush();g.flush()
                print(json.dumps({'model':model,'n':n,'reps':reps,'seconds':time.perf_counter()-stage,
                                  'peak_rss_mb':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1e6}),flush=True)
    metadata.update(elapsed_seconds=time.perf_counter()-start,
                    peak_rss_mb=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1e6,
                    threadpools_final=threadpool_info())
    (ROOT/'data'/f'{tag}_metadata.json').write_text(json.dumps(metadata,indent=2)+'\n')

if __name__=='__main__':
    with threadpool_limits(limits=1):main()
