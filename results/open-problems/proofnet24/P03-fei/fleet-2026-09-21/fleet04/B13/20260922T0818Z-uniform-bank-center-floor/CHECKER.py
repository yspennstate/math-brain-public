#!/usr/bin/env python3
from fractions import Fraction

d = Fraction(176114, 10_000_000)              # certified d > 0.0176114
A = Fraction(32275607, 125_000_000)           # 0.258204856 guaranteed AND bank
kbar = Fraction(67635, 1_000_000)             # peer theorem: kappa < 0.067635
B = Fraction(1078193, 1048576)                 # exact center coefficient

assert d - kbar*A > 0

def floor(rho):
    rho = Fraction(rho)
    return (d - kbar*rho*A)/(B + 4*kbar)

vals = [(Fraction(0), floor(0)),
        (Fraction(1,4), floor(Fraction(1,4))),
        (Fraction(1,2), floor(Fraction(1,2))),
        (Fraction(3,4), floor(Fraction(3,4))),
        (Fraction(1), floor(1))]

assert vals[-1][1] > Fraction(1137, 10_000_000)  # > 0.0001137
for i in range(4):
    assert vals[i][1] > vals[i+1][1] > 0

print('PASS')
print('d_minus_kA =', d-kbar*A, float(d-kbar*A))
print('denominator =', B+4*kbar, float(B+4*kbar))
for rho, e in vals:
    print('rho=', rho, 'E_floor=', e, 'decimal=', format(float(e), '.15f'))
print('full_bank_center_floor =', format(6.521851214 + float(vals[-1][1]), '.15f'))
