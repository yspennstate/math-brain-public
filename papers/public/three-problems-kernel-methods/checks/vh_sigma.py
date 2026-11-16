import numpy as np, math
rng=np.random.default_rng(3)
for d in (4,6,8):
    p=d*(d+1)//2; N=400000
    X=rng.standard_normal((N,d))
    Z=np.empty((N,p)); Z[:,:d]=(X**2-1)/math.sqrt(2); iu=np.triu_indices(d,1); Z[:,d:]=X[:,iu[0]]*X[:,iu[1]]
    nz=(Z**2).sum(1)
    M=(Z*nz[:,None]).T@Z/N - np.eye(p)        # E[|z|^2 z z^T] - I
    ev=np.linalg.eigvalsh(M)
    alpha=(d*d+13*d+16)/2; beta=(d*d+9*d+16)/2
    print(f"d={d}: top eig {ev[-1]:.3f} (pred alpha-1={alpha-1:.3f}), next {ev[-2]:.3f} (pred beta-1={beta-1:.3f}), min {ev[0]:.3f}; sigma^2=(p-1)(alpha-1)={(p-1)*(alpha-1):.1f}")
