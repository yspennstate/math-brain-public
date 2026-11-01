from itertools import product


def closure_from_mask(n, mask):
    pairs = [(i, j) for i in range(n) for j in range(i + 1, n)]
    rel = [[False] * n for _ in range(n)]
    for k, (i, j) in enumerate(pairs):
        if (mask >> k) & 1:
            rel[i][j] = True
    for k in range(n):
        for i in range(n):
            if rel[i][k]:
                for j in range(n):
                    if rel[k][j]:
                        rel[i][j] = True
    return tuple(tuple(row) for row in rel)


def inc(rel, i, j):
    return not rel[i][j] and not rel[j][i]


def cover(rel, i, j):
    if not rel[i][j]:
        return False
    n = len(rel)
    return not any(rel[i][k] and rel[k][j] for k in range(n) if k not in (i, j))


print("POS3_TERMINAL_BLOCK_BARRIER_REGRESSION")
for n in range(2, 7):
    m = n * (n - 1) // 2
    closures = {closure_from_mask(n, mask) for mask in range(1 << m)}
    canonical = block_vertices = heavy_bridges = 0
    for rel in closures:
        q = next((j for j in range(1, n) if any(inc(rel, i, j) for i in range(j))), None)
        if q is None:
            continue
        canonical += 1
        # Minimal later endpoint forces the whole prefix to be a chain.
        for i in range(q):
            for j in range(i + 1, q):
                assert rel[i][j]
        p = min(i for i in range(q) if inc(rel, i, q))
        for i in range(p):
            assert rel[i][q]
        for s in range(p, q):
            assert inc(rel, s, q)
            block_vertices += 1
            # D(s,q)=empty for every vertex of the terminal incomparability block.
            for z in range(n):
                if cover(rel, z, q):
                    assert not inc(rel, z, s)
            # Structural part of the heavy-bridge barrier.  If s<.r and q||r
            # with s<*q<*r, every F4 blocker c<.r, c||q, c!=s must lie in
            # one of the two strict-subspan intervals.  A putative c<*s would
            # satisfy c<s<r and so could not cover r.
            for r in range(q + 1, n):
                if cover(rel, s, r) and inc(rel, q, r):
                    heavy_bridges += 1
                    for c in range(n):
                        if c != s and cover(rel, c, r) and inc(rel, c, q):
                            assert (s < c < q) or (q < c < r)
    print(n, len(closures), canonical, block_vertices, heavy_bridges)
print("POS3_TERMINAL_BLOCK_BARRIER_REGRESSION_PASS")
