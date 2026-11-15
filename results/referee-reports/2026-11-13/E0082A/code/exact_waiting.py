"""Finite pattern calculations. Run with BLAS thread counts set to one.

Rational matching calculations are exact. Larger matching and independent
sliding-window Markov-chain calculations solve the exact equations in float64.
"""
import os
for key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS',
            'VECLIB_MAXIMUM_THREADS', 'NUMEXPR_NUM_THREADS'):
    os.environ[key] = '1'
import csv
import math
from pathlib import Path
import numpy as np
import sympy as sp
from scipy.sparse import coo_matrix
from scipy.sparse.linalg import spsolve


def level(alpha, n):
    a = math.floor(alpha * math.sqrt(n))
    return a if (a-n) % 2 == 0 else a+1


def patterns(n, a, family):
    out = []
    for word in range(1 << n):
        if 2*word.bit_count()-n != a:
            continue
        if family == 'FP':
            s = 0
            valid = a < 0
            for i in range(n):
                if s <= a:
                    valid = False
                    break
                s += 1 if (word >> (n-1-i)) & 1 else -1
            if not valid:
                continue
        out.append(word)
    return out


def matching(n, words):
    """Integer leading-number matrix C = 2**n M, source orientation."""
    w = np.asarray(words, dtype=np.int64)
    c = np.zeros((len(w), len(w)), dtype=np.int64)
    for ell in range(n):
        mask = (1 << (n-ell))-1
        c += ((w[:, None] >> ell) == (w[None, :] & mask)) * (1 << (n-ell))
    return c


def prefix_markov(n, words):
    """States: last n-1 letters. No pattern can have ended before step n."""
    size = 1 << (n-1)
    mask = size-1
    accept = set(words)
    rows, cols, vals = list(range(size)), list(range(size)), [1.0]*size
    for s in range(size):
        for b in (0, 1):
            v = (s << 1) | b
            if v not in accept:
                rows.append(s)
                cols.append(v & mask)
                vals.append(-0.5)
    mat = coo_matrix((vals, (rows, cols)), shape=(size, size)).tocsc()
    h = spsolve(mat, np.ones(size))
    return n-1+float(h.mean()), float(np.max(np.abs(mat@h-1)))


def main():
    records = []
    for n in (2, 3, 4, 5, 6, 7, 8, 10, 12):
        for family, alpha in [('BR', 0.0), ('BR', 1.0), ('FP', -1.0)]:
            a = level(alpha, n)
            words = patterns(n, a, family)
            if not words:
                continue
            c = matching(n, words)
            x = np.linalg.solve(c.astype(float), np.ones(len(words)))
            et = 1 / float(x.sum())
            p = x*et
            # Explicit contractions avoid spurious Accelerate matmul FPE flags
            # seen on this Mac despite finite, independently verified outputs.
            residual = float(np.max(np.abs(np.einsum('ij,j->i',c,p)-et)))
            markov, mr = prefix_markov(n, words)
            rational = ''
            if n <= 8:
                # Fraction-free exact inverse-vector calculation.
                xx = sp.polys.matrices.DomainMatrix.from_Matrix(sp.Matrix(c.tolist()))
                bb = sp.polys.matrices.DomainMatrix.from_Matrix(sp.ones(len(words), 1))
                num, den = xx.inv_den()
                sol = (num * bb).to_Matrix()
                rational = str(sp.Rational(den, sum(sol)))
                assert abs(float(sp.Rational(rational))-et) < 1e-9
            expected_count = math.comb(n, (n+a)//2)
            if family == 'FP':
                expected_count = expected_count*(-a)//n
            assert len(words) == expected_count
            assert abs(markov-et) < 2e-9*et
            assert p.min() > -1e-10
            col = c.sum(axis=0)/(1 << n)
            weighted = float(np.einsum('i,i->',col,p))
            assert math.isfinite(residual) and math.isfinite(weighted)
            assert abs(weighted-len(words)*et/(1 << n)) < 1e-9*et
            row = dict(n=n, family=family, alpha=alpha, level=a, patterns=len(words),
                       exact_rational=rational, matching_mean=et, markov_mean=markov,
                       mean_over_n=et/n, equation_residual=residual, markov_residual=mr,
                       hit_weighted_column=weighted, uniform_column=float(col.mean()))
            records.append(row)
            print(n, family, a, len(words), rational or f'{et:.12g}', flush=True)
    dest = Path('data/exact_waiting.csv')
    with dest.open('w') as f:
        writer = csv.DictWriter(f, fieldnames=records[0].keys())
        writer.writeheader()
        writer.writerows(records)


if __name__ == '__main__':
    main()
