import math
import random


def beta(a, b):
    return math.gamma(a) * math.gamma(b) / math.gamma(a + b)


def H(k, q):
    return (
        math.sqrt(math.e)
        / (k * 2 ** (3 / 4) * q ** (1 / 4))
        * beta(1 / (4 * k), 1 / (4 * q) - 1 / (4 * k))
    )


H32 = H(3, 2)
C_hi = H32 * 32 ** (1 / 12)
H215 = H(2, 1.5)
C_mid = H215 * 6 ** (1 / 8)
C_partner = 7.019062 * 6 ** (3 / 16)
F_floor = 768 ** (-1 / 4)

print(f"H_3,2={H32:.15f}")
print(f"C_hi={C_hi:.15f}")
print(f"H_2,3/2={H215:.15f}")
print(f"C_mid={C_mid:.15f}")
print(f"partner_frob_const={C_partner:.15f}")
print(f"matching_F_floor={F_floor:.15f}")
print(f"B19_hi_H={C_hi / math.sqrt(F_floor):.15f}")
print(f"B19_hi_density_a_ge_quarter={2*C_hi / math.sqrt(F_floor):.15f}")
print(f"B19_mid_density_a_ge_quarter={2*C_mid / math.sqrt(F_floor):.15f}")
print(
    "partner_density_if_Ffloor_dquarter="
    f"{C_partner * 4**(1/4) * F_floor**(-3/4):.15f}"
)

# Truncated version of E[1/|X+Y|] for iid Uniform[-1/2,1/2].
# The exact density of S=X+Y is 1-|s| on [-1,1], so
# E[1/|S|; |S|>=eps] = 2(log(1/eps)-1+eps).
for eps in (1e-1, 1e-3, 1e-6):
    value = 2 * (math.log(1 / eps) - 1 + eps)
    print(f"trunc_E_1_over_absS eps={eps:g} value={value:.12f}")

# Deterministic finite regression only: verify the two algebraic lower bounds
# on random nonnegative squared-singular-value lists.
random.seed(20260922)
min_e2_ratio = float("inf")
min_e3_ratio = float("inf")
count_e2 = 0
count_e3 = 0
for n in range(3, 13):
    for _ in range(500):
        x = [random.expovariate(1.0) for _ in range(n)]
        S = sum(x)
        m = max(x)
        sr = S / m
        e2 = sum(x[i] * x[j] for i in range(n) for j in range(i + 1, n))
        e3 = sum(
            x[i] * x[j] * x[k]
            for i in range(n)
            for j in range(i + 1, n)
            for k in range(j + 1, n)
        )
        if sr >= 1.5:
            lower2 = S * S / 6
            assert e2 + 1e-12 >= lower2
            min_e2_ratio = min(min_e2_ratio, e2 / lower2)
            count_e2 += 1
        if sr >= 2.5:
            lower3 = S**3 / 32
            assert e3 + 1e-12 >= lower3
            min_e3_ratio = min(min_e3_ratio, e3 / lower3)
            count_e3 += 1

print(f"E2_cases={count_e2} min_ratio={min_e2_ratio:.12f}")
print(f"E3_cases={count_e3} min_ratio={min_e3_ratio:.12f}")
print("STATUS=PASS")
