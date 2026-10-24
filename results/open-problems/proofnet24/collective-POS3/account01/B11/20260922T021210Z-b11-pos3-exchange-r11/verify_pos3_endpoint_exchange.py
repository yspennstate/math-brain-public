from itertools import permutations


def transitive_closure(n, edges):
    R = set(edges)
    changed = True
    while changed:
        changed = False
        add = set()
        for a, b in tuple(R):
            for c, d in tuple(R):
                if b == c and (a, d) not in R:
                    add.add((a, d))
        if add - R:
            R |= add
            changed = True
    return frozenset(R)


def linear_extensions(n, R):
    out = []
    for p in permutations(range(n)):
        pos = {v: i for i, v in enumerate(p)}
        if all(pos[a] < pos[b] for a, b in R):
            out.append(p)
    return out


def comparable(R, a, b):
    return a == b or (a, b) in R or (b, a) in R


def predecessors(R, x):
    return {a for a, b in R if b == x}


def minimal_elements(R, S):
    return {s for s in S if not any((t, s) in R for t in S if t != s)}


def endpoint_stats(n, R, x, y):
    L = linear_extensions(n, R)
    E = len(L)
    plus = []
    minus = []
    for p in L:
        pos = {v: i for i, v in enumerate(p)}
        (plus if pos[x] < pos[y] else minus).append(p)

    S = {z for z in range(n) if (x, z) in R and not comparable(R, z, y)}
    M = minimal_elements(R, S)
    Q = Rbad = I = 0
    channels = {m: 0 for m in M}

    for p in L:
        pos = {v: i for i, v in enumerate(p)}
        if all(pos[y] < pos[m] for m in M):
            Q += 1
        if pos[y] < pos[x]:
            between = p[pos[y] + 1:pos[x]]
            neutral = all(
                not comparable(R, z, x) and not comparable(R, z, y)
                for z in between
            )
            if neutral:
                I += 1
            else:
                Rbad += 1

        before = [m for m in M if pos[m] < pos[y]]
        if before:
            q = min(before, key=lambda m: pos[m])
            if all(pos[q] < pos[m] for m in M if m != q):
                channels[q] += 1

    return E, len(plus), len(minus), M, Q, Rbad, I, channels


def all_forward_closures(n):
    pairs = [(i, j) for i in range(n) for j in range(i + 1, n)]
    seen = set()
    for mask in range(1 << len(pairs)):
        edges = [pairs[k] for k in range(len(pairs)) if (mask >> k) & 1]
        seen.add(transitive_closure(n, edges))
    return seen


def check_general():
    nposets = 0
    npairs = 0
    for n in range(2, 6):
        for R in all_forward_closures(n):
            nposets += 1
            for x in range(n):
                for y in range(n):
                    if x == y or comparable(R, x, y):
                        continue
                    if not predecessors(R, y).issubset(predecessors(R, x)):
                        continue
                    E, ep, em, M, Q, Rbad, I, channels = endpoint_stats(n, R, x, y)
                    assert ep - em == E - Q - Rbad
                    assert 2 * em == Q + Rbad
                    assert 2 * I == Q - Rbad
                    assert sum(channels.values()) == E - Q
                    npairs += 1
    assert nposets == 406, nposets
    assert npairs == 2999, npairs
    return nposets, npairs


def check_79_witness():
    n = 7
    generators = [
        (0, 2), (0, 3), (0, 4), (0, 5), (0, 6),
        (1, 2), (1, 5), (2, 5), (4, 5), (4, 6),
    ]
    R = transitive_closure(n, generators)
    E, ep, em, M, Q, Rbad, I, channels = endpoint_stats(n, R, 0, 1)
    assert (E, ep, em, M, Q, Rbad, I) == (79, 54, 25, {3, 4}, 50, 0, 25)
    assert channels == {3: 9, 4: 20}, channels
    return E, Rbad, channels


def check_partner_family():
    # account02/B19 P(3,1)=C_2(A) disjoint-union C_5(B) disjoint-union C_1(C).
    # A1,A2 = 0,1; B1,...,B5 = 2,...,6; C1 = 7.
    n = 8
    edges = [(0, 1)]
    edges += [(i, j) for i in range(2, 7) for j in range(i + 1, 7)]
    R = transitive_closure(n, edges)
    E, ep, em, M, Q, Rbad, I, channels = endpoint_stats(n, R, 2, 0)
    assert (E, ep, em, M, Q, Rbad, I) == (168, 120, 48, {3}, 88, 8, 40)
    assert channels == {3: 80}
    assert 7 * ep == 5 * E
    assert 21 * Q == 11 * E
    assert 21 * Rbad == E
    return E, ep, Q, Rbad


if __name__ == "__main__":
    nposets, npairs = check_general()
    E79, R79, U79 = check_79_witness()
    Epart, eppart, Qpart, Rpart = check_partner_family()
    print("general_distinct_forward_labeled_closures", nposets)
    print("general_ordered_pairs_checked", npairs)
    print("witness79_E", E79, "reverse_nonneutral_R", R79, "channels", U79)
    print("partner_m3_E", Epart, "eplus", eppart, "Q", Qpart, "R", Rpart)
    print("POS3_ENDPOINT_EXCHANGE_IDENTITY_PASS")
