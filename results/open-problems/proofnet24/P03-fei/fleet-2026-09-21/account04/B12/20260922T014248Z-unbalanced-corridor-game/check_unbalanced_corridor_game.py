"""Exact finite certificate for the account04/B12 unbalanced-corridor theorem.

Reconstructs the source-exact arity-10 balanced monotone FEI gate witness,
checks a fixed physical coordinate reveal order, solves the adaptive
first-balanced-return game over all 3^10 restriction states, and certifies
the one-step entropy/Poincare ratios along the fixed corridor by rational
logarithm intervals.

This is a finite theorem about one explicit Boolean gate.  It does not prove FEI.
"""
from fractions import Fraction
from functools import lru_cache
from collections import Counter
import hashlib

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
FIXED = {9:0, 10:0, 11:0, 12:1, 13:1, 14:0, 15:1, 16:1}
FREE = [0,1,2,3,4,5,6,7,8,17]
N = 10
FULL = (1 << N) - 1
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
    return table

def restrict_parent(parent):
    out = []
    base = sum(v << i for i, v in FIXED.items())
    for z in range(1 << len(FREE)):
        idx = base
        for j, i in enumerate(FREE):
            idx |= ((z >> j) & 1) << i
        out.append(parent[idx])
    return tuple(out)

PARENT = reconstruct_parent()
WITNESS = restrict_parent(PARENT)
assert hashlib.sha256(",".join(map(str, WITNESS)).encode()).hexdigest() == EXPECTED_WITNESS_SHA
assert sum(WITNESS) == 0

@lru_cache(None)
def subtable(mask, val):
    free = tuple(i for i in range(N) if not ((mask >> i) & 1))
    arr = []
    for z in range(1 << len(free)):
        idx = val
        for j, i in enumerate(free):
            idx |= ((z >> j) & 1) << i
        arr.append(WITNESS[idx])
    return tuple(arr), free

