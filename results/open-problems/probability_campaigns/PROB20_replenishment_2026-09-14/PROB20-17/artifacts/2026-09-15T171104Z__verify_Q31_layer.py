"""PROB20-17 run verifier: sharp Q31 layer and improved n=4 constant.

The numerical tests below are corroborative only.  The mathematical proof is in
runs/2026-09-15/2026-09-15T171104Z__report.md.
"""

import itertools
from collections import Counter
import math
import numpy as np


def opnorm(M):
    return np.linalg.svd(M, compute_uv=False)[0]


def rand_psd(d, rng):
    Q, _ = np.linalg.qr(rng.normal(size=(d, d)))
    vals = np.exp(rng.uniform(-4.0, 3.0, size=d))
    return Q @ np.diag(vals) @ Q.T


# ------------------------------------------------------------
# 1. Scalar optimization from the report
# ------------------------------------------------------------

def quartic(x):
    return x**4 - 6*x - 3

lo, hi = 1.0, 3.0
for _ in range(200):
    mid = (lo + hi) / 2
    if quartic(mid) < 0:
        lo = mid
    else:
        hi = mid
xstar = (lo + hi) / 2
estar = xstar**2
Fstar = 6 + 2/xstar + 1/(2*estar) + estar/6
cstar = 3*Fstar/32

print("x* =", xstar)
print("e* =", estar)
print("R/S lower constant =", Fstar)
print("normalized lower factor =", cstar)

assert abs(xstar - 1.9600874554733903) < 1e-13
assert abs(estar - 3.84194283310415) < 1e-13
assert abs(Fstar - 7.7908289283058305) < 1e-13
assert abs(cstar - 0.7303902120286716) < 1e-13


# ------------------------------------------------------------
# 2. Pairwise eight-word Q31 theorem
# ------------------------------------------------------------
rng = np.random.default_rng(20260915171104)
worst_pair_ratio = float("inf")

for d in [2, 3, 4, 6]:
    for _ in range(300):
        A = rand_psd(d, rng)
        B = rand_psd(d, rng)
        p = opnorm(A @ B)

        mats = [
            A@A@A@B,
            A@A@B@A,
            A@B@A@A,
            B@A@A@A,
            B@B@B@A,
            B@B@A@B,
            B@A@B@B,
            A@B@B@B,
        ]
        pair_sum = sum(opnorm(M) for M in mats)
        target = 8*p*p
        if target > 1e-300:
            ratio = pair_sum/target
            worst_pair_ratio = min(worst_pair_ratio, ratio)
            assert pair_sum >= target - 1e-9*max(1.0, target)

print("worst random pair ratio Q31_pair/(8 p^2) =", worst_pair_ratio)


# ------------------------------------------------------------
# 3. Full occupancy checks
# ------------------------------------------------------------
words = list(itertools.product(range(4), repeat=4))


def occupancy(A):
    S = Q211 = Q22 = Q31 = Q4 = 0.0
    for w in words:
        v = opnorm(A[w[0]] @ A[w[1]] @ A[w[2]] @ A[w[3]])
        shape = sorted(Counter(w).values(), reverse=True)
        if shape == [1,1,1,1]:
            S += v
        elif shape == [2,1,1]:
            Q211 += v
        elif shape == [2,2]:
            Q22 += v
        elif shape == [3,1]:
            Q31 += v
        elif shape == [4]:
            Q4 += v
    return S,Q211,Q22,Q31,Q4

worst_q31_P = float("inf")
worst_q31_S = float("inf")
worst_final = float("inf")

for _ in range(250):
    A = [rand_psd(3, rng) for _ in range(4)]
    S,Q211,Q22,Q31,Q4 = occupancy(A)

    aa = [opnorm(X) for X in A]
    P = 0.0
    E = 0.0
    for i in range(4):
        for j in range(i+1,4):
            pij = opnorm(A[i] @ A[j])
            P += pij*pij
            E += aa[i]**2 * aa[j]**2
    Q = sum(x**4 for x in aa)

    assert S <= 4*P + 1e-8*max(1.0,S)
    assert P <= E + 1e-8*max(1.0,E)
    assert E <= 1.5*Q + 1e-8*max(1.0,E,Q)

    assert Q31 >= 8*P - 1e-8*max(1.0,Q31,8*P)
    assert Q31 >= 2*S - 1e-8*max(1.0,Q31,2*S)

    if P > 1e-300:
        worst_q31_P = min(worst_q31_P, Q31/(8*P))
    if S > 1e-300:
        worst_q31_S = min(worst_q31_S, Q31/(2*S))

    if S > 1e-300 and P > 1e-300 and E > 1e-300:
        lower = 3*S + S*S/(2*math.sqrt(P*E)) + 12*P + 2*P*P/E + Q
        R = S+Q211+Q22+Q31+Q4
        # The report's cumulative lower formula also depends on previously proved
        # Q211 and Q22 estimates.  Here we directly test those estimates before
        # testing the combined lower bound.
        assert Q211 >= 2*S + S*S/(2*math.sqrt(P*E)) - 1e-7*max(1.0,Q211)
        assert Q22 >= 4*P + 2*P*P/E - 1e-7*max(1.0,Q22)
        assert R >= lower - 1e-7*max(1.0,R,lower)
        assert R >= Fstar*S - 1e-7*max(1.0,R,Fstar*S)
        worst_final = min(worst_final, R/(Fstar*S))

print("worst random Q31/(8P) =", worst_q31_P)
print("worst random Q31/(2S) =", worst_q31_S)
print("worst random R/(F* S) =", worst_final)
print("All corroborative checks passed.")
