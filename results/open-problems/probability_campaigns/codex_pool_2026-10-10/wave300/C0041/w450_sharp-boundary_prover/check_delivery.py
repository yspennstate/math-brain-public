"""Check local deliverables and bind proof evidence; never open a live store."""
from pathlib import Path
from fractions import Fraction as F
import hashlib
import json

ROOT = Path(__file__).resolve().parent
bundle = json.loads(ROOT.joinpath("draft/bundle_001.json").read_text(encoding="utf-8"))
claims = [json.loads(line) for line in ROOT.joinpath("CLAIMS.jsonl").read_text(encoding="utf-8").splitlines()]
receipt = json.loads(ROOT.joinpath("exact_receipt.json").read_text(encoding="utf-8"))
states = json.loads(ROOT.joinpath("SUBMISSION_STATE.json").read_text(encoding="utf-8"))
source = json.loads(ROOT.joinpath("SOURCE_STATUS.json").read_text(encoding="utf-8"))
hook = json.loads(ROOT.joinpath("hook_proposals/probability-boundary-w450.jsonl").read_text(encoding="utf-8"))
assert receipt["status"] == "PASS" and receipt["cases"] == 973
assert F(receipt["counterexample"]["mean_one_step_drift"]) > 0 > F(receipt["counterexample"]["kalikow_drift"])
assert F(receipt["rare_bias_bound"]["binary_bound"])/F(receipt["rare_bias_bound"]["generic_bound"]) == F(425,43)
assert len(claims) == 7 and len({c["id"] for c in claims}) == 7
assert claims[-1]["status"] == "conjecture" and source["current_openness"] == "UNKNOWN"
assert not source["recent_resolution_claim"]["lean_build_run"]
assert bundle["spec"] == "mathbrain-draft-v1" and bundle["author_agent"] == "w450"
allowed = {"depends_on","defines","proves","refutes","generalizes","specializes","analogous_to","cites","semantic_association"}
keys = {e["key"] for e in bundle["entries"]}
assert len(keys) == len(bundle["entries"]) == 7
for entry in bundle["entries"]:
    assert entry["kind"] in {"definition","concept"} and entry["proof_text"] is None
    assert entry["source"]["license"].startswith("owner-own-work")
    assert entry["statement"] and entry["assumptions"]
    if entry["kind"] == "concept":
        assert any(label in entry["statement"] for label in ("DRAFT","REFUTED","STATUS NOTE"))
edges = {key:[] for key in keys}
for relation in bundle["relations"]:
    assert relation["from_key"] in keys and relation["kind"] in allowed
    if "to_key" in relation:
        assert relation["to_key"] in keys
    else:
        assert relation["to_existing_logical"].startswith("math:probability.randomenvironment:open-problem-c0041-")
    if relation["kind"] == "depends_on":
        edges[relation["from_key"]].append(relation["to_key"])
    if relation["kind"] == "refutes":
        assert relation["from_key"] == "two-site-obstruction" and relation["to_key"] == "false-bridge"
def walk(key, visiting, visited):
    assert key not in visiting, "cyclic depends_on relations"
    if key in visited:
        return
    visiting.add(key)
    for target in edges[key]:
        walk(target,visiting,visited)
    visiting.remove(key)
    visited.add(key)
visited = set()
for key in keys:
    walk(key,set(),visited)
for patch_name, staged, live in (
    ("01_c0041_draft.diff","draft/bundle_001.json","~/math-brain-inbox/w450/bundle_001.json"),
    ("02_probability_hook.diff","hook_proposals/probability-boundary-w450.jsonl","~/primary_directive/hooks1000/proposals/probability-boundary-w450.jsonl")):
    patch = ROOT.joinpath("patches",patch_name).read_text(encoding="utf-8")
    assert patch.startswith("--- a/"+live+"\n+++ b/"+live+"\n")
    # These are all-addition diffs; reconstruct their complete intended contents.
    restored = "\n".join(line[1:] for line in patch.splitlines()[3:] if line.startswith("+"))+"\n"
    assert restored == ROOT.joinpath(staged).read_text(encoding="utf-8")
assert len(hook["text"]) <= 300 and hook["fire_when"] and hook["silent_when"] and hook["evidence"]
assert states["prepared"] and not any(states[k] for k in ("submitted","reviewed","ingested","retrievable"))
files = ["ATTEMPT.md","CLAIMS.jsonl","SOURCE_STATUS.json","exact_receipt.json","verify_exact.py",
 "draft/bundle_001.json","patches/01_c0041_draft.diff","patches/02_probability_hook.diff",
 "hook_proposals/probability-boundary-w450.jsonl","REVIEW_PACKET.md","REPORT.md","check_delivery.py"]
hashes = {"purpose":"Review artifact byte bindings only; not integrator source manifests or proof certificates.",
 "files":{name:hashlib.sha256(ROOT.joinpath(name).read_bytes()).hexdigest() for name in files}}
ROOT.joinpath("REVIEW_HASHES.json").write_text(json.dumps(hashes,indent=2)+"\n",encoding="utf-8")
result = {"status":"PASS","claims":len(claims),"draft_entries":len(keys),"relations":len(bundle["relations"]),
 "patches":2,"hook_controls":2,"proof_evidence_files_bound":len(files),"live_store_writes":0,"formal_theorem_check":False}
ROOT.joinpath("delivery_receipt.json").write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
print(json.dumps(result))
