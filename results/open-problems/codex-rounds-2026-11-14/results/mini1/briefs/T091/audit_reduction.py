#!/usr/bin/env python3
"""Exact finite algebra checks for the identities in PROOF.md.

No numerical PDE integration is used. Gaussian rational Fourier coefficients
make the drift and translation checks exact. Symmetric finite increments
independently recover the quadratic Ito drift by averaging.
"""
import itertools
import json
import os
import random
import resource
import signal
import sys
from fractions import Fraction as F
from pathlib import Path

signal.alarm(30)
assert os.environ.get("OMP_NUM_THREADS") == "1"
inherited_nice = os.getpriority(os.PRIO_PROCESS, 0)
if inherited_nice < 15:
    sys.exit(f"AUDIT NOT RUN: inherited nice={inherited_nice}; required nice>=15")
print(f"Inherited nice: {inherited_nice}", flush=True)
# Lower only the soft limit and preserve the existing hard limit.
limit_notes = []
for limit, cap in ((resource.RLIMIT_DATA, 512 * 1024**2),
                   (resource.RLIMIT_RSS, 768 * 1024**2)):
    soft, hard = resource.getrlimit(limit)
    bounded_cap = cap if hard == resource.RLIM_INFINITY else min(cap, hard)
    try:
        resource.setrlimit(limit, (bounded_cap, hard))
        limit_notes.append(f"resource {limit}: soft cap {bounded_cap} bytes")
    except (OSError, ValueError) as exc:
        # Darwin may reject lowering these limits. The finite test uses at
        # most 9 input modes and 81 mode pairs per convolution; record RSS.
        limit_notes.append(f"resource {limit}: cap unavailable: {exc}")

# Gaussian rationals are represented by pairs (real, imaginary).
Z = (F(0), F(0))
I = (F(0), F(1))
ONE = (F(1), F(0))
UNITS = (ONE, I, (F(-1), F(0)), (F(0), F(-1)))

def add(a, b):
    return (a[0] + b[0], a[1] + b[1])

def mul(a, b):
    return (a[0]*b[0] - a[1]*b[1], a[0]*b[1] + a[1]*b[0])

def scale(c, a):
    return (c*a[0], c*a[1])

def neg(a):
    return scale(-1, a)

def conj(a):
    return (a[0], -a[1])

def gsum(xs):
    ans = Z
    for x in xs:
        ans = add(ans, x)
    return ans

def cross(k, a):
    return (k[1]*a[2]-k[2]*a[1],
            k[2]*a[0]-k[0]*a[2],
            k[0]*a[1]-k[1]*a[0])

VZERO = (Z, Z, Z)

def vadd(a, b):
    return tuple(add(x, y) for x, y in zip(a, b))

def vscale(c, a):
    return tuple(mul(c, x) for x in a)

def project(k, a):
    kk = sum(x*x for x in k)
    if kk == 0:
        return a
    ka = gsum(scale(x, y) for x, y in zip(k, a))
    return tuple(add(y, scale(-F(x, kk), ka)) for x, y in zip(k, a))

def convection(field):
    # Independently expand (u dot grad)u in Fourier coordinates, then project.
    ans = {}
    for p, up in field.items():
        for q, uq in field.items():
            k = tuple(x+y for x, y in zip(p, q))
            up_dot_q = gsum(scale(x, z) for x, z in zip(q, up))
            term = vscale(mul(I, up_dot_q), uq)
            ans[k] = vadd(ans.get(k, VZERO), term)
    return {k: project(k, a) for k, a in ans.items()}

def phase(k):
    # X = (pi/2)*(1,2,3), so exp(i*k.X) is an exact Gaussian unit.
    return UNITS[sum((j+1)*x for j, x in enumerate(k)) % 4]

def energy(field):
    return sum((z[0]*z[0] + z[1]*z[1]
                for a in field.values() for z in a), F(0)) / 2

