from fractions import Fraction as F

lo = F(792847, 2000000)   # 0.3964235
hi = F(991059, 2500000)   # 0.3964236

def P(z):
    return 46818*z**6 - 113508*z**5 + 112815*z**4 - 58105*z**3 + 16065*z**2 - 2193*z + 108

def P1(z):
    return 280908*z**5 - 567540*z**4 + 451260*z**3 - 174315*z**2 + 32130*z - 2193

def P2(z):
    return 1404540*z**4 - 2270160*z**3 + 1353780*z**2 - 348630*z + 32130

def P3(z):
    return 5618160*z**3 - 6810480*z**2 + 2707560*z - 348630

def P4(z):
    return 16854480*z**2 - 13620960*z + 2707560

def P5(z):
    return 33708960*z - 13620960

# P6 = 33708960 > 0. Therefore P5 is increasing. The endpoint sign chain below
# implies successively: P5<0, P4<0, P3>0, P2<0, P1<0 throughout [lo,hi].
checks = {
    "P_lo": P(lo),
    "P_hi": P(hi),
    "P5_hi": P5(hi),
    "P4_lo": P4(lo),
    "P3_hi": P3(hi),
    "P2_hi": P2(hi),
    "P1_lo": P1(lo),
}

assert checks["P_lo"] > 0
assert checks["P_hi"] < 0
assert checks["P5_hi"] < 0
assert checks["P4_lo"] < 0
assert checks["P3_hi"] > 0
assert checks["P2_hi"] < 0
assert checks["P1_lo"] < 0

print("ALL_FRONTIER_CHECKS_PASS")
for name, value in checks.items():
    print(f"{name}={value} ~= {float(value):.16g}")
print("Conclusion: P is strictly decreasing on [0.3964235,0.3964236] and has a unique root there.")
