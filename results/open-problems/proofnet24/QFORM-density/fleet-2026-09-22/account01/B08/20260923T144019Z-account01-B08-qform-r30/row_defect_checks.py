import math
import numpy as np

rng=np.random.default_rng(20260923144444)
viol=0
min_slack=float('inf')
cnt=0
for trial in range(500):
    n=int(rng.integers(8,40))
    Q,_=np.linalg.qr(rng.normal(size=(n,n)))
    lam=rng.uniform(-4,4,n)
    lam[:3]=rng.choice([-1,1],3)*rng.uniform(1,3,3)
    A=Q@np.diag(lam)@Q.T
    R=Q[:,:3]
    L=float(np.min(np.abs(lam[:3])))
    for i in rng.choice(n,size=min(5,n),replace=False):
        p=float(np.sum(R[i,:]**2))
        if p>=1:
            continue
        T=[j for j in range(n) if j!=i]
        C=A[np.ix_(T,T)]
        b=A[T,i]
        s3=float(np.linalg.svd(C,compute_uv=False)[2])
        rhs=L*math.sqrt(max(0,1-p))-np.linalg.norm(b)*math.sqrt(p)
        slack=s3-max(0,rhs)
        min_slack=min(min_slack,slack)
        cnt+=1
        assert slack>=-1e-8

kappa=math.sqrt(47/48)-1/(4*math.sqrt(48))
CR=288*math.sqrt(3*math.e)/13
print('instances',cnt)
print('violations',viol)
print('minimum_slack',min_slack)
print('kappa',kappa)
print('child_payment_constant',CR/kappa)
print('second_core_row_factor',kappa/512)
print('QFORM_B08_R30_ROW_DEFECT_CHECK_PASS')
