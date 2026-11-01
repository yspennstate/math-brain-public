import itertools
import math
import numpy as np

rng = np.random.default_rng(20260923140748)


def e2(M):
    m, n = M.shape
    return sum(
        float(np.linalg.det(M[np.ix_(R, T)]) ** 2)
        for R in itertools.combinations(range(m), 2)
        for T in itertools.combinations(range(n), 2)
    )


def anchored_e3(N):
    m, n = N.shape
    return sum(
        float(np.linalg.det(N[np.ix_((0,) + R, (0,) + T)]) ** 2)
        for R in itertools.combinations(range(1, m), 2)
        for T in itertools.combinations(range(1, n), 2)
    )


# Regression 1: bordered third-compound inequality.
max_ratio = 0.0
for _ in range(200):
    N = rng.integers(-3, 4, size=(5, 6)).astype(float)
    b = N[0, 0]
    r = N[0, 1:]
    c = N[1:, 0]
    H = N[1:, 1:]
    lhs = math.sqrt(anchored_e3(N))
    rhs = abs(b) * math.sqrt(e2(H)) + np.linalg.norm(c) * np.linalg.norm(r) * np.linalg.norm(H)
    assert lhs <= rhs + 1e-10
    if rhs > 0:
        max_ratio = max(max_ratio, lhs / rhs)

# Regression 2: in the diffuse collision branch, exhaustive small colorings
# attain at least the probabilistic lower bound C^2 R^2 F^2 / 32.
color_trials = 0
min_best_ratio = float("inf")
for _ in range(100):
    m, n = 4, 5
    c = rng.integers(-4, 5, size=m).astype(float)
    r = rng.integers(-4, 5, size=n).astype(float)
    H = rng.integers(-3, 4, size=(m, n)).astype(float)
    C, R, F = np.linalg.norm(c), np.linalg.norm(r), np.linalg.norm(H)
    if C == 0 or R == 0 or F == 0:
        continue
    p = c * c / C**2
    q = r * r / R**2
    ur = (H * H).sum(axis=1) / F**2
    vc = (H * H).sum(axis=0) / F**2
    A = float(p @ ur)
    B = float(q @ vc)
    if A >= 0.25 or B >= 0.25:
        continue
    target = C**2 * R**2 * F**2 / 32.0
    best = 0.0
    for rb in itertools.product((0, 1), repeat=m):
        rb = np.array(rb)
        c0 = float((c[rb == 0] ** 2).sum())
        for cb in itertools.product((0, 1), repeat=n):
            cb = np.array(cb)
            r0c = float((r[cb == 0] ** 2).sum())
            h11 = float((H[np.ix_(rb == 1, cb == 1)] ** 2).sum())
            best = max(best, c0 * r0c * h11)
    assert best + 1e-9 >= target
    color_trials += 1
    min_best_ratio = min(min_best_ratio, best / target)

beta = math.sqrt(63) / 16
h = (2 * math.sqrt(2) - 1) / 1572864
r0 = 16 * math.sqrt(beta / 4617)
tau0 = h * h / 128
a_min = r0 * h
Cvol = (9 * math.sqrt(3) * math.e / 2) * (8 / 3) ** (-1 / 6)
Cpair = 3 * 400 ** (1 / 3) * (32 / 9) ** (1 / 6) * (2 * tau0) ** (-5 / 6)
# Tiny-edge branch |b|<=2 tau0 from |b| sqrt(E2)>(sqrt2/3)a^3.
tiny_sqrtE2_over_a2 = (math.sqrt(2) / 6) * a_min / tau0
tiny_matching_over_a2 = tiny_sqrtE2_over_a2 / 4
# Tiny selected hub edge <=2 tau0 from edge*star*star>a^3/(12sqrt14).
tiny_hub_twostar_over_a2 = a_min / (24 * math.sqrt(14) * tau0)

print(f"bordered_trials=200 max_ratio={max_ratio:.15f}")
print(f"diffuse_color_trials={color_trials} min_best_over_target={min_best_ratio:.15f}")
print(f"h={h:.16e} tau0={tau0:.16e} a_over_h_floor={r0:.15f} a_floor={a_min:.16e}")
print(f"tiny_sqrtE2_over_a2={tiny_sqrtE2_over_a2:.15f}")
print(f"tiny_matching_over_a2={tiny_matching_over_a2:.15f}")
print(f"tiny_hub_twostar_over_a2={tiny_hub_twostar_over_a2:.15f}")
print(f"continuous_branch_constant_per_a={Cvol:.15f} universal_at_a_floor={Cvol/a_min:.15f}")
print(f"pair_threshold_bound={Cpair:.15e}")
print(f"hub_product_constant={1/(12*math.sqrt(14)):.15f}")
print("STATUS=PASS")
