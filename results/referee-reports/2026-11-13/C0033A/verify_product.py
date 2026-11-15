"""Audit the explicit fourth variation at arbitrary coordinate product kernels."""
import os
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):os.environ[k]='1'
import numpy as np,json
import mpmath as mp
from pathlib import Path
from dpp import probabilities,basis,hessian,mp_matrix
rng=np.random.default_rng(330017);rows=[]
for n in (2,3,4,6,8):
    for cx in (False,True):
        errors=[];hess_errors=[];ratios=[]
        for trial in range(20):
            q=rng.uniform(.05,.95,n);Q=np.diag(q);bb=basis(n,cx)
            x=rng.normal(size=len(bb));A=np.einsum('b,bij->ij',x,bb);np.fill_diagonal(A,0)
            A/=np.linalg.norm(A)
            p,m=probabilities(Q);inv=np.linalg.inv(m);c=np.einsum('sij,jk->sik',inv,A)
            r=-p/2*np.einsum('sij,sji->s',c,c).real
            got=np.sum(r*r/p)/2
            v=q*(1-q);expected=sum(abs(A[i,j])**4/(2*v[i]*v[j]) for i in range(n) for j in range(i))
            errors.append(float(abs(got-expected)));ratios.append(float(got/(4/(n*(n-1)))))
            hh=hessian(Q,bb);target=np.zeros_like(hh);target[np.arange(n),np.arange(n)]=-1/v
            hess_errors.append(float(np.max(abs(hh-target))))
        # The sharp equality uses all pairs, including triangles for n>=3.
        Q=np.eye(n)/2;A=(np.ones((n,n))-np.eye(n))/np.sqrt(n*(n-1))
        equality=sum(abs(A[i,j])**4*8 for i in range(n) for j in range(i))
        assert max(errors)<1e-10 and max(hess_errors)<1e-10
        assert abs(equality-4/(n*(n-1)))<1e-12
        rows.append({'n':n,'field':'complex' if cx else 'real','trials':20,'max_coefficient_error':max(errors),'max_hessian_error':max(hess_errors),'min_ratio_to_dimension_bound':min(ratios),'sharp_coefficient':equality})

with mp.workdps(100):
    q=mp.diag([mp.mpf('.4'),mp.mpf('.6'),mp.mpf('.3')])
    a=mp.matrix([[0,mp.mpc('.1','.03'),mp.mpc('.02','-.04')],
                 [mp.mpc('.1','-.03'),0,mp.mpc('.07','.01')],
                 [mp.mpc('.02','.04'),mp.mpc('.07','-.01'),0]])
    def entropy(t):
        h=mp.mpf(0)
        for s in range(8):
            m=q+t*a
            for i in range(3):
                if not s>>i&1:m[i,i]-=1
            p=mp.re(mp.det(m))*(-1)**(3-s.bit_count());h-=p*mp.log(p)
        return h
    h4=mp.diff(entropy,0,4)
    variance=[q[i,i]*(1-q[i,i]) for i in range(3)]
    coefficient=sum(abs(a[i,j])**4/(2*variance[i]*variance[j]) for i in range(3) for j in range(i))
    assert abs(h4+24*coefficient)<mp.mpf('1e-90')
    mp_record={'n':3,'fourth_derivative':mp.nstr(h4,90),'predicted_coefficient':mp.nstr(coefficient,90),'residual':mp.nstr(abs(h4+24*coefficient),5)}
Path('data/product_verification.json').write_text(json.dumps({'seed':330017,'rows':rows,'direct_mp_fourth_derivative':mp_record},indent=2)+'\n')
print(json.dumps(rows,indent=2));print(mp_record)
