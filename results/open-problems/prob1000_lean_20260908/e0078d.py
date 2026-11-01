"""Independent re-derivation of the Conjecture 4.2 counterexample.
Method 1: expm (as before).  Method 2: solve u' = C u, u(0)=1 by RK45 with tight tolerances, then
(pi-alpha).u(t).  Method 3: mpmath 30-digit matrix exponential at the worst t.  Also the smallest m."""
import numpy as np
from scipy.linalg import expm
from scipy.integrate import solve_ivp
def inst(m, k, L, r=1.0):
    Q = np.zeros((m,m))
    for i in range(m): Q[i,(i+1)%m] = r
    np.fill_diagonal(Q, -r)
    lam = np.zeros(m); lam[:k] = L
    pi = np.full(m, 1.0/m); ls = pi@lam; al = pi*lam/ls
    return Q - np.diag(lam), pi, al, ls
def worst_expm(m,k,L,n=400):
    C,pi,al,ls = inst(m,k,L); T=m; ts=np.linspace(T/n, 1.5*T, n); one=np.ones(m)
    v=np.array([(pi-al)@expm(C*t)@one for t in ts]); S=np.array([pi@expm(C*t)@one for t in ts])
    i=np.argmin(v/S); return ts[i], v[i], S[i], (v/S)[i]
# smallest m with a violation (k = m/2, L = 2E/m so E = kL = fixed 8)
print("smallest violating m (block m/2, per-lap exposure 8):")
for m in [8,12,16,20,24,32,48]:
    k=m//2; L=8.0/k
    t,v,S,rel = worst_expm(m,k,L)
    print(f"  m={m:3d} k={k:2d} L={L:.4f}: min rel = {rel:+.4f} at t={t:.2f} (={t/m:.2f} laps), (pi-alpha)e^Ct1={v:+.3e}")
# the m=64 instance, three ways
m,k,L = 64,32,0.25
t,v,S,rel = worst_expm(m,k,L)
print(f"\nm=64 k=32 L=0.25 expm: t*={t:.3f}, (pi-alpha)e^Ct1={v:+.6e}, S={S:.6e}, rel={rel:+.5f}")
C,pi,al,ls = inst(m,k,L)
sol = solve_ivp(lambda s,u: C@u, (0,t), np.ones(m), rtol=1e-11, atol=1e-14, method='DOP853')
u = sol.y[:,-1]
print(f"   ODE DOP853:            (pi-alpha).u(t*)={(pi-al)@u:+.6e}, S={pi@u:.6e}, rel={((pi-al)@u)/(pi@u):+.5f}")
import mpmath as mp
mp.mp.dps = 30
Cm = mp.matrix(C.tolist()); E = mp.expm(Cm*mp.mpf(t)); one = mp.matrix([1]*m)
Eu = E*one
val = sum((mp.mpf(pi[i])-mp.mpf(al[i]))*Eu[i] for i in range(m)); Sm = sum(mp.mpf(pi[i])*Eu[i] for i in range(m))
print(f"   mpmath 30 digits:      (pi-alpha)e^Ct1={mp.nstr(val,8)}, S={mp.nstr(Sm,8)}, rel={mp.nstr(val/Sm,6)}")
print(f"   lambda* = {ls}, hazard/lambda* at t* = {1-rel:.4f}")
