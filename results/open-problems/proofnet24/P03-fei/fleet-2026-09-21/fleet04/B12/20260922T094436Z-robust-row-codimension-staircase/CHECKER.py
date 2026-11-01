#!/usr/bin/env python3
"""Deterministic arithmetic checker for the robust-row codimension staircase.

This checker verifies only the numerical threshold evaluations used in REPORT.md.
The analytic proof is symbolic: R(q)=h_2(q)/q is strictly decreasing because
R'(q)=log_2(1-q)/q^2<0, and the remaining inequalities are exact rational
consequences of eta=1/16.
"""
from decimal import Decimal, getcontext
from fractions import Fraction

getcontext().prec = 70
D = Decimal
LN2 = D(2).ln()
ETA = Fraction(1, 16)
C = 1 - 2 * ETA  # 7/8


def h2(q: Decimal) -> Decimal:
    return -(q*q.ln() + (D(1)-q)*(D(1)-q).ln()) / LN2


def R(q: Decimal) -> Decimal:
    return h2(q) / q


def q_of_K(K: Decimal) -> Decimal:
    lo, hi = D('1e-50'), D('0.5')
    for _ in range(320):
        mid = (lo + hi) / 2
        # R is strictly decreasing.
        if R(mid) > K:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


rows = []
for m in range(2, 7):
    qstar = D(16) / (D(17) * (D(2) ** (m-1)))
    Km = R(qstar)
    cap = D(8) / (D(8) + D(7)*m)
    rows.append((m, qstar, Km, cap))

K4 = D(4)
q4 = q_of_K(K4)
assert q4 < D(4)/D(17)
assert rows[1][2] < K4 < rows[2][2]  # K3 < 4 < K4
assert Fraction(1, 1) / (Fraction(1, 1) + C*3) == Fraction(8, 29)
assert Fraction(1, 1) / (Fraction(1, 1) + C*4) == Fraction(2, 9)
assert Fraction(1, 1) / (Fraction(1, 1) + C*6) == Fraction(4, 25)

C_RECORD = D('6.521845710923046575')
K_RECORD_PHASE = C_RECORD - D(2)/LN2
q_record = q_of_K(K_RECORD_PHASE)
assert rows[1][2] < K_RECORD_PHASE < rows[2][2]
assert q_record < D(4)/D(17)

print('PASS')
print('eta', ETA)
print('trigger_comparability', C)
for m, qstar, Km, cap in rows:
    print('m', m, 'q_threshold', qstar, 'K_threshold', Km, 'row_fraction_cap', cap)
print('K=4 q_K', q4)
print('K=4 forced_min_codimension', 3)
print('K=4 q_i_over_J_cap', D(8)/D(29))
print('record_phase_calibration_K', K_RECORD_PHASE)
print('record_phase_calibration_q_K', q_record)
print('record_phase_calibration_forced_min_codimension', 3)
print('address_payment_eta_1_16: r_i*q_i <= (8/7)*(J-q_i)')
