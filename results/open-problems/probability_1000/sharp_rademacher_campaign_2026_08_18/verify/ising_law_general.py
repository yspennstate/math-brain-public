"""Extend the Ising law to triangles with THREE shared coordinates - the gap in my own statement.

Proved earlier today for <=2 shared coordinates per triangle:
    |A| / (2^r (3/4)^k) = SUM over even subgraphs S of (-1/3)^{|S|}
because a 1-private triangle {u,v,a} integrates to (3/2)(1 - x_u x_v/3): ONE Ising edge.

A 0-private triangle {u,v,w} has no private coordinate to integrate out; its weight is the NAE
indicator itself. For +-1 variables all-equal happens iff uv = 1 and vw = 1, so

    [all equal] = (1+uv)(1+vw)/4 = (1 + uv + vw + uw)/4     (using uv*vw = uw)
    NAE weight  = 1 - that = (3 - uv - vw - uw)/4 = (3/4)(1 - (uv + vw + uw)/3).

So it still carries the independence factor 3/4, and its residual term offers a CHOICE of any ONE of
its three edges at weight -1/3 (or nothing). PREDICTION:

    Z = SUM over selections S of (-1/3)^{|S|},
    where each triangle contributes AT MOST ONE edge - its unique shared pair if it has two shared
    coordinates, or any one of its three pairs if it has three - and the selected multiset of edges
    must make every vertex even.

That is a strictly larger sum than the plain cycle space: a 3-shared triangle is a vertex of degree
three in the hypergraph but supplies only one edge at a time.

This tests the prediction against exact brute force on systems containing 3-shared triangles.
A single exact mismatch kills it.
"""
import itertools
import math

BETA = math.log2(4.0 / 3.0)


def fibre_size(r, T):
    n = 0
    for s in itertools.product((0, 1), repeat=r):
        if all(not (s[a] == s[b] == s[c]) for (a, b, c) in T):
            n += 1
    return n


def is_linear(T):
    return all(len(set(x) & set(y)) < 2 for x, y in itertools.combinations(T, 2))


def Z_general(T):
    cnt = {}
    for t in T:
        for x in t:
            cnt[x] = cnt.get(x, 0) + 1
    sh = {x for x in cnt if cnt[x] >= 2}
    # options per triangle: list of edges it may contribute (or None)
    opts = []
    for t in T:
        s = [x for x in t if x in sh]
        if len(s) <= 1:
            opts.append([None])
        elif len(s) == 2:
            opts.append([None, tuple(sorted(s))])
        else:
            opts.append([None] + [tuple(sorted(p)) for p in itertools.combinations(s, 2)])
    if len(opts) > 14:
        return None
    verts = sorted(sh)
    idx = {v: i for i, v in enumerate(verts)}
    total = 0.0
    for choice in itertools.product(*opts):
        deg = [0] * len(verts)
        ne = 0
        for e in choice:
            if e is None:
                continue
            deg[idx[e[0]]] += 1
            deg[idx[e[1]]] += 1
            ne += 1
        if all(d % 2 == 0 for d in deg):
            total += (-1.0 / 3.0) ** ne
    return total


def check(name, T):
    lab = {x: i for i, x in enumerate(sorted({x for t in T for x in t}))}
    T2 = [tuple(lab[x] for x in t) for t in T]
    r, k = len(lab), len(T2)
    if not is_linear(T2):
        print("  %-30s NOT LINEAR - skipped" % name)
        return None
    if r > 20:
        print("  %-30s r=%d too big" % (name, r))
        return None
    pred = Z_general(T2)
    if pred is None:
        print("  %-30s too many triangles for the enumerator" % name)
        return None
    n = fibre_size(r, T2)
    ratio = n / ((2.0 ** r) * (0.75 ** k))
    ok = abs(ratio - pred) < 1e-9
    nsh3 = sum(1 for t in T2 if sum(1 for x in t if sum(1 for u in T2 if x in u) >= 2) == 3)
    print("  %-30s k=%-2d r=%-3d 3sh=%d |A|=%-6d ratio=%.9f pred=%.9f  %s"
          % (name, k, r, nsh3, n, ratio, pred, "MATCH" if ok else "*** MISMATCH ***"))
    return ok


res = []
print("# controls: no 3-shared triangles (the law is already proved here)")
res.append(check("pure 4-cycle", [(i, (i + 1) % 4, 10 + i) for i in range(4)]))
res.append(check("pure 5-cycle", [(i, (i + 1) % 5, 10 + i) for i in range(5)]))

print()
print("# ATTACK: systems containing 3-shared-coordinate triangles")
# a central triangle all of whose coordinates are shared with three outer triangles
T = [(0, 1, 2)]                      # central, will become 3-shared
T += [(0, 10, 11), (1, 12, 13), (2, 14, 15)]
res.append(check("central + 3 pendants", T))

# central 3-shared triangle inside a cycle structure
T = [(0, 1, 2), (0, 1, 20)]          # shares TWO coords -> not linear; expect skip
res.append(check("two triangles sharing 2 (illegal)", T))

# central triangle whose three coords each sit on a path back to each other
T = [(0, 1, 2)]
T += [(0, 3, 30), (1, 3, 31)]        # 0-3-1 path: makes a cycle with the central via edge (0,1)
res.append(check("central 3-shared + one loop", T))

T = [(0, 1, 2)]
T += [(0, 3, 30), (1, 3, 31), (1, 4, 32), (2, 4, 33)]
res.append(check("central 3-shared + two loops", T))

# two 3-shared triangles joined
T = [(0, 1, 2), (3, 4, 5)]
T += [(0, 3, 30), (1, 4, 31), (2, 5, 32)]
res.append(check("prism: two 3-shared + 3 rungs", T))

# 3-shared triangle with all three coords on a common 4-cycle
T = [(0, 1, 2)]
T += [(0, 5, 40), (5, 1, 41), (1, 6, 42), (6, 2, 43)]
res.append(check("3-shared + two 4-cycles", T))

print()
good = [x for x in res if x is not None]
print("matched %d of %d" % (sum(1 for x in good if x), len(good)))
