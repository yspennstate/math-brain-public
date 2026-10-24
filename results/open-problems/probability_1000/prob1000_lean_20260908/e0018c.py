"""Random search for a traceless pair (B0,B1) whose exponent G(r) has TWO humps with a dip, so that a level
abar (Hurwitz-compatible: abar > G(0+) = (lam0+lam1)/2 and abar > G(inf)) cuts the instability set into two intervals."""
import numpy as np, sys, time, json
from e0018 import G_of_r
rng = np.random.default_rng(18)
rs = np.geomspace(0.02, 60, 32)
def lam_top(B):
    d,b,c = B[0,0],B[0,1],B[1,0]; q = d*d+b*c
    return np.sqrt(q) if q>0 else 0.0
def score_pair(B0,B1,N=400):
    G = np.array([G_of_r(B0,B1,r,N) for r in rs])
    G0 = 0.5*(lam_top(B0)+lam_top(B1)); Ginf = lam_top(0.5*(B0+B1))
    # best two-hump split: r1<r2<r3 maximizing min(G1,G3) - max(G2,G0,Ginf)
    best = -1e9; arg=None
    n=len(rs)
    for i in range(n):
        for k in range(i+2,n):
            j = i+1+np.argmin(G[i+1:k])
            s = min(G[i],G[k]) - max(G[j],G0,Ginf)
            if s>best: best=s; arg=(i,j,k)
    return best, G, arg, G0, Ginf
def rand_B():
    kind = rng.integers(4)
    if kind==0:   # generic
        d,b,c = rng.normal(size=3)
    elif kind==1: # rotation-like
        w = rng.uniform(0.2,3); d = rng.normal()*0.3; b = w; c = -w - d*d/w*0  # ensure d^2+bc<0 roughly
        c = -(d*d + rng.uniform(0.1,4))/b
    elif kind==2: # hyperbolic
        l = rng.uniform(0.1,2); th = rng.uniform(0,np.pi)
        R = np.array([[np.cos(th),-np.sin(th)],[np.sin(th),np.cos(th)]])
        return R@np.diag([l,-l])@R.T
    else:         # nilpotent-ish shear rotated
        s = rng.uniform(0.2,3); th = rng.uniform(0,np.pi)
        R = np.array([[np.cos(th),-np.sin(th)],[np.sin(th),np.cos(th)]])
        return R@np.array([[0,s],[0,0]])@R.T
    return np.array([[d,b],[c,-d]])
t0=time.time(); results=[]
for it in range(1500):
    B0, B1 = rand_B(), rand_B()
    sc = 1.0/max(np.abs(B0).max(), np.abs(B1).max()); B0=B0*sc; B1=B1*sc   # scale so entries O(1)
    s, G, arg, G0, Ginf = score_pair(B0,B1)
    results.append((s, B0.tolist(), B1.tolist(), G.round(4).tolist(), arg, G0, Ginf))
    if it % 100 == 0:
        results.sort(key=lambda x:-x[0]); print(f"it {it} t={time.time()-t0:.0f}s best score so far {results[0][0]:+.4f}", flush=True)
results.sort(key=lambda x:-x[0])
json.dump(results[:40], open("e0018c_top.json","w"))
for s,B0,B1,G,arg,G0,Ginf in results[:6]:
    print(f"score {s:+.4f}  G0={G0:.3f} Ginf={Ginf:.3f} arg={arg}\n  B0={np.round(B0,3).tolist()} B1={np.round(B1,3).tolist()}\n  G={G}")
