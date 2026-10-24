"""Rigorous certificate for a heterogeneous recursive Numaro magnitude-flow stress family.

This is NOT a proof of unrestricted Fourier entropy-influence (FEI).

Let G be the exact balanced 18-variable Numaro seed used in the current FEI
handoff. Its first nine coordinates form class C and its last nine class A.
Let F_0 be a dictator and recursively define F_{d+1} by putting independent
copies of F_d into all nine class-C inputs of G and dictators into all nine
class-A inputs.

The script reconstructs G, checks its truth-table hash, derives rational
interval enclosures for the logarithmic constants, propagates the exact/upper
recurrences for I,Q,E,A through depth 25, bounds every later depth by a closed
geometric forcing estimate, and independently encloses the limiting A/I ratio.

Certified conclusion:
    A(F_d)/I(F_d) < 1.499392 < 3/2 for every d >= 1.
"""
from fractions import Fraction
from collections import Counter
import hashlib

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
LOG_TERMS = 24
TARGET = Fraction(1499392, 10**6)
DEPTH_CERT = 25


def reconstruct_seed():
    base = int("".join(SLICES[0]), 16)
    masks = [int("".join(row), 16) ^ base for row in SLICES[1:]]
    seen = base
    hosts = []
    for mask in masks:
        assert mask.bit_count() == 2
        assert not (seen & mask)
        seen |= mask
        hosts.append([x for x in range(512) if (mask >> x) & 1])
    core = [-1 if (base >> x) & 1 else 1 for x in range(512)]
    table = []
    for y in range(512):
        row = core.copy()
        for j, cells in enumerate(hosts):
            if (y >> j) & 1:
                for x in cells:
                    row[x] = -1
        table.extend(row)
    digest = hashlib.sha256(",".join(map(str, table)).encode()).hexdigest()
    assert digest == EXPECTED_SHA
    assert sum(table) == 0
    return table


def fwht_int(a):
    a = list(a)
    h = 1
    while h < len(a):
        for start in range(0, len(a), 2*h):
            for j in range(start, start+h):
                x, y = a[j], a[j+h]
                a[j], a[j+h] = x+y, x-y
        h *= 2
    return a


def pair_histogram(W, i):
    bit = 1 << i
    out = Counter()
    for low in range(len(W)):
        if not (low & bit):
            out[(abs(W[low]), abs(W[low | bit]))] += 1
    return out


def alpha_from_hist(hist, N):
    return Fraction(sum(count*v*v for (u, v), count in hist.items()), N*N)


def pow2(k):
    return Fraction(1 << k, 1) if k >= 0 else Fraction(1, 1 << (-k))


def normalize_pow2(x):
    assert x > 0
    k = x.numerator.bit_length() - x.denominator.bit_length()
    while x < pow2(k):
        k -= 1
    while x >= pow2(k+1):
        k += 1
    y = x / pow2(k)
    assert 1 <= y < 2
    return k, y


def ln_interval_unit(y, terms=LOG_TERMS):
    assert 1 <= y <= 2
    z = (y-1)/(y+1)
    if z == 0:
        return Fraction(0), Fraction(0)
    z2 = z*z
    zp = z
    partial = Fraction(0)
    for j in range(terms):
        if j:
            zp *= z2
        partial += zp / (2*j+1)
    lo = 2*partial
    remainder = 2*z**(2*terms+1) / ((2*terms+1)*(1-z2))
    return lo, lo + remainder


def log2_interval(x):
    k, y = normalize_pow2(x)
    ly_lo, ly_hi = ln_interval_unit(y)
    l2_lo, l2_hi = ln_interval_unit(Fraction(2))
    return Fraction(k) + ly_lo/l2_hi, Fraction(k) + ly_hi/l2_lo


def L_interval(hist, N):
    lo = Fraction(0)
    hi = Fraction(0)
    for (u, v), count in hist.items():
        if u and v and u > v:
            l, h = log2_interval(Fraction(u, v))
            mass = Fraction(count*v*v, N*N)
            lo += mass*l
            hi += mass*h
    return lo, hi


def C_interval(hist, N):
    lo = Fraction(0)
    hi = Fraction(0)
    for (u, v), count in hist.items():
        if u and v:
            l, h = log2_interval(Fraction(u, v))
            mass = Fraction(count*v*v, N*N)
            lo += mass*l
            hi += mass*h
    return lo, hi


def overlap_mass(hist, N):
    return Fraction(
        sum(count*v*v for (u, v), count in hist.items() if u and v),
        N*N,
    )


def decimal_floor(x, digits=16):
    assert x >= 0
    scale = 10**digits
    n = x.numerator*scale // x.denominator
    return f"{n//scale}.{n%scale:0{digits}d}"


def decimal_ceil(x, digits=16):
    assert x >= 0
    scale = 10**digits
    n = (x.numerator*scale + x.denominator - 1)//x.denominator
    return f"{n//scale}.{n%scale:0{digits}d}"


