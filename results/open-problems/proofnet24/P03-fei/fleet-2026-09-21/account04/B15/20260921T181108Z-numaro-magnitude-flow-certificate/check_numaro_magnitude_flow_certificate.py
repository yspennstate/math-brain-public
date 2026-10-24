"""Exact certificate for the recursive Numaro aggregate magnitude-flow stress test.

This is a certificate for one structured family, not a proof of unrestricted FEI.

It reconstructs the exact 18-variable balanced monotone Numaro seed used by the
current FEI handoff, checks its hash and Walsh transform, verifies the two
coordinate classes, and uses rational upper bounds for every logarithm in the
proved balanced-composition recurrence.  It then combines the depth-15
recurrence upper bound with the previously proved geometric path-tail bound.

Certified conclusion:
    A(G^{o d}) / I(G^{o d}) < 1.488912 < 3/2
for every recursion depth d >= 1, where A is the aggregate one-sided Fourier
magnitude flow and G is this exact seed.
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
LOG_TERMS = 20
TARGET = Fraction(1488912, 10**6)


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
    """Rational enclosure for ln(y), 1 <= y <= 2."""
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
    # Positive tail: denominators are >= 2*terms+1.
    remainder = 2 * z**(2*terms+1) / ((2*terms+1) * (1-z2))
    return lo, lo + remainder


def log2_interval(x):
    """Rational enclosure for log_2(x), x > 0."""
    k, y = normalize_pow2(x)
    ly_lo, ly_hi = ln_interval_unit(y)
    l2_lo, l2_hi = ln_interval_unit(Fraction(2))
    return Fraction(k) + ly_lo/l2_hi, Fraction(k) + ly_hi/l2_lo


def M_upper(hist, q, N):
    """Rigorous upper bound for sum v^2 log_+(u/(v q))."""
    total = Fraction(0)
    for (u, v), count in hist.items():
        if u == 0 or v == 0:
            continue
        ratio = Fraction(u, v) / q
        if ratio > 1:
            _, hi = log2_interval(ratio)
            total += Fraction(count*v*v, N*N) * hi
    return total


def decimal_upper(x, digits=16):
    """Return a terminating decimal guaranteed >= nonnegative rational x."""
    assert x >= 0
    scale = 10**digits
    n = (x.numerator*scale + x.denominator - 1)//x.denominator
    return f"{n//scale}.{n%scale:0{digits}d}"


def main():
    table = reconstruct_seed()
    W = fwht_int(table)
    N = len(W)
    assert N == 1 << 18
    abs_levels = sorted(set(map(abs, W)))
    assert abs_levels == [0,1024,2048,3072,4096,5120,8192,9216,19456,22528,58368]

    hC = pair_histogram(W, 0)
    hA = pair_histogram(W, 9)
    assert all(pair_histogram(W, i) == hC for i in range(9))
    assert all(pair_histogram(W, i) == hA for i in range(9,18))

    alphaC = alpha_from_hist(hC, N)
    alphaA = alpha_from_hist(hA, N)
    singletonC = Fraction(abs(W[1]), N)
    singletonA = Fraction(abs(W[1 << 9]), N)
    assert alphaC == singletonC == Fraction(57,256)
    assert alphaA == singletonA == Fraction(1,256)
    assert 9*alphaC + 9*alphaA == Fraction(261,128)

    ellC = M_upper(hC, Fraction(1), N) / alphaC
    ellA = M_upper(hA, Fraction(1), N) / alphaA
    assert ellC < 1
    assert ellA < 3

    # Exact-rational upper recursion from the proved balanced-composition identity.
    stats = {
        "C": (alphaC, singletonC, hC),
        "A": (alphaA, singletonA, hA),
    }
    states = {
        (1,0): (9*alphaC, 9*alphaC*ellC),
        (0,1): (9*alphaA, 9*alphaA*ellA),
    }
    rows = [(1, sum(w for m,w in states.values()) /
                sum(m for m,w in states.values()))]
    cache = {}
    for depth in range(2, 16):
        nxt = {}
        for (nc,na),(mass,weighted) in states.items():
            q = singletonC**nc * singletonA**na
            p = alphaC**nc * alphaA**na
            z = q*q/p
            for name,(alpha,singleton,hist) in stats.items():
                key = (nc,na,name)
                if key not in cache:
                    cache[key] = M_upper(hist, q, N)
                increment = z * cache[key] / alpha
                factor = 9*alpha
                key2 = (nc + (name == "C"), na + (name == "A"))
                m2 = mass * factor
                w2 = weighted * factor + m2 * increment
                oldm, oldw = nxt.get(key2, (Fraction(0),Fraction(0)))
                nxt[key2] = (oldm+m2, oldw+w2)
        states = nxt
        ratio = sum(w for m,w in states.values()) / sum(m for m,w in states.values())
        rows.append((depth, ratio))

    # Every correction in the composition recurrence is nonnegative, so these are
    # increasing upper iterates.  The inherited path-tail theorem gives, after
    # depth 15, sum_{m>=15} theta^m (8m + ell_*).  We use ell_* < 3.
    assert all(rows[k][1] >= rows[k-1][1] for k in range(1,len(rows)))
    theta = Fraction(57,256)
    m0 = 15
    sum_q = theta**m0 / (1-theta)
    sum_mq = theta**m0 * (m0-(m0-1)*theta) / (1-theta)**2
    tail = 8*sum_mq + 3*sum_q
    total_upper = rows[-1][1] + tail

    assert total_upper < TARGET
    assert TARGET < Fraction(3,2)

    print("PASS")
    print("truth_table_sha256", EXPECTED_SHA)
    print("influence", "261/128")
    print("alpha_C", "57/256", "alpha_A", "1/256")
    print("ell_C_upper", decimal_upper(ellC, 16))
    print("ell_A_upper", decimal_upper(ellA, 16))
    for d, r in rows:
        print("depth_upper", d, decimal_upper(r, 16))
    print("tail_exact", f"{tail.numerator}/{tail.denominator}")
    print("tail_upper", decimal_upper(tail, 16))
    print("all_depth_upper", decimal_upper(total_upper, 16))
    print("certified_target", "1.488912")
    print("strictly_below_3_over_2", True)


if __name__ == "__main__":
    main()
