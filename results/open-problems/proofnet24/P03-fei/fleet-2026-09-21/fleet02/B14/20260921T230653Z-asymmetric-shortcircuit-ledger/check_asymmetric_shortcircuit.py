from fractions import Fraction
from math import comb, log


def influence(vals, n, k):
    N = 1 << n
    return Fraction(sum(vals[x] != vals[x ^ (1 << k)] for x in range(N)), N)


# 1. Exact random-order survival identity.
identity_cases = 0
for r in range(1, 65):
    for m in range(1, r + 1):
        lhs = sum(
            (Fraction(comb(r - m, t), comb(r, t)) if t <= r - m else Fraction(0))
            for t in range(r)
        )
        rhs = Fraction(r + 1, m + 1)
        assert lhs == rhs, (r, m, lhs, rhs)
        identity_cases += 1

# 2. Exhaustive folded pivotality boundary check through n=4.
#    Inf_k(eta_i) <= 2 min(Inf_k(f), 1-Inf_k(f)).
boundary_checks = 0
for n in range(1, 5):
    N = 1 << n
    for mask in range(1 << N):
        vals = [1 if (mask >> x) & 1 else -1 for x in range(N)]
        infs = [influence(vals, n, k) for k in range(n)]
        for i in range(n):
            eta = [vals[x] != vals[x ^ (1 << i)] for x in range(N)]
            for k in range(n):
                if k == i:
                    continue
                lhs = influence(eta, n, k)
                rhs = 2 * min(infs[k], 1 - infs[k])
                assert lhs <= rhs, (n, mask, i, k, lhs, rhs)
                boundary_checks += 1

# 3. Numerical regression for the scalar coefficient-12 margin after the
#    analytic proof. Work with q-scaled quantities to avoid underflow.
A = 12 - 2 / log(2)
min_margin = None
min_r = None
for r in range(3, 10001):
    I_lower_over_q = 15 * r / 16 - 1 / (8 * (r + 1))
    H_upper_over_q = 17 * r / 2 - 17 / 8
    margin = A * I_lower_over_q - H_upper_over_q
    assert margin > 0, (r, margin)
    if min_margin is None or margin < min_margin:
        min_margin = margin
        min_r = r

print(f"random_order_identity=PASS cases={identity_cases}")
print(f"folded_boundary=PASS checks={boundary_checks}")
print(f"coefficient12_scaled_margin=PASS r=3..10000 min_margin={min_margin:.15f} at_r={min_r}")
