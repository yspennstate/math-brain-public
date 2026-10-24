#!/usr/bin/env python3
"""Exact affine/gauge restriction-core certificate for the 10-input FEI gate.

This is a finite theorem about the explicit G10 inherited from account03/B12.
It reconstructs the exact 18-input source and G10, then exhausts every proper
coordinate restriction h of G10.  For every character chi_T that balances h
(hat h(T)=0), it computes the minimum possible ordinary influence after every
invertible F_2-linear input change by greedy minimum-weight vector-matroid
basis.  It proves the resulting balanced orbit has

    H/(I-1) <= R* = 46/5 - (9/5) log_2 3 < 6.35

whenever I>1.  Equality is classified by an exact normalized Walsh histogram.
It also proves the parent G10 itself is already influence-minimal over its
entire balanced affine/character orbit and keeps its certified violation of
the read-once cap C0=6.4548.

No floating-point quantity decides any asserted inequality.  Decimal output
is diagnostic only.  Standard library only.
"""
from fractions import Fraction
from collections import Counter
from functools import lru_cache
from itertools import combinations
import hashlib

EXPECTED_PARENT_SHA = "f8a7bb2c738d86368305111633376b1a3a83d8ee1f1abcc9a37d841b0f9c7839"
EXPECTED_G10_SHA = "3168d8fb8ac9f5d6d7dca1d79146392aecb5eb55cc76ccb028395a9e6a62bfb4"

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
FIXED_PARENT = {9:0, 10:0, 11:0, 12:1, 13:1, 14:0, 15:1, 16:1}
FREE_PARENT = [0,1,2,3,4,5,6,7,8,17]
C0 = Fraction(16137, 2500)  # 6.4548
RSTAR_FORM = "46/5-(9/5)log2(3)"
LOG_TERMS = 48

def sha_table(a):
    return hashlib.sha256(",".join(map(str, a)).encode()).hexdigest()

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
    assert sha_table(table) == EXPECTED_PARENT_SHA
    assert sum(table) == 0
    return table

def make_g10(parent):
    base = sum(v << i for i, v in FIXED_PARENT.items())
    out = []
    for z in range(1 << len(FREE_PARENT)):
        idx = base
        for j, i in enumerate(FREE_PARENT):
            idx |= ((z >> j) & 1) << i
        out.append(parent[idx])
    assert sha_table(out) == EXPECTED_G10_SHA
    assert sum(out) == 0
    return out

def fwht(a):
    a = list(a)
    h = 1
    while h < len(a):
        for s in range(0, len(a), 2*h):
            for j in range(s, s+h):
                x, y = a[j], a[j+h]
                a[j], a[j+h] = x+y, x-y
        h *= 2
    return a

def restrict10(table, free, fixed_bits):
    free = tuple(free)
    fixed = [i for i in range(10) if i not in free]
    base = 0
    for j, i in enumerate(fixed):
        base |= ((fixed_bits >> j) & 1) << i
    out = []
    for z in range(1 << len(free)):
        idx = base
        for j, i in enumerate(free):
            idx |= ((z >> j) & 1) << i
        out.append(table[idx])
    return out, fixed

def add_to_basis(basis, v):
    x = v
    while x:
        p = x.bit_length()-1
        if basis[p]:
            x ^= basis[p]
        else:
            basis[p] = x
            return True
    return False

def min_basis_cost_for_balance(W, T):
    """Min I(chi_T h after GL) exactly, conditional on W[T]=0."""
    N = len(W)
    n = N.bit_length()-1
    sq = [w*w for w in W]
    corr = fwht(sq)  # denominator N^2
    weights = []
    for u in range(1, N):
        sign = -1 if ((T & u).bit_count() & 1) else 1
        # q_T(u)=(1-(-1)^{T.u} c_h(u))/2
        weights.append((N*N - sign*corr[u], u))
    weights.sort()
    basis = [0]*n
    total = 0
    rank = 0
    for w, u in weights:
        if add_to_basis(basis, u):
            total += w
            rank += 1
            if rank == n:
                break
    assert rank == n
    return Fraction(total, 2*N*N)

