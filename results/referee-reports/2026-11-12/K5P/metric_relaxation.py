"""Test whether resistance triangles and the rank-one formula suffice.

This is a relaxation, not a search for chains. It does not impose that the
inverse Green matrix has nonpositive off-diagonal entries.
"""
import os
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS',
          'VECLIB_MAXIMUM_THREADS','NUMEXPR_NUM_THREADS'):
    os.environ[k]='1'
from q1_core import np
from scipy.optimize import linprog
import json, time
from pathlib import Path

start=time.monotonic(); rng=np.random.default_rng(4810)
best=0; output=[]
for n in (4,5,6):
    q=n-1; ij=list(zip(*np.triu_indices(q))); ids={p:i for i,p in enumerate(ij)}
    m=len(ij)+1
    for rep in range(60):
        pi=rng.dirichlet(np.ones(n)*.6)
        h=np.r_[rng.uniform(0,1,n-2),1,0]; p=pi@h; s=h-p
        f=list(range(n-2))+[q-1,q-1]
        def C(i,j):
            z=np.zeros(m); z[ids[tuple(sorted((f[i],f[j])))]]=1
            return z
        def F(i,j):
            z=C(i,j); z[-1]=-s[i]*s[j]; return z
        A=[]; b=[]; E=[]
        for i in range(n):
            E.append(sum(pi[j]*F(i,j) for j in range(n)))
            for j in range(n):
                A.append(F(i,j)); b.append(1)
                for k in range(n):
                    A.append(F(i,j)+F(k,k)-F(i,k)-F(k,j)); b.append(0)
                    A.append(C(i,j)+C(k,k)-C(i,k)-C(k,j)); b.append(0)
        cost=-C(0,1)
        res=linprog(cost,A_ub=A,b_ub=b,A_eq=E,b_eq=np.zeros(n),
                    bounds=[(None,None)]*(m-1)+[(0,None)],method='highs')
        val=-res.fun if res.success else res.message
        if isinstance(val,float) and val>best+1e-7:
            best=val; output.append({'n':n,'value':val,'pi':pi.tolist(),
                       'h':h.tolist(),'variables':res.x.tolist()})
            print(n,rep,val,flush=True)
Path('metric_relaxation_results.json').write_text(json.dumps(output,indent=2))
print('best',best,'seconds',time.monotonic()-start)
