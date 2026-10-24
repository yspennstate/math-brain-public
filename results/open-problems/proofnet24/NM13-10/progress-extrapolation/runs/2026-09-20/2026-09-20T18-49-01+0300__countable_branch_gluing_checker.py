import math
import random
import numpy as np
from numpy.polynomial.hermite import hermgauss

random.seed(20260920)
rng = np.random.default_rng(20260920)

# 1. Exact constants used in the restart theorem.
c_sum = 2**(1/3) * (1 + math.log(2))**(2/3)
c_restart = (4 * c_sum**3)**(1/3)
c_restart_closed = 2 * (1 + math.log(2))**(2/3)

# 2. Randomized stress test of the exact disjoint-gluing inequality.
# Local extremal form: A_j = R^3 s_j/(K^3 L_j^2), T_j=s_j*exp(L_j-1).
# The theorem claims R^3 sum s_j <= K^3 sum A_j * L^2 where
# L = 1+log(sum T_j/sum s_j). Set R=K=1.
worst_glue = 0.0
worst_avg_over_global = 0.0
worst_recip_jensen = 0.0
for _ in range(30000):
    n = random.randint(1, 60)
    s = np.array([10**random.uniform(-10, 2) for _ in range(n)], dtype=float)
    L = np.array([1 + 10**random.uniform(-4, 1.7) for _ in range(n)], dtype=float)
    T = s * np.exp(L - 1)
    s_tot = float(s.sum())
    T_tot = float(T.sum())
    L_global = 1 + math.log(T_tot / s_tot)
    A_tot = float(np.sum(s / (L*L)))
    ratio = s_tot / (A_tot * L_global**2)
    worst_glue = max(worst_glue, ratio)

    w = s/s_tot
    L_avg = float(np.dot(w, L))
    inv_avg = float(np.dot(w, 1/(L*L)))
    worst_avg_over_global = max(worst_avg_over_global, L_avg/L_global)
    worst_recip_jensen = max(worst_recip_jensen, (1/(L_avg*L_avg))/inv_avg)

# 3. Gauss-Hermite check of the passive critical L^3 contraction.
# U_t(lambda)=x_lambda exp(sqrt(lambda)B_t -3 lambda t/2).
# Analytically E||U_t||^3 <= ||x||^3 by Jensen and E M_lambda^3=1.
nodes, weights = hermgauss(120)
G = math.sqrt(2) * nodes
WG = weights / math.sqrt(math.pi)
max_passive_ratio = 0.0
for _ in range(500):
    n = int(rng.integers(2, 20))
    a = rng.uniform(1, 12, size=n)  # a=sqrt(lambda)
    x = rng.normal(size=n)
    xnorm = float(np.linalg.norm(x))
    t = float(10**rng.uniform(-4, -0.2))
    expo = np.outer(a, math.sqrt(t)*G) - 1.5*np.outer(a*a, np.full_like(G, t))
    M = np.exp(expo)
    values = np.sum((x[:, None]*M)**2, axis=0)**1.5
    ratio = float(np.dot(WG, values)/(xnorm**3))
    max_passive_ratio = max(max_passive_ratio, ratio)

# 4. Exact scaling check for conditioning on a branch of probability pi:
# local ambient H and quantile u map to ambient pi H and quantile pi u
# with cubic budget pi a^3, leaving the Z_{3,2/3} ratio unchanged.
branch_scaling_err = 0.0
for _ in range(10000):
    pi = 10**random.uniform(-8, 0)
    H = 10**random.uniform(-3, 2)
    u = H * 10**random.uniform(-8, -0.001)
    a = 10**random.uniform(-4, 3)
    lhs = (pi*u)**(1/3) * (pi**(-1/3) * a * u**(-1/3) * (1+math.log(H/u))**(2/3)) / (1+math.log((pi*H)/(pi*u)))**(2/3)
    branch_scaling_err = max(branch_scaling_err, abs(lhs/a - 1))

ok = (
    worst_glue <= 1 + 2e-12
    and worst_avg_over_global <= 1 + 2e-12
    and worst_recip_jensen <= 1 + 2e-12
    and abs(c_restart-c_restart_closed) <= 1e-12
    and max_passive_ratio <= 1 + 5e-5
    and branch_scaling_err <= 5e-12
)

print(f"c_sum={c_sum:.15f}")
print(f"c_restart={c_restart:.15f}")
print(f"c_restart_closed={c_restart_closed:.15f}")
print(f"worst_gluing_ratio={worst_glue:.15f}")
print(f"worst_avg_over_global={worst_avg_over_global:.15f}")
print(f"worst_reciprocal_jensen_ratio={worst_recip_jensen:.15f}")
print(f"max_passive_L3_ratio_GH120={max_passive_ratio:.15f}")
print(f"max_branch_scaling_relative_error={branch_scaling_err:.3e}")
print("CHECK_PASS" if ok else "CHECK_FAIL")
