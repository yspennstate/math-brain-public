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

# New cycle-rate upper bound from transformed-cost and progress moments.
a_hat = (U - a0 * eta_lo) / (F(4) - eta_lo)
a_prev = F(1032894873580371, 2000000000000000)


def log_bounds(x, N=160):
    """Exact rational lower/upper bounds for log(x), x>0."""
    if x == 1:
        return F(0), F(0)
    if x < 1:
        lo, hi = log_bounds(1 / x, N)
        return -hi, -lo
    z = (x - 1) / (x + 1)
    assert 0 < z < 1
    s = F(0)
    zpow = z
    z2 = z * z
    for k in range(N + 1):
        s += zpow / F(2 * k + 1)
        zpow *= z2
    lo = 2 * s
    tail = 2 * zpow / (F(2 * N + 3) * (1 - z2))
    return lo, lo + tail


# Axis improvement.
assert a_hat < a_prev
assert a_prev - a_hat > F(51, 10**9)  # >5.1e-8

# Critical slope rho_* = ((r-1)a_hat-log A)/log B.
LAlo, LAhi = log_bounds(A)
LBlo, LBhi = log_bounds(B)
const = (r - 1) * a_hat
rho_lo = (const - LAhi) / LBhi
rho_hi = (const - LAlo) / LBlo
assert rho_lo > F(1356755215, 10**9)          # 1.356755215
assert rho_hi < F(169594402, 125000000)       # 1.356755216

# Closed new cone at rho0=1.3567554.
rho0 = F(6783777, 5000000)
c = F(2582237, 5000000)                       # 0.5164474
s = F(39825001, 10000000)                     # r-1 + 1e-7
q = r / (1 + s)
assert q == F(49825000, 49825001)
beta_hat = F(9999999, 10000000)

LQlo, LQhi = log_bounds(1 / q, 80)
LBHlo, LBHhi = log_bounds(1 / beta_hat, 80)
logbeta_hi = -LAlo - rho0 * LBlo + s * c - (1 + rho0) * LQlo
log_betahat_lo = -LBHhi
assert logbeta_hi < log_betahat_lo

delta = 2 * (c - a_hat)
assert delta > 0

# Canonical ten-local prefactor: K<2e14. Here 1/(1-q)=49,825,001,
# so C=K/(1-q)<1e22 exactly.
assert 200000000000000 * 49825001 < 10**22

# Explicit finite transfer at m=10^16.
m = 10**16
endpoint_hat = F(1129, 10**11)                 # 1.129e-8
assert endpoint_hat * endpoint_hat > F(2) * vbar / (d_lo * m)

# beta_hat^m <= exp(-m/10^7)=exp(-10^9). Since e>2 and
# 2^1000>10^300, beta_hat^m<10^-300. Thus
# 2*c*C*beta_hat^m < 2*10^22*10^-300 < 10^-270.
assert 2**1000 > 10**300
lower_residual = delta - endpoint_hat - F(3, m) - F(1, 10**270)
assert lower_residual > F(17, 10**9)

print("ALL_EXACT_CHECKS_PASS = True")
print("a_prev_decimal = %.18g" % float(a_prev))
print("eta_interval = [%.18g, %.18g]" % (float(eta_lo), float(eta_hi)))
print("d_lo_decimal = %.18g" % float(d_lo))
print("a_hat_fraction = %s" % a_hat)
print("a_hat_decimal = %.18g" % float(a_hat))
print("axis_improvement_decimal = %.18g" % float(a_prev - a_hat))
print("rho_star_certified_bracket = (1.356755215, 1.356755216)")
print("rho0_decimal = %.7f" % float(rho0))
print("c_decimal = %.7f" % float(c))
print("delta_fraction = %s" % delta)
print("delta_decimal = %.18g" % float(delta))
print("q_fraction = %s" % q)
print("logbeta_upper_decimal = %.18g" % float(logbeta_hi))
print("log_beta_hat_lower_decimal = %.18g" % float(log_betahat_lo))
print("endpoint_error_bound_decimal = %.18g" % float(endpoint_hat))
print("finite_residual_lower_decimal = %.18g" % float(lower_residual))
