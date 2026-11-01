"""E0045 endpoint case d = p-1: Gamma_V = |g|^2 - min_i (v_i.g)^2, so the conjecture says the eigenbasis MINIMISES
E min_i Y_i^2, Y = V^T g.  Test with common random numbers, p = 3 and 4, structured rotations and random ones."""
import numpy as np
from scipy.stats import special_ortho_group
rng=np.random.default_rng(4546); N=1_500_000
def Emin(V, Z, sig):
    Y=(Z*sig)@V; return (Y**2).min(1).mean()
for p, sig in [(3,np.array([1.0,0.6,0.3])),(3,np.array([1.0,1.0,0.3])),(4,np.array([1.0,0.7,0.4,0.2])),(4,np.array([1.0,1.0,1.0,0.3]))]:
    Z=rng.standard_normal((N,p)); base=Emin(np.eye(p),Z,sig); worst=base; rec=None
    # rotations in each coordinate 2-plane by a grid of angles
    for i in range(p):
        for j in range(i+1,p):
            for t in np.linspace(0.05,np.pi/2-0.05,12):
                V=np.eye(p); c,s=np.cos(t),np.sin(t); V[i,i]=c; V[j,j]=c; V[i,j]=-s; V[j,i]=s
                v=Emin(V,Z,sig)
                if v<worst: worst=v; rec=('plane',i,j,round(t,3))
    for _ in range(60):
        V=special_ortho_group.rvs(p,random_state=rng); v=Emin(V,Z,sig)
        if v<worst: worst=v; rec=('random',np.round(V,3).tolist())
    print(f"p={p} sig={sig.tolist()}: E min at eigenbasis {base:.6f}; smallest found elsewhere {worst:.6f} (diff {worst-base:+.2e}) {rec if rec else '(none below eigenbasis)'}")
