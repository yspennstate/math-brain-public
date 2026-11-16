"""NUMERICAL: one-thread conic discovery; export only rationally checked cells."""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','VECLIB_MAXIMUM_THREADS','MKL_NUM_THREADS'):
    os.environ[key] = '1'
import argparse
import json
import numpy as np
from scipy import sparse
import clarabel
from fractions import Fraction as F
from moment_bounds import vertices, value, blocks, controls, check

VERTS = vertices()
SETTINGS = clarabel.DefaultSettings()
SETTINGS.max_threads = 1
SETTINGS.verbose = False
SETTINGS.tol_feas = SETTINGS.tol_gap_abs = SETTINGS.tol_gap_rel = 1e-9


def choose(lo, hi, ahi, t, shift):
    alo = F(443,1000)
    # All entries of the conic model are affine in the three multipliers.
    vecs = [(0,)*7]+[tuple(int(i==j) for i in range(7)) for j in range(7)]
    def val(p,a,r,x):
        return value(p,a,r,*x[:3],t,shift,x[3:])
    def blk(r,x):
        return blocks(r,*x[:3],x[3:])
    rows, rhs = [], []
    for p in VERTS:
        for a in (alo,ahi):
            cc = [controls(lambda r: val(p,a,r,x),lo,hi) for x in vecs]
            for j in range(3):
                rows.append([-float(cc[i][j]-cc[0][j]) for i in range(1,8)]+[1.])
                rhs.append(float(cc[0][j]))
    for j in range(7):
        row = [0.]*8
        row[j] = -1.
        rows.append(row)
        rhs.append(0.)
    count = len(rhs)
    cones = [clarabel.NonnegativeConeT(count)]
    for i in range(2):
        vv = [[controls(lambda r: blk(r,x)[i][j],lo,hi) for j in range(3)] for x in vecs]
        for k in range(3):
            soc = [[v[0][k]+v[2][k], v[0][k]-v[2][k], 2*v[1][k]] for v in vv]
            for j in range(3):
                rows.append([-float(soc[n][j]-soc[0][j]) for n in range(1,8)]+[0.])
                rhs.append(float(soc[0][j]))
            cones.append(clarabel.SecondOrderConeT(3))
    sol = clarabel.DefaultSolver(sparse.csc_matrix((8,8)), np.r_[np.zeros(7),-1.],
          sparse.csc_matrix(rows),np.array(rhs),cones,SETTINGS).solve()
    return sol.x[-1], sol.x[:7]


def discover(lo, hi, ahi, quick=False):
    best = None
    ts = [F(k,40) for k in range(20,29)]
    vs = [F(k,20) for k in range(-1,7)]
    if quick:
        ts,vs = [F(k,20) for k in range(10,15)], [F(k,10) for k in range(4)]
    for t in ts:
        for shift in vs:
            margin, x = choose(lo,hi,ahi,t,shift)
            if best is None or margin > best[0]:
                best = margin, x, t, shift
    margin,x,t,shift = best
    for factor in (F(999999,1000000),F(9999,10000),F(999,1000)):
        multipliers = [max(F(0),F(round(v*10**8),10**8))*factor for v in x]
        # Slightly enlarge Bessel penalties: this moves the PSD residual inward.
        multipliers[3:]=[v/factor**2+F(1,10**7) for v in multipliers[3:]]
        rec = dict(rlo=str(lo),rhi=str(hi),alo='443/1000',ahi=str(ahi),
                   theta_n=str(multipliers[0]),theta_j=str(multipliers[1]),
                   theta_d=str(multipliers[2]),tangent=str(t),shift=str(shift),
                   penalties=list(map(str,multipliers[3:])))
        try:
            exact = check(rec,VERTS)
        except AssertionError:
            continue
        rec['margin'] = str(exact)
        return rec
    return None


def main():
    global VERTS
    parser = argparse.ArgumentParser()
    parser.add_argument('--step',type=int,default=2)
    parser.add_argument('--start',type=int,default=15)
    parser.add_argument('--stop',type=int,default=100)
    parser.add_argument('--enhanced',action='store_true')
    parser.add_argument('--output',default='strong_moment_cells.json')
    args = parser.parse_args()
    if args.enhanced:
        VERTS=vertices(enhanced=True)
    print('PROVED: exact polytope vertices',len(VERTS),flush=True)
    records = []
    for k in range(args.start,args.stop,args.step):
        lo,hi=F(k,100),F(min(k+args.step,args.stop),100)
        low,high = 443,650
        winner = None
        while low+1 < high:
            mid=(low+high)//2
            rec=discover(lo,hi,F(mid,1000),quick=True)
            if rec:
                low,winner=mid,rec
            else:
                high=mid
        if winner:
            winner['moment_polytope']='enhanced' if args.enhanced else 'base'
            records.append(winner)
            print('PROVED: cell',lo,hi,'ceiling',winner['ahi'],'margin',winner['margin'],flush=True)
        else:
            print('NUMERICAL: no improved cell',lo,hi,flush=True)
        with open(args.output,'w') as out:
            json.dump(records,out,indent=2)


if __name__=='__main__':
    main()
