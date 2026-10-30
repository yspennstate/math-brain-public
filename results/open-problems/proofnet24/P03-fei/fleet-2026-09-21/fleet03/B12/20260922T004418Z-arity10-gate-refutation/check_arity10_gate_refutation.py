"""Exact certificate for a 10-input balanced monotone FEI gate-margin obstruction.

Reconstructs the source-exact 18-variable Numaro seed from the inherited
certificate, takes an explicit 10-variable coordinate restriction, verifies
the restricted truth-table hash, balance, monotonicity, essentiality and
non-read-once root structure, then proves with rational log enclosures that
its balanced-uniform gate margin exceeds the current two-input AND margin.

This refutes AND-extremality for the current read-once Gamma candidate.
It does NOT prove or disprove full FEI.
"""
from fractions import Fraction
from collections import Counter
import hashlib

EXPECTED_PARENT_SHA = "f8a7bb2c738d86368305111633376b1a3a83d8ee1f1abcc9a37d841b0f9c7839"
EXPECTED_WITNESS_SHA = "3168d8fb8ac9f5d6d7dca1d79146392aecb5eb55cc76ccb028395a9e6a62bfb4"

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

# Parent coordinates 9..16 are fixed; 0..8 and 17 remain live.
FIXED = {9:0, 10:0, 11:0, 12:1, 13:1, 14:0, 15:1, 16:1}
FREE = [0,1,2,3,4,5,6,7,8,17]
C0 = Fraction(16137, 2500)              # 6.4548
AND_MARGIN = Fraction(43974201, 10**10) # 0.0043974201
LOG_TERMS = 40

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

def restrict_parent(parent):
    out = []
    base = sum(v << i for i, v in FIXED.items())
    for z in range(1 << len(FREE)):
        idx = base
        for j, i in enumerate(FREE):
            idx |= ((z >> j) & 1) << i
        out.append(parent[idx])
    return out

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

def influences(table):
    n = len(table).bit_length() - 1
    den = 1 << (n-1)
    out = []
    for i in range(n):
        bit = 1 << i
        edges = sum(table[x] != table[x|bit] for x in range(len(table)) if not (x & bit))
        out.append(Fraction(edges, den))
    return out

def check_monotone(table):
    # Truth is encoded by -1, hence monotone increasing truth means numerical
    # values can only move +1 -> -1 as an input bit changes 0 -> 1.
    n = len(table).bit_length() - 1
    for i in range(n):
        bit = 1 << i
        for x in range(len(table)):
            if not (x & bit):
                assert table[x] >= table[x|bit]

def rectangle_test(table, A_mask, target):
    """Whether target-valued cells form U x V for this bipartition."""
    n = len(table).bit_length() - 1
    A = [i for i in range(n) if (A_mask >> i) & 1]
    B = [i for i in range(n) if not ((A_mask >> i) & 1)]
    patterns = set()
    for aa in range(1 << len(A)):
        row = 0
        for bb in range(1 << len(B)):
            idx = 0
            for j, i in enumerate(A):
                idx |= ((aa >> j) & 1) << i
            for j, i in enumerate(B):
                idx |= ((bb >> j) & 1) << i
            if table[idx] == target:
                row |= 1 << bb
        if row:
            patterns.add(row)
            if len(patterns) > 1:
                return False
    return True

def check_no_monotone_readonce_root(table):
    n = len(table).bit_length() - 1
    FULL = (1 << n) - 1
    # Every nontrivial read-once monotone AND/OR formula has a root partition.
    # AND => true(-1) cells form a rectangle; OR => false(+1) cells do.
    for mask in range(1, FULL):
        if not (mask & 1):  # quotient by A/B symmetry
            continue
        assert not rectangle_test(table, mask, -1)
        assert not rectangle_test(table, mask, +1)

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
    # ln y = 2*sum_{j>=0} z^(2j+1)/(2j+1), z=(y-1)/(y+1).
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
    rem = 2*z**(2*terms+1) / ((2*terms+1)*(1-z2))
    return lo, lo+rem

