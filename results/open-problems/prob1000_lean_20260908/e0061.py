"""E0061: Volterra QSO on S^2, x'=x(1+ay-bz), y'=y(1-ax+cz), z'=z(1+bx-cy), a,b,c in [-1,1].
Theorem 3 (source): a,b,c same sign, none zero => Cesaro means of V^k(x) do not converge (interior x).
Problem 4: is the negation sufficient?  Probe: mixed signs / a zero, long orbits, Cesaro means at
several horizons, and the trajectory itself."""
import numpy as np
rng = np.random.default_rng(61)
def V(p, a, b, c):
    x, y, z = p
    q = np.array([x*(1+a*y-b*z), y*(1-a*x+c*z), z*(1+b*x-c*y)])
    return q / q.sum()          # sum is 1 already (skew-symmetric); renormalise against roundoff
def run(a, b, c, p0, K=300_000, checkpoints=(30_000, 100_000, 300_000)):
    p = p0.copy(); S = np.zeros(3); out = {}; traj_late = []
    for k in range(1, K+1):
        p = V(p, a, b, c); S += p
        if k in checkpoints: out[k] = S / k
        if k > K - 5: traj_late.append(p.copy())
    return out, np.array(traj_late)
cases = [("cyclic control a=b=c=1", 1,1,1), ("cyclic control 0.5,0.5,0.5", .5,.5,.5),
         ("mixed +,+,-", .7,.6,-.5), ("mixed +,-,+", .7,-.6,.5), ("mixed -,+,+", -.7,.6,.5),
         ("a=0,b,c>0", 0,.6,.5), ("a=0,b>0,c<0", 0,.6,-.5), ("a=b=0,c>0", 0,0,.5),
         ("mixed small", .1,.9,-.05), ("mixed near-cyclic a=-0.01", -.01,.8,.8), ("c=0, a,b>0", .8,.8,0)]
for name,a,b,c in cases:
    p0 = rng.dirichlet([1,1,1])
    out, late = run(a,b,c,p0)
    ks = sorted(out); m = np.array([out[k] for k in ks])
    drift = np.abs(m[-1]-m[-2]).max()
    print(f"{name:28s} p0={np.round(p0,3)}  Cesaro@{ks[-2]}={np.round(m[-2],4)} @{ks[-1]}={np.round(m[-1],4)}  |diff|={drift:.2e}  last p={np.round(late[-1],4)}")
