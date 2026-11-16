"""Independent bounded, single-thread numerical reproduction; no imported project code."""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):
    os.environ[key] = '1'
import json
import time
from itertools import combinations
import numpy as np
from scipy.linalg import null_space
from scipy.optimize import minimize

START = time.monotonic()

def setup(n):
    pairs = list(combinations(range(n), 2))
    B = np.zeros((len(pairs), n))
    for row, (i,j) in enumerate(pairs):
        B[row,i], B[row,j] = 1, -1
    H = null_space(np.ones((1,n)))
    return pairs, B, H

def evaluate(n,w):
    pairs,B,H = setup(n)
    L = B.T @ (np.asarray(w)[:,None]*B)
    ev,V = np.linalg.eigh(H.T@L@H)
    V = H@V
    lam = ev[-1]
    mask = lam-ev < 1e-9*lam
    U = V[:,mask]
    Pi = U@U.T
    D = U.shape[1]
    c = 2*n/(n-2)
    P = Q = 0.
    min_terms = np.full(3,np.inf)
    for mu,v in zip(ev[~mask],V[:,~mask].T):
        for u in U.T:
            p = u*v
            terms = np.array([mu,c*(lam*(p@p)-p@L@p),(1-lam)*(1-c*(p@p))/(n-2)])
            min_terms = np.minimum(min_terms,terms)
            P += (lam-mu)*sum(terms)
            Q += (lam-mu)*2*np.dot(w,((B@u)*(B@v))**2)
    G = lam*(np.eye(n)-np.ones((n,n))/n)-L
    tau = np.einsum('ei,ij,ej->e',B,Pi,B)
    gamma = np.einsum('ei,ij,ej->e',B,G,B)
    s2 = np.diag(Pi)@np.diag(G)
    s3 = np.trace(L@(Pi*G))
    x1 = D*(2*lam-np.trace(L@L))
    x2 = c*(lam*s2-s3)
    x3 = (1-lam)/(n-2)*(D*np.trace(G)-c*s2)
    y = 2*np.dot(w,tau*gamma)
    assert abs(P-x1-x2-x3)<1e-8
    assert abs(Q-y)<1e-8
    assert np.min(gamma)>-1e-8
    assert np.max(gamma-lam*(2-tau))<1e-8
    return dict(n=n,D=D,lam=lam,relative_gap=(ev[-1]-ev[-2])/lam,
                P=P,Q=Q,T=P-Q,ratio=Q/P if P>1e-15 else None,
                min_terms=min_terms.tolist(),trace_error=max(abs(P-x1-x2-x3),abs(Q-y)))

def main():
    records=[]
    for n in (5,7):
        pairs,_,_=setup(n)
        w=np.array([1/n if (j-i in (1,n-1)) else 0 for i,j in pairs])
        r=evaluate(n,w);r['name']=f'C{n}';records.append(r);print(r,flush=True)
    pairs,_,_=setup(6)
    w=np.array([1/6 if (i<3 and j<3) or (i>=3 and j>=3) else 0 for i,j in pairs])
    r=evaluate(6,w);r['name']='two triangles';records.append(r);print(r,flush=True)
    rng=np.random.default_rng(20261112)
    for n in (5,6,7):
        pairs,B,H=setup(n)
        BH=B@H
        def gap(z):
            if time.monotonic()-START>110:
                raise TimeoutError('110 second global computation cap')
            w=z*z;w=w/w.sum()
            ev=np.linalg.eigvalsh(BH.T@(w[:,None]*BH))
            return (ev[-1]-ev[-2])/ev[-1]
        for run in range(5):
            z=np.sqrt(rng.dirichlet(np.ones(len(pairs))*.7))
            fit=minimize(gap,z,method='Nelder-Mead',options=dict(maxiter=6500,xatol=1e-12,fatol=1e-14))
            w=fit.x**2;w/=sum(w)
            if gap(fit.x)<1e-9:
                r=evaluate(n,w);r.update(name=f'random {n} {run}',weights=w.tolist())
                records.append(r);print({k:v for k,v in r.items() if k!='weights'},flush=True)
                if r['ratio'] is not None and r['ratio']>1+1e-9:
                    with open('candidate.json','w') as f:json.dump(r,f,indent=2)
                    raise RuntimeError('Counterexample candidate: stop and verify at 50 digits')
    with open('numerical_reproduction.json','w') as f:json.dump(records,f,indent=2)
    with open('LOG.md','a') as f:
        f.write('\n## 2. Independent numerical reproduction\n\nNUMERICAL. '+str(len(records))+' records saved in numerical_reproduction.json; pair definitions and trace identities agree. No ratio above one. Runtime %.2f seconds.\n'%(time.monotonic()-START))

if __name__=='__main__':main()
