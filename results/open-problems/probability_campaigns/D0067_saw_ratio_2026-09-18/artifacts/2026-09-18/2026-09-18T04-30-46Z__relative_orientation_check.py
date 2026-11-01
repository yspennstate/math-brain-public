#!/usr/bin/env python3
"""Exact finite sanity checks for D0067 run 5.

The run report proves the all-k/all-relative-orientation statement on the page.
This executable checks representative integer instances only:
  * T_k is a self-avoiding trapping pattern;
  * all eight D4 images are distinct;
  * the family {g T_k} is prefix-free for k<=K;
  * for every relative D4 orientation q and k<=K_COMPAT, explicit translated
    two-end pairs admit a self-avoiding connector for two opposite root parities;
  * the resulting concatenated walks really contain the requested patterns at
    both ends and have D_0=D_+=0.

No asymptotic Madras constant is estimated here.
"""
from collections import deque

K_PREFIX = 20
K_COMPAT = 8

D4 = {
    "I":    lambda x, y: ( x,  y),
    "R90":  lambda x, y: (-y,  x),
    "R180": lambda x, y: (-x, -y),
    "R270": lambda x, y: ( y, -x),
    "MX":   lambda x, y: ( x, -y),
    "MY":   lambda x, y: (-x,  y),
    "MD":   lambda x, y: ( y,  x),
    "MA":   lambda x, y: (-y, -x),
}
DIRS = ((1,0),(-1,0),(0,1),(0,-1))


def trap(k):
    p = [(0, 0)]
    p += [(x, 0) for x in range(1, k + 1)]
    p += [(k, 1)]
    p += [(x, 1) for x in range(k - 1, -1, -1)]
    p += [(-1, 1), (-1, 0), (-1, -1), (0, -1)]
    return p


def act(path, name):
    f = D4[name]
    return [f(x, y) for x, y in path]


def shift(path, v):
    a, b = v
    return [(x + a, y + b) for x, y in path]


def adjacency_path(path):
    return all(abs(x-x2) + abs(y-y2) == 1 for (x,y),(x2,y2) in zip(path, path[1:]))


def free_degree_at_endpoint(path, endpoint_index):
    occupied = set(path)
    x, y = path[endpoint_index]
    return sum((x+dx, y+dy) not in occupied for dx,dy in DIRS)


def bfs_connector(start, target, blocked, bound):
    blocked = set(blocked) - {start, target}
    q = deque([start])
    prev = {start: None}
    while q:
        v = q.popleft()
        if v == target:
            out = []
            while v is not None:
                out.append(v)
                v = prev[v]
            return out[::-1]
        x, y = v
        for dx, dy in DIRS:
            w = (x + dx, y + dy)
            if abs(w[0]) > bound or abs(w[1]) > bound:
                continue
            if w in blocked or w in prev:
                continue
            prev[w] = v
            q.append(w)
    return None


# Basic trapping geometry.
for k in range(1, K_PREFIX + 1):
    p = trap(k)
    assert adjacency_path(p)
    assert len(p) == len(set(p))
    assert len(p) - 1 == 2*k + 5
    assert {(1,0),(-1,0),(0,1),(0,-1)} <= set(p)
    imgs = {tuple(act(p, g)) for g in D4}
    assert len(imgs) == 8

# Prefix-freeness of all checked oriented patterns.
patterns = []
for k in range(1, K_PREFIX + 1):
    for g in D4:
        patterns.append((k, g, act(trap(k), g)))
for i, (k, g, p) in enumerate(patterns):
    for k2, g2, q in patterns[i+1:]:
        m = min(len(p), len(q))
        assert p[:m] != q[:m], ("prefix collision", k, g, k2, g2)

# Representative two-end compatibility for every relative orientation.
# Fix the starting orientation to I; global D4 symmetry supplies the other 8.
# Two adjacent terminal-root x-coordinates test opposite checkerboard parities.
compat_cases = 0
for k in range(1, K_COMPAT + 1):
    start_pattern = trap(k)
    for rel in D4:
        terminal_pattern_local = act(trap(k), rel)
        for parity_shift in (0, 1):
            M = 8*k + 30 + parity_shift
            root = (M, 0)
            terminal_forward = list(reversed(shift(terminal_pattern_local, root)))
            start_tip = start_pattern[-1]
            terminal_tip = terminal_forward[0]
            blocked = set(start_pattern[:-1]) | set(terminal_forward[1:])
            connector = bfs_connector(start_tip, terminal_tip, blocked, bound=12*k + 80)
            assert connector is not None, (k, rel, parity_shift)
            full = start_pattern + connector[1:-1] + terminal_forward
            assert adjacency_path(full)
            assert len(full) == len(set(full)), ("self-intersection", k, rel, parity_shift)
            assert full[:len(start_pattern)] == start_pattern
            terminal_read_back = [
                (x-root[0], y-root[1]) for x,y in reversed(full[-len(terminal_pattern_local):])
            ]
            assert terminal_read_back == terminal_pattern_local
            assert free_degree_at_endpoint(full, 0) == 0
            assert free_degree_at_endpoint(full, -1) == 0
            compat_cases += 1

print(f"PASS basic trapping/orbit checks for k=1..{K_PREFIX}")
print(f"PASS prefix-free D4 family for {8*K_PREFIX} checked patterns")
print(f"PASS two-end compatibility for {compat_cases} representative (k,relative-orientation,parity) cases")
print("PASS endpoint free degrees D_0=D_+=0 in every compatibility case")
print("NOTE: all-k compatibility and positive Madras frequencies are proved in the report, not inferred from this finite checker")
