"""Exact interval checker for account04/B12: two-step quadratic block ledger.

Reconstructs the exact 10-input balanced monotone FEI gate with truth-table
SHA256 3168..., then evaluates every branch-adaptive two-coordinate restriction
policy. Entropy logarithms are enclosed with rational atanh-series intervals.
For Gamma_C(p)=4 C p(1-p), C=6.4548, the block corrected slack is
4 C Q_block - L_block = 4 Q_block (C-rho_block),
rho_block = L_block/(4 Q_block).
The checker proves all 810 depth-two policies have positive corrected block slack.
It also proves coordinate 9 (zero-based) is unsafe at depth one but repaired
after any legal second reveal.
"""
from fractions import Fraction
from collections import Counter
from functools import lru_cache
import hashlib

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
C0 = Fraction(16137, 2500)  # 6.4548 exactly
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

def restrict_table(table, coord, bitval):
    n = len(table).bit_length() - 1
    return [table[x] for x in range(1 << n) if ((x >> coord) & 1) == bitval]

def restrict_original(table, remaining, orig_coord, bitval):
    pos = remaining.index(orig_coord)
    out = restrict_table(table, pos, bitval)
    return out, [c for c in remaining if c != orig_coord]

def total_influence(table):
    n = len(table).bit_length() - 1
    if n == 0:
        return Fraction(0)
    den = 1 << (n - 1)
    ans = Fraction(0)
    for i in range(n):
        bit = 1 << i
        edges = sum(
            table[x] != table[x | bit]
            for x in range(len(table))
            if not (x & bit)
        )
        ans += Fraction(edges, den)
    return ans

def output_minus_probability(table):
    return Fraction(sum(v == -1 for v in table), len(table))

def poincare_currency(table):
    q = output_minus_probability(table)
    return total_influence(table) / 4 - q * (1 - q)

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
    y = x / pow2(k)
    assert 1 <= y < 2
    return k, y

def ln_interval_unit(y):
    z = (y - 1) / (y + 1)
    if z == 0:
        return Fraction(0), Fraction(0)
    z2 = z*z
    zp = z
    partial = Fraction(0)
    for j in range(LOG_TERMS):
        if j:
            zp *= z2
        partial += zp / (2*j + 1)
    lo = 2 * partial
    rem = 2 * z**(2*LOG_TERMS+1) / ((2*LOG_TERMS+1) * (1-z2))
    return lo, lo + rem

LN2_LO, LN2_HI = ln_interval_unit(Fraction(2))

@lru_cache(maxsize=None)
def log2_invprob_interval(a, N):
    p = Fraction(a*a, N*N)
    k, y = normalize_pow2(1/p)
    lo, hi = ln_interval_unit(y)
    return Fraction(k) + lo/LN2_HI, Fraction(k) + hi/LN2_LO

@lru_cache(maxsize=None)
def entropy_interval_tuple(table_tuple):
    W = fwht_int(table_tuple)
    N = len(W)
    hist = Counter(abs(x) for x in W if x)
    lo = Fraction(0)
    hi = Fraction(0)
    for a, count in hist.items():
        p = Fraction(a*a, N*N)
        llo, lhi = log2_invprob_interval(a, N)
        lo += count * p * llo
        hi += count * p * lhi
    return lo, hi

def entropy_interval(table):
    return entropy_interval_tuple(tuple(table))

def decimal_floor(x, digits=18):
    scale = 10**digits
    q = x.numerator * scale // x.denominator
    sign = "-" if q < 0 else ""
    q = abs(q)
    return f"{sign}{q//scale}.{q%scale:0{digits}d}"

