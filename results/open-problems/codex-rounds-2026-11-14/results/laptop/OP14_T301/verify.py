"""Exact, small checks for PROOF.md. No third-party packages or training.

Run: python -B verify.py
Writes only verification.json beside this file; deterministic and single threaded.
"""
import os
os.environ["OMP_NUM_THREADS"] = "1"
os.environ["OPENBLAS_NUM_THREADS"] = "1"
os.environ["MKL_NUM_THREADS"] = "1"
import ctypes
import itertools
import json
from fractions import Fraction as F
from pathlib import Path
from time import monotonic

START = monotonic()
if os.name == "nt":
    kernel = ctypes.WinDLL("kernel32", use_last_error=True)
    kernel.GetCurrentProcess.restype = ctypes.c_void_p
    kernel.SetPriorityClass.argtypes = [ctypes.c_void_p, ctypes.c_uint32]
    if not kernel.SetPriorityClass(kernel.GetCurrentProcess(), 0x4000):
        raise OSError(ctypes.get_last_error(), "SetPriorityClass failed")


def sweep(centers, radii, weights):
    """Integrate by cells, independently of sum_i 2*r_i*p_i."""
    endpoints = sorted(set(c-r for c, r in zip(centers, radii)) |
                       set(c+r for c, r in zip(centers, radii)))
    area = F(0)
    maximum = F(0)
    for left, right in zip(endpoints, endpoints[1:]):
        mid = (left+right)/2
        value = sum((p for c, r, p in zip(centers, radii, weights)
                     if abs(mid-c) <= r), F(0))
        area += (right-left)*value
        maximum = max(maximum, value)
    # Closed balls can have a larger maximum exactly at touching endpoints.
    for t in endpoints:
        value = sum((p for c, r, p in zip(centers, radii, weights)
                     if abs(t-c) <= r), F(0))
        maximum = max(maximum, value)
    return area, maximum


incidence_cases = 0
unequal_radius_cases = 0
for m in range(1, 5):
    # Includes repeated centers, zero span, and touching intervals.
    for centers in itertools.combinations_with_replacement(map(F, range(-2, 3)), m):
        for r0 in (F(1, 4), F(1), F(3, 2)):
            for raw in (list(range(1, m+1)), [1]*m):
                weights = [F(k, sum(raw)) for k in raw]
                area, maximum = sweep(centers, [r0]*m, weights)
                assert area == 2*r0
                span = max(centers)-min(centers)
                assert maximum >= 2*r0/(span+2*r0)
                assert 1/maximum <= 1+span/(2*r0)
                incidence_cases += 1
                radii = [r0*(i+1) for i in range(m)]
                area2, maximum2 = sweep(centers, radii, weights)
                direct = sum((2*r*p for r, p in zip(radii, weights)), F(0))
                assert area2 == direct
                assert maximum2 >= maximum
                unequal_radius_cases += 1

# Verify the Lipschitz coefficient squared in two independent forms.
lip_cases = 0
for d, n1, n2, n3, b in itertools.product(range(1, 5), repeat=5):
    frobenius_squared = (b*b*n1*d)*(b*b*n2*n1)*(b*b*n3*n2)*(b*b*n3)
    coordinate_squared = b**8*d*(n1*n2*n3)**2
    assert frobenius_squared == coordinate_squared
    lip_cases += 1

# Independent variance identity and the radius upper bound, for f(x)=x.
variance_cases = 0
for points in itertools.combinations_with_replacement(map(F, range(-2, 3)), 3):
    probabilities = [F(1, 6), F(1, 3), F(1, 2)]
    mean = sum(p*x for p, x in zip(probabilities, points))
    variance = sum(p*(x-mean)**2 for p, x in zip(probabilities, points))
    pairwise = sum(p*q*(x-y)**2/2
                   for p, x in zip(probabilities, points)
                   for q, y in zip(probabilities, points))
    assert variance == pairwise
    radius = max(map(abs, points))
    assert variance <= radius**2
    variance_cases += 1

# Explicitly test merging the first layer, using rational affine maps.
def relu(x):
    return max(F(0), x)

collapse_cases = 0
# A1(x) = (2x+3, -x-2, 0, 5) on [-1,1]; all activations fixed.
w1, b1 = [F(2), F(-1), F(0), F(0)], [F(3), F(-2), F(0), F(5)]
mask = [1, 0, 0, 1]
w2 = [[F(1), F(2), F(3), F(-1)], [F(-2), F(1), F(4), F(2)]]
b2 = [F(-1), F(3)]
w3, b3 = [F(2), F(-3)], F(1)
merged_w = [sum(a*s*w for a, s, w in zip(row, mask, w1)) for row in w2]
merged_b = [bias+sum(a*s*b for a, s, b in zip(row, mask, b1))
            for row, bias in zip(w2, b2)]
