"""Discover rational SOS matrices; only exact verified matrices are certificates.

The floating SDP is a discovery aid. Rational coefficient matching and exact
LDL tests decide whether a matrix is exported as a proof.
"""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','VECLIB_MAXIMUM_THREADS','MKL_NUM_THREADS'):
    os.environ[key]='1'
import itertools,json,sys
import sympy as s
import numpy as np
from scipy import sparse
import clarabel

from sympy.polys.rings import ring
from sympy.polys.domains import QQ
ring0,*gen=ring('z0,z1,z2,z3,x0,x1,x2',QQ)
zz,xi=gen[:4],gen[4:]
U=[sum(((5-j) if i<j else -j)*zz[j-1] for j in range(1,5)) for i in range(5)]
t=sum(x*x for x in U)
q=sum(x**4 for x in U)
d=sum(x**3 for x in U)
p=-U[0]*U[4]
delta=U[0]-U[4]
W=[sum((U[4]-U[j+1])*xi[j] for j in range(3))]
W += [delta*xi[j] for j in range(3)]
W += [sum((U[j+1]-U[0])*xi[j] for j in range(3))]
zeta=sum(x*x for x in W)
cf=sum(U[i]**2*W[i]**2 for i in range(5))
ef=sum(U[i]**2*W[i] for i in range(5))
ff=sum(U[i]*W[i]**2 for i in range(5))
hh=sum(W[i]**3 for i in range(5))
b4=sum(W[i]**4 for i in range(5))
v=U[0]+U[4]
lu=QQ(14,9)*(q*zeta+t*cf-t*t*zeta/5)
lw=QQ(14,9)*(t*b4+cf*zeta-t*zeta*zeta/5)
qb=QQ(2,9)*(q*zeta*zeta+t*t*b4+2*t*cf*zeta-QQ(2,5)*t*t*zeta*zeta)-QQ(4,3)*t*cf*zeta
qb+=QQ(10,3)*(ef*ef*zeta+t*ff*ff)+2*d*ff*zeta+2*t*ef*hh
rb=QQ(58,45)*t**3*zeta*zeta-QQ(40,9)*t**3*b4-QQ(299,72)*t*t*cf*zeta
alpha=140*p*q-28*p*t*t-47*q*t+13*t**3+24*d*d
enum=alpha*zeta+(140*p*t-41*t*t)*cf+6*t*ef*ef+18*t*d*ff
ratio=s.Rational(sys.argv[1]) if len(sys.argv)>1 else s.Rational(1,10)
rq=QQ(ratio.p,ratio.q)
poly=enum*zeta+QQ(9,2)*rq*(t*(20*p-t)*lw-(7*t-5*v*v)*lu*zeta+2*t*qb)
poly+=QQ(9,2)*rq*rq*(-t*(7*t-5*v*v)*lw+2*rb)
coeff={}
for mon,coef in poly.terms():
    c=s.Rational(coef.numerator,coef.denominator)
    zz,xx=mon[:4],mon[4:]
    assert sum(zz)==10 and sum(xx)==4
    coeff.setdefault(zz,{})[xx]=c
print('PROVED: expanded',len(coeff),'ternary quartic coefficient forms at r =',ratio,flush=True)

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
        if len(failed)<=3: print('NUMERICAL: no rational SOS at coefficient',zz,'solver status',sol.status,'margin',sol.x[-1],flush=True)
    else:
        den=s.ilcm(*[x.q for x in mat])
        records.append(dict(monomial=zz,scale=str(scale),denominator=int(den),matrix=[[int(den*x) for x in mat.row(i)] for i in range(6)]))
    if (number+1)%50==0:print('PROVED: processed',number+1,'exact SOS forms',len(records),'unresolved',len(failed),flush=True)
filename='quartic_ratio_matrices_'+str(ratio.p)+'_'+str(ratio.q)+'.json'
with open(filename,'w') as out:json.dump(dict(r=str(ratio),monomials=mons,records=records,failed=failed),out,indent=2)
print('PROVED: exact SOS forms',len(records),'NUMERICAL: unresolved coefficient forms',len(failed),flush=True)
if failed:sys.exit(1)
print('PROVED: all coefficient forms are SOS; endpoint certified.',flush=True)
