"""Exact SAWs on explicit infinite cubic Cayley graphs; one thread, inherited nice 10.

Hanoi states are canonical full tree automorphisms, not finite Schreier vertices.
Composition uses wreath recursion; sections contract to singleton generators.
"""
import argparse
import csv
import json
import math
import os
import pathlib
import resource
import time

ROOT = pathlib.Path(__file__).resolve().parents[1]


class Hanoi:
    """a=(1,1,a)(01), b=(1,b,1)(02), c=(c,1,1)(12)."""
    def __init__(self):
        self.states = [((0, 1, 2), (0, 0, 0)),
                       ((1, 0, 2), (0, 0, 1)),
                       ((2, 1, 0), (0, 2, 0)),
                       ((0, 2, 1), (3, 0, 0))]
        self.ids = {state: i for i, state in enumerate(self.states)}
        self.products = {}
        self.generators = (1, 2, 3)
        self.origin = 0

    def product(self, x, y):
        """Return x composed with y; hence (xy)|_i = x|_(y(i)) y|_i."""
        if x == 0:
            return y
        if y == 0:
            return x
        if x == y and x <= 3:
            return 0
        pair = (x, y)
        if pair in self.products:
            return self.products[pair]
        px, sx = self.states[x]
        py, sy = self.states[y]
        p = tuple(px[py[i]] for i in range(3))
        s = tuple(self.product(sx[py[i]], sy[i]) for i in range(3))
        key = (p, s)
        z = self.ids.get(key)
        if z is None:
            z = len(self.states)
            self.ids[key] = z
            self.states.append(key)
        self.products[pair] = z
        return z

    def neighbors(self, x):
        return tuple(self.product(x, g) for g in self.generators)


class Lamplighter:
    """C2 wr Z, generators toggle, shift+, shift-. Lamps use signed integer bitset."""
    origin = (0, 0)

    @staticmethod
    def neighbors(v):
        lamps, pos = v
        bit = 2 * pos if pos >= 0 else -2 * pos - 1
        return ((lamps ^ (1 << bit), pos), (lamps, pos + 1), (lamps, pos - 1))


class Ladder:
    origin = (0, 0)

    @staticmethod
    def neighbors(v):
        pos, rail = v
        return ((pos + 1, rail), (pos - 1, rail), (pos, 1 - rail))


def enumerate_saws(graph, n):
    counts = [0] * (n + 1)
    seen = {graph.origin}

    def dfs(v, depth):
        counts[depth] += 1
        if counts[depth] % 100000 == 0:
            if resource.getrusage(resource.RUSAGE_SELF).ru_maxrss > 3 * 1024**3:
                raise MemoryError("Stopped at 3 GiB RSS")
        if depth == n:
            return
        for w in graph.neighbors(v):
            if w not in seen:
                seen.add(w)
                dfs(w, depth + 1)
                seen.remove(w)

    dfs(graph.origin, 0)
    return counts


def write_counts(name, counts, elapsed, graph):
    folder = ROOT / "data"
    folder.mkdir(exist_ok=True)
    with (folder / (name + ".csv")).open("w") as f:
        writer = csv.writer(f)
        writer.writerow(["n", "c_n", "ratio_evidence_only", "two_step_ratio_evidence_only",
                         "root_upper_bound", "edge_transitive_only_block_upper_bound"])
        for n, c in enumerate(counts):
            writer.writerow([n, c, c / counts[n-1] if n else "",
                             math.sqrt(c / counts[n-2]) if n >= 2 else "",
                             c ** (1/n) if n else "",
                             ((c / 3) ** (1/(n-1))) if n >= 2 and name.startswith('hanoi') else ""])
    info = {"graph": name, "n_max": len(counts)-1, "counts": counts,
            "elapsed_seconds": elapsed, "nice": os.getpriority(os.PRIO_PROCESS, 0),
            "threads": 1, "peak_rss_bytes_macos": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
            "tree_automorphism_states": len(graph.states) if isinstance(graph, Hanoi) else None}
    (folder / (name + ".json")).write_text(json.dumps(info, indent=2) + "\n")
    print(json.dumps(info), flush=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("graph", choices=["hanoi", "lamplighter", "ladder"])
    parser.add_argument("--n", type=int, default=18)
    args = parser.parse_args()
    assert os.getpriority(os.PRIO_PROCESS, 0) >= 10
    # macOS RLIMIT_AS is not reliable; cap data segment and keep the task small.
    soft, hard = resource.getrlimit(resource.RLIMIT_DATA)
    cap = min(3 * 1024**3, hard) if hard != resource.RLIM_INFINITY else 3 * 1024**3
    try:
        resource.setrlimit(resource.RLIMIT_DATA, (cap, hard))
    except (ValueError, OSError):
        # The managed macOS shell may reject setrlimit; DFS checks RSS as well.
        pass
    graph = {"hanoi": Hanoi, "lamplighter": Lamplighter, "ladder": Ladder}[args.graph]()
    start = time.monotonic()
    counts = enumerate_saws(graph, args.n)
    write_counts(args.graph, counts, time.monotonic() - start, graph)
