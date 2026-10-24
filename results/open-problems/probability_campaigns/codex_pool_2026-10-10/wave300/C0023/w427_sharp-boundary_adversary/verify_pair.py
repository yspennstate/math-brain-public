"""A fresh bounded exact check of the paired counterexample and cyclic boundary."""
import json
from datetime import datetime, timezone
from fractions import Fraction
from itertools import product
from pathlib import Path
from time import perf_counter

started = perf_counter()
gate = {"opened_at": datetime.now(timezone.utc).isoformat(),
        "max_configurations": 32, "max_seconds": 10,
        "local_cpu_only": True, "gpu_or_training": False}
configuration_count = 0


def connected(edges, states, start, target):
    adjacency = {}
    for (u, v), opened in zip(edges, states):
        if opened:
            adjacency.setdefault(u, []).append(v)
            adjacency.setdefault(v, []).append(u)
    reached = {start}
    queue = [start]
    for u in queue:
        for v in adjacency.get(u, []):
            if v not in reached:
                reached.add(v)
                queue.append(v)
    return target in reached


def table(edges):
    global configuration_count
    for states in product((False, True), repeat=len(edges)):
        configuration_count += 1
        assert configuration_count <= gate["max_configurations"]
        assert perf_counter() - started <= gate["max_seconds"]
        yield states, Fraction(1, 2 ** len(edges))


path = [("o", "a2"), ("a2", "a1"), ("a1", "b")]
terminal = selection_a1 = selection_a2 = conditional_numerator = Fraction(0)
for states, weight in table(path):
    hit_a1 = connected(path, states, "o", "a1")
    hit_a2 = connected(path, states, "o", "a2")
    terminal += weight * connected(path, states, "o", "b")
    selection_a1 += weight * hit_a1
    if not hit_a1 and hit_a2:
        selection_a2 += weight
        conditional_numerator += weight * connected(path, states, "a2", "b")
averaged_marginals = selection_a1 * Fraction(1, 2) + selection_a2 * Fraction(1, 4)
assert terminal == Fraction(1, 8)
assert averaged_marginals == Fraction(3, 16)
assert selection_a2 > 0 and conditional_numerator == 0

cycle = [("o", "a"), ("a", "b"), ("b", "c"), ("c", "o")]
cycle_terminal = cycle_relay = a_to_b = c_to_b = Fraction(0)
for states, weight in table(cycle):
    cycle_terminal += weight * connected(cycle, states, "o", "b")
    cycle_relay += weight * (connected(cycle, states, "o", "a") or
                             connected(cycle, states, "o", "c"))
    a_to_b += weight * connected(cycle, states, "a", "b")
    c_to_b += weight * connected(cycle, states, "c", "b")
assert cycle_terminal == Fraction(7, 16)
assert cycle_relay == Fraction(3, 4)
assert a_to_b == c_to_b == Fraction(9, 16)
assert cycle_terminal - cycle_relay * min(a_to_b, c_to_b) == Fraction(1, 64)

result = {
    "gate": gate, "enumerated_configurations": configuration_count,
    "path_actual_terminal_probability": str(terminal),
    "path_incorrect_marginal_average": str(averaged_marginals),
    "path_excess": str(averaged_marginals - terminal),
    "path_selected_a2_conditional_terminal_probability": "0",
    "cycle_actual_terminal_probability": str(cycle_terminal),
    "cycle_correct_product_lower_bound": str(cycle_relay * min(a_to_b, c_to_b)),
    "cycle_positive_margin": "1/64", "all_exact_checks_pass": True,
    "elapsed_seconds": perf_counter() - started,
    "limits": "Two finite graphs; general proofs are in PAIRED_AUDIT.md, not certified by this enumeration.",
}
(Path(__file__).resolve().parent / "PAIR_MEASUREMENTS.json").write_text(
    json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