def log2_interval(x):
    k, y = normalize_pow2(x)
    ly_lo, ly_hi = ln_interval_unit(y)
    l2_lo, l2_hi = ln_interval_unit(Fraction(2))
    return Fraction(k) + ly_lo/l2_hi, Fraction(k) + ly_hi/l2_lo

def entropy_interval(W):
    N = len(W)
    hist = Counter(abs(w) for w in W if w)
    lo = Fraction(0)
    hi = Fraction(0)
    for a, count in hist.items():
        p = Fraction(a*a, N*N)
        llo, lhi = log2_interval(1/p)
        lo += count*p*llo
        hi += count*p*lhi
    return lo, hi, hist

def decimal_lower(x, digits=18):
    assert x >= 0
    scale = 10**digits
    q = x.numerator * scale // x.denominator
    return f"{q//scale}.{q%scale:0{digits}d}"

def decimal_upper(x, digits=18):
    assert x >= 0
    scale = 10**digits
    q = (x.numerator * scale + x.denominator - 1)//x.denominator
    return f"{q//scale}.{q%scale:0{digits}d}"

def main():
    parent = reconstruct_parent()
    witness = restrict_parent(parent)
    witness_sha = hashlib.sha256(",".join(map(str, witness)).encode()).hexdigest()
    assert witness_sha == EXPECTED_WITNESS_SHA
    assert len(witness) == 1024
    assert sum(witness) == 0
    check_monotone(witness)

    infs = influences(witness)
    assert infs == [
        Fraction(29,128), Fraction(29,128), Fraction(29,128),
        Fraction(29,128), Fraction(29,128), Fraction(29,128),
        Fraction(49,256), Fraction(29,128), Fraction(29,128),
        Fraction(1,256)
    ]
    assert all(x > 0 for x in infs)
    I = sum(infs, Fraction(0))
    assert I == Fraction(257,128)

    # Essential + monotone + no root AND/OR split => not a read-once
    # AND/OR/NOT gate: an essential monotone read-once representation can be
    # De-Morganized to a monotone read-once AND/OR representation.
    check_no_monotone_readonce_root(witness)

    W = fwht_int(witness)
    assert sum(w*w for w in W) == len(witness)**2
    H_lo, H_hi, hist = entropy_interval(W)
    expected_hist = {
        4:337, 8:48, 12:108, 16:28, 24:32, 28:18, 32:34, 36:36,
        40:24, 48:8, 56:8, 72:8, 80:16, 84:12, 96:8, 112:4,
        196:1, 232:8
    }
    assert dict(sorted(hist.items())) == expected_hist

    # Balanced-uniform identity from the consumed peer theorem:
    # c_G = 4 * ( H/(I-1) - C0 ).
    threshold_H = (I-1) * (C0 + AND_MARGIN/4)
    assert H_lo > threshold_H
    ratio_lo = H_lo/(I-1)
    c_lo = 4*(ratio_lo-C0)
    assert c_lo > AND_MARGIN

    print("PASS")
    print("parent_sha256", EXPECTED_PARENT_SHA)
    print("fixed_parent_coordinates", sorted(FIXED.items()))
    print("free_parent_coordinates", FREE)
    print("witness_sha256", EXPECTED_WITNESS_SHA)
    print("balanced", True, "monotone", True, "essential_inputs", 10)
    print("non_readonce_root_certificate", "all 511 canonical nontrivial bipartitions reject AND and OR factorization")
    print("influences", [str(x) for x in infs])
    print("I", str(I))
    print("H_lower", decimal_lower(H_lo, 18))
    print("H_upper", decimal_upper(H_hi, 18))
    print("H_over_I_minus_1_lower", decimal_lower(ratio_lo, 18))
    print("c_G_lower", decimal_lower(c_lo, 18))
    print("and_margin", "0.0043974201")
    print("c_G_over_and_margin_lower", decimal_lower(c_lo/AND_MARGIN, 18))
    print("entropy_excess_over_and_threshold_lower", decimal_lower(H_lo-threshold_H, 18))
    print("full_FEI", "OPEN_NOT_PROVED")

if __name__ == "__main__":
    main()
