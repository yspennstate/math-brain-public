import json, numpy as np
from scipy.linalg import qr
from scipy.special import lambertw
rng=np.random.default_rng(20260915024)

def calc(K, with_detail=False):
    n=len(K); A=K@(np.eye(n)-K); g=np.trace(A).real
    ps=[]; dds=[]; vals=[]
    for s in range(1<<n):
        J=np.array([not (s>>i&1) for i in range(n)])
        N=K-np.diag(J.astype(float)); p=(-1)**J.sum()*np.linalg.det(N).real
        R=np.linalg.solve(N,A)
        dd=p*(np.trace(R)**2-np.trace(R@R)).real
        ps.append(p); dds.append(dd)
    acc=np.dot(dds,np.log(ps)); ratio=-acc/g
    return (ratio, g, acc, ps, dds) if with_detail else ratio

ans={}
for n in (2,3,4,5,6):
    best=(-1,None)
    count=1500 if n<5 else 500
    for k in range(count):
        if k%2:
            c=rng.uniform(.01,.499)
            lam=np.full(n,.5-c); lam[:n//2]=.5+c
        else:
            lam=rng.beta(.55,.55,n)*.998+.001
        U=qr(rng.normal(size=(n,n))+1j*rng.normal(size=(n,n)))[0]
        K=(U*lam)@U.conj().T
        r=calc(K)
        if r>best[0]:best=(r,K)
    ans[str(n)]={'max_ratio':best[0], 'K_re':best[1].real.tolist(), 'K_im':best[1].imag.tolist()}
    print(n,best[0],flush=True)
ans['kappa']=float(lambertw(np.exp(-1)).real)
open('computations/C024/explore.json','w').write(json.dumps(ans,indent=2))
