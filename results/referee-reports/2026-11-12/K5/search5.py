"""Bounded sequential random/restart log-weight search over all ten pair merges.

All numerical winners are recomputed with fractions; numerical values alone are
never accepted as a lower bound. Run with BLAS thread counts fixed to one.
"""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):
    os.environ[key] = '1'
import time
import argparse
import itertools
import numpy as np
from scipy.optimize import minimize
from fractions import Fraction
from exact_core import calculate, lump, save_json, leaf_family

TRI = np.triu_indices(5)
PAIRS = list(itertools.combinations(range(5),2))
MAPS = []
for pair in PAIRS:
    _, groups = lump([[0]*5 for _ in range(5)],pair)
    a = np.zeros((5,4))
    for j,g in enumerate(groups):
        a[g,j] = 1
    MAPS.append(a)


def matrix(z):
    w = np.zeros((5,5))
    w[TRI] = np.exp(z)
    return w + w.T - np.diag(w.diagonal())


def mix(w):
    d = w.sum(axis=1)
    n = len(d)
    root = int(np.argmax(d))
    ix = [i for i in range(n) if i != root]
    lap = np.diag((w-np.diag(w.diagonal())).sum(axis=1))-w+np.diag(w.diagonal())
    k = np.zeros((n,n))
    k[np.ix_(ix,ix)] = np.linalg.inv(lap[np.ix_(ix,ix)])
    a = k@d
    return np.max(a[:,None]+a[None,:]-(d@a)/d.sum()-d.sum()*k)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--seconds',type=float,default=150)
    parser.add_argument('--seed',type=int,default=20261112)
    parser.add_argument('--random',type=int,default=4000)
    args = parser.parse_args()
    rng = np.random.default_rng(args.seed)
    begun = time.monotonic()
    deadline = begun+args.seconds
    candidates = []
    best = 0
    history = []
    count = 0
    rejected = 0
    per_pair = [0.]*10

    def score(z,which=None):
        nonlocal count
        if time.monotonic() > deadline:
            raise TimeoutError
        count += 1
        try:
            w = matrix(z)
            tx = mix(w)
            ids = range(10) if which is None else [which]
            ratios = [(mix(MAPS[j].T@w@MAPS[j])/tx,j) for j in ids]
            val,j = max(ratios)
            if not np.isfinite(val) or val > 3.00001 or tx <= 0:
                return (0.,0)
            return float(val),j
        except np.linalg.LinAlgError:
            return (0.,0)

    def consider(z,val,j,stage):
        nonlocal best, rejected
        per_pair[j] = max(val,per_pair[j])
        if val > best+1e-10:
            # Eight significant digits, positive rational weights.
            w = matrix(z)
            ew = [[Fraction(format(x,'.8g')) for x in row] for row in w]
            x = calculate(ew)
            hy,groups = lump(ew,PAIRS[j])
            y = calculate(hy)
            er = y['tmix']/x['tmix']
            if abs(float(er)-val) > 2e-5:
                rejected += 1
                return
            best = float(er)
            record = dict(stage=stage, seconds=time.monotonic()-begun,
                          numerical_ratio=val,exact_ratio=er,weights=ew,
                          pair=PAIRS[j],groups=groups, original=x['tmix'],
                          quotient=y['tmix'],original_pairs=x['pairs'],
                          quotient_pairs=y['pairs'])
            history.append(record)
            save_json('search5_best.json',record)
            print(f"best={best:.14f} pair={PAIRS[j]} stage={stage} evals={count}",flush=True)

    try:
        for r in range(args.random):
            z = rng.uniform(-10,10,15)
            if r%3 == 0:
                z[rng.random(15)<.35] = -14
            val,j = score(z)
            candidates.append((val,j,z.copy()))
            consider(z,val,j,'random')
        # Symmetric four-state and five-state constructions, perturbed to break symmetry.
        for t in (3,10,50):
            w = np.array(leaf_family(3,t),dtype=float)
            z = np.log(np.maximum(w[TRI],1e-6))
            z -= .5*(z.max()+z.min())
            z = np.clip(z,-14,14)
            val,j = score(z)
            candidates.append((val,j,z.copy()))
            consider(z,val,j,'structured')
        seeds = sorted(candidates,key=lambda x:x[0],reverse=True)[:12]
        # Ensure every pair has its own locally optimized random start.
        for j in range(10):
            subset = [c for c in candidates if c[1] == j]
            if subset:
                seeds.append(max(subset,key=lambda x:x[0]))
            else:
                z = rng.uniform(-7,7,15)
                seeds.append((0,j,z))
        for run,(val,j,z) in enumerate(seeds):
            print(f"restart={run} pair={PAIRS[j]} initial={val:.10f}",flush=True)
            def obj(v):
                val,jj = score(v,j)
                consider(v,val,jj,'local')
                return -val
            res = minimize(obj,z,method='Powell',bounds=[(-14,14)]*15,
                           options=dict(maxfev=2000,xtol=1e-5,ftol=1e-9))
            val,jj = score(res.x)
            consider(res.x,val,jj,'all-pairs-after-local')
    except TimeoutError:
        print('Time budget reached.',flush=True)
    result = dict(seed=args.seed, wall_seconds=time.monotonic()-begun,
                  evaluations=count,rejected_numerical_records=rejected,
                  best=history[-1] if history else None, history=history,
                  numerical_best_by_pair=per_pair)
    save_json('search5_results.json',result)
    print(f"FINAL best={best:.14f} evaluations={count} seconds={result['wall_seconds']:.3f} rejected={rejected}",flush=True)


if __name__ == '__main__':
    main()
