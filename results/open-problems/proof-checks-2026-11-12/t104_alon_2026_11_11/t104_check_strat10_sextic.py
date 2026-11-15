import numpy as np
from scipy.optimize import minimize
rng=np.random.default_rng(7)
def proj(x):
    x=x-x.mean(); return x/np.linalg.norm(x)
def f(x):
    u=proj(x); return (u**3).sum()**2-3*(u**4).sum()+1.5
best=(9,None)
X=rng.standard_normal((400000,5)); X-=X.mean(1,keepdims=True); X/=np.linalg.norm(X,axis=1,keepdims=True)
v=(X**3).sum(1)**2-3*(X**4).sum(1)+1.5
print("random min",v.min())
for i in np.argsort(v)[:40]:
    r=minimize(f,X[i],method="Nelder-Mead",options=dict(xatol=1e-13,fatol=1e-15,maxiter=20000))
    if r.fun<best[0]: best=(r.fun,proj(r.x))
print("local min",best[0]); print("at",np.round(np.sort(best[1]),6))
