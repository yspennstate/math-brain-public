"""Exact certificate for account03/B16's adaptive two-step FEI gate calculation.

This reconstructs the source-exact 18-input balanced Numaro gate inherited
from the arity-10 certificate, verifies its truth-table digest, and checks
the Poincare-currency restriction ledger of account02/B16's Theorem 3.1.
It proves only the finite source-gate statement in the adjacent REPORT.md;
it does not prove FEI.
"""
from fractions import Fraction
from collections import Counter
import hashlib

EXPECTED_PARENT_SHA = "f8a7bb2c738d86368305111633376b1a3a83d8ee1f1abcc9a37d841b0f9c7839"
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
NVAR = 18
LOG_TERMS = 50
POLICY = {
    9:(4,1), 10:(1,0), 11:(0,2), 12:(0,1), 13:(3,0),
    14:(0,1), 15:(0,2), 16:(3,0), 17:(1,0),
}

def reconstruct_parent():
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
    assert digest == EXPECTED_PARENT_SHA
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

def pow2(k):
    return Fraction(1 << k, 1) if k >= 0 else Fraction(1, 1 << (-k))

def normalize_pow2(x):
    k = x.numerator.bit_length() - x.denominator.bit_length()
    while x < pow2(k):
        k -= 1
    while x >= pow2(k+1):
        k += 1
    return k, x / pow2(k)

def ln_interval_unit(y):
    assert 1 <= y <= 2
    z = (y-1)/(y+1)
    if z == 0:
        return Fraction(0), Fraction(0)
    z2 = z*z
    zp = z
    partial = Fraction(0)
    for j in range(LOG_TERMS):
        if j:
            zp *= z2
        partial += zp/(2*j+1)
    lo = 2*partial
    rem = 2*z**(2*LOG_TERMS+1)/((2*LOG_TERMS+1)*(1-z2))
    return lo, lo+rem

LN2_LO, LN2_HI = ln_interval_unit(Fraction(2))

def log2_interval(x):
    k, y = normalize_pow2(x)
    lo, hi = ln_interval_unit(y)
    return Fraction(k) + lo/LN2_HI, Fraction(k) + hi/LN2_LO

def entropy_interval(coeffs, dimension):
    size = 1 << dimension
    hist = Counter(abs(x) for x in coeffs if x)
    lo = Fraction(0)
    hi = Fraction(0)
    for a, count in hist.items():
        p = Fraction(a*a, size*size)
        llo, lhi = log2_interval(1/p)
        lo += count*p*llo
        hi += count*p*lhi
    return lo, hi

