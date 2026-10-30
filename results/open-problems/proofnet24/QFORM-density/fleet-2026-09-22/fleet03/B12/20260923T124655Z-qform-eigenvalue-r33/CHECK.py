import json, math
import numpy as np

rng=np.random.default_rng(20260923)
N=10000
min_rank_margin=float('inf')
max_beta_minus_delta=-float('inf')
min_theta_margin=float('inf')
violations=0

for _ in range(N):
    r=int(rng.integers(0,4))
    k=int(rng.integers(5,9))
    p=int(rng.integers(r+k,r+k+8))
    q=int(rng.integers(r+k,r+k+8))
    m=min(p,q)
    a=float(rng.uniform(0.5,3.0))
    delta=float(rng.uniform(0.0,0.9*a))

    U,_=np.linalg.qr(rng.normal(size=(p,m)))
    V,_=np.linalg.qr(rng.normal(size=(q,m)))
    sv=np.sort(rng.uniform(a,4*a,size=m))[::-1]
    B0=U@np.diag(sv)@V.T

    if r:
        Ur,_=np.linalg.qr(rng.normal(size=(p,r)))
        Vr,_=np.linalg.qr(rng.normal(size=(q,r)))
        huge=np.diag(rng.uniform(1.0,1000.0,size=r)*rng.choice([-1,1],size=r))
        Er=Ur@huge@Vr.T
    else:
        Er=np.zeros((p,q))

    Uf,_=np.linalg.qr(rng.normal(size=(p,m)))
    Vf,_=np.linalg.qr(rng.normal(size=(q,m)))
    fs=rng.uniform(0.0,delta,size=m)
    fs[0]=delta
    F=Uf@np.diag(fs)@Vf.T
    E=Er+F
    B=B0+E

    s0=np.linalg.svd(B0,compute_uv=False)
    sE=np.linalg.svd(E,compute_uv=False)
    s=np.linalg.svd(B,compute_uv=False)
    beta=sE[r] if r<len(sE) else 0.0

    rank_margin=s[k-1]-(s0[r+k-1]-beta)
    beta_minus_delta=beta-delta

    b=a-delta
    x=math.sqrt((k-4)/12)
    gamma=b*x
    theta=float(np.sum(s*s/(gamma*gamma+s*s)))
    theta0=12*k/(k+8)
    theta_margin=theta-theta0

    min_rank_margin=min(min_rank_margin,rank_margin)
    max_beta_minus_delta=max(max_beta_minus_delta,beta_minus_delta)
    min_theta_margin=min(min_theta_margin,theta_margin)
    if rank_margin < -1e-8 or beta_minus_delta > 1e-8 or theta_margin < -1e-8:
        violations += 1

constants={}
for k in range(5,11):
    constants[str(k)]=3*k*math.sqrt(3*math.e)/(2*(k-4)**1.5)

ell2=(9-math.sqrt(17))/8
partner_gap=2*ell2-0.25
partner_density=2*math.sqrt(30*math.pi)/partner_gap

out={
  'seed':20260923,
  'trials':N,
  'violations':violations,
  'min_rank_margin':min_rank_margin,
  'max_beta_minus_delta':max_beta_minus_delta,
  'min_theta_margin':min_theta_margin,
  'C_k':constants,
  'r2_k6_delta_quarter_bound':3*math.sqrt(6*math.e),
  'partner_ell_squared':ell2,
  'partner_gap_delta_quarter':partner_gap,
  'partner_density_bound':partner_density
}
print(json.dumps(out,indent=2,sort_keys=True))
