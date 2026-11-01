"""Independent check of the closed forms used in the memo.
(1) Renyi: for independent E_i ~ Exp(i*theta), i=1..d,  P(sum E_i > t) = 1 - (1 - e^{-theta t})^d  (law of max of d iid Exp(theta)).
    Checked by Monte Carlo against the formula and against the matrix-exponential pure-birth chain.
(2) Constant rates a: mass at site k (1-based) of the pure-birth chain started at 1 equals e^{-at}(at)^{k-1}/(k-1)!; total mass = P(Poisson(at) <= d-1).
"""
import numpy as np
from scipy.linalg import expm
from scipy.stats import poisson
rng=np.random.default_rng(3)
theta=1.0
for d in [8,32]:
    rates=theta*np.arange(1,d+1)
    N=200000; S=np.sum(rng.exponential(1/rates, size=(N,d)),axis=1)
    A=np.zeros((d,d))
    for i in range(d):
        A[i,i]=-rates[i]
        if i+1<d: A[i+1,i]=rates[i]
    for t in [1.0, 2.0, 4.0, 6.0]:
        mc=(S>t).mean(); formula=1-(1-np.exp(-theta*t))**d; chain=expm(A*t)[:,0].sum()
        print(f"d={d} t={t}: MC {mc:.4f}  formula {formula:.4f}  chain {chain:.4f}  d*e^-t {d*np.exp(-theta*t):.4f}")
a=1.0
for d in [8,32]:
    A=np.zeros((d,d))
    for i in range(d):
        A[i,i]=-a
        if i+1<d: A[i+1,i]=a
    for t in [d/2, d, 2*d]:
        p=expm(A*t)[:,0]; k=np.arange(d)
        closed=np.exp(-a*t)*(a*t)**k/np.array([np.math.factorial(int(x)) if hasattr(np,'math') else 1 for x in k]) if False else None
        from scipy.special import gammaln
        closed=np.exp(-a*t + k*np.log(a*t) - gammaln(k+1))
        print(f"const a: d={d} t={t}: max|chain-closed| {np.abs(p-closed).max():.2e}; total {p.sum():.4f} vs Poisson cdf {poisson.cdf(d-1,a*t):.4f}")
