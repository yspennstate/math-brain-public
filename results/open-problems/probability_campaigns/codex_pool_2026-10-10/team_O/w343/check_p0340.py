"""Finite deterministic and exact-distribution checks; writes only beside this file."""
import json
import math
import os
import time
from pathlib import Path

os.environ['OPENBLAS_NUM_THREADS'] = '1'
import numpy as np

start = time.perf_counter()
root = Path(__file__).resolve().parent
trees = {1: [(0, 0, 0, 0, 1.0)]}  # height, depth sum, length, subtree-height sum, weight
counts = []
checks = 0
for n in range(2, 11):
    hn = sum(1 / j for j in range(1, n))
    rows = []
    for i in range(1, n):
        q = n / (2 * hn * i * (n-i))
        for hl, dl, ll, sl, pl in trees[i]:
            for hr, dr, lr, sr, pr in trees[n-i]:
                h = 1 + max(hl, hr)
                d = dl + dr + n
                length = ll + lr + 2 + abs(hl-hr)
                s = sl + sr + h
                assert length == s + h
                assert 2*(n-1) <= length <= d
                assert h <= n-1
                rows.append((h, d, length, s, q*pl*pr))
                checks += 1
    trees[n] = rows
    expected_count = math.comb(2*n-2, n-1)//n
    assert len(rows) == expected_count
    assert abs(sum(x[4] for x in rows)-1) < 3e-13
    counts.append({'n': n, 'ordered_trees': len(rows)})

N = 128
grid = np.arange(N)
F = np.ones((N+1, N))
H = np.zeros(N+1)
L = np.zeros(N+1)
D = np.zeros(N+1)
max_split_error = 0.0
for n in range(2, N+1):
    harmonic = sum(1/j for j in range(1, n))
    cdf = np.zeros(N)
    L[n] = D[n] = 0.0
    qsum = 0.0
    for i in range(1, n):
        j = n-i
        q = n/(2*harmonic*i*j)
        qsum += q
        cdf[1:] += q*F[i, :-1]*F[j, :-1]
        min_height = float(np.sum((1-F[i])*(1-F[j])))
        abs_difference = H[i]+H[j]-2*min_height
        L[n] += q*(L[i]+L[j]+2+abs_difference)
        D[n] += q*(D[i]+D[j]+n)
    max_split_error = max(max_split_error, abs(qsum-1))
    cdf = np.clip(cdf, 0, 1)
    cdf[n-1:] = 1.0
    F[n] = cdf
    H[n] = float(np.sum(1-cdf))
    assert 2*(n-1)-1e-8 <= L[n] <= D[n]+1e-8
    if n <= 10:
        exact_l = sum(x[2]*x[4] for x in trees[n])
        exact_h = sum(x[0]*x[4] for x in trees[n])
        assert abs(L[n]-exact_l) < 3e-11
        assert abs(H[n]-exact_h) < 3e-11

A = np.zeros((N+1,N+1))
A[1,1] = 1.0
for n in range(2,N+1):
    harmonic=sum(1/j for j in range(1,n))
    weights=np.array([1/(harmonic*(n-j)) for j in range(1,n)])
    A[n]=weights @ A[1:n]
    A[n,n]=1.0
    identity=float(np.sum(A[n,2:n+1]*H[2:n+1]/np.arange(2,n+1)))+H[n]/n
    assert abs(identity-L[n]/n)<1e-10
    clades=float(np.sum(n*A[n,2:n+1]/np.arange(2,n+1)))
    assert abs(clades-(n-1))<1e-10
block_checks=0
for n in range(2,N+1):
    for b in [1,2,4,8,16,32,64]:
        bound=2*sum(1/j for j in range(1,2*b))
        assert float(np.sum(A[n,b+1:min(2*b,N)+1]))<=bound+1e-11
        block_checks+=1
height_bounds=[]
for n in [2,4,8,16,32,64,128]:
    harmonic=sum(1/j for j in range(1,n))
    p=1/(2*harmonic)
    b=math.ceil(math.log2(n))
    theta=-math.log1p(-p/2)
    moment=np.ones(n+1)
    for m in range(2,n+1):
        hm=sum(1/j for j in range(1,m))
        moment[m]=math.exp(theta)*sum(moment[j]/(hm*(m-j)) for j in range(1,m))
        halving=sum(1/(hm*(m-j)) for j in range(1,m//2+1))
        assert halving>=1/(2*hm)-1e-13
    assert moment[n]<=2**b+1e-9
    new=(math.log(n)+b*math.log(2))/theta
    old=(4/p)*(math.log(n)+b*math.log(3)+1)
    assert H[n]<=new+1e-10 and new<=old
    height_bounds.append(dict(n=n, actual_mean_height=float(H[n]),
                              prior_proof_bound=old, tightened_bound=new,
                              bound_reduction_percent=100*(1-new/old)))

out = {
    'command': 'python -X utf8 ~/brain_workers/w343/check_p0340.py',
    'label': 'finite checks and numerical evidence; no asymptotic inference',
    'trees_checked': checks+1, 'identity_failures': 0,
    'inequality_failures': 0, 'tree_counts': counts,
    'split_probability_max_error': max_split_error,
    'recursion_enumeration_comparison': 'matches for n=2..10 within 3e-11',
    'occupation_tree_identity_checks': N-1,
    'dyadic_occupation_checks': block_checks,
    'height_bound_comparison': height_bounds,
    'expectations': [dict(n=n, expected_length=float(L[n]), length_per_leaf=float(L[n]/n),
                          expected_height=float(H[n]), expected_depth_sum=float(D[n]))
                     for n in [1,2,4,8,16,32,64,128]],
    'elapsed_seconds': time.perf_counter()-start,
}
root.joinpath('measurement_p0340.json').write_text(json.dumps(out, indent=2), encoding='utf-8')
print(json.dumps(out, indent=2))
