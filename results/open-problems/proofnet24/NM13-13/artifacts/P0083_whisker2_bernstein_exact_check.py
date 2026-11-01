#!/usr/bin/env python3
from fractions import Fraction as F
from math import comb


def add(a, b):
    n = max(len(a), len(b))
    out = [F(0) for _ in range(n)]
    for i in range(n):
        if i < len(a):
            out[i] += a[i]
        if i < len(b):
            out[i] += b[i]
    return out


def mul(a, b):
    out = [F(0) for _ in range(len(a) + len(b) - 1)]
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return out


def power(a, n):
    out = [F(1)]
    for _ in range(n):
        out = mul(out, a)
    return out


# P(t)=(1-t)(1+t)^6 - t(3/2-t)^6.
lhs = mul([F(1), F(-1)], power([F(1), F(1)], 6))
rhs = mul([F(0), F(1)], power([F(3, 2), F(-1)], 6))
P = add(lhs, [-c for c in rhs])
expected_power_t = [
    F(1),
    F(-409, 64),
    F(873, 16),
    F(-1135, 16),
    F(125, 2),
    F(-171, 4),
    F(4),
    F(-2),
]
assert P == expected_power_t

# Substitute t=u/2.
a = [c * F(1, 2) ** k for k, c in enumerate(P)]

# Convert degree-7 power coefficients a_k u^k to Bernstein coefficients:
# b_j=sum_{k<=j} a_k * C(j,k)/C(7,k).
n = 7
bernstein = []
for j in range(n + 1):
    bj = sum(
        (a[k] * F(comb(j, k), comb(n, k)) for k in range(j + 1)),
        F(0),
    )
    bernstein.append(bj)

expected_bernstein = [
    F(1),
    F(487, 896),
    F(165, 224),
    F(297, 224),
    F(243, 112),
    F(711, 224),
    F(1899, 448),
    F(665, 128),
]
assert bernstein == expected_bernstein
assert all(x > 0 for x in bernstein)

# Reconstruct the power basis from the Bernstein coefficients as an
# independent exact identity check:
# B_{j,n}(u)=C(n,j) u^j (1-u)^(n-j).
reconstructed = [F(0) for _ in range(n + 1)]
for j, bj in enumerate(bernstein):
    basis = mul(
        [F(0)] * j + [F(comb(n, j))],
        power([F(1), F(-1)], n - j),
    )
    reconstructed = add(reconstructed, [bj * c for c in basis])
assert reconstructed == a

# Endpoint values are also strictly positive.
def eval_poly(coeffs, x):
    acc = F(0)
    p = F(1)
    for c in coeffs:
        acc += c * p
        p *= x
    return acc


assert eval_poly(P, F(0)) == F(1)
assert eval_poly(P, F(1, 2)) == F(665, 128)
assert eval_poly(P, F(1, 6)) > 0

# Algebra used in the derivative sign of the depth lemma:
# (alpha-1)^2-(alpha+1)(alpha-3)=4 identically.
# Verify the coefficient identity symbolically in Q[alpha].
sq1 = power([F(-1), F(1)], 2)
prod = mul([F(1), F(1)], [F(-3), F(1)])
gap = add(sq1, [-c for c in prod])
assert gap == [F(4), F(0), F(0)]

print("PASS")
print("P_t_power =", [str(x) for x in P])
print("P_u_over_2_bernstein =", [str(x) for x in bernstein])
print("min_bernstein =", str(min(bernstein)))
print("P(0) =", str(eval_poly(P, F(0))))
print("P(1/6) =", str(eval_poly(P, F(1, 6))))
print("P(1/2) =", str(eval_poly(P, F(1, 2))))
print("root_comparison_gap =", str(gap[0]))
