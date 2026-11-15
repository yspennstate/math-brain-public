#!/usr/bin/env python3
"""Reproduce D0004 discretized transport LPs and rearrangement diagnostics.

One process and one numerical thread. LP and RA results are diagnostics;
the proofs and support certificates in REPORT.md establish nonmixability.
"""
import os
for name in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS",
             "VECLIB_MAXIMUM_THREADS", "NUMEXPR_NUM_THREADS"):
    os.environ[name] = "1"
import csv
import itertools
import json
import resource
import time
from pathlib import Path
import numpy as np
import scipy
from scipy.optimize import linprog
from scipy.sparse import coo_matrix

ROOT = Path(__file__).resolve().parents[1]


def segments(n, floor=False):
    """(left,right,intercept,slope), density intercept+slope*x."""
    if n == 3:
        e, p = .1, .5
        base = [(0., e, 5., 0.), (e, 1-e, 0., 0.), (1-e, 1., 5., 0.)]
        h = (1., 0.)
    else:
        e, p = .05, .4
        base = [(0., e, 12., 0.), (e, 1-e, 0., 0.), (1-e, 1., 8., 0.)]
        h = (1.57, -1.14)
    if floor:
        return [(l,r,.9*a+.1*h[0],.9*b+.1*h[1]) for l,r,a,b in base]
    return base


def integral(seg, lo, hi, power=0):
    l,r,a,b = seg
    lo,hi = max(l,lo),min(r,hi)
    if hi <= lo:
        return 0.
    return a*(hi**(power+1)-lo**(power+1))/(power+1) + b*(hi**(power+2)-lo**(power+2))/(power+2)


def quantile(ss, q):
    out = np.empty_like(q)
    cumulative = 0.
    for seg in ss:
        l,r,a,b = seg
        mass = integral(seg,l,r)
        mask = (q >= cumulative-1e-14) & (q <= cumulative+mass+1e-14)
        if mass > 0 and np.any(mask):
            y = np.clip(q[mask]-cumulative,0,mass)
            left_density = a+b*l
            d = y/left_density if abs(b)<1e-14 else 2*y/(left_density+np.sqrt(left_density**2+2*b*y))
            out[mask] = l+d
        cumulative += mass
    return out


def grid(ss, m):
    edges = np.linspace(0,1,m+1)
    mass = np.array([sum(integral(s,l,r) for s in ss) for l,r in zip(edges[:-1],edges[1:])])
    return (edges[:-1]+edges[1:])/2, mass


def transport_lp(n, floor, m, band):
    """Exchangeable transport LP on multisets, with exact cell probabilities.

    band=True retains sums within n/(2*m) of the true center. Any continuous
    complete mix pushes forward to a feasible point of this relaxed LP.
    band=False minimizes squared sum deviation over all midpoint tuples.
    """
    ss = segments(n,floor)
    mu = sum(integral(s,0,1,1) for s in ss)
    x,p = grid(ss,m)
    active = np.flatnonzero(p>1e-13)
    xs,ps = x[active],p[active]
    rows,cols,values,cost = [],[],[],[]
    count = 0
    for prefix in itertools.combinations_with_replacement(range(len(xs)),n-1):
        subtotal = sum(xs[j] for j in prefix)
        first = prefix[-1]
        if band:
            lo = np.searchsorted(xs,n*mu-n/(2*m)-subtotal-1e-12,side='left')
            hi = np.searchsorted(xs,n*mu+n/(2*m)-subtotal+1e-12,side='right')
            js = range(max(first,lo),hi)
        else:
            js = range(first,len(xs))
        for j in js:
            tup = prefix+(j,)
            for k in set(tup):
                rows.append(k);cols.append(count);values.append(tup.count(k)/n)
            cost.append(0. if band else (subtotal+xs[j]-n*mu)**2)
            count += 1
    start = time.monotonic()
    if count:
        aeq = coo_matrix((values,(rows,cols)),shape=(len(xs),count)).tocsc()
        result = linprog(cost,A_eq=aeq,b_eq=ps,bounds=(0,None),method='highs',
                         options={'threads':1,'time_limit':20.,'primal_feasibility_tolerance':1e-9,
                                  'dual_feasibility_tolerance':1e-9})
        status = int(result.status)
        objective = float(result.fun) if result.success else None
        residual = float(np.max(np.abs(aeq@result.x-ps))) if result.success else None
    else:
        status,objective,residual = 2,None,None
    return dict(n=n,floor=floor,m=m,kind='band_feasibility' if band else 'min_squared_error',
                columns=count,status=status,objective=objective,residual=residual,
                seconds=round(time.monotonic()-start,4),mean=mu,band=n/(2*m) if band else None)


def rearrangement(n, floor, m, restarts=4, sweeps=100):
    ss = segments(n,floor)
    q = quantile(ss,(np.arange(m)+.5)/m)
    target = n*sum(integral(s,0,1,1) for s in ss)
    rng = np.random.default_rng(20261113+n+m+int(floor))
    best = None
    for restart in range(restarts):
        arr = np.column_stack([rng.permutation(q) for _ in range(n)])
        old = np.inf
        for sweep in range(sweeps):
            for j in range(n):
                partial = arr.sum(axis=1)-arr[:,j]
                order = np.argsort(partial,kind='stable')
                arr[order,j] = q[::-1]
            sums = arr.sum(axis=1)
            mse = float(np.mean((sums-target)**2))
            if old-mse < 1e-14:
                break
            old = mse
        row = dict(n=n,floor=floor,m=m,restart=restart,sweeps=sweep+1,
                   mse=mse,min_sum=float(sums.min()),max_sum=float(sums.max()),
                   quantile_mean=float(q.mean()),target=target)
        if best is None or mse<best['mse']:
            best=row
    return best


def main():
    data = ROOT/'data'
    lp=[];ra=[]
    for n in (3,4):
        for floor in (False,True):
            for m in (20,40,80,160):
                row=transport_lp(n,floor,m,True);lp.append(row)
                print(json.dumps(row),flush=True)
            for m in (10,20):
                row=transport_lp(n,floor,m,False);lp.append(row)
                print(json.dumps(row),flush=True)
            for m in (1000,4000,16000):
                row=rearrangement(n,floor,m);ra.append(row)
                print(json.dumps(row),flush=True)
    for name,records in [('lp_results',lp),('ra_results',ra)]:
        (data/(name+'.json')).write_text(json.dumps(records,indent=2)+'\n')
        with (data/(name+'.csv')).open('w',newline='') as f:
            w=csv.DictWriter(f,fieldnames=list(records[0]));w.writeheader();w.writerows(records)
    # macOS ru_maxrss is in bytes, Linux in KiB.
    import sys
    rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    rss_bytes=rss if sys.platform=='darwin' else rss*1024
    meta=dict(numpy=np.__version__,scipy=scipy.__version__,python=sys.version,
              peak_rss_bytes=rss_bytes,threads=1,seed=20261113)
    (data/'environment.json').write_text(json.dumps(meta,indent=2)+'\n')
    if rss_bytes>=4_000_000_000:
        raise RuntimeError('4 GB memory budget exceeded')


if __name__=='__main__':
    main()
