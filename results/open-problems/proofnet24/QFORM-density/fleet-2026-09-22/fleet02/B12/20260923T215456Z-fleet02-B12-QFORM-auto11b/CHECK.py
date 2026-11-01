import math
import numpy as np

rng=np.random.default_rng(20260923215457)

def sv(M):
    return np.linalg.svd(M,compute_uv=False)

viol=0
min_margin=float('inf')
admissible=0
for trial in range(30000):
    m=int(rng.integers(3,10)); p=int(rng.integers(2,13))
    Q,_=np.linalg.qr(rng.normal(size=(m,m)))
    lam=float(rng.uniform(1.0,8.0))*(-1 if rng.integers(0,2) else 1)
    b0=float(rng.uniform(0.0,abs(lam)/(2.2*m)))
    eigs=np.empty(m); eigs[0]=lam
    rem=rng.uniform(-b0,b0,size=m-1)
    rem[0]=b0*(-1 if rng.integers(0,2) else 1)
    eigs[1:]=rem
    C=Q@np.diag(eigs)@Q.T
    B=rng.normal(size=(m,p))*10**rng.uniform(-2,3)
    ev,U=np.linalg.eigh(C); q=int(np.argmax(np.abs(ev))); u=U[:,q]
    abses=np.sort(np.abs(ev))[::-1]; c=float(abses[0]); b=float(abses[1])
    alpha=c/m-b
    if alpha<=1e-12: continue
    i=int(np.argmax(np.abs(u))); K=[k for k in range(m) if k!=i]
    a=C[i,i]; r=C[K,i]
    Bsharp=B[K,:]-np.outer(r/a,B[i,:])
    g=float(sv(np.concatenate([C,B],axis=1))[2])
    h=float(np.linalg.norm(B[i,:]))
    eta=(1+math.sqrt(m-1))*b/alpha
    rhs=g-b-eta*h
    s2=float(sv(Bsharp)[1])
    margin=s2-rhs
    min_margin=min(min_margin,margin)
    admissible+=1
    if margin < -1e-8:
        viol+=1
        break

# exact rank-one stress with cross norms up to 1e6
exact_viol=0
exact_min=float('inf')
for trial in range(10000):
    m=int(rng.integers(3,9)); p=int(rng.integers(2,12))
    u=rng.normal(size=m); u/=np.linalg.norm(u)
    lam=float(rng.uniform(1,5))*(-1 if rng.integers(0,2) else 1)
    C=lam*np.outer(u,u)
    B=rng.normal(size=(m,p))*10**rng.uniform(-2,6)
    i=int(np.argmax(np.abs(u))); K=[k for k in range(m) if k!=i]
    a=C[i,i]; r=C[K,i]
    Bsharp=B[K,:]-np.outer(r/a,B[i,:])
    g=float(sv(np.concatenate([C,B],axis=1))[2])
    s2=float(sv(Bsharp)[1])
    exact_min=min(exact_min,s2-g)
    if s2+1e-7*max(1,g)<g:
        exact_viol+=1
        break

# explicit dense-tail corollary constants
m=3; delta=0.01; c0=2.0
Bop=2*math.sqrt(2)
g0=math.sqrt(6-math.sqrt(20))
alpha=(c0-delta)/m-delta
eta=(1+math.sqrt(m-1))*delta/alpha
Delta=g0-2*delta-eta*(Bop+delta)
density=2**(11/4)/math.sqrt(alpha*Delta)
d5=5*math.sqrt(2*math.e)/(2-delta)

print({
  'random_admissible':admissible,
  'random_violations':viol,
  'random_min_margin':min_margin,
  'exact_rank1_trials':10000,
  'exact_rank1_violations':exact_viol,
  'exact_rank1_min_margin':exact_min,
  'stress_g0':g0,
  'stress_alpha':alpha,
  'stress_Delta':Delta,
  'stress_density_bound':density,
  'D5_sibling_bound':d5,
})
