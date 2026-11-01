from fractions import Fraction
from math import comb, log2


def h2(x):
    if x == 0 or x == 1:
        return 0.0
    x = float(x)
    return -x * log2(x) - (1 - x) * log2(1 - x)


def d2(a, b):
    a = float(a)
    b = float(b)
    return a * log2(a / b) + (1 - a) * log2((1 - a) / (1 - b))


def q_high(m, p):
    q = Fraction(0, 1)
    for k in range(m + 1):
        prob = Fraction(comb(m, k), 1) * (p**k) * ((1 - p) ** (m - k))
        if 2 * k > m:
            q += prob
        elif 2 * k == m:
            q += prob / 2
    return q


for m in [4, 5, 6, 8, 10, 12, 16, 20]:
    p = Fraction(1, 2 ** (m - 1))
    N = 2**m
    a0 = 1 - p

    # Exact full-complement Booleanity equation for g_m.
    forced = 2 * a0 * (-p)
    rest = (N - 2) * p * p
    assert forced + rest == 0

    # The Cauchy lower bound from the oriented cancellation theorem is exact here.
    gamma = (Fraction(N, 2) - 1) * p * p
    ell = (a0 * a0 * p * p) / gamma
    beta = (Fraction(N, 2) - 1) * p * p
    assert ell == beta == p * (1 - p)

    q = q_high(m, p)
    assert q < beta

    pf = float(p)
    Hq = m * h2(pf)
    P0 = float((1 - p) * (1 - p))
    Pn = float(p * p)
    Hp = -(P0 * log2(P0) + (N - 1) * Pn * log2(Pn))
    K = Hq - Hp
    cert = d2(beta, q)

    coarse_log1q = (m - 1) * (m / 2 - 1)
    coarse = float(beta) * coarse_log1q - h2(float(beta))
    print(
        f"m={m:2d} p={float(p):.12g} beta={float(beta):.12g} "
        f"qH={float(q):.12g} cert={cert:.12g} K={K:.12g} "
        f"cert/K={cert/K:.9f} coarse={coarse:.12g}"
    )

print("PASS: exact complement equation, forced high-side mass, and qH<beta verified.")
