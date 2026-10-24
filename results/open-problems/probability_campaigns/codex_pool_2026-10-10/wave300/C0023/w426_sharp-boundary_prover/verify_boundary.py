"""Bounded, exact checks for w426's finite-graph boundary packet; stdlib only."""
from fractions import Fraction as Q
from itertools import product, combinations
from pathlib import Path
import json
import time
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parent
START = time.monotonic()
GATE = {"issued_utc": datetime.now(timezone.utc).isoformat(),
        "purpose": "Exact finite forest and relay counterexample checks, no sampling",
        "max_vertices": 5, "max_edges": 5, "max_seconds": 120,
        "max_configurations": 2000, "max_probability_cases": 30000,
        "gpu": False, "parallelism": 1, "network": False}
(ROOT / "COMPUTE_GATE.json").write_text(json.dumps(GATE, indent=2), encoding="utf-8")
COUNTS = {"configurations": 0, "probability_cases": 0, "pointwise_cases": 0,
          "forest_topologies": 0, "counterexample_weight_vectors": 0}

def gate():
    assert time.monotonic() - START < GATE["max_seconds"], "fresh compute time gate"
    assert COUNTS["configurations"] <= GATE["max_configurations"]
    assert COUNTS["probability_cases"] <= GATE["max_probability_cases"]

def all_states(n, edges):
    assert n <= GATE["max_vertices"] and len(edges) <= GATE["max_edges"]
    result = []
    for bits in product((0, 1), repeat=len(edges)):
        parent = list(range(n))
        def find(v):
            while parent[v] != v:
                v = parent[v]
            return v
        for (u, v), bit in zip(edges, bits):
            if bit:
                parent[find(u)] = find(v)
        labels = tuple(find(v) for v in range(n))
        result.append((bits, tuple(tuple(labels[u] == labels[v] for v in range(n))
                                   for u in range(n))))
    COUNTS["configurations"] += len(result)
    gate()
    return result

def weights(states, probabilities):
    out = []
    for bits, _ in states:
        w = Q(1)
        for bit, p in zip(bits, probabilities):
            w *= p if bit else 1 - p
        out.append(w)
    assert sum(out) == 1
    return out

def probability(states, ws, event):
    return sum((w for (_, c), w in zip(states, ws) if event(c)), Q(0))

def prufer_tree(n, sequence):
    degree = [1] * n
    for x in sequence:
        degree[x] += 1
    edges = []
    for x in sequence:
        leaf = next(v for v in range(n) if degree[v] == 1)
        edges.append((leaf, x))
        degree[leaf] -= 1
        degree[x] -= 1
    u, v = [v for v in range(n) if degree[v] == 1]
    return edges + [(u, v)]

def check_forest(n, edges):
    states = all_states(n, edges)
    COUNTS["forest_topologies"] += 1
    distributions = [tuple(Q(1, 2) for _ in edges),
                     tuple(Q(1 + (i % 2), 3) for i in range(len(edges))),
                     tuple(Q(i % 2) for i in range(len(edges))),
                     tuple(Q(1 - (i % 2)) for i in range(len(edges)))]
    distributions = list(dict.fromkeys(distributions))
    probability_data = []
    for ps in distributions:
        ws = weights(states, ps)
        pair = [[probability(states, ws, lambda c, u=u, v=v: c[u][v])
                 for v in range(n)] for u in range(n)]
        probability_data.append((ws, pair))
    for o in range(n):
        for b in range(n):
            for relay_mask in range(1, 1 << n):
                A = tuple(a for a in range(n) if relay_mask & (1 << a))
                hits = [any(c[o][a] for a in A) for _, c in states]
                witnesses = [a for a in A if all(not (hit and c[a][b]) or c[o][b]
                              for hit, (_, c) in zip(hits, states))]
                assert witnesses, ("no pointwise witness in forest", n, edges, o, b, A)
                COUNTS["pointwise_cases"] += 1
                for ws, pair in probability_data:
                    hit_p = sum((w for hit, w in zip(hits, ws) if hit), Q(0))
                    terminal_p = pair[o][b]
                    q = min(pair[a][b] for a in A)
                    assert terminal_p >= hit_p * q, (n, edges, o, b, A)
                    intersections = [sum((w for hit, (_, c), w in zip(hits, states, ws)
                                          if hit and c[a][b]), Q(0)) for a in A]
                    both = sum((w for hit, (_, c), w in zip(hits, states, ws)
                                if hit and c[o][b]), Q(0))
                    assert both >= min(intersections)
                    COUNTS["probability_cases"] += 1
                gate()