@lru_cache(None)
def state_stats(mask, val):
    arr, free = subtable(mask, val)
    m = len(arr)
    neg = sum(x == -1 for x in arr)
    q = Fraction(neg, m)
    I = Fraction(0)
    for j in range(len(free)):
        bit = 1 << j
        edges = sum(arr[x] != arr[x | bit] for x in range(m) if not (x & bit))
        I += Fraction(edges, m // 2)
    P = I / 4 - q * (1 - q)
    assert P >= 0
    return q, I, P, (2 * neg == m)

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
    rem = 2*z**(2*terms+1) / ((2*terms+1)*(1-z2))
    return lo, lo+rem

def log2_interval(x):
    k, y = normalize_pow2(x)
    ly_lo, ly_hi = ln_interval_unit(y)
    l2_lo, l2_hi = ln_interval_unit(Fraction(2))
    return Fraction(k) + ly_lo/l2_hi, Fraction(k) + ly_hi/l2_lo

@lru_cache(None)
def entropy_interval(mask, val):
    arr, _ = subtable(mask, val)
    W = fwht_int(arr)
    N0 = len(W)
    hist = Counter(abs(w) for w in W if w)
    lo = Fraction(0)
    hi = Fraction(0)
    for a, count in hist.items():
        p = Fraction(a*a, N0*N0)
        llo, lhi = log2_interval(1/p)
        lo += count*p*llo
        hi += count*p*lhi
    return lo, hi

def dec_lower(x, digits=15):
    scale = 10**digits
    q = x.numerator * scale // x.denominator
    return f"{q//scale}.{q%scale:0{digits}d}"

def dec_upper(x, digits=15):
    scale = 10**digits
    q = (x.numerator * scale + x.denominator - 1) // x.denominator
    return f"{q//scale}.{q%scale:0{digits}d}"

# Game terminal: first proper balanced NONAFFINE restriction.  Affine states carry P=0.
@lru_cache(None)
def hit_prob_extrema(mask, val):
    q, I, P, bal = state_stats(mask, val)
    if mask and bal and P > 0:
        return Fraction(1), Fraction(1)
    if P == 0 or mask == FULL:
        return Fraction(0), Fraction(0)
    rows = []
    for i in range(N):
        if not ((mask >> i) & 1):
            nm = mask | (1 << i)
            mn0, mx0 = hit_prob_extrema(nm, val)
            mn1, mx1 = hit_prob_extrema(nm, val | (1 << i))
            rows.append(((mn0+mn1)/2, (mx0+mx1)/2))
    return min(a for a,b in rows), max(b for a,b in rows)

@lru_cache(None)
def terminal_P_extrema(mask, val):
    q, I, P, bal = state_stats(mask, val)
    if mask and bal and P > 0:
        return P, P
    if P == 0 or mask == FULL:
        return Fraction(0), Fraction(0)
    rows = []
    for i in range(N):
        if not ((mask >> i) & 1):
            nm = mask | (1 << i)
            mn0, mx0 = terminal_P_extrema(nm, val)
            mn1, mx1 = terminal_P_extrema(nm, val | (1 << i))
            rows.append(((mn0+mn1)/2, (mx0+mx1)/2))
    return min(a for a,b in rows), max(b for a,b in rows)

def main():
    q0, I0, P0, bal0 = state_stats(0,0)
    assert bal0 and I0 == Fraction(257,128) and P0 == Fraction(129,512)

    # Fixed reveal order 0,1,...,9: no proper nonaffine balanced node occurs.
    prefix_summary = []
    for t in range(1, N+1):
        mask = (1 << t) - 1
        nonaff_bal = aff_bal = unbal = 0
        for val in range(1 << t):
            q, I, P, bal = state_stats(mask, val)
            if bal and P > 0:
                nonaff_bal += 1
            elif bal:
                aff_bal += 1
            else:
                unbal += 1
        assert nonaff_bal == 0
        prefix_summary.append((t, nonaff_bal, aff_bal, unbal))

    # Exact adaptive game over all restriction states.
    min_hit, max_hit = hit_prob_extrema(0,0)
    min_tP, max_tP = terminal_P_extrema(0,0)
    assert min_hit == 0
    assert max_hit == Fraction(19,32)
    assert min_tP == 0
    assert max_tP == Fraction(47,512)

    # Along the fixed order, certify every positive-Q one-step entropy/P ratio <=32.
    # The inherited exact martingale then says their Q-weighted average is H(root)/P(root).
    positive_Q_states = 0
    exact_32_states = 0
    exact_32_Qmass = Fraction(0)
    for t in range(N):
        mask = (1 << t) - 1
        i = t
        nm = mask | (1 << i)
        for val in range(1 << t):
            q, I, P, bal = state_stats(mask, val)
            if P == 0:
                continue
            P_a = state_stats(nm, val)[2]
            P_b = state_stats(nm, val | (1 << i))[2]
            Q = P - (P_a+P_b)/2
            if Q == 0:
                continue
            assert Q > 0
            positive_Q_states += 1
            Hlo,Hhi = entropy_interval(mask,val)
            H0lo,H0hi = entropy_interval(nm,val)
            H1lo,H1hi = entropy_interval(nm,val | (1 << i))
            Llo = Hlo - (H0hi+H1hi)/2
            Lhi = Hhi - (H0lo+H1lo)/2
            assert Lhi <= 32*Q
            if Llo == Lhi == 32*Q:
                assert t > 0 and not bal
                exact_32_states += 1
                exact_32_Qmass += Fraction(1, 1 << t) * Q
    assert positive_Q_states == 96
    assert exact_32_states == 37
    assert exact_32_Qmass == Fraction(29,1024)

    Hlo,Hhi = entropy_interval(0,0)
    c_lo = Hlo/P0
    c_hi = Hhi/P0
    assert c_lo > Fraction(25837489126551, 10**12)  # >25.837489126551
    assert c_hi < 32

    # The first (balanced-root) local split is strictly easier than the root average.
    P_left = state_stats(1,0)[2]
    P_right = state_stats(1,1)[2]
    Q_root = P0 - (P_left+P_right)/2
    H0lo,H0hi = entropy_interval(1,0)
    H1lo,H1hi = entropy_interval(1,1)
    Lroot_hi = Hhi - (H0lo+H1lo)/2
    assert Lroot_hi/Q_root < 23

    print("PASS")
    print("witness_sha256", EXPECTED_WITNESS_SHA)
    print("root_I", I0)
    print("root_P", P0)
    print("root_H_over_P_lower", dec_lower(c_lo, 15))
    print("root_H_over_P_upper", dec_upper(c_hi, 15))
    print("balanced_root_first_split_entropy_over_Q_upper", dec_upper(Lroot_hi/Q_root, 15))
    print("fixed_order", list(range(N)))
    print("prefix_summary_t_nonaffine_balanced_affine_balanced_unbalanced", prefix_summary)
    print("adaptive_first_nonaffine_balanced_hit_probability_min", min_hit)
    print("adaptive_first_nonaffine_balanced_hit_probability_max", max_hit)
    print("adaptive_terminal_P_min", min_tP)
    print("adaptive_terminal_P_max", max_tP)
    print("positive_Q_fixed_order_states", positive_Q_states)
    print("local_entropy_over_Q_upper_bound", 32)
    print("exact_ratio_32_states", exact_32_states)
    print("exact_ratio_32_weighted_Q_mass", exact_32_Qmass)
    print("full_FEI", "OPEN_NOT_PROVED")

if __name__ == "__main__":
    main()
