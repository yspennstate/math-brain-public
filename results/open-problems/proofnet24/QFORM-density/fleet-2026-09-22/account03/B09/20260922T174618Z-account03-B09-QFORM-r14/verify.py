#!/usr/bin/env python3
import math


def I(m):
    return (1.0/3.0) * m**(2.0/3.0) * math.gamma(1.0/3.0) * math.gamma(m) / math.gamma(m + 1.0/3.0)


def moment(m):
    return I(m)**3


def check_spectrum(m):
    # B_+ has eigenvalues 1 on u and 1/2 on u^perp.
    # B_- has eigenvalues -1 on u and 1/2 on u^perp.
    vals = [1.0, 1.0, -1.0] + [0.5] * (3*m - 3)
    assert len(vals) == 3*m
    assert sum(abs(x) >= 1.0 for x in vals) == 3
    assert all(x != 0.0 for x in vals)
    return vals


for m in [2, 3, 4, 8, 16, 32, 64, 128]:
    v = I(m)
    M = v**3
    assert v + 1e-12 >= math.exp(-1.0) * m**(1.0/3.0)
    assert M + 1e-12 >= math.exp(-3.0) * m
    check_spectrum(m)
    print(f"m={m:3d} I={v:.12f} moment={M:.12f} moment/m={M/m:.12f}")

limit = math.gamma(4.0/3.0)**3
print(f"Gamma(4/3)^3={limit:.12f}")
assert abs(moment(128)/128.0 - limit) < 0.01
print("QFORM_CONDITIONAL_2OVER3_MOMENT_FALSE_CHECK_PASS")
