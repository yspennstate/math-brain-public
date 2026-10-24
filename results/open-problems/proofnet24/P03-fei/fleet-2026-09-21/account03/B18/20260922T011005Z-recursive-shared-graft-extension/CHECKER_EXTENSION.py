from __future__ import annotations

from collections import Counter
from fractions import Fraction as F
from functools import lru_cache
from decimal import Decimal, getcontext
import hashlib
import numpy as np

# This extends the source-valid account01/B18 shared-graft checker by two rounds.
# Twenty atanh-series terms give an explicit exact-rational remainder interval
# much narrower than the strict signs certified below.
TERMS = 20
EXPECTED_SHA = 'f8a7bb2c738d86368305111633376b1a3a83d8ee1f1abcc9a37d841b0f9c7839'
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
    x = np.array(a, dtype=np.int64, copy=True)
    h = 1
    while h < len(x):
        y = x.reshape(-1, 2*h)
        u = y[:, :h].copy()
        v = y[:, h:].copy()
        y[:, :h] = u + v
        y[:, h:] = u - v
        h *= 2
    return x


def log_unit_interval(x):
    assert F(1) <= x <= F(2)
    if x == 1:
        return F(0), F(0)
    z = (x-1)/(x+1)
    z2 = z*z
    power = z
    s = F(0)
    for k in range(TERMS):
        s += power/(2*k+1)
        power *= z2
    lo = 2*s
    rem = 2*power/((2*TERMS+1)*(1-z2))
    return lo, lo+rem


@lru_cache(maxsize=None)
def log2_interval(x):
    x = F(x)
    if x < 1:
        lo, hi = log2_interval(1/x)
        return -hi, -lo
    e = x.numerator.bit_length() - x.denominator.bit_length()
    if x < F(2)**e:
        e -= 1
    m = x/F(2)**e
    a, b = log_unit_interval(m)
    c, d = log_unit_interval(F(2))
    return F(e)+a/d, F(e)+b/c


def entropy_hist(hist, norm):
    lo = F(0)
    hi = F(0)
    for s, mult in hist.items():
        if not s:
            continue
        a, b = log2_interval(F(norm, s))
        w = F(s*mult, norm)
        lo += w*a
        hi += w*b
    return lo, hi


def phi_interval(x):
    x = F(x)
    if not x:
        return F(0), F(0)
    a, b = log2_interval(1/x)
    return x*a, x*b


def core_and_hosts():
    base = int(''.join(SLICES[0]), 16)
    masks = [int(''.join(row), 16) ^ base for row in SLICES[1:]]
    assert all(m.bit_count() == 2 for m in masks)
    hosts = [[x for x in range(512) if (m >> x) & 1] for m in masks]
    return base, hosts


def source_table(base, hosts):
    core = np.array([-1 if (base >> x) & 1 else 1 for x in range(512)], dtype=np.int64)
    table = np.tile(core, (512, 1))
    for j, cells in enumerate(hosts):
        mask = (np.arange(512) & (1 << j)) != 0
        table[np.ix_(mask, np.array(cells, dtype=int))] = -1
    return table.ravel()


def core_data(base, hosts):
    a = np.array([-1 if (base >> x) & 1 else 1 for x in range(512)], dtype=np.int64)
    for h in hosts:
        a[h] = 0
    A = fwht(a)
    Q = []
    for lo, hi in hosts:
        q = np.zeros(512, dtype=np.int64)
        q[lo] = 1
        q[hi] = -1
        Q.append(fwht(q))
    return A, np.sum(np.array(Q), axis=0)


def hcore_interval(A, Qsum, b):
    b = F(b)
    num, den = b.numerator, b.denominator
    nums = [int(ai)*den + num*int(qi) for ai, qi in zip(A, Qsum)]
    norm = (512*den)**2
    return entropy_hist(Counter(v*v for v in nums if v), norm)


