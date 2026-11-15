"""NUMERICAL discovery followed by exact repair and PSD certification.

Use: python3 sextic_endpoint_certificate.py 1/5
All files are written to the current working directory.
"""
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
from exact_endpoint import construct


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
    ratio = F(sys.argv[1])
    _, poly = construct(ratio)
    coeff = {}
    for mon, c in poly.terms():
        assert sum(mon[:4]) == 12 and sum(mon[4:]) == 6
        coeff.setdefault(mon[:4], {})[mon[4:]] = F(int(c.numerator), int(c.denominator))
    mons = [(i, j, 3-i-j) for i in range(3, -1, -1) for j in range(3-i, -1, -1)]
    pairs = [(i, j) for j in range(10) for i in range(j+1)]
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
    cones = [clarabel.ZeroConeT(len(exps)), clarabel.PSDTriangleConeT(10)]
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
            mat = [[F(0)]*10 for _ in range(10)]
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
    filename = 'sextic_endpoint_'+str(ratio.numerator)+'_'+str(ratio.denominator)+'.json'
    with open(filename, 'w') as out:
        json.dump(dict(r=str(ratio), monomials=mons, records=records, failed=failed), out, indent=2)
    print('PROVED: exact PSD forms', len(records), 'NUMERICAL: unresolved', len(failed), flush=True)
    return bool(failed)


if __name__ == '__main__':
    sys.exit(main())