def selected_relay_counterexample(r, s, t):
    # Vertices 0=o, 1=a2, 2=a1, 3=b. First relay order is (2,1).
    states = all_states(4, [(0, 1), (1, 2), (2, 3)])
    ws = weights(states, (r, s, t))
    selection = [next((a for a in (2, 1) if c[0][a]), None) for _, c in states]
    selected_a1 = sum((w for i, w in zip(selection, ws) if i == 2), Q(0))
    selected_a2 = sum((w for i, w in zip(selection, ws) if i == 1), Q(0))
    m1 = probability(states, ws, lambda c: c[2][3])
    m2 = probability(states, ws, lambda c: c[1][3])
    true_p = probability(states, ws, lambda c: c[0][3])
    numerator = sum((w for i, (_, c), w in zip(selection, states, ws)
                     if i == 1 and c[1][3]), Q(0))
    assert selected_a1 == r * s and selected_a2 == r * (1 - s)
    assert m1 == t and m2 == s * t
    assert numerator == 0 and selected_a2 > 0
    wrong_p = selected_a1 * m1 + selected_a2 * m2
    assert true_p == r * s * t
    assert wrong_p - true_p == r * s * t * (1 - s) > 0
    COUNTS["counterexample_weight_vectors"] += 1
    return {"r": str(r), "s": str(s), "t": str(t),
            "actual_terminal_probability": str(true_p),
            "incorrect_relay_sum": str(wrong_p),
            "overstatement": str(wrong_p - true_p),
            "selected_a2_probability": str(selected_a2),
            "unconditional_a2_terminal_probability": str(m2),
            "conditional_a2_terminal_probability": "0"}

def cycle_obstruction():
    # Square 0--1--3--2--0 with terminal 4 attached to 3; relays {1,2}.
    edges = [(0, 1), (1, 3), (0, 2), (2, 3), (3, 4)]
    states = all_states(5, edges)
    witnesses = [a for a in (1, 2) if all(
        not ((c[0][1] or c[0][2]) and c[a][4]) or c[0][4] for _, c in states)]
    assert witnesses == [], "cyclic counterexample to deterministic witness extension"
    ws = weights(states, (Q(1, 2),) * 5)
    p = probability(states, ws, lambda c: c[0][4])
    h = probability(states, ws, lambda c: c[0][1] or c[0][2])
    q = min(probability(states, ws, lambda c, a=a: c[a][4]) for a in (1, 2))
    assert (p, h, q, p - h*q) == (Q(7,32), Q(3,4), Q(9,32), Q(1,128))
    return {"deterministic_witnesses": witnesses, "terminal_probability": str(p),
            "relay_hit_probability": str(h), "minimum_relay_terminal_probability": str(q),
            "product_gluing_margin": str(p - h*q),
            "meaning": "No deterministic relay witness, although the product bound holds here."}

def main():
    for n in range(2, 5):
        for sequence in product(range(n), repeat=n-2):
            check_forest(n, prufer_tree(n, sequence))
    for edges in [[(0,1),(1,2),(2,3),(3,4)],
                  [(0,1),(0,2),(0,3),(0,4)],
                  [(0,1),(1,2),(1,3),(3,4)],
                  [(0,1),(2,3)], []]:
        check_forest(5, edges)
    for r, s, t in product((Q(1,4), Q(1,2), Q(3,4)), repeat=3):
        selected_relay_counterexample(r, s, t)
    half = selected_relay_counterexample(Q(1,2), Q(1,2), Q(1,2))
    near_one = selected_relay_counterexample(Q(99,100), Q(99,100), Q(99,100))
    cycle = cycle_obstruction()
    # Sharp coefficient: P(o--a--b)=rs=P(o--a)P(a--b).
    states = all_states(3, [(0,1),(1,2)])
    ws = weights(states, (Q(2,3),Q(3,4)))
    assert probability(states,ws,lambda c:c[0][2]) == Q(1,2)
    assert probability(states,ws,lambda c:c[0][1]) * probability(states,ws,lambda c:c[1][2]) == Q(1,2)
    gate()
    receipt = {"status": "PASS", "command": "python -X utf8 verify_boundary.py",
               "arithmetic": "fractions.Fraction; exhaustive open/closed states, no float tolerance",
               "counts": COUNTS, "elapsed_seconds": time.monotonic()-START,
               "half_weight_counterexample": half, "near_one_counterexample": near_one,
               "cyclic_witness_obstruction": cycle,
               "scope": "Finite consistency checks support the written proofs; not a lattice proof or formal proof receipt."}
    (ROOT/"VERIFICATION.json").write_text(json.dumps(receipt,indent=2),encoding="utf-8")
    print(json.dumps(receipt,indent=2))

if __name__ == "__main__":
    main()
