import numpy as np
rng=np.random.default_rng(3341);R=np.array([[1,1,1],[1,-1,-1],[-1,1,-1],[-1,-1,1]])
worst_sdd=1e9;worst=1e9;minoff=1e9
for tr in range(30000):
 v=rng.dirichlet([.4,.4,.4, .1])[:3];w=1-R@v;D=R-v
 if w.min()<1e-8:continue
 J=D.T@(D/w[:,None]);C=-sum(np.log(w[k])*(np.outer(R[k],R[k])-np.eye(3)) for k in range(4));M=J-C-4*np.eye(3)
 val=(np.diag(M)-(np.abs(M).sum(axis=1)-abs(np.diag(M)))).min();eig=np.linalg.eigvalsh(M)[0]
 if val<worst_sdd:worst_sdd=val;ws=v.tolist()
 if eig<worst:worst=eig;we=v.tolist()
 minoff=min(minoff,M[np.triu_indices(3,1)].min())
print('sdd',worst_sdd,ws,'eig',worst,we,'minoff',minoff)
