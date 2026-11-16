"""The counting proof of the Erdos-Sos conjecture (as written out in arXiv 2609.17877, Wood), checked on small graphs.

Notation of the exposition.  G has n vertices and m edges.  M(G) is the set of pairs (pi, i), pi an ordering
(v_1..v_n) of V(G), with v_1 v_i an edge.  For a tree T and a vertex r of T, R(T, r) is the set of (pi, i) in M(G)
such that G[{v_1..v_i}] contains T with r mapped to v_1.

Claims checked:
  (1)  |M(G)| = 2 m (n-1)!
  (2)  |M(G)| <= |R(T, r)| + (t-2) n!                      for every tree T on t >= 2 vertices and every r
  L3   |R(T - r, r')| <= |R(T, r)| + n!                    r a leaf, r' its neighbour, t >= 3
  L4   |R(T1, r)| + |R(T2, r)| <= |M(G)| + |R(T, r)| + n!  T = T1 u T2 glued at a non-leaf r
  Thm  average degree > t-2  implies  G contains every tree on t vertices

Part A (literal): every labelled graph on n <= 4 vertices and every graph on 5 vertices up to isomorphism.  The
sets are built as explicit sets of (ordering, index) pairs, and the two maps f of Lemmas 3 and 4 are applied to
every element: f must land in the stated target set and be injective.
Part B (counting): every graph on 6 vertices up to isomorphism and random graphs on 7 and 8 vertices; |R| is
computed from subsets, |R| = sum over (S, v_1, v_i) of (|S|-2)! (n-|S|)!.
A rooted tree is the sorted tuple of its children's rooted trees; () is a single vertex.
"""
import random
import sys
from itertools import combinations, permutations
from math import factorial


def rooted_trees(t, _memo={}):
    """All rooted trees with t vertices, as canonical nested tuples."""
    if t in _memo:
        return _memo[t]
    if t == 1:
        res = [()]
    else:
        res = set()

        def parts(total, maxpart):
            if total == 0:
                yield []
                return
            for p in range(min(total, maxpart), 0, -1):
                for rest in parts(total - p, p):
                    yield [p] + rest

        for part in parts(t - 1, t - 1):
            def build(idx, acc):
                if idx == len(part):
                    res.add(tuple(sorted(acc)))
                    return
                for sub in rooted_trees(part[idx]):
                    build(idx + 1, acc + [sub])
            build(0, [])
        res = sorted(res)
    _memo[t] = res
    return res


def size(tree):
    return 1 + sum(size(c) for c in tree)


def embeddings(adj, allowed, v, tree, used):
    """Yield the vertex masks 'used' after embedding tree rooted at host vertex v (v already in used)."""
    if not tree:
        yield used
        return
    first, rest = tree[0], tree[1:]
    nb = adj[v] & allowed & ~used
    w = 0
    while nb:
        if nb & 1:
            for u2 in embeddings(adj, allowed, w, first, used | (1 << w)):
                yield from embeddings(adj, allowed, v, rest, u2)
        nb >>= 1
        w += 1


def contains(adj, S, v, tree, cache):
    key = (S, v, tree)
    if key not in cache:
        ok = False
        if size(tree) <= bin(S).count("1"):
            for _ in embeddings(adj, S, v, tree, 1 << v):
                ok = True
                break
        cache[key] = ok
    return cache[key]


def adj_of(n, edges):
    adj = [0] * n
    for a, b in edges:
        adj[a] |= 1 << b
        adj[b] |= 1 << a
    return adj


