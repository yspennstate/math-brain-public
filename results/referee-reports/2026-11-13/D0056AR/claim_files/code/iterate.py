#!/usr/bin/env python3
"""Single-threaded exponentially tilted FFT iteration of the DR recursion.

No criticality projection. Deleted tail mass is transferred to zero. FFT padding
prevents cyclic aliasing. See REPORT.md for the exact-arithmetic coupling bound.
"""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):
    os.environ[key]='1'
import argparse, csv, json, math, resource, time
from pathlib import Path
import numpy as np
from scipy.fft import rfft, irfft, next_fast_len
import mpmath as mp

def initial(m, law, K):
    mp.mp.dps=70
    k=np.arange(K+1,dtype=float); a=np.zeros(K+1)
    if law.startswith('two'):
        h=int(law[3:]); p=1/(1+((m-1)*h-1)*mp.mpf(m)**h)
        a[h]=float(p*mp.mpf(m)**h); q=float(p)
        info={'type':'two-point','k':h,'p':str(p)}
    elif law=='geom':
        r=mp.mpf(1)/(2*m); t=m*r
        A=(m-1)*t/(1-t)**2-t/(1-t)
        c=1/(A+r/(1-r)); q=float(c*r/(1-r))
        a[1:]=float(c)*np.exp(k[1:]*math.log(float(t)))
        info={'type':'geometric','r':str(r),'c':str(c)}
    elif law=='sparse':
        A=(m-1)*mp.zeta(2)-mp.polylog(2,mp.mpf(1)/2)
        T=sum(mp.mpf(m)**(-(2**j))/(j*j*2**j) for j in range(1,21))
        c=1/(A+T);q=float(c*T)
        for j in range(1,K.bit_length()):
            h=2**j
            if h<=K:a[h]=float(c/(j*j*h))
        info={'type':'sparse','c':str(c),'p0':str(c*A),'tail_formula':'c*m^(-2^j)/(j^2*2^j)'}
    elif law.startswith('power'):
        b=mp.mpf(law[5:]); L=mp.polylog(b,mp.mpf(1)/m)
        A=(m-1)*mp.zeta(b-1)-mp.zeta(b); c=1/(A+L)
        a[1:]=float(c)*k[1:]**(-float(b)); q=float(c*L)
        info={'type':'power','b':str(b),'c':str(c),'p0':str(c*A)}
    else: raise ValueError(law)
    return a,q,info

def run(m,law,N,K,out):
    start=time.time(); a,qexact,info=initial(m,law,K)
    L=next_fast_len(m*K+1,real=True)
    # q is formed from positive masses, avoiding cancellation in 1-p0.
    T=min(K,1070); weights=np.exp(-math.log(m)*np.arange(1,T+1))
    rows=[]; clip_total=0.; log_product=0.
    def record(n,q):
        rows.append(dict(n=n,q=q,n2q=n*n*q,tilted_positive_mass=float(a.sum()),
                         tilted_first=float(np.dot(np.arange(K+1),a)),
                         log_product_truncated=log_product,clip_l1_total=clip_total))
    q=float(np.dot(a[1:T+1],weights)); record(0,q)
    for n in range(1,N+1):
        p0=1-q
        log_product+=(m-1)*math.log(p0+float(a.sum()))
        F=rfft(a,n=L,workers=1)
        if m==2:
            F=F*F
        elif m==3:
            F=F*F*(3*p0+F)
        else:
            # Sum the nonlinear terms without subtracting the O(1) pedestal.
            base=F; F=np.zeros_like(base)
            for j in range(2,m+1): F+=math.comb(m,j)*p0**(m-j)*base**j
        nonlinear=irfft(F,n=L,workers=1)[2:K+2]/m
        nonlinear[:-1]+=p0**(m-1)*a[2:]
        neg=nonlinear<0
        clip_total+=float(-nonlinear[neg].sum())
        np.maximum(nonlinear,0,out=nonlinear)
        a[0]=0; a[1:]=nonlinear
        q=float(np.dot(a[1:T+1],weights))
        if not math.isfinite(q) or q>1: raise ArithmeticError((n,q))
        if n<=10 or n%50==0 or n==N or n&(n+1)==0: record(n,q)
        if n%2000==0: print(f'm={m} {law} K={K} n={n} n2q={n*n*q:.10g}',flush=True)
    out=Path(out);out.parent.mkdir(exist_ok=True)
    with out.open('w') as f:
        w=csv.DictWriter(f,fieldnames=rows[0]);w.writeheader();w.writerows(rows)
    meta={'m':m,'law':law,'N':N,'K':K,'fft_length':L,'initial':info,
          'initial_q_exact':qexact,'seconds':time.time()-start,
          'peak_rss_bytes':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
          'float_epsilon':float(np.finfo(float).eps),'threads':1,
          'truncation_log10_bound':float(math.log10(m)/(m-1)-(K+1)*math.log10(m)+(N+1)*math.log10(m)-math.log10(m-1))}
    out.with_suffix('.json').write_text(json.dumps(meta,indent=2)+'\n')
    print(json.dumps(meta),flush=True)

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--m',type=int,required=True)
    p.add_argument('--law',required=True);p.add_argument('--N',type=int,default=10000)
    p.add_argument('--K',type=int);p.add_argument('--out',required=True);a=p.parse_args()
    if os.getpriority(os.PRIO_PROCESS,0)<10:
        os.nice(10)
    run(a.m,a.law,a.N,a.K or a.N+128,a.out)
