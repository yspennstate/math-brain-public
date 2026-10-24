from __future__ import annotations

from decimal import Decimal, localcontext, ROUND_FLOOR, ROUND_CEILING
from fractions import Fraction as F

# Extension of account01/B18, report blob
# cbe682d84b52232ab4e91367b08bbfe73d74a39e.
# We start from its certified F2 interval, widened by 1e-45 on each side,
# and iterate its exact depth-4 self-composition + nine-host graft map.

PREC = 100
NTERMS = 45
ALPHA = F(9, 256)
ISRC = F(261, 128)
B = F(257, 256)
D0 = F(133, 128)

TOP = 'fefefeeefefafc00feaafeaafeaafc00fefeccccfefacc00eeaacc00eeaacc00'
BOT = 'fefefeeef0f0f000faaafaaaf000f000fcfcccccf0f000000000000000000000'
SLICES = [
    (TOP, BOT),
    (TOP, 'fefefeeef0f0f000faaafaaaf000f000fcfcccccf0f0c0000000000000000000'),
    (TOP, 'fefefeeef0f0f000faaafaaaf000f000fefeccccf0f000000000000000000000'),
    ('fefefefefefafc00feaafeaafeaafc00fefeccccfefacc00eeaacc00eeaacc00',
     'fefefefef0f0f000faaafaaaf000f000fcfcccccf0f000000000000000000000'),
    (TOP, 'fefefeeef0f0f000feaafeaaf000f000fcfcccccf0f000000000000000000000'),
    (TOP, 'fefefeeef0f0f000faaafaaaf0a0f000fcfcccccf0f000000000000000000000'),
    ('fefefeeefefefc00feaafeaafeaafc00fefeccccfefecc00eeaacc00eeaacc00', BOT),
    ('fefefeeefefafc00feaafeaafeaafc00fefeccccfefacc00feaacc00feaacc00', BOT),
    ('fefefeeefefafc00feaafeaafeaafc00fefeccccfefacc00eeaacc88eeaacc00', BOT),
    ('fefefeeefefafe00feaafeaafeaafe00fefeccccfefacc00eeaacc00eeaacc00', BOT),
]


def fwht(a):
    x = list(a)
    h = 1
    while h < len(x):
        for i in range(0, len(x), 2 * h):
            for j in range(i, i + h):
                u, v = x[j], x[j + h]
                x[j], x[j + h] = u + v, u - v
        h *= 2
    return x


def core_data():
    base = int(''.join(SLICES[0]), 16)
    masks = [int(''.join(row), 16) ^ base for row in SLICES[1:]]
    assert all(m.bit_count() == 2 for m in masks)
    hosts = [[x for x in range(512) if (m >> x) & 1] for m in masks]
    a = [-1 if (base >> x) & 1 else 1 for x in range(512)]
    for h in hosts:
        for x in h:
            a[x] = 0
    A = fwht(a)
    qsum = [0] * 512
    for lo, hi in hosts:
        q = [0] * 512
        q[lo], q[hi] = 1, -1
        w = fwht(q)
        qsum = [u + v for u, v in zip(qsum, w)]
    assert A[1] == 114 and qsum[1] == 2
    return A, qsum


def qbounds(q: F):
    with localcontext() as c:
        c.prec = PREC
        c.rounding = ROUND_FLOOR
        lo = Decimal(q.numerator) / Decimal(q.denominator)
    with localcontext() as c:
        c.prec = PREC
        c.rounding = ROUND_CEILING
        hi = Decimal(q.numerator) / Decimal(q.denominator)
    return lo, hi


def add(a, b):
    with localcontext() as c:
        c.prec = PREC
        c.rounding = ROUND_FLOOR
        lo = a[0] + b[0]
    with localcontext() as c:
        c.prec = PREC
        c.rounding = ROUND_CEILING
        hi = a[1] + b[1]
    return lo, hi


def sub(a, b):
    with localcontext() as c:
        c.prec = PREC
        c.rounding = ROUND_FLOOR
        lo = a[0] - b[1]
    with localcontext() as c:
        c.prec = PREC
        c.rounding = ROUND_CEILING
        hi = a[1] - b[0]
    return lo, hi


def mulpos(a, b):
    assert a[0] >= 0 and b[0] >= 0
    with localcontext() as c:
        c.prec = PREC
        c.rounding = ROUND_FLOOR
        lo = a[0] * b[0]
    with localcontext() as c:
        c.prec = PREC
        c.rounding = ROUND_CEILING
        hi = a[1] * b[1]
    return lo, hi


