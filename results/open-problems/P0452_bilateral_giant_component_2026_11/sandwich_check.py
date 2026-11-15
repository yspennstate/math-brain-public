# heeded:crlf_cross_os_parse local-only script, not copied to another OS
# Brute-force test of F_k(G(t)) <= F_k(G) <= F_k(G(t)) + |W| + (k-1) b + 2(k-1)|E_1| on random small instances,
# and of E b <= n B |W| / (n-1) by averaging.   usage: python sandwich_check.py [trials]
import random, sys

def comps(n, edges):
    p = list(range(n))
    def f(x):
        while p[x] != x:
            p[x] = p[p[x]]; x = p[x]
        return x
    for a, b in edges:
        p[f(a)] = f(b)
    size = {}
    for v in range(n):
        r = f(v); size[r] = size.get(r, 0) + 1
    return [size[f(v)] for v in range(n)]

def Fk(n, edges, k):
    return sum(1 for s in comps(n, edges) if s >= k)

rng = random.Random(4522026)
trials = int(sys.argv[1]) if len(sys.argv) > 1 else 4000
bad = 0; sb = 0.0; sbound = 0.0; tight = 0
for T in range(trials):
    n = rng.randint(5, 14)
    B = rng.randint(1, 3)
    d = [rng.choice([1, 1, 2, 2, 3, 4, 6, n - 2]) for _ in range(n)]
    d = [max(1, min(x, n - 2)) for x in d]
    t = rng.choice([0.3, 1.0, 2.0, 4.0]) * n      # cost scale: exponential of mean n
    cost = {}
    for i in range(n):
        for j in range(i + 1, n):
            cost[(i, j)] = rng.expovariate(1.0 / n)
    pref = []
    for i in range(n):
        inc = sorted(((cost[(min(i, j), max(i, j))], j) for j in range(n) if j != i))
        pref.append({j for _, j in inc[:d[i]]})
    G = [(i, j) for (i, j) in cost if j in pref[i] and i in pref[j]]
    Gt = [e for e in G if cost[e] <= t]
    W = {i for i in range(n) if d[i] > B}
    b = sum(1 for (i, j) in G if (i in W) != (j in W))
    E1 = [e for e in G if cost[e] > t and e[0] not in W and e[1] not in W]
    sb += b; sbound += n * B * len(W) / (n - 1)
    for k in range(1, 7):
        lo = Fk(n, Gt, k); mid = Fk(n, G, k)
        hi = lo + len(W) + (k - 1) * b + 2 * (k - 1) * len(E1)
        if not (lo <= mid <= hi):
            bad += 1
            print('VIOLATION', n, B, d, k, lo, mid, hi)
        if mid == hi and mid > lo:
            tight += 1
print('trials', trials, 'violations', bad, 'cases with equality on the right', tight)
print('mean b', round(sb / trials, 4), 'mean of bound nB|W|/(n-1)', round(sbound / trials, 4))
