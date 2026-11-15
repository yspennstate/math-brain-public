"""Summaries from independent per-graph samples; uncertainty uses graphs as units."""
import os
os.environ['OPENBLAS_NUM_THREADS']='1'
os.environ['OMP_NUM_THREADS']='1'
import csv, math, collections
from pathlib import Path
import numpy as np
from scipy.stats import poisson

old={(1000,6):(.067,.014),(1000,7):(.413,.028),(1000,8):(.713,.026),(1000,9):(.910,.017),
     (3000,7):(.035,.013),(3000,8):(.395,.035),(3000,9):(.705,.032),(3000,10):(.880,.023)}
def wilson(x,n):
    z=1.959963984540054;p=x/n;d=1+z*z/n
    mid=(p+z*z/(2*n))/d;half=z*math.sqrt(p*(1-p)/n+z*z/(4*n*n))/d
    return mid-half,mid+half
with open('referee_tables.md','w') as out:
    out.write('| n | k | samples | mean Z (SE) | lambda | variance | P(conn) (SE) | limit | empirical TV | no-isolate disconnections |\n')
    out.write('|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|\n')
    for n in [1000,2000,3000,10000,50000]:
        groups=collections.defaultdict(list)
        path=f'referee_sim_{n}_window.csv' if n==1000 else f'referee_sim_{n}.csv'
        with open(path) as f:
            for row in csv.DictReader(f):groups[int(row['k'])].append((int(row['Z']),int(row['components'])))
        for k,rows in sorted(groups.items()):
            Z=np.array([x[0] for x in rows]);nc=np.array([x[1] for x in rows]);T=len(Z)
            C=nc==1;lam=n*math.exp(-k);pc=C.mean();se=math.sqrt(pc*(1-pc)/T)
            upto=max(int(Z.max()),int(poisson.ppf(1-1e-13,lam)))
            h=np.bincount(Z,minlength=upto+1)/T;theory=poisson.pmf(np.arange(upto+1),lam)
            tv=(np.abs(h-theory).sum()+poisson.sf(upto,lam))/2
            fitted=poisson.pmf(np.arange(upto+1),Z.mean())
            fitted_tv=(np.abs(h-fitted).sum()+poisson.sf(upto,Z.mean()))/2
            bad=np.count_nonzero((Z==0)&~C)
            out.write(f'| {n} | {k} | {T} | {Z.mean():.4f} ({Z.std(ddof=1)/math.sqrt(T):.4f}) | {lam:.4f} | {Z.var(ddof=1):.4f} | {pc:.4f} ({se:.4f}) | {math.exp(-lam):.4f} | {tv:.4f} | {bad} |\n')
            f2=Z*(Z-1);scale=lam*lam*(n-1)/n
            print(f'n={n} k={k} T={T} p1ratio={Z.mean()/lam:.6f}+/-{Z.std(ddof=1)/math.sqrt(T)/lam:.6f} p2ratio={f2.mean()/scale:.6f}+/-{f2.std(ddof=1)/math.sqrt(T)/scale:.6f} fittedPoissonTV={fitted_tv:.6f} connWilson95={wilson(int(C.sum()),T)}')
            if (n,k) in old:
                p,s=old[n,k];diff=(pc-p)/math.sqrt(se*se+s*s)
                print(f'  paperConnectivity={p:.3f}+/-{s:.3f} independentMinusPaperSE={diff:.3f}')
    # Check the exact K4 distribution without using the limiting formulas.
    g=collections.defaultdict(list)
    with open('referee_sim_4.csv') as f:
        for row in csv.DictReader(f):g[int(row['k'])].append(int(row['Z']))
    for k,zs in sorted(g.items()):
        h=collections.Counter(zs)
        print('K4 validation',k,'histogram',dict(h),'P(Z=0)',h[0]/len(zs))
