from fractions import Fraction
from math import sqrt

# Exact exponent bookkeeping for epsilon=m^{-3/4}, R=m^{1/8}.
e_eps = Fraction(-3,4)
e_R = Fraction(1,8)
e_mean_bank = Fraction(1,2) + e_eps + e_R
e_var_sat = e_eps + 2*e_R
e_third_sat = e_eps + 3*e_R
e_sat_count = 1 + e_eps

assert e_mean_bank == Fraction(-1,8)
assert e_var_sat == Fraction(-1,2)
assert e_third_sat == Fraction(-3,8)
assert e_sat_count == Fraction(1,4)
assert all(x < 0 for x in (e_mean_bank, e_var_sat, e_third_sat))
assert e_sat_count > 0

# Rank-one spectrum identity: B=I-alpha nn^T with ||n||=1 has
# eigenvalues 1,1,1-alpha. alpha=2+1/m -> 1,1,-(1+1/m).
for m in (16, 81, 256, 4096):
    alpha = 2.0 + 1.0/m
    eig3 = 1.0-alpha
    assert abs(eig3 + (1.0+1.0/m)) < 1e-15

def moments(m):
    eps = m**(-0.75)
    ell = 1.0-eps
    R = m**0.125
    mu = R*eps + 0.5*eps*eps
    raw2 = ell**3/12.0 + R*R*eps + R*eps*eps + eps**3/3.0
    var = raw2-mu*mu
    meanY = sqrt(m)*mu
    third_sat = eps*(R+eps)**3
    p_clean = (1.0-eps)**(3*m)
    return eps,R,meanY,var,third_sat,p_clean

print("exponents:",
      "meanY", e_mean_bank,
      "var_sat", e_var_sat,
      "third_sat", e_third_sat,
      "sat_count", e_sat_count)

for m in (10_000, 1_000_000, 100_000_000):
    eps,R,meanY,var,third,pclean = moments(m)
    print(m,
          "gap~", R-0.5,
          "meanY", meanY,
          "var", var,
          "third_sat_bound", third,
          "P(any satellite)", 1.0-pclean)

v = 1.0/12.0
tip = 1.0/(2.0*sqrt(2.0)*v)
assert abs(tip-3.0*sqrt(2.0)) < 1e-14
print("gaussian_tip", tip)
print("PASS QFORM_ALMOST_SURE_SATELLITE_DIVERGING_GAP")
