"""Exact exhaustive certificate: the 10-input FEI gate obstruction is balanced-restriction-minimal.

Reconstructs the certified 10-input monotone balanced gate from the source-exact
18-input Numaro seed, then enumerates all 3^10 coordinate restrictions. For
every proper balanced non-affine restriction it proves, with rational logarithm
intervals, H/(I-1) < C0=6.4548. Thus the positive balanced gate-margin
obstruction at the root does not persist to any proper balanced subcube.
This is a statement about the read-once base potential, not a proof/disproof of FEI.
"""
from fractions import Fraction
from collections import Counter
from functools import lru_cache
import hashlib
import itertools

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
EXPECTED_PARENT_SHA = "f8a7bb2c738d86368305111633376b1a3a83d8ee1f1abcc9a37d841b0f9c7839"
EXPECTED_ROOT_SHA = "3168d8fb8ac9f5d6d7dca1d79146392aecb5eb55cc76ccb028395a9e6a62bfb4"
FIXED_PARENT = {9:0, 10:0, 11:0, 12:1, 13:1, 14:0, 15:1, 16:1}
FREE_PARENT = [0,1,2,3,4,5,6,7,8,17]
C0 = Fraction(16137, 2500)
LOG_TERMS = 30

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

def root_gate(parent):
    base = sum(v << i for i, v in FIXED_PARENT.items())
    out = []
    for z in range(1 << len(FREE_PARENT)):
        idx = base
        for j, i in enumerate(FREE_PARENT):
            idx |= ((z >> j) & 1) << i
        out.append(parent[idx])
    digest = hashlib.sha256(",".join(map(str, out)).encode()).hexdigest()
    assert digest == EXPECTED_ROOT_SHA
    assert sum(out) == 0
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

def total_influence(table):
    n = len(table).bit_length() - 1
    den = 1 << (n-1)
    total = Fraction(0)
    for i in range(n):
        bit = 1 << i
        edges = sum(table[x] != table[x|bit] for x in range(len(table)) if not (x & bit))
        total += Fraction(edges, den)
    return total

def influence_vector(table):
    n = len(table).bit_length() - 1
    den = 1 << (n-1)
    ans = []
    for i in range(n):
        bit = 1 << i
        edges = sum(table[x] != table[x|bit] for x in range(len(table)) if not (x & bit))
        ans.append(Fraction(edges, den))
    return ans

def pow2(k):
    return Fraction(1 << k, 1) if k >= 0 else Fraction(1, 1 << (-k))

def normalize_pow2(x):
    k = x.numerator.bit_length() - x.denominator.bit_length()
    while x < pow2(k):
        k -= 1
    while x >= pow2(k+1):
        k += 1
    y = x / pow2(k)
    assert 1 <= y < 2
    return k, y

def ln_interval_unit(y):
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
    rem = 2*z**(2*LOG_TERMS+1) / ((2*LOG_TERMS+1)*(1-z2))
    return lo, lo+rem

LN2_LO, LN2_HI = ln_interval_unit(Fraction(2))

@lru_cache(maxsize=None)
def log2_invprob_interval(a, N):
    p = Fraction(a*a, N*N)
    k, y = normalize_pow2(1/p)
    lo, hi = ln_interval_unit(y)
    return Fraction(k) + lo/LN2_HI, Fraction(k) + hi/LN2_LO

def entropy_interval(table):
    W = fwht_int(table)
    N = len(W)
    hist = Counter(abs(x) for x in W if x)
    lo = Fraction(0)
    hi = Fraction(0)
    for a, count in hist.items():
        p = Fraction(a*a, N*N)
        llo, lhi = log2_invprob_interval(a, N)
        lo += count*p*llo
        hi += count*p*lhi
    return lo, hi, hist

def decimal_lower(x, digits=18):
    scale = 10**digits
    q = x.numerator * scale // x.denominator
    sign = "-" if q < 0 else ""
    q = abs(q)
    return f"{sign}{q//scale}.{q%scale:0{digits}d}"

