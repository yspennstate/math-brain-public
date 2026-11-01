import math

# Critical m=2 endpoint from REPORT.md
pi = math.pi
t0 = pi * math.e / math.sqrt(2.0)
t2 = 2.0 * pi
ratio = t2 / t0
H = math.sqrt(2.0/pi) * 2.0 * math.sqrt(t0) * (2.0 + max(0.0, math.log(ratio)))

assert abs(ratio - (2.0*math.sqrt(2.0)/math.e)) < 1e-14
assert H < 8.0

# Exponent identities in the subcritical hybrid theorem.
for beta in (0.01, 0.1, 0.25, 0.49):
    alpha = beta/(2.0*(1.0-beta))
    delta = (1.0-2.0*beta)/(2.0*(1.0-beta))
    assert abs((alpha+delta)-0.5) < 1e-14
    # Delta^{-1} exponent tends from 1/4 to 0 as beta goes 0 -> 1/2.
    det_exp = (1.0-2.0*beta)/(4.0*(1.0-beta))
    assert 0.0 < det_exp < 0.25

print(f"t0={t0:.15f}")
print(f"t2={t2:.15f}")
print(f"ratio={ratio:.15f}")
print(f"critical_half_riesz_bound={H:.15f}")
print("QFORM_B03_HYBRID_TIME_PASS")
