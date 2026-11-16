"""NUMERICAL Gram discovery; export only exact rational coefficient/PSD checks."""
import os
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):os.environ[k]='1'
import itertools,json,time
from pathlib import Path
import sympy as s
import numpy as np
from scipy import sparse
from scipy.spatial import ConvexHull
import clarabel
from cubic_moment import construct
from quartic_sos import psd

def mons(n,d):
    return [x for x in itertools.product(range(d+1),repeat=n)if sum(x)==d]

def setup():
    z,p=construct();target={m:s.Rational(c)for m,c in p.terms()};hull=ConvexHull(np.array(list(target),float)[:,:3])
    blocks=[]
    for deg in (0,2,4):
        for inds in itertools.combinations(range(4),deg):
            w=tuple(int(i in inds)for i in range(4));mm=mons(4,(6-deg)//2)
            mm=[m for m in mm if np.max(hull.equations[:,:3]@np.array([2*m[i]+w[i]for i in range(3)])+hull.equations[:,3])<1e-7]
            # At (1,0,0,1), every summand with positive multiplier must vanish.
            if w[1]+w[2]<=1:
                row=s.Matrix([[int(m[1]==m[2]==0)for m in mm]])
                ns=row.nullspace();basis=[{m:v[i]for i,m in enumerate(mm)if v[i]}for v in ns]
            else:basis=[{m:s.Integer(1)}for m in mm]
            if basis:blocks.append((w,basis))
    exps=mons(4,6);idx={m:i for i,m in enumerate(exps)}
    columns=[];positions=[]
    for bi,(w,basis)in enumerate(blocks):
        for j in range(len(basis)):
            for i in range(j+1):
                c={}
                for a,x in basis[i].items():
                    for b,y in basis[j].items():
                        m=tuple(w[k]+a[k]+b[k]for k in range(4));c[m]=c.get(m,0)+(1 if i==j else 2)*x*y
                columns.append(c);positions.append((bi,i,j))
    E=s.zeros(len(exps),len(columns))
    for j,c in enumerate(columns):
        for m,v in c.items():E[idx[m],j]=v
    return blocks,exps,E,positions,s.Matrix([target.get(m,0)for m in exps])

def main():
    blocks,exps,E,positions,target=setup();n=len(positions)
    # Uniform interior margin after exact zero-face reduction.
    cone_rows=np.zeros((n,n+1));offset=0
    for k,(bi,i,j)in enumerate(positions):cone_rows[k,k]=-(1 if i==j else np.sqrt(2));cone_rows[k,-1]=int(i==j)
    scale=max(abs(v)for v in target);emat=np.array(E,float)
    mat=np.vstack((np.c_[emat,np.zeros(len(exps))],cone_rows));rhs=np.r_[np.array(target,float).ravel()/float(scale),np.zeros(n)]
    cones=[clarabel.ZeroConeT(len(exps))]+[clarabel.PSDTriangleConeT(len(b))for w,b in blocks]
    settings=clarabel.DefaultSettings();settings.verbose=False;settings.max_threads=1;settings.max_iter=200
    settings.tol_feas=settings.tol_gap_abs=settings.tol_gap_rel=1e-10
    obj=np.r_[np.zeros(n),-1.]
    sol=clarabel.DefaultSolver(sparse.csc_matrix((n+1,n+1)),obj,sparse.csc_matrix(mat),rhs,cones,settings).solve()
    print('NUMERICAL: SOS blocks',[len(b)for w,b in blocks],'unknowns',n,'status',sol.status,'margin',sol.x[-1],flush=True)
    Path('cubic_sos_attempt.json').write_text(json.dumps(dict(label='NUMERICAL',status=str(sol.status),margin=sol.x[-1],block_sizes=[len(b)for w,b in blocks]),indent=2)+'\n')
    if sol.x[-1]<-1e-8:return
    # Compute one exact right inverse on independent rows/columns for repairs.
    _,cols=E.rref();Ep=E[:,list(cols)];_,rows=Ep.T.rref();inv=Ep[list(rows),:].inv()
    for digits in (7,10,13,16):
        x=s.Matrix([s.Rational(round(v*10**digits),10**digits)for v in sol.x[:-1]])
        residual=target/scale-E*x;correction=inv*residual[list(rows),:]
        for j,v in zip(cols,correction):x[j]+=v
        assert E*x==target/scale
        mats=[s.zeros(len(b))for w,b in blocks]
        for v,(bi,i,j)in zip(x,positions):mats[bi][i,j]=mats[bi][j,i]=v
        good=[psd(m)for m in mats]
        print('NUMERICAL: rational repair digits',digits,'exact PSD decisions',good,flush=True)
        if all(good):
            records=[]
            for(w,b),m in zip(blocks,mats):
                records.append(dict(weight=w,basis=[[[list(mon),str(c)]for mon,c in bb.items()]for bb in b],matrix=[[str(v)for v in m.row(i)]for i in range(m.rows)]))
            Path('cubic_sos.json').write_text(json.dumps(dict(label='PROVED',scale=str(scale),blocks=records),indent=2)+'\n')
            with open('LOG.md','a')as f:f.write('\nPROVED (cubic_sos.json; verify_cubic_sos.py): exact rational orthant SOS of d^2+3/2-3A established after sorting the zero-sum vector. Every coefficient matched and every Gram matrix PSD by rational elimination.\n')
            print('PROVED: exact cubic-moment sextic SOS exported',flush=True);return
    with open('LOG.md','a')as f:f.write('\nOPEN: Higher-degree scalar cubic-moment SOS numerical discovery failed rational PSD acceptance. No inequality is promoted to PROVED. See cubic_sos_attempt.json.\n')
if __name__=='__main__':main()
