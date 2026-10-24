"""Optimise a continuous non-unimodality measure D over traceless pairs.
D(G) = max_{i<j<k} [ min(G_i,G_k) - G_j ]  on a log grid of r: negative for unimodal, positive for two humps."""
import numpy as np, json, time, sys
from scipy.optimize import minimize
from e0018 import G_of_r
rs = np.geomspace(1e-3, 1e3, 25)
def unpack(x):
    d0,b0,c0,d1,b1,c1 = x
    return np.array([[d0,b0],[c0,-d0]]), np.array([[d1,b1],[c1,-d1]])
def Dscore(G):
    n=len(G); best=-1e9
    for i in range(n):
        for k in range(i+2,n):
            j=i+1+np.argmin(G[i+1:k]); s=min(G[i],G[k])-G[j]
            if s>best: best=s
    return best
def obj(x):
    B0,B1 = unpack(x)
    sc = max(np.abs(B0).max(), np.abs(B1).max())
    if sc < 1e-6: return 1.0
    B0, B1 = B0/sc, B1/sc
    G = np.array([G_of_r(B0,B1,r,300) for r in rs])
    return -Dscore(G)
rng = np.random.default_rng(1818)
seeds = [np.array([0,1,0, 0,0,-1.]), np.array([0,1,-0.1, 0,0.1,-1.]), np.array([0,1,-0.3, 0,0.0,-1.]),
         np.array([0.2,1,-0.5, -0.2,0.3,-1.]), np.array([0,1,0.3, 0,0,-1.])]
seeds += [rng.normal(size=6) for _ in range(9)]
t0=time.time(); out=[]
for si,s in enumerate(seeds):
    res = minimize(obj, s, method='Nelder-Mead', options={'maxfev':160,'xatol':1e-3,'fatol':1e-5,'initial_simplex':None})
    B0,B1 = unpack(res.x); sc=max(np.abs(B0).max(),np.abs(B1).max()); B0,B1=B0/sc,B1/sc
    G = np.array([G_of_r(B0,B1,r,300) for r in rs])
    out.append((-res.fun, B0.tolist(), B1.tolist(), G.round(4).tolist()))
    print(f"seed {si}: D = {-res.fun:+.5f}  t={time.time()-t0:.0f}s  B0={np.round(B0,3).tolist()} B1={np.round(B1,3).tolist()}", flush=True)
    print("   G:", " ".join(f"{g:.3f}" for g in G), flush=True)
out.sort(key=lambda t:-t[0]); json.dump(out, open("e0018e_out.json","w",encoding="utf-8"))
print("BEST D:", out[0][0])
