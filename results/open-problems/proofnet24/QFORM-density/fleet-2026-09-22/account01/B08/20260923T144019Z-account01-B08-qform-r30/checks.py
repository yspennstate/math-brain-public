import json, math
import numpy as np

rng=np.random.default_rng(20260923144019)
min_slack=float('inf')
tested=0
for trial in range(500):
    n=int(rng.integers(6,30))
    Q,_=np.linalg.qr(rng.normal(size=(n,n)))
    lam=rng.uniform(-2,2,n)
    lam[np.abs(lam)<0.02]=0.03
    A=Q@np.diag(lam)@Q.T
    order=np.argsort(-np.abs(lam))
    r=int(rng.integers(2,min(n,8)+1))
    idx=order[:r]
    U=Q[:,idx]
    a=float(np.min(np.abs(lam[idx])))
    for i in rng.choice(n,size=min(4,n),replace=False):
        T=[j for j in range(n) if j!=i]
        C=A[np.ix_(T,T)]
        s=np.linalg.svd(C,compute_uv=False)
        p=float(np.sum(U[i,:]**2))
        lhs=float(s[r-2])
        rhs=a*math.sqrt(max(0.0,1-p))
        slack=lhs-rhs
        min_slack=min(min_slack,slack)
        tested+=1
        assert slack>=-1e-9

CR=288*math.sqrt(3*math.e)/13
out={
  'seed':20260923144019,
  'rank_loss_random_instances':tested,
  'minimum_numeric_slack':min_slack,
  'violations':0,
  'C_ridge':CR,
  'C_second_level':CR*64*math.sqrt(3),
  'L1_factor':1/(64*math.sqrt(3)),
  'ultrahigh_pivot_or_star_factor':1/(64*math.sqrt(3)),
  'selected_child2_factor':math.sqrt(47/48),
  'partner_star_factor':(3/16)*math.sqrt(3/10),
  'second_core_row_factor':1/(32768*math.sqrt(3)),
}
print(json.dumps(out,indent=2))
