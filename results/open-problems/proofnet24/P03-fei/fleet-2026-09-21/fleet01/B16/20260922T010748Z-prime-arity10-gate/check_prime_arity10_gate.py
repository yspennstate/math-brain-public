"""Exact composition-prime certificate for the inherited 10-input FEI gate.

Reconstructs the source-exact Numaro restriction used by fleet03/B12 and
checks the module criterion for every nontrivial candidate inner block A:
if G=F(g_A(x_A),x_{A^c}), the rows x_A -> G(x_A, .) take at most two
values. Conversely <=2 row types gives such a decomposition. Thus a Boolean
gate is prime for disjoint functional composition iff no A with 2<=|A|<=n-1
has <=2 row types (after deleting unary blocks).
"""
import hashlib
import itertools
from collections import Counter

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
FREE = [0,1,2,3,4,5,6,7,8,17]

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

def restrict_parent(parent):
    out = []
    base = sum(v << i for i, v in FIXED.items())
    for z in range(1 << len(FREE)):
        idx = base
        for j, i in enumerate(FREE):
            idx |= ((z >> j) & 1) << i
        out.append(parent[idx])
    digest = hashlib.sha256(",".join(map(str, out)).encode()).hexdigest()
    assert digest == EXPECTED_WITNESS_SHA
    assert len(out) == 1024 and sum(out) == 0
    return out

def row_type_count(table, A):
    n = len(table).bit_length() - 1
    A = tuple(A)
    Aset = set(A)
    B = tuple(i for i in range(n) if i not in Aset)
    rows = set()
    for xa in range(1 << len(A)):
        row = []
        for xb in range(1 << len(B)):
            idx = 0
            for j, i in enumerate(A):
                idx |= ((xa >> j) & 1) << i
            for j, i in enumerate(B):
                idx |= ((xb >> j) & 1) << i
            row.append(table[idx])
        rows.add(tuple(row))
    return len(rows)

def main():
    table = restrict_parent(reconstruct_parent())
    n = 10
    hist = Counter()
    modules = []
    minimizers = []
    min_types = None
    checked = 0
    for r in range(2, n):
        for A in itertools.combinations(range(n), r):
            checked += 1
            c = row_type_count(table, A)
            hist[c] += 1
            if c <= 2:
                modules.append((A, c))
            if min_types is None or c < min_types:
                min_types = c
                minimizers = [A]
            elif c == min_types:
                minimizers.append(A)
    assert checked == 1012
    assert not modules
    assert min_types == 3
    assert len(minimizers) == 18
    assert sum(hist.values()) == 1012
    print("PASS")
    print("witness_sha256", EXPECTED_WITNESS_SHA)
    print("candidate_inner_blocks_checked", checked)
    print("modules_with_at_most_two_row_types", len(modules))
    print("minimum_row_type_count", min_types)
    print("number_of_minimizers", len(minimizers))
    print("row_type_histogram", sorted(hist.items()))
    print("prime_for_disjoint_functional_composition", True)

if __name__ == "__main__":
    main()
