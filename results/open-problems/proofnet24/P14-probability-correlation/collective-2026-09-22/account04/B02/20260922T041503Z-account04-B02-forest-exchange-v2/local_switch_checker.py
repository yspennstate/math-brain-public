from itertools import combinations


def edge(u, v):
    return (u, v) if u < v else (v, u)


def forest_and_components(n, edges):
    p = list(range(n))
    size = [1] * n
    def find(x):
        while p[x] != x:
            p[x] = p[p[x]]
            x = p[x]
        return x
    for u, v in edges:
        a, b = find(u), find(v)
        if a == b:
            return False, None
        if size[a] < size[b]:
            a, b = b, a
        p[b] = a
        size[a] += size[b]
    comps = {}
    for x in range(n):
        r = find(x)
        comps.setdefault(r, set()).add(x)
    return True, list(comps.values())


def is_forest(n, edges):
    return forest_and_components(n, edges)[0]


def component_map(n, edges):
    ok, cs = forest_and_components(n, edges)
    assert ok
    out = {}
    for i, c in enumerate(cs):
        for v in c:
            out[v] = (i, c)
    return out


def path_edges(n, edges, s, t):
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v); adj[v].append(u)
    parent = {s: None}
    stack = [s]
    while stack:
        u = stack.pop()
        if u == t:
            break
        for v in adj[u]:
            if v not in parent:
                parent[v] = u
                stack.append(v)
    if t not in parent:
        return None
    verts = []
    x = t
    while parent[x] is not None:
        verts.append(edge(x, parent[x]))
        x = parent[x]
    verts.reverse()
    return verts


def all_forests(n, allowed):
    m = len(allowed)
    for mask in range(1 << m):
        es = [allowed[i] for i in range(m) if mask >> i & 1]
        if is_forest(n, es):
            yield tuple(es)


def in_D(n, H, e, f):
    return is_forest(n, list(H) + [e, f])


def in_Q(n, H, e, f):
    return (is_forest(n, list(H) + [e]) and
            is_forest(n, list(H) + [f]) and
            not is_forest(n, list(H) + [e, f]))


def one_edge_blockers(n, H, allowed, e, f):
    hs = set(H)
    ans = []
    for h in allowed:
        if h in hs:
            continue
        Hp = list(H) + [h]
        if (is_forest(n, Hp) and is_forest(n, Hp + [f]) and
                not is_forest(n, Hp + [e, f])):
            ans.append(h)
    return ans


def zero_blocker_characterization(n, H, e, f):
    a, b = e; c, d = f
    cm = component_map(n, H)
    return (len(cm[a][1]) == 1 and len(cm[b][1]) == 1 and
            cm[c][0] != cm[d][0])


def count_forests_containing_fixed_edge(m):
    if m < 2:
        return 0
    E = list(combinations(range(m), 2))
    fixed = (0, 1)
    return sum(1 for F in all_forests(m, E) if fixed in F)


def check_disjoint(n):
    E = list(combinations(range(n), 2))
    e, f = (0, 1), (2, 3)
    K = [g for g in E if g not in (e, f)]
    D = []
    Q = []
    zero = []
    bad_class = []
    map0, map1 = set(), set()
    domain_pairs = 0
    local_pairs_pass = 0

    Fs = list(all_forests(n, K))
    badF = [F for F in Fs if not is_forest(n, list(F) + [e])]

    for H in Fs:
        if in_Q(n, H, e, f):
            Q.append(H)
        if not in_D(n, H, e, f):
            continue
        D.append(H)
        blockers = one_edge_blockers(n, H, K, e, f)
        zchar = zero_blocker_characterization(n, H, e, f)
        if (len(blockers) == 0) != zchar:
            bad_class.append((H, blockers, zchar))
        if not blockers:
            zero.append(H)
            Hs = set(H)
            M0 = tuple(sorted(Hs | {(0, 2), (1, 3)}))
            M1 = tuple(sorted(Hs | {(0, 3), (1, 2)}))
            assert is_forest(n, M0) and in_Q(n, M0, e, f)
            assert is_forest(n, M1) and in_Q(n, M1, e, f)
            map0.add(M0); map1.add(M1)

        # Check the explicit size-preserving local repair for every bad F.
        for F in badF:
            domain_pairs += 1
            P = path_edges(n, F, 0, 1)
            assert P is not None and len(P) >= 2
            if blockers:
                h = min(blockers)
                Fp = tuple(g for g in F if g != P[0])
                Hp = tuple(sorted(set(H) | {h}))
            else:
                Fp = tuple(g for g in F if g not in {P[0], P[-1]})
                Hp = tuple(sorted(set(H) | {(0, 2), (1, 3)}))
            if not is_forest(n, Fp):
                raise AssertionError('Fp cyclic')
            if not is_forest(n, list(Fp) + [e]):
                raise AssertionError('e not addable after cuts')
            if not is_forest(n, Hp):
                raise AssertionError('Hp cyclic')
            if not is_forest(n, list(Hp) + [f]):
                raise AssertionError('f not addable in target')
            if is_forest(n, list(Hp) + [e, f]):
                raise AssertionError('target still in D')
            if len(Fp) + len(Hp) != len(F) + len(H):
                raise AssertionError('total size not preserved')
            local_pairs_pass += 1

    z_formula = count_forests_containing_fixed_edge(n - 2)
    assert not bad_class
    assert len(zero) == z_formula
    assert len(map0) == len(zero) and len(map1) == len(zero)
    assert map0.isdisjoint(map1)
    assert map0 | map1 <= set(Q)
    assert len(Q) >= 2 * len(zero)
    assert local_pairs_pass == domain_pairs
    return {
        'n': n, 'N': len(Fs), 'badF': len(badF), 'D': len(D), 'Q': len(Q),
        'zero': len(zero), 'two_zero_images': 2 * len(zero),
        'domain_pairs': domain_pairs,
    }


def check_adjacent(n):
    E = list(combinations(range(n), 2))
    e, f, h = (0, 1), (0, 2), (1, 2)
    K = [g for g in E if g not in (e, f)]
    Fs = list(all_forests(n, K))
    badF = [F for F in Fs if not is_forest(n, list(F) + [e])]
    D = []
    pairs = 0
    for H in Fs:
        if not in_D(n, H, e, f):
            continue
        D.append(H)
        Hp = tuple(sorted(set(H) | {h}))
        assert is_forest(n, Hp)
        assert is_forest(n, list(Hp) + [f])
        assert not is_forest(n, list(Hp) + [e, f])
        for F in badF:
            pairs += 1
            P = path_edges(n, F, 0, 1)
            assert P is not None and len(P) >= 2
            Fp = tuple(g for g in F if g != P[0])
            assert is_forest(n, list(Fp) + [e])
            assert len(Fp) + len(Hp) == len(F) + len(H)
    return {'n': n, 'N': len(Fs), 'badF': len(badF), 'D': len(D), 'domain_pairs': pairs}


def main():
    print('FOREST_LOCAL_TWO_SWITCH_EXACT_CHECK')
    print('candidate_one_cut_one_join=REFUTED by disjoint K4 with H=empty')
    for n in range(3, 7):
        r = check_adjacent(n)
        print('ADJ', ' '.join(f'{k}={v}' for k,v in r.items()))
    for n in range(4, 7):
        r = check_disjoint(n)
        print('DIS', ' '.join(f'{k}={v}' for k,v in r.items()))
    print('K4_ZERO_BLOCKER exact: H=empty, one_edge_blockers=0, two_switch_images=2')
    print('ALL_EXACT_ASSERTIONS_PASSED')


if __name__ == '__main__':
    main()
