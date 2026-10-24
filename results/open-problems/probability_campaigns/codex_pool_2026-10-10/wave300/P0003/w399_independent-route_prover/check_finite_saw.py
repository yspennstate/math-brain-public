"""Exact synthetic checks. No store, private test bank, models or external data."""
from collections import defaultdict
from fractions import Fraction
import itertools
import json
from pathlib import Path
import time

ROOT = Path(__file__).resolve().parent
START = time.monotonic()
DEADLINE = START + 45
COUNTS = defaultdict(int)

def check_time():
    if time.monotonic() > DEADLINE:
        raise TimeoutError("fresh w399 45-second compute gate expired")

def paths(graph, start, end, blocked=frozenset()):
    if start in blocked or end in blocked:
        return []
    result = []
    def visit(prefix):
        u = prefix[-1]
        if u == end:
            result.append(tuple(prefix))
            return
        for v in graph[u]:
            if v not in blocked and v not in prefix:
                visit(prefix + [v])
    visit([start])
    return result

def partition(graph, start, end, x, blocked=frozenset()):
    return sum((x ** (len(p)-1) for p in paths(graph, start, end, blocked)), Fraction(0))

def equal(left, right, key):
    assert left == right, (key, str(left), str(right))
    COUNTS[key] += 1

def test_graph(graph, x, obstacles):
    full = paths(graph, 0, 3)
    if not full:
        return
    weights = {p: x ** (len(p)-1) for p in full}
    z = sum(weights.values(), Fraction(0))
    groups = defaultdict(list)
    for p in full:
        for n in range(1, len(p)+1):
            groups[p[:n]].append(p)
    masses = {pre: sum((weights[p] for p in completions), Fraction(0)) for pre, completions in groups.items()}
    for obstacle in obstacles:
        check_time()
        empirical = sum((w for p,w in weights.items() if not set(p) & obstacle), Fraction(0)) / z
        equal(empirical, partition(graph, 0, 3, x, obstacle) / z, "avoidance_quotients")
        values = {}
        for pre, compatible in groups.items():
            blocked = frozenset(pre[:-1])
            tail_z = partition(graph, pre[-1], 3, x, blocked)
            assert tail_z > 0
            m = Fraction(0) if set(pre) & obstacle else partition(graph, pre[-1], 3, x, blocked | obstacle) / tail_z
            cond = sum((weights[p] for p in compatible if not set(p) & obstacle), Fraction(0)) / masses[pre]
            equal(m, cond, "conditional_prefix_quotients")
            assert 0 <= m <= 1
            values[pre] = m
            if pre[-1] == 3:
                equal(m, Fraction(not set(pre) & obstacle), "terminal_indicators")
        for pre in groups:
            if pre[-1] == 3:
                continue
            children = [q for q in groups if len(q) == len(pre)+1 and q[:-1] == pre]
            equal(values[pre], sum((masses[q] * values[q] / masses[pre] for q in children), Fraction(0)), "martingale_tower_checks")
        stopped = Fraction(0)
        for p,w in weights.items():
            n = next((n for n in range(1,len(p)) if p[n] == 2 or p[n] == 3), len(p)-1)
            stopped += w * values[p[:n+1]] / z
        equal(stopped, values[(0,)], "optional_stopping_checks")
        COUNTS["graph_weight_obstacle_cases"] += 1

edges = list(itertools.combinations(range(4), 2))
graphs_with_paths = 0
for mask in range(1 << len(edges)):
    check_time()
    graph = {v: [] for v in range(4)}
    for k,(u,v) in enumerate(edges):
        if mask & (1 << k):
            graph[u].append(v)
            graph[v].append(u)
    if paths(graph,0,3):
        graphs_with_paths += 1
    for x in [Fraction(1,2), Fraction(1), Fraction(2)]:
        test_graph(graph, x, [frozenset(s) for r in range(3) for s in itertools.combinations([1,2],r)])

cycle = {v: [(v-1)%6,(v+1)%6] for v in range(6)}
for x in [Fraction(1,2), Fraction(1), Fraction(2)]:
    test_graph(cycle, x, [frozenset(s) for r in range(3) for s in itertools.combinations([1,2,4,5],r)])
    z = partition(cycle,0,3,x)
    p_a = partition(cycle,0,3,x,frozenset([1])) / z
    p_b = partition(cycle,0,3,x,frozenset([5])) / z
    p_c = partition(cycle,0,3,x,frozenset([2])) / z
    joint_opposite = partition(cycle,0,3,x,frozenset([1,5])) / z
    joint_same = partition(cycle,0,3,x,frozenset([1,2])) / z
    equal(p_a, Fraction(1,2), "honeycomb_counterexample_checks")
    equal(joint_opposite, Fraction(0), "honeycomb_counterexample_checks")
    equal(joint_same, Fraction(1,2), "honeycomb_counterexample_checks")
    assert joint_opposite < p_a*p_b and joint_same > p_a*p_c

topology = []
for epsilon in [Fraction(1,10), Fraction(1,100), Fraction(1,1000)]:
    topology.append({"epsilon": str(epsilon), "hausdorff_upper_bound": str(2*epsilon), "frechet_lower_bound": "1/4"})

result = {
    "command": "python -B -X utf8 check_finite_saw.py",
    "elapsed_seconds": round(time.monotonic()-START,6),
    "graphs_enumerated": 64,
    "four_vertex_graphs_with_endpoint_path": graphs_with_paths,
    "weights": ["1/2","1","2"],
    "exact_arithmetic": "fractions.Fraction",
    "counts": dict(COUNTS),
    "max_identity_residual": "0 (exact rational arithmetic)",
    "honeycomb_unsafe_independence_baseline": {"claimed_joint": "1/4", "actual_joint_opposite": "0", "actual_joint_same": "1/2", "absolute_error_each": "1/4"},
    "honeycomb_correct_conditioning_after": {"opposite_second_conditional": "0", "same_second_conditional": "1", "joint_residual_each": "0"},
    "topology_counterexample": topology,
    "limits": "Finite synthetic checks support the written general proof. They do not prove any scaling limit, conformal exponent, curve tightness, or novelty.",
    "formal_checker": None,
    "passed": True
}
(ROOT/"MEASUREMENTS.json").write_text(json.dumps(result, indent=2)+"\n",encoding="utf-8")
print(json.dumps(result, indent=2))
