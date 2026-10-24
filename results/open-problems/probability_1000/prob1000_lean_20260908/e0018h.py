"""Optimiser v3: humps must rise above BOTH limits.  F = max(G(r_min), G(r_max)) stands in for max(G(0+), G(inf)).
S = max_{i<j<k} [ min(G_i, G_k) - max(G_j, F) ]  (>0 iff a Hurwitz-compatible level cuts two intervals);
objective = S + 0.3*min(max(G) - F, 0.1).  Parametrisation as in e0018g.mats."""
import numpy as np, json, time
from scipy.optimize import minimize
from e0018 import G_of_r
from e0018g import mats
rs = np.geomspace(1e-3, 1e3, 25)
def Sscore(G):
    F = max(G[0], G[-1]); n=len(G); best=-1e9
    for i in range(1,n-1):
        for k in range(i+2,n-1):
            j=i+1+np.argmin(G[i+1:k]); s=min(G[i],G[k])-max(G[j],F)
            if s>best: best=s
    return best, F
def Gcurve(x,N=300):
    B0,B1 = mats(x); return np.array([G_of_r(B0,B1,r,N) for r in rs])
def obj(x):
    if abs(x[0])>5: return 1.0
    G = Gcurve(x); S,F = Sscore(G); return -(S + 0.3*min(G.max()-F, 0.1))
if __name__ == "__main__":
    rng = np.random.default_rng(1820)
    seeds = [np.array([0.0, 1.0, -1.0, np.pi]), np.array([0.0, 1.05, -1.05, np.pi]), np.array([0.0, 0.95, -0.95, np.pi]),
             np.array([1.5, 1.0, -1.0, np.pi]), np.array([-1.5, 1.0, -1.0, np.pi]), np.array([0.0, 1.0, -1.0, 2.5])]
    for _ in range(24):
        seeds.append(np.array([rng.uniform(-3,3), rng.uniform(-1.5,1.5), rng.uniform(-1.5,1.5), rng.uniform(0,2*np.pi)]))
    t0=time.time(); out=[]
    for si,s in enumerate(seeds):
        res = minimize(obj, s, method='Nelder-Mead', options={'maxfev':150,'xatol':1e-3,'fatol':1e-6})
        G = Gcurve(res.x); S,F = Sscore(G); B0,B1 = mats(res.x)
        out.append((float(S), res.x.tolist(), B0.tolist(), B1.tolist(), G.round(4).tolist()))
        print(f"seed {si:2d}: S={S:+.5f} F={F:.3f} maxG={G.max():.3f} x={np.round(res.x,3).tolist()} t={time.time()-t0:.0f}s", flush=True)
        if S > -0.01: print("   G:", " ".join(f"{g:.3f}" for g in G), flush=True)
    out.sort(key=lambda t:-t[0]); json.dump(out, open("e0018h_out.json","w",encoding="utf-8"))
    print("BEST S:", out[0][0], "x=", out[0][1])