# ---------------------------------------------------------------- part A: literal sets and maps
def literal(n, edges, stats):
    adj = adj_of(n, edges)
    m = len(edges)
    cache = {}
    perms = list(permutations(range(n)))
    M = set()
    for pi in perms:
        for i in range(2, n + 1):
            if adj[pi[0]] >> pi[i - 1] & 1:
                M.add((pi, i))
    assert len(M) == 2 * m * factorial(n - 1), "claim (1) fails"
    stats["eq1"] += 1

    def R(tree):
        out = set()
        for (pi, i) in M:
            S = 0
            for x in pi[:i]:
                S |= 1 << x
            if contains(adj, S, pi[0], tree, cache):
                out.add((pi, i))
        return out

    Rs = {}
    for t in range(2, n + 1):
        for tree in rooted_trees(t):
            Rs[tree] = R(tree)
    nf = factorial(n)
    for tree, RT in Rs.items():
        t = size(tree)
        assert len(M) <= len(RT) + (t - 2) * nf, ("claim (2) fails", n, edges, tree)
        stats["ineq2"] += 1
        if t < 3:
            continue
        if len(tree) == 1:
            # the root r is a leaf; T - r rooted at r' is tree[0]
            Rsub = Rs[tree[0]]
            assert len(Rsub) <= len(RT) + nf, ("Lemma 3 fails", n, edges, tree)
            stats["L3"] += 1
            # the map f of Lemma 3
            firsts = {}
            for (pi, i) in Rsub:
                if pi not in firsts or i < firsts[pi]:
                    firsts[pi] = i
            images = set()
            for (pi, i) in Rsub:
                if firsts[pi] == i:
                    continue
                img = (tuple(reversed(pi[:i])) + pi[i:], i)
                assert img in RT, ("Lemma 3: f leaves R(T, r)", n, edges, tree, pi, i)
                assert img not in images, ("Lemma 3: f not injective", n, edges, tree, pi, i)
                images.add(img)
                stats["L3_f"] += 1
        else:
            kids = list(tree)
            k = len(kids)
            seen_splits = set()
            for r_ in range(1, k):
                for A in combinations(range(k), r_):
                    T1 = tuple(sorted(kids[a] for a in A))
                    T2 = tuple(sorted(kids[b] for b in range(k) if b not in A))
                    if (T1, T2) in seen_splits:
                        continue
                    seen_splits.add((T1, T2))
                    R1, R2 = Rs[T1], Rs[T2]
                    assert RT <= R1 and R2 <= M
                    assert len(R1) + len(R2) <= len(M) + len(RT) + nf, ("Lemma 4 fails", n, edges, tree, T1, T2)
                    stats["L4"] += 1
                    D = R1 - RT
                    firsts = {}
                    for (pi, i) in D:
                        if pi not in firsts or i < firsts[pi]:
                            firsts[pi] = i
                    images = set()
                    for (pi, i) in D:
                        j = firsts[pi]
                        if j == i:
                            continue
                        img = ((pi[0],) + pi[j:i] + pi[1:j] + pi[i:], i - j + 1)
                        assert img in M, ("Lemma 4: f leaves M(G)", n, edges, tree, pi, i)
                        assert img not in R2, ("Lemma 4: f lands in R(T2, r)", n, edges, tree, pi, i)
                        assert img not in images, ("Lemma 4: f not injective", n, edges, tree, pi, i)
                        images.add(img)
                        stats["L4_f"] += 1


# ---------------------------------------------------------------- part B: counting
def counting(n, edges, stats, tmax=None):
    adj = adj_of(n, edges)
    m = len(edges)
    cache = {}
    nf = factorial(n)
    Msize = 2 * m * factorial(n - 1)
    # pairs (S, v1) -> number of v_i in S adjacent to v1, weight (|S|-2)! (n-|S|)!
    weights = []
    for S in range(1, 1 << n):
        s = bin(S).count("1")
        if s < 2:
            continue
        wgt = factorial(s - 2) * factorial(n - s)
        for v in range(n):
            if S >> v & 1:
                d = bin(adj[v] & S).count("1")
                if d:
                    weights.append((S, v, d * wgt))
    assert sum(w for _, _, w in weights) == Msize, "counting form of (1) fails"
    stats["eq1"] += 1
    tmax = tmax or n
    Rs = {}
    for t in range(2, tmax + 1):
        for tree in rooted_trees(t):
            Rs[tree] = sum(w for S, v, w in weights if contains(adj, S, v, tree, cache))
    full = (1 << n) - 1
    slack_min = None
    for tree, r in Rs.items():
        t = size(tree)
        slack = r + (t - 2) * nf - Msize
        assert slack >= 0, ("claim (2) fails", n, edges, tree)
        stats["ineq2"] += 1
        if slack_min is None or slack < slack_min:
            slack_min = slack
        if 2 * m > (t - 2) * n:
            assert any(contains(adj, full, v, tree, cache) for v in range(n)), ("theorem fails", n, edges, tree)
            stats["thm"] += 1
        if t < 3:
            continue
        if len(tree) == 1:
            assert Rs[tree[0]] <= r + nf, ("Lemma 3 fails", n, edges, tree)
            stats["L3"] += 1
        else:
            kids = list(tree)
            k = len(kids)
            seen = set()
            for r_ in range(1, k):
                for A in combinations(range(k), r_):
                    T1 = tuple(sorted(kids[a] for a in A))
                    T2 = tuple(sorted(kids[b] for b in range(k) if b not in A))
                    if (T1, T2) in seen:
                        continue
                    seen.add((T1, T2))
                    assert Rs[T1] + Rs[T2] <= Msize + r + nf, ("Lemma 4 fails", n, edges, tree, T1, T2)
                    stats["L4"] += 1
    return slack_min


