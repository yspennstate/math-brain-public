import math
import random

C = 6.521851214


def kl2(p, q):
    out = 0.0
    for a, b in zip(p, q):
        if a:
            out += a * math.log2(a / b)
    return out


def states_costs(a):
    k = len(a)
    states = list(range(1, 1 << k))
    costs = []
    for mask in states:
        costs.append(sum(a[i] for i in range(k) if (mask >> i) & 1))
    return states, costs


rng = random.Random(20260922)
max_identity_error = 0.0
min_variational_gap = float("inf")
for _ in range(500):
    k = rng.randint(2, 7)
    a = [rng.uniform(0.2, 9.0) for _ in range(k)]
    states, c = states_costs(a)
    b0 = [2.0 ** (-z) for z in c]
    A0 = sum(b0)
    nu = [z / A0 for z in b0]
    raw = [rng.expovariate(1.0) for _ in states]
    sr = sum(raw)
    w = [z / sr for z in raw]
    m = sum(pi * ci for pi, ci in zip(w, c))
    lam = rng.uniform(-1.5, 1.5)
    bl = [2.0 ** (-(1.0 - lam) * z) for z in c]
    Al = sum(bl)
    rho = [z / Al for z in bl]
    lhs = kl2(w, nu)
    rhs = kl2(w, rho) + lam * m - math.log2(Al / A0)
    max_identity_error = max(max_identity_error, abs(lhs - rhs))
    lower = lam * m - math.log2(Al / A0)
    min_variational_gap = min(min_variational_gap, lhs - lower)

max_tilt_equality_error = 0.0
for _ in range(200):
    k = rng.randint(2, 8)
    a = [rng.uniform(0.1, 10.0) for _ in range(k)]
    states, c = states_costs(a)
    A0 = sum(2.0 ** (-z) for z in c)
    nu = [2.0 ** (-z) / A0 for z in c]
    lam = rng.uniform(-1.0, 1.0)
    Al = sum(2.0 ** (-(1.0 - lam) * z) for z in c)
    rho = [2.0 ** (-(1.0 - lam) * z) / Al for z in c]
    m = sum(pi * ci for pi, ci in zip(rho, c))
    lhs = kl2(rho, nu)
    lower = lam * m - math.log2(Al / A0)
    max_tilt_equality_error = max(max_tilt_equality_error, abs(lhs - lower))

x = 2.0 ** (-C)


def log2_A_central(k, lam):
    y = x ** (1.0 - lam)
    z = k * math.log1p(y)
    return (z + math.log1p(-math.exp(-z))) / math.log(2.0)


def threshold_ratio(k, lam):
    return (log2_A_central(k, lam) - math.log2(x)) / (lam * C)


def golden(f, a, b, it=120):
    gr = (math.sqrt(5.0) - 1.0) / 2.0
    c = b - gr * (b - a)
    d = a + gr * (b - a)
    fc = f(c)
    fd = f(d)
    for _ in range(it):
        if fc < fd:
            b, d, fd = d, c, fc
            c = b - gr * (b - a)
            fc = f(c)
        else:
            a, c, fc = c, d, fd
            d = a + gr * (b - a)
            fd = f(d)
    z = (a + b) / 2.0
    return z, f(z)


rows = []
for k in (2, 3, 4, 5, 6, 8, 10, 12, 16, 18, 22, 32):
    grid = [(threshold_ratio(k, j / 1000.0), j / 1000.0) for j in range(1, 1501)]
    _, lm = min(grid)
    lam, val = golden(
        lambda z: threshold_ratio(k, z),
        max(1e-8, lm - 0.01),
        min(1.5, lm + 0.01),
    )
    rows.append((k, lam, val))

assert max_identity_error < 5e-13
assert max_tilt_equality_error < 5e-13
assert min_variational_gap >= -5e-13

print("candidate LIMIT-PRIME-GATE-LIFT-v1 / B-GIBBS-KL-v1")
print("random_decomposition_trials 500")
print("max_decomposition_abs_error %.17g" % max_identity_error)
print("min_variational_gap %.17g" % min_variational_gap)
print("tilted_equality_trials 200")
print("max_tilt_equality_abs_error %.17g" % max_tilt_equality_error)
print("central_balanced_thresholds: k lambda_star influence_threshold")
for k, lam, val in rows:
    print("%2d %.12f %.12f" % (k, lam, val))
print("PASS")
