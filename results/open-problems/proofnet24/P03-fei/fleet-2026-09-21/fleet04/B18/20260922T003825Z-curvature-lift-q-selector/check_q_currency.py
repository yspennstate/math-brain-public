from fractions import Fraction
from itertools import product

BIAS = (Fraction(1, 3), Fraction(1, 2), Fraction(2, 3))


def point_prob(x, p):
    q = Fraction(1)
    for z, t in zip(x, p):
        q *= t if z else (1 - t)
    return q


def coeff_square(values, p, mask):
    n = len(p)
    den = Fraction(1)
    num = Fraction(0)
    for i in range(n):
        if mask >> i & 1:
            den *= p[i] * (1 - p[i])
    for x in product((0, 1), repeat=n):
        idx = sum(x[i] << i for i in range(n))
        term = Fraction(values[idx]) * point_prob(x, p)
        for i in range(n):
            if mask >> i & 1:
                term *= Fraction(x[i]) - p[i]
        num += term
    return num * num if mask == 0 else num * num / den


def direct_q(values, p, i):
    n = len(p)
    others = [j for j in range(n) if j != i]
    d = Fraction(0)
    p0 = Fraction(0)
    p1 = Fraction(0)
    for xo in product((0, 1), repeat=n - 1):
        x0 = [0] * n
        x1 = [0] * n
        pr = Fraction(1)
        for j, z in zip(others, xo):
            x0[j] = x1[j] = z
            pr *= p[j] if z else (1 - p[j])
        x1[i] = 1
        idx0 = sum(x0[j] << j for j in range(n))
        idx1 = sum(x1[j] << j for j in range(n))
        y0 = int(values[idx0] == -1)
        y1 = int(values[idx1] == -1)
        p0 += pr * y0
        p1 += pr * y1
        if values[idx0] != values[idx1]:
            d += pr
    t = p[i]
    return t * (1 - t) * (d - (p1 - p0) ** 2)


def check(values, p):
    n = len(p)
    w = {m: coeff_square(values, p, m) for m in range(1 << n)}
    assert sum(w.values(), Fraction(0)) == 1

    influence = sum(Fraction(m.bit_count()) * a for m, a in w.items())
    variance = sum(w[m] for m in range(1, 1 << n))
    global_p = (influence - variance) / 4

    q_sum = Fraction(0)
    for i in range(n):
        it_i = sum(w[m] for m in w if m >> i & 1)
        singleton = w[1 << i]
        q_fourier = (it_i - singleton) / 4
        q_split = direct_q(values, p, i)
        assert q_fourier == q_split
        higher = sum(w[m] for m in w if (m >> i & 1) and m.bit_count() >= 2) / 4
        assert q_fourier == higher
        q_sum += q_fourier

    expected_q_sum = sum(Fraction(m.bit_count()) * a for m, a in w.items() if m.bit_count() >= 2) / 4
    higher_mass = sum(a for m, a in w.items() if m.bit_count() >= 2)
    assert q_sum == expected_q_sum
    assert q_sum - global_p == higher_mass / 4
    assert global_p <= q_sum <= 2 * global_p


cases = 0
for n in range(1, 4):
    for truth_bits in range(1 << (1 << n)):
        values = [-1 if (truth_bits >> k) & 1 else 1 for k in range(1 << n)]
        for p in product(BIAS, repeat=n):
            check(values, p)
            cases += 1

print(f"PASS exact rational Q-currency checks: {cases} gate/bias instances")
print("arities: 1,2,3; coordinate biases: 1/3,1/2,2/3")
print("verified: Parseval; split Q identity; singleton subtraction; P <= sum Q <= 2P")
