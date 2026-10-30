#!/usr/bin/env python3
"""Deterministic arithmetic checks for fleet03/B06 r29.
The REPORT.md contains the proof; this script only verifies constants and
the optimized layer-cake algebra numerically.
"""
import math

def neg_half_bound(m, k):
    return math.sqrt(k/2.0)*(12.0+2.0/k) + m*math.sqrt(2.0/k)

for m in [0.05, 0.25, 1.0, 4.0, 25.0, 100.0]:
    k=(1.0+m)/6.0
    lhs=neg_half_bound(m,k)
    rhs=4.0*math.sqrt(3.0*(1.0+m))
    assert abs(lhs-rhs) <= 1e-12*max(1.0,rhs), (m,lhs,rhs)

hub=math.sqrt(127.0/800.0)
quarter_root=(127.0/800.0)**0.25
eta=0.25
residual=2.0*math.sqrt(3.0*math.e)*math.sqrt(1.0+1.0/eta)/quarter_root
outer=2.0*math.sqrt(residual)

assert 0.3984 < hub < 0.3985
assert 0.6312 < quarter_root < 0.6313
assert residual < 20.233
assert outer < 8.997

print("QFORM_B06_R29_CHECK_PASS")
print(f"sqrt(127/800)={hub:.12f}")
print(f"(127/800)^(1/4)={quarter_root:.12f}")
print(f"eta=1/4 residual_constant={residual:.12f}")
print(f"eta=1/4 outer_square_constant={outer:.12f}")
for m in [0.05,0.25,1.0,4.0,25.0,100.0]:
    k=(1.0+m)/6.0
    print(f"m={m:g} kopt={k:.12g} bound={neg_half_bound(m,k):.12f}")
