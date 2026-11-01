"""Cheap exact referee checks and handoff-shape validation for C0023."""

from fractions import Fraction
from itertools import product
import hashlib
import json
from pathlib import Path

root = Path(__file__).resolve().parent

# w420 L2, at the asserted threshold q <= 800**(-K).
t = Fraction(1, 100)
error = Fraction(1, 800) + 9 * t * (1 + t) / (1 - t) ** 3
assert error < Fraction(1, 10)

# w421 003, all eight edge configurations on o--a2--b--a1.
states = list(product((0, 1), repeat=3))
f2 = [s for s in states if s[0] and not (s[1] and s[2])]
f2_and_y = [s for s in f2 if s[1]]
assert len(f2) == 3 and len(f2_and_y) == 1
assert Fraction(len(f2_and_y), len(f2)) == Fraction(1, 3)
assert sum(bool(x and y) for x, y, z in states) == 2

with (root / "DRAFT_BUNDLE.json").open(encoding="utf-8") as stream:
    draft = json.load(stream)
assert draft["spec"] == "mathbrain-draft-v1"
keys = [entry["key"] for entry in draft["entries"]]
assert len(keys) == len(set(keys)) == 3
assert all(entry["source"]["license"].startswith("owner-own-work") for entry in draft["entries"])
assert all(relation["from_key"] in keys and relation["to_key"] in keys for relation in draft["relations"])

with (root / "REVIEW_VERDICTS.jsonl").open(encoding="utf-8") as stream:
    verdicts = [json.loads(line) for line in stream if line.strip()]
assert len({row["id"] for row in verdicts}) == len(verdicts)

pdf_hashes = {}
for name in (
    "garban_steif_1102_5761.pdf",
    "openai_critical_z3_20260924.pdf",
    "openai_quasi_transitive_20260924.pdf",
):
    pdf_hashes[name] = hashlib.sha256((root / name).read_bytes()).hexdigest()

print("L2 error at threshold:", error, "< 1/10")
print("selector F2 states:", len(f2), "/ 8; joint with Y:", len(f2_and_y), "/ 8; conditional=1/3")
print("review verdicts:", len(verdicts), "KEEP:", sum(v["verdict"] == "KEEP" for v in verdicts), "FIX:", sum(v["verdict"] == "FIX" for v in verdicts))
print("draft entries:", len(draft["entries"]), "relations:", len(draft["relations"]))
print("source SHA256:", json.dumps(pdf_hashes, sort_keys=True))
