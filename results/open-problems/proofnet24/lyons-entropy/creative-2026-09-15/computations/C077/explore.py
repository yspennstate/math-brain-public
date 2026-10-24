import numpy as np
from scipy.optimize import linprog
import json

def curvature(K,d):
    n=len(d); B=(d[:,None]-d[None,:])**2*K
    ps=[]; cs=[]
    for s in range(1<<n):
        q=K-np.diag([not(s>>i&1) for i in range(n)])
        p=(-1)**(n-s.bit_count())*np.linalg.det(q).real
        ps.append(p); cs.append(p*np.trace(np.linalg.solve(q,B)).real)
    return np.array(ps),np.array(cs)

def constraints(n):
    rows=[]
    for i in range(n):
        for j in range(i):
            for s in range(1<<n):
                if (s>>i&1) or (s>>j&1): continue
                row=np.zeros(1<<n)
                row[s]=row[s|(1<<i)|(1<<j)]=1
                row[s|(1<<i)]=row[s|(1<<j)]=-1
                rows.append(row)
    return np.array(rows)

if __name__=='__main__':
    rng=np.random.default_rng(77001)
    out=[]
    for n in [3,4,5,6]:
        rows=constraints(n)
        best=-np.inf
        for it in range(120):
            z=rng.normal(size=(n,n))+1j*rng.normal(size=(n,n))
            U,_=np.linalg.qr(z)
            eigenvalues=rng.uniform(.03,.97,n)
            K=(U*eigenvalues)@U.conj().T
            d=rng.normal(size=n)
            ps,cs=curvature(K,d)
            bounds=[(0,0) if s.bit_count()<=1 else (None,None) for s in range(1<<n)]
            res=linprog(-cs,A_ub=np.r_[-rows,rows],b_ub=np.r_[np.zeros(len(rows)),np.ones(len(rows))],bounds=bounds,method='highs')
            if not res.success: raise RuntimeError(res.message)
            value=cs@res.x
            best=max(best,value)
            if value>1e-8:
                data=dict(n=n,it=it,value=float(value),K_real=K.real.tolist(),K_imag=K.imag.tolist(),d=d.tolist(),f=res.x.tolist(),cs=cs.tolist(),entropy_curvature=float(-cs@np.log(ps)))
                out.append(data)
                print(json.dumps(data),flush=True)
                break
        print('n',n,'best',best,flush=True)
    with open('supermod_search.json','w') as f: json.dump(out,f,indent=2)
