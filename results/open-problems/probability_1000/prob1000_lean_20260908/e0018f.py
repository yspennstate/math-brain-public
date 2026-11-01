"""Optimiser v2.  Parametrise the traceless pair in the phi = 2 theta picture:
   f_i(phi) = rho_i + R_i cos(phi - psi_i),  growth g_i = -f_i'(phi) = R_i sin(phi - psi_i).
   |rho|<R hyperbolic (gap sqrt(R^2-rho^2)), |rho|>R elliptic, |rho|=R nilpotent.  R_0 = 1, psi_0 = 0.
   x = (log R_1, k_0 = rho_0/R_0, k_1 = rho_1/R_1, psi_1).  Objective: D + 0.3*min(maxG, 0.1), D = non-unimodality."""
import numpy as np, json, time
from scipy.optimize import minimize
from e0018 import G_of_r
rs = np.geomspace(1e-3, 1e3, 25)
def mats(x):
    u1,k0,k1,psi = x
    R0, R1 = 1.0, float(np.exp(np.clip(u1,-5,5)))
    def B(R,k,ps):
        rho = k*R; s = R*np.cos(ps); d = -R*np.sin(ps)     # s=(b+c)/2, rho=(c-b)/2 -> b = s-rho, c = s+rho
        return np.array([[d, s-rho],[s+rho, -d]])
    return B(R0,k0,0.0), B(R1,k1,psi)
def Dscore(G):
    n=len(G); best=-1e9
    for i in range(n):
        for k in range(i+2,n):
            j=i+1+np.argmin(G[i+1:k]); s=min(G[i],G[k])-G[j]
            if s>best: best=s
    return best
def Gcurve(x,N=300):
    B0,B1 = mats(x); return np.array([G_of_r(B0,B1,r,N) for r in rs])
def obj(x):
    G = Gcurve(x); return -(Dscore(G) + 0.3*min(G.max(),0.1))
rng = np.random.default_rng(1819)
seeds = [np.array([0.0, 1.0, -1.0, np.pi])]        # the survey pair: rho0=R0 (nilpotent), rho1=-R1, crossed
for _ in range(29):
    seeds.append(np.array([rng.uniform(-3,3), rng.uniform(-1.5,1.5), rng.uniform(-1.5,1.5), rng.uniform(0,2*np.pi)]))
t0=time.time(); out=[]
for si,s in enumerate(seeds):
    res = minimize(obj, s, method='Nelder-Mead', options={'maxfev':150,'xatol':1e-3,'fatol':1e-6})
    G = Gcurve(res.x); D = Dscore(G); B0,B1 = mats(res.x)
    out.append((float(D), res.x.tolist(), B0.tolist(), B1.tolist(), G.round(4).tolist()))
    print(f"seed {si:2d}: D={D:+.5f} maxG={G.max():.3f} x={np.round(res.x,3).tolist()} t={time.time()-t0:.0f}s", flush=True)
    if D > 1e-3: print("   G:", " ".join(f"{g:.3f}" for g in G), flush=True)
out.sort(key=lambda t:-t[0]); json.dump(out, open("e0018f_out.json","w",encoding="utf-8"))
print("BEST D:", out[0][0], "x=", out[0][1])
