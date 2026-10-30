from itertools import combinations


def states_from_word(word, m, n):
    coords = []
    i = j = 0
    for ch in word:
        coords.append((i, j))
        if ch == '+':
            i = (i - 1) % m
        else:
            j = (j - 1) % n
    assert (i, j) == (0, 0)
    plus = [coords[k] for k, ch in enumerate(word) if ch == '+']
    minus = [coords[k] for k, ch in enumerate(word) if ch == '-']
    return plus, minus, coords


def cycset(s, t, n):
    z = s
    out = {z}
    while z != t:
        z = (z + 1) % n
        out.add(z)
    return out


def functional(word, m, n):
    plus, minus, coords = states_from_word(word, m, n)
    return set(plus).isdisjoint(set(minus)) and len({(word[k], coords[k]) for k in range(len(word))}) == len(word)


def canonical_two_splice(m, n, plus, minus):
    for ip in combinations(range(len(plus)), 2):
        for im in combinations(range(len(minus)), 2):
            ps = [plus[k] for k in ip]
            ms = [minus[k] for k in im]
            pts = ps + ms
            if len({x for x, _ in pts}) < 4 or len({y for _, y in pts}) < 4:
                continue
            for swap in (0, 1):
                pairs = [(0, swap), (1, 1 - swap)]
                A = []
                B = []
                for r, s in pairs:
                    pi, pj = ps[r]
                    mi, mj = ms[s]
                    A.append(cycset(mi, pi, m))
                    B.append(cycset(pj, mj, n))
                if A[0].isdisjoint(A[1]) and B[0].isdisjoint(B[1]):
                    return True
    return False


def check(m, n):
    L = m + n
    valid = four = splice = 0
    for plus_positions in combinations(range(L), m):
        if 0 not in plus_positions:
            continue
        chars = ['-'] * L
        for k in plus_positions:
            chars[k] = '+'
        word = ''.join(chars)
        if not functional(word, m, n):
            continue
        valid += 1
        plus, minus, _ = states_from_word(word, m, n)
        has_four = False
        for ip in combinations(range(m), 2):
            for im in combinations(range(n), 2):
                pts = [plus[k] for k in ip] + [minus[k] for k in im]
                if len({x for x, _ in pts}) == 4 and len({y for _, y in pts}) == 4:
                    has_four = True
                    break
            if has_four:
                break
        four += int(has_four)
        splice += int(canonical_two_splice(m, n, plus, minus))
    return valid, four, splice


for m in range(3, 8):
    for n in range(3, 8):
        valid, four, splice = check(m, n)
        print(f'm={m} n={n} valid={valid} four_port={four} canonical_two_splice={splice}')
        assert splice == 0
