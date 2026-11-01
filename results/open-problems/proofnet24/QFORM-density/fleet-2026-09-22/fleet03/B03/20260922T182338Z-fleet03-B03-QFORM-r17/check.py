from math import pi, e, sqrt, gamma, sin

# QFORM B03 r17 arithmetic/checker for the bank-level fractional collision splice.
k = 3
r = 5.0/3.0
alpha = r/2.0
p = k*r/8.0
assert abs(alpha - 5.0/6.0) < 1e-15
assert abs(p - 5.0/8.0) < 1e-15
assert p > 0.5

# Integral: int_R (1+(2 sigma t/(pi e))^2)^(-5/8) dt
# = sigma^{-1} * (pi e/2) sqrt(pi) Gamma(1/8)/Gamma(5/8).
I_sigma1 = (pi*e/2.0)*sqrt(pi)*gamma(1.0/8.0)/gamma(5.0/8.0)
C = 2.0/sqrt(pi*(1.0-alpha))*sqrt(I_sigma1)
C_closed = 2.0*sqrt(3.0*e*sqrt(pi)*gamma(1.0/8.0)/gamma(5.0/8.0))
assert abs(C-C_closed) < 1e-12
assert C < 17.426

# General integrability threshold for the unconditional regularized-determinant envelope:
# p_time = k*r/8 > 1/2 iff k*r > 4. With r<2 this is possible iff k>=3.
assert k*r > 4.0
# k=2 cannot satisfy 2*r>4 with r<2; the endpoint r=2 is logarithmic.
assert 2.0*1.999999 < 4.0

s0 = 4.0*sin(0.5)**2
fejer_interval_factor = pi/s0

print(f"alpha={alpha:.15f}")
print(f"time_power={p:.15f}")
print(f"I_sigma1={I_sigma1:.15f}")
print(f"C_bank3={C:.15f}")
print(f"fejer_interval_factor={fejer_interval_factor:.15f}")
print("rank_threshold=k>=3 for this RD + fractional-collision splice")
print("QFORM_B03_R17_CHECK_PASS")
