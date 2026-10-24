from fractions import Fraction
from math import log, log2

# Exact certificate for h_2(1/6) < 2/3:
# 6 log_2 6 - 5 log_2 5 < 4  <=>  6^6 < 16*5^5.
assert 6**6 < 16 * 5**5

# Exact finite Taylor lower bound proving exp(7/10)>2, hence ln 2 < 7/10.
exp_partial = (
    Fraction(1, 1)
    + Fraction(7, 10)
    + Fraction(49, 200)
    + Fraction(343, 6000)
)
assert exp_partial > 2

# Display-only decimal evaluation of the analytic constants used in REPORT.md.
# The theorem itself depends only on the exact formulas and inequalities above.
lambda4 = Fraction(7, 44) * log2(Fraction(17, 16))
phase_coeff = Fraction(128, 105) * lambda4
hidden_coeff = Fraction(64, 105) * lambda4
J_coeff = phase_coeff * 2 / log(2)
heavy_J_1_16 = (J_coeff / 4) / Fraction(1, 16)
heavy_U_1_16 = (hidden_coeff / 4) / Fraction(1, 16)

print("CERT h2(1/6)<2/3:", 6**6, "<", 16 * 5**5)
print("CERT ln2<7/10 exp-series partial:", float(exp_partial), "> 2")
print("lambda4 =", float(lambda4))
print("phase_coeff =", float(phase_coeff))
print("hidden_coeff =", float(hidden_coeff))
print("J_coeff =", float(J_coeff))
print("tau=1/16 robust-mass J coeff =", float(heavy_J_1_16))
print("tau=1/16 robust-mass U4 coeff =", float(heavy_U_1_16))
print("RESULT PASS")
