from itertools import combinations, permutations


def closure_ok_relation(n, mask):
    rel = [[False] * n for _ in range(n)]
    bit = 0
    for i in range(n):
        for j in range(i + 1, n):
            if (mask >> bit) & 1:
                rel[i][j] = True
            bit += 1
    for i in range(n):
        for j in range(n):
            if rel[i][j]:
                for k in range(n):
                    if rel[j][k] and not rel[i][k]:
                        return None
    return rel


def inc(rel, a, b):
    return not rel[a][b] and not rel[b][a]


def width_leq3(rel):
    n = len(rel)
    for q in combinations(range(n), 4):
        if all(inc(rel, a, b) for a, b in combinations(q, 2)):
            return False
    return True


def extensions(rel):
    n = len(rel)
    pred = [0] * n
    for v in range(n):
        for u in range(n):
            if rel[u][v]:
                pred[v] |= 1 << u
    out = []

    def rec(mask, word):
        if mask == (1 << n) - 1:
            out.append(tuple(word))
            return
        for v in range(n):
            if not (mask >> v) & 1 and pred[v] & ~mask == 0:
                rec(mask | (1 << v), word + [v])

    rec(0, [])
    return out


def count_before(exts, a, b):
    return sum(e.index(a) < e.index(b) for e in exts)


def relation_code(rel, t, a):
    if rel[t][a]:
        return -1
    if rel[a][t]:
        return 1
    return 0


def distinguishers(rel, x, y):
    return [
        t
        for t in range(len(rel))
        if t not in (x, y) and relation_code(rel, t, x) != relation_code(rel, t, y)
    ]


def event_count(exts, *ordered):
    return sum(
        all(e.index(ordered[i]) < e.index(ordered[i + 1]) for i in range(len(ordered) - 1))
        for e in exts
    )


def maximal_in(rel, S):
    return [s for s in S if not any(s != t and rel[s][t] for t in S)]


def minimal_in(rel, S):
    return [s for s in S if not any(s != t and rel[t][s] for t in S)]


def check_config(rel, exts, x, y, d, u):
    N = len(exts)
    assert inc(rel, x, y) and set(distinguishers(rel, x, y)) == {d, u}
    assert rel[d][y] and inc(rel, d, x)
    assert rel[x][u] and inc(rel, u, y) and inc(rel, d, u)

    for t in range(len(rel)):
        assert not (rel[d][t] and rel[t][y] and t not in (d, y))
        assert not (rel[x][t] and rel[t][u] and t not in (x, u))

    D = [t for t in range(len(rel)) if t not in (d, u) and rel[t][u] and not rel[t][d]]
    U = [t for t in range(len(rel)) if t not in (d, u) and rel[d][t] and not rel[u][t]]
    assert x in D and y in U
    assert x in maximal_in(rel, D)
    assert y in minimal_in(rel, U)

    for z in D:
        if z != x:
            assert rel[z][x] or inc(rel, z, x)
    for w in U:
        if w != y:
            assert rel[y][w] or inc(rel, w, y)

    lower_shadows = [z for z in D if z != x and rel[z][x]]
    for z in maximal_in(rel, lower_shadows):
        assert not any(rel[z][t] and rel[t][x] and t not in (z, x) for t in range(len(rel)))
        n_dz = count_before(exts, d, z)
        n_dx = count_before(exts, d, x)
        n_zd = count_before(exts, z, d)
        n_sandwich = event_count(exts, z, d, x)
        assert n_sandwich == n_dx - n_dz
        assert n_sandwich == n_dx + n_zd - N
        if 3 * n_zd > 2 * N and 3 * n_dx > 2 * N:
            assert 3 * n_sandwich > N

    upper_shadows = [w for w in U if w != y and rel[y][w]]
    for w in minimal_in(rel, upper_shadows):
        assert not any(rel[y][t] and rel[t][w] and t not in (y, w) for t in range(len(rel)))
        n_yu = count_before(exts, y, u)
        n_wu = count_before(exts, w, u)
        n_uw = count_before(exts, u, w)
        n_sandwich = event_count(exts, y, u, w)
        assert n_sandwich == n_yu - n_wu
        assert n_sandwich == n_yu + n_uw - N
        if 3 * n_yu > 2 * N and 3 * n_uw > 2 * N:
            assert 3 * n_sandwich > N


