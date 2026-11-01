"""Finish the local review packet after a successful authorized draft submission."""
import json
import shutil
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent
submission_path = ROOT / "SUBMISSION.json"
submission = json.loads(submission_path.read_text(encoding="utf-8"))
assert submission["submitted"] and not submission["ingested"]
submitted = json.loads(Path(submission["draft_path"]).read_text(encoding="utf-8"))
assert submitted == json.loads((ROOT / "bundle_001.json").read_text(encoding="utf-8"))
audit_path = Path("~/brain_workers/w550/AUDIT_W549.md")
audit_text = audit_path.read_text(encoding="utf-8")
assert "KEEP" in audit_text.upper()
second = {"reviewer": "w550", "source": str(audit_path), "message_scope": "KEEP G1-G6 conditionally", "verdict": "KEEP", "phase_existence_kept": False, "different_login_verified": False, "review_text": audit_text}
(ROOT / "SECOND_AUDIT_RECEIPT.json").write_text(json.dumps(second, ensure_ascii=False, indent=2), encoding="utf-8")
submission["partial_mathematical_keep"].update(reviewers=["w551", "w550"], additional_evidence=str(audit_path), different_logins_verified=False)
submission_path.write_text(json.dumps(submission, indent=2), encoding="utf-8")
source_path = ROOT / "SOURCE_STATUS.json"
source = json.loads(source_path.read_text(encoding="utf-8"))
source["independent_review"].update(status="partial: w551 and w550 conditional KEEP for G1-G6", additional_evidence=str(audit_path), account_independence_verified=False)
source["recent_primary_check"] = {
    "authors": "Pawel Matus and Tobias Holder",
    "title": "Theory of two-dimensional Wigner crystals with defects: Interactions, melting transitions and collective modes",
    "version": "arXiv:2607.18477v1, 2026-07-20",
    "url": "https://arxiv.org/html/2607.18477v1",
    "locators_checked": ["abstract", "II model and quadratic effective action", "IV opening KTHNY/dislocation-proliferation discussion"],
    "short_quote": "a zero-temperature version of the hexatic Wigner crystal",
    "scope_inference": "The checked passages use an elastic effective action and a KTHNY phase description; no microscopic positive-temperature classical Riesz DLR phase-existence theorem was recovered from these passages. This is a limited scope check, not a proof of absence from all literature.",
}
source_path.write_text(json.dumps(source, ensure_ascii=False, indent=2), encoding="utf-8")
claim_path = ROOT / "CLAIMS.jsonl"
claims = [json.loads(line) for line in claim_path.read_text(encoding="utf-8").splitlines() if line.strip()]
for claim in claims:
    if claim["id"] in {"w549-P0321-G1", "w549-P0321-G3", "w549-P0321-G5"}:
        claim["additional_independent_reviewer"] = "w550"
        claim["additional_review_evidence"] = str(audit_path)
        claim["different_logins_verified"] = False
if not any(claim["id"] == "w549-P0321-M1" for claim in claims):
    claims.append({"id": "w549-P0321-M1", "kind": "measured-retrieval-failure", "statement": "The bounded strong-mixing title query returned only a qualitative dynamical mixing definition for a measure-preserving map and fixed event pairs. It supplied no quantitative all-local-event, growing-window, Delaunay-stabilization, or void-tail theorem needed for the P0321 bond-covariance bridge.", "assumptions": ["targeted title LIKE queries only; not a full retrieval benchmark or proof of global card absence"], "source": {"path": "brain_cards.json", "logical_id": "math:dynamics.ergodic:mixing-definition", "command": "python -X utf8 retrieve_cards.py"}, "proof_or_counterexample": "Complete card body/metadata comparison in HYPOTHESIS_COMPARISON.md; three cards returned in 0.2551538 seconds, zero applicable quantitative theorem bridges. The separate memory recall returned zero output after its 60-second budget.", "independent_reviewer": "w551 (scope audit pending)", "remaining_gap": "No post-ingestion retrieval benchmark; new scoped entries and gate are drafts/proposals.", "status": "sketch", "review_state": "unreviewed measurement", "bounded_repair": "Explicit local-event alpha definition, geometric localization proof, and hypothesis-scope gate, with no live global changes."})
