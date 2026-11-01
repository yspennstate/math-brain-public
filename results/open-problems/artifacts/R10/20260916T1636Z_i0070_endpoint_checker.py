#!/usr/bin/env python3
from fractions import Fraction

print("R10 I0070 endpoint algebra checker")
print("All arithmetic below is exact rational arithmetic.")

for rho_i in range(1, 11):
    rho = Fraction(rho_i, 1)
    beta = Fraction(rho_i + 2, 2 * (rho_i + 1))
    s = 2 * beta - 1
    critical = (2 * beta - 1) * (rho + 1)
    scale_lhs = beta * (rho + 1)
    scale_rhs = rho / 2 + 1

    # High-frequency point-evaluation test used in the report:
    # ||f_N||_L2 ~ 1, |f_N(0)| ~ N^(1/2), ||f_N||_{B^s_{2,1}} ~ N^s.
    # The local Lipschitz derivative ratio grows like N^(1-s), while a
    # candidate source growth factor with exponent q grows like N^(s q).
    # Hence q >= (1-s)/s. At the source-admissible critical relation this
    # lower bound is exactly rho.
    rho_min = (1 - s) / s

    assert critical == 1
    assert s == Fraction(1, rho_i + 1)
    assert scale_lhs == scale_rhs
    assert rho_min == rho

    print(
        f"rho={rho_i:2d} beta={beta} s=2beta-1={s} "
        f"critical={critical} beta(rho+1)={scale_lhs} "
        f"rho_min={rho_min}"
    )

# Frozen special model used in the report.
rho = Fraction(1, 1)
beta = Fraction(3, 4)
s = Fraction(1, 2)
assert (2 * beta - 1) * (rho + 1) == 1
assert -1 + 2 * beta == s
assert beta * (rho + 1) == Fraction(3, 2)

print("special_model: rho=1 beta=3/4 spatial_real_interpolation_index=1/2")
print("single_scale_saturation: beta*(rho+1)=rho/2+1=3/2")
print("PASS")
