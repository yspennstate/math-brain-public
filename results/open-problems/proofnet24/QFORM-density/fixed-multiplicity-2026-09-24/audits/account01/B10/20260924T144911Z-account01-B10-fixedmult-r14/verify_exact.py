#!/usr/bin/env python3
"""account01/B10 r14 exact finite diagnostics; not a proof certificate."""
from fractions import Fraction
from itertools import combinations
import json
import sympy as sp


def atanh_log_upper(z: Fraction, m: int) -> Fraction:
    # log((1+z)/(1-z)); bound tail using 1/(2k+1)<=1/(2m+3).
    s = Fraction(0)
    for k in range(m + 1):
        s += 2 * z ** (2 * k + 1) / (2 * k + 1)
    return s + 2 * z ** (2 * m + 3) / ((2 * m + 3) * (1 - z * z))


def volume(A: sp.Matrix, r: int):
    n = A.rows
    total = sp.Integer(0)
    for S in combinations(range(n), r):
        rem = [x for x in range(n) if x not in S]
        for T in combinations(rem, r):
            total += A.extract(S, T).det() ** 2
    return sp.expand(total)


def sampling_weighted(A: sp.Matrix, r: int):
    n = A.rows
    vr = volume(A, r)
    vr1 = volume(A, r + 1)
    weighted = sp.Integer(0)
    seeds = 0
    for S in combinations(range(n), r):
        rem = [x for x in range(n) if x not in S]
        for T in combinations(rem, r):
            B = A.extract(S, T)
            det = B.det()
            if det == 0:
                continue
            L = [x for x in range(n) if x not in S and x not in T]
            P = A[:, T] * B.inv() * A.extract(S, range(n))
            F2 = sp.Integer(0)
            for ell in L:
                for m in L:
                    if ell != m:
                        F2 += (A[ell, m] - P[ell, m]) ** 2
            weighted += det ** 2 * F2
            seeds += 1
    return vr, vr1, weighted, seeds


def completion(A: sp.Matrix, S, T):
    n = A.rows
    L = [i for i in range(n) if i not in S and i not in T]
    B = A.extract(S, T)
    P = A[:, T] * B.inv() * A.extract(S, range(n))
    E = sp.zeros(n)
    D = sp.zeros(n)
    for i in L:
        D[i, i] = A[i, i] - P[i, i]
        for j in L:
            if i != j:
                E[i, j] = A[i, j] - P[i, j]
    R = A - D - E
    return B, P, D, E, R, L


# Fejer coefficient fourth-power rational upper bound using pi<22/7, e<11/4.
cf4_upper = Fraction(2500, 2209) ** 4 * Fraction(16, 21) ** 4 * Fraction(5, 6) * Fraction(242, 7)
assert cf4_upper < 16
cf4_margin = Fraction(16) - cf4_upper

log2_upper = atanh_log_upper(Fraction(1, 3), 2)
log3_upper = atanh_log_upper(Fraction(1, 2), 4)
assert log2_upper == Fraction(23581, 34020)
assert log3_upper == Fraction(487259, 443520)
C0_upper = 2 * log3_upper + Fraction(37, 14) * log2_upper
assert C0_upper < Fraction(403, 100)

# r=2 simultaneous rank sharpness in the no-pivot regime.
A0 = sp.Matrix([
    [1,1,-2,0,2,1], [1,1,0,1,0,2], [-2,0,-1,2,-1,0],
    [0,1,2,-1,-2,2], [2,0,-1,-2,0,2], [1,2,0,2,2,2],
])
A2 = A0 / 1000
B, P, D, E, R, L = completion(A2, [0,1], [2,3])
max_diag = max(abs(A2[i,i]) for i in range(6))
max_principal_det = max(abs(A2.extract([i,j],[i,j]).det()) for i in range(6) for j in range(i+1,6))
assert max_diag == sp.Rational(1, 500)
assert max_principal_det == sp.Rational(3, 500000)
assert B.det() == -sp.Rational(1, 500000)
assert R.rank() == 6 and R.extract(L,L).rank() == 2

# Singular r=2 seed with a nonsingular one-step extension.
Asing = sp.Matrix([
    [-1,2,-2,0,-2,1], [2,1,1,1,-1,-2], [-2,1,1,-2,1,1],
    [0,1,-2,2,-2,1], [-2,-1,1,-2,0,-1], [1,-2,1,1,-1,2],
])
S, T = [0,3], [2,4]
assert Asing.extract(S,T).det() == 0
assert Asing.extract(sorted(S+[5]), sorted(T+[1])).det() == 4

# Higher-order finite sampling diagnostics omitted by root verify.py.
A3 = sp.Matrix([
[-2,-2,0,-1,-1,-1,-2,2],[-2,-2,2,1,-2,-2,-2,-1],[0,2,-1,2,2,-2,2,-1],[-1,1,2,2,1,-1,1,2],
[-1,-2,2,1,0,-2,-1,1],[-1,-2,-2,-1,-2,0,0,-1],[-2,-2,2,1,-1,0,-1,0],[2,-1,-1,2,1,-1,0,-2],
])
A4 = sp.Matrix([
[-2,1,-2,0,0,2,0,-2,1,2],[1,-2,1,-2,2,0,2,0,2,-1],[-2,1,-2,-2,-1,0,-2,-1,-2,1],[0,-2,-2,0,1,0,-1,0,0,-1],
[0,2,-1,1,0,-2,2,-1,2,-1],[2,0,0,0,-2,-1,1,1,0,2],[0,2,-2,-1,2,1,-1,0,-2,-1],[-2,0,-1,0,-1,1,0,-2,0,1],
[1,2,-2,0,2,0,-2,0,0,-2],[2,-1,1,-1,-1,2,-1,1,-2,-1],
])
vr3, vr4, w3, seeds3 = sampling_weighted(A3, 3)
vr4b, vr5, w4, seeds4 = sampling_weighted(A4, 4)
assert (vr3, vr4, w3, seeds3) == (33892, 24552, 356740, 498)
assert 16 * vr4 - w3 == 36092
assert (vr4b, vr5, w4, seeds4) == (982996, 838608, 20125054, 2706)
assert 25 * vr5 - w4 == 840146

result = {
    "status": "PASS",
    "scope": "finite exact diagnostics only; not a proof certificate",
    "fejer_cf4_upper": str(cf4_upper),
    "fejer_margin_to_16": str(cf4_margin),
    "log2_upper": str(log2_upper),
    "log3_upper": str(log3_upper),
    "C0_upper": str(C0_upper),
    "r2_rank_sharpness": {"rank_R": R.rank(), "rank_R_LL": R.extract(L,L).rank(), "max_diag": str(max_diag), "max_principal_2det": str(max_principal_det)},
    "singular_seed_extension_det": 4,
    "r3_sampling": {"V3": int(vr3), "V4": int(vr4), "weighted": int(w3), "seeds": seeds3, "slack": int(16*vr4-w3)},
    "r4_sampling": {"V4": int(vr4b), "V5": int(vr5), "weighted": int(w4), "seeds": seeds4, "slack": int(25*vr5-w4)},
}
print(json.dumps(result, indent=2))