def graphs_up_to_iso(n):
    pairs = [(a, b) for a in range(n) for b in range(a + 1, n)]
    idx = {p: k for k, p in enumerate(pairs)}
    perms = list(permutations(range(n)))
    maps = []
    for p in perms:
        maps.append([idx[tuple(sorted((p[a], p[b])))] for (a, b) in pairs])
    seen = bytearray(1 << len(pairs))
    reps = []
    for mask in range(1 << len(pairs)):
        if seen[mask]:
            continue
        reps.append([pairs[k] for k in range(len(pairs)) if mask >> k & 1])
        bits = [k for k in range(len(pairs)) if mask >> k & 1]
        for mp in maps:
            im = 0
            for k in bits:
                im |= 1 << mp[k]
            seen[im] = 1
    return reps


def main():
    print("rooted trees with t = 1..8 vertices: %s (OEIS A000081: 1, 1, 2, 4, 9, 20, 48, 115)" % [len(rooted_trees(t)) for t in range(1, 9)])
    stats = dict(eq1=0, ineq2=0, L3=0, L4=0, L3_f=0, L4_f=0, thm=0)
    ng = 0
    for n in (2, 3, 4):
        pairs = [(a, b) for a in range(n) for b in range(a + 1, n)]
        for mask in range(1 << len(pairs)):
            literal(n, [pairs[k] for k in range(len(pairs)) if mask >> k & 1], stats)
            ng += 1
    g5 = graphs_up_to_iso(5)
    for e in g5:
        literal(5, e, stats)
    print("A: %d labelled graphs on 2..4 vertices and %d graphs on 5 vertices (34 expected): (1) %d times, (2) %d, Lemma 3 %d, Lemma 4 %d; the map of Lemma 3 applied %d times and the map of Lemma 4 %d times, always into the stated set and injective" % (ng, len(g5), stats["eq1"], stats["ineq2"], stats["L3"], stats["L4"], stats["L3_f"], stats["L4_f"]))
    sys.stdout.flush()

    stats = dict(eq1=0, ineq2=0, L3=0, L4=0, L3_f=0, L4_f=0, thm=0)
    g6 = graphs_up_to_iso(6)
    tight = 0
    for e in g6:
        if counting(6, e, stats) == 0:
            tight += 1
    print("B: %d graphs on 6 vertices (156 expected): (2) checked %d times, Lemma 3 %d, Lemma 4 %d, theorem %d; graphs where (2) holds with equality for some rooted tree: %d" % (len(g6), stats["ineq2"], stats["L3"], stats["L4"], stats["thm"], tight))
    sys.stdout.flush()
    rng = random.Random(5)
    for n, cnt in ((7, 150), (8, 40)):
        stats = dict(eq1=0, ineq2=0, L3=0, L4=0, L3_f=0, L4_f=0, thm=0)
        pairs = [(a, b) for a in range(n) for b in range(a + 1, n)]
        for _ in range(cnt):
            p = rng.choice((0.25, 0.4, 0.5, 0.6, 0.75))
            counting(n, [e for e in pairs if rng.random() < p], stats)
        print("B: %d random graphs on %d vertices: (2) checked %d times, Lemma 3 %d, Lemma 4 %d, theorem %d" % (cnt, n, stats["ineq2"], stats["L3"], stats["L4"], stats["thm"]))
        sys.stdout.flush()
    # a control: the inequality with t-3 in place of t-2 must fail somewhere (K_{t-1} is extremal)
    n = 5
    pairs = [(a, b) for a in range(n) for b in range(a + 1, n)]
    adj = adj_of(n, pairs)
    cache = {}
    bad = 0
    for tree in rooted_trees(6):
        r = 0  # K_5 has no tree on 6 vertices
        if 2 * len(pairs) * factorial(n - 1) > r + (6 - 3) * factorial(n):
            bad += 1
    print("control: on K_5 with trees on 6 vertices, |M| = %d, (t-2) n! = %d (equality), (t-3) n! = %d; the weakened inequality fails for %d of %d rooted trees" % (2 * len(pairs) * factorial(n - 1), 4 * factorial(n), 3 * factorial(n), bad, len(rooted_trees(6))))
    print("all assertions passed")


if __name__ == "__main__":
    main()
