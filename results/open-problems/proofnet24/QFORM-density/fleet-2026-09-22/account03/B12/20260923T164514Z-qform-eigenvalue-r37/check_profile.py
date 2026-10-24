import numpy as np, math, json

rng=np.random.default_rng(20260923)

def rand_orth(n):
    q,_=np.linalg.qr(rng.normal(size=(n,n)))
    return q

def svals(m):
    return np.linalg.svd(m,compute_uv=False)

profile_violations=0
profile_tests=0
min_margin=float('inf')
for _ in range(10000):
    n=int(rng.integers(7,16))
    qmat=rand_orth(n)
    k=int(rng.integers(3,min(6,n-1)+1))
    lam0=np.zeros(n)
    lam0[:k]=(1+rng.random(k)*3)*rng.choice([-1,1],size=k)
    lamr=np.zeros(n)
    lamr[k:]=(10**rng.uniform(-4,4,size=n-k))*rng.choice([-1,1],size=n-k)
    a0=qmat@np.diag(lam0)@qmat.T
    r=qmat@np.diag(lamr)@qmat.T
    a=a0+r
    m=int(rng.integers(k,n))
    I=np.sort(rng.choice(n,size=m,replace=False))
    keep=np.ones(n,dtype=bool); keep[I]=False
    J=np.nonzero(keep)[0]
    g=(a0@a0)[np.ix_(I,I)]
    ev=np.linalg.eigvalsh(g)[::-1]
    gamma2=max(float(ev[k-1]),0.0)
    c=a[np.ix_(I,I)]
    b=a[np.ix_(I,J)]
    sc=svals(c); sb=svals(b)
    for p in range(1,k+1):
        q=k+1-p
        if q<=len(sb):
            margin=float(sc[p-1]**2+sb[q-1]**2-gamma2)
            profile_tests+=1
            min_margin=min(min_margin,margin)
            if margin < -1e-8:
                profile_violations+=1

def hadamard(n):
    h=np.array([[1.0]])
    while h.shape[0]<n:
        h=np.block([[h,h],[h,-h]])
    return h

h=hadamard(1024)
u=h[:,:3]/math.sqrt(1024)
max_lev=float(np.max(np.sum(u*u,axis=1)))
partition_trials=5000
success=0
max_dev=0.0
min_eig=1.0
for _ in range(partition_trials):
    mask=rng.integers(0,2,size=1024).astype(bool)
    gram=u[mask].T@u[mask]
    dev=float(np.linalg.norm(gram-0.5*np.eye(3),2))
    max_dev=max(max_dev,dev)
    min_eig=min(min_eig,float(np.linalg.eigvalsh(gram).min()))
    success += int(dev<=0.25)

out={
  'seed':20260923,
  'profile_random_matrices':10000,
  'profile_inequality_instances':profile_tests,
  'profile_violations':profile_violations,
  'minimum_profile_margin':min_margin,
  'hadamard_n':1024,
  'hadamard_max_row_leverage':max_lev,
  'required_leverage_cap':1/256,
  'partition_trials':partition_trials,
  'partition_successes_deviation_le_1_4':success,
  'largest_partition_deviation_observed':max_dev,
  'smallest_lambda_min_Gram_observed':min_eig,
  'analytic_union_bound_failure_probability_upper':9826*math.exp(-18),
  'note':'finite checks only; not proof'
}
print(json.dumps(out,indent=2,sort_keys=True))
