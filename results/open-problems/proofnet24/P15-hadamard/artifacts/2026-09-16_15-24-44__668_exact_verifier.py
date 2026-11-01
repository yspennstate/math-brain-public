#!/usr/bin/env python3
"""Exact integer verifier for the August 2026 bordered Goethals-Seidel H(668).

The four subsets are transcribed from the August 2026 preprint
"Two H-inequivalent Hadamard matrices of order 668". We verify the
supplementary difference-family equations, construct the full 668x668 sign
matrix, and check HH^T = 668 I using int64 arithmetic. Every dot product is
a sum of 668 products in {-1,+1}, so int64 arithmetic is exact and cannot
overflow. The final row-major byte hash encodes +1 as 1 and -1 as 0.
"""
import hashlib
import numpy as np

v = 166
X1 = {3,5,7,9,11,12,14,15,19,22,23,24,25,28,29,31,32,33,34,36,37,38,39,40,44,45,46,49,51,52,53,61,63,64,66,68,70,71,74,76,77,79,80,82,83,84,85,87,89,91,93,96,99,100,101,103,104,109,110,113,118,124,125,127,128,129,132,134,135,136,146,147,149,151,153,154,157,159,160,162,163,165}
X2 = {0,1,2,3,7,11,14,16,21,24,26,27,29,30,32,33,34,35,36,37,40,41,43,46,48,50,51,52,54,55,57,59,61,63,64,67,68,69,75,76,77,78,79,87,88,89,91,92,93,95,96,98,100,101,103,105,106,108,111,114,121,123,126,129,131,133,134,135,137,138,140,142,144,146,147,150,151,152,158,159,160,161,162}
X3 = {0,1,2,3,5,7,10,11,12,14,17,18,19,20,22,23,24,30,31,33,34,35,37,38,41,49,51,52,54,55,56,58,59,60,61,64,68,69,70,71,74,75,76,80,81,82,87,89,91,92,96,98,99,104,108,109,110,111,112,115,119,123,132,134,135,137,138,139,141,142,143,144,147,151,152,153,154,157,158,159,163,164,165}
X4 = {3,4,5,7,9,10,13,14,15,16,18,19,21,25,27,28,31,32,33,34,35,36,40,41,48,50,51,54,55,57,60,61,62,64,65,68,69,70,72,73,74,77,78,80,82,83,84,85,89,91,94,95,100,103,105,106,107,109,112,113,120,121,122,131,133,134,137,138,140,144,145,147,148,151,152,153,155,156,157,160,161,163,165}
Xs = [X1, X2, X3, X4]
assert [len(X) for X in Xs] == [82,83,83,83]

def diff_count(X, t):
    return sum(1 for x in X if ((x+t) % v) in X)

diff_sums = [sum(diff_count(X,t) for X in Xs) for t in range(1,v)]
assert min(diff_sums) == max(diff_sums) == 164

def circulant_from_support(X):
    row = np.array([-1 if j in X else 1 for j in range(v)], dtype=np.int64)
    return np.stack([np.roll(row, r) for r in range(v)], axis=0)

A,B,C,D = [circulant_from_support(X) for X in Xs]
R = np.fliplr(np.eye(v, dtype=np.int64))
G = np.block([
    [A,      B@R,       C@R,       D@R],
    [-B@R,   A,         D.T@R,    -C.T@R],
    [-C@R,  -D.T@R,     A,         B.T@R],
    [-D@R,   C.T@R,    -B.T@R,     A],
])
K = np.array([[-1,1,1,-1],[1,-1,1,-1],[1,1,-1,-1],[-1,-1,-1,-1]], dtype=np.int64)
T = np.array([[-1,-1,-1,1],[-1,-1,1,-1],[-1,1,-1,-1],[1,-1,-1,-1]], dtype=np.int64)
S = np.array([[1,1,1,-1],[-1,-1,1,-1],[-1,1,-1,-1],[1,-1,-1,-1]], dtype=np.int64)
one = np.ones((v,1), dtype=np.int64)
H = np.block([
    [K,                    np.kron(T, one.T)],
    [np.kron(S, one),      G],
])
assert H.shape == (668,668)
assert set(np.unique(H).tolist()) == {-1,1}
Gram = H @ H.T
err = Gram - 668*np.eye(668, dtype=np.int64)
max_abs = int(np.max(np.abs(err)))
assert max_abs == 0
payload = bytes((H.reshape(-1) == 1).astype(np.uint8).tolist())
digest = hashlib.sha256(payload).hexdigest()
expected = '19f435b31eb6561dd97356b761e9b0f174824e42c215c33fbafc20f9b1b20744'
assert digest == expected
print('source_order=668')
print('block_sizes=', [len(X) for X in Xs])
print('difference_sum_min=', min(diff_sums))
print('difference_sum_max=', max(diff_sums))
print('H_shape=', H.shape)
print('H_entries=', sorted(np.unique(H).tolist()))
print('max_abs_HHt_minus_668I=', max_abs)
print('sha256_rowmajor_plus1eq1_minus1eq0=', digest)
print('EXACT H(668) VERIFICATION PASSED')
