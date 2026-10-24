"""Small checkpoint replay of already captured recall, not a test-bank item."""

import importlib.util
import json
from pathlib import Path
import re
import time

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("staged_gate", ROOT / "staged/p0297_recall_gate.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

def main():
    gate_path = Path("~/.claude/compute/compute_state.json")
    state = json.loads(gate_path.read_text(encoding="utf-8-sig"))
    gate = {k: state.get(k) for k in ("ts", "status", "mode", "reasons")}
    # This process only validates and saves the current checkpoint: 3 captured
    # strings and 6 hand-written controls. It creates no sample/network/model.
    gate["workload"] = "atomic_checkpoint_string_replay"
    gate["bounds"] = "one process; standard library; at most 9 strings; no enumeration"
    t = time.perf_counter()
    recall = json.loads((ROOT / "evidence/brain_recall.json").read_text(encoding="utf-8"))
    lines = recall["stdout"].splitlines()
    hits = []
    for i, line in enumerate(lines):
        match = re.match(r"^\s+\d+\.\d+\s+\[.*\]\s+(\S+)\s*$", line)
        if match:
            hits.append({"slug": match.group(1), "text": lines[i+1].strip() if i+1<len(lines) else ""})
        if len(hits)==3:
            break
    assert len(hits)==3, "Capture is not the intended top-three replay"
    result = module.filter_lqg_hits(hits)
    assert result["abstained"] and result["rejected_count"]==3
    controls = [
        ("KPZ formulas for the Liouville quantum gravity metric", True),
        ("LFPP normalization exponent with covariance assumptions", True),
        ("LQG geodesic and field independence", True),
        ("KPZ relation for first-passage percolation on Z^d", False),
        ("Liouville theorem for bounded entire functions", False),
        ("Quantum immortality and unrelated metric instrumentation", False),
    ]
    for text, expected in controls:
        decision = module.filter_lqg_hits([{"title": text}])
        assert bool(decision["accepted"]) == expected, text
    report = {
        "command": "python -B -X utf8 checks/check_recall_gate.py",
        "gate": gate,
        "scope": "exact captured top three plus six controls; relevance only",
        "before": {"off_target_hints_served": 3, "target_relevant_top3": 0},
        "after": {"off_target_hints_served": len(result["accepted"]), "abstained": result["abstained"]},
        "controls_passed": len(controls),
        "elapsed_seconds": time.perf_counter()-t,
        "deployment": "staged proposal; live recall unchanged",
        "limitation": "Does not establish general recall accuracy or mathematical correctness",
    }
    (ROOT / "evidence/gate_replay.json").write_text(json.dumps(report,indent=2),encoding="utf-8")
    print(json.dumps(report))

if __name__=="__main__":
    main()
