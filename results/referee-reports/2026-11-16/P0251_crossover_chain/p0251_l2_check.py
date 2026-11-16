import numpy as np, sys
from math import comb, log2
rng=np.random.default_rng(11)
K=int(sys.argv[1]); R=int(sys.argv[2]); TMAX=int(sys.argv[3]); s=K//2
lam=(K-2)/(2*(K-1))
# original chain, two columns, shared permutation, independent coins per column
X=np.zeros((R,2,K),dtype=np.int8); X[:,:,:s]=1
hyp=np.array([comb(s,k)*comb(K-s,s-k) for k in range(s+1)],dtype=float); hyp/=hyp.sum()
for t in range(1,TMAX+1):
    for r in range(R):
        p=rng.permutation(K); y=X[r][:,p]
        for c in range(2):
            sw=rng.random(K//2)<0.5; e=y[c,0::2].copy(); o=y[c,1::2].copy()
            y[c,0::2]=np.where(sw,o,e); y[c,1::2]=np.where(sw,e,o)
        X[r]=y
    W=(X[:,0,:]&X[:,1,:]).sum(1); Y=W-s*s/K
    emp=np.bincount(W,minlength=s+1)/R
    print(f"orig L=2 K={K} t={t} meanY={Y.mean():.2f} pred={lam**t*K/4:.2f} varY={Y.var():.1f} TV(W)>={0.5*np.abs(emp-hyp).sum():.3f}")
print("half log2 K =",0.5*log2(K))
