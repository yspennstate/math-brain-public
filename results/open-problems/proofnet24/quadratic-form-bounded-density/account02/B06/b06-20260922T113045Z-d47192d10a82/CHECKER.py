#!/usr/bin/env python3
from itertools import combinations
from collections import Counter
from fractions import Fraction
import json

def sylvester(k):
    H = [[1]]
    for _ in range(k):
        H = [r+r for r in H] + [r+[-x for x in r] for r in H]
    return H

def matmul(A, B):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B)))
             for j in range(len(B[0]))] for i in range(len(A))]

n = 16
H = sylvester(4)
cols = [[H[i][j] for i in range(n)] for j in range(3)]
gram = [[sum(cols[a][i]*cols[b][i] for i in range(n))
         for b in range(3)] for a in range(3)]
assert gram == [[n,0,0],[0,n,0],[0,0,n]]

# A = M/n = U diag(1,1,-1) U^T, U = first 3 Hadamard columns / sqrt(n).
M = [[cols[0][i]*cols[0][j] + cols[1][i]*cols[1][j]
      - cols[2][i]*cols[2][j] for j in range(n)] for i in range(n)]

M2 = matmul(M, M)
M3 = matmul(M2, M)
assert all(M3[i][j] == n*n*M[i][j] for i in range(n) for j in range(n))
assert Fraction(sum(M[i][i] for i in range(n)), n) == 1
assert Fraction(sum(M2[i][i] for i in range(n)), n*n) == 3

dets = []
for i,j in combinations(range(n), 2):
    detnum = M[i][i]*M[j][j] - M[i][j]*M[j][i]
    dets.append(detnum)
assert all(d <= 0 for d in dets)

# Positive rank-two same-sign spectral component.
P = [[cols[0][i]*cols[0][j] + cols[1][i]*cols[1][j]
      for j in range(n)] for i in range(n)]
pos_dets = []
for i,j in combinations(range(n), 2):
    pos_dets.append(P[i][i]*P[j][j] - P[i][j]*P[j][i])
assert Fraction(sum(pos_dets), n*n) == 1

result = {
    "status": "PASS",
    "n": n,
    "gram_first3": gram,
    "A_spectrum_certificate": {
        "M3_equals_n2M": True,
        "trace_A": str(Fraction(sum(M[i][i] for i in range(n)), n)),
        "trace_A2": str(Fraction(sum(M2[i][i] for i in range(n)), n*n)),
        "conclusion": "eigenvalues exactly +1,+1,-1, then zeros"
    },
    "full_A_2x2_principal_det_numerators": dict(sorted(Counter(dets).items())),
    "all_full_A_2x2_principal_determinants_nonpositive": True,
    "same_sign_rank2_det_mass": str(Fraction(sum(pos_dets), n*n)),
    "same_sign_rank2_det_numerator_counts": dict(sorted(Counter(pos_dets).items())),
    "row_leverage_first3": f"3/{n}",
    "compression_bound": "for every coordinate S, |S|=m: ||A_SS||op <= 3m/n"
}
print(json.dumps(result, sort_keys=True, indent=2))
