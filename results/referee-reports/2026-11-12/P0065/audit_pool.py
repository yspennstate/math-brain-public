"""Independent synchronous population dynamics with derivative and common randomness.

One law/seed is a separate bounded invocation. No trees or programs from authors.
All arrays <100 MB in the default run; signal alarm enforces <5 minutes.
"""
import os
for name in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):
    os.environ[name]='1'
import signal
signal.alarm(280)
import argparse
import json
import time
import numpy as np


MEANS={'12':1.5,'24':3.,'123':2.,'geom':2.}


def offspring(rng,law,p):
    if law=='12': return rng.integers(1,3,p)
    if law=='24': return 2*rng.integers(1,3,p)
    if law=='123': return rng.integers(1,4,p)
    if law=='geom': return rng.geometric(.5,p)
    raise ValueError(law)


def run(law,seed,p,sweeps,average):
    start=time.monotonic()
    rng=np.random.default_rng(seed)
    # Fine near zero, and the requested dimension grid, all sharing draws.
    ratios=np.array([0.,.0025,.005,.01,.02]+[i/10 for i in range(1,10)])
    lam=(ratios*MEANS[law])[:,None]
    b=np.ones((len(lam),p)); db=np.zeros_like(b)
    with open('exact_results.json') as f:
        constants=json.load(f)['constants'][law]
    ell=float(constants['d0'])
    samples=[]
    checkpoints={}
    for sweep in range(sweeps):
        n=offspring(rng,law,p)
        # A ragged collection of child slots, reduced by independent root labels.
        parent=np.repeat(np.arange(p),n)
        child=rng.integers(p,size=len(parent))
        s=np.stack([np.bincount(parent,weights=row[child],minlength=p) for row in b])
        ds=np.stack([np.bincount(parent,weights=row[child],minlength=p) for row in db])
        if sweep>=sweeps-average:
            other=rng.integers(p,size=p)
            B=b[:,other]; dB=db[:,other]
            D=lam-1+B+s
            W=B*s/D
            dW=(dB*s+B*ds)/D-B*s*(1+dB+ds)/D**2
            L=np.log(lam+s)
            dL=(1+ds)/(lam+s)
            ew=W.mean(axis=1)
            raw=(W*L).mean(axis=1)/ew
            quotient=((dW*L+W*dL).mean(axis=1)-raw*dW.mean(axis=1))/ew
            # Remove only the exactly known visibility baseline; retain the tilt.
            controlled=raw-raw[0]+ell
            samples.append(dict(d=controlled.tolist(),raw=raw.tolist(),derivative=quotient.tolist()))
        bnew=s/(lam+s)
        dbnew=(lam*ds-s)/(lam+s)**2
        b,db=bnew,dbnew
        if sweep+1 in (40,80,120,160,sweeps):
            checkpoints[str(sweep+1)]=b.mean(axis=1).tolist()
    avg={key:np.mean([v[key] for v in samples],axis=0).tolist() for key in samples[0]}
    result=dict(law=law,seed=seed,pool=p,sweeps=sweeps,averaged_sweeps=average,
                ratios=ratios.tolist(),lam=lam[:,0].tolist(),**avg,checkpoints=checkpoints,
                seconds=time.monotonic()-start,
                note='d = raw dimension minus paired empirical d0 plus exact d0; raw also saved')
    path=f'pool_{law}_{seed}.json'
    with open(path,'w') as f: json.dump(result,f,indent=2)
    print(json.dumps({k:v for k,v in result.items() if k not in ('checkpoints','raw')}),flush=True)


if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('law',choices=list(MEANS))
    parser.add_argument('seed',type=int)
    parser.add_argument('--pool',type=int,default=40000)
    parser.add_argument('--sweeps',type=int,default=180)
    parser.add_argument('--average',type=int,default=40)
    args=parser.parse_args()
    run(args.law,args.seed,args.pool,args.sweeps,args.average)
