"""Reproducible minimum-coordinate experiments; one BLAS thread, one worker."""
import os
for key in ('OPENBLAS_NUM_THREADS', 'MKL_NUM_THREADS', 'OMP_NUM_THREADS',
            'VECLIB_MAXIMUM_THREADS', 'NUMEXPR_NUM_THREADS'):
    os.environ[key] = '1'

import argparse
import csv
import datetime
import json
from pathlib import Path
import resource
import time

import numpy as np
import scipy
from scipy.linalg import eigh
from scipy.stats import kstest
from threadpoolctl import threadpool_limits, threadpool_info

ROOT = Path(__file__).resolve().parents[1]
RATE = np.sqrt(2 / np.pi)

def governor():
    path = Path('~/.claude/compute/compute_state.json')
    if path.exists():
        state = json.loads(path.read_text())
        if state.get('status') == 'distress':
            raise RuntimeError('Compute governor is in distress; stop this experiment')
        return {k: state.get(k) for k in ('ts', 'status', 'mode')}
    return {'status': 'unavailable'}

def matrix(rng, n, ensemble):
    if ensemble == 'goe':
        raw = rng.normal(size=(n, n))
        w = np.triu(raw, 1)
        w += w.T
        w[np.diag_indices(n)] = rng.normal(scale=np.sqrt(2), size=n)
    elif ensemble == 'rademacher':
        raw = 2 * rng.integers(0, 2, size=(n, n), dtype=np.int8) - 1
        w = np.triu(raw).astype(float)
        w += np.triu(w, 1).T
    elif ensemble == 'bernoulli_p010':
        p = 0.10  # fixed in n; centered, variance one, bounded atom law
        raw = (rng.random((n, n)) < p).astype(float)
        raw = (raw - p) / np.sqrt(p * (1-p))
        w = np.triu(raw)
        w += np.triu(w, 1).T
    else:
        raise ValueError(ensemble)
    return np.array(w / np.sqrt(n), order='F')

def run(args):
    root = ROOT / 'data'
    root.mkdir(exist_ok=True)
    output = root / (args.tag + '_samples.csv')
    meta_path = root / (args.tag + '_metadata.json')
    if output.exists():
        raise RuntimeError(f'Will not overwrite {output}')
    rng = np.random.default_rng(args.seed)
    start = time.monotonic()
    initial_governor = governor()
    metadata = {'seed': args.seed, 'sizes_and_repetitions': args.spec,
                'ensembles': args.ensembles, 'numpy': np.__version__, 'scipy': scipy.__version__,
                'started_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
                'threads': 1, 'priority': 'inherits nice 10 from launch.sh',
                'initial_governor': initial_governor, 'status': 'running'}
    meta_path.write_text(json.dumps(metadata, indent=2))
    fields = ['ensemble','n','replicate','index','region','scaled_min','eigenvalue',
              'residual_l2','norm_error','minimum_coordinate','second_minimum_coordinate','count_t1','count_t2']
    with threadpool_limits(limits=1), output.open('w', newline='') as stream:
        writer = csv.DictWriter(stream, fieldnames=fields)
        writer.writeheader()
        for n, reps in args.spec:
            for ensemble in args.ensembles:
                for rep in range(reps):
                    if rep % 10 == 0:
                        governor()
                    w = matrix(rng, n, ensemble)
                    # Select 3 eigenpairs using three narrow calls. A subset call across
                    # [0,n-1] would compute the full eigenbasis. Each call performs its
                    # own bounded-memory tridiagonal reduction.
                    for index, region in ((0,'lower_edge'), (n//2,'bulk'), (n-1,'upper_edge')):
                        vals, vectors = eigh(w, subset_by_index=(index,index), driver='evr',
                                             check_finite=False, overwrite_a=False)
                        v = vectors[:,0]
                        absolute = np.abs(v)
                        minimums = np.partition(absolute,1)[:2]
                        # Independent scalar-loop contraction avoids this platform's spurious
                        # floating-point status warnings from NumPy/Accelerate matmul.
                        residual = np.linalg.norm(np.einsum('ij,j->i',w,v,optimize=False)-vals[0]*v)
                        assert np.isfinite(v).all() and np.isfinite(vals).all()
                        assert residual < 1e-9 and abs(np.linalg.norm(v)-1) < 1e-10
                        writer.writerow({'ensemble':ensemble,'n':n,'replicate':rep,'index':index+1,
                            'region':region,'scaled_min':n**1.5*minimums[0], 'eigenvalue':vals[0],
                            'residual_l2':residual,'norm_error':abs(np.linalg.norm(v)-1),
                            'minimum_coordinate':minimums[0], 'second_minimum_coordinate':minimums[1],
                            'count_t1':int(np.count_nonzero(absolute<=n**-1.5)),
                            'count_t2':int(np.count_nonzero(absolute<=2*n**-1.5))})
                    stream.flush()
                    if resource.getrusage(resource.RUSAGE_SELF).ru_maxrss > 3_500_000_000:
                        raise RuntimeError('Memory guard: peak RSS exceeded 3.5 GB')
                elapsed = time.monotonic()-start
                print(ensemble, n, reps, 'matrices;', round(elapsed,1), 'seconds total', flush=True)
    metadata.update(status='complete', elapsed_seconds=time.monotonic()-start,
                    max_rss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
                    threadpools=threadpool_info())
    meta_path.write_text(json.dumps(metadata, indent=2))

if __name__ == '__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--tag',default='main')
    parser.add_argument('--seed',type=int,default=980013)
    parser.add_argument('--spec',default='128:240,512:100,1024:40,2048:12')
    parser.add_argument('--ensembles',default='goe,rademacher,bernoulli_p010')
    args=parser.parse_args()
    args.spec=[tuple(map(int,x.split(':'))) for x in args.spec.split(',')]
    args.ensembles=args.ensembles.split(',')
    run(args)
