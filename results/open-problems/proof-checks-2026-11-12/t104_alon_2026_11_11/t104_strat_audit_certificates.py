"""Cross-check exact certificates against original eigenvector definitions."""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):
    os.environ[key]='1'
import numpy as np
import sympy as s
from exact_circulants import run
from verify_independent import setup

def direct(n,top,x):
    pairs,B,_=setup(n)
    w=np.array([x[min(j-i,n-(j-i))-1]*(2 if 2*(j-i)==n else 1)/n for i,j in pairs])
    L=B.T@(w[:,None]*B)
    topvec=[];lowvec=[]
    js=np.arange(n)
    for k in range(1,n//2+1):
        vecs=[(-1.)**js/np.sqrt(n)] if 2*k==n else [np.sqrt(2/n)*np.cos(2*np.pi*k*js/n),np.sqrt(2/n)*np.sin(2*np.pi*k*js/n)]
        (topvec if k in top else lowvec).extend(vecs)
    lam=topvec[0]@L@topvec[0]
    out=0.
    for u in topvec:
        for v in lowvec:
            mu=v@L@v;p=u*v;c=2*n/(n-2)
            P=mu+c*(lam*(p@p)-p@L@p)+(1-lam)*(1-c*(p@p))/(n-2)
            Q=2*np.dot(w,((B@u)*(B@v))**2)
            out+=(lam-mu)*(P-Q)
    return out

worst=0.;count=0
for n,top in [(5,(1,)),(6,(1,)),(6,(2,)),(6,(1,3)),(6,(2,3)),(7,(1,))]:
    r=run(n,top);K=r['field'];vertices=r['vertices']
    # All diagonal and cross coefficients checked independently at midpoints.
    for v in vertices:
        for w in vertices:
            mid=tuple((a+b)/K.from_sympy(s.Integer(2)) for a,b in zip(v,w))
            x=np.array([float(K.to_sympy(a).evalf()) for a in mid])
            expected=float(K.to_sympy(r['T'](mid)).evalf())
            error=abs(expected-direct(n,top,x));worst=max(worst,error);count+=1
            assert error<2e-13,(n,top,x,error)
print('Independent eigenvector audit:',count,'points; maximum absolute error',worst)
with open('LOG.md','a') as f:
    f.write('\n## 5. Independent certificate audit\n\nNUMERICAL cross-check of exact identities at all '+str(count)+' vertex pairs/midpoints, using real Fourier eigenvectors and the original P,Q definitions rather than the trace formula. Maximum absolute discrepancy '+str(worst)+'. Exact positivity itself uses rational interval lower bounds, not these floating-point checks.\n')
