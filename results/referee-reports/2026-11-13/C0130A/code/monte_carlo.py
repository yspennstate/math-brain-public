"""Independent forward branching-process Monte Carlo.

It estimates finite-generation survival, an upper bound on infinite survival.
No finite simulation is mislabeled as an observation of infinite escape.
"""
import argparse
import json
import os
import time
from pathlib import Path

os.environ.setdefault('OPENBLAS_NUM_THREADS', '1')
os.environ.setdefault('OMP_NUM_THREADS', '1')
import numpy as np


def run(M, p, samples, generations, seed):
    rng = np.random.default_rng(seed)
    population = np.ones(samples, dtype=np.int64)
    output = []
    checkpoints = sorted(set([256,1024,4096,generations]))
    start = time.monotonic()
    for n in range(1, generations+1):
        big = population >= M
        result = np.zeros(len(population), dtype=np.int64)
        successes = rng.binomial(M, p, int(np.sum(big)))
        left = population[big] - M + successes
        after = np.zeros(len(left), dtype=np.int64)
        pos = left > 0
        after[pos] = rng.negative_binomial(left[pos], .5)
        result[big] = successes + after
        small = ~big
        k = population[small].copy()
        s = np.zeros(len(k), dtype=np.int64)
        for _ in range(M):
            active = k > 0
            coin = rng.random(int(np.sum(active))) < p
            s[active] += coin
            k[active] -= ~coin
        pos = k > 0
        s[pos] += rng.negative_binomial(k[pos], .5)
        result[small] = s
        population = result[result > 0]
        if n in checkpoints:
            q = len(population) / samples
            se = float(np.sqrt(q*(1-q)/samples))
            output.append(dict(generation=n, survivors=len(population),
                               survival=q, standard_error=se,
                               escape_upper_estimate=p*q,
                               escape_standard_error=p*se,
                               max_population=int(np.max(population)) if len(population) else 0))
            print(n,len(population),p*q,'seconds',round(time.monotonic()-start,2),flush=True)
        if not len(population):
            break
    return dict(M=M,p=p,samples=samples,generations=generations,seed=seed,
                checkpoints=output,seconds=time.monotonic()-start,
                priority=os.getpriority(os.PRIO_PROCESS,0),
                interpretation='Finite-generation survival; binomial standard error excludes finite-generation bias.')


if __name__ == '__main__':
    ap=argparse.ArgumentParser()
    ap.add_argument('--M',type=int,required=True)
    ap.add_argument('--p',type=float,required=True)
    ap.add_argument('--samples',type=int,default=100000)
    ap.add_argument('--generations',type=int,default=16384)
    ap.add_argument('--seed',type=int,default=130)
    ap.add_argument('--output',required=True)
    args=ap.parse_args()
    result=run(args.M,args.p,args.samples,args.generations,args.seed)
    Path(args.output).write_text(json.dumps(result,indent=2)+'\n')
