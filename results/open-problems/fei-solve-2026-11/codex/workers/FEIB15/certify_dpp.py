#!/usr/bin/env python3
"""Certify every NA spectrum type through n=4 as a positive-contraction DPP.

No numerical eigenvalue tolerances: generating polynomials and all principal
minors of K and I-K are checked over the rationals.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import itertools,json,time,resource
import numpy as np
import sympy as sp

def principal_minors_nonnegative(K):
    n=K.rows
    return all(K.extract(ids,ids).det()>=0 for k in range(1,n+1) for ids in itertools.combinations(range(n),k))

start=time.monotonic(); output=[]
for n in range(1,5):
    r=np.load(f'census_n{n}.npz'); w=r['weights']; m=1<<n
    z=sp.symbols(f'z1:{n+1}')
    maps=[[sum(((s>>j)&1)<<perm[j] for j in range(n)) for s in range(m)] for perm in itertools.permutations(range(n))]
    groups={}
    for t in np.flatnonzero(r['NA']):
        key=min(tuple(int(w[t,s]) for s in smap) for smap in maps)
        if key not in groups:groups[key]={'representative_table':int(t),'functions':0}
        groups[key]['functions']+=1
    rows=[]
    for key,row in groups.items():
        g=sum(v*sp.prod(z[j] for j in range(n) if s>>j&1) for s,v in enumerate(key))
        K=sp.zeros(n); claimed=set(); factors=sp.factor_list(g)[1]
        for fac,power in factors:
            assert power==1
            vs=sorted(fac.free_symbols,key=str)
            assert not claimed.intersection(vs); claimed.update(vs)
            B=None; order=vs
            if len(vs)==1:
                zz=vs[0]; den=fac.subs(zz,1)
                B=sp.Matrix([[sp.diff(fac,zz)/den]])
            elif len(vs)==2:
                assert sp.expand(fac/fac.coeff(vs[0]))==vs[0]+vs[1]
                B=sp.ones(2)/2
            elif len(vs)==3:
                for a,b,c in itertools.permutations(vs):
                    q=(a+b)*(1+c)+4*c
                    qr=sp.expand(a*b*c*q.subs({a:1/a,b:1/b,c:1/c},simultaneous=True))
                    N=sp.Matrix([[1,1,1],[1,1,1],[1,1,3]])/4
                    norm=fac/fac.subs({v:1 for v in vs})
                    if sp.expand(norm-q/8)==0: B=N;order=[a,b,c];break
                    if sp.expand(norm-qr/8)==0: B=sp.eye(3)-N;order=[a,b,c];break
            assert B is not None,(n,key,fac)
            ids=[z.index(v) for v in order]
            for i,ii in enumerate(ids):
                for j,jj in enumerate(ids): K[ii,jj]=B[i,j]
        # Variables not appearing in g are absent with probability one.
        assert principal_minors_nonnegative(K) and principal_minors_nonnegative(sp.eye(n)-K)
        norm=g/g.subs({v:1 for v in z})
        det=sp.expand((sp.eye(n)-K+K*sp.diag(*z)).det())
        assert sp.expand(det-norm)==0
        row.update(polynomial=str(sp.factor(norm)),kernel=[[str(v) for v in K.row(i)] for i in range(n)],all_principal_minors_nonnegative=True,determinant_identity_exact=True)
        rows.append(row)
    output.append(dict(n=n,NA_functions=int(r['NA'].sum()),certified_DPP_functions=sum(row['functions'] for row in rows),types=len(rows),certificates=rows))
out=dict(census=output,seconds=time.monotonic()-start,max_rss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
with open('dpp_certificates.json','w') as f:json.dump(out,f,indent=2)
print(json.dumps(out,indent=2))
