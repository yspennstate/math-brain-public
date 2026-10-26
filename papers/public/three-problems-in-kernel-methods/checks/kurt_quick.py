import numpy as np, math
rng=np.random.default_rng(11)
def unvec(v,d):
    M=np.zeros((d,d)); iu=np.triu_indices(d,1); M[np.diag_indices(d)]=v[:d]; M[iu]=v[d:]/math.sqrt(2); return M+M.T-np.diag(np.diag(M))
N=600000
for d in (6,10,20,30):
    p=d*(d+1)//2; U=unvec(rng.standard_normal(p),d); U/=np.linalg.norm(U,'fro')
    X=rng.standard_normal((N,d)); z=(((X@U)*X).sum(1)-np.trace(U))/math.sqrt(2)
    kg=np.mean(z**4)/np.mean(z**2)**2
    Xs=X/np.linalg.norm(X,axis=1,keepdims=True); zs=((Xs@U)*Xs).sum(1)-np.trace(U)/d; ks=np.mean(zs**4)/np.mean(zs**2)**2
    tr4=float((np.linalg.eigvalsh(U)**4).sum())
    print(f"d={d}: Gaussian row kurt {kg:.3f} (formula 3+12TrU^4={3+12*tr4:.3f}, 3+24/d={3+24/d:.3f}); sphere row {ks:.3f}; (kurt-3)*d={(kg-3)*d:.1f}")
