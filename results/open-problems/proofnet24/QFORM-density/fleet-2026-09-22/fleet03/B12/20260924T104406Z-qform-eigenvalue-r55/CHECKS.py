import json, math
import numpy as np

SEED=20260924104406
rng=np.random.default_rng(SEED)
alpha=213/2500
m=47
tau=1/512
delta=0.5-alpha-math.sqrt(2*alpha)
sigma=delta-tau
beta=(m*alpha-4)/(m-4)
K3=3*2**(4/3)*math.e**(1/3)
C_heavy=math.sqrt(24*math.pi*m+K3**2)/(tau*math.sqrt(beta))
C_light=27*math.sqrt(math.e)/(2*sigma)

# Check the downstream singular-value mechanism used after the MSS partition.
# This does not numerically certify MSS; MSS is a published theorem used analytically.
viol=0
min_margin=float('inf')
min_theta=float('inf')
for _ in range(10000):
    h=int(rng.integers(0,8))
    q=2*h
    d=5+q+int(rng.integers(0,5))
    sC=np.sort(1+rng.random(d))[::-1]
    C=np.diag(sC)
    valsL=delta+(0.95-delta)*rng.random(d)
    valsR=delta+(0.95-delta)*rng.random(d)
    L=np.diag(np.sqrt(valsL)); R=np.diag(np.sqrt(valsR))
    G=L@C@R
    if q:
        X=rng.normal(size=(d,q)); Y=rng.normal(size=(q,d))
        F=(10**rng.uniform(-2,4))*X@Y
    else:
        F=np.zeros((d,d))
    BH=G+F
    T=rng.normal(size=(d,d))
    op=np.linalg.svd(T,compute_uv=False)[0]
    T*=rng.random()*tau/op
    B=BH+T
    ss=np.linalg.svd(B,compute_uv=False)
    margin=float(ss[4]-sigma)
    min_margin=min(min_margin,margin)
    if margin < -1e-9:
        viol+=1
    gamma=sigma/3
    theta=float(np.sum(ss**2/(gamma**2+ss**2)))
    min_theta=min(min_theta,theta)

# Check the elementary positive-contraction trace implication in the heavy branch.
heavy_viol=0
min_heavy_margin=float('inf')
for _ in range(10000):
    vals=np.sort(rng.random(m))[::-1]
    tr=float(vals.sum())
    if tr <= m*alpha:
        vals += min(1-vals.max(), (m*alpha-tr+1e-3)/m)
        vals=np.clip(vals,0,1)
    if vals.sum() <= m*alpha:
        continue
    margin=float(vals[4]-beta)
    min_heavy_margin=min(min_heavy_margin,margin)
    if margin < -1e-12:
        heavy_viol+=1

out={
  'seed':SEED,
  'constants':{
    'alpha':alpha,'m':m,'tau':tau,'delta':delta,'sigma':sigma,
    'heavy_beta':beta,'heavy_density_bound':C_heavy,
    'light_density_bound':C_light,
    'universal_189_large_eigenvalue_bound':max(C_heavy,C_light)
  },
  'light_downstream_randomized':{
    'trials':10000,'violations':viol,'minimum_s5_minus_sigma':min_margin,
    'minimum_ridge_theta_at_gamma_sigma_over_3':min_theta
  },
  'heavy_trace_randomized':{
    'trials':10000,'violations':heavy_viol,'minimum_lambda5_minus_beta':min_heavy_margin
  },
  'status':'SANITY_CHECK_ONLY_ANALYTIC_PROOF_IN_REPORT'
}
print(json.dumps(out,indent=2,sort_keys=True))
