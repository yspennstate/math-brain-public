#!/usr/bin/env python3
from fractions import Fraction
from math import factorial

CHECKS = 0

def ok(cond, msg):
    global CHECKS
    CHECKS += 1
    if not cond:
        raise AssertionError(msg)

def poly_mul(a, b, N):
    out = [Fraction(0)] * (N + 1)
    for i, x in enumerate(a):
        if x == 0:
            continue
        for j in range(min(len(b) - 1, N - i) + 1):
            y = b[j]
            if y:
                out[i + j] += x * y
    return out

def poly_pow(a, k, N):
    out = [Fraction(1)] + [Fraction(0)] * N
    for _ in range(k):
        out = poly_mul(out, a, N)
    return out

def deriv(a, r):
    out = a[:]
    for _ in range(r):
        out = [out[i] * i for i in range(1, len(out))]
    return out

def cycle_series(N):
    # One connected labelled simple 2-regular graph on m>=3 vertices is an
    # undirected m-cycle. There are (m-1)!/2 of them, hence EGF coefficient 1/(2m).
    return [Fraction(0) if m < 3 else Fraction(1, 2 * m) for m in range(N + 1)]

def denominator_count(N, R):
    if N < 3 * R:
        return 0
    C = cycle_series(N)
    P = poly_pow(C, R, N)
    value = Fraction(factorial(N), factorial(R)) * P[N]
    ok(value.denominator == 1, f"denominator integrality N={N},R={R}")
    return value.numerator

def visible_count(N, R, sizes):
    b = sum(sizes)
    q = len(sizes)
    if q > R:
        return 0
    C = cycle_series(N)
    P = [Fraction(1)] + [Fraction(0)] * N
    for s in sizes:
        P = poly_mul(P, deriv(C, s), N)
    Q = poly_pow(C, R - q, N)
    Q = [x / Fraction(factorial(R - q), 1) for x in Q]
    P = poly_mul(P, Q, N)
    index = N - b
    if index < 0:
        return 0
    value = Fraction(factorial(N - b), 1) * P[index]
    ok(value.denominator == 1, f"visible integrality N={N},R={R},sizes={sizes}")
    return value.numerator

def probability(N, R, sizes):
    return Fraction(visible_count(N, R, sizes), denominator_count(N, R))

def beta(i, j):
    return Fraction(factorial(i - 1) * factorial(j - 1), factorial(i + j - 1))

# EGF coefficient check for every connected undirected cycle size through 30.
for m in range(3, 31):
    connected = factorial(m - 1) // 2
    ok(cycle_series(m)[m] == Fraction(connected, factorial(m)),
       f"connected-cycle coefficient m={m}")

# C036 uses R=4. Verify nonempty conditioned state spaces over a substantial range.
for N in range(12, 41):
    ok(denominator_count(N, 4) > 0, f"positive denominator N={N}")

# At the minimum N=12, four simple-cycle components must all be triangles.
# The exact count is the number of partitions of [12] into four unordered triples.
expected12 = factorial(12) // (factorial(3) ** 4 * factorial(4))
ok(denominator_count(12, 4) == expected12, "N=12 four-triangle denominator")

# Exact restriction normalization and a deterministic lower bound on pair separation.
for N in range(12, 61):
    p11 = probability(N, 4, (1, 1))
    psame = probability(N, 4, (2,))
    ok(p11 + psame == 1, f"pair normalization N={N}")
    # Every component has size >=3. Separation is minimized at (N-9,3,3,3).
    lower = Fraction(9 * (2 * N - 12), N * (N - 1))
    ok(p11 >= lower, f"pair lower bound N={N}")
    lam = 1 / p11
    ok(Fraction(1, N * N) * lam < 1, f"activation probability N={N}")

# Exact visible set-partition normalization for b=3 and b=4.
for N in range(12, 31):
    p3 = probability(N, 4, (3,))
    p12 = probability(N, 4, (1, 2))
    p111 = probability(N, 4, (1, 1, 1))
    ok(p3 + 3 * p12 + p111 == 1, f"b=3 normalization N={N}")

    p4 = probability(N, 4, (4,))
    p13 = probability(N, 4, (1, 3))
    p22 = probability(N, 4, (2, 2))
    p112 = probability(N, 4, (1, 1, 2))
    p1111 = probability(N, 4, (1, 1, 1, 1))
    ok(p4 + 4 * p13 + 3 * p22 + 6 * p112 + p1111 == 1,
       f"b=4 normalization N={N}")

trend = []
for N in (20, 50, 100, 200):
    p11 = probability(N, 4, (1, 1))
    lam = 1 / p11
    q12 = lam * probability(N, 4, (1, 2))
    q22 = lam * probability(N, 4, (2, 2))
    q111 = lam * probability(N, 4, (1, 1, 1))
    q1111 = lam * probability(N, 4, (1, 1, 1, 1))
    ok(q12 > 0 and q22 > 0 and q111 > 0, f"positive rates N={N}")
    trend.append((N, float(lam), float(q12), float(q22), float(q111), float(q1111)))

ok(beta(1, 1) == 1, "B(1,1)")
ok(beta(1, 2) == Fraction(1, 2), "B(1,2)")
ok(beta(2, 2) == Fraction(1, 6), "B(2,2)")

print(f"EXACT_CHECKS={CHECKS}")
print(f"N12_DEN={expected12}")
print("C036_N12_FULL_ROOT_SHAPE=(3,3,3,3)_WITH_PROBABILITY_1")
print("C036_RATE_TREND columns N lambda q12 q22 q111 q1111")
for row in trend:
    print("%d %.12f %.12f %.12f %.12f %.12f" % row)
print("CTCS_TARGETS q12=0.5 q22=0.166666666667 q111=0 q1111=0")
print("ALL_EXACT_CHECKS_PASS")
