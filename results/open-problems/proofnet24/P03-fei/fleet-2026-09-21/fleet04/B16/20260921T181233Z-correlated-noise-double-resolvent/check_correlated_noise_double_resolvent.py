#!/usr/bin/env python3
"""Exact self-check for B16 correlated-noise double-resolvent current.

Standard library only.  This is falsification evidence for the algebraic
proof in REPORT.md; it is not an FEI certificate.
"""
from fractions import Fraction
from itertools import product
import json
import random

def pc(x):
    return int(x).bit_count()

def chi(mask, state):
    return -1 if pc(mask & state) & 1 else 1

def pair_params(mask, m):
    q = k = r = 0
    for j in range(m):
        occ = ((mask >> (2*j)) & 1) + ((mask >> (2*j+1)) & 1)
        q += occ
        if occ == 1:
            k += 1
        elif occ == 2:
            r += 1
    return q, k, r

def noise_kernel(bits, rho):
    p = (Fraction(1) - rho) / 2
    z = Fraction(1) - p
    return [p**pc(a) * z**(bits-pc(a)) for a in range(1 << bits)]

def pair_law(y, lam):
    p = (1-y) / 2
    return {
        0: (1-p)**2 + lam*p*(1-p),
        3: p**2 + lam*p*(1-p),
        1: (1-lam)*p*(1-p),
        2: (1-lam)*p*(1-p),
    }

def pair_dlaw(y):
    p = (1-y) / 2
    a = p*(1-p)
    return {0:a, 3:a, 1:-a, 2:-a}

def product_pair_kernel(m, y, lam, derivative=False, exclude=None):
    if not derivative:
        laws = []
        for j in range(m):
            laws.append({0:Fraction(1)} if j == exclude else pair_law(y, lam))
        out = [Fraction(0) for _ in range(1 << (2*m))]
        for states in product(*[tuple(L) for L in laws]):
            mask = 0
            w = Fraction(1)
            for j, st in enumerate(states):
                mask |= st << (2*j)
                w *= laws[j][st]
            out[mask] += w
        return out

    out = [Fraction(0) for _ in range(1 << (2*m))]
    for deriv_j in range(m):
        if deriv_j == exclude:
            continue
        laws = []
        for j in range(m):
            if j == exclude:
                laws.append({0:Fraction(1)})
            elif j == deriv_j:
                laws.append(pair_dlaw(y))
            else:
                laws.append(pair_law(y, lam))
        for states in product(*[tuple(L) for L in laws]):
            mask = 0
            w = Fraction(1)
            for j, st in enumerate(states):
                mask |= st << (2*j)
                w *= laws[j][st]
            out[mask] += w
    return out

def apply_conv(vec, kernel):
    n = len(vec)
    return [sum(kernel[z] * vec[s ^ z] for z in range(n)) for s in range(n)]

def inner(a, b):
    return sum(x*y for x, y in zip(a,b)) / len(a)

def pair_difference(vec, j):
    a = 1 << (2*j)
    b = 1 << (2*j+1)
    return [vec[s] + vec[s^a^b] - vec[s^a] - vec[s^b] for s in range(len(vec))]

rng = random.Random(20260921)
transition_checks = 0
operator_checks = 0
curvature_checks = 0
scalar_checks = 0
central_checks = 0

# One-pair transition eigenvalues and derivative.
for yi in range(1,5):
    y = Fraction(yi,5)
    for li in range(5):
        lam = Fraction(li,4)
        law = pair_law(y, lam)
        dlaw = pair_dlaw(y)
        assert sum(law.values()) == 1
        assert sum(dlaw.values()) == 0
        a = y*y + lam*(1-y*y)
        for support in (0,1,2,3):
            eig = sum(w*chi(support,z) for z,w in law.items())
            deig = sum(w*chi(support,z) for z,w in dlaw.items())
            occ = pc(support)
            expect = Fraction(1) if occ == 0 else (y if occ == 1 else a)
            dexpect = Fraction(0) if occ < 2 else 1-y*y
            assert eig == expect
            assert deig == dexpect
            transition_checks += 1

# Direct configuration-space quadratic forms versus the Walsh formula.
for m in (1,2,3):
    bits = 2*m
    size = 1 << bits
    for _ in range(8):
        coeff = {}
        for R in range(1, size):
            q,k,r = pair_params(R,m)
            if q & 1 and rng.random() < 0.35:
                coeff[R] = Fraction(rng.randint(-3,3), rng.randint(1,4))
        if not coeff:
            coeff[1] = Fraction(1,2)

        phi = [sum(b*chi(R,s) for R,b in coeff.items()) for s in range(size)]
        x = Fraction(rng.randint(1,4),5)
        y = Fraction(rng.randint(1,4),5)
        lam = Fraction(rng.randint(0,4),4)

        nx = noise_kernel(bits, x)
        dc = product_pair_kernel(m, y, lam, derivative=True)
        lhs = inner(phi, apply_conv(apply_conv(phi, dc), nx))

        aa = y*y + lam*(1-y*y)
        rhs = Fraction(0)
        for R,b in coeff.items():
            q,k,r = pair_params(R,m)
            deig = 0 if r == 0 else r*(1-y*y)*(y**k)*(aa**(r-1))
            rhs += b*b*(x**q)*deig
        assert lhs == rhs
        operator_checks += 1

        rhs2 = Fraction(0)
        for j in range(m):
            dphi = pair_difference(phi, j)
            cex = product_pair_kernel(m, y, lam, exclude=j)
            rhs2 += inner(dphi, apply_conv(apply_conv(dphi, cex), nx))
        rhs2 *= (1-y*y)/16
        assert lhs == rhs2
        curvature_checks += 1

# Exact integrated multipliers and sharp full/central constants.
max_full_ratio = Fraction(0)
max_full_at = None
max_central_ratio = Fraction(0)
max_central_at = None
for q in range(1,80,2):
    for k in range(1,q+1,2):
        if (q-k) & 1:
            continue
        r = (q-k)//2
        full = 2*(Fraction(1,q*k)-Fraction(1,q*q))
        ward = Fraction(q-1,q)
        assert full == Fraction(4*r, q*q*k)
        assert full <= Fraction(2,3)*ward
        if ward and full/ward > max_full_ratio:
            max_full_ratio = full/ward
            max_full_at = [q,k]
        scalar_checks += 1

        central = 2*Fraction(1,(2**q)*q) * (
            Fraction(1,(2**k)*k) - Fraction(1,(2**q)*q)
        )
        assert 0 <= central <= full
        if ward:
            assert central <= Fraction(11,192)*ward
            if central/ward > max_central_ratio:
                max_central_ratio = central/ward
                max_central_at = [q,k]
        central_checks += 1

result = {
    "status": "PASS",
    "transition_eigenvalue_checks": transition_checks,
    "configuration_operator_checks": operator_checks,
    "curvature_square_checks": curvature_checks,
    "integrated_multiplier_checks": scalar_checks,
    "central_truncation_checks": central_checks,
    "sharp_full_ward_ratio": f"{max_full_ratio.numerator}/{max_full_ratio.denominator}",
    "sharp_full_at_q_k": max_full_at,
    "sharp_central_ward_ratio": f"{max_central_ratio.numerator}/{max_central_ratio.denominator}",
    "sharp_central_at_q_k": max_central_at,
    "notes": [
        "All arithmetic exact Fraction arithmetic.",
        "Signed coefficient fields include negative coefficients.",
        "Finite checks are falsification evidence; REPORT.md contains the algebraic proof."
    ]
}
print(json.dumps(result, indent=2, sort_keys=True))
