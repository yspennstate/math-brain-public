"""P0245 at n=6: minimise E_pi(cover time) over reversible chains (weighted graphs with loops); 21 params."""
import numpy as np, sys, time
from scipy.optimize import minimize
from p0245 import cover_time, P_from
n=6; H=sum(1.0/k for k in range(1,n)); target=(n-1)*H
Kn=(np.ones((n,n))-np.eye(n))/(n-1)
print(f"n=6: bound (n-1)H_5 = {target:.6f}; K_6 walk = {cover_time(Kn):.6f}", flush=True)
rng=np.random.default_rng(2456); best=(np.inf,None); m=n*(n+1)//2; t0=time.time()
for trial in range(16):
    x0=rng.normal(size=m)*2
    res=minimize(lambda x: cover_time(P_from(x,n)), x0, method='Nelder-Mead', options={'maxfev':700,'xatol':1e-5,'fatol':1e-8})
    if res.fun<best[0]: best=(res.fun,res.x)
    print(f"  trial {trial}: {res.fun:.6f}  (best {best[0]:.6f}, ratio {best[0]/target:.5f}) t={time.time()-t0:.0f}s", flush=True)
# polish from the complete graph itself (is it a local min?)
x0=np.zeros(m); k=0
for i in range(n):
    for j in range(i,n):
        x0[k]= -30.0 if i==j else 0.0; k+=1
res=minimize(lambda x: cover_time(P_from(x,n)), x0, method='Nelder-Mead', options={'maxfev':1500,'xatol':1e-7,'fatol':1e-10})
print(f"polish from K_6: {res.fun:.8f} vs bound {target:.8f}  (diff {res.fun-target:+.2e})")
print("argmin of random starts:\n", np.round(P_from(best[1],n),4))
