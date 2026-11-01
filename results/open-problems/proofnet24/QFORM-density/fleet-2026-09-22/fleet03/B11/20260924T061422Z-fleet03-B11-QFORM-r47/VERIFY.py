#!/usr/bin/env python3
"""Deterministic regression checks for fleet03/B11 puncture two-Jacobian identity.

This is not a proof. REPORT.md contains the exact proof.
"""
import math
import random


def dot(a, b):
    return sum(x*y for x, y in zip(a, b))


def norm(a):
    return math.sqrt(dot(a, a))


def gram_schmidt(cols):
    out = []
    for z in cols:
        y = list(z)
        for q in out:
            d = dot(y, q)
            y = [yi-d*qi for yi, qi in zip(y, q)]
        n = norm(y)
        if n < 1e-12:
            return None
        out.append([yi/n for yi in y])
    return out


random.seed(20260924)
N = 5000
max_abs = 0.0
max_rel = 0.0
for _ in range(N):
    m = 8
    cols = [[random.gauss(0.0, 1.0) for _ in range(m)] for _ in range(3)]
    orth = gram_schmidt(cols)
    if orth is None:
        continue
    t, w, v = orth
    a, b, c, eta, delta = [random.uniform(-3.0, 3.0) for _ in range(5)]
    if abs(c) < 0.1:
        c = 0.1 if c >= 0 else -0.1
    H = random.uniform(-2.0, 2.0)
    x = [random.uniform(-2.0, 2.0) for _ in range(m)]
    T = dot(t, x)
    W = dot(w, x)
    V = dot(v, x)
    Vp = V + eta*W

    lhs = 0.0
    for j in range(m):
        D = -2.0*a*W*w[j]
        lhs += D*D
    for j in range(m):
        for k in range(j+1, m):
            D = (2.0*b*W*(w[j]*t[k]-w[k]*t[j])
                 + 2.0*c*Vp*(w[j]*v[k]-w[k]*v[j]))
            lhs += D*D

    kappa2 = a*a+b*b
    rhs = 4.0*(kappa2*W*W+c*c*Vp*Vp)
    err = abs(lhs-rhs)
    max_abs = max(max_abs, err)
    max_rel = max(max_rel, err/max(1.0, abs(rhs)))

print(f"checks={N}")
print(f"max_abs_identity_error={max_abs:.17g}")
print(f"max_relative_identity_error={max_rel:.17g}")
print(f"sqrt_2pi={math.sqrt(2.0*math.pi):.17g}")
print(f"small_J_tail_coefficient_pi_over_2={math.pi/2.0:.17g}")
assert max_rel < 1e-12
assert abs(math.sqrt(2.0*math.pi)-2.5066282746310002) < 1e-15
print("QFORM_B11_PUNCTURE_TWOJACOBIAN_CHECK_PASS")
