"""Deterministic convolution of the law; no sampling, no criticality projection.

Written for this referee audit without consulting claim_files/code.
The positive part of a_k=m^k P(X=k) is convolved separately to avoid
subtracting the dominant zero atom inside the Fourier transform.
"""
import os
for key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS', 'VECLIB_MAXIMUM_THREADS'):
    os.environ[key] = '1'
import argparse
import csv
import json
import math
from pathlib import Path
import resource
import time
import numpy as np
from scipy.fft import rfft, irfft, next_fast_len

ROOT = Path(__file__).resolve().parents[1]

def evolve(a, m, cap, degree):
    weight = np.power(float(m), -np.arange(len(a), dtype=float))
    pzero = 1 - float(np.dot(a[1:], weight[1:]))
    # (pzero+B)^m. Its coefficients of degree >=2 determine all positive outputs.
    size = next_fast_len(m*degree+1)
    spec = rfft(a[:degree+1], n=size, workers=1)
    result = m*pzero**(m-1)*a.copy()
    negative = 0.0
    for j in range(2, m+1):
        term = irfft(spec**j, n=size, workers=1)
        valid = min(j*degree, cap+1)
        term[:j] = 0  # every factor B has minimum degree one
        term[valid+1:] = 0
        negative += float(-np.minimum(term[:valid+1], 0).sum())
        term[:valid+1] = np.maximum(term[:valid+1], 0)
        result[:valid+1] += math.comb(m,j)*pzero**(m-j)*term[:valid+1]
    out = np.zeros(cap+2)
    newdegree = min(m*degree-1, cap)
    out[1:newdegree+1] = result[2:newdegree+2]/m
    # a[0] is always zero here; pzero is computed by ordinary normalization.
    return out, newdegree, negative

def stats(a, m, n):
    k = np.arange(1,len(a),dtype=float)
    p = a[1:]*np.power(float(m),-k)
    q = float(p.sum())
    assert np.isfinite(q) and 0 < q <= 1
    cond = p/q
    pi = (m-1)*np.power(float(m),-k)
    row = {'n':n, 'n2q':n*n*q}
    for r in (0.5,1,2,3):
        mu = float(np.dot(p,k**r))
        row[f'n2moment_{r}'] = n*n*mu
        row[f'conditional_moment_{r}'] = mu/q
    row['conditional_TV'] = float(np.abs(cond-pi).sum()/2)
    s = (1+m)/2
    row['conditional_exp_s'] = float(np.dot(a[1:]/q, np.power(s/m,k)))
    row['critical_defect_capped'] = float(np.dot((m-1)*k-1,a[1:])-(1-q))
    for i in range(1,11):
        row[f'conditional_p{i}'] = float(cond[i-1])
    return row

def run(m,b,cap,steps):
    a = np.zeros(cap+2)
    pb = 1/(1+((m-1)*b-1)*m**b)
    a[b] = m**b*pb
    degree = b
    rows = []
    neg = 0
    start=time.monotonic()
    for n in range(steps+1):
        if n in (1,2,5,10,20,50,100,200,500,1000,2000,3000):
            rows.append(stats(a,m,n))
        if n == steps: break
        a,degree,err = evolve(a,m,cap,degree)
        neg += err
    name=f'm{m}_b{b}_K{cap}'
    with (ROOT/'data'/f'{name}.csv').open('w') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
    meta=dict(m=m,b=b,cap=cap,steps=steps,p_b=pb,seconds=time.monotonic()-start,
              nice=os.getpriority(os.PRIO_PROCESS,0),fft_workers=1,
              peak_rss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
              clipped_tilted_mass_accumulated=neg,final=rows[-1])
    (ROOT/'data'/f'{name}.json').write_text(json.dumps(meta,indent=2))
    print(name,json.dumps(meta),flush=True)

if __name__ == '__main__':
    assert os.getpriority(os.PRIO_PROCESS,0)>=10
    for cap in (8192,16384):
        for m,b in ((2,2),(2,4),(3,1),(3,2)):
            run(m,b,cap,3000)
