"""Independent direct harmonic-ray entropy on lazily unfolded finite trees.

Keep each sampled node's offspring and child indices for all stored layers.
Conditional selection uses its actual children's beta values, retaining dependence.
Unfolding shared nodes produces a tree. Population sharing and finite depths are
systematic approximations, not included in across-seed standard errors.
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


def run(seed,p=12000,depth=420,rays=12000):
    start=time.monotonic()
    rng=np.random.default_rng(seed)
    lam=np.array([.3,.75,1.2])[:,None]
    b=np.ones((3,p))
    # Each layer lists children in the PREVIOUS layer. A second child with zero
    # weight is masked off for N=1. All arrays well under 250MB combined.
    history_b=[b.copy()]; history_children=[]; history_n=[]
    for lev in range(depth):
        n=rng.integers(1,3,p).astype(np.uint8)
        children=rng.integers(p,size=(p,2),dtype=np.int32)
        mask=np.arange(2)[None,:]<n[:,None]
        s=(b[:,children]*mask).sum(axis=2)
        b=s/(lam+s)
        history_children.append(children); history_n.append(n)
        history_b.append(b.copy())
    # Formula estimate at the independent root drawn above the last pool.
    n=rng.integers(1,3,p)
    children=rng.integers(p,size=(p,2))
    s=(b[:,children]*(np.arange(2)[None,:]<n[:,None])).sum(axis=2)
    B=b[:,rng.integers(p,size=p)]
    W=B*s/(lam-1+B+s)
    dimension=(W*np.log(lam+s)).sum(axis=1)/W.sum(axis=1)
    paths=[]
    # 40-level initial segment; then compare length 120,240,360 time averages.
    for a in range(3):
        idx=rng.integers(p,size=rays)
        increments=[]
        for lev in range(depth,40,-1):
            children=history_children[lev-1][idx]
            n=history_n[lev-1][idx]
            weights=history_b[lev-1][a,children].copy()
            weights[:,1]*=(n==2)
            probs=weights/weights.sum(axis=1)[:,None]
            pick=(rng.random(rays)>=probs[:,0]).astype(int)
            increments.append(-np.log(probs[np.arange(rays),pick]))
            idx=children[np.arange(rays),pick]
        increments=np.array(increments)
        # literal -(1/n)log mass from the root, and a burn-in version
        paths.append({str(length):dict(root=float(increments[:length].mean()),
                                      burn20=float(increments[20:20+length].mean()))
                      for length in (120,240,360)})
    result=dict(seed=seed,pool=p,depth=depth,rays=rays,lambda_values=lam[:,0].tolist(),
                formula=dimension.tolist(),paths=paths,seconds=time.monotonic()-start)
    with open(f'ray_{seed}.json','w') as f: json.dump(result,f,indent=2)
    print(json.dumps(result),flush=True)


if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('seed',type=int)
    args=parser.parse_args()
    run(args.seed)
