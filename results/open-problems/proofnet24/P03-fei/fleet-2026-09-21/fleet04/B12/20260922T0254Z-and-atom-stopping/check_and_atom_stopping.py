"""Exact certificate for the B12 AND-atom stopping theorem on the source-exact G10 FEI witness.

The checker reconstructs the certified arity-10 witness, follows the fixed reveal order
0,1,...,9, and stops at the first affine state or first state whose essential core is a
2-input AND/OR atom.  It proves exact terminal mass/currency/entropy and a rigorous
interval for the preceding block entropy/Poincare ratio.

This is a finite structural theorem about one explicit gate.  It does not prove FEI.
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
LOG_TERMS = 45
AND_OR_SHAPES = {
    (1,1,1,-1), (1,-1,-1,-1),
    (-1,-1,-1,1), (-1,1,1,1),
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

WITNESS = restrict_parent(reconstruct_parent())
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
    return q, I, P

def essential_shape(mask, val):
    arr, free = subtable(mask, val)
    m = len(arr)
    ess = []
    for j in range(len(free)):
        bit = 1 << j
        if any(arr[x] != arr[x | bit] for x in range(m) if not (x & bit)):
            ess.append(j)
    red = []
    for z in range(1 << len(ess)):
        idx = 0
        for t, j in enumerate(ess):
            if (z >> t) & 1:
                idx |= 1 << j
        red.append(arr[idx])
    return tuple(red), len(ess)

def is_and_or_atom(mask, val):
    shape, e = essential_shape(mask, val)
    return e == 2 and shape in AND_OR_SHAPES

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
    while x < pow2(k): k -= 1
    while x >= pow2(k+1): k += 1
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
        if j: zp *= z2
        partial += zp / (2*j+1)
    lo = 2*partial
    rem = 2*z**(2*terms+1) / ((2*terms+1)*(1-z2))
    return lo, lo+rem

def log2_interval(x):
    k, y = normalize_pow2(x)
    ly_lo, ly_hi = ln_interval_unit(y)
    l2_lo, l2_hi = ln_interval_unit(Fraction(2))
    return Fraction(k) + ly_lo/l2_hi, Fraction(k) + ly_hi/l2_lo

def entropy_interval(mask, val):
    arr, _ = subtable(mask, val)
    W = fwht_int(arr)
    n = len(W)
    hist = Counter(abs(w) for w in W if w)
    lo = Fraction(0); hi = Fraction(0)
    for a, count in hist.items():
        p = Fraction(a*a, n*n)
        llo, lhi = log2_interval(1/p)
        lo += count*p*llo
        hi += count*p*lhi
    return lo, hi

def dec_lower(x, digits=15):
    s = 10**digits
    q = x.numerator*s // x.denominator
    return f"{q//s}.{q%s:0{digits}d}"

def dec_upper(x, digits=15):
    s = 10**digits
    q = (x.numerator*s + x.denominator - 1)//x.denominator
    return f"{q//s}.{q%s:0{digits}d}"

def main():
    q0, I0, P0 = state_stats(0,0)
    assert q0 == Fraction(1,2)
    assert I0 == Fraction(257,128)
    assert P0 == Fraction(129,512)

    # Fixed reveal order, stopping at first affine or AND/OR atom.
    frontier = {(0,0): Fraction(1)}
    terminals = []
    for t in range(N+1):
        nxt = {}
        for (mask,val), w in frontier.items():
            P = state_stats(mask,val)[2]
            if P == 0 or is_and_or_atom(mask,val):
                terminals.append((mask,val,w))
                continue
            assert t < N
            i = t
            assert not ((mask >> i) & 1)
            nm = mask | (1 << i)
            nxt[(nm,val)] = nxt.get((nm,val), Fraction(0)) + w/2
            nxt[(nm,val | (1 << i))] = nxt.get((nm,val | (1 << i)), Fraction(0)) + w/2
        frontier = nxt
    assert not frontier
    assert sum(w for _,_,w in terminals) == 1

    and_terms = [(m,v,w) for m,v,w in terminals if is_and_or_atom(m,v)]
    affine_terms = [(m,v,w) for m,v,w in terminals if state_stats(m,v)[2] == 0]
    assert sum(w for _,_,w in and_terms) == Fraction(29,64)
    assert sum(w for _,_,w in affine_terms) == Fraction(35,64)

    # Every non-affine terminal is exactly a 2-input AND/OR atom with H=2, P=1/16.
    for m,v,w in and_terms:
        q,I,P = state_stats(m,v)
        assert q in (Fraction(1,4), Fraction(3,4))
        assert I == 1
        assert P == Fraction(1,16)
        shape,e = essential_shape(m,v)
        assert e == 2 and shape in AND_OR_SHAPES
    terminal_P = sum(w*state_stats(m,v)[2] for m,v,w in and_terms)
    terminal_H = sum(w*Fraction(2) for m,v,w in and_terms)
    assert terminal_P == Fraction(29,1024)
    assert terminal_H == Fraction(29,32)

    Hlo,Hhi = entropy_interval(0,0)
    block_P = P0-terminal_P
    assert block_P == Fraction(229,1024)
    block_lo = (Hlo-terminal_H)/block_P
    block_hi = (Hhi-terminal_H)/block_P

    # Coarse exact separation from the current certified center obstruction scale.
    assert block_hi < Fraction(251,10)              # <25.1
    assert Fraction(260874,10000) > Fraction(251,10) # 26.0874 >25.1

    print("PASS")
    print("witness_sha256", EXPECTED_WITNESS_SHA)
    print("root_I", I0)
    print("root_P", P0)
    print("terminal_AND_OR_probability", Fraction(29,64))
    print("terminal_affine_probability", Fraction(35,64))
    print("terminal_AND_OR_expected_P", terminal_P)
    print("terminal_AND_OR_expected_H", terminal_H)
    print("block_P", block_P)
    print("block_ratio_lower", dec_lower(block_lo, 15))
    print("block_ratio_upper", dec_upper(block_hi, 15))
    print("block_ratio_lt_25_1", True)
    print("current_center_scale_times4_gt_26_0874", True)
    print("full_FEI", "OPEN_NOT_PROVED")

if __name__ == "__main__":
    main()
