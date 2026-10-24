#!/usr/bin/env python3
"""Arithmetic checker for B12 zero-credit MUX collar.

This checks only the NEW collar budget in REPORT.md.  It does not regenerate
or certify the binary h96 candidate.  Source premises imported by the report:
  * base zero-credit-line reserve Z(s) > 1/64;
  * h96 upper/slope envelope constants;
  * exact six-mass Boolean MUX identities.
"""
from fractions import Fraction
from math import e, log2

ETA = Fraction(1, 2**15)
BASE = Fraction(1, 64)
TARGET = Fraction(1, 128)

# L1 coefficient bound in REPORT (4.2)-(4.3), using E,T <= 1/64.
coef_E = Fraction(3, 1) + Fraction(1, 32) + Fraction(49, 1024)
coef_T = Fraction(4, 1) + Fraction(1, 32) + Fraction(81, 1024)
assert coef_E < 5 and coef_T < 5

# New perturbation budget.
linear = 160 * ETA
fannes = Fraction(165, 65536)
small_entropy = Fraction(1, 2**22)
loss = linear + fannes + small_entropy
reserve = BASE - loss
assert loss < TARGET
assert reserve > TARGET

# Source-envelope numerical diagnostics used only to verify the deliberately
# rounded constants in the written proof.
alpha = 4.9096
wplus = 8.629
alift = 0.268204856
Cdag = 6.521851214

# max v log2(1/v) = 1/(e ln 2), and report rounds it upward by 0.531.
assert 1.0 / (e * __import__('math').log(2.0)) < 0.531
gamma_global_upper = alpha * 0.531 + wplus / 2 + alift / 4
assert gamma_global_upper < 7.0
assert gamma_global_upper + 1.0 < 8.0

eta = float(ETA)
# Output symmetric representative is at least 1/4-eta-eta^2.
vout = 0.25 - eta - eta * eta
xout = log2(1.0 / vout)
deriv_output_bound = alpha * xout + wplus + 31 * 1.5 + alift
assert xout < 2.001
assert deriv_output_bound < 66.0

vcenter = 0.5 - eta
xcenter = log2(1.0 / vcenter)
deriv_center_bound = alpha * xcenter + wplus + 31 * 1.5 + alift
assert xcenter < 1.001
assert deriv_center_bound < 66.0

# h_2(2^-28) <= 2^-28(28+log2 e), log2 e < 3/2.
hsmall_bound = (2.0**-28) * 29.5
assert 1.5 * hsmall_bound < 2.0**-22

# Fannes bound: delta <= 5/32768 and
# h2(delta)+delta log2 5 <= delta log2(5e/delta)
# < (5/32768)*(15+3/2) = 165/65536.
delta = 5.0 / 32768.0
fannes_analytic = delta * (15.0 + log2(e))
assert fannes_analytic < float(fannes)

print('ZERO_CREDIT_MUX_COLLAR_CHECK=PASS')
print(f'eta={float(ETA):.15g}')
print(f'l1_coef_E={float(coef_E):.15g}')
print(f'l1_coef_T={float(coef_T):.15g}')
print(f'gamma_global_upper={gamma_global_upper:.15g}')
print(f'deriv_center_bound={deriv_center_bound:.15g}')
print(f'deriv_output_bound={deriv_output_bound:.15g}')
print(f'linear_budget={float(linear):.15g}')
print(f'fannes_budget={float(fannes):.15g}')
print(f'small_entropy_budget={float(small_entropy):.15g}')
print(f'total_loss={float(loss):.15g}')
print(f'base_floor={float(BASE):.15g}')
print(f'proved_reserve={float(reserve):.15g}')
print(f'target_reserve={float(TARGET):.15g}')
