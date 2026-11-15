#!/usr/bin/env python3
import os
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):os.environ[k]='1'
assert os.getpriority(os.PRIO_PROCESS,0)>=10
import csv,math
from pathlib import Path
import numpy as np
from scipy.special import roots_legendre
ROOT=Path(__file__).resolve().parents[1]
x,w=roots_legendre(160);x=(x+1)/2;w=w/2
phi=np.exp(4-1/(x*(1-x)))
rows=[]
for r in csv.DictReader((ROOT/'data'/'smooth_witnesses.csv').open()):
    if r['L']!='8192':continue
    beta=float(r['beta'])
    kernel=math.gamma(beta+1)*abs(math.sin(math.pi*beta/2))/math.pi
    J=float(np.sum((w*phi)[:,None]*(w*phi)[None,:]/abs(x[:,None]-(x[None,:]+2))**(1+beta)))
    expected=kernel*J
    observed=float(r['correlation'])*float(r['scaled_variance'])
    rows.append(dict(beta=beta,L=8192,predicted_abs_scaled_cross=expected,observed_abs_scaled_cross=observed,absolute_error=abs(expected-observed)))
with (ROOT/'data'/'kernel_limit_checks.csv').open('w',newline='') as f:
    writer=csv.DictWriter(f,fieldnames=list(rows[0]));writer.writeheader();writer.writerows(rows)
for r in rows:print(r)
