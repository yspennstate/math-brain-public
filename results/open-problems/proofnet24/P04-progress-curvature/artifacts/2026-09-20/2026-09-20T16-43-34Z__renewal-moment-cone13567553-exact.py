from fractions import Fraction as F

Q = 10**15
A = F(3889, 2000)
B = F(27893, 10000)
r = F(1993, 400)
a0 = F(16139, 31250)
U = F(2065789747160742, Q)
eta_lo = F(332278145403783, Q)
eta_hi = F(332278145403789, Q)
vbar = F(2334416160657687, Q)
d_lo = F(4) - eta_hi

a_hat = (U - a0 * eta_lo) / (F(4) - eta_lo)
a_prev = F(1032894873580371, 2000000000000000)


def log_bounds(x, N=160):
    if x == 1:
        return F(0), F(0)
    if x < 1:
        lo, hi = log_bounds(1 / x, N)
        return -hi, -lo
    z = (x - 1) / (x + 1)
    assert 0 < z < 1
    s = F(0)
    zp = z
    z2 = z * z
    for k in range(N + 1):
        s += zp / F(2 * k + 1)
        zp *= z2
    lo = 2 * s
    tail = 2 * zp / (F(2 * N + 3) * (1 - z2))
    return lo, lo + tail


assert a_hat < a_prev
assert a_prev - a_hat > F(51, 10**9)

LAlo, LAhi = log_bounds(A)
LBlo, LBhi = log_bounds(B)
const = (r - 1) * a_hat
rho_lo = (const - LAhi) / LBhi
rho_hi = (const - LAlo) / LBlo
assert rho_lo > F(1356755215, 10**9)      # 1.356755215
assert rho_hi < F(169594402, 125000000)   # 1.356755216

rho0 = F(13567553, 10000000)               # 1.3567553
c = F(51644739, 100000000)                 # 0.51644739
s = F(39825001, 10000000)                  # (r-1)+1e-7
q = r / (1 + s)
assert q == F(49825000, 49825001)
beta_hat = F(19999999, 20000000)           # 0.99999995

LQlo, LQhi = log_bounds(1 / q, 80)
LBHlo, LBHhi = log_bounds(1 / beta_hat, 80)
logbeta_hi = -LAlo - rho0 * LBlo + s * c - (1 + rho0) * LQlo
log_betahat_lo = -LBHhi
assert logbeta_hi < log_betahat_lo

delta = 2 * (c - a_hat)
assert delta > 0

# Canonical ten-local prefactor K<2e14 and 1/(1-q)=49,825,001.
assert 200000000000000 * 49825001 < 10**22

# Finite strict-triangle transfer at m=2e17.
m = 2 * 10**17
endpoint_hat = F(2523, 10**12)             # 2.523e-9
assert endpoint_hat * endpoint_hat > F(2) * vbar / (d_lo * m)

# beta_hat=1-1/(2e7), and m=(2e7)*1e10. Hence beta_hat^m<e^-1e10.
# Since e>2 and 2^1000>10^300, the resulting lower-tail contribution,
# even with C<1e22, is <1e-270.
assert m // 20000000 == 10000000000
assert 2**1000 > 10**300
lower_residual = delta - endpoint_hat - F(3, m) - F(1, 10**270)
assert lower_residual > F(59, 10**10)       # >5.9e-9

print("ALL_EXACT_CHECKS_PASS = True")
print("a_prev_decimal = %.18g" % float(a_prev))
print("eta_interval = [%.18g, %.18g]" % (float(eta_lo), float(eta_hi)))
print("d_lo_decimal = %.18g" % float(d_lo))
print("a_hat_fraction = %s" % a_hat)
print("a_hat_decimal = %.18g" % float(a_hat))
print("axis_improvement_decimal = %.18g" % float(a_prev - a_hat))
print("rho_star_certified_bracket = (1.356755215, 1.356755216)")
print("rho0_decimal = %.7f" % float(rho0))
print("c_decimal = %.8f" % float(c))
print("delta_fraction = %s" % delta)
print("delta_decimal = %.18g" % float(delta))
print("q_fraction = %s" % q)
print("beta_hat_decimal = %.8f" % float(beta_hat))
print("logbeta_upper_decimal = %.18g" % float(logbeta_hi))
print("log_beta_hat_lower_decimal = %.18g" % float(log_betahat_lo))
print("endpoint_error_bound_decimal = %.18g" % float(endpoint_hat))
print("finite_residual_lower_decimal = %.18g" % float(lower_residual))
