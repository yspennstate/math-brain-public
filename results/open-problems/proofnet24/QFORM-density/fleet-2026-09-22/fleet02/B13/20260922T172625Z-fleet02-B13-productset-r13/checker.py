#!/usr/bin/env python3
import math
import random

rng = random.Random(20260922172625)

C_ENV = 2.0 * math.sqrt(3.0)
C_LOCAL = (2.0 ** (5.0/4.0)) * math.sqrt(15.0) * C_ENV * ((5.0/4.0) ** 0.25)
C_BLOCK = 16.0 * (2.0 ** 0.25) * math.sqrt(15.0)

max_factor_rel = 0.0
max_kappad_rel = 0.0
max_schur_rel = 0.0
max_theta_excess = -1e100
max_A_excess = -1e100

for _ in range(20000):
    b = 10.0 ** rng.uniform(-3.0, 3.0)
    a = rng.uniform(-0.5, 0.5) * b
    c = rng.uniform(-0.5, 0.5) * b
    D = b*b - a*c
    delta = math.sqrt(D)
    kappa = 0.5 * (b + delta)
    r = c/(2.0*kappa)
    s = a/(2.0*kappa)
    d = 1.0-r*s

    # Exact coefficient reconstruction.
    aa = 2.0*kappa*s
    cc = 2.0*kappa*r
    bb = kappa*(1.0+r*s)
    scale = max(1.0, abs(a), abs(b), abs(c))
    max_factor_rel = max(max_factor_rel, abs(aa-a)/scale, abs(bb-b)/scale, abs(cc-c)/scale)
    max_kappad_rel = max(max_kappad_rel, abs(kappa*d-delta)/max(1.0, delta))

    theta = 1.0 + 0.5*(abs(r)+abs(s))
    max_theta_excess = max(max_theta_excess, theta-(3.0-math.sqrt(3.0)))
    A0 = theta*math.sqrt(kappa/b)
    max_A_excess = max(max_A_excess, A0-math.sqrt(2.0))

    # Random bordered 3x3 Schur determinant identity.
    p = rng.uniform(-3.0, 3.0)*b
    q = rng.uniform(-3.0, 3.0)*b
    gamma = rng.uniform(-3.0, 3.0)*b
    detC = a*c-b*b
    inv00, inv01, inv11 = c/detC, -b/detC, a/detC
    schur = gamma-(p*p*inv00+2.0*p*q*inv01+q*q*inv11)
    detB = a*(c*gamma-q*q)-b*(b*gamma-p*q)+p*(b*q-c*p)
    max_schur_rel = max(max_schur_rel, abs(detB-detC*schur)/max(1.0, abs(detB), abs(detC*schur)))

assert max_theta_excess <= 1e-12
assert max_A_excess <= 1e-12
assert max_factor_rel <= 1e-10
assert max_kappad_rel <= 1e-10
assert max_schur_rel <= 1e-10
assert C_LOCAL < C_BLOCK

print("QFORM_NEAR_NULL_CHECK_PASS")
print(f"max_factor_rel {max_factor_rel:.3e}")
print(f"max_kappad_rel {max_kappad_rel:.3e}")
print(f"max_schur_rel {max_schur_rel:.3e}")
print(f"max_theta_excess {max_theta_excess:.3e}")
print(f"max_A_excess {max_A_excess:.3e}")
print(f"C_env {C_ENV:.12f}")
print(f"C_local {C_LOCAL:.12f}")
print(f"C_block {C_BLOCK:.12f}")
