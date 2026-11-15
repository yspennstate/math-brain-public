#!/usr/bin/env python3
"""Check that the saved report, logs, source copy, and data agree."""

import csv
from fractions import Fraction
import json
import os
from pathlib import Path
import resource

resource.setrlimit(resource.RLIMIT_CPU, (30, 30))
assert os.getpriority(os.PRIO_PROCESS, 0) >= 15
assert os.environ.get("OMP_NUM_THREADS") == "1"
root = Path(__file__).resolve().parent
required = ("REPORT.md", "LOG.md", "PROOF.md", "verify.py", "VERIFY_OUTPUT.txt",
            "animal_counts.csv", "contour_bounds.csv", "verification.json",
            "prior_recheck/verify.py", "prior_recheck/VERIFY_OUTPUT.txt",
            "prior_recheck/verification.json")
for name in required:
    assert (root / name).stat().st_size > 0, name
previous_script = Path("~/codex_op_1114r3/briefs/T080/verify.py")
assert previous_script.read_bytes() == (root / "prior_recheck/verify.py").read_bytes()
report, log, proof = ((root / name).read_text() for name in ("REPORT.md", "LOG.md", "PROOF.md"))
assert report.splitlines()[0] == "VERDICT: PARTIAL uniform exponential bounds for connected underoccupied regions"
for name in ("VERIFY_OUTPUT.txt", "prior_recheck/VERIFY_OUTPUT.txt"):
    assert (root / name).read_text().strip() in log
data = json.loads((root / "verification.json").read_text())
old = json.loads((root / "prior_recheck/verification.json").read_text())
for record in (data, old):
    assert record["status"] == "PASS"
    assert record["peak_rss_mib"] < 128
    assert record["elapsed_seconds"] < 20*60
    assert record["nice_priority"] >= 15
assert data["exact_graph_cases"] == 3072 and data["weighted_graphs"] == 512
assert data["tilt_cases"] == 150
with (root / "animal_counts.csv").open() as handle:
    animals = list(csv.DictReader(handle))
assert len(animals) == len(data["animal_counts"]) == 9
for saved, expected in zip(animals, data["animal_counts"]):
    assert {key: int(value) for key, value in saved.items()} == expected
with (root / "contour_bounds.csv").open() as handle:
    examples = list(csv.DictReader(handle))
assert len(examples) == len(data["contour_examples"]) == 6
for saved, expected in zip(examples, data["contour_examples"]):
    for key, value in saved.items():
        assert float(value) == expected[key]
    assert expected["tau"] >= expected["tau_logarithmic_lower"]
assert Fraction(data["sufficient_thresholds"]["2"]["q_upper"]) == Fraction(4, 9)
assert Fraction(data["sufficient_thresholds"]["3"]["q_upper"]) == Fraction(729, 16384)
for text in (report, proof):
    assert "inside" in text or "contained" in text
assert "wholly contained" in proof
assert "T080 remains open" in report
assert not (root / "SOLVED_ELSEWHERE.md").exists()
print("PASS: report, full output logs, unchanged previous source copy, two data tables, exact thresholds, resource records, and finite-volume scope agree.")