def main():
    table = reconstruct_seed()
    W = fwht_int(table)
    N = len(W)
    assert N == 1 << 18
    assert sorted(set(map(abs, W))) == [
        0,1024,2048,3072,4096,5120,8192,9216,19456,22528,58368
    ]

    hC = pair_histogram(W, 0)
    hA = pair_histogram(W, 9)
    assert all(pair_histogram(W, i) == hC for i in range(9))
    assert all(pair_histogram(W, i) == hA for i in range(9, 18))

    c = alpha_from_hist(hC, N)
    a = alpha_from_hist(hA, N)
    sC = Fraction(abs(W[1]), N)
    sA = Fraction(abs(W[1 << 9]), N)
    assert c == sC == Fraction(57,256)
    assert a == sA == Fraction(1,256)
    assert 9*c + 9*a == Fraction(261,128)

    LC_lo, LC_hi = L_interval(hC, N)
    LA_lo, LA_hi = L_interval(hA, N)
    CC_lo, CC_hi = C_interval(hC, N)
    BC = overlap_mass(hC, N)
    assert BC == Fraction(5613,32768)
    assert CC_lo > 0

    ellC_lo, ellC_hi = log2_interval(Fraction(1,c))
    assert Fraction(2) < ellC_lo < ellC_hi < Fraction(3)

    ratios_C = [Fraction(u,v) for (u,v) in hC if u and v]
    assert min(ratios_C) == Fraction(1,2)
    assert c < Fraction(1,2)

    r = 9*c
    b = 9*a
    lam = 9*c*c
    q0 = 9*a*a

    I = 9*c + 9*a
    Q = 9*c*c + 9*a*a
    E = lam*ellC_hi + q0*8
    A = 9*LC_hi + 9*LA_hi
    rows = [(1, A/I, I, Q, E, A)]

    for d in range(1, DEPTH_CERT):
        oldI, oldQ, oldE, oldA = I, Q, E, A
        I = r*oldI + b
        Q = lam*oldQ + q0
        E = lam*(oldE + ellC_hi*oldQ) + q0*8
        A = r*oldA + 9*(BC*oldE + CC_hi*oldQ) + 9*LA_hi
        rows.append((d+1, A/I, I, Q, E, A))

    Ecap = (lam*ellC_hi + 8*q0)/(1-lam)
    assert rows[0][4] < Ecap
    assert lam + q0 < 1
    Fmax = 9*(BC*Ecap + CC_hi) + 9*LA_hi

    d, ratioD, ID, QD, ED, AD = rows[-1]
    assert d == DEPTH_CERT
    later_ratio_upper = ratioD + Fmax/((r-1)*ID)

    assert max(row[1] for row in rows) < TARGET
    assert later_ratio_upper < TARGET
    assert TARGET < Fraction(3,2)

    def limit_bound(ellC, CC, LC, LA):
        I1 = 9*c + 9*a
        Q1 = 9*c*c + 9*a*a
        E1 = lam*ellC + q0*8
        A1 = 9*LC + 9*LA
        SQ = (Q1/r + q0/(r*(r-1))) / (1-lam/r)
        SE = (
            E1/r
            + (lam*ellC/r)*SQ
            + 8*q0/(r*(r-1))
        ) / (1-lam/r)
        SF = 9*BC*SE + 9*CC*SQ + 9*LA/(r-1)
        return (A1 + SF)/(I1 + b/(r-1))

    lim_lo = limit_bound(ellC_lo, CC_lo, LC_lo, LA_lo)
    lim_hi = limit_bound(ellC_hi, CC_hi, LC_hi, LA_hi)
    assert lim_lo <= lim_hi < TARGET
    assert Fraction(1499391,10**6) < lim_lo

    print("PASS")
    print("truth_table_sha256", EXPECTED_SHA)
    print("class_C_alpha_singleton", "57/256")
    print("class_A_alpha_singleton", "1/256")
    print("B_C", f"{BC.numerator}/{BC.denominator}")
    print("L_C_ratio_upper", decimal_ceil(LC_hi/c, 16))
    print("L_A_ratio_upper", decimal_ceil(LA_hi/a, 16))
    print("log2_256_over_57_upper", decimal_ceil(ellC_hi, 16))
    for d, ratio, *_ in rows:
        if d <= 10 or d in (12,15,20,25):
            print("depth_upper", d, decimal_ceil(ratio, 16))
    print("later_all_depth_upper", decimal_ceil(later_ratio_upper, 16))
    print("limit_lower", decimal_floor(lim_lo, 16))
    print("limit_upper", decimal_ceil(lim_hi, 16))
    print("certified_all_depth_target", "1.499392")
    print("strictly_below_3_over_2", True)


if __name__ == "__main__":
    main()