def divpos(a, b):
    assert a[0] >= 0 and b[0] > 0
    with localcontext() as c:
        c.prec = PREC
        c.rounding = ROUND_FLOOR
        lo = a[0] / b[1]
    with localcontext() as c:
        c.prec = PREC
        c.rounding = ROUND_CEILING
        hi = a[1] / b[0]
    return lo, hi


def scale(a, n: int):
    return mulpos(a, (Decimal(n), Decimal(n)))


def log_unit(m: F):
    # Rigorous atanh series: ln m = 2 sum z^(2j+1)/(2j+1), z=(m-1)/(m+1).
    assert F(1) <= m <= F(2)
    if m == 1:
        return Decimal(0), Decimal(0)
    z = qbounds((m - 1) / (m + 1))
    z2 = mulpos(z, z)
    power = z
    s = (Decimal(0), Decimal(0))
    for k in range(NTERMS):
        s = add(s, divpos(power, (Decimal(2*k+1), Decimal(2*k+1))))
        power = mulpos(power, z2)
    with localcontext() as c:
        c.prec = PREC
        c.rounding = ROUND_FLOOR
        one_minus_z2_lo = Decimal(1) - z2[1]
        lo = Decimal(2) * s[0]
    with localcontext() as c:
        c.prec = PREC
        c.rounding = ROUND_CEILING
        rem_hi = Decimal(2) * power[1] / (Decimal(2*NTERMS+1) * one_minus_z2_lo)
        hi = Decimal(2) * s[1] + rem_hi
    return lo, hi


LN2 = log_unit(F(2))


def log2_ge1(x: F):
    assert x >= 1
    e = x.numerator.bit_length() - x.denominator.bit_length()
    if x < F(2) ** e:
        e -= 1
    m = x / (F(2) ** e)
    y = divpos(log_unit(m), LN2)
    with localcontext() as c:
        c.prec = PREC
        c.rounding = ROUND_FLOOR
        lo = Decimal(e) + y[0]
    with localcontext() as c:
        c.prec = PREC
        c.rounding = ROUND_CEILING
        hi = Decimal(e) + y[1]
    return lo, hi


def phi_interval(p: F):
    if p == 0:
        return Decimal(0), Decimal(0)
    return mulpos(qbounds(p), log2_ge1(1 / p))


def hcore(A, qsum, b: F):
    out = (Decimal(0), Decimal(0))
    for ai, qi in zip(A, qsum):
        coeff = F(ai, 512) + b * F(qi, 512)
        p = coeff * coeff
        if p:
            out = add(out, phi_interval(p))
    return out


def one_round(A, qsum, I: F, R, c: F):
    # Depth-4 self-composition then the exact nine-host shared-core transform.
    b = c ** 4
    K = add(
        hcore(A, qsum, b),
        mulpos(qbounds(ALPHA), add(sub((Decimal(0), Decimal(0)), phi_interval(b*b)), qbounds(F(16) * (1-b*b))))
    )
    numerator = sub(K, mulpos(qbounds(D0), R))
    assert numerator[0] > 0
    denominator = ALPHA * (I ** 4) + B
    gain = divpos(numerator, qbounds(denominator))
    R2 = add(R, gain)
    I2 = ISRC + ALPHA * (I ** 4 - 1)
    c2 = F(57, 256) + b / F(256)
    return I2, R2, c2, gain


def main():
    A, qsum = core_data()

    # account01/B18 CHECK_OUTPUT certifies this displayed F2 value to 45 digits;
    # widen by a full 1e-45 on each side before using it.
    x = Decimal('6.521850763518463531668608228451477683404661344')
    eps = Decimal('1e-45')
    R = (x - eps, x + eps)
    I = F(784028312243315011737, 295147905179352825856)
    c1 = F(14593, 65536)
    c = F(57, 256) + (c1 ** 4) / F(256)

    expected_gain_floors = {
        3: Decimal('1.5233725364776506e-7'),
        4: Decimal('3.2708727717115429e-8'),
        5: Decimal('9.860010492662845e-10'),
        6: Decimal('2.2390247684047e-15'),
    }

    for idx in range(3, 7):
        I, R, c, gain = one_round(A, qsum, I, R, c)
        assert gain[0] > expected_gain_floors[idx]
        print(f'F{idx}_I={I}')
        print(f'F{idx}_R_lower={R[0]}')
        print(f'F{idx}_R_upper={R[1]}')
        print(f'F{idx}_gain_lower={gain[0]}')

    target = Decimal('6.5218509495504481848401605388605')
    assert R[0] > target
    print('PASS')
    print('certified_FEI_lower_bound_gt=' + str(target))
    print('full_FEI_status=OPEN')


if __name__ == '__main__':
    main()
