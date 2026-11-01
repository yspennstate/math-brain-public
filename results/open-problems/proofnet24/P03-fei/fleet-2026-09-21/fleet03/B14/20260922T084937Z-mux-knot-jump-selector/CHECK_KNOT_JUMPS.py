import math, random
from fractions import Fraction

RNG = random.Random(2026092203)


def G_eval(x, knots, slopes, G0=1.23456789, x0=0.0):
    def integral(a, b):
        if a == b:
            return 0.0
        if a > b:
            return -integral(b, a)
        pts = [a] + [k for k in knots if a < k < b] + [b]
        total = 0.0
        for l, r in zip(pts[:-1], pts[1:]):
            mid = (l + r) / 2
            idx = sum(k < mid for k in knots)
            total += slopes[idx] * (r - l)
        return total
    return G0 + integral(x0, x)


def direct_J(p, rho, knots, slopes):
    x = math.log2(1 / p)
    alpha = -math.log2(1 - rho)
    beta = math.log2(1 + rho)
    G = lambda y: G_eval(y, knots, slopes)
    return (
        p * G(x)
        - 0.5 * p * (1 - rho) * G(x + alpha)
        - 0.5 * p * (1 + rho) * G(x - beta)
    )


def knot_J(p, rho, knots, slopes):
    x = math.log2(1 / p)
    alpha = -math.log2(1 - rho)
    beta = math.log2(1 + rho)
    idx = sum(k < x for k in knots)
    sigma0 = slopes[idx]
    K = (1 - rho) * math.log(1 - rho) + (1 + rho) * math.log(1 + rho)
    ans = p * sigma0 * K / (2 * math.log(2))
    for j, k in enumerate(knots):
        delta = slopes[j + 1] - slopes[j]
        if x < k < x + alpha:
            ans -= 0.5 * p * (1 - rho) * delta * (x + alpha - k)
        if x - beta < k < x:
            ans -= 0.5 * p * (1 + rho) * delta * (k - (x - beta))
    return ans


maxerr = 0.0
for _ in range(50000):
    n = RNG.randrange(0, 9)
    knots = sorted(RNG.uniform(0.2, 8.0) for _ in range(n))
    slopes = [RNG.uniform(-31, 31) for _ in range(n + 1)]
    p = 2 ** (-RNG.uniform(1.05, 6.5))
    rho = RNG.uniform(1e-7, 0.95)
    x = math.log2(1 / p)
    if min([abs(x - k) for k in knots] or [1.0]) < 1e-9:
        continue
    lhs = direct_J(p, rho, knots, slopes)
    rhs = knot_J(p, rho, knots, slopes)
    maxerr = max(maxerr, abs(lhs - rhs))
assert maxerr < 5e-12, maxerr

# Upward slope jumps can only reduce the midpoint loss relative to the
# containing-cell formula.
for _ in range(10000):
    n = RNG.randrange(1, 9)
    knots = sorted(RNG.uniform(0.2, 8.0) for _ in range(n))
    base = RNG.uniform(-10, 10)
    slopes = [base]
    for _ in range(n):
        slopes.append(slopes[-1] + RNG.uniform(0, 5))
    p = 2 ** (-RNG.uniform(1.05, 6.5))
    rho = RNG.uniform(1e-7, 0.95)
    x = math.log2(1 / p)
    idx = sum(k < x for k in knots)
    sigma0 = slopes[idx]
    K = (1 - rho) * math.log(1 - rho) + (1 + rho) * math.log(1 + rho)
    same_cell = p * sigma0 * K / (2 * math.log(2))
    assert knot_J(p, rho, knots, slopes) <= same_cell + 2e-12

# Exact peer margin and worst-case one-downward-jump overshoot radius.
peer_margin = Fraction(1114633887638025857, 271020516100000000000)
worst_single_knot_coeff = Fraction(713, 20)  # (1+3/20)*62/2
radius = peer_margin / worst_single_knot_coeff
assert peer_margin > Fraction(4, 1000)
assert radius > Fraction(1, 9000)

print("PASS exact PWL knot-jump identity")
print("max_formula_error", repr(maxerr))
print("peer_margin", float(peer_margin))
print("single_downward_knot_safe_overshoot", float(radius))
print("radius_exact", f"{radius.numerator}/{radius.denominator}")
