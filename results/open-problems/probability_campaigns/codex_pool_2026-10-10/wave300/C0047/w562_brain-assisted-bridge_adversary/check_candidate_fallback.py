"""Target-only validation on the authorized store in read-only mode."""
import importlib.util
import json
from pathlib import Path
import sys

sys.dont_write_bytecode=True
root=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location("candidate_fallback",root/"proposed/math_brain/target_fallback.py")
module=importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
database=Path("~/math-brain-build/local/population/brain.sqlite3")
record=module.lookup_candidate(database,"C0047")
expected={"claim_0bfe0a8a0e527dd20457f2c0393cb560907546ec53a1204204de0fc82235d788","claim_77d417df1817eac0893d67dcfcf0d7140581f4e26ce07c31919403d44d301960"}
assert {c["id"] for c in record["cards"]}==expected
assert all(c["body"] and c["metadata"]["truth_status"]=="unverified" for c in record["cards"])
assert record["read_only"] and "No proof certification" in record["warning"]
invalid=0
for candidate in ("c0047","C0047' OR 1=1 --","C00470",""):
    try:module.lookup_candidate(database,candidate)
    except ValueError:invalid+=1
    else:raise AssertionError("invalid candidate accepted")
empty=module.lookup_candidate(database,"Z9999")
assert not empty["cards"]
baseline=json.loads((root/"math_recall_output.json").read_text(encoding="utf-8"))
baseline_hits={h["id"] for h in baseline["hits"]}
measurement={"command":"python -X utf8 ~/brain_workers/w562/check_candidate_fallback.py","baseline_expected_cards_in_top6":len(expected&baseline_hits),"expected_cards":len(expected),"fallback_expected_cards":len(expected&{c["id"] for c in record["cards"]}),"fallback_elapsed_seconds":record["elapsed_seconds"],"fallback_budget_seconds":record["budget_seconds"],"invalid_inputs_rejected":invalid,"absent_candidate_cards":len(empty["cards"]),"all_checks_passed":True,"scope":"One known target; prior candidate ID and two metadata keys supplied. This is not a global ranking, latency, or theorem-accuracy benchmark.","fallback_result":record}
(root/"fallback_measurement.json").write_text(json.dumps(measurement,indent=2,ensure_ascii=False),encoding="utf-8")
print(json.dumps({k:v for k,v in measurement.items() if k!="fallback_result"},indent=2))
