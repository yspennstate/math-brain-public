"""Exact finite-network audits for the grandparent-graph proof (stdlib only)."""
from fractions import Fraction as Q
import itertools
import json
import os
from pathlib import Path

if os.getpriority(os.PRIO_PROCESS, 0) < 10:
    os.nice(10 - os.getpriority(os.PRIO_PROCESS, 0))
ROOT = Path(__file__).resolve().parents[1]


def cone(b, depth, with_parent=False):
    count = (b ** (depth + 1) - 1) // (b - 1)
    parent = [-1] + [(v - 1) // b for v in range(1, count)]
    if with_parent:
        parent[0] = count
    edges = []
    for v in range(count):
        if parent[v] >= 0:
            edges.append((v, parent[v]))
        p = parent[v]
        gp = parent[p] if 0 <= p < count else -1
        if gp >= 0:
            edges.append((v, gp))
    return count + int(with_parent), edges, parent


def connected(n, edges, bits, u, v):
    labels = list(range(n))

    def find(x):
        while labels[x] != x:
            labels[x] = labels[labels[x]]
            x = labels[x]
        return x

    for bit, (a, b) in zip(bits, edges):
        if bit:
            a, b = find(a), find(b)
            labels[a] = b
    return find(u) == find(v)


def reliability(n, edges, probabilities, u, v):
    answer = Q(0)
    for bits in itertools.product((0, 1), repeat=len(edges)):
        if connected(n, edges, bits, u, v):
            mass = Q(1)
            for bit, p in zip(bits, probabilities):
                mass *= p if bit else 1 - p
            answer += mass
    return answer


def check():
    records = []
    # Enumerate all 2^13 configurations, independent of the recursive argument.
    for p in (Q(1, 5), Q(11, 20), Q(4, 5)):
        r = p
        for depth in range(3):
            n, edges, _ = cone(2, depth, True)
            exact = reliability(n, edges, [p] * len(edges), 0, n - 1)
            assert exact == r, (p, depth, exact, r)
            records.append({"test": "cone_terminal_reliability", "p": str(p),
                            "depth": depth, "edges": len(edges), "value": str(exact)})
            r = 1 - (1 - p) * (1 - p * r) ** 2

        # A nontrivial core {0,1,2,3,5}; omitted leaves 4,6 each give
        # an independent parallel edge with probability p^2.
        n, edges, _ = cone(2, 2)
        exact = reliability(n, edges, [p] * len(edges), 3, 5)
        core_edges = [(a, b) for a, b in edges if a in {0, 1, 2, 3, 5}
                      and b in {0, 1, 2, 3, 5}]
        reduced = reliability(n, core_edges + [(1, 0), (2, 0)],
                              [p] * len(core_edges) + [p * p] * 2, 3, 5)
        assert exact == reduced
        records.append({"test": "two_terminal_core_reduction", "p": str(p),
                        "full_edges": len(edges), "reduced_edges": len(core_edges) + 2,
                        "value": str(exact)})

    # Enumerate cone boundaries directly and check their claimed form and
    # disjointness; this is separate from the reliability calculations.
    for b in (2, 3, 4):
        n, edges, parent = cone(b, 8)
        spine = [0]
        for _ in range(8):
            spine.append(b * spine[-1] + 1)
        boundaries = []
        for t in spine[2:8]:
            descendants = set()
            queue = [t]
            while queue:
                x = queue.pop()
                descendants.add(x)
                queue.extend(y for y in range(b * x + 1, b * x + b + 1) if y < n)
            cut = {tuple(sorted((a, c))) for a, c in edges
                   if (a in descendants) != (c in descendants)}
            expected = {tuple(sorted((t, parent[t]))),
                        tuple(sorted((t, parent[parent[t]])))}
            expected.update(tuple(sorted((y, parent[t])))
                            for y in range(b * t + 1, b * t + b + 1))
            assert cut == expected and len(cut) == b + 2
            boundaries.append(cut)
        selected = boundaries[::3]
        assert all(a.isdisjoint(c) for a, c in itertools.combinations(selected, 2))
        records.append({"test": "boundary_enumeration", "b": b,
                        "cut_size": b + 2, "boundaries_checked": len(boundaries)})

    output = {"status": "passed", "exact_checks": records,
              "nice": os.getpriority(os.PRIO_PROCESS, 0), "threads": 1}
    (ROOT / "data").mkdir(exist_ok=True)
    (ROOT / "data/proof_checks.json").write_text(json.dumps(output, indent=2) + "\n")
    print(json.dumps({"status": "passed", "checks": len(records), "nice": output["nice"]}))


if __name__ == "__main__":
    check()
