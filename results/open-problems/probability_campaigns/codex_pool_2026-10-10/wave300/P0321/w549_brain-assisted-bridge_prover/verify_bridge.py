"""Small exact checks under compute_gate.json; writes only worker artifacts."""
import itertools
import json
import time
from collections import Counter
from fractions import Fraction
from pathlib import Path

from proposed.bridge_hypothesis_gate import check_bridge_support

ROOT = Path(__file__).resolve().parent
start = time.monotonic()
gate = json.loads((ROOT / "compute_gate.json").read_text(encoding="utf-8"))


def parity_states(shared: bool) -> list[tuple[int, ...]]:
    states: list[tuple[int, ...]] = []
    for seed in itertools.product((-1, 1), repeat=5 if shared else 6):
        if shared:
            h, a, b, c, d = seed
            k = h
        else:
            h, k, a, b, c, d = seed
        states.append((a, b, h*a*b, c, d, k*c*d))
    assert len(states) <= gate["max_generated_states"]
    return states


def alpha_for_blocks(states: list[tuple[int, ...]]) -> Fraction:
    """Exact supremum over all events in each finite triple-state sigma field.

    For a chosen row event, the maximizing column event consists of columns
    with positive covariance contribution. This covers all 256 column events.
    """
    rows = sorted(set(s[:3] for s in states))
    cols = sorted(set(s[3:] for s in states))
    counts = Counter((s[:3], s[3:]) for s in states)
    n = len(states)
    row_counts = Counter(s[:3] for s in states)
    col_counts = Counter(s[3:] for s in states)
    best_numerator = 0
    for mask in range(1 << len(rows)):
        event = [row for i, row in enumerate(rows) if mask & (1 << i)]
        row_mass = sum(row_counts[row] for row in event)
        contributions = [n*sum(counts[row, col] for row in event) - row_mass*col_counts[col] for col in cols]
        best_numerator = max(best_numerator, sum(max(0, value) for value in contributions))
    return Fraction(best_numerator, n*n)


def fixture_metrics(shared: bool) -> dict:
    states = parity_states(shared)
    n = len(states)
    checked = 0
    largest_pair_covariance = Fraction(0)
    for i, j in itertools.combinations(range(6), 2):
        outcomes = Counter((state[i], state[j]) for state in states)
        assert len(outcomes) == 4 and all(count == n//4 for count in outcomes.values())
        covariance = Fraction(sum(state[i]*state[j] for state in states), n)
        largest_pair_covariance = max(largest_pair_covariance, abs(covariance))
        checked += 1
    product_covariance = Fraction(sum(state[0]*state[1]*state[2]*state[3]*state[4]*state[5] for state in states), n)
    actual_alpha = alpha_for_blocks(states)
    assert actual_alpha == (Fraction(1, 4) if shared else Fraction(0))
    assert product_covariance == (Fraction(1) if shared else Fraction(0))
    return {
        "states": n,
        "pairwise_independence_checks_passed": checked,
        "largest_pair_covariance": str(largest_pair_covariance),
        "triple_product_covariance": str(product_covariance),
        "exact_block_alpha": str(actual_alpha),
    }


shield_slack = 2*(Fraction(3, 8)-Fraction(1, 32)-Fraction(1, 8))-Fraction(17, 32)**2
assert shield_slack == Fraction(159, 1024) > 0
assert Fraction(17, 8) < 3
assert Fraction(9, 8) < 2
shared = fixture_metrics(True)
independent = fixture_metrics(False)
bad_support = {
    "dependence_support": "density_pair_decay",
    "window_bound_uniform": True,
    "void_bound_stated": True,
    "observable": "spatial_nearest_cell_delaunay_sixfold",
    "geometry_hypotheses_stated": True,
}
baseline_accepts = shared["largest_pair_covariance"] == "0"
repaired = check_bridge_support(bad_support)
assert baseline_accepts and not repaired["scope_compatible"]
matching_hypothesis_tags = {**bad_support, "dependence_support": "all_local_events_mixing"}
matching = check_bridge_support(matching_hypothesis_tags)
assert matching["scope_compatible"] and not matching["truth_verified"]
elapsed = time.monotonic() - start
assert elapsed <= gate["max_runtime_seconds"]
results = {
    "command": "python -X utf8 verify_bridge.py",
    "gate": gate["gate"],
    "status": "PASS",
    "shield_slack_exact": str(shield_slack),
    "shared_parity_fixture": shared,
    "independent_parity_fixture": independent,
    "baseline_false_admissions_on_one_negative_fixture": int(baseline_accepts),
    "proposed_gate_false_admissions_on_same_fixture": int(repaired["scope_compatible"]),
    "matching_tags_accepted": matching["scope_compatible"],
    "matching_tags_truth_verified": matching["truth_verified"],
    "elapsed_seconds": elapsed,
    "limitations": "Exact finite checks and hypothesis-scope admission only. No Riesz simulation, infinite-volume mixing certificate, proof assistant, independent audit, or deployed retrieval gain.",
}
(ROOT / "verification.json").write_text(json.dumps(results, indent=2), encoding="utf-8")
print(json.dumps(results, indent=2))
