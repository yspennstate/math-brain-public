"""Read-only input inventory and consistency check of this referee's artifacts."""
from pathlib import Path
import hashlib
import json
import re

root = Path(__file__).resolve().parent
source = (root / "PAPER.tex").read_text()
section = 0
counter = 0
items = []
for lineno, line in enumerate(source.splitlines(), 1):
    if re.search(r"\\section\{", line):
        section += 1
        counter = 0
    match = re.search(r"\\begin\{(theorem|lemma|proposition|corollary|remark|example)\}.*\\label(?:\[[^]]*\])?\{([^}]+)\}", line)
    if match:
        counter += 1
        items.append((f"{section}.{counter}", match[1], match[2], lineno))
for number, kind, label, line in items:
    print(f"{number:4} {kind:12} {label:24} line {line}")
assert len(items) == 17
expected_hash = "e5a894142d0911c941b99157f09d4efed1542ecef5958fd3f9ebd18120055664"
assert hashlib.sha256((root / "PAPER.tex").read_bytes()).hexdigest() == expected_hash
records = json.loads((root / "referee_checks_output.json").read_text())
assert len(records) == 15
assert all(r["mean"] > 0 and r["SE"] > 0 for r in records)
assert all(r["mean"] < r["BL_bound"] for r in records if r["law"] == "atom")
report = root / "REPORT.md"
if report.exists():
    text = report.read_text()
    assert text.splitlines()[0] in ["Overall verdict: " + x for x in ("ACCEPT", "MINOR", "MAJOR", "REJECT")]
    for _, _, label, _ in items:
        assert label in text, f"Missing numbered result: {label}"
    print("Report first line and all 17 result labels: PASS")
print("Source hash unchanged; 15 simulation rows; finite BL comparisons: PASS")
print("Total referee artifact bytes:", sum(p.stat().st_size for p in root.glob("referee_*") if p.is_file()))