def restricted_coefficients(root_w, fixed):
    fitems = sorted(fixed.items())
    fmask = sum(1 << i for i, _ in fitems)
    div = 1 << len(fitems)
    out = []
    for base in range(1 << NVAR):
        if base & fmask:
            continue
        s = 0
        for a in range(1 << len(fitems)):
            mask = base
            sign = 1
            for q, (i, b) in enumerate(fitems):
                if (a >> q) & 1:
                    mask |= 1 << i
                    if b:
                        sign = -sign
            s += sign * root_w[mask]
        assert s % div == 0
        out.append((s // div, base))
    return out

CACHE = {}
def stats(root_w, fixed):
    key = tuple(sorted(fixed.items()))
    if key in CACHE:
        return CACHE[key]
    pairs = restricted_coefficients(root_w, fixed)
    dimension = NVAR - len(fixed)
    size = 1 << dimension
    den2 = size*size
    coeffs = [w for w, _ in pairs]
    H = entropy_interval(coeffs, dimension)
    I = sum(Fraction(mask.bit_count()*w*w, den2) for w, mask in pairs)
    mean = Fraction(pairs[0][0], size)
    pout = (1-mean)/2
    P = I/4 - pout*(1-pout)
    CACHE[key] = (H, I, pout, P)
    return CACHE[key]

def interval_sub(A, B):
    return A[0]-B[1], A[1]-B[0]

def one_step(root_w, rootH, rootP, i):
    ch = [stats(root_w, {i:b}) for b in (0,1)]
    EH = (sum(x[0][0] for x in ch)/2, sum(x[0][1] for x in ch)/2)
    EP = sum(x[3] for x in ch)/2
    return interval_sub(rootH, EH), rootP-EP

def two_step(root_w, rootH, rootP, i, j0, j1):
    ch = []
    for b, j in ((0,j0),(1,j1)):
        for c in (0,1):
            ch.append(stats(root_w, {i:b, j:c}))
    EH = (sum(x[0][0] for x in ch)/4, sum(x[0][1] for x in ch)/4)
    EP = sum(x[3] for x in ch)/4
    return interval_sub(rootH, EH), rootP-EP

def branch_second(root_w, i, b, j):
    parent = stats(root_w, {i:b})
    kids = [stats(root_w, {i:b,j:c}) for c in (0,1)]
    EH = (sum(x[0][0] for x in kids)/2, sum(x[0][1] for x in kids)/2)
    EP = sum(x[3] for x in kids)/2
    return interval_sub(parent[0], EH), parent[3]-EP

def decimal_bounds(interval, digits=18):
    scale = 10**digits
    lo = interval[0].numerator*scale // interval[0].denominator
    hi = (interval[1].numerator*scale + interval[1].denominator - 1)//interval[1].denominator
    def fmt(q):
        return f"{q//scale}.{q%scale:0{digits}d}"
    return fmt(lo), fmt(hi)

def ratio_interval(L, Q):
    return L[0]/(4*Q), L[1]/(4*Q)

def main():
    table = reconstruct_parent()
    root_w = fwht_int(table)
    rootH, rootI, rootp, rootP = stats(root_w, {})
    assert rootp == Fraction(1,2)
    assert rootI == Fraction(261,128)
    assert rootP == Fraction(133,512)

    core_rows = []
    for i in range(9):
        L,Q = one_step(root_w,rootH,rootP,i)
        assert Q == Fraction(11343,262144)
        r = ratio_interval(L,Q)
        assert r[1] < Fraction(5889,1000)
        core_rows.append((i,L,Q,r))
    assert all(x[1] == core_rows[0][1] and x[2] == core_rows[0][2] for x in core_rows)

    host_first = []
    host_blocks = []
    for i in range(9,18):
        L1,Q1 = one_step(root_w,rootH,rootP,i)
        assert Q1 == Fraction(255,262144)
        r1 = ratio_interval(L1,Q1)
        assert r1[0] > Fraction(8,1)
        host_first.append((i,L1,Q1,r1))

        j0,j1 = POLICY[i]
        L2,Q2 = two_step(root_w,rootH,rootP,i,j0,j1)
        assert Q2 == Fraction(11739,262144)
        r2 = ratio_interval(L2,Q2)
        assert r2[1] < Fraction(5889,1000)
        host_blocks.append((i,j0,j1,L2,Q2,r2))

        for b,j in ((0,j0),(1,j1)):
            Lb,Qb = branch_second(root_w,i,b,j)
            assert Qb == Fraction(2871,65536)
            rb = ratio_interval(Lb,Qb)
            assert rb[1] < Fraction(5832,1000)

    print("PASS")
    print("parent_sha256", EXPECTED_PARENT_SHA)
    print("root_I", rootI, "root_P", rootP)
    print("root_H", decimal_bounds(rootH))
    i,L,Q,r = core_rows[0]
    print("core_coordinates", list(range(9)))
    print("core_Q", Q, "core_L", decimal_bounds(L), "core_rho", decimal_bounds(r))
    i,L,Q,r = host_first[0]
    print("host_coordinates", list(range(9,18)))
    print("host_first_Q", Q, "host_first_L", decimal_bounds(L), "host_first_rho", decimal_bounds(r))
    print("adaptive_policy", POLICY)
    i,j0,j1,L,Q,r = host_blocks[0]
    print("host_two_step_Q", Q, "host_two_step_L", decimal_bounds(L), "host_two_step_rho", decimal_bounds(r))
    Lb,Qb = branch_second(root_w,9,0,4)
    rb = ratio_interval(Lb,Qb)
    print("representative_second_Q", Qb, "second_L", decimal_bounds(Lb), "second_rho", decimal_bounds(rb))
    print("finite_source_gate_statement", "every first coordinate has an explicit restriction block of depth <=2 with rho_sigma<5.889")
    print("full_FEI", "OPEN_NOT_PROVED")

if __name__ == "__main__":
    main()
