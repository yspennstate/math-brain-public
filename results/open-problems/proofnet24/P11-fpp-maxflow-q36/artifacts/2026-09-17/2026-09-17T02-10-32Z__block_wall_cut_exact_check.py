#!/usr/bin/env python3
"""Exact finite checker for P11-I0062-LLOG-L-BLOCK-WALL-03.

It verifies the purely combinatorial finite core of the block/wall proof:
for small 3D lattice cylinders, for EVERY local source-side set in every
2x2x2 slab block (equivalently every local bottom/top cut induced by such a
set), the union of the local cuts, deterministic inter-block walls, and the
remainder-plane cut disconnects the global bottom from the global top.
It also exhaustively checks the deterministic wall-count inequality on a
finite parameter box.

No floating point arithmetic is used.
"""
from itertools import product
from collections import deque


def canon(a, b):
    return tuple(sorted((a, b)))


def all_edges(K, L, M):
    for x in range(K):
        for y in range(L):
            for z in range(M + 1):
                if x + 1 < K:
                    yield (x, y, z), (x + 1, y, z)
                if y + 1 < L:
                    yield (x, y, z), (x, y + 1, z)
                if z + 1 <= M:
                    yield (x, y, z), (x, y, z + 1)


def partition(K, L, n):
    rx, ry = K % n, L % n
    qx, qy = (K - rx) // n, (L - ry) // n
    blocks = []
    for i in range(qx):
        for j in range(qy):
            xs = tuple(range(rx + i * n, rx + (i + 1) * n))
            ys = tuple(range(ry + j * n, ry + (j + 1) * n))
            blocks.append((xs, ys))
    return rx, ry, qx, qy, blocks


def walls(K, L, H, n):
    rx, ry, qx, qy, _ = partition(K, L, n)
    xb = ([rx - 1] if rx > 0 and qx > 0 else []) + [rx + i * n - 1 for i in range(1, qx)]
    yb = ([ry - 1] if ry > 0 and qy > 0 else []) + [ry + j * n - 1 for j in range(1, qy)]
    W = set()
    for z in range(H + 1):
        for x in xb:
            for y in range(L):
                W.add(canon((x, y, z), (x + 1, y, z)))
        for y in yb:
            for x in range(K):
                W.add(canon((x, y, z), (x, y + 1, z)))
    return W


def remainder_plane(K, L, H, n):
    rx, ry, _, _, _ = partition(K, L, n)
    return {
        canon((x, y, H - 1), (x, y, H))
        for x in range(K) for y in range(L)
        if x < rx or y < ry
    }


def local_cut(xs, ys, H, mask):
    free = [(x, y, z) for x in xs for y in ys for z in range(1, H)]
    S = {(x, y, 0) for x in xs for y in ys}
    for j, v in enumerate(free):
        if (mask >> j) & 1:
            S.add(v)
    B = {(x, y, z) for x in xs for y in ys for z in range(H + 1)}
    cut = set()
    for u in B:
        x, y, z = u
        for dx, dy, dz in ((1, 0, 0), (0, 1, 0), (0, 0, 1)):
            v = (x + dx, y + dy, z + dz)
            if v in B and ((u in S) != (v in S)):
                cut.add(canon(u, v))
    return cut, len(free)


def bottom_top_disconnected(K, L, M, removed):
    adj = {}
    for a, b in all_edges(K, L, M):
        if canon(a, b) in removed:
            continue
        adj.setdefault(a, []).append(b)
        adj.setdefault(b, []).append(a)
    q = deque((x, y, 0) for x in range(K) for y in range(L))
    seen = set(q)
    while q:
        u = q.popleft()
        if u[2] == M:
            return False
        for v in adj.get(u, ()): 
            if v not in seen:
                seen.add(v)
                q.append(v)
    return True


def exhaustive_case(K, L, M, n, H):
    _, _, _, _, blocks = partition(K, L, n)
    W = walls(K, L, H, n)
    P = remainder_plane(K, L, H, n)
    mask_ranges = []
    for xs, ys in blocks:
        _, free_count = local_cut(xs, ys, H, 0)
        mask_ranges.append(range(1 << free_count))
    total = 1
    for R in mask_ranges:
        total *= len(R)
    checked = 0
    for masks in product(*mask_ranges):
        removed = set(W) | set(P)
        for (xs, ys), mask in zip(blocks, masks):
            cut, _ = local_cut(xs, ys, H, mask)
            removed |= cut
        assert bottom_top_disconnected(K, L, M, removed)
        checked += 1
    assert checked == total
    return checked


def check_wall_count_box():
    cases = 0
    for K in range(2, 16):
        for L in range(2, 16):
            for n in range(2, min(5, K, L) + 1):
                for H in range(1, 5):
                    _, _, qx, qy, _ = partition(K, L, n)
                    W = walls(K, L, H, n)
                    # At each z-level there are at most qx vertical x-boundary
                    # lines of L edges and qy y-boundary lines of K edges.
                    bound = (H + 1) * (qx * L + qy * K)
                    assert len(W) <= bound
                    # Since qx <= K/n and qy <= L/n:
                    assert bound * n <= 2 * (H + 1) * K * L
                    cases += 1
    return cases


if __name__ == "__main__":
    c1 = exhaustive_case(4, 4, 3, 2, 2)
    c2 = exhaustive_case(5, 4, 3, 2, 2)
    wc = check_wall_count_box()
    print("P11-I0062-LLOG-L-BLOCK-WALL-03 exact finite checker: PASS")
    print(f"all local-cut combinations, no remainder: {c1}")
    print(f"all local-cut combinations, with anchored remainder: {c2}")
    print(f"wall-count parameter cases: {wc}")
    print("floating_point_used = false")
    print("global_asymptotic_claim = proved_on_report_page_not_inferred_from_finite_checker")
