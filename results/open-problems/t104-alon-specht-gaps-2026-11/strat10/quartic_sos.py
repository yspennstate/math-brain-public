"""NUMERICAL discovery with exact rational coefficient repair and PSD acceptance."""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','VECLIB_MAXIMUM_THREADS','MKL_NUM_THREADS'):os.environ[key]='1'
import sympy as s
import numpy as np
from scipy import sparse
import clarabel

mons=[(2,0,0),(1,1,0),(1,0,1),(0,2,0),(0,1,1),(0,0,2)]
pairs=[(i,j) for j in range(6) for i in range(j+1)]
exps=sorted(set(tuple(a+b for a,b in zip(mons[i],mons[j])) for i,j in pairs))
idx={m:k for k,m in enumerate(exps)}
eq=np.zeros((len(exps),len(pairs)))
sv=np.zeros((len(pairs),len(pairs)))
for k,(i,j) in enumerate(pairs):
    m=tuple(a+b for a,b in zip(mons[i],mons[j]))
    eq[idx[m],k]=1 if i==j else 2
    sv[k,k]=1 if i==j else np.sqrt(2.)
Amat=sparse.csc_matrix(np.vstack((eq,-sv)))
cones=[clarabel.ZeroConeT(len(exps)),clarabel.PSDTriangleConeT(6)]
settings=clarabel.DefaultSettings()
settings.verbose=False
settings.max_threads=1
settings.tol_feas=1e-10
settings.tol_gap_abs=1e-10
settings.tol_gap_rel=1e-10
settings.max_iter=100

def psd(mat):
    # Exact symmetric elimination, valid for semidefinite matrices too.
    mat=s.MutableDenseMatrix(mat)
    while mat.rows:
        piv=mat[0,0]
        if piv<0:return False
        if piv==0:
            if any(mat[0,j]!=0 for j in range(1,mat.cols)):return False
            mat=mat[1:,1:]
        else:
            mat=mat[1:,1:]-(mat[1:,0]*mat[0,1:])/piv
    return True


def certify(poly):
    coeff={}
    for mon,coef in poly.terms():
        zz,xx=mon[:4],mon[4:]
        assert sum(zz)==10 and sum(xx)==4
        coeff.setdefault(zz,{})[xx]=s.Rational(coef.numerator,coef.denominator)
    records=[]
    failed=[]
    for number,(zz,ct) in enumerate(sorted(coeff.items())):
        scale=max(abs(c) for c in ct.values())
        target=np.array([float(ct.get(m,0)/scale) for m in exps])
        # Maximize a common diagonal margin via a tiny SDP.
        aa=np.hstack((Amat.toarray(),np.r_[np.zeros(len(exps)),np.array([1. if i==j else 0. for i,j in pairs])][:,None]))
        obj=np.zeros(len(pairs)+1)
        obj[-1]=-1
        sol=clarabel.DefaultSolver(sparse.csc_matrix((len(obj),len(obj))),obj,sparse.csc_matrix(aa),
                                   np.r_[target,np.zeros(len(pairs))],cones,settings).solve()
        success=False
        for digits in (7,10,13):
            vals=[s.Rational(round(x*10**digits),10**digits) for x in sol.x[:-1]]
            # Repair one Gram entry per monomial to make equality exact.
            for m in exps:
                ks=[k for k,(i,j) in enumerate(pairs) if tuple(a+b for a,b in zip(mons[i],mons[j]))==m]
                k=ks[0]
                factor=1 if pairs[k][0]==pairs[k][1] else 2
                current=sum((1 if pairs[j][0]==pairs[j][1] else 2)*vals[j] for j in ks)
                vals[k]+=(ct.get(m,0)/scale-current)/factor
            mat=s.zeros(6)
            for value,(i,j) in zip(vals,pairs):mat[i,j]=mat[j,i]=value
            if psd(mat):
                success=True
                break
        if not success:
            failed.append(zz)
            if len(failed)<=3: print('OPEN: no rational SOS at coefficient',zz,'solver status',sol.status,'margin',sol.x[-1],flush=True)
        else:
            den=s.ilcm(*[x.q for x in mat])
            records.append(dict(monomial=zz,scale=str(scale),denominator=int(den),matrix=[[int(den*x) for x in mat.row(i)] for i in range(6)]))
        if (number+1)%50==0:print('PROVED: processed',number+1,'exact SOS forms',len(records),'unresolved',len(failed),flush=True)
    return dict(monomials=mons,records=records,failed=failed)
