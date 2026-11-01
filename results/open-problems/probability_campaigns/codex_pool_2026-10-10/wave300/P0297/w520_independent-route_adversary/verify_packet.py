"""Bounded exact diagnostics; this is not a proof certificate or live integrator."""
from __future__ import annotations

from fractions import Fraction as R
from pathlib import Path
import json
import time

ROOT = Path(__file__).resolve().parent
started = time.perf_counter()
gate = json.loads((ROOT / "COMPUTE_GATE.json").read_text(encoding="utf-8"))
assert str(ROOT).replace("\\", "/") == gate["allowed_write_root"]
bundle_path = ROOT / "drafts" / "bundle_001.json"
bundle = json.loads(bundle_path.read_text(encoding="utf-8"))
assert bundle["spec"] == "mathbrain-draft-v1"
assert bundle["author_agent"] == "w520"
assert len(bundle["entries"]) == gate["limits"]["max_entries"]
required = {"key", "namespace", "logical_name", "kind", "title", "statement",
            "proof_text", "assumptions", "domain", "source"}
keys = set()
for entry in bundle["entries"]:
    assert required <= entry.keys()
    assert entry["key"] not in keys
    keys.add(entry["key"])
    assert entry["kind"] == "concept" and entry["proof_text"] is None
    assert entry["statement"].startswith("DRAFT")
    assert entry["assumptions"] and len(entry["statement"]) > 100
    source = entry["source"]
    assert {"source_id", "url", "revision", "license"} <= source.keys()
    assert source["license"].startswith("owner-own-work")
    local_source = Path(source["url"].removeprefix("file:///"))
    assert local_source.resolve().is_relative_to(ROOT) and local_source.is_file()

context = json.loads((ROOT / "reports" / "context_receipt.json").read_text(encoding="utf-8"))
assert context["readonly_uri"] and context["query_only"]
existing = {card["logical_id"] for card in context["cards"]}
for edge in bundle["relations"]:
    assert edge["from_key"] in keys
    if "to_key" in edge:
        assert edge["to_key"] in keys
    else:
        assert edge["to_existing_logical"] in existing
    assert edge["kind"] == "semantic_association" and edge["rationale"]

claims = [json.loads(line) for line in (ROOT / "CLAIMS.jsonl").read_text(encoding="utf-8").splitlines() if line.strip()]
assert len({c["id"] for c in claims}) == len(claims)
for claim in claims:
    assert {"id", "exact_statement", "assumptions", "source", "proof_or_counterexample",
            "independent_reviewer", "remaining_gap", "status"} <= claim.keys()
    assert not claim["ingested"] and not claim["retrievable"]
    if claim["id"].endswith(".002") or claim["id"].endswith(".003"):
        assert claim["reviewed"] is False

gammas = [R(1,100), R(1,4), R(1,2), R(3,4), R(1), R(3,2), R(7,4), R(19,10), R(199,100)]
xis = [R(1,13), R(1,6), R(1,3), R(2,5)]
base_alphas = [R(k,4) for k in range(-8,9)]
cases = 0
maxima = 0
for gamma in gammas:
    q = 2/gamma + gamma/2
    assert q > 2
    for xi in xis:
        alphas = sorted(set(base_alphas + [gamma]))
        values = []
        for alpha in alphas:
            assert q-alpha > 0
            f = (2-alpha*alpha/2)/(xi*(q-alpha))
            deficit = gamma/xi-f
            assert deficit == (alpha-gamma)**2/(2*xi*(q-alpha))
            assert deficit >= 0
            assert (deficit == 0) == (alpha == gamma)
            values.append(f)
            cases += 1
        assert max(values) == gamma/xi
        assert values[0] == 0 and values[-1] == 0
        # Check the two metric-KPZ quadratic roots without floating point.
        root_1, root_2 = gamma, 4/gamma
        for root in (root_1, root_2):
            assert q*root-root*root/2 == 2
        assert root_1 < q < root_2
        maxima += 1

assert cases <= gate["limits"]["max_profile_cases"]
critical_denominator = R(2,2) + R(2,2) - 2
assert critical_denominator == 0  # gamma=2, alpha=2 is explicitly excluded.
snowflake_scalar_checks = 0
for a in (R(1,3), R(1,2), R(2,3)):
    for gamma in gammas:
        for d in (R(2), R(4)):
            xi = gamma/d
            assert (a*xi)*(d/a) == gamma
            snowflake_scalar_checks += 1
partition_lengths = [1,2,4,8,16]
assert all(x < y for x,y in zip(partition_lengths, partition_lengths[1:]))

target = "~/math-brain-inbox/w520/bundle_001.json"
lines = bundle_path.read_text(encoding="utf-8").splitlines()
patch = "--- a/"+target+"\n+++ b/"+target+"\n@@ -0,0 +1,"+str(len(lines))+" @@\n"
patch += "\n".join("+"+line for line in lines)+"\n"
(ROOT / "patches").mkdir(exist_ok=True)
(ROOT / "patches" / "01_p0297_draft_bundle.diff").write_text(patch, encoding="utf-8")
reconstructed = "\n".join(line[1:] for line in patch.splitlines()[3:])+"\n"
assert reconstructed == bundle_path.read_text(encoding="utf-8")
hook = json.loads((ROOT / "hooks" / "proposals" / "math-w520.jsonl").read_text(encoding="utf-8"))
assert {"id", "area", "event", "cue", "fire_when", "silent_when", "text", "evidence", "proposer"} <= hook.keys()
assert hook["area"] == "math" and hook["proposer"] == "w520"
assert len(hook["text"]) <= 300 and hook["fire_when"] != hook["silent_when"]
lifecycle = {"bundle":"bundle_001.json", "prepared":True, "submitted":False,
             "reviewed":False, "ingested":False, "retrievable":False,
             "intended_destination":target, "staged_location":str(bundle_path),
             "reviewer":"w521", "integration_owner":"claude-4a88bc43",
             "reason_not_submitted":"Write-only-inside-worker-folder restriction; no shared mutation or live integration performed"}
(ROOT / "drafts" / "lifecycle.json").write_text(json.dumps(lifecycle,indent=2)+"\n", encoding="utf-8")
elapsed = time.perf_counter()-started
assert elapsed < gate["limits"]["max_seconds_inside_script"]
result = {"command":"python -X utf8 ~/brain_workers/w520/verify_packet.py",
          "exact_profile_cases":cases, "unique_maximum_cases":maxima,
          "kpz_root_checks":2*maxima, "snowflake_scalar_checks":snowflake_scalar_checks,
          "snowflaked_interval":{"a":"1/2","equal_partition_sizes":[1,4,16,64,256],"lengths":partition_lengths},
          "draft_entries":len(bundle["entries"]), "draft_relations":len(bundle["relations"]),
          "claim_rows":len(claims), "existing_endpoints_verified":len(existing),
          "patch_reconstruction_equal":True, "hook_proposals_validated":1,
          "new_theorems_promoted":0, "live_store_writes":0,
          "integration_or_recall_improvement_claim":False,
          "elapsed_seconds":round(elapsed,6), "formal_certificate":False,
          "result":"PASS: exact diagnostic instances and local handoff checks; independent mathematical review still required"}
(ROOT / "measurements.json").write_text(json.dumps(result,indent=2)+"\n", encoding="utf-8")
print(json.dumps(result,indent=2))
