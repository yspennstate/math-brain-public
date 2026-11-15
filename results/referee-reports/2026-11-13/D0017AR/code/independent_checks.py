#!/usr/bin/env python3
"""Independent finite-dimensional checks; no submitted code is imported.

Run from the audit root. Covariance tests are not proofs of the lemmas.
"""
import os
for name in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'VECLIB_MAXIMUM_THREADS',
             'MKL_NUM_THREADS', 'NUMEXPR_NUM_THREADS'):
    os.environ[name] = '1'
import json
import math
from pathlib import Path
import resource
import time
import numpy as np


def bridge_variance(t, anchors):
    anchors = np.unique(anchors)
    if np.any(anchors == t):
        return 0.0
    left = anchors[anchors < t][-1]
    right = anchors[anchors > t][0]
    return (t-left)*(right-t)/(right-left)


def covariance_check(rng):
    a = 0.375
    records = []
    modes = ('continuous', 'grid', 'duplicates', 'cycle', 'target_repeated', 'boundary')
    for mode in modes:
        for repeat in range(350):
            k = int(rng.integers(0, 26))
            pairs = np.column_stack((rng.random(k), 2+rng.random(k)))
            target = np.array([rng.random(), 2+rng.random()])
            if mode == 'grid':
                pairs = np.round(pairs*16)/16
                target = np.round(target*16)/16
            elif mode == 'duplicates' and k:
                pairs = pairs[rng.integers(0, max(1, k//3), k)]
            elif mode == 'cycle' and k >= 4:
                uu = rng.random(2)
                vv = 2+rng.random(2)
                pairs[:4] = [[uu[0],vv[0]], [uu[0],vv[1]],
                             [uu[1],vv[0]], [uu[1],vv[1]]]
                target = np.array([uu[1],vv[1]])
            elif mode == 'target_repeated' and k:
                target = pairs[0].copy()
            elif mode == 'boundary':
                target = np.array([float(rng.choice([0,1])),float(rng.choice([2,3]))])
            all_pairs = np.vstack((pairs, target))
            # Independent Brownian increments on the atomic partition give an
            # L2 representation of every pair-difference as a row vector.
            times = np.unique(np.r_[0,1,2,3,all_pairs.ravel()])
            midpoints = (times[1:]+times[:-1])/2
            rows = ((all_pairs[:,0,None] < midpoints) &
                    (midpoints < all_pairs[:,1,None])) * np.sqrt(np.diff(times))
            if k:
                weights = np.linalg.lstsq(rows[:-1].T, rows[-1], rcond=1e-12)[0]
                residual = rows[-1] - np.einsum('i,ij->j', weights, rows[:-1])
            else:
                residual = rows[-1]
            s = float(a + 3*rng.random())
            conditional = s*float(residual @ residual)
            # Second derivation: Gaussian covariance is s times overlap length.
            overlap = np.maximum(0, np.minimum(all_pairs[:,1,None],all_pairs[None,:,1])
                                    -np.maximum(all_pairs[:,0,None],all_pairs[None,:,0]))
            if k:
                eigenvalues, eigenvectors = np.linalg.eigh(overlap[:-1,:-1])
                keep = eigenvalues > 1e-12*max(eigenvalues[-1],1e-300)
                coefficients = np.einsum('ij,i->j',eigenvectors[:,keep],overlap[:-1,-1])
                schur = s*float(overlap[-1,-1] - np.sum(coefficients**2/eigenvalues[keep]))
            else:
                schur = s*float(overlap[-1,-1])
            U = np.r_[0,1,pairs[:,0]]
            V = np.r_[2,3,pairs[:,1]]
            rho = float(np.min(abs(U-target[0])) + np.min(abs(V-target[1])))
            bridge = s*(bridge_variance(target[0],U)+bridge_variance(target[1],V))
            lower = a*rho/2
            assert np.isfinite(conditional) and np.isfinite(schur)
            assert conditional + 2e-9 >= bridge >= lower-2e-12
            assert abs(conditional-schur) < 2e-7
            records.append(dict(mode=mode,k=k,s=s,conditional=conditional,
                                schur=schur,bridge=bridge,lower=lower))
    return dict(configurations=len(records), seed=131117,
                minimum_conditional_minus_bridge=min(x['conditional']-x['bridge'] for x in records),
                minimum_bridge_minus_lower=min(x['bridge']-x['lower'] for x in records),
                maximum_schur_discrepancy=max(abs(x['conditional']-x['schur']) for x in records),
                modes=list(modes), records=records)


def lattice_check(rng):
    records=[]
    max_shell=0
    for n in range(3,10):
        delta=2.0**(-n)
        u=np.arange(2**n+1)*delta
        v=2+u
        for k in (0,1,3,9):
            # Deliberately include anchors off the sampling lattice.
            U=np.r_[0,1,rng.integers(0,2**(n+2)+1,k)*delta/4]
            V=np.r_[2,3,2+rng.integers(0,2**(n+2)+1,k)*delta/4]
            for grid,anchors in ((u,U),(v,V)):
                for anchor in anchors:
                    shell=np.floor(abs(grid-anchor)/delta).astype(int)
                    max_shell=max(max_shell,int(np.bincount(shell).max()))
            rho_u=np.min(abs(u[:,None]-U),axis=1)
            rho_v=np.min(abs(v[:,None]-V),axis=1)
            Q=math.ceil(4/delta)
            q=np.arange(Q+1,dtype=float)
            harmonic=float(np.sum(1/(q+1)))
            for r2 in (delta,delta**0.7,0.5,1.0):
                total=float(np.sum(r2**2/(r2+rho_u[:,None]+rho_v[None,:])**2))
                qsum=float(np.sum((q+1)/(r2/delta+q)**2))
                factor=16*(k+2)**2*r2**2*delta**-2
                shell_bound=factor*qsum
                harmonic_bound=factor*harmonic
                assert qsum <= harmonic+1e-10
                assert total <= shell_bound+1e-8 <= harmonic_bound+1e-8
                records.append(dict(n=n,k=k,r2=r2,total=total,shell_bound=shell_bound,
                                    harmonic_bound=harmonic_bound,
                                    ratio_to_stated_scale=total/((k+2)**2*r2**2*delta**-2*(1+math.log(1/delta)))))
    assert max_shell <=4
    return dict(configurations=len(records),maximum_points_in_one_anchor_shell=max_shell,
                maximum_normalized_sum=max(x['ratio_to_stated_scale'] for x in records),records=records)


def dimensional_sanity():
    values=[]
    for n in range(4,10):
        delta=2.0**-n
        grid=np.arange(2**n+1)*delta
        rho=np.minimum(grid,1-grid)
        for d in (3,4):
            total=float(np.sum((delta/(delta+rho[:,None]+rho[None,:]))**(d/2)))
            values.append(dict(n=n,d=d,total=total,
                               normalized=total/(delta**(-0.5) if d==3 else 1+math.log(1/delta))))
    return values


if __name__=='__main__':
    start=time.monotonic()
    priority=os.getpriority(os.PRIO_PROCESS,0)
    if priority<10:
        os.nice(10-priority)
    rng=np.random.default_rng(131117)
    result=dict(covariance=covariance_check(rng),lattice=lattice_check(rng),
                dimension_sanity=dimensional_sanity(),nice=os.getpriority(os.PRIO_PROCESS,0),
                numerical_threads=1)
    result['seconds']=time.monotonic()-start
    result['peak_rss_bytes']=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    Path('data/independent_checks.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:({a:b for a,b in v.items() if a!='records'} if isinstance(v,dict) else v)
                      for k,v in result.items()},indent=2))
