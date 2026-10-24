#!/usr/bin/env python3
"""Verify the tensor endpoint obstruction and its exact growth parameter."""

from fractions import Fraction
import importlib.util
import json
import math
import numpy as np

U_INDEX = 22338
V_INDEX = 38505
U = [1 if (U_INDEX >> r) & 1 else -1 for r in range(16)]
V = [1 if (V_INDEX >> r) & 1 else -1 for r in range(16)]


def walsh(values):
    out = [Fraction(x) for x in values]
    step = 1
    while step < len(out):
        for base in range(0, len(out), 2*step):
            for k in range(base, base+step):
                x, y = out[k], out[k+step]
                out[k], out[k+step] = x+y, x-y
        step *= 2
    return [x/len(out) for x in out]


def upper(values):
    out = list(values)
    n = len(out).bit_length()-1
    for bit in range(n):
        for mask in range(1 << n):
            if not ((mask >> bit) & 1):
                out[mask] += out[mask | (1 << bit)]
    return out


uh = walsh(U)
vh = walsh(V)
p = [x*x for x in uh]
caps = upper(p)
A = sum((x/c for x, c in zip(p, caps)), Fraction())
rho = sum((x*y for x, y in zip(uh, vh)), Fraction())
assert vh[:-1] == [0]*15 and vh[-1] == 1
assert A == Fraction(6911, 960)
assert rho == Fraction(1, 8)

# Load the independently implemented float endpoint evaluator.
spec = importlib.util.spec_from_file_location("endpoint_search", "search_endpoint_outer5.py")
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

direct = []
uk = np.array(U, dtype=np.int8)
vk = np.array(V, dtype=np.int8)
for k in range(1, 4):
    if k > 1:
        uk = np.kron(uk, np.array(U, dtype=np.int8))
        vk = np.kron(vk, np.array(V, dtype=np.int8))
    ratio, beta = mod.endpoint_ratio(mod.fwht_rows(uk[None, :]),
                                     mod.fwht_rows(vk[None, :]))
    beta_exact = (1-rho**k)/2
    assert abs(beta[0]-float(beta_exact)) < 1e-12
    lower = (float(A)**k-3)/(2*math.log(2))-2*k
    direct.append({
        "tensor_power": k,
        "slice_dimension": 4*k,
        "beta_exact": str(beta_exact),
        "direct_endpoint_ratio_float64": float(ratio[0]),
        "proved_slope_lower_bound_using_U_le_dimension": lower,
    })

print(json.dumps({
    "status": "PASS",
    "base_u_index": U_INDEX,
    "base_v_index": V_INDEX,
    "v_is_full_parity": True,
    "base_correlation_exact": str(rho),
    "base_cap_ratio_sum_A_exact": str(A),
    "base_cap_ratio_sum_A_decimal": float(A),
    "direct_checks": direct,
    "proved_general_lower_bound": "Q_k >= (A^k-3)/(2 ln 2)-2k whenever RHS is positive",
    "conclusion": "sup_k Q_k = infinity",
    "random_seed": None,
}, indent=2, sort_keys=True))
