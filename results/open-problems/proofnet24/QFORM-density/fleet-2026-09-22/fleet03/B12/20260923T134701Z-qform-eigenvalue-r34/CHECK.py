import math
import numpy as np

rng=np.random.default_rng(20260923)
viol_reserve=0
viol_theta=0
min_margin=float('inf')
N=10000
for _ in range(N):
    m=int(rng.integers(7,15)); n=int(rng.integers(7,15)); d=min(m,n)
    maxr=max(1,min(4,d-5 if d>5 else 1))
    r=int(rng.integers(0,maxr))
    B0=rng.normal(size=(m,n))
    U,_,Vt=np.linalg.svd(rng.normal(size=(m,n)),full_matrices=False)
    sv=np.zeros(d)
    if r:
        sv[:r]=10**rng.uniform(0,3,size=r)
    Ebig=(U[:,:d]*sv)@Vt[:d,:]
    F=rng.normal(size=(m,n))
    sf=np.linalg.svd(F,compute_uv=False)
    delta=float(10**rng.uniform(-2,0))
    F*=delta/sf[0]
    E=Ebig+F
    s0=np.linalg.svd(B0,compute_uv=False)
    se=np.linalg.svd(E,compute_uv=False)
    sb=np.linalg.svd(B0+E,compute_uv=False)
    beta=se[r] if r<d else 0.0
    count=min(d,d-r)
    u=np.maximum(s0[r:r+count]-beta,0)
    for j in range(count):
        margin=sb[j]-u[j]
        min_margin=min(min_margin,float(margin))
        if margin < -1e-9:
            viol_reserve+=1
            break
    if np.any(u>0):
        gamma=float(10**rng.uniform(-2,1))
        theta=float(np.sum(u*u/(gamma*gamma+u*u)))
        S=float(np.sum(u*u)); T=float(np.sum(u**4))
        lower=S*S/(gamma*gamma*S+T) if S>0 else 0.0
        if theta+1e-12 < lower:
            viol_theta+=1

u=np.array([1.,1.,1.,1.]+[.8]*6)
S=float(np.sum(u*u)); T=float(np.sum(u**4)); D=S*S-4*T
gamma_closed=math.sqrt(D/(12*S))
closed=3*math.sqrt(3*math.e)/2*S**2.5/D**1.5
# high-resolution exact-profile scan, deterministic
G=np.linspace(1e-4,1.2,250000)
TH=np.array([np.sum(u*u/(g*g+u*u)) for g in G])
mask=TH>4
V=np.full_like(G,np.inf)
V[mask]=math.sqrt(math.e)/(2*G[mask])*TH[mask]/(TH[mask]-4)
i=int(np.argmin(V))
gamma_exact=float(G[i]); bound_exact=float(V[i]); theta_exact=float(TH[i])
old=(3*10*math.sqrt(3*math.e)/(2*(10-4)**1.5))/.8
ell2=(9-math.sqrt(17))/8
gap=2*ell2-1/3
partner=2*math.sqrt(30*math.pi)/gap

print({
  'tests':N,
  'reserve_violations':viol_reserve,
  'cauchy_violations':viol_theta,
  'minimum_reserve_margin':min_margin,
  'profile_S':S,
  'profile_T':T,
  'profile_participation_ratio':S*S/T,
  'closed_gamma':gamma_closed,
  'closed_bound':closed,
  'exact_gamma_scan':gamma_exact,
  'exact_theta_scan':theta_exact,
  'exact_bound_scan':bound_exact,
  'prior_flat_k10_bound':old,
  'partner_gap':gap,
  'partner_density_bound':partner,
})
