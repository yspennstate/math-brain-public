"""Exact finite certificate for proper balanced coordinate restrictions of the
explicit 10-input FEI gate-margin witness from fleet03/B12.

The parent 18-variable Numaro seed and the 10-variable witness are reconstructed
source-exactly from the inherited certificate.  We enumerate all 3^10-1 proper
physical coordinate restrictions of the 10-variable witness.  For every
balanced restriction with I>1 we compute exact influence and the integer Walsh
absolute-value histogram.  Exactly seven (dimension, I, histogram) types occur.
Elementary integer inequalities then certify H/(I-1)<6.4 for every proper
balanced restriction, while the unrestricted 10-variable witness has
H/(I-1)>6.45937228.

This is a finite structural certificate about this witness; it is not FEI.
"""
from fractions import Fraction
from collections import Counter
import hashlib

EXPECTED_PARENT_SHA = "f8a7bb2c738d86368305111633376b1a3a83d8ee1f1abcc9a37d841b0f9c7839"
EXPECTED_WITNESS_SHA = "3168d8fb8ac9f5d6d7dca1d79146392aecb5eb55cc76ccb028395a9e6a62bfb4"
C0 = Fraction(16137, 2500)  # 6.4548

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
    base = sum(v << i for i, v in FIXED_PARENT.items())
    for z in range(1 << len(FREE_PARENT)):
        idx = base
        for j, i in enumerate(FREE_PARENT):
            idx |= ((z >> j) & 1) << i
        out.append(parent[idx])
    digest = hashlib.sha256(",".join(map(str, out)).encode()).hexdigest()
    assert digest == EXPECTED_WITNESS_SHA
    assert sum(out) == 0
    return out


def fwht_int(a):
    a = list(a)
    h = 1
    while h < len(a):
        for s in range(0, len(a), 2*h):
            for j in range(s, s+h):
                x, y = a[j], a[j+h]
                a[j], a[j+h] = x+y, x-y
        h *= 2
    return a


def total_influence(table):
    n = len(table).bit_length() - 1
    if n == 0:
        return Fraction(0)
    edges = 0
    for i in range(n):
        bit = 1 << i
        edges += sum(table[x] != table[x | bit]
                     for x in range(len(table)) if not (x & bit))
    return Fraction(edges, 1 << (n-1))


def subtable(witness, state):
    # state[i] = -1 free, 0 fixed to 0, 1 fixed to 1.
    free = [i for i, s in enumerate(state) if s == -1]
    base = sum(s << i for i, s in enumerate(state) if s != -1)
    out = []
    for z in range(1 << len(free)):
        idx = base
        for j, i in enumerate(free):
            idx |= ((z >> j) & 1) << i
        out.append(witness[idx])
    return out


def histogram(table):
    return tuple(sorted(Counter(abs(x) for x in fwht_int(table) if x).items()))


def decode_state(code):
    # base-3 digit: 0=free, 1=fixed 0, 2=fixed 1
    state = []
    for _ in range(10):
        d = code % 3
        code //= 3
        state.append(-1 if d == 0 else d-1)
    return tuple(state)


def main():
    witness = restrict_parent(reconstruct_parent())
    balanced_counts = Counter()
    dangerous_types = Counter()
    effective_counts = Counter()
    total_balanced = 0
    i_gt_1 = 0
    no_balanced_free_8_or_9 = True

    for code in range(3**10):
        state = decode_state(code)
        free = state.count(-1)
        if free == 10:  # original witness, not a proper restriction
            continue
        table = subtable(witness, state)
        if sum(table) != 0:
            continue
        total_balanced += 1
        balanced_counts[free] += 1
        if free in (8, 9):
            no_balanced_free_8_or_9 = False
        I = total_influence(table)
        if I <= 1:
            continue
        i_gt_1 += 1
        infs = []
        n = len(table).bit_length() - 1
        for q in range(n):
            bit = 1 << q
            edges = sum(table[x] != table[x | bit]
                        for x in range(len(table)) if not (x & bit))
            infs.append(Fraction(edges, 1 << (n-1)))
        effective = sum(x > 0 for x in infs)
        effective_counts[(free, effective)] += 1
        dangerous_types[(free, I, histogram(table))] += 1

    expected_balanced = {
        1: 1028, 2: 2882, 3: 3112, 4: 1788,
        5: 512, 6: 152, 7: 40,
    }
    assert dict(sorted(balanced_counts.items())) == expected_balanced
    assert total_balanced == 9514
    assert no_balanced_free_8_or_9
    assert i_gt_1 == 460
    assert dict(sorted(effective_counts.items())) == {
        (4,4):184, (5,4):120, (6,4):16, (6,6):100, (7,6):40
    }
    # Thus every proper balanced restriction with I>1 has effective arity 4 or 6.

    expected_types = {
        (4, Fraction(3,2), ((4,8),(8,2))),
        (5, Fraction(3,2), ((8,8),(16,2))),
        (6, Fraction(3,2), ((16,8),(32,2))),
        (6, Fraction(13,8), ((4,32),(8,4),(16,4),(24,4))),
        (7, Fraction(13,8), ((8,32),(16,4),(32,4),(48,4))),
        (6, Fraction(13,8), ((4,28),(8,7),(12,2),(16,2),(20,2),(24,1),(32,1))),
        (7, Fraction(13,8), ((8,28),(16,7),(24,2),(32,2),(40,2),(48,1),(64,1))),
    }
    assert set(dangerous_types) == expected_types

    # The I=3/2 types have H=3 exactly, hence H/(I-1)=6.
    # The first I=13/8 pair has
    # H = 23/4 - (9/8) log_2 3,
    # R = H/(5/8) = 46/5 - (9/5) log_2 3.
    # It is < 6.4 iff log_2 3 > 14/9, certified by 3^9 > 2^14.
    assert 3**9 > 2**14

    # The other I=13/8 pair has
    # H = 11/2 - (27/64)log_2 3 - (25/64)log_2 5.
    # H<4 iff 3^27 5^25 > 2^96; hence its R<6.4.
    assert (3**27) * (5**25) > 2**96

    # The first pair is also the exact maximum: H1>H2 iff
    # 2^16 5^25 > 3^45.
    assert (2**16) * (5**25) > 3**45

    # Since C0=6.4548, every proper balanced restriction with I>1 has
    # c_G=4(R-C0)<4(6.4-C0)=-0.2192 < 0.
    c_upper = 4 * (Fraction(32,5) - C0)
    assert c_upper == Fraction(-137,625)  # -0.2192

    print("PASS")
    print("witness_sha256", EXPECTED_WITNESS_SHA)
    print("proper_restrictions", 3**10 - 1)
    print("balanced_proper_restrictions", total_balanced)
    print("balanced_counts_by_free_dimension", dict(sorted(balanced_counts.items())))
    print("balanced_with_I_gt_1", i_gt_1)
    print("distinct_I_histogram_types", len(dangerous_types))
    print("free_vs_effective_counts", dict(sorted(effective_counts.items())))
    print("effective_arities_with_I_gt_1", [4,6])
    print("balanced_free_8_or_9", False)
    print("max_ratio_exact", "46/5-(9/5)log2(3)")
    print("max_ratio_decimal", "6.347067498701918873...")
    print("universal_proper_margin_upper", "-0.2192 (strict)")
    print("full_FEI", "OPEN_NOT_PROVED")


if __name__ == "__main__":
    main()
