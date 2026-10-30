import math
import random


def e3(vals):
    ans = 0.0
    n = len(vals)
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                ans += vals[i] * vals[j] * vals[k]
    return ans


def theta(gamma, s2):
    return sum(x / (gamma * gamma + x) for x in s2)


def detreg(gamma, s2):
    g2 = gamma * gamma
    ans = 1.0
    for x in s2:
        ans *= 1.0 + x / g2
    return ans


def gamma_theta3(s2):
    lo = 0.0
    hi = max(math.sqrt(max(s2)), 1.0)
    while theta(hi, s2) > 3.0:
        hi *= 2.0
    for _ in range(200):
        mid = (lo + hi) / 2.0
        if theta(mid, s2) > 3.0:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2.0


rng = random.Random(20260922203121)
worst = 0.0
for trial in range(200):
    r = rng.randint(4, 12)
    s = [10.0 ** rng.uniform(-4.0, 4.0) for _ in range(r)]
    s2 = [x * x for x in s]
    E3 = e3(s2)
    gamma = gamma_theta3(s2)
    D = detreg(gamma, s2)
    ratio = (gamma ** -1.0) * (D ** (-1.0 / 6.0)) * (E3 ** (1.0 / 6.0))
    worst = max(worst, ratio)
    if ratio > 1.0 + 1e-10:
        raise AssertionError((trial, ratio))

factor = 256.0 ** (1.0 / 6.0)
rank3 = 3.0 * math.e * factor
rho_half = 3.0 * math.e / math.sqrt(2.0) * factor
rho_twothirds = 9.0 * math.e * math.sqrt(3.0 / 8.0) * factor

print("random spectral inequality PASS, worst ratio", worst)
print("E3>=1/256 factor", factor)
print("rank3 bound", rank3)
print("rho<=1/2 bound", rho_half)
print("rho<=2/3 bound", rho_twothirds)
print("STATUS=QFORM_E3_RIDGE_AGGREGATE_CHECK_PASS")
