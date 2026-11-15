"""Exact conditioning identity and singular-R examples; numerical scalar audit."""
import os
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):os.environ[k]='1'
import json,time,resource
from pathlib import Path
import sympy as sp
import numpy as np
import mpmath as mp
from dpp import basis,probabilities,random_kernel,mp_matrix
from probe_scalar import certificate

def main():
    start=time.monotonic();t=sp.symbols('t');q=sp.eye(4)/2
    aa=sp.Matrix([1,1,1,1])/4;bb=sp.Matrix([1,2,-1,-2])/4
    u=aa.row_join(bb);a=u*u.T;qt=q+t*a
    g=(u[3:4,:].T*u[3:4,:])*2
    w=u[:3,:]
    k=qt[:3,:3]-qt[:3,3:4]*qt[3:4,3:4].inv()*qt[3:4,:3]
    formula=sp.eye(3)/2+t*w*(sp.eye(2)+t*g).inv()*w.T
    assert all(sp.cancel(z)==0 for z in k-formula)
    k2=k.diff(t,2).subs(t,0);assert k2!=sp.zeros(3)
    result=dict(conditioning_example=dict(Q=str(q),A=str(a),rank=int(a.rank()),pattern_probability=str(qt[3,3]),conditional_second_derivative=str(k2),woodbury_exact=True))
    q3=sp.Matrix([[sp.Rational(2,5),sp.Rational(1,10),0],[sp.Rational(1,10),sp.Rational(1,2),0],[0,0,sp.Rational(3,5)]])
    p=[]
    for s in range(8):p.append(sp.factor((-1)**(3-s.bit_count())*(q3-sp.diag(*[0 if s>>i&1 else 1 for i in range(3)])).det()))
    gam=sp.cancel(p[7]*p[1]*p[2]*p[4]/(p[0]*p[3]*p[5]*p[6]));assert gam==1
    odds=[sp.cancel(p[2]*p[4]/(p[0]*p[6])),sp.cancel(p[1]*p[4]/(p[0]*p[5])),sp.cancel(p[1]*p[2]/(p[0]*p[3]))]
    assert odds[:2]==[1,1] and odds[2]>1
    result['singular_R_example']=dict(Q=str(q3),exp_gamma=str(gam),exp_ell0=list(map(str,odds)),rank_R=1)
    # Compare the scalar criterion against the direct original-coordinate formula.
    rng=np.random.default_rng(33363);err=0
    b=basis(3,True)
    for it in range(100):
        q=random_kernel(rng,3,True,'uniform');p,m=probabilities(q);inv=np.linalg.inv(m)
        ell=np.log([p[2]*p[4]/(p[0]*p[6]),p[1]*p[4]/(p[0]*p[5]),p[1]*p[2]/(p[0]*p[3])])
        gamma=np.log(p[7]*p[1]*p[2]*p[4]/(p[0]*p[3]*p[5]*p[6]));r=np.diag(ell)-gamma*q;ri=np.linalg.inv(r);d=np.linalg.det(r).real
        dp=p[:,None]*np.einsum('sij,bji->sb',inv,b,optimize=False).real
        f=np.einsum('sb,sc,s->bc',dp,dp,1/p,optimize=False)
        ri_b=np.einsum('ij,bjk->bik',ri,b,optimize=False)
        j=f+d*np.einsum('bij,cji->bc',ri_b,ri_b,optimize=False).real
        z=np.trace(ri_b,axis1=1,axis2=2).real
        direct=d*z@np.linalg.solve(j,z)
        err=max(err,abs(direct-certificate(q)))
    result['scalar_identity']=dict(trials=100,max_difference=err)
    result['seconds']=time.monotonic()-start;result['peak_rss_mib']=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/2**20
    Path('data/structural_audit.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