def decimal_upper(x, digits=18):
    scale = 10**digits
    q = -((-x.numerator * scale) // x.denominator)
    sign = "-" if q < 0 else ""
    q = abs(q)
    return f"{sign}{q//scale}.{q%scale:0{digits}d}"

def restricted_table(root, state):
    frees = [i for i,s in enumerate(state) if s == -1]
    fixed_idx = sum(s << i for i,s in enumerate(state) if s != -1)
    out = []
    for z in range(1 << len(frees)):
        idx = fixed_idx
        for j, i in enumerate(frees):
            idx |= ((z >> j) & 1) << i
        out.append(root[idx])
    return frees, out

def main():
    root = root_gate(reconstruct_parent())
    root_I = total_influence(root)
    assert root_I == Fraction(257,128)
    root_H_lo, root_H_hi, _ = entropy_interval(root)
    root_ratio_lo = root_H_lo/(root_I-1)
    root_c_lo = 4*(root_ratio_lo-C0)
    assert root_c_lo > Fraction(1,100)

    balanced_total = 0
    balanced_nonaffine = 0
    balanced_by_free_arity = Counter()
    nonaffine_by_free_arity = Counter()
    max_ratio_hi = None
    max_record = None

    for state in itertools.product((-1,0,1), repeat=10):
        if all(s == -1 for s in state):
            continue
        frees, table = restricted_table(root, state)
        if not frees or sum(table) != 0:
            continue
        balanced_total += 1
        balanced_by_free_arity[len(frees)] += 1
        I = total_influence(table)
        if I <= 1:
            continue
        balanced_nonaffine += 1
        nonaffine_by_free_arity[len(frees)] += 1
        H_lo, H_hi, hist = entropy_interval(table)
        assert H_hi < C0*(I-1), (state, H_hi, I)
        ratio_hi = H_hi/(I-1)
        if max_ratio_hi is None or ratio_hi > max_ratio_hi:
            max_ratio_hi = ratio_hi
            max_record = (state, frees, table, I, H_lo, H_hi, hist)

    assert balanced_by_free_arity[9] == 0
    assert balanced_by_free_arity[8] == 0
    assert balanced_total == 9514
    assert balanced_nonaffine == 460

    state, frees, table, I, H_lo, H_hi, hist = max_record
    assert len(frees) == 7
    assert I == Fraction(13,8)
    infs = influence_vector(table)
    assert sum(x > 0 for x in infs) == 6
    max_sha = hashlib.sha256(",".join(map(str, table)).encode()).hexdigest()

    print("PASS")
    print("root_sha256", EXPECTED_ROOT_SHA)
    print("root_I", str(root_I))
    print("root_H_lower", decimal_lower(root_H_lo))
    print("root_H_upper", decimal_upper(root_H_hi))
    print("root_H_over_I_minus_1_lower", decimal_lower(root_ratio_lo))
    print("root_c_G_lower", decimal_lower(root_c_lo))
    print("proper_balanced_restrictions", balanced_total)
    print("proper_balanced_nonaffine_restrictions", balanced_nonaffine)
    print("balanced_by_free_arity", dict(sorted(balanced_by_free_arity.items())))
    print("nonaffine_by_free_arity", dict(sorted(nonaffine_by_free_arity.items())))
    print("no_balanced_codim1_or_codim2", True)
    print("max_state_free0_fixed01", state)
    print("max_free_coordinates", frees)
    print("max_restriction_sha256", max_sha)
    print("max_I", str(I))
    print("max_essential_coordinates", sum(x > 0 for x in infs))
    print("max_influence_vector", [str(x) for x in infs])
    print("max_H_lower", decimal_lower(H_lo))
    print("max_H_upper", decimal_upper(H_hi))
    print("max_H_over_I_minus_1_upper", decimal_upper(max_ratio_hi))
    print("C0", "6.454800000000000000")
    print("proper_balanced_gate_margin_upper",
          decimal_upper(4*(max_ratio_hi-C0)))
    print("full_FEI", "OPEN_NOT_PROVED")

if __name__ == "__main__":
    main()
