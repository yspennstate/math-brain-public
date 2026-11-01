"""Tiny exact checks. Gate is fresh and read-only; no GPU or model import."""
from datetime import datetime, timezone
from fractions import Fraction
from itertools import product
from pathlib import Path
import json
import math
import sys
import time

ROOT = Path(__file__).resolve().parent
GOVERNOR = Path("~/.claude/compute/compute_state.json")
started = time.perf_counter()
receipt = {"command": "python -X utf8 verify_obstructions.py", "timestamp_utc": datetime.now(timezone.utc).isoformat(),
           "scope": "eight exact graph configurations, 650 integer shell checks, rational Peierls constants; no sampling",
           "formal_check": False, "independent_review": "pending"}
try:
    age = time.time() - GOVERNOR.stat().st_mtime
    state = json.loads(GOVERNOR.read_text(encoding="utf-8-sig"))
    safe_keys = ("ts", "status", "mode", "reasons", "commit_used_pct", "commit_avail_mb", "cpu_pct")
    receipt["fresh_gate"] = {"file": str(GOVERNOR), "age_seconds": age,
                              **{key: state.get(key) for key in safe_keys}}
    commit = state.get("commit_used_pct")
    headroom = state.get("commit_avail_mb")
    permitted = (0 <= age <= 60 and state.get("status") == "ok"
                 and state.get("mode") not in {"throttle", "pause", "hold", "distress"}
                 and isinstance(commit, (int, float)) and commit < 85
                 and isinstance(headroom, (int, float)) and headroom > 16384)
except (OSError, ValueError) as exc:
    permitted = False
    receipt["fresh_gate"] = {"error": type(exc).__name__ + ": " + str(exc)}

if not permitted:
    receipt.update(status="GATE_HELD", checks_run=0, elapsed_seconds=time.perf_counter() - started)
    (ROOT / "MEASUREMENTS.json").write_text(json.dumps(receipt, indent=2), encoding="utf-8")
    print(json.dumps(receipt, indent=2))
    raise SystemExit(2)

vertices = ("o", "a2", "b", "a1")
edges = (("o", "a2"), ("a2", "b"), ("b", "a1"))
counts = {key: 0 for key in ("reach_A", "o_b", "a1_b", "a2_b", "F1", "F1_a1_b", "F2", "F2_a2_b")}
truth_table = []
for bits in product((0, 1), repeat=3):
    adj = {v: set() for v in vertices}
    for bit, (u, v) in zip(bits, edges):
        if bit:
            adj[u].add(v)
            adj[v].add(u)
    def connected(u, v):
        seen, pending = {u}, [u]
        while pending:
            for w in adj[pending.pop()]:
                if w not in seen:
                    seen.add(w)
                    pending.append(w)
        return v in seen
    oa1, oa2 = connected("o", "a1"), connected("o", "a2")
    a1b, a2b = connected("a1", "b"), connected("a2", "b")
    flags = {"reach_A": oa1 or oa2, "o_b": connected("o", "b"), "a1_b": a1b, "a2_b": a2b,
             "F1": oa1, "F1_a1_b": oa1 and a1b,
             "F2": oa2 and not oa1, "F2_a2_b": oa2 and not oa1 and a2b}
    for key, value in flags.items():
        counts[key] += int(value)
    truth_table.append({"bits": bits, **flags})
prob = {key: Fraction(value, 8) for key, value in counts.items()}
conditional = prob["F2_a2_b"] / prob["F2"]
minimum = min(prob["a1_b"], prob["a2_b"])
assert conditional == Fraction(1, 3) and minimum == Fraction(1, 2)
assert prob["o_b"] - prob["reach_A"] * minimum == 0
assert prob["F1_a1_b"] + prob["F2_a2_b"] == prob["o_b"]
receipt["selector"] = {"states": 8, "probabilities": {k: str(v) for k, v in prob.items()},
                       "conditional": str(conditional), "min_marginal": str(minimum),
                       "false_premise_gap": str(conditional - minimum), "global_KN_margin": "0",
                       "truth_table": truth_table}

worst = (Fraction(0), 0, 0)
shell_checks = 0
for d in range(1, 11):
    def b(r):
        return (2 * r + 1) ** d if r >= 0 else 0
    c = 12 * d * d * 21 ** (d - 1)
    for r in range(65):
        numerator = (b(r) - b(r - 1)) * (b(r + 2) - b(r - 1))
        denominator = c * (r + 1) ** (2 * d - 2)
        ratio = Fraction(numerator, denominator)
        assert ratio <= 1
        if ratio > worst[0]:
            worst = (ratio, d, r)
        shell_checks += 1
receipt["shell_count"] = {"checks": shell_checks, "dimensions": [1, 10], "radii": [0, 64],
                          "largest_ratio": str(worst[0]), "largest_ratio_at": {"d": worst[1], "r": worst[2]},
                          "scope_limit": "finite sanity check; the all-radius inequality uses the analytic proof"}

def lower_bound(base):
    q, t = Fraction(1, base), Fraction(8, base)
    return 1 - q - 9 * t * (1 + t) / (1 - t) ** 3
old, new = lower_bound(800), lower_bound(101)
assert old > Fraction(9, 10)
assert new == Fraction(378252, 81240057) and new > 0
assert lower_bound(100) < 0
receipt["peierls"] = {"baseline_base": 800, "baseline_lower_bound": str(old),
                      "positive_threshold_base": 101, "new_lower_bound": str(new),
                      "new_lower_bound_decimal": float(new),
                      "allowed_failure_ratio_per_K": "(800/101)^K", "base_100_lower_bound": str(lower_bound(100)),
                      "scope_limit": "constants in an elementary sufficient bound, not critical lattice estimates"}
receipt.update(status="PASS", checks_run=8 + shell_checks + 3, elapsed_seconds=time.perf_counter() - started)
(ROOT / "MEASUREMENTS.json").write_text(json.dumps(receipt, indent=2), encoding="utf-8")
print(json.dumps({key: value for key, value in receipt.items() if key != "selector"}, indent=2))
print("selector", conditional, "<", minimum, "gap", conditional - minimum, "KN margin=0")
