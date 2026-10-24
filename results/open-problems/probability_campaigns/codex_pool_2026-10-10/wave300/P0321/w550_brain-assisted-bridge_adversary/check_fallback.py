"""Small fresh-gate checks of the actual source locator and failure modes."""
import json
import pathlib
import time

from target_source_fallback import lookup

root = pathlib.Path(__file__).resolve().parent
source = "~/<private-repo>/06_math_research/probability_1000_intake_claude_20260907/brain_bundle_C006a05.json"
started = time.perf_counter()
result = lookup(source, "at-p0321", timeout=3)
elapsed = time.perf_counter()-started
assert result["state"] == "located", result
assert result["card"]["kind"] == "concept"
assert result["card"]["assumptions"] == ["Refers to the open problem node open-problem-p0321-existence-of-a-hexatic-phase-for-two-dimensional-riesz-gases", "No independent review"]
assert result["proof_witness"] is False and result["current_openness"] == "UNKNOWN"

fixture = root/"fallback_negative_fixture.json"
fixture.write_text('{"entries":[\n{\n"key": "p03210",\n"kind": "concept",\n"statement": "different ID",\n"assumptions": [],\n"source": {}\n},\n{\n"key": "duplicate",\n"kind": "concept",\n"statement": "first",\n"assumptions": [],\n"source": {}\n},\n{\n"key": "duplicate",\n"kind": "concept",\n"statement": "second",\n"assumptions": [],\n"source": {}\n}\n]}', encoding="utf-8")
prefix = lookup(fixture, "p0321", timeout=1)
duplicate = lookup(fixture, "duplicate", timeout=1)
assert prefix["state"] == "abstained"
assert duplicate["state"] == "abstained"

baseline = json.loads((root/"recall_measurement.json").read_text(encoding="utf-8"))
out = {"gate": "compute_gate.json", "commands": ["python -X utf8 recall_probe.py", "python -X utf8 check_fallback.py"],
       "baseline": {"timeout": baseline["timeout"], "seconds": baseline["seconds"], "output_bytes": len(baseline["stdout"].encode("utf-8")), "located_target_cards": 0},
       "exact_source_fallback": {"seconds": elapsed, "located_target_cards": 1, "source_line": result["source_line"], "card_kind": result["card"]["kind"], "proved_phase_witnesses": 0},
       "checks_passed": 3, "limitations": "One known-source exact locator case. Not a benchmark of ranked math recall, not a proof, and not an improvement deployed in the live brain."}
(root/"fallback_measurement.json").write_text(json.dumps(out, indent=2), encoding="utf-8")
(root/"retrieved_prior_card.json").write_text(json.dumps(result, indent=2), encoding="utf-8")
print(json.dumps(out))
