"""Brute-force check of the two combinatorial claims behind Theorem 4:
 (a) layer(v) = second largest branch height at v  (branch height counted with one vertex = 1);
 (b) max layer = floor(diam/2)  and  max layer <= height from the root.
Leaf stripping is done literally: remove every degree-<=1 vertex, repeat.
"""
import numpy as np, sys
from collections import deque

rng = np.random.default_rng(7)

def rrt(n):
    par = np.zeros(n, dtype=int); par[0] = -1
    for i in range(1, n):
        par[i] = rng.integers(0, i)
    adj = [[] for _ in range(n)]
    for i in range(1, n):
        adj[i].append(par[i]); adj[par[i]].append(i)
    return par, adj

def layers(n, adj):
    """layer(v) = number of strip rounds after which v is a leaf (degree <= 1); leaves are 0."""
    deg = np.array([len(a) for a in adj])
    alive = np.ones(n, dtype=bool)
    lay = np.full(n, -1)
    t = 0
    while alive.any():
        leaves = [v for v in range(n) if alive[v] and deg[v] <= 1]
        for v in leaves:
            if lay[v] < 0: lay[v] = t
        if not leaves: break
        for v in leaves:
            alive[v] = False
            for u in adj[v]:
                if alive[u]: deg[u] -= 1
        t += 1
    return lay

def bfs(n, adj, src):
    d = np.full(n, -1); d[src] = 0; q = deque([src])
    while q:
        v = q.popleft()
        for u in adj[v]:
            if d[u] < 0: d[u] = d[v] + 1; q.append(u)
    return d

def branch_second(n, adj, v):
    """second largest branch height at v, one vertex = height 1"""
    hs = []
    for u in adj[v]:
        # height of the component of u in T - v
        d = np.full(n, -1); d[v] = 0; d[u] = 1; q = deque([u]); h = 1
        while q:
            w = q.popleft()
            for z in adj[w]:
                if d[z] < 0: d[z] = d[w] + 1; q.append(z); h = max(h, d[z])
        hs.append(h)
    hs.sort(reverse=True)
    return hs[1] if len(hs) > 1 else 0

bad_a = bad_b = 0
for trial in range(int(sys.argv[1]) if len(sys.argv) > 1 else 40):
    n = int(rng.integers(6, 120))
    par, adj = rrt(n)
    lay = layers(n, adj)
    # (a) on a sample of vertices
    for v in rng.choice(n, size=min(n, 12), replace=False):
        if lay[v] != branch_second(n, adj, int(v)): bad_a += 1
    # (b) diameter and height
    d0 = bfs(n, adj, 0); a = int(np.argmax(d0)); da = bfs(n, adj, a)
    diam = int(da.max()); height = int(d0.max()); L = int(lay.max())
    if L != diam // 2 or L > height:
        bad_b += 1
        print(f"  n={n} L={L} diam={diam} floor(diam/2)={diam//2} height={height}")
print(f"claim (a) layer = second branch height: {bad_a} failures")
print(f"claim (b) max layer = floor(diam/2) and <= height: {bad_b} failures")
# a deliberate negative control: the claim should FAIL if we use the LARGEST branch height
n = 60; par, adj = rrt(n); lay = layers(n, adj)
worst = sum(1 for v in range(n) if lay[v] == max([1] + [0]))
print("negative control - on a path of 5 vertices the max layer must be 2, not 4:")
adjp = [[1],[0,2],[1,3],[2,4],[3]]
print("  computed:", int(layers(5, adjp).max()), " (path P5: diam 4, floor(diam/2) = 2)")
