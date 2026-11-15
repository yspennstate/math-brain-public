"""Finite binary grandparent cones; counts are evidence, never infinite clusters.

Nested depths and increasing p share edge labels. Large means >=64 vertices.
Uses one thread, no numerical libraries, and preserves inherited nice >=10.
"""
import csv
import json
import os
from pathlib import Path
import random
import resource
import sys
import time
from collections import Counter, defaultdict

if os.getpriority(os.PRIO_PROCESS, 0) < 10:
    os.nice(10 - os.getpriority(os.PRIO_PROCESS, 0))
ROOT = Path(__file__).resolve().parents[1]
DEPTHS = (10, 12, 14)
PARAMETERS = (0.55, 0.65, 0.75)
REPLICATES = 12
MIN_SIZE = 64


class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n
        self.minimum = list(range(n))

    def find(self, v):
        while self.parent[v] != v:
            self.parent[v] = self.parent[self.parent[v]]
            v = self.parent[v]
        return v

    def union(self, u, v):
        u, v = self.find(u), self.find(v)
        if u == v:
            return
        if self.size[u] < self.size[v]:
            u, v = v, u
        self.parent[v] = u
        self.size[u] += self.size[v]
        self.minimum[u] = min(self.minimum[u], self.minimum[v])


def write_csv(name, rows):
    with (ROOT / "data" / name).open("w", newline="") as out:
        writer = csv.DictWriter(out, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def graph(depth):
    n = 2 ** (depth + 1) - 1
    edges = []
    for v in range(1, n):
        parent = (v - 1) // 2
        edges.append((v, parent))
        if parent:
            edges.append((v, (parent - 1) // 2))
    assert len(edges) == 2 * n - 4
    return n, edges


def run():
    started = time.monotonic()
    nmax, edges = graph(max(DEPTHS))
    summaries, levels, pair_rows, anchored, anchored_levels = [], [], [], [], []
    for replicate in range(REPLICATES):
        seed = 159000 + replicate
        rng = random.Random(seed)
        labels = [rng.random() for _ in edges]
        for p in PARAMETERS:
            anchors = None
            for depth in DEPTHS:
                n = 2 ** (depth + 1) - 1
                edge_count = 2 * n - 4
                dsu = DSU(n)
                for i in range(edge_count):
                    if labels[i] < p:
                        dsu.union(*edges[i])
                roots = [dsu.find(v) for v in range(n)]
                canonical = {r: dsu.minimum[r] for r in set(roots)}
                sizes = {canonical[r]: dsu.size[r] for r in canonical}
                cluster = [canonical[r] for r in roots]
                contacts = defaultdict(list)
                for u, v in edges[:edge_count]:
                    a, b = cluster[u], cluster[v]
                    if a != b and sizes[a] >= MIN_SIZE and sizes[b] >= MIN_SIZE:
                        if a > b:
                            a, b, u, v = b, a, v, u
                        contacts[a, b].append((u, v))
                per_level = defaultdict(lambda: {"edges": 0, "a": set(), "b": set(), "pairs": set()})
                for (a, b), touching_edges in sorted(contacts.items()):
                    av = {u for u, _ in touching_edges}
                    bv = {v for _, v in touching_edges}
                    counts = Counter(max((u + 1).bit_length() - 1, (v + 1).bit_length() - 1)
                                     for u, v in touching_edges)
                    pair_rows.append(dict(seed=seed, p=p, depth=depth, anchor_a=a, anchor_b=b,
                                          size_a=sizes[a], size_b=sizes[b],
                                          adjacency_edges=len(touching_edges), touch_a=len(av), touch_b=len(bv),
                                          weight_a=sum(2.0 ** (-((u + 1).bit_length() - 1)) for u in av),
                                          weight_b=sum(2.0 ** (-((v + 1).bit_length() - 1)) for v in bv),
                                          min_edge_level=min(counts), max_edge_level=max(counts)))
                    for u, v in touching_edges:
                        level = max((u + 1).bit_length() - 1, (v + 1).bit_length() - 1)
                        item = per_level[level]
                        item["edges"] += 1
                        item["a"].add((a, b, u))
                        item["b"].add((a, b, v))
                        item["pairs"].add((a, b))
                for level in range(depth + 1):
                    item = per_level[level]
                    levels.append(dict(seed=seed, p=p, depth=depth, edge_level=level,
                                       vertices_at_level=2 ** level, adjacency_edges=item["edges"],
                                       pair_touch_a=len(item["a"]), pair_touch_b=len(item["b"]),
                                       distinct_pairs=len(item["pairs"])))

                if depth == DEPTHS[0] and contacts:
                    anchors = max(sorted(contacts), key=lambda pair: len(contacts[pair]))
                if anchors is not None:
                    a, b = (cluster[x] for x in anchors)
                    if a == b:
                        status, ae, av, bv = "merged_in_window", [], set(), set()
                    else:
                        status = "distinct_in_window"
                        ae = contacts[tuple(sorted((a, b)))]
                        if a > b:
                            ae = [(v, u) for u, v in ae]
                        av, bv = {u for u, _ in ae}, {v for _, v in ae}
                    anchored.append(dict(seed=seed, p=p, depth=depth, anchor_a=anchors[0],
                                         anchor_b=anchors[1], status=status, size_a=sizes[a], size_b=sizes[b],
                                         adjacency_edges=len(ae), touch_a=len(av), touch_b=len(bv),
                                         weight_a=sum(2.0 ** (-((u + 1).bit_length() - 1)) for u in av),
                                         weight_b=sum(2.0 ** (-((v + 1).bit_length() - 1)) for v in bv)))
                    for level in range(depth + 1):
                        at = {u for u in av if (u + 1).bit_length() - 1 == level}
                        bt = {v for v in bv if (v + 1).bit_length() - 1 == level}
                        anchored_levels.append(dict(seed=seed, p=p, depth=depth, level=level,
                                                    anchor_a=anchors[0], anchor_b=anchors[1], status=status,
                                                    touch_a=len(at), touch_b=len(bt),
                                                    weight_a=len(at) * 2.0 ** -level,
                                                    weight_b=len(bt) * 2.0 ** -level))

                summaries.append(dict(seed=seed, p=p, depth=depth, vertices=n, edges=edge_count,
                                      clusters=len(sizes), large_clusters=sum(s >= MIN_SIZE for s in sizes.values()),
                                      largest_cluster=max(sizes.values()), adjacent_large_pairs=len(contacts),
                                      large_pair_edges=sum(len(x) for x in contacts.values()),
                                      max_pair_edges=max(map(len, contacts.values()), default=0)))

    (ROOT / "data").mkdir(exist_ok=True)
    for name, rows in (("simulation_summary.csv", summaries), ("contacts_by_level.csv", levels),
                       ("cluster_pairs.csv", pair_rows), ("anchored_pairs.csv", anchored),
                       ("anchored_levels.csv", anchored_levels)):
        write_csv(name, rows)
    rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    rss_bytes = rss if sys.platform == "darwin" else rss * 1024
    metadata = dict(graph="binary descendant cone with parent and grandparent edges; free boundary",
                    depths=DEPTHS, probabilities=PARAMETERS, replicates=REPLICATES,
                    seeds=list(range(159000, 159000 + REPLICATES)), large_threshold=MIN_SIZE,
                    threads=1, nice=os.getpriority(os.PRIO_PROCESS, 0), peak_rss_bytes=rss_bytes,
                    elapsed_seconds=round(time.monotonic() - started, 3), python=sys.version,
                    note="No finite component is asserted to be infinite. Finite windows may split a full-graph cluster.")
    (ROOT / "data/simulation_metadata.json").write_text(json.dumps(metadata, indent=2) + "\n")
    print(json.dumps(metadata, indent=2))


if __name__ == "__main__":
    run()
