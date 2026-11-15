#!/usr/bin/env python3
"""Reproducible torus experiments. One solver and one numerical thread."""
import os
for variable in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','VECLIB_MAXIMUM_THREADS',
                 'MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):
    os.environ[variable]='1'
import argparse
import csv
import hashlib
import json
from pathlib import Path
import resource
import subprocess
import time
import numpy as np
from scipy.spatial import cKDTree

ROOT=Path(__file__).resolve().parents[1]
# macOS sandbox may disallow changing the address-space limit. Memory is also
# bounded by construction: a point array and 33 neighbors per point, n<=10000.
try:
    soft,hard=resource.getrlimit(resource.RLIMIT_AS)
    cap=min(3_000_000_000,hard) if hard!=resource.RLIM_INFINITY else 3_000_000_000
    resource.setrlimit(resource.RLIMIT_AS,(cap,hard))
except (ValueError,OSError):
    pass

def instance(n, index, kicks=80, audit=False, seed_base=300013):
    point_seed=seed_base+n*1_000_000+index
    xy=np.random.Generator(np.random.PCG64(point_seed)).random((n,2))
    k=min(32,n-1)
    distances,indices=cKDTree(xy,boxsize=1.0).query(xy,k=k+1,workers=1)
    assert np.array_equal(indices[:,0],np.arange(n))
    payload=f'{n} {k} {kicks} {point_seed+177} {int(audit)}\n'
    payload+='\n'.join(f'{x:.17g} {y:.17g}' for x,y in xy)+'\n'
    payload+='\n'.join(' '.join(map(str,row)) for row in indices[:,1:])+'\n'
    proc=subprocess.run([str(ROOT/'code/torus_tsp')],input=payload,text=True,
                        stdout=subprocess.PIPE,stderr=subprocess.PIPE,check=True)
    result=json.loads(proc.stdout)
    tour=np.array(result.pop('tour'),dtype=np.int64)
    assert np.array_equal(np.sort(tour),np.arange(n))
    delta=np.abs(xy[tour]-xy[np.roll(tour,-1)])
    delta=np.minimum(delta,1-delta)
    independent=float(np.sqrt((delta*delta).sum(axis=1)).sum())
    assert abs(independent-result['best'])<1e-9
    result.update(n=n,index=index,point_seed=point_seed,kicks=kicks,
                  lower_bound=float(0.5*distances[:,1:3].sum()),
                  points_sha256=hashlib.sha256(xy.tobytes()).hexdigest(),
                  length_recheck=independent,
                  nice=os.getpriority(os.PRIO_PROCESS,0),
                  python_peak_rss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
                  child_peak_rss_bytes=resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss)
    assert result['lower_bound']<=result['best']+1e-10
    return result,xy,tour

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--sizes',default='100:400,300:400,1000:300,3000:200,10000:120')
    parser.add_argument('--kicks',type=int,default=80)
    parser.add_argument('--output',default='torus_samples.csv')
    parser.add_argument('--seed-base',type=int,default=300013)
    parser.add_argument('--audit',action='store_true')
    parser.add_argument('--offset',type=int,default=0)
    args=parser.parse_args()
    path=ROOT/'data'/args.output
    path.parent.mkdir(exist_ok=True)
    done=set()
    if path.exists():
        with path.open() as f:
            done={(int(r['n']),int(r['index'])) for r in csv.DictReader(f)}
    begin=time.monotonic()
    with path.open('a',buffering=1) as f:
        writer=None
        for spec in args.sizes.split(','):
            n,count=map(int,spec.split(':'))
            for index in range(args.offset,args.offset+count):
                if (n,index) in done:continue
                state=Path('~/.claude/compute/compute_state.json')
                if state.exists():
                    governor=json.loads(state.read_text())
                    if governor.get('status')=='distress':
                        print('Stopped before next instance: compute distress',flush=True)
                        return
                row,xy,tour=instance(n,index,args.kicks,args.audit,args.seed_base)
                if writer is None:
                    writer=csv.DictWriter(f,fieldnames=list(row))
                    if f.tell()==0:writer.writeheader()
                writer.writerow(row)
                if index==args.offset:
                    artifact=ROOT/'data'/f'{path.stem}_n{n}_example.json'
                    artifact.write_text(json.dumps({'row':row,'points':xy.tolist(),'tour':tour.tolist()}))
                if (index-args.offset+1)%20==0 or count==1:
                    print(json.dumps({'n':n,'completed':index-args.offset+1,
                                      'elapsed_s':round(time.monotonic()-begin,1),
                                      'last_solver_s':round(row['seconds'],3)}),flush=True)

if __name__=='__main__':main()
