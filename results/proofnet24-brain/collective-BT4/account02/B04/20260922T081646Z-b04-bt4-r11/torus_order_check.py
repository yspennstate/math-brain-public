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
    distinct = len({(word[t], coords[t]) for t in range(len(word))}) == len(word)
    return oriented and distinct


def four_distinct_selection(m, n, plus, minus):
    for pi in combinations(range(len(plus)), 2):
        ps = [plus[t] for t in pi]
        for mi in combinations(range(len(minus)), 2):
            ms = [minus[t] for t in mi]
            aport = {ps[0][0], ps[1][0], ms[0][0], ms[1][0]}
            bport = {ps[0][1], ps[1][1], ms[0][1], ms[1][1]}
            if len(aport) == 4 and len(bport) == 4:
                return pi, mi, ps, ms
    return None


def canonical_two_splice(m, n, plus, minus):
    for pi in combinations(range(len(plus)), 2):
        ps = [plus[t] for t in pi]
        for mi in combinations(range(len(minus)), 2):
            ms = [minus[t] for t in mi]
            aport = {ps[0][0], ps[1][0], ms[0][0], ms[1][0]}
            bport = {ps[0][1], ps[1][1], ms[0][1], ms[1][1]}
            if len(aport) < 4 or len(bport) < 4:
                continue
            for perm in ((0, 1), (1, 0)):
                aseg = []
                bseg = []
                for r in (0, 1):
                    s = perm[r]
                    i, j = ps[r]
                    k, l = ms[s]
                    aseg.append(cyc_path_vertices(k, i, m))
                    bseg.append(cyc_path_vertices(j, l, n))
                if aseg[0].isdisjoint(aseg[1]) and bseg[0].isdisjoint(bseg[1]):
                    return pi, mi, perm
    return None


def enumerate_normalized(m, n):
    # Primitive winding u=v=1.  We fix symbol 0 to '+'; every mixed cyclic
    # word has a rotation with this normalization.  Counts are encodings, not
    # isomorphism classes.
    length = m + n
    valid = []
    for plus_pos in combinations(range(length), m):
        if 0 not in plus_pos:
            continue
        chars = ["-"] * length
        for p in plus_pos:
            chars[p] = "+"
        word = "".join(chars)
        if not valid_functional(word, m, n):
            continue
        plus, minus, coords = states_from_word(word, m, n)
        valid.append((word, plus, minus, coords))
    return valid


for m, n in ((4, 4), (5, 5), (6, 6), (4, 6), (5, 4), (4, 5)):
    recs = enumerate_normalized(m, n)
    four_port = sum(four_distinct_selection(m, n, p, q) is not None for _, p, q, _ in recs)
    splice = sum(canonical_two_splice(m, n, p, q) is not None for _, p, q, _ in recs)
    print((m, n), "valid=", len(recs), "four_port=", four_port, "canonical_two_splice=", splice)

word = "++-+--+-"
plus, minus, coords = states_from_word(word, 4, 4)
print("example_word", word)
print("plus", plus)
print("minus", minus)
print("states", coords)
print("valid_functional", valid_functional(word, 4, 4))
print("four_distinct_selection", four_distinct_selection(4, 4, plus, minus))
print("canonical_two_splice", canonical_two_splice(4, 4, plus, minus))
