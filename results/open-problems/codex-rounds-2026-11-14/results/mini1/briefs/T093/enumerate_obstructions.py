#!/usr/bin/env python3
"""Exact small-obstruction census; standard library only, one thread."""
import itertools as it
import json
import math
import os
from pathlib import Path
import resource
import time

LIMIT_STATUS = []
for kind, bound in [(resource.RLIMIT_DATA, 768 * 1024**2), (resource.RLIMIT_CPU, 1140)]:
    try:
        soft, hard = resource.getrlimit(kind)
        resource.setrlimit(kind, (min(soft, bound), hard))
        LIMIT_STATUS.append([kind, 'soft limit set'])
    except (ValueError, OSError) as error:
        LIMIT_STATUS.append([kind, str(error)])
assert os.environ.get('OMP_NUM_THREADS') == '1'
assert os.getpriority(os.PRIO_PROCESS, 0) >= 15
START = time.monotonic()


def graphs(n, m):
    """Choose each vertex's later neighbours; no duplicate labelled graphs."""
    adj = [0] * n
    degree = [0] * n

    def visit(i, left):
        if time.monotonic() - START > 1100:
            raise TimeoutError('wall-time limit')
        if resource.getrusage(resource.RUSAGE_SELF).ru_maxrss >= 768 * 1024**2:
            raise MemoryError('RSS limit')
        if i == n:
            if left == 0:
                yield tuple(adj)
            return
        if left < 0 or 2 * left < sum(max(0, 3 - degree[j]) for j in range(i, n)):
            return
        available = list(range(i + 1, n))
        lo = max(0, 3 - degree[i], left - math.comb(n - i - 1, 2))
        hi = min(len(available), left)
        for k in range(lo, hi + 1):
            for neighbours in it.combinations(available, k):
                for j in neighbours:
                    adj[i] |= 1 << j
                    adj[j] |= 1 << i
                    degree[j] += 1
                if all(degree[j] + n - i - 2 >= 3 for j in available):
                    yield from visit(i + 1, left - k)
                for j in neighbours:
                    adj[i] ^= 1 << j
                    adj[j] ^= 1 << i
                    degree[j] -= 1

    yield from visit(0, m)


def colourable(adj, deleted=None):
    n = len(adj)
    colours = [-1] * n
    active = [v for v in range(n) if v != deleted]
    order = sorted(active, key=lambda v: -adj[v].bit_count())

    def visit(i, used):
        if i == len(order):
            return True
        v = order[i]
        forbidden = {colours[u] for u in active if adj[v] >> u & 1}
        for colour in range(min(3, used + 1)):
            if colour not in forbidden:
                colours[v] = colour
                if visit(i + 1, max(used, colour + 1)):
                    return True
        colours[v] = -1
        return False

    return visit(0, 0)


def has_k4(adj):
    return any(all(adj[a] >> b & 1 for a, b in it.combinations(vs, 2))
               for vs in it.combinations(range(len(adj)), 4))


def edge_list(adj):
    return [[i, j] for i in range(len(adj)) for j in range(i + 1, len(adj))
            if adj[i] >> j & 1]


def orbit(adj):
    n = len(adj)
    edges = edge_list(adj)
    pairs = list(it.combinations(range(n), 2))
    index = {e: i for i, e in enumerate(pairs)}
    masks = set()
    for perm in it.permutations(range(n)):
        mask = 0
        for i, j in edges:
            e = tuple(sorted((perm[i], perm[j])))
            mask |= 1 << index[e]
        masks.add(mask)
    return masks


def main():
    rows = []
    representatives = []
    for n in range(4, 9):
        for m in range((3 * n + 1) // 2, min(n + 4, math.comb(n, 2)) + 1):
            count = k4free = noncolourable = 0
            bad = []
            for adj in graphs(n, m):
                count += 1
                if has_k4(adj):
                    continue
                k4free += 1
                if not colourable(adj):
                    noncolourable += 1
                    assert all(colourable(adj, v) for v in range(n))
                    bad.append(adj)
            row = dict(n=n, m=m, min_degree_3=count, k4free=k4free,
                       k4free_non3colourable=noncolourable)
            rows.append(row)
            print(json.dumps(row), flush=True)
            if bad:
                masks = orbit(bad[0])
                pairs = list(it.combinations(range(n), 2))
                actual = {sum(1 << i for i, (a, b) in enumerate(pairs)
                              if adj[a] >> b & 1) for adj in bad}
                assert actual == masks, 'more than one isomorphism class'
                representative = dict(n=n, m=m, edges=edge_list(bad[0]),
                                      labelled_count=len(masks),
                                      automorphisms=math.factorial(n)//len(masks))
                representatives.append(representative)
                print('representative', json.dumps(representative), flush=True)
    data = dict(rows=rows, representatives=representatives,
                nice=os.getpriority(os.PRIO_PROCESS, 0),
                peak_rss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
                limit_status=LIMIT_STATUS,
                seconds=round(time.monotonic()-START, 3))
    Path('obstructions.json').write_text(json.dumps(data, indent=2) + '\n')
    print('PASS: census, vertex-criticality, and permutation orbits')
    print('seconds', data['seconds'])


if __name__ == '__main__':
    main()