def min_balanced_affine_influence(W):
    zeros = [T for T,w in enumerate(W) if w == 0]
    if not zeros:
        return None, None, 0
    best = None
    bestT = None
    for T in zeros:
        val = min_basis_cost_for_balance(W, T)
        if best is None or val < best:
            best, bestT = val, T
    return best, bestT, len(zeros)

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

@lru_cache(maxsize=None)
def ln_unit(y):
    assert 1 <= y <= 2
    z = (y-1)/(y+1)
    if z == 0:
        return Fraction(0), Fraction(0)
    z2 = z*z
    zp = z
    s = Fraction(0)
    for j in range(LOG_TERMS):
        if j:
            zp *= z2
        s += zp/(2*j+1)
    lo = 2*s
    rem = 2*z**(2*LOG_TERMS+1)/((2*LOG_TERMS+1)*(1-z2))
    return lo, lo+rem

@lru_cache(maxsize=None)
def log2_interval(x):
    k, y = normalize_pow2(x)
    ylo, yhi = ln_unit(y)
    l2lo, l2hi = ln_unit(Fraction(2))
    return Fraction(k) + ylo/l2hi, Fraction(k) + yhi/l2lo

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
    return lo, hi

def normalized_hist(W):
    N = len(W)
    return Counter(Fraction(abs(w), N) for w in W if w)

EQ_HIST = Counter({
    Fraction(1,16): 32,
    Fraction(1,8): 4,
    Fraction(1,4): 4,
    Fraction(3,8): 4,
})

def dec_lo(x, digits=15):
    scale = 10**digits
    q = x.numerator*scale // x.denominator
    return f"{q//scale}.{q%scale:0{digits}d}"

def dec_hi(x, digits=15):
    scale = 10**digits
    q = (x.numerator*scale + x.denominator-1)//x.denominator
    return f"{q//scale}.{q%scale:0{digits}d}"

