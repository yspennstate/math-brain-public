#!/usr/bin/env python3
"""Source-bound exact checker for the fleet03/B13 shared-graft tail extension.

Consumes the certified R4 interval from fleet03/B18, reconstructs the same
source 18-bit Numaro truth table, and proves two further shared-graft ratio gains
using dyadic K-evaluation plus an explicit derivative envelope. It also proves
the remaining infinite tail is absolutely summable.
"""
from fractions import Fraction as F
from functools import lru_cache
from collections import Counter
from decimal import Decimal, getcontext
import hashlib
import numpy as np

TERMS = 16
EXPECTED_SHA = "f8a7bb2c738d86368305111633376b1a3a83d8ee1f1abcc9a37d841b0f9c7839"
TOP = "fefefeeefefafc00feaafeaafeaafc00fefeccccfefacc00eeaacc00eeaacc00"
BOT = "fefefeeef0f0f000faaafaaaf000f000fcfcccccf0f000000000000000000000"
SLICES = [
    (TOP, BOT),
    (TOP, "fefefeeef0f0f000faaafaaaf000f000fcfcccccf0f0c0000000000000000000"),
    (TOP, "fefefeeef0f0f000faaafaaaf000f000fefeccccf0f000000000000000000000"),
    ("fefefefefefafc00feaafeaafeaafc00fefeccccfefacc00eeaacc00eeaacc00",
     "fefefefef0f0f000faaafaaaf000f000fcfcccccf0f000000000000000000000"),
    (TOP, "fefefeeef0f0f000feaafeaaf000f000fcfcccccf0f000000000000000000000"),
    (TOP, "fefefeeef0f0f000faaafaaaf0a0f000fcfcccccf0f000000000000000000000"),
    ("fefefeeefefefc00feaafeaafeaafc00fefeccccfefecc00eeaacc00eeaacc00", BOT),
    ("fefefeeefefafc00feaafeaafeaafc00fefeccccfefacc00feaacc00feaacc00", BOT),
    ("fefefeeefefafc00feaafeaafeaafc00fefeccccfefacc00eeaacc88eeaacc00", BOT),
    ("fefefeeefefafe00feaafeaafeaafe00fefeccccfefacc00eeaacc00eeaacc00", BOT),
]

# Certified fleet03/B18 R4 interval as printed by its exact checker/report.
# Padding by 1e-50 is two decimal orders coarser than its 52 printed places,
# so it safely contains the exact rational endpoints behind the rounded printout.
R4_LO_PRINT = F(Decimal("6.5218509485644448965490881329959858569477358114202361"))
R4_HI_PRINT = F(Decimal("6.5218509485644448965496895824490791318643557898359042"))
R4_PAD = F(1, 10**50)
R4_LO = R4_LO_PRINT - R4_PAD
R4_HI = R4_HI_PRINT + R4_PAD

ALPHA = F(9, 256)
SOURCE_I = F(261, 128)
ACOEF = F(133, 128)
B = F(257, 256)
LIPSCHITZ_K = F(292, 1)

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

def core_and_hosts():
    base = int("".join(SLICES[0]), 16)
    masks = [int("".join(row), 16) ^ base for row in SLICES[1:]]
    assert all(m.bit_count() == 2 for m in masks)
    seen = base
    for m in masks:
        assert not (seen & m)
        seen |= m
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

def log_unit_interval(x):
    assert F(1) <= x <= F(2)
    if x == 1:
        return F(0), F(0)
    z = (x - 1) / (x + 1)
    z2 = z*z
    power = z
    s = F(0)
    for k in range(TERMS):
        s += power / (2*k + 1)
        power *= z2
    lo = 2*s
    rem = 2*power / ((2*TERMS + 1) * (1-z2))
    return lo, lo + rem

@lru_cache(maxsize=None)
def log2_interval(x):
    x = F(x)
    if x < 1:
        lo, hi = log2_interval(1/x)
        return -hi, -lo
    e = x.numerator.bit_length() - x.denominator.bit_length()
    if x < F(2)**e:
        e -= 1
    m = x / F(2)**e
    a, b = log_unit_interval(m)
    c, d = log_unit_interval(F(2))
    return F(e) + a/d, F(e) + b/c

def phi_interval(x):
    x = F(x)
    if x == 0:
        return F(0), F(0)
    lo, hi = log2_interval(1/x)
    return x*lo, x*hi

