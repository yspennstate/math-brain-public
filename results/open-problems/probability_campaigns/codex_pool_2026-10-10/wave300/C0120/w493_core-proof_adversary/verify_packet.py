"""Validate draft packaging and explicit proof gaps; never integrate a store."""
import hashlib
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent
checks = []
def check(name, condition):
    if not condition:
        raise AssertionError(name)
    checks.append(name)

bundle = json.loads((ROOT / "bundle_001.json").read_text(encoding="utf-8"))
check("draft schema", bundle["spec"] == "mathbrain-draft-v1")
check("author identity", bundle["author_agent"] == "w493")
check("two disjoint entries", len(bundle["entries"]) == 2)
keys = {e["key"] for e in bundle["entries"]}
check("unique keys", len(keys) == 2)
allowed_relations = {"depends_on", "defines", "proves", "refutes", "generalizes", "specializes",
                     "analogous_to", "cites", "semantic_association"}
required = {"key", "namespace", "logical_name", "kind", "title", "statement", "proof_text",
            "assumptions", "domain", "source"}
for e in bundle["entries"]:
    check(e["key"]+" fields", required <= e.keys())
    check(e["key"]+" concept only", e["kind"] == "concept" and e["proof_text"] is None)
    check(e["key"]+" explicit draft status", "UNREVIEWED" in e["statement"])
    check(e["key"]+" complete source model", "origin" in e["statement"] and "Gaussian" in e["statement"])
    check(e["key"]+" source tag", e["source"]["license"].startswith("owner-own-work"))
    check(e["key"]+" logical name", re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", e["logical_name"]) is not None)
for rel in bundle["relations"]:
    check("relation endpoints", rel["from_key"] in keys and rel["to_key"] in keys)
    check("allowed relation", rel["kind"] in allowed_relations)
    check("nonempty rationale", bool(rel["rationale"]))
evidence = json.loads((ROOT / "RELATION_EVIDENCE.jsonl").read_text(encoding="utf-8"))
by_key = {e["key"]: e for e in bundle["entries"]}
check("exact quoted relation from", evidence["from_statement"] == by_key[evidence["relation"]["from_key"]]["statement"])
check("exact quoted relation to", evidence["to_statement"] == by_key[evidence["relation"]["to_key"]]["statement"])
claims = [json.loads(x) for x in (ROOT / "CLAIMS.jsonl").read_text(encoding="utf-8").splitlines() if x.strip()]
check("five exact claim rows", len(claims) == 5)
check("no solved parent", all(c["parent_problem_solved"] is False for c in claims))
check("all claims have honest review state", all(c["review_state"] in {"pending", "scoped KEEP by w494"} for c in claims))
check("independent-check label has evidence", all(c["status"] != "independently checked proof" or (c["independent_reviewer"] == "w494" and c.get("review_evidence")) for c in claims))
check("source fidelity not mathematical proof", next(c for c in claims if c["claim_id"].endswith("002"))["mathematical_proof_claim"] is False)
audits = [json.loads(x) for x in (ROOT / "AUDIT_VERDICTS.jsonl").read_text(encoding="utf-8").splitlines() if x.strip()]
check("four scoped KEEP rows", sum(a["verdict"] == "KEEP" for a in audits) == 4)
check("hardest input unproved", any(a["claim"] == "w492-G1" and a["verdict"] == "UNPROVED" for a in audits))
source = json.loads((ROOT / "SOURCE_STATUS.json").read_text(encoding="utf-8"))
check("primary body checked", source["primary_source"]["body_verified"])
check("openness remains unknown", source["current_openness"] == "UNKNOWN")
check("served identity not invented", source["served_identity"]["author"] == "UNVERIFIED")
check("independent derivation unchanged", hashlib.sha256((ROOT / "ATTEMPT.md").read_bytes()).hexdigest() == source["independent_save_sha256_before_peer_read"])
measurements = json.loads((ROOT / "MEASUREMENTS.json").read_text(encoding="utf-8"))
check("116 exact finite checks", measurements["all_finite_checks_passed"] and measurements["exact_checks"] == 116)
check("measurements are not formal proof", measurements["measurement_is_not_formal_proof"])
hook = json.loads((ROOT / "HOOK_PROPOSAL.jsonl").read_text(encoding="utf-8"))
check("hook schema", {"id", "area", "event", "cue", "fire_when", "silent_when", "text", "evidence", "proposer"} <= hook.keys())
check("hook text cap", len(hook["text"]) <= 300)
check("hook has both controls", bool(hook["fire_when"]) and bool(hook["silent_when"]))

patch_dir = ROOT / "patches"
patch_dir.mkdir(exist_ok=True)
live = "~/primary_directive/hooks1000/proposals/polymer-overlap-floor-w493.jsonl"
patch = f"--- a/{live}\n+++ b/{live}\n@@ -0,0 +1 @@\n+"+json.dumps(hook)+"\n"
(patch_dir / "01_polymer_overlap_floor_hook.diff").write_text(patch, encoding="utf-8")
receipt = {"packaging_checks_passed": len(checks), "checks": checks,
           "mathematical_proof_certified": False, "formal_checker_invoked": False,
           "admitted_placeholders_counted": False, "parent_problem_solved": False,
           "independent_saved_artifact_sha256": source["independent_save_sha256_before_peer_read"],
           "command": "python -X utf8 ~/brain_workers/w493/verify_packet.py"}
(ROOT / "CHECK_RECEIPT.json").write_text(json.dumps(receipt, indent=2)+"\n", encoding="utf-8")
print(json.dumps({"packaging_checks_passed": len(checks), "mathematical_proof_certified": False,
                  "parent_problem_solved": False}))
