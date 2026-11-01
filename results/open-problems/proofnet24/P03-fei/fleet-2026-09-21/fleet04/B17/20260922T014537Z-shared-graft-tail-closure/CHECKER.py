from __future__ import annotations

from decimal import Decimal, localcontext, ROUND_FLOOR, ROUND_CEILING, getcontext
from fractions import Fraction as F

PREC = 100
getcontext().prec = PREC
NTERMS = 45
ALPHA = F(9, 256)
ISRC = F(261, 128)
B = F(257, 256)
D0 = F(133, 128)
U = F(153, 16)  # uniform upper bound for K(b), 0<=b<=1

# Exact multiplicities of (A_S,Q_S) Walsh numerators for the source-bound
# nine-bit shared-core transform.  Sum of multiplicities is 512.
PAIRS = [
    ((-18, -2), 72),
    ((2, 2), 72),
    ((0, 0), 46),
    ((-16, 0), 36),
    ((16, 0), 36),
    ((10, -6), 36),
    ((4, 4), 36),
    ((-4, -4), 36),
    ((-2, -2), 36),
    ((44, -4), 18),
    ((-44, 4), 18),
    ((-6, 10), 18),
    ((38, 6), 12),
    ((114, 2), 9),
    ((8, 8), 9),
    ((-8, -8), 9),
    ((4, -12), 6),
    ((-4, 12), 6),
    ((2, 18), 1),
]


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


def mul(a, b):
    candidates = []
    for x in a:
        for y in b:
            candidates.append(x * y)
    with localcontext() as c:
        c.prec = PREC
        c.rounding = ROUND_FLOOR
        lo = min(candidates)
    with localcontext() as c:
        c.prec = PREC
        c.rounding = ROUND_CEILING
        hi = max(candidates)
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


def powpos(a, n):
    assert n >= 0 and a[0] >= 0
    out = (Decimal(1), Decimal(1))
    base = a
    while n:
        if n & 1:
            out = mulpos(out, base)
        base = mulpos(base, base)
        n >>= 1
    return out


def log_unit(m: F):
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


def hcore(b: F):
    out = (Decimal(0), Decimal(0))
    for (a, q), mult in PAIRS:
        coeff = F(a, 512) + b * F(q, 512)
        p = coeff * coeff
        if p:
            term = phi_interval(p)
            term = mulpos(term, (Decimal(mult), Decimal(mult)))
            out = add(out, term)
    return out


def one_round(I, R, c):
    # Exact depth-four balanced self-composition followed by shared-core graft.
    b = c ** 4
    negative_phi = (-phi_interval(b*b)[1], -phi_interval(b*b)[0])
    bracket = add(negative_phi, qbounds(F(16) * (1 - b*b)))
    K = add(hcore(b), mulpos(qbounds(ALPHA), bracket))
    numerator = sub(K, mulpos(qbounds(D0), R))
    assert numerator[0] > 0
    denominator = add(mulpos(qbounds(ALPHA), powpos(I, 4)), qbounds(B))
    gain = divpos(numerator, denominator)
    R2 = add(R, gain)
    I2 = add(qbounds(ISRC - ALPHA), mulpos(qbounds(ALPHA), powpos(I, 4)))
    c2 = F(57, 256) + b / F(256)
    return I2, R2, c2, gain


def main():
    assert sum(mult for _, mult in PAIRS) == 512

    # Parseval polynomial for the nine-bit shared-core block:
    # sum_S (a_S + b q_S)^2 = 1-alpha + alpha b^2 <= 1.
    denom = 512 * 512
    s_a2 = sum(F(mult * a * a, denom) for (a, q), mult in PAIRS)
    s_cross = sum(F(mult * 2 * a * q, denom) for (a, q), mult in PAIRS)
    s_q2 = sum(F(mult * q * q, denom) for (a, q), mult in PAIRS)
    assert s_a2 == 1 - ALPHA
    assert s_cross == 0
    assert s_q2 == ALPHA

    # Start from fleet01/B18's certified F2 displayed value, widened by 1e-45,
    # exactly as fleet03/B15 did.  I2 and c2 are exact rationals.
    x = Decimal('6.521850763518463531668608228451477683404661344')
    eps = Decimal('1e-45')
    R = (x - eps, x + eps)
    I = qbounds(F(784028312243315011737, 295147905179352825856))
    c1 = F(14593, 65536)
    c = F(57, 256) + c1**4 / F(256)

    for idx in range(3, 8):
        I, R, c, gain = one_round(I, R, c)
        if idx == 7:
            print('F7_R_lower=' + str(R[0]))
            print('F7_R_upper=' + str(R[1]))
            print('F7_gain_lower=' + str(gain[0]))
            print('F7_I_lower=' + str(I[0]))

    target = Decimal('6.521850949550448184840160538860511501350329679')
    assert R[0] > target
    assert I[0] > Decimal('1e30')

    # Uniform tail closure for this fixed depth-four recurrence.
    #
    # H_core(b)<=9 because its 512 Fourier masses have total <=1.
    # Hence K(b)<=9 + 16*alpha = 153/16 = U for 0<=b<=1.
    #
    # Let D_next=I_next-1=alpha I^4+B.  From I7>1e30,
    # D8>alpha*1e120.  Therefore any positive post-F7 increment is
    # < U/(alpha*1e120) = 272e-120 = 2.72e-118.
    # Future denominators satisfy D_{n+1}>=alpha D_n^4. Since D8 is
    # astronomically >1, the corresponding positive-increment bounds
    # fall by a factor <1/2, so their whole tail is <2 times the first.
    assert U / ALPHA == 272
    first_tail = Decimal(272) * (Decimal(10) ** Decimal(-120))
    tail_bound = Decimal(2) * first_tail
    D8_crude = qbounds(ALPHA)[0] * (Decimal(10) ** Decimal(120))
    assert qbounds(ALPHA)[0] * D8_crude**3 > Decimal(2)
    assert tail_bound == Decimal('5.44e-118')

    c0 = Decimal('6.4548')
    margin_lower = Decimal(4) * (R[0] - c0)

    print('PASS')
    print('certified_FEI_lower_bound_gt=' + str(target))
    print('old_reference_margin_lower=' + str(margin_lower))
    print('fixed_d4_post_F7_positive_tail_lt=' + str(tail_bound))
    print('full_FEI_status=OPEN')
    print('brain_status=WITHOUT_VERIFIED_BRAIN')


if __name__ == '__main__':
    main()
