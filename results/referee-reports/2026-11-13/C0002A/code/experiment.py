"""Reproducible single-worker DGFF experiments; incremental CSV output."""
import argparse
import csv
import gc
import json
import time
from pathlib import Path
from dgff import sample, observables, check_resources, peak_bytes
import numpy as np

p=argparse.ArgumentParser()
p.add_argument('--plan', default='main', choices=['main','large','calibration'])
args=p.parse_args()
root=Path(__file__).resolve().parents[1]
plans={'main':[(32,1500),(64,1200),(128,900),(256,600),(512,350),(1024,160),
               (2048,60),(4096,12)],
       'large':[(8192,3),(16384,1)],
       'calibration':[(512,2000),(1024,600),(2048,250)]}
plan=plans[args.plan]
lambdas=[.2,.4,.6,.8]
outpath=root/'data'/f'samples_{args.plan}.csv'
metadata=dict(plan=plan,lambdas=lambdas,seed={'main':2026111301,'large':2026111302,'calibration':2026111304}[args.plan],
              resources=check_resources(max(n for n,_ in plan), np.float32 if args.plan=='large' else np.float64),
              dtype='float32' if args.plan=='large' else 'float64',
              coupling='independent field draws across N; shared field across lambdas',
              started=time.strftime('%Y-%m-%d %H:%M:%S %z'))
(root/'data'/f'metadata_{args.plan}.json').write_text(json.dumps(metadata,indent=2)+'\n')
rng=np.random.default_rng(metadata['seed'])
dtype=np.float32 if args.plan=='large' else np.float64
starttime=time.monotonic()
with outpath.open('w',newline='') as f:
    writer=csv.DictWriter(f,fieldnames=['N','replicate','lambda','count','X','Y','D','Q'])
    writer.writeheader()
    for N,reps in plan:
        t0=time.monotonic()
        for rep in range(reps):
            h=sample(N,rng,dtype)
            for lam,values in observables(h,N,lambdas).items():
                writer.writerow(dict(N=N,replicate=rep,**{'lambda':lam},**values))
            del h
            if rep%10==0: f.flush()
        f.flush(); gc.collect()
        print(f'N={N}, reps={reps}, seconds={time.monotonic()-t0:.2f}, peak={peak_bytes()/1e9:.3f} GB',flush=True)
metadata.update(seconds=time.monotonic()-starttime,peak_bytes=peak_bytes(),
                finished=time.strftime('%Y-%m-%d %H:%M:%S %z'))
(root/'data'/f'metadata_{args.plan}.json').write_text(json.dumps(metadata,indent=2)+'\n')
