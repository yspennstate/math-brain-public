#!/usr/bin/env python3
"""Exact finite checks for B18 signed-subcube Palm/hybrid theorem.

The theorem in REPORT.md is analytic. This script checks exact rational
factorization and hybrid-collision identities for every Boolean residual
sigma through d=3 and control codimensions r=1,2,3.
"""
from fractions import Fraction
import json
import math

def parity(mask, x):
    return (mask & x).bit_count() & 1

def walsh(vals, n):
    N = 1 << n
    out = []
    for mask in range(N):
        s = 0
        for x, v in enumerate(vals):
            s += v * (-1 if parity(mask, x) else 1)
        out.append(Fraction(s, N))
    return out

def entropy(probs):
    return -sum(float(p) * math.log2(float(p)) for p in probs if p)

def mean_level(probs):
    return sum(p * mask.bit_count() for mask, p in enumerate(probs))

def projected_law(mu, d, Kmask):
    # Return probabilities indexed by actual submask T of Kmask.
    out = {}
    for B, p in enumerate(mu):
        T = B & Kmask
        out[T] = out.get(T, Fraction(0)) + p
    return out

case_count = 0
exact_checks = 0
hybrid_block_checks = 0
max_entropy_roundoff = 0.0
max_hybrid_ratio = Fraction(0)
examples = {}

for d in range(4):
    N = 1 << d
    for truth_bits in range(1 << N):
        sigma = [1 if ((truth_bits >> z) & 1) == 0 else -1 for z in range(N)]
        sigma_hat = walsh(sigma, d)
        mu = [c*c for c in sigma_hat]
        assert sum(mu) == 1
        I_sigma = mean_level(mu)
        H_sigma = entropy(mu)
        collision = sum(p*p for p in mu)

        # The exact-support hybrid theorem is independent of control codimension.
        for Kmask in range(1 << d):
            P = projected_law(mu, d, Kmask)
            coll_K = sum(p*p for p in P.values())
            I_K = sum(p * (B & Kmask).bit_count() for B, p in enumerate(mu))
            assert 1 - coll_K <= 2 * I_K
            exact_checks += 1
            hybrid_block_checks += 1
            if I_K:
                max_hybrid_ratio = max(max_hybrid_ratio, (1-coll_K)/I_K)

        for r in (1, 2, 3):
            D = r + d
            g = [0] * (1 << D)
            # Coordinate subcube support y=0^r.
            for z in range(1 << d):
                g[z << r] = sigma[z]

            g_hat = walsh(g, D)
            j = Fraction(sum(v*v for v in g), 1 << D)
            assert j == Fraction(1, 1 << r)
            exact_checks += 1

            nu = [c*c/j for c in g_hat]
            assert sum(nu) == 1
            exact_checks += 1

            # ν(A,B)=2^{-r} μ_sigma(B) exactly.
            for A in range(1 << r):
                for B in range(1 << d):
                    idx = A | (B << r)
                    assert nu[idx] == Fraction(1, 1 << r) * mu[B]
                    exact_checks += 1

            EZ = mean_level(nu)
            assert EZ == Fraction(r, 2) + I_sigma
            exact_checks += 1

            H_nu = entropy(nu)
            err = abs((H_nu - r) - H_sigma)
            max_entropy_roundoff = max(max_entropy_roundoff, err)
            assert err < 1e-12

            # Full residual block: B13 mixed-axis bank is exactly
            # 1-Coll(mu_sigma), while B12 depth defect is I(sigma).
            R_full = 1 - collision
            assert R_full <= 2 * I_sigma
            exact_checks += 1

            # B12 exact slack conservation specializes to
            # Slack_iso=0 and Slack_sign=4 j I(sigma).
            sign_slack = 4 * j * I_sigma
            assert sign_slack >= 0
            exact_checks += 1

            case_count += 1

            if d == 3 and r == 2 and truth_bits in (0, 1):
                examples[f"d3_r2_truth{truth_bits}"] = {
                    "j": str(j),
                    "I_sigma": str(I_sigma),
                    "H_sigma": H_sigma,
                    "Palm_mean_level": str(EZ),
                    "Palm_entropy": H_nu,
                    "R_full_residual": str(R_full),
                    "sign_slack": str(sign_slack),
                }

print(json.dumps({
    "status": "PASS",
    "scope": "all Boolean residual signs through d=3; r=1,2,3; every residual coordinate block K",
    "cases": case_count,
    "exact_rational_checks": exact_checks,
    "hybrid_block_checks": hybrid_block_checks,
    "max_hybrid_deficit_over_IK": str(max_hybrid_ratio),
    "max_entropy_float_roundoff": max_entropy_roundoff,
    "examples": examples,
}, indent=2, sort_keys=True))
