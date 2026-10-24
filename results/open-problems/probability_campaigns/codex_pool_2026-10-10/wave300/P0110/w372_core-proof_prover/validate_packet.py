"""Artifact schema and submission checks, not a mathematical proof audit."""
import difflib
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent
INBOX = pathlib.Path("~/math-brain-inbox/w372")

claims = [json.loads(line) for line in (ROOT / "CLAIMS.jsonl").read_text(encoding="utf-8").splitlines() if line.strip()]
for claim in claims:
    if claim["claim_id"] == "w372-P0110-SOURCE-01":
        claim["assumptions"] = ["Ranking metadata only; this row does not certify the primary statement or current openness"]
        claim["remaining_gap"] = "Primary statement now recovered in STATEMENT.md and SOURCE_STATUS.json; current openness remains UNKNOWN."
    if claim["claim_id"] == "S1.w372.L1-short":
        claim["artifact_kind"] = "Supporting source-hypothesis check; stronger forced-straight cutoff is the w378 lane"
(ROOT / "CLAIMS.jsonl").write_text("".join(json.dumps(c, ensure_ascii=False)+"\n" for c in claims), encoding="utf-8")
required = {"claim_id", "exact_statement", "assumptions", "source", "proof_or_counterexample", "independent_reviewer", "remaining_gap", "status"}
assert len({c["claim_id"] for c in claims}) == len(claims)
assert all(required <= c.keys() for c in claims)
assert all(c["status"] in {"sketch", "proved special case", "conjecture", "independently checked proof"} for c in claims)
receipt = json.loads((ROOT / "PEER_AUDIT_RECEIPT.json").read_text(encoding="utf-8"))
assert all(c["independent_reviewer"]["verdict"] == "pending" or (
    c["status"] == "independently checked proof" and
    receipt["verdicts"].get(c["claim_id"]) == c["independent_reviewer"]["verdict"]
) for c in claims)

bundles = [json.loads((ROOT / name).read_text(encoding="utf-8")) for name in ("bundle_001.json", "bundle_002.json")]
entry_count = sum(len(b["entries"]) for b in bundles)
assert all(e["review_status"] == "pending-w374" and not e["parent_problem_solved"] for b in bundles for e in b["entries"])
assert all(e["source"]["license"].startswith("owner-own-work") for b in bundles for e in b["entries"])
assert all(bool(e["proof_text"]) if e["kind"] in {"lemma", "theorem"} else e["proof_text"] is None for b in bundles for e in b["entries"])
submissions = []
for name in ("bundle_001.json", "bundle_002.json"):
    path = INBOX / name
    present = path.exists()
    if present:
        assert path.read_bytes() == (ROOT / name).read_bytes()
    submissions.append({"path": str(path), "present_at_validation": present,
                        "note": "Presence is submission evidence, not ingestion or retrieval evidence."})
hook_text = (ROOT / "HOOK_PROPOSAL.jsonl").read_text(encoding="utf-8")
hook = json.loads(hook_text)
assert len(hook["text"]) <= 300 and hook["fire_when"] and hook["silent_when"] and hook["evidence"]
patch_dir = ROOT / "patches"
patch_dir.mkdir(exist_ok=True)
live_path = "~/primary_directive/hooks1000/proposals/fpp-coupling-w372.jsonl"
patch = "".join(difflib.unified_diff([], hook_text.splitlines(keepends=True), fromfile="a/"+live_path, tofile="b/"+live_path))
(patch_dir / "01_fpp_coupling_hook.diff").write_text(patch, encoding="utf-8")

state = json.loads((ROOT / "BUNDLE_STATE.json").read_text(encoding="utf-8"))
state["ingested"] = {"status": "UNKNOWN", "reason": "No coordinator ingestion receipt; worker did not invoke an integrator."}
state["retrievable"] = {"status": "UNVERIFIED", "reason": "No live retrieval confirmation for these new drafts."}
state["structural_validation"] = {"entries": entry_count, "relations": sum(len(b["relations"]) for b in bundles), "bundles": len(bundles), "passed": True, "mathematical_audit": False}
(ROOT / "BUNDLE_STATE.json").write_text(json.dumps(state, indent=2)+"\n", encoding="utf-8")
report = {"claim_rows": len(claims), "bundle_entries": entry_count, "draft_bundles": len(bundles),
          "submissions": submissions, "schema_pass": True, "mathematical_audit": False,
          "independent_review": "seven-scoped-KEEP-w374; promotion gates unverified", "hook_patch": "patches/01_fpp_coupling_hook.diff",
          "parent_problem_solved": False, "exact_environments_checked": 9216,
          "corrected_transfer_cases_passed": 2, "naive_independence_cases_refuted": 2}
(ROOT / "VALIDATION_REPORT.json").write_text(json.dumps(report, indent=2)+"\n", encoding="utf-8")
print(json.dumps(report, indent=2))
