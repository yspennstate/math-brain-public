"""Reproduce the P0043 source-scope and draft-state counts; no store writes."""

import csv
import json
from pathlib import Path

here = Path(__file__).resolve().parent
rank = Path(
    "~/<private-repo>/06_math_research/"
    "probability_1000_intake_claude_20260907/RANKING_2026-09-07.csv"
)
with rank.open(encoding="utf-8-sig", newline="") as stream:
    row = next(r for r in csv.reader(stream) if len(r) > 1 and r[1] == "P0043")
raw = " ".join(row).lower()
bundle_path = here / "bundle_001.json"
bundle = json.loads(bundle_path.read_text(encoding="utf-8"))
json.loads((here / "SOURCE_STATUS.json").read_text(encoding="utf-8"))
claims = [
    json.loads(line)
    for line in (here / "CLAIMS.jsonl").read_text(encoding="utf-8").splitlines()
    if line.strip()
]
keys = {entry["key"] for entry in bundle["entries"]}
assert all(rel["from_key"] in keys and rel["to_key"] in keys for rel in bundle["relations"])
assert all(entry["kind"] == "concept" and entry["proof_text"] is None for entry in bundle["entries"])
inbox = Path("~/math-brain-inbox/w440/bundle_001.json")
assert inbox.read_bytes() == bundle_path.read_bytes()
print("rank_model_qualifier", int("site" in raw or "bond" in raw))
print("rank_pc_lt_1_qualifier", int("p_c < 1" in raw or "pc<1" in raw))
print(
    "draft_model_qualified_nodes",
    sum("site" in e["statement"].lower() or "bond" in e["statement"].lower() for e in bundle["entries"]),
)
print(
    "draft_pc_lt_1_nodes",
    sum(
        "p_c(g)<1" in e["statement"].lower()
        or "p_c(g) is below 1" in e["statement"].lower()
        for e in bundle["entries"]
    ),
)
print("draft_nodes", len(bundle["entries"]), "draft_relations", len(bundle["relations"]))
print("review_rows", len(claims), "inbox_bytes", inbox.stat().st_size)
