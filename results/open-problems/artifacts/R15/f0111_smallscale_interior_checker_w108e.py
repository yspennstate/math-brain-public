"""Exact rational self-check for R15 retained F0111 small-scale theorem.

This checker validates only finite rational inequalities used in the proof that the
coarse necessary gap is positive throughout both remaining N=12,13 scalar cells
for 0<s<=10^-4.  It says nothing about native I0076 and is not an independent audit.
"""
from fractions import Fraction as F
from math import factorial

SMAX = F(1, 10000)


def UK(d, s):
    d, s = F(d), F(s)
    return F(29)*(d+1)*(d+s+1)*(d+2*s+1) / (4*(s+1)*(s+2))


def exp_lower(q, n):
    q = F(q)
    return sum(q**j / F(factorial(j)) for j in range(n+1))


# 1. Outer d walls imply the uniform x-slope roof (x-1)/s < 9/10.
d12 = F(49,100) - SMAX/F(4)       # 19599/40000
d13 = F(53,100) - SMAX/F(5)       # 26499/50000
assert d12 == F(19599,40000)
assert d13 == F(26499,50000)

# The numerator of 9/10-(x-1)/s is
# 2d^2+6ds+8d-5s^2-9s-4 over the positive denominator.
# It increases in d and decreases in s throughout the relevant region, so its
# worst N=12 point is (d12,SMAX); N=13 has a larger d floor.
def xroof_numerator(d, s):
    return 2*d*d + 6*d*s + 8*d - 5*s*s - 9*s - 4

xroof_margin = xroof_numerator(d12, SMAX)
assert xroof_margin == F(319475949,800000000) > 0
assert d13 > d12

# 2. U_K monotonicity plus the upper d walls gives eta=U_K-N<1/4.
eta12_margin = F(49,4) - UK(F(1,2), SMAX)
eta13_margin = F(53,4) - UK(F(7,13), SMAX)
assert eta12_margin == F(2002077,133353334) > 0
assert eta13_margin == F(29056383467,585954549596) > 0

# 3. L_K is increasing in d,s and L_K(d,0)=6/(1-d).
# The lower d walls are strictly above 19/39 and 67/127 respectively,
# giving L_K>117/10 and >127/10.  Combining with the U_K roofs yields c_K<21/20.
assert d12 > F(19,39)
assert d13 > F(67,127)
assert F(6)/(1-F(19,39)) == F(117,10)
assert F(6)/(1-F(67,127)) == F(127,10)
assert F(49,4)/F(117,10) < F(21,20)
assert F(53,4)/F(127,10) < F(21,20)

# 4. Exact Taylor lower bounds proving q2<29/5 (N=12) and q2<59/10 (N=13).
# u2 < 20(C+9/10): 318 and 358 respectively.
exp58 = exp_lower(F(29,5), 10)
exp59 = exp_lower(F(59,10), 11)
assert exp58 > 318
assert exp59 > 358
exp58_margin = exp58 - 318
exp59_margin = exp59 - 358

# 5. L=log S>12 on s<=1e-4 was certified in v107d.  Consequently eps<1/400,
# t<401/400.  With eta<1/4 and c_K<21/20,
# t(1+eta/2)c_K < (401/400)(9/8)(21/20).
prod = F(401,400)*F(9,8)*F(21,20)
assert prod == F(75789,64000) > 1

# D=-k/29 < (13/232)s, so eta D < (13/928)s.
etad_coeff = F(13,928)
K_bracket_loss = (prod-1)*etad_coeff
assert K_bracket_loss == F(153257,59392000)

# 6. Complete rational lower margin for t * overline_Gamma_N divided by s.
# Contributions:
# + c C
# - c etaD/s
# - eps B q2/s, with eps<1/400 and B<(C+9/10)s
# - (eps^2/2) B log^2 B /s <= (c^2/2)(C+9/10)
# - (eps^2/2) A log^2 A /s, using A log^2 A <= (Cs)^2/A and s<=1e-4
# - t eps Umax q1 q2 /s <= (401/400)c(9/8)q2
# - the possible negative K-bracket term.
C_ADAPT = F(3,100)

def total_margin(C, q2roof):
    beta = F(C)+F(9,10)
    entropy_eta_loss = C_ADAPT*etad_coeff
    entropy_B_loss = F(1,400)*beta*q2roof
    variance_B_loss = F(9,20000)*beta     # c^2/2 = 9/20000
    variance_A_loss = F(C*C,3200000000) / (1-F(C,10000))
    energy_loss = F(401,400)*C_ADAPT*F(9,8)*q2roof
    margin = (C_ADAPT*C - entropy_eta_loss - entropy_B_loss
              - variance_B_loss - variance_A_loss
              - energy_loss - K_bracket_loss)
    return margin, (entropy_eta_loss, entropy_B_loss, variance_B_loss,
                    variance_A_loss, energy_loss, K_bracket_loss)

m12, parts12 = total_margin(15, F(29,5))
m13, parts13 = total_margin(17, F(59,10))
assert m12 == F(38709573299,2965145600000) > 0
assert m13 == F(523190108977,14822758400000) > 0

print("X_SLOPE_ROOF_PASS", xroof_margin)
print("ETA12_MARGIN_PASS", eta12_margin)
print("ETA13_MARGIN_PASS", eta13_margin)
print("EXP_5P8_MARGIN_PASS", exp58_margin)
print("EXP_5P9_MARGIN_PASS", exp59_margin)
print("N12_SMALLS_GAP_MARGIN_PASS", m12, float(m12))
print("N13_SMALLS_GAP_MARGIN_PASS", m13, float(m13))
print("SMALLS_INTERIORS_N12_N13_EXCLUDED")
print("ALL_EXACT_CHECKS_PASS")
