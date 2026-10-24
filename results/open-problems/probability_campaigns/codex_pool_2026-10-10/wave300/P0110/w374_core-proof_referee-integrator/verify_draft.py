"""Validate the handoff format and exact finite checks; not a formal FPP proof."""

import json
from fractions import Fraction
from pathlib import Path

root = Path(__file__).resolve().parent
bundle = json.loads((root / "DRAFT_BUNDLE.json").read_text(encoding="utf-8"))
assert bundle["spec"] == "mathbrain-draft-v1"
assert bundle["author_agent"] == "w374"
assert 0 < len(bundle["entries"]) <= 200
keys = {entry["key"] for entry in bundle["entries"]}
assert len(keys) == len(bundle["entries"])
for entry in bundle["entries"]:
    assert entry["namespace"] == "probability.core"
    assert entry["kind"] in {"concept", "lemma", "theorem", "definition"}
    assert bool(entry["proof_text"]) == (entry["kind"] in {"lemma", "theorem"})
    assert entry["source"]["license"].startswith("owner-own-work")
    assert entry["statement"] and entry["logical_name"] and entry["assumptions"]
for relation in bundle["relations"]:
    assert relation["from_key"] in keys and relation["to_key"] in keys
    assert relation["kind"] == "semantic_association" and relation["rationale"]

rare_checks = 0
for m in (2, 3, 10, 100, 1000):
    n = m**3
    var = Fraction(n-1, n) * m**2 + Fraction(1, n) * m**4
    assert var == Fraction(m**2) + Fraction(m) - Fraction(1, m)
    rare_checks += 1

print(json.dumps({"schema": "PASS", "entries": len(bundle["entries"]),
                  "relations": len(bundle["relations"]), "rare_variance_checks": rare_checks,
                  "live_ingestion_checked": False}))
