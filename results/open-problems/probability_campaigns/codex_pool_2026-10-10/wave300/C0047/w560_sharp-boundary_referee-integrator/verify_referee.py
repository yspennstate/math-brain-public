"""Small exact arithmetic and packet-structure checks for the referee handoff."""
import json
from fractions import Fraction as F
from pathlib import Path
from time import perf_counter

start = perf_counter()
root = Path(__file__).resolve().parent

def mean(p):
    return 2*p*p + 2*p**3 - 2*p**4

assert mean(F(1, 2)) == F(5, 8)
assert mean(F(2, 3)) == F(88, 81)
assert mean(F(63, 100)) < 1 < mean(F(64, 100))
assert 2*F(63, 100) > 1
assert F(1, 3)*(2*(1+F(1, 3))/(1-F(1, 3))-1) == 1
assert F(4, 3) > 1  # square of 2*sqrt(3)/3 on the 4-regular tree

status = json.loads((root / "SOURCE_STATUS.json").read_text(encoding="utf-8"))
bundle = json.loads((root / "draft_bundle_001.json").read_text(encoding="utf-8"))
state = json.loads((root / "BUNDLE_STATE.json").read_text(encoding="utf-8"))
claims = [json.loads(s) for s in (root / "CLAIMS.jsonl").read_text(encoding="utf-8").splitlines()]
verdicts = [json.loads(s) for s in (root / "REVIEW_VERDICTS.jsonl").read_text(encoding="utf-8").splitlines()]
hooks = [json.loads(s) for s in (root / "HOOK_PROPOSAL.jsonl").read_text(encoding="utf-8").splitlines()]
assert status["id"] == "C0047" and status["model_scope"]["site_current_openness"] == "UNKNOWN"
assert bundle["spec"] == "mathbrain-draft-v1" and len(bundle["entries"]) == 2 and len(bundle["relations"]) == 1
assert all(e["source"]["license"].startswith("owner-own-work") for e in bundle["entries"])
assert all(v["verdict"] == "KEEP" for v in verdicts) and len(verdicts) == 10
assert len(hooks) == 1 and len(hooks[0]["text"]) <= 300
assert not any(state[k] for k in ("submitted", "reviewed", "ingested", "retrievable"))
assert len(claims) >= 4
print(json.dumps({"status":"PASS","exact_checks":6,"review_verdicts":len(verdicts),"claims":len(claims),"bundle_entries":2,"bundle_relations":1,"hook_proposals":1,"elapsed_seconds":round(perf_counter()-start,6)}))
