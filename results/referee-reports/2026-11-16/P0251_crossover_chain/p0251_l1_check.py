import numpy as np, sys
from math import comb, log2
rng=np.random.default_rng(7)
K=int(sys.argv[1]); R=int(sys.argv[2]); TMAX=int(sys.argv[3])
s=K//2; h=K//2
lam=(K-2)/(2*(K-1))
def step_labeled(X):
    # X: R x K 0/1; each row: uniform perfect matching, each pair swapped w.p. 1/2
    out=X.copy()
    for r in range(X.shape[0]):
        p=rng.permutation(K); a=p[0::2]; b=p[1::2]
        sw=rng.random(K//2)<0.5
        out[r,a[sw]]=X[r,b[sw]]; out[r,b[sw]]=X[r,a[sw]]
    return out
def step_original(X):
    out=np.empty_like(X)
    for r in range(X.shape[0]):
        p=rng.permutation(K); sw=rng.random(K//2)<0.5
        y=X[r,p].copy(); e=y[0::2].copy(); o=y[1::2].copy()
        y[0::2]=np.where(sw,o,e); y[1::2]=np.where(sw,e,o); out[r]=y
    return out
# hypergeometric law of n_A under u_s
hyp=np.array([comb(s,k)*comb(K-s,h-k) for k in range(h+1)],dtype=float); hyp/=hyp.sum()
def tv_nA(X):
    n=X[:,:h].sum(1); emp=np.bincount(n,minlength=h+1)/len(n)
    return 0.5*np.abs(emp-hyp).sum()
x0=np.zeros(K,dtype=np.int8); x0[:s]=1
for name,f in (("labeled",step_labeled),("original",step_original)):
    X=np.tile(x0,(R,1))
    for t in range(1,TMAX+1):
        X=f(X); Z=X[:,:h].sum(1)-K/4
        print(f"{name} K={K} t={t} meanZ={Z.mean():.2f} pred={lam**t*K/4:.2f} varZ={Z.var():.1f} K/16={K/16:.1f} TV(nA)>={tv_nA(X):.3f}")
print("half log2 K =",0.5*log2(K))
