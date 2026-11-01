from itertools import combinations


def cyc_path_vertices(start, end, n):
    out = [start]
    x = start
    while x != end:
        x = (x + 1) % n
        out.append(x)
    return set(out)


def states_from_word(word, m, n):
    coords = [(0, 0)]
    for t in range(1, len(word)):
        i, j = coords[-1]
        if word[t] == "+":
            i = (i - 1) % m
        else:
            j = (j - 1) % n
        coords.append((i, j))
    i, j = coords[-1]
    if word[0] == "+":
        i = (i - 1) % m
    else:
        j = (j - 1) % n
    assert (i, j) == coords[0]
    plus = [coords[t] for t, c in enumerate(word) if c == "+"]
    minus = [coords[t] for t, c in enumerate(word) if c == "-"]
    return plus, minus, coords


def valid_functional(word, m, n):
    plus, minus, coords = states_from_word(word, m, n)
    oriented = set(plus).isdisjoint(set(minus))
    signed_states_distinct = len({(word[t], coords[t]) for t in range(len(word))}) == len(word)
    return oriented and signed_states_distinct


def has_four_distinct_ports(plus, minus):
    for pi in combinations(range(len(plus)), 2):
        ps = [plus[t] for t in pi]
        for mi in combinations(range(len(minus)), 2):
            ms = [minus[t] for t in mi]
            aport = {ps[0][0], ps[1][0], ms[0][0], ms[1][0]}
            bport = {ps[0][1], ps[1][1], ms[0][1], ms[1][1]}
            if len(aport) == 4 and len(bport) == 4:
                return True
    return False


def has_canonical_two_splice(m, n, plus, minus):
    for pi in combinations(range(len(plus)), 2):
        ps = [plus[t] for t in pi]
        for mi in combinations(range(len(minus)), 2):
            ms = [minus[t] for t in mi]
            aport = {ps[0][0], ps[1][0], ms[0][0], ms[1][0]}
            bport = {ps[0][1], ps[1][1], ms[0][1], ms[1][1]}
            if len(aport) < 4 or len(bport) < 4:
                continue
            for perm in ((0, 1), (1, 0)):
                aseg, bseg = [], []
                for r in (0, 1):
                    s = perm[r]
                    i, j = ps[r]
                    k, ell = ms[s]
                    aseg.append(cyc_path_vertices(k, i, m))
                    bseg.append(cyc_path_vertices(j, ell, n))
                if aseg[0].isdisjoint(aseg[1]) and bseg[0].isdisjoint(bseg[1]):
                    return True
    return False


def enumerate_normalized_primitive(m, n):
    # Primitive winding u=v=1.  The cycle has m plus states and n minus states.
    # Rotation is normalized by requiring state 0 to have plus sign.
    length = m + n
    records = []
    for plus_pos in combinations(range(length), m):
        if 0 not in plus_pos:
            continue
        chars = ["-"] * length
        for p in plus_pos:
            chars[p] = "+"
        word = "".join(chars)
        if valid_functional(word, m, n):
            plus, minus, coords = states_from_word(word, m, n)
            records.append((word, plus, minus, coords))
    return records


for m in range(3, 8):
    for n in range(3, 8):
        records = enumerate_normalized_primitive(m, n)
        four_port = sum(has_four_distinct_ports(p, q) for _, p, q, _ in records)
        splice = sum(has_canonical_two_splice(m, n, p, q) for _, p, q, _ in records)
        print(f"m={m} n={n} valid={len(records)} four_port={four_port} canonical_two_splice={splice}")
        assert splice == 0