def main():
    parent = reconstruct_parent()
    g10 = make_g10(parent)

    # Exact interval for R*.
    l3lo, l3hi = log2_interval(Fraction(3))
    Rlo = Fraction(46,5) - Fraction(9,5)*l3hi
    Rhi = Fraction(46,5) - Fraction(9,5)*l3lo

    # Elementary strict comparison R* < 6.35 < C0:
    # 3^12 > 2^19 => log2 3 > 19/12.
    assert 3**12 > 2**19
    assert Fraction(46,5) - Fraction(9,5)*Fraction(19,12) == Fraction(127,20)
    assert Fraction(127,20) < C0

    # Parent: search all output characters that preserve balance and all GL bases.
    Wp = fwht(g10)
    Ip, Tp, parent_zero_gauges = min_balanced_affine_influence(Wp)
    assert Ip == Fraction(257,128)
    assert Tp == 0
    parent_min_ties = [
        T for T,w in enumerate(Wp)
        if w == 0 and min_basis_cost_for_balance(Wp, T) == Ip
    ]
    assert parent_min_ties == [0]
    Hplo, Hphi = entropy_interval(Wp)
    # rigorous read-once-cap violation at uniform balanced bias
    assert Hplo > (Ip-1)*C0
    parent_Rlo = Hplo/(Ip-1)

    total_restrictions = 0
    balance_capable = 0
    zero_gauges = 0
    character_nodes = 0
    strict_checks = 0
    equality_nodes = 0
    equality_by_dim = Counter()
    balance_nodes_by_dim = Counter()
    best_diag = {}

    for m in range(1,10):
        best_upper = None
        best_record = None
        for free in combinations(range(10), m):
            fixed = [i for i in range(10) if i not in free]
            for a in range(1 << len(fixed)):
                total_restrictions += 1
                h, _ = restrict10(g10, free, a)
                W = fwht(h)
                Imin, Tmin, nz = min_balanced_affine_influence(W)
                if Imin is None:
                    continue
                balance_capable += 1
                zero_gauges += nz
                balance_nodes_by_dim[m] += 1
                assert Imin >= 1  # Poincare, checked arithmetically here.
                Hlo, Hhi = entropy_interval(W)
                if Imin == 1:
                    character_nodes += 1
                    assert Hhi == 0
                    continue

                nh = normalized_hist(W)
                is_eq = (Imin == Fraction(13,8) and nh == EQ_HIST)
                if is_eq:
                    equality_nodes += 1
                    equality_by_dim[m] += 1
                    # Exact entropy from the normalized histogram:
                    # H=23/4-(9/8)log2 3, so H/(5/8)=R*.
                    # The exact normalized histogram itself proves this identity.
                    ratio_hi = Rhi
                else:
                    strict_checks += 1
                    # Rigorous strict inequality H/(Imin-1) < R*.
                    assert Hhi < (Imin-1)*Rlo
                    ratio_hi = Hhi/(Imin-1)

                if best_upper is None or ratio_hi > best_upper:
                    best_upper = ratio_hi
                    best_record = (tuple(free), a, Imin, Tmin, sha_table(h), nh)

        if best_record is not None:
            best_diag[m] = {
                "ratio_upper": dec_hi(best_upper, 15),
                "free": best_record[0],
                "fixed_assignment_integer": best_record[1],
                "Imin": str(best_record[2]),
                "balancing_character": best_record[3],
                "table_sha256": best_record[4],
            }

    assert total_restrictions == 58024
    assert balance_capable == 50546
    assert zero_gauges == 626208
    assert character_nodes == 30992
    assert equality_nodes == 28
    assert equality_by_dim == Counter({6:20, 7:8})
    assert strict_checks == balance_capable - character_nodes - equality_nodes

    # A canonical equality descendant.
    h6, fixed6 = restrict10(g10, (0,1,2,3,4,5), 2)
    W6 = fwht(h6)
    I6, T6, _ = min_balanced_affine_influence(W6)
    assert I6 == Fraction(13,8) and T6 == 0
    assert normalized_hist(W6) == EQ_HIST
    assert sha_table(h6) == "0a2bea73d6d57e71efb6a5058257f54cb8a21a51f53d41ef062af85899372be5"
    assert fixed6 == [6,7,8,9]
    # assignment 2 means x6=0,x7=1,x8=0,x9=0 in G10-local coordinates.
    assert [(fixed6[j], (2>>j)&1) for j in range(4)] == [(6,0),(7,1),(8,0),(9,0)]

    print("PASS")
    print("parent_g10_sha256", EXPECTED_G10_SHA)
    print("parent_balanced_affine_min_I", Ip)
    print("parent_unique_best_balancing_character", Tp)
    print("parent_minimizer_count", len(parent_min_ties))
    print("parent_balancing_character_count", parent_zero_gauges)
    print("parent_R_lower", dec_lo(parent_Rlo, 18))
    print("C0", dec_lo(C0, 4))
    print("proper_restrictions", total_restrictions)
    print("balance_capable_restrictions", balance_capable)
    print("balancing_character_gauges", zero_gauges)
    print("character_orbit_nodes_Ieq1", character_nodes)
    print("strict_Rstar_checks", strict_checks)
    print("Rstar_equality_nodes", equality_nodes)
    print("Rstar_equality_by_dimension", dict(sorted(equality_by_dim.items())))
    print("Rstar_formula", RSTAR_FORM)
    print("Rstar_interval", dec_lo(Rlo,18), dec_hi(Rhi,18))
    print("Rstar_lt_6.35_via", "3^12>2^19")
    print("canonical_equality_free", (0,1,2,3,4,5))
    print("canonical_equality_fixed", [(6,0),(7,1),(8,0),(9,0)])
    print("canonical_equality_sha256", sha_table(h6))
    print("canonical_equality_Imin", I6)
    print("best_diagnostics", best_diag)
    print("full_FEI", "OPEN_NOT_PROVED")

if __name__ == "__main__":
    main()
