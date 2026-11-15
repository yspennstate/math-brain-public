"""Independent exact-transition experiment. No submitted code is imported.

Run with OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1
MKL_NUM_THREADS=1 python3 code/independent_simulation.py
"""
import csv
import json
import os
from pathlib import Path
import resource
import sys
import time

for key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'VECLIB_MAXIMUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[key] = '1'
import numpy as np
from scipy.linalg import eigh, eigh_tridiagonal
from threadpoolctl import threadpool_limits, threadpool_info

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'data'
SEED = 460811132026
RNG = np.random.default_rng(SEED)
LIMIT = 4 * 1024**3

def check_resources():
    assert os.getpriority(os.PRIO_PROCESS, 0) >= 10
    peak = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    if sys.platform != 'darwin':
        peak *= 1024
    assert peak < LIMIT, peak
    statepath = Path('~/.claude/compute/compute_state.json')
    if statepath.exists():
        state = json.loads(statepath.read_text())
        if state.get('status') == 'distress':
            raise RuntimeError('Governor distress: stopping at batch boundary')
    return peak

def gue(n):
    # Upper off-diagonal real/imaginary variances 1/2, diagonal variance 1.
    row, col = np.triu_indices(n, 1)
    h = np.zeros((n, n), dtype=np.complex128, order='F')
    z = (RNG.normal(size=len(row)) + 1j * RNG.normal(size=len(row))) / np.sqrt(2.)
    h[row, col] = z
    h[col, row] = z.conj()
    h[np.diag_indices(n)] = RNG.normal(size=n)
    return h

def edge_dense(h):
    n = len(h)
    return n**(1/6) * (eigh(h, subset_by_index=(n-2, n-1), eigvals_only=True,
                            check_finite=False, driver='evr')[::-1] - 2*np.sqrt(n))

def edge_tri(a, b, vectors=False):
    n = len(a)
    result = eigh_tridiagonal(a, b, eigvals_only=not vectors, select='i',
                             select_range=(n-2, n-1), check_finite=False)
    if vectors:
        vals, vecs = result
        return n**(1/6)*(vals[::-1]-2*np.sqrt(n)), vecs[:, ::-1]
    return n**(1/6)*(result[::-1]-2*np.sqrt(n))

def experiment():
    OUT.mkdir(exist_ok=True)
    start = time.monotonic()
    stats = []
    with (OUT / 'independent_samples.csv').open('w') as stream:
        writer = csv.writer(stream)
        writer.writerow(('model','n','replicate','s','rank','initial','final','increment','grid_sup_abs'))
        for model in ('tridiagonal', 'matrix_OU'):
            sizes = [(64,800),(256,800),(512,800),(1024,800),(2048,800),(4096,800)] if model == 'tridiagonal' else [(64,400),(256,240),(512,100),(1024,48),(2048,16)]
            for n, repetitions in sizes:
                check_resources()
                # 16 exact time steps also measure a sampled path maximum for tri.
                grid = np.linspace(0, 1, 17) if model == 'tridiagonal' else np.array([0., .25, 1.])
                collected = {s:[] for s in (.25,1.)}
                energy = []
                supcol = []
                degrees = 2*np.arange(n-1, 0, -1)
                for rep in range(repetitions):
                    if model == 'tridiagonal':
                        a = RNG.normal(size=n)
                        b = np.sqrt(RNG.chisquare(degrees)/2)
                        x0, v = edge_tri(a,b,vectors=True)
                        p = v*v
                        energy.append(np.sum(p*p,axis=0)+2*np.sum(p[:-1]*p[1:],axis=0))
                    else:
                        h = gue(n)
                        x0 = edge_dense(h)
                    maximum = np.zeros(2)
                    for left, s in zip(grid[:-1],grid[1:]):
                        rho = np.exp(-(s-left)*n**(-1/3))
                        variance = -np.expm1(-2*(s-left)*n**(-1/3))
                        sd = np.sqrt(variance)
                        if model == 'tridiagonal':
                            a = rho*a + sd*RNG.normal(size=n)
                            # Rotate conditional vector OU so old vector lies on first axis.
                            # Squared radius is one shifted normal square plus d-1 chi squares.
                            b = np.sqrt(((rho*np.sqrt(2)*b + sd*RNG.normal(size=n-1))**2
                                         + variance*RNG.chisquare(degrees-1))/2)
                            x = edge_tri(a,b)
                        else:
                            h = rho*h + sd*gue(n)
                            x = edge_dense(h)
                        maximum = np.maximum(maximum, np.abs(x-x0))
                        if s in collected:
                            collected[s].append((x0.copy(),x.copy()))
                            for j in range(2):
                                writer.writerow((model,n,rep,s,j+1,x0[j],x[j],x[j]-x0[j],maximum[j]))
                    supcol.append(maximum**2)
                    if rep % 40 == 0:
                        stream.flush()
                        check_resources()
                for s, pairs in collected.items():
                    first = np.array([p[0] for p in pairs])
                    last = np.array([p[1] for p in pairs])
                    sq = (last-first)**2
                    for j in range(2):
                        record = dict(model=model,n=n,replicates=repetitions,s=s,rank=j+1,
                            mean_squared_increment=float(sq[:,j].mean()),
                            se_squared_increment=float(sq[:,j].std(ddof=1)/np.sqrt(repetitions)),
                            correlation=float(np.corrcoef(first[:,j],last[:,j])[0,1]),
                            mean_grid_sup_squared=float(np.array(supcol)[:,j].mean()),
                            mean_Gamma=float(np.mean(energy,axis=0)[j]) if energy else 1.)
                        stats.append(record)
                print(model,n,repetitions,'MSE(s=1)',[round(x['mean_squared_increment'],5) for x in stats[-2:]],
                      'elapsed',round(time.monotonic()-start,1),'peak_MB',round(check_resources()/1024**2,1),flush=True)
                with (OUT / 'independent_summary.csv').open('w') as summary:
                    sw = csv.DictWriter(summary, fieldnames=list(stats[0]))
                    sw.writeheader()
                    sw.writerows(stats)
    metadata = dict(seed=SEED, elapsed_seconds=time.monotonic()-start, peak_rss_bytes=check_resources(),
                    nice=os.getpriority(os.PRIO_PROCESS,0), thread_limits=1, pools=threadpool_info(),
                    numpy=np.__version__,python=sys.version, path_maximum='Sampled 16-step grid only; not continuum supremum')
    (OUT / 'independent_metadata.json').write_text(json.dumps(metadata,indent=2))

if __name__ == '__main__':
    with threadpool_limits(limits=1):
        experiment()