rng = random.Random(910314)
base_modes = ((1, 0, 0), (0, 1, 1), (1, 1, 0), (1, -1, 2))
trial_results = []
nu = F(3, 7)
for trial in range(6):
    y = {}
    for k in base_modes:
        real = cross(k, tuple(rng.randint(-3, 3) for _ in range(3)))
        imag = cross(k, tuple(rng.randint(-3, 3) for _ in range(3)))
        a = tuple((F(x, 2), F(z, 3)) for x, z in zip(real, imag))
        y[k] = a
        y[tuple(-x for x in k)] = tuple(conj(z) for z in a)
    for k, a in y.items():
        assert gsum(scale(x, z) for x, z in zip(k, a)) == Z
    m = (F(trial+1, 2), F(-2, 3), F(5-trial, 4))
    full = dict(y)
    full[(0, 0, 0)] = tuple((x, F(0)) for x in m)
    cy = convection(y)
    cu = convection(full)
    ty = {k: vscale(phase(k), a) for k, a in y.items()}
    cty = convection(ty)
    all_modes = set(cy) | set(cu) | set(y)
    wrong_sign_nonzero_modes = 0
    nonlinear_nonzero_modes = 0
    for k in sorted(all_modes):
        a = y.get(k, VZERO)
        mk = sum(x*z for x, z in zip(m, k))
        adv = vscale(scale(mk, I), a)
        visc = vscale((-nu*sum(x*x for x in k), F(0)), a)
        # Full Fourier drift after subtracting dm (no transformation used here).
        raw_drift = vadd(visc, tuple(neg(z) for z in cu.get(k, VZERO)))
        # Differentiating exp(+i*k.X) contributes +i*(k.m)*a.
        corrected = vadd(raw_drift, adv)
        deterministic = vadd(visc, tuple(neg(z) for z in cy.get(k, VZERO)))
        assert corrected == deterministic
        wrong = vadd(raw_drift, tuple(neg(z) for z in adv))
        wrong_sign_nonzero_modes += (wrong != deterministic)
        assert cty.get(k, VZERO) == vscale(phase(k), cy.get(k, VZERO))
        nonlinear_nonzero_modes += (cy.get(k, VZERO) != VZERO)
    assert wrong_sign_nonzero_modes > 0
    assert nonlinear_nonzero_modes > 0
    assert energy(ty) == energy(y)
    assert energy(full) - energy(y) == sum(x*x for x in m)/2
    trial_results.append({
        "trial": trial,
        "checked_output_modes": len(all_modes),
        "nonzero_projected_nonlinearity_modes": nonlinear_nonzero_modes,
        "drift_residual": "0 (exact)",
        "translation_covariance_residual": "0 (exact)",
        "parseval_energy_split_residual": "0 (exact)",
        "wrong_translation_sign_nonzero_modes": wrong_sign_nonzero_modes,
    })

# Recover Ito's coefficient for a quadratic by exact averaging of increments.
# These are not simulated Brownian paths. The +/- increments have exactly
# the first two moments required for the quadratic expectation calculation.
matrices = [
    ("rank_0", ((0, 0, 0),)),
    ("rank_1", ((2, -1, 3),)),
    ("rank_2", ((1, 0, 0), (0, 2, 0))),
    ("rank_3", ((1, 0, 0), (0, 2, 0), (0, 0, 3))),
    ("rank_3_redundant", ((1, 2, 0), (0, 1, 1), (1, 0, 2), (2, -1, 1))),
]
m = (F(3, 2), F(-4, 3), F(5, 4))
root_h = F(1, 10)
h = root_h**2
ito_results = []
for label, columns in matrices:
    increments = []
    for signs in itertools.product((-1, 1), repeat=len(columns)):
        dm = tuple(sum((root_h*s*col[i] for s, col in zip(signs, columns)), F(0))
                   for i in range(3))
        delta_energy = sum(((m[i]+dm[i])**2-m[i]**2 for i in range(3)), F(0))/2
        increments.append(delta_energy)
    average = sum(increments, F(0))/len(increments)
    trace_k = sum(x*x for col in columns for x in col)
    expected = h*trace_k/2
    assert average == expected
    wrong = h*trace_k
    if trace_k:
        assert wrong != average
    ito_results.append({
        "covariance_case": label,
        "trace_K": trace_k,
        "averaged_quadratic_energy_increment": str(average),
        "half_trace_times_dt": str(expected),
        "residual": "0 (exact)",
        "wrong_full_trace_coefficient_residual": str(wrong-average),
    })

rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
rss_bytes = rss if sys.platform == "darwin" else rss * 1024
assert rss_bytes < 1024**3
out = {
    "arithmetic": "exact fractions and Gaussian rationals",
    "inherited_nice": inherited_nice,
    "resource_limit_notes": limit_notes,
    "seed": 910314,
    "nu": str(nu),
    "fourier_trials": trial_results,
    "quadratic_increment_trials": ito_results,
    "dt": str(h),
    "peak_rss_bytes": rss_bytes,
    "scope": "Finite algebra checks only; no PDE existence or regularity computation.",
}
Path("audit_results.json").write_text(json.dumps(out, indent=2) + "\n")
print("PASS: 6 exact Fourier drift, translation, and energy-splitting trials")
print("PASS: 5 exact quadratic-increment averages (covariance ranks 0 through 3)")
print("PASS: wrong translation sign and wrong nonzero Ito trace coefficient rejected")
print("Data: audit_results.json")
print(f"Peak RSS: {rss_bytes} bytes")
