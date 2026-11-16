"""NUMERICAL: discover a universal normalized concavity SOS certificate."""
import os
for key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS',
            'VECLIB_MAXIMUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[key] = '1'
import json
import sys
from fractions import Fraction as F
import numpy as np
from scipy import sparse
import clarabel
from exact_endpoint import ingredients
from sympy.polys.rings import ring
from sympy.polys.domains import QQ


def psd(mat):
    while mat:
        pivot = mat[0][0]
        if pivot < 0:
            return False
        if pivot == 0:
            if any(mat[0]):
                return False
            mat = [row[1:] for row in mat[1:]]
        else:
            mat = [[mat[i][j]-mat[i][0]*mat[0][j]/pivot
                    for j in range(1, len(mat))] for i in range(1, len(mat))]
    return True


def main():
    base,U,W,t,n,Lu,Lw,P,Q,R = ingredients()
    outer,*gens=ring('z0,z1,z2,z3,x0,x1,x2,v0,v1',QQ)
    def lift(p):
        return outer.from_dict({m+(0,0):c for m,c in p.terms()})
    v0,v1=gens[-2:]
    poly=-lift(P-t*n*Lu/2)*v0*v0-lift(Q-t*n*(Lu+Lw)/2)*v0*v1-lift(R-t*n*Lw/2)*v1*v1
    coeff = {}
    for mon, c in poly.terms():
        assert sum(mon[:4]) == 12 and sum(mon[4:7]) == 6 and sum(mon[7:])==2
        coeff.setdefault(mon[:4], {})[mon[4:]] = F(int(c.numerator), int(c.denominator))
    mons = [(i,j,3-i-j,k,1-k) for i in range(3,-1,-1)
            for j in range(3-i,-1,-1) for k in range(2)]
    size=len(mons)
    pairs = [(i, j) for j in range(size) for i in range(j+1)]
    exps = sorted({tuple(a+b for a, b in zip(mons[i], mons[j])) for i, j in pairs})
    eq = np.zeros((len(exps), len(pairs)))
    sv = np.zeros((len(pairs), len(pairs)))
    for k, (i, j) in enumerate(pairs):
        m = tuple(a+b for a, b in zip(mons[i], mons[j]))
        eq[exps.index(m), k] = 1 if i == j else 2
        sv[k, k] = 1 if i == j else np.sqrt(2.)
    matrix = np.vstack((eq, -sv))
    diag = np.r_[np.zeros(len(exps)), [1. if i == j else 0. for i, j in pairs]]
    matrix = sparse.csc_matrix(np.column_stack((matrix, diag)))
    objective = np.r_[np.zeros(len(pairs)), -1.]
    cones = [clarabel.ZeroConeT(len(exps)), clarabel.PSDTriangleConeT(size)]
    settings = clarabel.DefaultSettings()
    settings.max_threads = 1
    settings.verbose = False
    settings.tol_feas = settings.tol_gap_abs = settings.tol_gap_rel = 1e-10
    settings.max_iter = 100
    records, failed = [], []
    for number, (zz, ct) in enumerate(sorted(coeff.items())):
        scale = max(abs(c) for c in ct.values())
        rhs = np.r_[[float(ct.get(m, 0)/scale) for m in exps], np.zeros(len(pairs))]
        sol = clarabel.DefaultSolver(sparse.csc_matrix((len(objective), len(objective))),
                                    objective, matrix, rhs, cones, settings).solve()
        accepted = None
        for digits in (7, 10, 13):
            vals = [F(round(v*10**digits), 10**digits) for v in sol.x[:-1]]
            for m in exps:
                indices = [k for k, (i, j) in enumerate(pairs)
                           if tuple(a+b for a, b in zip(mons[i], mons[j])) == m]
                k = indices[0]
                cur = sum((1 if pairs[k0][0] == pairs[k0][1] else 2)*vals[k0] for k0 in indices)
                vals[k] += (ct.get(m, 0)/scale-cur)/(1 if pairs[k][0] == pairs[k][1] else 2)
            mat = [[F(0)]*size for _ in range(size)]
            for value, (i, j) in zip(vals, pairs):
                mat[i][j] = mat[j][i] = value
            if psd(mat):
                accepted = mat
                break
        if accepted is None:
            failed.append(list(zz))
            if len(failed) <= 5:
                print('NUMERICAL: unresolved coefficient', zz, sol.status, sol.x[-1], flush=True)
        else:
            records.append(dict(monomial=zz, scale=str(scale), matrix=[[str(v) for v in row] for row in accepted]))
        if (number+1) % 50 == 0:
            print('PROVED: PSD forms', len(records), 'NUMERICAL: unresolved', len(failed), flush=True)
    filename = 'concavity_matrices.json'
    with open(filename, 'w') as out:
        json.dump(dict(monomials=mons, records=records, failed=failed), out, indent=2)
    print('PROVED: exact PSD forms', len(records), 'NUMERICAL: unresolved', len(failed), flush=True)
    return bool(failed)


if __name__ == '__main__':
    sys.exit(main())
