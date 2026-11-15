#!/usr/bin/env python3
"""Independent binary64 diagnostics; deliberately not a rounding certificate."""
import os
for key in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):
    os.environ[key]='1'
import argparse,csv,json,math,time,resource
from pathlib import Path
import numpy as np
from scipy.fft import rfft,irfft,next_fast_len
import mpmath as mp

def run(law,N):
    try:os.nice(15)
    except OSError:pass
    start=time.monotonic(); K=N+128;L=next_fast_len(2*K+1,real=True)
    state=np.zeros(K+1)
    if law=='two2':state[2]=.8
    elif law=='power3':
        mp.mp.dps=80
        c=1/(mp.zeta(2)-mp.zeta(3)+mp.polylog(3,mp.mpf(1)/2))
        state[1:]=float(c)*np.arange(1,K+1,dtype=float)**(-3.)
    else:raise ValueError(law)
    wt=np.exp(-math.log(2)*np.arange(1,1071));rows=[];clip=0.
    for n in range(N+1):
        survival=float(np.dot(state[1:1071],wt))
        if n<=10 or n%50==0:
            rows.append(dict(n=n,n2q=n*n*survival,clip_mass=clip))
        if n==N:break
        pzero=1-survival
        transformed=rfft(state,n=L,workers=1)
        square=irfft(transformed*transformed,n=L,workers=1)
        nxt=square[2:K+2]*.5
        nxt[:-1]+=pzero*state[2:]
        clip-=float(nxt[nxt<0].sum())
        np.maximum(nxt,0,out=nxt)
        state[1:]=nxt
        if (n+1)%10000==0:print(law,n+1,'seconds',round(time.monotonic()-start,2),flush=True)
    out=Path('audit_results')/f'fft_long_{law}_N{N}'
    with out.with_suffix('.csv').open('w') as f:
        w=csv.DictWriter(f,fieldnames=rows[0].keys());w.writeheader();w.writerows(rows)
    info=dict(law=law,N=N,K=K,fft_length=L,threads=1,
              seconds=time.monotonic()-start,
              peak_rss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
              rounding_certified=False,final=rows[-1])
    out.with_suffix('.json').write_text(json.dumps(info,indent=2)+'\n')
    print(json.dumps(info),flush=True)

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--law');p.add_argument('--N',type=int,default=100000)
    a=p.parse_args();run(a.law,a.N)