for x in map(lambda k: F(k, 20), range(-20, 21)):
    layer1 = [relu(w*x+b) for w, b in zip(w1, b1)]
    layer2 = [relu(sum(a*z for a, z in zip(row, layer1))+bias)
              for row, bias in zip(w2, b2)]
    original = sum(a*z for a, z in zip(w3, layer2))+b3
    merged = sum(a*relu(w*x+b) for a, w, b in zip(w3, merged_w, merged_b))+b3
    assert original == merged
    collapse_cases += 1

# A max-over-hyperplanes union bound can be very loose: disjoint intervals.
# This records why the theorem is only a ceiling on the stated certificate.
_, disjoint_max = sweep([F(0), F(4)], [F(1), F(1)], [F(1,2), F(1,2)])
assert disjoint_max == F(1, 2)

# Unequal local hardness: directly check (9), with L=1 and r_i=epsilon_i.
# The threshold t is rational here so all calculations remain exact.
variable_hardness_cases = 0
for m in range(1, 4):
    for centers in itertools.combinations_with_replacement(map(F, (-1, 0, 1)), m):
        for epsilons in itertools.product(map(F, (0, 1, 2)), repeat=m):
            raw = list(range(1, m+1))
            weights = [F(k, sum(raw)) for k in raw]
            energy = [p*e*e for p, e in zip(weights, epsilons)]
            beta = sum(energy)
            if beta == 0:
                continue
            _, gamma = sweep(centers, epsilons, energy)
            span = max(centers)-min(centers)
            for t in (F(1, 4), F(1, 2), F(3, 4)):
                if t*t >= beta:
                    continue
                lower = (beta-t*t)*2*t/(span+2*t)
                assert gamma >= lower
                assert gamma > 0
                variable_hardness_cases += 1

# Verify the 4/3 constant by substituting beta=q^2 and t=q/2.
variable_constant_cases = 0
for q, span in itertools.product(map(F, (F(1, 2), 1, 2, 3)), range(5)):
    beta, t = q*q, q/2
    lower = (beta-t*t)*2*t/(span+2*t)
    assert beta/lower == F(4, 3)*(1+span/q)
    variable_constant_cases += 1

result = {
    "status": "PASS",
    "equal_radius_incidence_cases": incidence_cases,
    "unequal_radius_incidence_cases": unequal_radius_cases,
    "lipschitz_coefficient_cases": lip_cases,
    "variance_identity_cases": variance_cases,
    "explicit_layer_collapse_points": collapse_cases,
    "variable_hardness_cases": variable_hardness_cases,
    "variable_hardness_constant_cases": variable_constant_cases,
    "arithmetic": "exact rational/integer",
    "dimension_note": "incidence tests are 1D projections, not an exhaustive high-dimensional search",
    "resource_note": "standard library; at most four intervals and 1024 scalar parameter tuples",
}
if os.name == "nt":
    class ProcessMemoryCounters(ctypes.Structure):
        _fields_ = [("cb", ctypes.c_uint32), ("PageFaultCount", ctypes.c_uint32)] + [
            (name, ctypes.c_size_t) for name in (
                "PeakWorkingSetSize", "WorkingSetSize", "QuotaPeakPagedPoolUsage",
                "QuotaPagedPoolUsage", "QuotaPeakNonPagedPoolUsage",
                "QuotaNonPagedPoolUsage", "PagefileUsage", "PeakPagefileUsage")]
    counters = ProcessMemoryCounters()
    counters.cb = ctypes.sizeof(counters)
    psapi = ctypes.WinDLL("psapi", use_last_error=True)
    psapi.GetProcessMemoryInfo.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint32]
    if not psapi.GetProcessMemoryInfo(kernel.GetCurrentProcess(), ctypes.byref(counters), counters.cb):
        raise OSError(ctypes.get_last_error(), "GetProcessMemoryInfo failed")
    result["peak_working_set_bytes"] = counters.PeakWorkingSetSize
    result["peak_pagefile_usage_bytes"] = counters.PeakPagefileUsage
    assert max(counters.PeakWorkingSetSize, counters.PeakPagefileUsage) < 1_000_000_000
result["elapsed_seconds"] = round(monotonic()-START, 6)
assert monotonic()-START < 1200
destination = Path(__file__).resolve().parent / "verification.json"
destination.write_text(json.dumps(result, indent=2)+"\n", encoding="utf-8")
print(json.dumps(result, sort_keys=True))
