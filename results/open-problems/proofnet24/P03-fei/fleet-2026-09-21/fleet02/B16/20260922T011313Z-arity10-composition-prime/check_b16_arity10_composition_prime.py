from collections import Counter
from itertools import combinations
import hashlib, json

EXPECTED_PARENT_SHA = "f8a7bb2c738d86368305111633376b1a3a83d8ee1f1abcc9a37d841b0f9c7839"
EXPECTED_CHILD_SHA = "3168d8fb8ac9f5d6d7dca1d79146392aecb5eb55cc76ccb028395a9e6a62bfb4"
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
FREE_PARENT_COORDS = tuple(range(9)) + (17,)
FIXED_PARENT_COORDS = tuple(range(9,17))
FIXED_VALUES = (0,0,0,1,1,0,1,1)


def sha_table(table):
    return hashlib.sha256(",".join(map(str, table)).encode()).hexdigest()


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
    assert len(table) == 1 << 18
    assert sum(table) == 0
    assert sha_table(table) == EXPECTED_PARENT_SHA
    return table


def restrict_to_child(parent):
    out = []
    for z in range(1 << 10):
        x = 0
        for j, c in enumerate(FREE_PARENT_COORDS):
            if (z >> j) & 1:
                x |= 1 << c
        for c, v in zip(FIXED_PARENT_COORDS, FIXED_VALUES):
            if v:
                x |= 1 << c
        out.append(parent[x])
    assert sum(out) == 0
    assert sha_table(out) == EXPECTED_CHILD_SHA
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


def exact_influence_numerator(table, n):
    # I = sum_edges 1{different}/2^(n-1) over undirected coordinate edges.
    total = 0
    for i in range(n):
        bit = 1 << i
        for x in range(1 << n):
            if not (x & bit) and table[x] != table[x | bit]:
                total += 1
    return total, 1 << (n-1)


def essential_and_monotone(table, n):
    essential = []
    monotone_directions = []
    for i in range(n):
        bit = 1 << i
        pairs = [(table[x], table[x | bit]) for x in range(1 << n) if not (x & bit)]
        essential.append(any(a != b for a,b in pairs))
        # +/-1 convention: record whether there is a consistent sign direction, without choosing 0/1 orientation.
        nondec = all(a <= b for a,b in pairs)
        noninc = all(a >= b for a,b in pairs)
        monotone_directions.append(nondec or noninc)
    return essential, monotone_directions


def cofactor_signature(table, n, S, assignment):
    S = tuple(S)
    T = tuple(i for i in range(n) if i not in S)
    vec = []
    for tm in range(1 << len(T)):
        x = 0
        for a, i in enumerate(S):
            if (assignment >> a) & 1:
                x |= 1 << i
        for a, i in enumerate(T):
            if (tm >> a) & 1:
                x |= 1 << i
        vec.append(table[x])
    return tuple(vec)


def distinct_cofactors(table, n, S):
    return len({cofactor_signature(table, n, S, sm) for sm in range(1 << len(S))})


def restricted_table(table, n, S, assignment):
    S = tuple(S)
    T = tuple(i for i in range(n) if i not in S)
    out = []
    for tm in range(1 << len(T)):
        x = 0
        for a, i in enumerate(S):
            if (assignment >> a) & 1:
                x |= 1 << i
        for a, i in enumerate(T):
            if (tm >> a) & 1:
                x |= 1 << i
        out.append(table[x])
    return out


def main():
    parent = reconstruct_parent()
    gate = restrict_to_child(parent)
    n = 10
    essential, monotone = essential_and_monotone(gate, n)
    assert all(essential)
    assert all(monotone)

    W = fwht_int(gate)
    walsh_hist = Counter(abs(w) for w in W if w)
    expected_hist = {
        4:337, 8:48, 12:108, 16:28, 24:32, 28:18, 32:34, 36:36,
        40:24, 48:8, 56:8, 72:8, 80:16, 84:12, 96:8, 112:4,
        196:1, 232:8,
    }
    assert dict(sorted(walsh_hist.items())) == expected_hist
    inf_num, inf_den = exact_influence_numerator(gate, n)
    # Peer-certified I = 257/128.
    assert inf_num * 128 == 257 * inf_den

    by_size = {}
    candidate_total = 0
    decomposable_blocks = []
    rejection_stream = hashlib.sha256()
    for r in range(2, n):
        hist = Counter()
        min_distinct = None
        argmin = None
        for S in combinations(range(n), r):
            candidate_total += 1
            nd = distinct_cofactors(gate, n, S)
            hist[nd] += 1
            if min_distinct is None or nd < min_distinct:
                min_distinct, argmin = nd, S
            if nd <= 2:
                decomposable_blocks.append(S)
            rejection_stream.update((str(S)+":"+str(nd)+"\n").encode())
        by_size[str(r)] = {
            "blocks": sum(hist.values()),
            "min_distinct_cofactors": min_distinct,
            "argmin_block": list(argmin),
            "distinct_cofactor_histogram": {str(k): v for k,v in sorted(hist.items())},
        }
    assert candidate_total == 1012
    assert not decomposable_blocks
    assert all(row["min_distinct_cofactors"] >= 3 for row in by_size.values())

    balanced_restrictions = {}
    for r in (1, 2, 3):
        checked = 0
        balanced = 0
        for S in combinations(range(n), r):
            for assignment in range(1 << r):
                checked += 1
                child = restricted_table(gate, n, S, assignment)
                if sum(child) == 0:
                    balanced += 1
        balanced_restrictions[str(r)] = {"restrictions_checked": checked, "balanced": balanced}
    assert balanced_restrictions["1"] == {"restrictions_checked": 20, "balanced": 0}
    assert balanced_restrictions["2"] == {"restrictions_checked": 180, "balanced": 0}
    assert balanced_restrictions["3"]["balanced"] == 40

    out = {
        "status": "PASS",
        "parent_truth_table_sha256": EXPECTED_PARENT_SHA,
        "arity10_truth_table_sha256": EXPECTED_CHILD_SHA,
        "balanced": True,
        "all_10_coordinates_essential": all(essential),
        "coordinatewise_monotone_or_antitone": all(monotone),
        "influence": "257/128",
        "walsh_abs_histogram": {str(k): v for k,v in sorted(walsh_hist.items())},
        "functional_decomposition_criterion": "a proper block S can be compressed to one Boolean bit iff its assignments induce at most two distinct cofactors on the complement",
        "candidate_blocks_checked_sizes_2_to_9": candidate_total,
        "decomposable_blocks_found": len(decomposable_blocks),
        "composition_prime": True,
        "balanced_coordinate_restrictions": balanced_restrictions,
        "per_block_size": by_size,
        "rejection_stream_sha256": rejection_stream.hexdigest(),
    }
    print(json.dumps(out, indent=2, sort_keys=True))

if __name__ == "__main__":
    main()
