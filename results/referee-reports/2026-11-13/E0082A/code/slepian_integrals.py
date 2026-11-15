"""Randomized Sobol integration of the continuous Shepp integrals.

Condition on Brownian values at integers and integers+theta. Conditional
noncrossing probabilities are heat-kernel determinant ratios. This avoids
time-grid crossing bias. Scramble variability is numerical evidence only.
The separate analytic truncation bound is rigorous in exact arithmetic.
"""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS',
            'VECLIB_MAXIMUM_THREADS','NUMEXPR_NUM_THREADS'):
    os.environ[key]='1'
import csv
import math
from pathlib import Path
import numpy as np
from scipy.special import ndtr, ndtri
from scipy.stats import qmc


def bridge_order(start, end, duration):
    count, size=start.shape
    if not count:
        return np.zeros(0)
    if size == 1:
        return np.ones(count)
    logs=-(end[:,None,:]-start[:,:,None])**2/(2*duration[:,None,None])
    diagonal=np.einsum('nii->n',logs)
    shift=logs.max(axis=2)
    mat=np.exp(logs-shift[:,:,None])
    sign, logdet=np.linalg.slogdet(mat)
    # Tiny negative roundoff is possible near a collision; record it upstream
    # by clipping the resulting probability to its mathematical range.
    value=np.where(sign>0,np.exp(np.minimum(0,logdet+shift.sum(axis=1)-diagonal)),0)
    return value


def slab(alpha, m, power, seed):
    u=qmc.Sobol(2*m+4,scramble=True,seed=seed).random_base2(power)
    theta=u[:,0]
    z=ndtri(u[:,1:])
    a=z[:,:m+2]*np.sqrt(theta[:,None])
    b=z[:,m+2:]*np.sqrt(1-theta[:,None])
    w=np.concatenate([np.zeros((len(u),1)),np.cumsum(a[:,:m+1]+b,axis=1)],axis=1)
    yy=w+a
    total=np.zeros(len(u))
    for h in (alpha,-alpha):
        x=w+np.arange(m+2)[None,:]*h
        y=yy+np.arange(m+2)[None,:]*h
        ok=(np.diff(x,axis=1)>0).all(axis=1)&(np.diff(y,axis=1)>0).all(axis=1)
        k=np.flatnonzero(ok)
        # Bound working memory independently of quadrature size.
        for j in range(0,len(k),1024):
            ix=k[j:j+1024]
            p=bridge_order(x[ix],y[ix],theta[ix])
            p*=bridge_order(y[ix,:m+1],x[ix,1:]-h,1-theta[ix])
            total[ix]+=p
    return float(total.mean())


def one_unit(h):
    ph=math.exp(-h*h/2)/math.sqrt(2*math.pi)
    return float(ndtr(h)**2-h*ph*ndtr(h)-ph*ph)


def tail(alpha, slabs):
    answer=0
    for h in (alpha,-alpha):
        r=one_unit(h)
        if slabs%2==0:
            answer+=r**(slabs//2)*(1+r)/(1-r)
        else:
            answer+=2*r**((slabs+1)//2)/(1-r)
    return answer


def main():
    records=[]
    with Path('data/slepian_slabs.csv').open('w') as f:
        writer=csv.writer(f);writer.writerow(['alpha','slab','scramble','integral'])
        for alpha, count in [(0,12),(1,26)]:
            totals=[]
            first=[]
            for rep in range(8):
                total=0
                for m in range(count):
                    v=slab(alpha,m,14,820200+100*rep+m)
                    writer.writerow([alpha,m,rep,v]);f.flush()
                    total+=v
                    if m==0:first.append(v)
                totals.append(1+total)
                print(alpha,rep,totals[-1],flush=True)
            records.append(dict(alpha=alpha,slabs=count,scrambles=8,points_per_slab=2**14,
                truncated_constant=np.mean(totals),scramble_se=np.std(totals,ddof=1)/math.sqrt(8),
                analytic_tail_bound=tail(alpha,count),first_slab=np.mean(first),
                first_slab_se=np.std(first,ddof=1)/math.sqrt(8)))
    with Path('data/slepian_constants.csv').open('w') as f:
        writer=csv.DictWriter(f,fieldnames=records[0].keys());writer.writeheader();writer.writerows(records)


if __name__=='__main__':
    main()
