#!/usr/bin/env python3
from fractions import Fraction
from decimal import Decimal, getcontext

# Exact specialization of the finite-degree slack formula for P0151 at m=2, delta=1.
m = 2
delta = Fraction(1, 1)
A = Fraction(2*m, 1) + delta
a = Fraction(m, 1) + delta
K0 = 4*m + 1  # ceil(4m+delta) when delta=1

p = {}
p[m] = A / (A + m*a)
for k in range(m + 1, K0):
    p[k] = (
        Fraction(m, 1) * (Fraction(k - 1, 1) + delta) * p[k - 1]
        / (A + Fraction(m, 1) * (Fraction(k, 1) + delta))
    )

finite_mass = sum(p.values(), Fraction(0, 1))
tail_mass = Fraction(1, 1) - finite_mass
assert tail_mass > 0

# s(w)=w*min(w,2A)-(2Aw-A^2): (w-A)^2 below 2A, A^2 above.
S_star = sum(
    pk * (Fraction(k, 1) + delta - A) ** 2 for k, pk in p.items()
) + A*A*tail_mass

degree_m_atom_slack = p[m] * Fraction(m*m, 1)
assert S_star >= degree_m_atom_slack > 0
assert S_star <= A*A

getcontext().prec = 50
sqrt6 = Decimal(6).sqrt()
pi_c = Decimal(1) / (Decimal(12) + Decimal(4)*sqrt6)
eta_star = Decimal(2) * pi_c*pi_c
S_decimal = Decimal(S_star.numerator) / Decimal(S_star.denominator)
extra = eta_star * S_decimal / Decimal(25)

print('A =', A)
print('a =', a)
print('K0 =', K0)
for k in sorted(p):
    print(f'p_{k} = {p[k]}')
print('finite_mass =', finite_mass)
print('tail_mass =', tail_mass)
print('S_star =', S_star)
print('S_star_decimal =', S_decimal)
print('degree_m_atom_slack =', degree_m_atom_slack)
print('pi_c_decimal =', pi_c)
print('extra_exponent_gain_decimal =', extra)
