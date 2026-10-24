try:
    import psutil; psutil.Process().nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
except Exception: pass
import numpy as np, itertools
rng=np.random.default_rng(3)
def esym(lam,k):
    c=np.array([1.0])
    for l in lam: c=np.convolve(c,[1.0,l])
    return c[k] if k<len(c) else 0.0
def vs_marginals(M):
    U,s,Vt=np.linalg.svd(M,full_matrices=False); lam=s**2
    Z=esym(lam,3)
    p=np.array([lam[m]*esym(np.delete(lam,m),2)/Z for m in range(len(lam))])
    alpha=(U**2)@p
    return Z,alpha,p.sum()
# brute-force check of the marginal formula on a small matrix
M=rng.standard_normal((5,6)); Z,alpha,ps=vs_marginals(M)
tot=0; marg=np.zeros(5)
for S in itertools.combinations(range(5),3):
    for T in itertools.combinations(range(6),3):
        d=np.linalg.det(M[np.ix_(S,T)])**2; tot+=d
        for i in S: marg[i]+=d
print("Z formula",round(Z,4),"brute",round(tot,4)," alpha formula",alpha.round(4)," brute",(marg/tot).round(4)," sum p",round(ps,4))
# Theorem D bound on rank-3 + eps*dense models
for n in [40,120,400]:
    R,_=np.linalg.qr(rng.standard_normal((n,3)))
    A3=R@np.diag([1.,1.,-1.])@R.T
    G=rng.standard_normal((n,n)); B=(G+G.T)/np.sqrt(2*n)
    for eps in [0.0,0.1,0.5,1.0]:
        A=A3+eps*B
        perm=rng.permutation(n); I=perm[:n//2]; J=perm[n//2:]
        Z,alpha,_=vs_marginals(A[np.ix_(I,J)])
        bound=6*np.sqrt(np.e)*Z**(-1/6)
        print(f"n={n:4d} eps={eps:3.1f}  Z={Z:10.4g}  max alpha={alpha.max():.3f}  density bound={bound:7.3f}")
