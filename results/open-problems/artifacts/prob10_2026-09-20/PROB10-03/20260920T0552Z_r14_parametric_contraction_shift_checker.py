#!/usr/bin/env python3
from fractions import Fraction as F

# Exact constants imported from the already-executed NM13-07 alpha=12.75 certificate.
A = [
    [F(-1601,20), F(-493,12500)],
    [F(-60418,25), F(-5789,2500)],
]
r = [F(1,10_000_000), F(1,250_000)]
q = F(23849,25000)

# Sharper rational ceilings read directly from the archived center intervals:
# |H(x_c)| < 1.214e-12 and |alpha(x_c)-12.75| < 1.203e-11.
EH = F(607,500_000_000_000_000)
EA = F(1203,100_000_000_000_000)

# New exact density decrement.
delta = F(78251,1_000_000_000_000)

margin = 1-q
base = []
slope = []
eta = []
for i in range(2):
    b = F(1,r[i])*(abs(A[i][0])*EH + abs(A[i][1])*EA)
    s = F(1,r[i])*abs(A[i][1])
    e = b + s*delta
    base.append(b); slope.append(s); eta.append(e)

delta_max = min((margin-base[i])/slope[i] for i in range(2))
assert delta < delta_max
assert max(eta) < margin

alpha_L = F(630297437506,10**11)
alpha_U_old = F(51,4)
alpha_U_new = alpha_U_old-delta
width_old = alpha_U_old-alpha_L
width_new = alpha_U_new-alpha_L

assert alpha_U_new == F(12749999921749,10**12)
assert width_new == F(6447025546689,10**12)
assert width_old-width_new == delta

print("Q", q, float(q))
print("ONE_MINUS_Q", margin, float(margin))
for i in range(2):
    print(f"ROW_{i}_BASE", base[i], float(base[i]))
    print(f"ROW_{i}_SHIFT_SLOPE", slope[i], float(slope[i]))
    print(f"ROW_{i}_ETA_SHIFTED", eta[i], float(eta[i]))
    print(f"ROW_{i}_SLACK", margin-eta[i], float(margin-eta[i]))
print("DELTA_MAX_FROM_CURRENT_BOX", delta_max, float(delta_max))
print("CHOSEN_DELTA", delta, float(delta))
print("ALPHA_U_OLD", alpha_U_old, float(alpha_U_old))
print("ALPHA_U_NEW", alpha_U_new, float(alpha_U_new))
print("WIDTH_OLD", width_old, float(width_old))
print("WIDTH_NEW", width_new, float(width_new))
print("WIDTH_GAIN", width_old-width_new, float(width_old-width_new))
print("ALL_EXACT_PARAMETRIC_SHIFT_CHECKS_PASS")