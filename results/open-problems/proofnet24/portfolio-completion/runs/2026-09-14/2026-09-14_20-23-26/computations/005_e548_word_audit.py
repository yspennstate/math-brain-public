"""Exact integer audit of the rooted-word inequality in E548_port.lean.

No Lean kernel validation is performed. A failure is a mathematical
counterexample to the displayed intermediate inequality, not to Erdos--Sos.
Only Python's standard library is used.
"""
from itertools import permutations
from math import factorial
import json
import random


def rooted_counts(n, host_edges, t, tree_edges):
    adj = [[False] * n for _ in range(n)]
    for u, v in host_edges:
        adj[u][v] = adj[v][u] = True
    images = [[False] * (1 << n) for _ in range(t * n)]
    for f in permutations(range(n), t):
        if all(adj[f[u]][f[v]] for u, v in tree_edges):
            mask = sum(1 << v for v in f)
            for r, b in enumerate(f):
                images[r * n + b][mask] = True
    # Superset closure: a support qualifies iff it contains an image.
    for a in images:
        for bit in range(n):
            for mask in range(1 << n):
                if mask & (1 << bit) and a[mask ^ (1 << bit)]:
                    a[mask] = True
    out = []
    for r in range(t):
        total = 0
        for b in range(n):
            for mask in range(1 << n):
                if mask & (1 << b) or not images[r * n + b][mask | (1 << b)]:
                    continue
                k = mask.bit_count()
                if not k:
                    continue
                marked = sum(adj[b][v] for v in range(n) if mask & (1 << v))
                total += marked * factorial(k - 1) * factorial(n - 1 - k)
        out.append(total)
    return out


def audit(n, host_edges, t, tree_edges):
    base = 2 * len(host_edges) * factorial(n - 1)
    counts = rooted_counts(n, host_edges, t, tree_edges)
    allowance = (t - 2) * factorial(n)
    for root, count in enumerate(counts):
        if base > count + allowance:
            return dict(n=n, host_edges=host_edges, t=t, tree_edges=tree_edges,
                        root=root, base=base, rooted=count,
                        allowance=allowance, excess=base-count-allowance)
    return None


def run():
    rng = random.Random(548005)
    checked = 0
    for n in range(3, 9):
        for trial in range(250):
            t = rng.randrange(3, n + 1)
            tree = [(v, rng.randrange(v)) for v in range(1, t)]
            p = rng.uniform(0.1, 0.9)
            host = [(u, v) for u in range(n) for v in range(u + 1, n)
                    if rng.random() < p]
            result = audit(n, host, t, tree)
            checked += 1
            if result:
                print(json.dumps(dict(status="COUNTEREXAMPLE", checked=checked,
                                      witness=result), indent=2))
                return
    print(json.dumps(dict(status="NO_COUNTEREXAMPLE_IN_BOUNDED_SEARCH", checked=checked)))


if __name__ == "__main__":
    run()
