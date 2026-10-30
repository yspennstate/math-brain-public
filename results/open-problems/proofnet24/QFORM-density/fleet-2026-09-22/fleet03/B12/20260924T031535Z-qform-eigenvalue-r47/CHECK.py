import itertools, json, math
import numpy as np

SEED=20260924031535
TRIALS=10000
rng=np.random.default_rng(SEED)
viol_profile=0
viol_e3=0
min_profile=float('inf')
min_e3_ratio=float('inf')

for _ in range(TRIALS):
    m=int(rng.integers(5,10))
    q=int(rng.integers(3,10))
    X=rng.normal(size=(m,m))
    C=(X+X.T)/2
    B=rng.normal(size=(m,q))
    G=C@C+B@B.T
    lam=np.linalg.eigvalsh(G)[::-1]
    sc=np.linalg.svd(C,compute_uv=False)
    sb=np.linalg.svd(B,compute_uv=False)
    lhs=sc[2]**2+sb[2]**2
    rhs=lam[4]
    margin=float(lhs-rhs)
    min_profile=min(min_profile,margin)
    if margin < -1e-9:
        viol_profile += 1

    sq=sb**2
    z3=0.0
    for i,j,k in itertools.combinations(range(len(sq)),3):
        z3 += sq[i]*sq[j]*sq[k]
    base=sb[2]**6
    if base>0:
        min_e3_ratio=min(min_e3_ratio,float(z3/base))
    if z3+1e-9 < base:
        viol_e3 += 1

rng2=np.random.default_rng(471103)
viol_opt=0
min_opt_slack=float('inf')
for _ in range(TRIALS):
    g=float(rng2.uniform(.1,5))
    th=float(rng2.uniform(0,math.pi/2))
    rad=g*float(rng2.uniform(1,3))
    a=rad*math.cos(th)
    b=rad*math.sin(th)
    A=float(rng2.uniform(.1,20))
    K=float(rng2.uniform(.1,20))
    lhs=min(A/a if a>1e-15 else float('inf'), K/b if b>1e-15 else float('inf'))
    rhs=math.sqrt(A*A+K*K)/g
    slack=float(rhs-lhs)
    min_opt_slack=min(min_opt_slack,slack)
    if slack < -1e-10:
        viol_opt += 1

K3=3*(2**(4/3))*math.exp(1/3)
partner_bound=(4/7)*math.sqrt(264*math.pi+K3*K3)

out={
  'seed':SEED,
  'matrix_trials':TRIALS,
  'profile_violations':viol_profile,
  'minimum_profile_margin':min_profile,
  'e3_violations':viol_e3,
  'minimum_e3_to_s3six_ratio':min_e3_ratio,
  'optimization_trials':TRIALS,
  'optimization_violations':viol_opt,
  'minimum_optimization_slack':min_opt_slack,
  'K3':K3,
  'partner_m11_g7over4_bound':partner_bound
}
print(json.dumps(out,indent=2,sort_keys=True))