def exhaustive():
    total_configs = 0
    lower_shadow_tests = 0
    upper_shadow_tests = 0
    heavy_orientation_activations = 0
    for n in range(4, 7):
        npos = 0
        ncfg = 0
        for mask in range(1 << (n * (n - 1) // 2)):
            rel = closure_ok_relation(n, mask)
            if rel is None or not width_leq3(rel):
                continue
            npos += 1
            exts = extensions(rel)
            for x, y in permutations(range(n), 2):
                if not inc(rel, x, y):
                    continue
                ds = distinguishers(rel, x, y)
                if len(ds) != 2:
                    continue
                for d, u in permutations(ds, 2):
                    if not (
                        rel[d][y]
                        and inc(rel, d, x)
                        and rel[x][u]
                        and inc(rel, u, y)
                        and inc(rel, d, u)
                    ):
                        continue
                    N = len(exts)
                    if not (
                        3 * count_before(exts, x, y) > 2 * N
                        and 3 * count_before(exts, x, d) < N
                        and 3 * count_before(exts, u, y) < N
                    ):
                        continue
                    check_config(rel, exts, x, y, d, u)
                    D = [t for t in range(n) if t not in (d, u) and rel[t][u] and not rel[t][d]]
                    U = [t for t in range(n) if t not in (d, u) and rel[d][t] and not rel[u][t]]
                    lower = maximal_in(rel, [z for z in D if z != x and rel[z][x]])
                    upper = minimal_in(rel, [w for w in U if w != y and rel[y][w]])
                    lower_shadow_tests += len(lower)
                    upper_shadow_tests += len(upper)
                    for z in lower:
                        if 3 * count_before(exts, z, d) > 2 * N and 3 * count_before(exts, d, x) > 2 * N:
                            heavy_orientation_activations += 1
                    for w in upper:
                        if 3 * count_before(exts, y, u) > 2 * N and 3 * count_before(exts, u, w) > 2 * N:
                            heavy_orientation_activations += 1
                    ncfg += 1
                    total_configs += 1
        print("n", n, "natural_posets_width_leq3", npos, "crossed_exact_two_strong_configs", ncfg)
    print("total_configs", total_configs)
    print("lower_shadow_cover_tests", lower_shadow_tests)
    print("upper_shadow_cover_tests", upper_shadow_tests)
    print("heavy_orientation_activations", heavy_orientation_activations)


def adversary():
    n = 8
    relations = [
        (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7),
        (1, 4), (1, 6), (1, 7),
        (2, 6), (2, 7),
        (3, 5), (3, 6), (3, 7),
        (4, 6), (4, 7),
        (5, 7), (6, 7),
    ]
    rel = [[False] * n for _ in range(n)]
    for a, b in relations:
        rel[a][b] = True
    assert width_leq3(rel)
    exts = extensions(rel)
    x, y, d, u, z, w = 3, 4, 1, 5, 0, 6
    assert len(exts) == 60
    check_config(rel, exts, x, y, d, u)
    vals = {
        "N": len(exts),
        "x<y": count_before(exts, x, y),
        "d<u": count_before(exts, d, u),
        "z<d": count_before(exts, z, d),
        "d<x": count_before(exts, d, x),
        "z<d<x": event_count(exts, z, d, x),
        "y<u": count_before(exts, y, u),
        "u<w": count_before(exts, u, w),
        "y<u<w": event_count(exts, y, u, w),
    }
    print("adversary", vals)
    assert vals == {
        "N": 60,
        "x<y": 44,
        "d<u": 55,
        "z<d": 42,
        "d<x": 41,
        "z<d<x": 23,
        "y<u": 41,
        "u<w": 42,
        "y<u<w": 23,
    }
    print("POS3_SHADOW_COVER_CHARGE_CHECK_PASS")


if __name__ == "__main__":
    exhaustive()
    adversary()
