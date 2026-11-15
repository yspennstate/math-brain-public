"""A second urn implementation and RNG: exact embedded chain, vectorized replicas.

No exponential waiting times: run a deterministic number of individual rings.
The exact identity E M_k^2 = E [M]_k is the finite-horizon reference.
This is a diagnostic for the low L=400 C-simulator sample variance.
"""
import time
import math
import numpy as np

start=time.monotonic()
rng=np.random.default_rng(449318394)
for L,R,steps in [(4,10000,4000),(400,10000,40000)]:
    n=np.ones((R,L),dtype=np.uint32)
    rows=np.arange(R)
    M=np.zeros(R);optional=np.zeros(R)
    for k in range(steps):
        v=rng.integers(L,size=R)
        left=(v+L-1)%L
        a=n[rows,left];b=n[rows,v]
        e=np.where(rng.random(R)*(a+b)<a,left,v)
        old=n[rows,e].astype(float)
        M+=np.where(e%2==0,1.,-1.)/old
        optional+=1./(old*old)
        n[rows,e]+=1
        if k%100==0 and time.monotonic()-start>220:
            break
    Z=M/math.sqrt(L)
    var=Z.var(ddof=1)
    se=np.sqrt(np.mean((Z-Z.mean())**4)-var*var)/math.sqrt(R)
    print(f'L={L}, R={R}, rings/rep={k+1}, elapsed={time.monotonic()-start:.3f}s',flush=True)
    print(f'  Var(M/sqrt(L))={var:.8f} +/- {se:.8f}; '
          f'E optional/L={optional.mean()/L:.8f}; '
          f'estimated future variance={math.pi**2/6-optional.mean()/L:.8f}; '
          f'mean Z={Z.mean():.8f} +/- {Z.std(ddof=1)/math.sqrt(R):.8f}',flush=True)