def decimal_ceil(x, digits=18):
    scale = 10**digits
    q = -((-x.numerator * scale) // x.denominator)
    sign = "-" if q < 0 else ""
    q = abs(q)
    return f"{sign}{q//scale}.{q%scale:0{digits}d}"

def one_step_ratio(root, first):
    coords = list(range(len(root).bit_length() - 1))
    hrl, hrh = entropy_interval(root)
    pr = poincare_currency(root)
    hcl = Fraction(0)
    hch = Fraction(0)
    pc = Fraction(0)
    for b in (0, 1):
        child, _ = restrict_original(root, coords, first, b)
        lo, hi = entropy_interval(child)
        hcl += lo
        hch += hi
        pc += poincare_currency(child)
    Llo = hrl - hch/2
    Lhi = hrh - hcl/2
    Q = pr - pc/2
    assert Q > 0
    return Llo/(4*Q), Lhi/(4*Q), Q, Llo, Lhi

def two_step_ratio(root, first, second0, second1):
    coords = list(range(len(root).bit_length() - 1))
    hrl, hrh = entropy_interval(root)
    pr = poincare_currency(root)
    hgl = Fraction(0)
    hgh = Fraction(0)
    pg = Fraction(0)
    for b, second in ((0, second0), (1, second1)):
        child, rem = restrict_original(root, coords, first, b)
        for c in (0, 1):
            grandchild, _ = restrict_original(child, rem, second, c)
            lo, hi = entropy_interval(grandchild)
            hgl += lo
            hgh += hi
            pg += poincare_currency(grandchild)
    Llo = hrl - hgh/4
    Lhi = hrh - hgl/4
    Q = pr - pg/4
    assert Q > 0
    return Llo/(4*Q), Lhi/(4*Q), Q, Llo, Lhi

parent = reconstruct_parent()
root = root_gate(parent)
assert total_influence(root) == Fraction(257, 128)
assert poincare_currency(root) == Fraction(129, 512)

root_H_lo, root_H_hi = entropy_interval(root)
assert root_H_lo < root_H_hi
assert decimal_floor(root_H_lo, 18) == "6.509836127588151479"
assert decimal_ceil(root_H_hi, 18) == "6.509836127588151480"

one = []
for i in range(10):
    lo, hi, Q, Llo, Lhi = one_step_ratio(root, i)
    one.append((lo, hi, i, Q, Llo, Lhi))

unsafe = [(lo, hi, i) for lo, hi, i, *_ in one if lo > C0]
assert len(unsafe) == 1
assert unsafe[0][2] == 9
assert unsafe[0][0] > C0

policies = []
for i in range(10):
    remaining = [j for j in range(10) if j != i]
    for j0 in remaining:
        for j1 in remaining:
            lo, hi, Q, Llo, Lhi = two_step_ratio(root, i, j0, j1)
            assert hi < C0
            corrected_slack_lo = 4*C0*Q - Lhi
            corrected_slack_hi = 4*C0*Q - Llo
            assert corrected_slack_lo > 0
            policies.append(
                (lo, hi, i, j0, j1, Q, corrected_slack_lo, corrected_slack_hi)
            )

assert len(policies) == 10 * 9 * 9
worst = max(policies, key=lambda x: x[1])
best = min(policies, key=lambda x: x[0])
min_slack = min(policies, key=lambda x: x[6])
after_bad = [x for x in policies if x[2] == 9]
worst_after_bad = max(after_bad, key=lambda x: x[1])
best_after_bad = min(after_bad, key=lambda x: x[0])
assert len(after_bad) == 81
assert worst_after_bad[1] < C0

bad_one = unsafe[0]
print("PASS")
print("root_truth_sha256 =", EXPECTED_ROOT_SHA)
print("root_I = 257/128")
print("root_P = 129/512")
print("root_H_interval =", decimal_floor(root_H_lo, 18), decimal_ceil(root_H_hi, 18))
print("policies_checked =", len(policies))
print("depth1_unsafe_coordinates_zero_based =", [x[2] for x in unsafe])
print("depth1_coord9_rho_interval =", decimal_floor(bad_one[0], 18), decimal_ceil(bad_one[1], 18))
print("C0 =", decimal_floor(C0, 4))
print("worst_depth2_policy_zero_based =", worst[2], worst[3], worst[4])
print("worst_depth2_rho_interval =", decimal_floor(worst[0], 18), decimal_ceil(worst[1], 18))
print("worst_depth2_safety_margin_lower =", decimal_floor(C0 - worst[1], 18))
print("minimum_corrected_block_slack_lower =", decimal_floor(min_slack[6], 18))
print("coord9_depth2_policies_checked =", len(after_bad))
print("coord9_best_depth2_policy_zero_based =", best_after_bad[3], best_after_bad[4])
print("coord9_best_depth2_rho_interval =", decimal_floor(best_after_bad[0], 18), decimal_ceil(best_after_bad[1], 18))
print("coord9_worst_depth2_policy_zero_based =", worst_after_bad[3], worst_after_bad[4])
print("coord9_worst_depth2_rho_interval =", decimal_floor(worst_after_bad[0], 18), decimal_ceil(worst_after_bad[1], 18))
print("coord9_worst_depth2_safety_margin_lower =", decimal_floor(C0 - worst_after_bad[1], 18))
print("best_depth2_policy_zero_based =", best[2], best[3], best[4])
print("best_depth2_rho_interval =", decimal_floor(best[0], 18), decimal_ceil(best[1], 18))
