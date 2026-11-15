"""Independently verify depth-10 simulation output by breadth-first search."""
from collections import Counter, defaultdict, deque
import csv
import json
import os
from pathlib import Path
import random

if os.getpriority(os.PRIO_PROCESS, 0) < 10:
    os.nice(10 - os.getpriority(os.PRIO_PROCESS, 0))
ROOT = Path(__file__).resolve().parents[1]


def audit():
    with (ROOT / "data/simulation_summary.csv").open() as stream:
        rows = [r for r in csv.DictReader(stream) if r["depth"] == "10"]
    with (ROOT / "data/contacts_by_level.csv").open() as stream:
        saved_levels = {(int(r["seed"]), float(r["p"]), int(r["edge_level"])):
                        int(r["adjacency_edges"]) for r in csv.DictReader(stream) if r["depth"] == "10"}
    for row in rows:
        n = 2047
        p, seed = float(row["p"]), int(row["seed"])
        rng = random.Random(seed)
        adjacency = [[] for _ in range(n)]
        edges, depth = [], [0] * n
        for v in range(1, n):
            parent = (v - 1) // 2
            depth[v] = depth[parent] + 1
            neighbors = [parent]
            if parent > 0:
                neighbors.append((parent - 1) // 2)
            for u in neighbors:
                edges.append((v, u))
                if rng.random() < p:
                    adjacency[u].append(v)
                    adjacency[v].append(u)
        component = [-1] * n
        sizes = {}
        for root in range(n):
            if component[root] >= 0:
                continue
            component[root] = root
            queue = deque([root])
            count = 0
            while queue:
                u = queue.popleft()
                count += 1
                for v in adjacency[u]:
                    if component[v] < 0:
                        component[v] = root
                        queue.append(v)
            sizes[root] = count
        pair_counts, level_counts = Counter(), Counter()
        for v, u in edges:
            a, b = component[v], component[u]
            if a != b and sizes[a] >= 64 and sizes[b] >= 64:
                pair_counts[tuple(sorted((a, b)))] += 1
                level_counts[max(depth[v], depth[u])] += 1
        observed = dict(vertices=n, edges=len(edges), clusters=len(sizes),
                        large_clusters=sum(s >= 64 for s in sizes.values()),
                        largest_cluster=max(sizes.values()), adjacent_large_pairs=len(pair_counts),
                        large_pair_edges=sum(pair_counts.values()),
                        max_pair_edges=max(pair_counts.values(), default=0))
        for key, value in observed.items():
            assert value == int(row[key]), (seed, p, key, value, row[key])
        for level in range(11):
            assert level_counts[level] == saved_levels[seed, p, level]

    # Check the tracked-pair vertex-level data against its separate summary.
    with (ROOT / "data/anchored_levels.csv").open() as stream:
        aggregate = defaultdict(lambda: [0, 0, 0.0, 0.0])
        for r in csv.DictReader(stream):
            key = tuple(r[k] for k in ("seed", "p", "depth", "anchor_a", "anchor_b"))
            for i, k in enumerate(("touch_a", "touch_b", "weight_a", "weight_b")):
                aggregate[key][i] += float(r[k])
    with (ROOT / "data/anchored_pairs.csv").open() as stream:
        tracked = list(csv.DictReader(stream))
    for r in tracked:
        key = tuple(r[k] for k in ("seed", "p", "depth", "anchor_a", "anchor_b"))
        for i, k in enumerate(("touch_a", "touch_b", "weight_a", "weight_b")):
            assert aggregate[key][i] == float(r[k]), (key, k)
    result = dict(status="passed", independent_bfs_configurations=len(rows),
                  per_level_counts_checked=len(rows) * 11,
                  tracked_pair_rows_checked=len(tracked), nice=os.getpriority(os.PRIO_PROCESS, 0))
    (ROOT / "data/data_audit.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result))


if __name__ == "__main__":
    audit()
