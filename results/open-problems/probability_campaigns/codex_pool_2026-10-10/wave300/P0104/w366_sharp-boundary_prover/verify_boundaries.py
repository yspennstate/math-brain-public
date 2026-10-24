"""Small exact checks; not a formal proof or a claim about asymptotic KPZ."""
import ctypes
import heapq
import itertools
import json
import os
from fractions import Fraction
from pathlib import Path
from time import perf_counter, process_time

ROOT = Path(__file__).resolve().parent
start = perf_counter()
cpu_start = process_time()
gate = {"created_utc": __import__("datetime").datetime.now(__import__("datetime").timezone.utc).isoformat(),
        "command": "python -X utf8 verify_boundaries.py", "cpu_budget_seconds": 4,
        "wall_budget_seconds": 30, "max_configurations": 4000, "max_lattice_n": 64,
        "gpu": False, "background_processes": False}
if os.name == "nt":
    class MEMORYSTATUSEX(ctypes.Structure):
        _fields_ = [("dwLength", ctypes.c_ulong), ("dwMemoryLoad", ctypes.c_ulong),
                    ("ullTotalPhys", ctypes.c_ulonglong), ("ullAvailPhys", ctypes.c_ulonglong),
                    ("ullTotalPageFile", ctypes.c_ulonglong), ("ullAvailPageFile", ctypes.c_ulonglong),
                    ("ullTotalVirtual", ctypes.c_ulonglong), ("ullAvailVirtual", ctypes.c_ulonglong),
                    ("ullAvailExtendedVirtual", ctypes.c_ulonglong)]
    mem = MEMORYSTATUSEX()
    mem.dwLength = ctypes.sizeof(mem)
    if not ctypes.windll.kernel32.GlobalMemoryStatusEx(ctypes.byref(mem)):
        raise RuntimeError("fresh memory gate unavailable")
    gate["available_memory_bytes"] = mem.ullAvailPhys
    gate["memory_load_percent"] = mem.dwMemoryLoad
    gate["allowed"] = mem.ullAvailPhys >= 512 * 1024**2
else:
    gate["allowed"] = True
(ROOT / "COMPUTE_GATE.json").write_text(json.dumps(gate, indent=2), encoding="utf-8")
if not gate["allowed"]:
    raise SystemExit("GATE REFUSED: less than 512 MiB free; no experiment run")

def budget():
    if process_time() - cpu_start > 4 or perf_counter() - start > 30:
        raise RuntimeError("fresh compute gate exhausted")

def expand(turns):
    vertices = [turns[0]]
    for (x, y), (a, b) in itertools.pairwise(turns):
        assert x == a or y == b
        while (x, y) != (a, b):
            x += (a > x) - (a < x)
            y += (b > y) - (b < y)
            vertices.append((x, y))
    return vertices

def edge(a, b):
    return tuple(sorted((a, b)))

route_cases = 0
for n in range(1, 65):
    budget()
    turns = [[(0, 0), (n, 0)], [(0, 0), (0, 1), (n, 1), (n, 0)],
             [(0, 0), (0, -1), (n, -1), (n, 0)],
             [(0, 0), (-1, 0), (-1, 2), (n+1, 2), (n+1, 0), (n, 0)]]
    paths = [expand(t) for t in turns]
    sets = [set(edge(a, b) for a, b in itertools.pairwise(p)) for p in paths]
    assert [len(s) for s in sets] == [n, n+2, n+2, n+8]
    assert all(not a.intersection(b) for a, b in itertools.combinations(sets, 2))
    assert all(p[0] == (0, 0) and p[-1] == (n, 0) for p in paths)
    route_cases += 1

def shortest(adj, target):
    dist = {(0, 0): 0}
    todo = [(0, (0, 0))]
    while todo:
        d, u = heapq.heappop(todo)
        if d != dist[u]:
            continue
        if u == target:
            return d
        for v, w in adj[u]:
            nd = d + w
            if nd < dist.get(v, 10**9):
                dist[v] = nd
                heapq.heappush(todo, (nd, v))
    raise AssertionError("disconnected finite checking graph")

cases = []
configs = 0
for n in range(1, 4):
    nodes = [(x, y) for x in range(n+1) for y in [0, 1]]
    edges = [(u, v) for u, v in itertools.combinations(nodes, 2)
             if abs(u[0]-v[0]) + abs(u[1]-v[1]) == 1]
    for numerator in [1, 2, 3]:
        # epsilon=numerator/n; integer edge costs n or n+numerator.
        costs, losses = [], 0
        for bits in itertools.product([0, 1], repeat=len(edges)):
            budget()
            adj = {u: [] for u in nodes}
            straight = 0
            for (u, v), bit in zip(edges, bits):
                w = n + numerator * bit
                adj[u].append((v, w))
                adj[v].append((u, w))
                if u[1] == v[1] == 0:
                    straight += w
            t = shortest(adj, (n, 0))
            losses += (t < straight)
            if numerator <= 2:
                assert t == straight
            costs.append(t)
            configs += 1
            assert configs <= gate["max_configurations"]
        count = len(costs)
        mean = Fraction(sum(costs), count*n)
        var = Fraction(sum(t*t for t in costs), count*n*n) - mean*mean
        expected_var = Fraction(numerator*numerator, 4*n)
        if numerator <= 2:
            assert var == expected_var
        else:
            assert losses > 0
        cases.append({"n": n, "epsilon": str(Fraction(numerator, n)), "configurations": count,
                      "straight_losses": losses, "variance_exact": str(var),
                      "linear_window_expected_variance": str(expected_var) if numerator <= 2 else None})

uniform_ratios = []
for k in [2, 4, 8]:
    n = k**3
    variance = Fraction(1, 12*n)
    edge_variance = Fraction(1, 12*n*n)
    # n^(2/3)=k^2, so this ratio is exactly rational.
    ratio = variance / (edge_variance * k*k)
    assert ratio == k
    uniform_ratios.append({"n": n, "epsilon": str(Fraction(1, n)),
                           "variance": str(variance), "edge_variance": str(edge_variance),
                           "ratio_to_edge_variance_times_n_two_thirds": str(ratio)})
result = {"status": "PASS", "formal_proof": False, "command": gate["command"],
          "route_cases": route_cases, "pairwise_disjointness_checks": 6*route_cases,
          "finite_graph_configurations": configs, "finite_graph_cases": cases,
          "uniform_law_ratios": uniform_ratios,
          "cpu_seconds": process_time()-cpu_start, "wall_seconds": perf_counter()-start,
          "scope": "Exact finite checks plus algebraic evaluations; the infinite-lattice proofs are in LEMMAS.md. No asymptotic exponent verified."}
(ROOT / "MEASUREMENTS.json").write_text(json.dumps(result, indent=2), encoding="utf-8")
print(json.dumps(result, indent=2))
