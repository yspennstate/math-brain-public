#!/usr/bin/env python3
import math
import numpy as np

SEED = 20260920
rng = np.random.default_rng(SEED)

def Phi(x):
    return 0.5*(1.0 + math.erf(x/math.sqrt(2.0)))

def unit_ball(n):
    z = rng.normal(size=n)
    z /= np.linalg.norm(z)
    r = rng.random()**(1.0/n)
    return r*z

# 1. Deterministic theorem stress test with a planted stronger-margin witness.
N, m, K = 12, 40, 25
kappa = -1.0
tau = 0.17
x = rng.normal(size=N)
x /= np.linalg.norm(x)
A = rng.normal(size=(m, N))
for i in range(m):
    p = float(A[i] @ x)
    if p < kappa + tau:
        A[i] += ((kappa + tau) - p) * x

new_rows = []
required_tau = 0.0
for _ in range(K):
    s = rng.uniform(0.15, 1.0)
    q = rng.dirichlet(np.ones(m))
    # Choose an excess e beyond the free budget so that tau_j <= tau.
    excess = rng.uniform(0.0, s*tau)
    e_norm = (1.0-s)*(-kappa) + excess
    u = unit_ball(N)
    e = e_norm * u / max(np.linalg.norm(u), 1e-300)
    b = s*(q @ A) + e
    new_rows.append(b)
    tau_j = max(0.0, e_norm - (-kappa)*(1.0-s))/s
    required_tau = max(required_tau, tau_j)

B = np.vstack(new_rows)
core_min = float(np.min(A @ x))
added_min = float(np.min(B @ x))
assert core_min >= kappa + tau - 1e-12
assert required_tau <= tau + 1e-12
assert added_min >= kappa - 1e-12

# 2. Zero-loss safe-hull case at order-one ambient perturbation.
s = 0.5
u = unit_ball(N)
e = (1.0-s)*u/np.linalg.norm(u)
q = rng.dirichlet(np.ones(m))
b = s*(q@A) + e
assert float(b@x) >= kappa - 1e-12
tau_zero = max(0.0, np.linalg.norm(e) - (1.0-s))/s
assert abs(tau_zero) < 1e-12

# 3. Sharpness of the rowwise loss formula in N=1.
# Core at margin kappa+tau0 has the unique witness x=+1.
s_sharp = 0.4
e_sharp = 0.9
tau_star = (e_sharp - (1.0-s_sharp))/s_sharp
tau_bad = tau_star - 1e-3
a1 = kappa + tau_bad
a2 = 2.0
# +1 satisfies the core at margin kappa+tau_bad, -1 fails row a2.
assert a1 >= kappa + tau_bad - 1e-15
assert -a2 < kappa + tau_bad
b_bad = s_sharp*a1 - e_sharp
assert b_bad < kappa

# 4. Concrete T03 comparison rate.
alpha_old = 1.0/Phi(-0.5)
alpha_new = 1.0/Phi(-1.0)
alpha_U = 12.31963484
records = []
for n in (10**3, 10**6, 10**9):
    c = n**(-1.0/3.0)
    eps_old = 0.5 + c
    tau_new = 2.0*c
    lp_new_n = 1.0/Phi(-1.0 + tau_new)
    records.append((n, eps_old, tau_new, lp_new_n))

# 5. Full-rank and non-Gaussian checks for B_j = 0.5 A_j + r_N U_j.
N2, m2 = 20, 140
c2 = N2**(-1.0/3.0)
rN = 0.5 + c2
A2 = rng.normal(size=(m2, N2))
B2 = np.vstack([0.5*A2[j] + rN*unit_ball(N2) for j in range(N2)])
svals = np.linalg.svd(B2, compute_uv=False)
assert np.linalg.matrix_rank(B2) == N2
assert svals[-1] > 0.0

# One-coordinate fourth cumulant for uniform unit-ball noise.
# E U_1^2=1/(N+2), E U_1^4=3/((N+2)(N+4)).
kappa4 = -6.0*(rN**4)/((N2+2)**2*(N2+4))
assert kappa4 < 0.0

# 6. Bracket arithmetic in total density lambda=alpha+1.
before_L_total = alpha_old + 1.0
after_L_total = alpha_new + 1.0
U_total = alpha_U + 1.0
before_width = U_total - before_L_total
after_width = U_total - after_L_total
gain = before_width - after_width
assert abs(gain - (alpha_new-alpha_old)) < 1e-12

print("SEED", SEED)
print("PLANTED_CORE_MIN", format(core_min, ".15g"))
print("REQUIRED_TAU_MAX", format(required_tau, ".15g"))
print("ADDED_MIN", format(added_min, ".15g"))
print("ZERO_LOSS_TAU", format(tau_zero, ".15g"))
print("SHARPNESS_TAU_STAR", format(tau_star, ".15g"))
print("SHARPNESS_TAU_BAD", format(tau_bad, ".15g"))
print("SHARPNESS_BAD_ROW_AT_WITNESS", format(b_bad, ".15g"))
for n, oldloss, newloss, lp in records:
    print("RATE", n, "OLD_LOSS", format(oldloss, ".15g"),
          "NEW_LOSS", format(newloss, ".15g"),
          "LP_LOWER", format(lp, ".15g"))
print("SAMPLE_FULL_RANK", np.linalg.matrix_rank(B2))
print("SAMPLE_SMIN", format(float(svals[-1]), ".15g"))
print("COORD_FOURTH_CUMULANT", format(kappa4, ".15g"))
print("PARENT_LOWER", format(alpha_new, ".15g"))
print("PARENT_UPPER", format(alpha_U, ".15g"))
print("APPLICATION_BEFORE_TOTAL_BRACKET",
      format(before_L_total, ".15g"), format(U_total, ".15g"))
print("APPLICATION_AFTER_TOTAL_BRACKET",
      format(after_L_total, ".15g"), format(U_total, ".15g"))
print("APPLICATION_WIDTH_GAIN", format(gain, ".15g"))
print("ALL_DEFICIT_COMPENSATED_CHECKS_PASS")
