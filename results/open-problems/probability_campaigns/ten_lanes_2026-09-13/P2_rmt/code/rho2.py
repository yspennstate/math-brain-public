import numpy as np, sys, time
from p0016_rho_k import rho_k
print(" M   k   E[phi]    rho_k(corr)  rho_k(raw)   eps      secs")
jobs=[(6,3,None),(8,4,None),(10,5,None),(12,6,None),(6,5,None),(8,7,None),(10,9,None),
      (8,4,0.0035),(8,4,0.014)]
for (M,k,eps) in jobs:
    t0=time.time()
    m,r,rr,e = rho_k(M,k,nB=400,nG=6000,eps=eps)
    print(f"{M:3d} {k:3d}  {m:.5f}   {r:9.4f}   {rr:9.4f}   {e:.4f}  ({time.time()-t0:.0f})")
    sys.stdout.flush()
