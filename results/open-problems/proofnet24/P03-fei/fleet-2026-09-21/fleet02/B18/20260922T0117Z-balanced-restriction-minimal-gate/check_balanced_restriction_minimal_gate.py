"""Exact restriction-lattice certificate for the 10-input FEI gate witness.

Source witness: fleet03/B12 20260922T004418Z-arity10-gate-refutation.
This checker reconstructs that exact witness from its inherited 18-input parent and
enumerates all 3^10-1 proper coordinate restrictions. It proves that every
balanced proper restriction is either a literal or has at most six essential
coordinates. It also records the exact seven nonliteral Walsh-profile classes.

This is a finite structural certificate, not a proof of FEI.
"""
from collections import Counter
from fractions import Fraction
import hashlib
import itertools

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
FIXED = {9:0, 10:0, 11:0, 12:1, 13:1, 14:0, 15:1, 16:1}
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
    return table

def source_witness(parent):
    out = []
    base = sum(v << i for i, v in FIXED.items())
    for z in range(1 << len(FREE_PARENT)):
        idx = base
        for j, i in enumerate(FREE_PARENT):
            idx |= ((z >> j) & 1) << i
        out.append(parent[idx])
    digest = hashlib.sha256(",".join(map(str, out)).encode()).hexdigest()
    assert digest == EXPECTED_WITNESS_SHA
    assert len(out) == 1024 and sum(out) == 0
    return out

def restrict_local(table, status):
    fixed = {i:s for i,s in enumerate(status) if s != -1}
    free = [i for i,s in enumerate(status) if s == -1]
    base = sum(v << i for i,v in fixed.items())
    out = []
    for z in range(1 << len(free)):
        idx = base
        for j,i in enumerate(free):
            idx |= ((z >> j) & 1) << i
        out.append(table[idx])
    return out, free

def influences(table):
    n = len(table).bit_length() - 1
    if n == 0:
        return []
    den = 1 << (n-1)
    ans = []
    for i in range(n):
        bit = 1 << i
        edges = sum(table[x] != table[x|bit]
                    for x in range(len(table)) if not (x & bit))
        ans.append(Fraction(edges, den))
    return ans

def fwht_int(a):
    a = list(a)
    h = 1
    while h < len(a):
        for start in range(0, len(a), 2*h):
            for j in range(start, start+h):
                x,y = a[j],a[j+h]
                a[j],a[j+h] = x+y,x-y
        h *= 2
    return a

def main():
    witness = source_witness(reconstruct_parent())
    count_by_free_essential = Counter()
    nonliteral_classes = Counter()
    balanced_total = 0
    codim_true_counts = {1: Counter(), 2: Counter(), 3: Counter()}

    for status in itertools.product((-1,0,1), repeat=10):
        if all(s == -1 for s in status):
            continue
        sub, free = restrict_local(witness, status)
        codim = 10-len(free)
        if codim in codim_true_counts:
            codim_true_counts[codim][sum(v == -1 for v in sub)] += 1
        if sum(sub) != 0:
            continue
        balanced_total += 1
        infs = influences(sub)
        essential = sum(x > 0 for x in infs)
        count_by_free_essential[(len(free), essential)] += 1
        assert essential == 1 or essential <= 6
        if essential > 1:
            I = sum(infs, Fraction())
            hist = tuple(sorted(Counter(abs(w) for w in fwht_int(sub) if w).items()))
            nonliteral_classes[(len(free), essential, I, hist)] += 1

    expected_counts = {
        (1,1):1028, (2,1):2882, (3,1):3112,
        (4,1):1604, (4,4):184,
        (5,1):392, (5,4):120,
        (6,1):36, (6,4):16, (6,6):100,
        (7,6):40,
    }
    assert balanced_total == 9514
    assert dict(count_by_free_essential) == expected_counts
    assert not any(k[0] in (8,9) for k in count_by_free_essential)

    expected_classes = {
        (4,4,Fraction(3,2),((4,8),(8,2))):184,
        (5,4,Fraction(3,2),((8,8),(16,2))):120,
        (6,4,Fraction(3,2),((16,8),(32,2))):16,
        (6,6,Fraction(13,8),((4,28),(8,7),(12,2),(16,2),(20,2),(24,1),(32,1))):80,
        (6,6,Fraction(13,8),((4,32),(8,4),(16,4),(24,4))):20,
        (7,6,Fraction(13,8),((8,28),(16,7),(24,2),(32,2),(40,2),(48,1),(64,1))):32,
        (7,6,Fraction(13,8),((8,32),(16,4),(32,4),(48,4))):8,
    }
    assert dict(nonliteral_classes) == expected_classes

    assert 256 not in codim_true_counts[1]
    assert 128 not in codim_true_counts[2]
    assert codim_true_counts[3][64] == 40

    print("PASS")
    print("witness_sha256", EXPECTED_WITNESS_SHA)
    print("proper_coordinate_restrictions", 3**10 - 1)
    print("proper_balanced_restrictions", balanced_total)
    print("balanced_counts_by_free_and_essential", sorted(count_by_free_essential.items()))
    print("no_balanced_codim1", True)
    print("no_balanced_codim2", True)
    print("first_balanced_codim3_count", 40)
    print("max_essential_arity_proper_balanced_nonliteral", 6)
    print("nonliteral_profile_classes", len(nonliteral_classes))
    for key, count in sorted(nonliteral_classes.items(), key=lambda kv:(kv[0][0],kv[0][1],kv[0][2],kv[0][3])):
        free, essential, I, hist = key
        print("class", "count", count, "free", free, "essential", essential,
              "I", str(I), "walsh_abs_hist", hist)
    print("full_FEI", "OPEN_NOT_PROVED")

if __name__ == "__main__":
    main()
