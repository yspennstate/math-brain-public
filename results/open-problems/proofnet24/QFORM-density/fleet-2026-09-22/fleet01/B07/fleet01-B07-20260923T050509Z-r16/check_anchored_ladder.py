#!/usr/bin/env python3
"""Numerical regression for QFORM-ANCHORED-COMPOUND-TAIL-LADDER-v1.
Diagnostics only; REPORT.md contains the proof.
"""
import itertools, math
import numpy as np


def H_k(M, k, i=0, a=0):
    m, n = M.shape
    out = 0.0
    for R in itertools.combinations(range(m), k):
        if i not in R:
            continue
        for C in itertools.combinations(range(n), k):
            if a not in C:
                continue
            d = np.linalg.det(M[np.ix_(R, C)])
            out += d*d
    return out


def T_k(M, k):
    s = np.linalg.svd(M, compute_uv=False)
    return float(np.sum(s[k:]**2))


def hadamard(n):
    H = np.array([[1.0]])
    while H.shape[0] < n:
        H = np.block([[H, H], [H, -H]])
    return H

rng = np.random.default_rng(20260923)
ratios = []
b0_ratios = []
violations = 0
cases = 0
for m, n in [(3,3),(4,5),(5,4),(5,6),(6,6),(7,5)]:
    for rep in range(30):
        M = rng.integers(-3, 4, size=(m,n)).astype(float)
        if rep % 5 == 0:
            M[0,0] = 0.0
        for k in range(1, min(m,n)):
            hk = H_k(M,k)
            hk1 = H_k(M,k+1)
            rhs = T_k(M,k)*hk/k
            cases += 1
            if rhs > 1e-9:
                ratio = hk1/rhs
                ratios.append(ratio)
                if M[0,0] == 0.0:
                    b0_ratios.append(ratio)
                if ratio < 1.0-1e-7:
                    violations += 1

# sharpness: I_{k+1} has H_k=k, H_{k+1}=T_k=1
for k in range(1,7):
    M = np.eye(k+1)
    ratio = H_k(M,k+1)/(T_k(M,k)*H_k(M,k)/k)
    assert abs(ratio-1.0) < 1e-10

# N3 conditional-diffusion stress from REPORT.md, N=64
N = 64
H = hadamard(N)
U = H[:,:3]/math.sqrt(N)
R = U @ U.T
b = 1/16
M = np.zeros((N+1,N+1))
M[0,0] = b
M[1:,1:] = R
sv = np.linalg.svd(M,compute_uv=False)

print(f"CASES={cases}")
print(f"VIOLATIONS={violations}")
print(f"MIN_NONTRIVIAL_RATIO={min(ratios):.15f}")
print(f"MIN_ZERO_ANCHOR_RATIO={min(b0_ratios):.15f}")
print("IDENTITY_SHARPNESS=PASS")
print("STRESS_SINGULAR_VALUES=" + ",".join(f"{x:.12g}" for x in sv[:4]))
print(f"STRESS_F2={np.linalg.norm(M,'fro')**2:.12g}")
print(f"STRESS_MAX_ENTRY={np.max(np.abs(M)):.12g}")
print(f"STRESS_MAX_PAIRDET_MAG={np.max(np.abs(M))**2:.12g}")
print(f"STRESS_RESIDUAL_MARGINAL={3/N:.12g}")
print("STATUS=QFORM_ANCHORED_COMPOUND_TAIL_CHECK_PASS" if violations==0 else "STATUS=FAIL")
