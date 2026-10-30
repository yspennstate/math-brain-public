import math


def ridge_const(q, r, sigma):
    theta = 3 / (1 + r*r)
    return math.sqrt(math.e) / (math.sqrt(2*q) * r * sigma) * theta / (theta - 2*q)

# Exact-range corollary, leverage 1/18.
ell = 1/18
delta = 0.5 - math.sqrt(2*ell) - ell
r = 1 / math.sqrt(6)
q = 1
theta = 3 / (1 + r*r)
h = ell / delta
C = ridge_const(q, r, delta)
print("exact_1_18", delta, h, theta, C)
assert h <= q/2 + 1e-14
assert theta > 2*q

# Exact-range corollary, leverage 1/16.
ell = 1/16
delta = 0.5 - math.sqrt(2*ell) - ell
r = 1/20
q = 149/100
theta = 3 / (1 + r*r)
h = ell / delta
C = ridge_const(q, r, delta)
print("exact_1_16", delta, h, q/2, theta, 2*q, C)
assert h < q/2
assert theta > 2*q

# Full spectral-window corollary.
ell = 1/20
tau = 1/128
delta = 0.5 - math.sqrt(2*ell) - ell
sigma = delta - tau
r = 1/2
q = 11/10
h = (math.sqrt(ell/delta) + tau/(r*sigma))**2
theta = 3 / (1 + r*r)
C = ridge_const(q, r, sigma)
print("window_1_20", delta, sigma, h, q/2, theta, 2*q, C)
assert sigma > 0
assert h < q/2
assert theta > 2*q

# Partner-family robust perturbation.
eps = 1/1024
L0factor = 1 - eps
ell0 = 3/128
tau = 1/32
ell = (math.sqrt(ell0) + eps/(tau*L0factor))**2
delta = 0.5 - math.sqrt(2*ell) - ell
sigma = delta - tau
r = 3/5
q = 1
h = (math.sqrt(ell/delta) + tau/(r*sigma))**2
theta = 3 / (1 + r*r)
C_L0 = ridge_const(q, r, sigma)
C_L = C_L0 / L0factor
print("partner", ell, delta, sigma, h, q/2, theta, 2*q, C_L0, C_L)
assert sigma > 0
assert h < q/2
assert theta > 2*q
assert C_L < 120

frontier = 39/98 - 3*math.sqrt(30)/49
print("exact_range_limit_ell", frontier)
print("QFORM_B08_R30_CHECK_PASS")
