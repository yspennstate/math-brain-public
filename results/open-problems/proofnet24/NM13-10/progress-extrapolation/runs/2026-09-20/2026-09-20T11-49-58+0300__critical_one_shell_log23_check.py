import math

# NM13-10 critical one-shell excursion/hitting checker.
# This is a sanity checker for constants used in the analytic proof.
# The proof itself is in the run report.

def young_margin(delta, t):
    p = 3.0 - 2.0*delta
    lhs = -delta + (p-1.0)*t + 0.5*(p-1.0)*t*t
    rhs = -0.5*delta + 136.0*(delta**(-(p-1.0)))*(t**p)
    return rhs-lhs

# Dense log grid for the pointwise p-generator inequality.
min_margin = float("inf")
worst = None
for i in range(401):
    if i == 400:
        delta = 0.5
    else:
        a = math.log(1e-6)
        b = math.log(0.5)
        delta = math.exp(a + (b-a)*i/400.0)
    for j in range(2401):
        a = math.log(1e-10)
        b = math.log(1e6)
        t = math.exp(a + (b-a)*j/2400.0)
        m = young_margin(delta, t)
        if m < min_margin:
            min_margin = m
            worst = (delta, 3.0-2.0*delta, t)

small_case_ratio = 0.25 + 0.5/64.0
large_case_constant = 128 + 8

max_log_violation = -float("inf")
log_worst = None
for j in range(50001):
    s = 10.0*j/50000.0
    if s <= 0.5:
        u = -s
    else:
        u = -0.5
    lhs = -1.0-u-u*u+0.5*s*s
    violation = lhs - s**3
    if violation > max_log_violation:
        max_log_violation = violation
        log_worst = (s, u, lhs)

excursion_crude = 272.0*3.0*math.log(2.0)/(0.75)
large_rho_coeff = 755.0*math.e**2/9.0 + 16.0/36.0
small_rho_trivial = math.e**6
K = 621.0
C = 50.0
quantile_factor = K/(C**3) * (1.0 + 3.0*math.log(C) + 2.0/math.e)**2

print("NM13-10 critical one-shell checker")
print(f"minimum sampled Young margin RHS-LHS = {min_margin:.12e}")
print("worst sampled (delta,p,t) =", tuple(f"{x:.12e}" for x in worst))
print(f"small-case ratio upper = {small_case_ratio:.12f} < 0.5")
print(f"large-case constant = {large_case_constant} = 136")
print(f"max sampled log-drift violation = {max_log_violation:.12e}")
print("log-drift worst sampled (s,u,lhs) =", tuple(f"{x:.12e}" for x in log_worst))
print(f"crude excursion coefficient = {excursion_crude:.12f} < 755")
print(f"large-rho tail coefficient = {large_rho_coeff:.12f} < 621")
print(f"small-rho trivial coefficient e^6 = {small_rho_trivial:.12f} < 621")
print(f"quantile factor for C=50 = {quantile_factor:.12f} < 1")
assert min_margin >= -1e-9
assert small_case_ratio < 0.5
assert large_case_constant == 136
assert max_log_violation <= 1e-12
assert excursion_crude < 755.0
assert large_rho_coeff < K
assert small_rho_trivial < K
assert quantile_factor < 1.0
print("CHECK_PASS")
