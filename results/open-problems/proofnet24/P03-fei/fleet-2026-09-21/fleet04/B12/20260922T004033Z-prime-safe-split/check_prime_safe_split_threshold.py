#!/usr/bin/env python3
from decimal import Decimal, getcontext
from fractions import Fraction

getcontext().prec = 100

H_LO = Decimal("6.776605309005978082519790221891882314787235038")
H_HI = Decimal("6.776605309005978082519790221891882314787235039")
I = Decimal(261) / Decimal(128)
C0 = Decimal("6.4548")
C_STAR = Decimal("0.2681828")
AND_FLOOR = Decimal("0.0043974201")

P = (I - Decimal(1)) / Decimal(4)
assert P == Decimal(133) / Decimal(512)

c_lo = Decimal(4) * (H_LO / (I - Decimal(1)) - C0)
c_hi = Decimal(4) * (H_HI / (I - Decimal(1)) - C0)

assert c_lo > C_STAR
assert C_STAR / AND_FLOOR > Decimal("60.986")
assert C0 + c_lo / Decimal(4) == H_LO / (I - Decimal(1))

# At threshold C_STAR, the certified n=18 gate has strictly negative
# corrected slack S_c = D + c P = (c - c_G) P.
slack_upper = (C_STAR - c_lo) * P
assert slack_upper < 0

# Pure algebra sanity for the safe-split barycenter:
# if all child margins <= c and the residual margin <= c, then any
# nonnegative weighted barycenter is <= c.
cases = 0
for a in range(0, 8):
    for b in range(0, 8):
        for q in range(1, 8):
            A, B, Q = map(Decimal, (a,b,q))
            for x0_num in range(-5, 6):
                for x1_num in range(-5, 6):
                    for xr_num in range(-5, 6):
                        x0 = C_STAR - Decimal(x0_num*x0_num)/Decimal(1000)
                        x1 = C_STAR - Decimal(x1_num*x1_num)/Decimal(1000)
                        xr = C_STAR - Decimal(xr_num*xr_num)/Decimal(1000)
                        parent = (A*x0+B*x1+Q*xr)/(A+B+Q)
                        assert parent <= C_STAR
                        cases += 1

print("PASS")
print("I_seed =", I)
print("P_seed =", P)
print("c_seed_lower =", c_lo)
print("c_seed_upper =", c_hi)
print("chosen_threshold =", C_STAR)
print("threshold_gap_lower =", c_lo-C_STAR)
print("threshold_over_AND_floor =", C_STAR/AND_FLOOR)
print("corrected_slack_upper_at_threshold =", slack_upper)
print("cap_lower_from_seed =", C0+c_lo/Decimal(4))
print("synthetic_barycenter_cases =", cases)
