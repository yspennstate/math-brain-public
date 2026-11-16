#!/usr/bin/env python3
"""Numerical companion to the paper: exact survival probabilities on small graphs
and Monte Carlo collision times on larger ones, compared with Theorem 1.2.

p_k(delta) is the probability that the non-backtracking walk started with the
directed edge delta is vertex-simple for k steps. Theorem 1.2 gives
p_k <= 256 Q (1+Q) n / k^2 with Q = M/(m-1). The script reports
  * on small graphs, the exact value of max_{delta,k} p_k k^2 / n;
  * on larger graphs, the mean first-collision time divided by sqrt(n), next to
    the bound 32 sqrt(Q(1+Q)) + 2/sqrt(n) of Corollary 1.4, and the empirical
    survival at lengths where the bound of Theorem 1.2 is below 1.
These checks are not part of the proof. Pure Python 3, no dependencies.
Usage: python code/check_bound.py  (writes data/bound_checks.json)
"""
import json
import math
import pathlib
import random
from collections import defaultdict

ROOT = pathlib.Path(__file__).resolve().parent.parent
rng = random.Random(20261113)


def random_graph(n, extra, max_deg):
    """Random Hamiltonian cycle plus a random perfect matching (minimum degree 3),
    then `extra` random edges added while both ends have degree < max_deg."""
    assert n % 2 == 0 and n >= 6
    while True:
        order = list(range(n))
        rng.shuffle(order)
        adj = [set() for _ in range(n)]
        for a, b in zip(order, order[1:] + order[:1]):
            adj[a].add(b)
            adj[b].add(a)
        rest = list(range(n))
        rng.shuffle(rest)
        ok = True
        while rest and ok:
            a = rest.pop()
            for t in range(len(rest)):
                b = rest[t]
                if b not in adj[a]:
                    rest.pop(t)
                    adj[a].add(b)
                    adj[b].add(a)
                    break
            else:
                ok = False
        if ok:
            break
    tries = 0
    while extra > 0 and tries < 50 * n:
        tries += 1
        a, b = rng.randrange(n), rng.randrange(n)
        if a != b and b not in adj[a] and len(adj[a]) < max_deg and len(adj[b]) < max_deg:
            adj[a].add(b)
            adj[b].add(a)
            extra -= 1
    return [sorted(s) for s in adj]


def params(adj):
    m = min(map(len, adj))
    big_m = max(map(len, adj))
    q = big_m / (m - 1)
    return m, big_m, q


def exact_survival(adj, start):
    """p_k for k = 1..n-1 by dynamic programming over (visited set, previous, current)."""
    u, v = start
    states = {(1 << u | 1 << v, u, v): 1.0}
    out = [1.0]
    while states:
        nxt = defaultdict(float)
        for (seen, prev, cur), mass in states.items():
            share = mass / (len(adj[cur]) - 1)
            for w in adj[cur]:
                if w != prev and not seen >> w & 1:
                    nxt[(seen | 1 << w, cur, w)] += share
        states = nxt
        if states:
            out.append(sum(states.values()))
    return out  # out[k-1] = p_k


def collision_time(adj, start):
    """First t >= 2 at which the walk revisits a vertex."""
    prev, cur = start
    seen = {prev, cur}
    t = 1
    while True:
        nb = adj[cur]
        while True:
            w = nb[rng.randrange(len(nb))]
            if w != prev:
                break
        t += 1
        if w in seen:
            return t
        seen.add(w)
        prev, cur = cur, w


FAMILIES = [("cubic", 0, 3), ("degrees 3-6", 1.0, 6), ("degrees 3-10", 2.5, 10)]

exact_rows = []
for n in (8, 10, 12):
    for name, extra_per_vertex, cap in FAMILIES:
        adj = random_graph(n, int(extra_per_vertex * n), cap)
        m, big_m, q = params(adj)
        worst = 0.0
        for a in range(n):
            for b in adj[a]:
                for k, p in enumerate(exact_survival(adj, (a, b)), start=1):
                    worst = max(worst, p * k * k / n)
        exact_rows.append({"n": n, "family": name, "m": m, "M": big_m, "Q": q,
                           "max_pk_k2_over_n": worst, "theorem_constant": 256 * q * (1 + q)})

mc_rows = []
for n in (2000, 20000):
    for name, extra_per_vertex, cap in FAMILIES:
        adj = random_graph(n, int(extra_per_vertex * n), cap)
        m, big_m, q = params(adj)
        h = 256 * q * (1 + q) * n
        times = []
        for _ in range(4):
            a = rng.randrange(n)
            start = (a, adj[a][rng.randrange(len(adj[a]))])
            times += [collision_time(adj, start) for _ in range(1000)]
        k_star = math.floor(math.sqrt(h)) + 1
        survivors = sum(t > k_star for t in times) if k_star < n else None
        mc_rows.append({"n": n, "family": name, "m": m, "M": big_m, "Q": q, "walks": len(times),
                        "mean_tau_over_sqrt_n": sum(times) / len(times) / math.sqrt(n),
                        "corollary_bound_over_sqrt_n": 32 * math.sqrt(q * (1 + q)) + 2 / math.sqrt(n),
                        "max_tau": max(times),
                        "first_k_with_bound_below_1": k_star if k_star < n else None,
                        "walks_simple_past_that_k": survivors})

out = {"seed": 20261113, "exact": exact_rows, "monte_carlo": mc_rows}
(ROOT / "data").mkdir(exist_ok=True)
(ROOT / "data" / "bound_checks.json").write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
for row in exact_rows + mc_rows:
    print(json.dumps(row))