claim_path.write_text("".join(json.dumps(claim, ensure_ascii=False)+"\n" for claim in claims), encoding="utf-8")
for name in ("REPORT.md", "ATTEMPT.md", "REVIEW_PACKET.md", "BRIDGE_PROOF.md"):
    path = ROOT / name
    body = path.read_text(encoding="utf-8")
    body = body.replace("Referee w551 independently kept", "Referees w551 and w550 independently kept")
    body = body.replace("G1-G6 independently kept by w551", "G1-G6 independently kept by w551 and w550")
    path.write_text(body, encoding="utf-8")
report_path = ROOT / "REPORT.md"
report = report_path.read_text(encoding="utf-8")
report = report.replace("The small draft has", "The submitted draft is ~/math-brain-inbox/w549/bundle_001.json. Both peer IDs kept G1-G6 conditionally; distinct logins have not been verified, so no two-account admission is claimed. The small draft has")
report_path.write_text(report, encoding="utf-8")
packet = ROOT / "review_packet"
packet.mkdir(exist_ok=True)
files = ["REVIEW_PACKET.md", "REPORT.md", "STATEMENT_FIRST.md", "SOURCE_STATUS.json", "ATTEMPT.md", "BRIDGE_PROOF.md", "CLAIMS.jsonl", "RELATIONS.jsonl", "REASONING_FAILURE.md", "HYPOTHESIS_COMPARISON.md", "brain_cards.json", "verification.json", "compute_gate.json", "recall_measurement.json", "canonical_target_probe.json", "AUDIT_RECEIPT.json", "SECOND_AUDIT_RECEIPT.json", "SUBMISSION.json", "draft_validation.json", "bundle_001.json", "verify_bridge.py", "proposed/bridge_hypothesis_gate.py", "patches/01_bridge_hypothesis_gate.diff", "patches/02_probability_hook.diff", "proposals/probability-w549.jsonl", "PROGRESS_EVENT.json"]
for relative in files:
    destination = packet / relative
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(ROOT / relative, destination)
(packet / "README.md").write_text("Start with REVIEW_PACKET.md and REPORT.md. The code and hook patches are proposals; the math draft is submitted, partially kept, not ingested. Exact checks: python -X utf8 verify_bridge.py. The last proof gap is a nonzero microscopic Riesz orientational lower bound.\n", encoding="utf-8")
assert all({"statement", "assumptions", "source", "proof_or_counterexample", "independent_reviewer", "remaining_gap", "status"} <= set(claim) for claim in claims)
status_path = ROOT / "STATUS.md"
old = status_path.read_text(encoding="utf-8-sig").splitlines()
log = "\n".join(line for line in old[2:] if not line.startswith("STATE:") and not line.startswith("NEXT:"))
now = datetime.now(timezone.utc).isoformat()
status_path.write_text("STATE: NEEDS_REVIEW\nNEXT: Finish K1/gate/edge admission audits; next proof step is a microscopic Riesz six-fold orientational lower bound.\n"+log+"\n"+now+": Submitted 8-entry/8-relation draft, four proof-bearing entries; w551 and w550 conditionally kept G1-G6. Exact checks PASS; code/hook proposals and complete review_packet saved. No P0321 solution, live-store write, ingestion, new-node retrievability, or verified distinct-login admission claimed.\n", encoding="utf-8")
receipt = {"state": "NEEDS_REVIEW", "review_packet": str(packet), "files": len(files)+1, "claim_rows": len(claims), "draft_entries": len(submitted["entries"]), "draft_relations": len(submitted["relations"]), "conditional_keeps": ["w551", "w550"], "ingested": False, "phase_existence_proved": False}
(ROOT / "DELIVERY.json").write_text(json.dumps(receipt, indent=2), encoding="utf-8")
print(json.dumps(receipt, indent=2))
