"""E0105 / E0104 (mobile Boolean survey, Open problems 3 and 2, inertial case).
Particles: homogeneous Poisson(lam) in R^d, each carries a ball of radius r and moves x + t v, v i.i.d.
K = r0 B (ball at the origin), a = a fixed point.  S_K, S_a = detection times.  tau = S_K on {S_K < S_a}, +inf otherwise.
Joint survival: P(S_K > t, S_a > s) = exp(-lam E_v Vol(C_R(t;v) U C_r^a(s;v))), where C_R(t;v) is the capsule of radius
R = r0 + r around the segment [0, -t v] and C_r^a(s;v) the capsule of radius r around [a, a - s v] (same direction).
The union volume is V1 + V2 - I with I = int over the axial coordinate z of the (d-1)-lens of the two cross-sections.
Validation: simulate the particle system directly."""
import numpy as np
from math import pi, sqrt, acos
rng = np.random.default_rng(105)
d = 2; lam = 0.3; r = 0.5; r0 = 1.0; R = r0 + r; a = np.array([3.0, 0.0]); c = 1.0     # constant speed, isotropic direction
w = {1: 2.0, 2: pi, 3: 4*pi/3}                                                        # unit-ball volumes omega_k
def lens(rho1, rho2, h, k):
    """(k)-dimensional volume of B(0,rho1) cap B(h e, rho2), k in {1,2}."""
    if rho1 <= 0 or rho2 <= 0: return 0.0
    if h >= rho1 + rho2: return 0.0
    if h <= abs(rho1 - rho2): return w[k]*min(rho1, rho2)**k
    if k == 1: return min(rho1, h+rho2) - max(-rho1, h-rho2)
    # circular lens
    x = (h*h + rho1*rho1 - rho2*rho2)/(2*h)
    y = (h*h + rho2*rho2 - rho1*rho1)/(2*h)
    return rho1*rho1*acos(x/rho1) - x*sqrt(max(rho1*rho1-x*x,0)) + rho2*rho2*acos(y/rho2) - y*sqrt(max(rho2*rho2-y*y,0))
def union_vol(t, s, apar, h, nz=600):
    """Vol of capsule(R, [0,tc]) U capsule(r, [apar, apar+sc]) with perpendicular offset h; axial coordinate z."""
    V1 = w[d]*R**d + w[d-1]*R**(d-1)*t*c
    V2 = w[d]*r**d + w[d-1]*r**(d-1)*s*c
    zlo = max(-R, apar - r); zhi = min(t*c + R, apar + s*c + r)
    if zlo >= zhi: return V1 + V2
    zs = np.linspace(zlo, zhi, nz); dz = zs[1]-zs[0]; I = 0.0
    for z in zs:
        d1 = 0.0 if 0 <= z <= t*c else min(abs(z), abs(z - t*c))
        d2 = 0.0 if apar <= z <= apar + s*c else min(abs(z - apar), abs(z - apar - s*c))
        rho1 = sqrt(max(R*R - d1*d1, 0)); rho2 = sqrt(max(r*r - d2*d2, 0))
        I += lens(rho1, rho2, h, d-1)
    return V1 + V2 - I*dz
phis = np.linspace(0, 2*pi, 64, endpoint=False) + pi/64
def Lam(t, s):
    """lam * E_v Vol(union); direction e = -v/|v| uniform: a_par = a.e, h = |a - (a.e)e|."""
    tot = 0.0
    for ph in phis:
        e = np.array([np.cos(ph), np.sin(ph)]); apar = a@e; h = np.linalg.norm(a - apar*e)
        tot += union_vol(t, s, apar, h)
    return lam*tot/len(phis)
def P_tau_le(t, n=60):
    """P(tau <= t) = int_0^t -d/dt' P(S_K > t', S_a > s)|_{s=t'} dt'  (numerical derivative)."""
    us = np.linspace(0, t, n+1); eps = 1e-3; acc = 0.0
    vals = []
    for u in us:
        L0 = Lam(u, u); L1 = Lam(u+eps, u); dens = (L1 - L0)/eps * np.exp(-L0); vals.append(dens)
    return np.trapezoid(vals, us)
# ---- Monte Carlo of the particle system ----
def simulate(nrep=20000, Tmax=12.0):
    box = R + c*Tmax + 0.5 + np.linalg.norm(a)
    out_SK = np.empty(nrep); out_Sa = np.empty(nrep)
    for k in range(nrep):
        n = rng.poisson(lam*pi*box*box)
        rad = box*np.sqrt(rng.random(n)); ang = rng.uniform(0, 2*pi, n)
        x = np.c_[rad*np.cos(ang), rad*np.sin(ang)]
        vang = rng.uniform(0, 2*pi, n); v = c*np.c_[np.cos(vang), np.sin(vang)]
        def first_hit(center, rho):
            y = x - center; b = (y*v).sum(1); cc = (y*y).sum(1) - rho*rho; disc = b*b - cc*(v*v).sum(1)
            t = np.full(n, np.inf); ok = disc >= 0
            tt = (-b[ok] - np.sqrt(disc[ok]))/ (v[ok]*v[ok]).sum(1)
            inside = cc[ok] <= 0
            tt = np.where(inside, 0.0, tt); tt = np.where(tt < 0, np.inf, tt); t[ok] = tt
            return t.min() if n else np.inf
        out_SK[k] = first_hit(np.zeros(2), R); out_Sa[k] = first_hit(a, r)
    return out_SK, out_Sa
if __name__ == "__main__":
    print(f"d={d} lam={lam} r={r} r0={r0} (R={R}) a={a.tolist()} speed c={c} isotropic")
    print("formula  P(S_K > t):        ", [round(float(np.exp(-lam*(w[d]*R**d + w[d-1]*R**(d-1)*t*c))),4) for t in (1,3,6)])
    print("formula  P(S_K > t, S_a > t):", [round(float(np.exp(-Lam(t,t))),4) for t in (1,3,6)])
    pt = {t: P_tau_le(t) for t in (1,3,6,12)}
    print("formula  P(tau <= t):        ", {t: round(v,4) for t,v in pt.items()}, " -> P(S_K < S_a) ~", round(P_tau_le(40, n=200),4))
    SK, Sa = simulate()
    print("MC       P(S_K > t):        ", [round(float((SK>t).mean()),4) for t in (1,3,6)])
    print("MC       P(S_K > t, S_a > t):", [round(float(((SK>t)&(Sa>t)).mean()),4) for t in (1,3,6)])
    print("MC       P(tau <= t):        ", {t: round(float(((SK<=t)&(SK<Sa)).mean()),4) for t in (1,3,6,12)}, " P(S_K < S_a) =", round(float((SK<Sa).mean()),4), "+-", round(float(np.sqrt((SK<Sa).mean()*(1-(SK<Sa).mean())/len(SK))),4))
