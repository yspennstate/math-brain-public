#!/usr/bin/env python3
"""Exact/finite checks for the one-point-defect Hellinger-vs-KL FEI calibration.

No claim of full FEI. This script:
  * verifies the Walsh spectrum of a one-point defect by brute force for d<=5;
  * evaluates the exact closed forms for larger d;
  * checks tensor-product amplification of the product-marginal excess versus
    the global squared-root/Hellinger displacement t=||sqrt(mu)-sqrt(Q)||_2^2.
"""
from __future__ import annotations

import json
import math

C = 6.4547837


def h2(p: float) -> float:
    if p <= 0.0 or p >= 1.0:
        return 0.0
    return -p * math.log2(p) - (1.0 - p) * math.log2(1.0 - p)


def fwht(a):
    a = list(map(float, a))
    h = 1
    while h < len(a):
        for i in range(0, len(a), 2*h):
            for j in range(i, i+h):
                x, y = a[j], a[j+h]
                a[j], a[j+h] = x+y, x-y
        h *= 2
    n = len(a)
    return [x/n for x in a]


def one_point_truth(d: int):
    n = 1 << d
    # Defect at vertex 0; moving it only changes Fourier signs.
    return [-1.0] + [1.0] * (n-1)


def brute_check(d: int):
    p = 2.0 ** (1-d)
    coeff = fwht(one_point_truth(d))
    assert abs(abs(coeff[0]) - (1-p)) < 1e-12
    for a in coeff[1:]:
        assert abs(abs(a) - p) < 1e-12
    mu = [a*a for a in coeff]
    marg = []
    for i in range(d):
        marg.append(sum(w for mask, w in enumerate(mu) if mask & (1 << i)))
    assert max(abs(x-p) for x in marg) < 1e-12
    return {"d": d, "p": p, "max_marginal_error": max(abs(x-p) for x in marg)}


def closed_metrics(d: int):
    p = 2.0 ** (1-d)
    mu0 = (1-p)**2
    mun = p*p
    H = -mu0*math.log2(mu0) - (2**d-1)*mun*math.log2(mun)
    I = d*p
    tc = d*h2(p) - H
    excess = d*(h2(p)-C*p)
    affinity = (1-2*p)*(1-p)**(d/2) + p*(math.sqrt(p)+math.sqrt(1-p))**d
    t = 2*(1-affinity)
    assert tc >= -1e-12
    assert t >= -1e-12
    return {
        "d": d, "p": p, "H": H, "I": I, "H_over_I": H/I,
        "TC": tc, "product_excess_C": excess, "affinity": affinity, "t": t,
        "product_excess_over_t": excess/t if t else None,
        "TC_over_t": tc/t if t else None,
    }


def tensor_metrics(d: int, m: int):
    base = closed_metrics(d)
    affinity_m = base["affinity"]**m
    t_m = 2*(1-affinity_m)
    excess_m = m*base["product_excess_C"]
    tc_m = m*base["TC"]
    assert t_m <= 2.0 + 1e-12
    return {
        "d": d, "m": m, "product_excess_C": excess_m,
        "TC": tc_m, "t": t_m,
        "product_excess_over_t": excess_m/t_m,
        "TC_over_t": tc_m/t_m,
    }


out = {
    "status": "PASS_FINITE_AND_CLOSED_FORM_CHECKS",
    "constant_C": C,
    "brute_walsh": [brute_check(d) for d in range(2, 6)],
    "closed_form": [closed_metrics(d) for d in [6,7,8,10,12,16,20,30]],
    "tensor_d8": [tensor_metrics(8, m) for m in [1,2,4,8,16,32,64]],
}
print(json.dumps(out, indent=2, sort_keys=True))
