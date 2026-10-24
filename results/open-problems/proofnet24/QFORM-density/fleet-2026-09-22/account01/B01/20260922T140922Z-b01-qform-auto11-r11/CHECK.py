import math
import random

# Finite sanity checks for the analytic identities in REPORT.md.
# These checks are not substitutes for the proofs.

K = 8 * math.sqrt(2)
C_INDEF = 4 * math.sqrt(K)
C_DEF = 2 * math.sqrt(2 * math.pi)
C_ZERO = 2 ** (1 / 3) * (3 + math.log(8))

print(f"K_small_ball={K:.15f}")
print(f"C_indef={C_INDEF:.15f}")
print(f"C_def={C_DEF:.15f}")
print(f"C_zero_diag={C_ZERO:.15f}")
print(f"C_zero_diag_canonical={3 + math.log(8):.15f}")


def sublevel_length(c, d, e, eps):
    """Exact interval decomposition in floating arithmetic for |cz^2+dz+e|<=eps."""
    if abs(c) < 1e-14:
        if abs(d) < 1e-14:
            return math.inf if abs(e) <= eps else 0.0
        return 2 * eps / abs(d)
    roots = []
    for level in (-eps, eps):
        disc = d * d - 4 * c * (e - level)
        if disc >= 0:
            sd = math.sqrt(disc)
            roots.extend([(-d - sd) / (2 * c), (-d + sd) / (2 * c)])
    roots = sorted(set(roots))
    cuts = [-math.inf] + roots + [math.inf]
    total = 0.0
    for lo, hi in zip(cuts[:-1], cuts[1:]):
        if math.isinf(lo):
            x = hi - 1 - max(1, abs(hi))
        elif math.isinf(hi):
            x = lo + 1 + max(1, abs(lo))
        else:
            x = (lo + hi) / 2
        if abs(c * x * x + d * x + e) <= eps * (1 + 1e-10):
            if math.isinf(lo) or math.isinf(hi):
                return math.inf
            total += hi - lo
    return total


random.seed(20260922)
max_ratio = 0.0
worst = None
for _ in range(100000):
    c = (-1 if random.random() < 0.5 else 1) * 10 ** random.uniform(-3, 3)
    d = (-1 if random.random() < 0.5 else 1) * 10 ** random.uniform(-3, 3)
    e = (-1 if random.random() < 0.5 else 1) * 10 ** random.uniform(-3, 3)
    eps = 10 ** random.uniform(-4, 2)
    actual = sublevel_length(c, d, e, eps)
    Delta = d * d - 4 * c * e
    proposed = 8 * eps / math.sqrt(abs(Delta) + 4 * eps * abs(c))
    if math.isfinite(actual):
        ratio = actual / proposed
        if ratio > max_ratio:
            max_ratio = ratio
            worst = (c, d, e, eps, actual, proposed, Delta)
        assert actual <= proposed * (1 + 2e-10)
print(f"quadratic_sublevel_random_max_ratio={max_ratio:.15f}")
print("quadratic_sublevel_random_worst=", worst)

for _ in range(10000):
    a, b, c = [(-1 if random.random() < 0.5 else 1) * 10 ** random.uniform(-2, 2) for _ in range(3)]
    x, y, z = [random.uniform(-2, 2) for _ in range(3)]
    kappa = a * b / c
    alpha = c / b
    beta = c / a
    lhs = a * x * y + b * x * z + c * y * z
    rhs = kappa * (x + alpha * y) * (x + beta * z) - kappa * x * x
    assert abs(lhs - rhs) <= 1e-8 * (1 + abs(lhs))
print("zero_diagonal_factorization=PASS")

# The final zero-diagonal determinant envelope is decreasing for r>=1 because
# d/dr [(3+log 8+3 log r)/r] has numerator 3-(3+log 8)-3 log r < 0.
assert 3 - (3 + math.log(8)) < 0
print("zero_diagonal_envelope_monotonicity=PASS")
print("STATUS=PASS")
