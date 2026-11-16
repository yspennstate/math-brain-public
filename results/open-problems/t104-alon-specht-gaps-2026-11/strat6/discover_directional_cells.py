"""NUMERICAL: perspective-conic discovery, then exact rational certification."""
import os
for key in('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','VECLIB_MAXIMUM_THREADS','MKL_NUM_THREADS'):
    os.environ[key]='1'
import argparse
import json
from fractions import Fraction as F
import numpy as np
from scipy import sparse
import clarabel
from moment_bounds import vertices,controls
from directional_bounds import DIRECTIONS,lower_value,residual_blocks,check

COUNT=5*len(DIRECTIONS)+5
SETTINGS=clarabel.DefaultSettings()
SETTINGS.max_threads=1
SETTINGS.verbose=False
SETTINGS.tol_feas=SETTINGS.tol_gap_abs=SETTINGS.tol_gap_rel=1e-10
SETTINGS.max_iter=150


def solve(verts,lo,hi,ahi,d_zero=False):
    alo=F(443,1000)
    units=[tuple(F(0)for _ in range(COUNT))]
    units += [tuple(F(int(i==j))for i in range(COUNT))for j in range(COUNT)]
    rows,rhs=[],[]
    for p in verts:
        for a in(alo,ahi):
            cc=[controls(lambda r:lower_value(p,a,r,x),lo,hi)for x in units]
            for j in range(3):
                rows.append([-float(cc[i][j]-cc[0][j])for i in range(1,COUNT+1)]+[1.])
                rhs.append(float(cc[0][j]))
    # theta_d and all Bessel penalties are nonnegative.
    for i in range(5*len(DIRECTIONS),COUNT):
        row=[0.]*(COUNT+1)
        row[i]=-1.
        rows.append(row)
        rhs.append(0.)
    cones=[clarabel.NonnegativeConeT(len(rhs))]
    for block in range(2):
        bb=[[controls(lambda r:residual_blocks(r,x,d_zero)[block][j],lo,hi)for j in range(3)]for x in units]
        for k in range(3):
            soc=[[v[0][k]+v[2][k],v[0][k]-v[2][k],2*v[1][k]]for v in bb]
            for j in range(3):
                rows.append([-float(soc[n][j]-soc[0][j])for n in range(1,COUNT+1)]+[0.])
                rhs.append(float(soc[0][j]))
            cones.append(clarabel.SecondOrderConeT(3))
    # Perspective cones enforce theta*c>=q^2 and theta*d>=v^2.
    for i in range(len(DIRECTIONS)):
        for k,l in[(2,1),(4,3)]:
            for coeff in[(1,1,0),(1,-1,0),(0,0,2)]:
                row=[0.]*(COUNT+1)
                row[5*i]=-coeff[0]
                row[5*i+k]=-coeff[1]
                row[5*i+l]=-coeff[2]
                rows.append(row)
                rhs.append(0.)
            cones.append(clarabel.SecondOrderConeT(3))
    sol=clarabel.DefaultSolver(sparse.csc_matrix((COUNT+1,COUNT+1)),
         np.r_[np.zeros(COUNT),-1.],sparse.csc_matrix(rows),np.array(rhs),cones,SETTINGS).solve()
    return sol


def discover(verts,lo,hi,ahi,d_zero=False):
    sol=solve(verts,lo,hi,ahi,d_zero)
    if sol.x[-1]<-1e-8:
        return None
    for factor in(F(999999,1000000),F(9999,10000),F(999,1000)):
        directions=[]
        for i in range(len(DIRECTIONS)):
            theta=max(F(0),F(round(sol.x[5*i]*10**9),10**9))
            if theta<F(1,10**8):
                theta,t,v=F(0),F(0),F(0)
            else:
                q=F(round(sol.x[5*i+1]*10**9),10**9)
                vv=F(round(sol.x[5*i+3]*10**9),10**9)
                t,v=q/theta,vv/theta
            directions.append(dict(theta=str(theta*factor),tangent=str(t),shift=str(v)))
        offset=5*len(DIRECTIONS)
        td=max(F(0),F(round(sol.x[offset]*10**9),10**9))*factor
        penalties=[max(F(0),F(round(v*10**9),10**9))/factor+F(1,10**7)for v in sol.x[offset+1:offset+5]]
        rec=dict(rlo=str(lo),rhi=str(hi),alo='443/1000',ahi=str(ahi),
                 theta_d=str(td),penalties=list(map(str,penalties)),directions=directions)
        if d_zero:
            rec['basis_d_zero']=True
        try:
            margin=check(rec,verts)
        except AssertionError:
            continue
        rec['margin']=str(margin)
        return rec
    return None


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--step',type=int,default=2)
    parser.add_argument('--start',type=int,default=12)
    parser.add_argument('--stop',type=int,default=100)
    parser.add_argument('--equal-gap-only',action='store_true')
    args=parser.parse_args()
    if args.equal_gap_only:
        verts=vertices(enhanced=True,extra=[((1,0,0),F(1,2))])
        low,high=443,1001
        best=None
        while low+1<high:
            mid=(low+high)//2
            candidate=discover(verts,F(1),F(1),F(mid,1000),d_zero=True)
            if candidate:
                low,best=mid,candidate
            else:
                high=mid
        assert best is not None
        with open('equal_gap_cell.json','w')as out:
            json.dump([best],out,indent=2)
        print('PROVED: basis-rotated equal-gap ceiling',best['ahi'],'margin',best['margin'],flush=True)
        return
    verts=vertices(enhanced=True)
    records=[]
    for j in range(args.start,args.stop,args.step):
        lo,hi=F(j,100),F(min(j+args.step,args.stop),100)
        low,high=443,950
        best=None
        while low+1<high:
            mid=(low+high)//2
            candidate=discover(verts,lo,hi,F(mid,1000))
            if candidate:
                low,best=mid,candidate
            else:
                high=mid
        if best:
            records.append(best)
            print('PROVED: directional cell',lo,hi,'ceiling',best['ahi'],'margin',best['margin'],flush=True)
        else:
            print('NUMERICAL: unresolved cell',lo,hi,flush=True)
        with open('directional_moment_cells.json','w')as out:
            json.dump(records,out,indent=2)


if __name__=='__main__':
    main()
