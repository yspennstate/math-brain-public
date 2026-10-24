"""Certificate for the Numaro recursive-tree Bellman barrier.

This is a self-check for a structured FEI lemma, NOT a proof of unrestricted FEI.

For the exact recovered balanced 18-variable Numaro seed G, let class C be
coordinates 0..8 and class A coordinates 9..17.  Consider the full recursive
tree closure obtained by replacing ANY subset of C or A dictator leaves by
arbitrary earlier members of the same closure on disjoint variables.

The proof in REPORT.md shows that the aggregate one-sided magnitude flow A
obeys A/I < R_* throughout this entire nonstationary closure, with
R_* < 1.499392 < 3/2.  Pure C recursion approaches R_*, so R_* is the sharp
constant of this closure.

This script reconstructs G, certifies all seed constants with rational
logarithm intervals, and checks the Bellman coefficients/sign conditions.
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
        partial += zp/(2*j+1)
    lo = 2*partial
    remainder = 2*z**(2*terms+1)/((2*terms+1)*(1-z2))
    return lo, lo + remainder

def log2_interval(x):
    k, y = normalize_pow2(x)
    ly_lo, ly_hi = ln_interval_unit(y)
    l2_lo, l2_hi = ln_interval_unit(Fraction(2))
    return Fraction(k) + ly_lo/l2_hi, Fraction(k) + ly_hi/l2_lo

def weighted_log_interval(hist, N, positive_part):
    lo = Fraction(0)
    hi = Fraction(0)
    for (u, v), count in hist.items():
        if not (u and v):
            continue
        if positive_part and not (u > v):
            continue
        l, h = log2_interval(Fraction(u, v))
        mass = Fraction(count*v*v, N*N)
        lo += mass*l
        hi += mass*h
    return lo, hi

def overlap_mass(hist, N):
    return Fraction(sum(count*v*v for (u,v), count in hist.items() if u and v), N*N)

class Iv:
    def __init__(self, lo, hi=None):
        self.lo = Fraction(lo)
        self.hi = Fraction(lo if hi is None else hi)
        assert self.lo <= self.hi
    def __add__(self, other):
        other = other if isinstance(other, Iv) else Iv(other)
        return Iv(self.lo+other.lo, self.hi+other.hi)
    __radd__ = __add__
    def __neg__(self):
        return Iv(-self.hi, -self.lo)
    def __sub__(self, other):
        return self + -(other if isinstance(other, Iv) else Iv(other))
    def __rsub__(self, other):
        return (other if isinstance(other, Iv) else Iv(other)) - self
    def __mul__(self, other):
        other = other if isinstance(other, Iv) else Iv(other)
        vals = [self.lo*other.lo, self.lo*other.hi,
                self.hi*other.lo, self.hi*other.hi]
        return Iv(min(vals), max(vals))
    __rmul__ = __mul__
    def inv(self):
        assert not (self.lo <= 0 <= self.hi)
        vals = [1/self.lo, 1/self.hi]
        return Iv(min(vals), max(vals))
    def __truediv__(self, other):
        other = other if isinstance(other, Iv) else Iv(other)
        return self*other.inv()
    def __rtruediv__(self, other):
        return (other if isinstance(other, Iv) else Iv(other))/self

def decimal_floor(x, digits=16):
    scale = 10**digits
    sign = -1 if x < 0 else 1
    y = abs(x)
    n = y.numerator*scale // y.denominator
    if sign > 0:
        return f"{n//scale}.{n%scale:0{digits}d}"
    nceil = (y.numerator*scale + y.denominator - 1)//y.denominator
    return f"-{nceil//scale}.{nceil%scale:0{digits}d}"

def decimal_ceil(x, digits=16):
    scale = 10**digits
    sign = -1 if x < 0 else 1
    y = abs(x)
    if sign > 0:
        n = (y.numerator*scale + y.denominator - 1)//y.denominator
        return f"{n//scale}.{n%scale:0{digits}d}"
    nfloor = y.numerator*scale // y.denominator
    return f"-{nfloor//scale}.{nfloor%scale:0{digits}d}"

def show_iv(name, v, digits=16):
    print(f"{name} in [{decimal_floor(v.lo,digits)}, {decimal_ceil(v.hi,digits)}]")

def main():
    table = reconstruct_seed()
    W = fwht_int(table)
    N = len(W)
    assert N == 1 << 18

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

    BC = overlap_mass(hC, N)
    BA = overlap_mass(hA, N)
    assert BC == Fraction(5613,32768)
    assert BA == Fraction(117,32768)

    ratiosC = [Fraction(u,v) for (u,v) in hC if u and v]
    ratiosA = [Fraction(u,v) for (u,v) in hA if u and v]
    assert min(ratiosC) == Fraction(1,2)
    assert min(ratiosA) == 1
    assert c < Fraction(1,2)

    LC_lo, LC_hi = weighted_log_interval(hC, N, True)
    LA_lo, LA_hi = weighted_log_interval(hA, N, True)
    CC_lo, CC_hi = weighted_log_interval(hC, N, False)
    CA_lo, CA_hi = weighted_log_interval(hA, N, False)
    ellC_lo, ellC_hi = log2_interval(Fraction(1,c))
    assert CA_lo == LA_lo and CA_hi == LA_hi

    cI, aI = Iv(c), Iv(a)
    BCI, BAI = Iv(BC), Iv(BA)
    LCI, LAI = Iv(LC_lo,LC_hi), Iv(LA_lo,LA_hi)
    CCI, CAI = Iv(CC_lo,CC_hi), Iv(CA_lo,CA_hi)
    ellC = Iv(ellC_lo,ellC_hi)
    ellA = Iv(8)

    IG = Iv(9*c+9*a)
    QG = Iv(9*c*c+9*a*a)
    EG = 9*cI*cI*ellC + Iv(9*a*a*8)
    AG = 9*LCI + 9*LAI

    x = -BCI/(cI*(1-cI))
    y = -(CCI - x*cI*cI*ellC)/(cI*(1-cI))
    numer = cI*(AG-x*EG-y*QG) - LCI + x*cI*cI*ellC + y*cI*cI
    R = -numer/(cI*(1-IG))
    z = AG-R*IG-x*EG-y*QG

    assert x.hi < 0
    assert y.hi < 0
    assert z.hi < 0
    assert R.hi < TARGET < Fraction(3,2)
    assert QG.hi < 1

    etaE = BAI + x*aI*(1-aI)
    etaQ = CAI - x*aI*aI*ellA + y*aI*(1-aI)
    eta0 = -LAI + R*aI + x*aI*aI*ellA + y*aI*aI + aI*z
    assert etaE.hi < 0
    assert etaQ.lo > 0
    residual_cap = etaQ*QG + eta0
    assert residual_cap.hi < 0

    etaEC = BCI + x*cI*(1-cI)
    etaQC = CCI - x*cI*cI*ellC + y*cI*(1-cI)
    eta0C = -LCI + R*cI + x*cI*cI*ellC + y*cI*cI + cI*z
    assert etaEC.lo <= 0 <= etaEC.hi
    assert etaQC.lo <= 0 <= etaQC.hi
    assert eta0C.lo <= 0 <= eta0C.hi

    print("seed_sha256", EXPECTED_SHA)
    print("c", c, "a", a, "BC", BC, "BA", BA, "Q_G", QG.lo)
    show_iv("x", x)
    show_iv("y", y)
    show_iv("R_star", R)
    show_iv("z", z)
    show_iv("eta_E_A", etaE)
    show_iv("eta_Q_A", etaQ)
    show_iv("eta_0_A", eta0)
    show_iv("A_residual_cap_at_QG", residual_cap)
    print("target", float(TARGET), "half", 1.5)
    print("PASS: full nonstationary Numaro recursive-tree Bellman barrier certified")

if __name__ == "__main__":
    main()