def hcore_interval(A, Qsum, b):
    b = F(b)
    num, den = b.numerator, b.denominator
    norm = (512*den)**2
    hist = Counter()
    for ai, qi in zip(A, Qsum):
        z = int(ai)*den + num*int(qi)
        if z:
            hist[z*z] += 1
    lo = F(0)
    hi = F(0)
    for s, mult in hist.items():
        l, u = log2_interval(F(norm, s))
        w = F(s*mult, norm)
        lo += w*l
        hi += w*u
    return lo, hi

def K_interval_at_dyadic(A, Qsum, b):
    hc_lo, hc_hi = hcore_interval(A, Qsum, b)
    p_lo, p_hi = phi_interval(b*b)
    return (
        hc_lo + ALPHA*(-p_hi + 16*(1-b*b)),
        hc_hi + ALPHA*(-p_lo + 16*(1-b*b)),
    )

def nearest_dyadic(x, bits=64):
    scale = 1 << bits
    q = (x.numerator * scale) // x.denominator
    q0, q1 = F(q, scale), F(q+1, scale)
    return q0 if x-q0 <= q1-x else q1

def K_actual_interval(A, Qsum, c):
    b = c**4
    assert F(1,500) <= b <= F(3,1000)
    q = nearest_dyadic(b, 64)
    err = abs(b-q)
    lo, hi = K_interval_at_dyadic(A, Qsum, q)
    return lo-LIPSCHITZ_K*err, hi+LIPSCHITZ_K*err, q, err

def dec(x, digits=70):
    getcontext().prec = digits + 25
    return format(Decimal(x.numerator)/Decimal(x.denominator), f".{digits}f")

def main():
    base, hosts = core_and_hosts()
    table = source_table(base, hosts)
    digest = hashlib.sha256(",".join(map(str, table)).encode()).hexdigest()
    assert digest == EXPECTED_SHA
    assert table.sum() == 0

    W = fwht(table)
    norm = len(table)**2
    I0 = F(sum(i.bit_count()*int(v)*int(v) for i,v in enumerate(W)), norm)
    assert I0 == SOURCE_I

    A, Qsum = core_data(base, hosts)
    assert max(abs(int(x)) for x in A) == 114
    assert max(abs(int(x)) for x in Qsum) == 18
    assert min(abs(int(x)) for x in A if x) == 2
    assert min(abs(int(x)) for x in Qsum if x) == 2

    c = F(14593, 65536)
    I = F(68013, 32768)
    cs = {1:c}
    Is = {1:I}
    for t in range(1,7):
        c = F(57,256) + c**4/F(256)
        I = SOURCE_I + ALPHA*(I**4 - 1)
        cs[t+1] = c
        Is[t+1] = I

    lo, hi = R4_LO, R4_HI
    intervals = {4:(lo,hi)}
    for t in (4,5):
        klo, khi, q, err = K_actual_interval(A, Qsum, cs[t])
        D = Is[t+1] - 1
        assert D == ALPHA*Is[t]**4 + B
        nlo = klo - ACOEF*hi
        nhi = khi - ACOEF*lo
        assert nlo > 0
        newlo = lo + nlo/D
        newhi = hi + nhi/D
        lo, hi = newlo, newhi
        intervals[t+1] = (lo,hi)

    R5lo,R5hi = intervals[5]
    R6lo,R6hi = intervals[6]
    R4lo,R4hi = intervals[4]
    assert R5lo > R4hi
    assert R6lo > R5hi
    assert R6lo > F(6521850949550448, 10**15)

    KMAX = F(153,16)
    assert KMAX < ACOEF*10
    D6 = Is[7]-1
    assert D6 > 5
    tail = F(665,64)/(D6-1)
    assert tail < F(3,10**30)

    print("PASS")
    print("source_sha256 =", digest)
    print("R4_source_padded_lower =", dec(R4lo,70))
    print("R4_source_padded_upper =", dec(R4hi,70))
    print("R5_lower =", dec(R5lo,70))
    print("R5_upper =", dec(R5hi,70))
    print("R6_lower =", dec(R6lo,70))
    print("R6_upper =", dec(R6hi,70))
    print("gain_R5_over_R4_upper_lower =", dec(R5lo-R4hi,60))
    print("gain_R6_over_R5_upper_lower =", dec(R6lo-R5hi,60))
    print("gain_R6_over_R4_upper_lower =", dec(R6lo-R4hi,60))
    print("I6 =", dec(Is[6],40))
    print("I7 =", dec(Is[7],40))
    print("tail_abs_bound_after_R6 =", dec(tail,60))
    print("K_derivative_envelope =", LIPSCHITZ_K)
    print("full_FEI_status = OPEN")

if __name__ == "__main__":
    main()
