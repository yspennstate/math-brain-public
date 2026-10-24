#!/usr/bin/env python3
"""Self-check algebra/numerics for account03/B14 gate restriction reserve.

This is a numerical consistency check, not a proof authority.
"""
from decimal import Decimal, getcontext
import random

getcontext().prec = 80

C0 = Decimal("6.4548")
CN_LO = Decimal("6.5218457109230465756581439729485784683666622922105")
CN_HI = Decimal("6.5218457109230465756581439729485784683666622931729")
C_N_LO = Decimal(4) * (CN_LO - C0)
C_N_HI = Decimal(4) * (CN_HI - C0)
REFUND_HI = C_N_HI / Decimal(4)
PRINTED_DEFICIT = Decimal("7.0237") - Decimal("6.4548")
PRINTED_REMAINDER = PRINTED_DEFICIT - REFUND_HI

def phi(x):
    return x * (1.0 - x)

rng = random.Random(20260922003943)
max_abs_error = 0.0
min_reserve = 1.0
for _ in range(200000):
    t = rng.random()
    q0 = rng.random()
    q1 = rng.random()
    delta = abs(q1 - q0)
    # Any coupling of two Bernoulli variables with means q0,q1 has
    # disagreement d in [|q1-q0|, min(q0+q1,2-q0-q1)].
    dmax = min(q0 + q1, 2.0 - q0 - q1)
    if dmax < delta:
        dmax = delta
    d = delta + (dmax - delta) * rng.random()
    q = (1.0 - t) * q0 + t * q1

    direct = (4.0*t*(1.0-t)*d)/4.0 - (
        phi(q) - ((1.0-t)*phi(q0) + t*phi(q1))
    )
    closed = t*(1.0-t)*(d - (q1-q0)**2)
    max_abs_error = max(max_abs_error, abs(direct - closed))
    min_reserve = min(min_reserve, closed)
    if closed < -2e-15 or closed > 0.250000000000002:
        raise AssertionError((t,q0,q1,d,direct,closed))

print("cN_lo =", C_N_LO)
print("cN_hi =", C_N_HI)
print("max_one_step_quadratic_refund_hi =", REFUND_HI)
print("printed_blind_deficit =", PRINTED_DEFICIT)
print("printed_remainder_after_max_refund =", PRINTED_REMAINDER)
print("random_admissible_trials = 200000")
print("max_abs_identity_error =", f"{max_abs_error:.17g}")
print("min_sampled_reserve =", f"{min_reserve:.17g}")
print("PASS")