def transform(Hlo, Hhi, I, c, source_I, A, Qsum):
    alpha = F(9, 256)
    IA = I**4
    factor = (IA-1)/(I-1)
    b = c**4
    hclo, hchi = hcore_interval(A, Qsum, b)
    philo, phihi = phi_interval(b*b)
    Hnlo = hclo + alpha*(Hlo*factor - phihi + 16*(1-b*b))
    Hnhi = hchi + alpha*(Hhi*factor - philo + 16*(1-b*b))
    In = source_I + alpha*(IA-1)
    cn = F(57, 256) + b/F(256)
    return Hnlo, Hnhi, In, cn


def dec(x, digits=70):
    getcontext().prec = digits + 20
    return format(Decimal(x.numerator)/Decimal(x.denominator), f'.{digits}f')


def main():
    base, hosts = core_and_hosts()
    table = source_table(base, hosts)
    digest = hashlib.sha256(','.join(map(str, table)).encode()).hexdigest()
    assert digest == EXPECTED_SHA
    assert table.sum() == 0

    W = fwht(table)
    norm = len(table)**2
    assert sum(int(v)*int(v) for v in W) == norm
    Hglo, Hghi = entropy_hist(Counter(int(v)*int(v) for v in W if v), norm)
    source_I = F(sum(i.bit_count()*int(v)*int(v) for i, v in enumerate(W)), norm)
    assert source_I == F(261, 128)

    A, Qsum = core_data(base, hosts)
    alpha = F(9, 256)
    b0 = F(1, 256)
    hc0lo, hc0hi = hcore_interval(A, Qsum, b0)
    p0lo, p0hi = phi_interval(b0*b0)
    H1lo = hc0lo + alpha*(Hglo-p0hi+16*(1-b0*b0))
    H1hi = hc0hi + alpha*(Hghi-p0lo+16*(1-b0*b0))
    I1 = source_I + alpha*(source_I-1)
    assert I1 == F(68013, 32768)
    c1 = F(14593, 65536)

    H2lo, H2hi, I2, c2 = transform(H1lo, H1hi, I1, c1, source_I, A, Qsum)
    H3lo, H3hi, I3, c3 = transform(H2lo, H2hi, I2, c2, source_I, A, Qsum)
    H4lo, H4hi, I4, c4 = transform(H3lo, H3hi, I3, c3, source_I, A, Qsum)

    R1lo, R1hi = H1lo/(I1-1), H1hi/(I1-1)
    R2lo, R2hi = H2lo/(I2-1), H2hi/(I2-1)
    R3lo, R3hi = H3lo/(I3-1), H3hi/(I3-1)
    R4lo, R4hi = H4lo/(I4-1), H4hi/(I4-1)

    gain32 = R3lo-R2hi
    gain43 = R4lo-R3hi
    gain42 = R4lo-R2hi

    # All sign decisions are exact comparisons of Fraction endpoints.
    assert gain32 > F(152, 1_000_000_000)      # > 1.52e-7
    assert gain43 > F(327, 10_000_000_000)     # > 3.27e-8
    assert gain42 > F(185, 1_000_000_000)      # > 1.85e-7
    assert R4lo > F(6521850948, 1_000_000_000) # > 6.521850948

    print('PASS')
    print('source_sha256=' + digest)
    print('TERMS=' + str(TERMS))
    print('I1=' + str(I1))
    print('I2=' + str(I2))
    print('I3=' + str(I3))
    print('I4_approx=' + dec(I4, 40))
    print('c1=' + str(c1))
    print('c2=' + dec(c2, 45))
    print('c3=' + dec(c3, 45))
    print('c4=' + dec(c4, 45))
    print('R1_lower=' + dec(R1lo))
    print('R1_upper=' + dec(R1hi))
    print('R2_lower=' + dec(R2lo))
    print('R2_upper=' + dec(R2hi))
    print('R3_lower=' + dec(R3lo))
    print('R3_upper=' + dec(R3hi))
    print('R4_lower=' + dec(R4lo))
    print('R4_upper=' + dec(R4hi))
    print('gain_R3_over_R2_lower=' + dec(gain32, 60))
    print('gain_R4_over_R3_lower=' + dec(gain43, 60))
    print('gain_R4_over_R2_lower=' + dec(gain42, 60))
    print('full_FEI_status=OPEN')


if __name__ == '__main__':
    main()
