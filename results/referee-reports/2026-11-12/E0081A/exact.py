#!/usr/bin/env python3
"""Exact rational matching-matrix values; independent prefix-automaton check.

Run with OPENBLAS_NUM_THREADS=1 for the floating automaton linear solves.
"""
import argparse
import csv
import itertools
import math
from fractions import Fraction as F
from pathlib import Path
import numpy as np


def words(n, a):
    out = []
    for plus in itertools.combinations(range(n), (n-a)//2):
        w = [-1]*n
        for i in plus:
            w[i] = 1
        heights = list(itertools.accumulate(w, initial=0))
        if min(heights[:-1]) > -a:
            out.append(tuple(w))
    return out


def rational_solve(matrix, rhs):
    b = [list(map(F, row))+[F(y)] for row, y in zip(matrix, rhs)]
    k = len(b)
    for i in range(k):
        pivot = next(j for j in range(i, k) if b[j][i])
        b[i], b[pivot] = b[pivot], b[i]
        d = b[i][i]
        b[i] = [v/d for v in b[i]]
        for j in range(i+1, k):
            d = b[j][i]
            if d:
                for l in range(i+1, k+1):
                    b[j][l] -= d*b[i][l]
                b[j][i] = F(0)
    x = [F(0)]*k
    for i in reversed(range(k)):
        x[i] = b[i][-1]-sum(b[i][j]*x[j] for j in range(i+1, k))
    return x


def matching(w):
    n = len(w[0])
    m = [[sum((F(1, 2**s) for s in range(n) if u[:n-s] == v[s:]), F(0))
          for v in w] for u in w]
    x = rational_solve(m, [1]*len(w))
    return F(2**n)/sum(x)


def automaton(w):
    targets = set(w)
    prefixes = sorted({u[:j] for u in w for j in range(len(u))}, key=lambda u:(len(u),u))
    index = {u:i for i,u in enumerate(prefixes)}
    mat = np.eye(len(prefixes))
    for i,u in enumerate(prefixes):
        for bit in [-1,1]:
            v = u+(bit,)
            if v in targets:
                continue
            while v not in index:
                v = v[1:]
            mat[i,index[v]] -= .5
    return np.linalg.solve(mat,np.ones(len(prefixes)))[0],len(prefixes)


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--max-n',type=int,default=12)
    ap.add_argument('--out',default='data/exact.csv');args=ap.parse_args()
    Path(args.out).parent.mkdir(exist_ok=True)
    with open(args.out,'w') as f:
        wr=csv.writer(f);wr.writerow(['n','a','patterns','exact_ET','ET','automaton_ET','automaton_states','absolute_difference'])
        for n in range(2,args.max_n+1):
            endpoint=math.ceil(-math.sqrt(n))
            if (endpoint-n)%2: endpoint+=1
            a=-endpoint
            if not (0<a<=n): continue
            w=words(n,a)
            assert len(w)==a*math.comb(n,(n-a)//2)//n
            value=matching(w);other,k=automaton(w)
            assert abs(float(value)-other)<1e-8*float(value)
            row=[n,a,len(w),str(value),float(value),other,k,abs(float(value)-other)]
            wr.writerow(row);f.flush();print(row,flush=True)


if __name__=='__main__':main()
