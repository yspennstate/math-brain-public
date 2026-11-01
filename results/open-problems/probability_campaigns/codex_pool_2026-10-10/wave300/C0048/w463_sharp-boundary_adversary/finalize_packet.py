"""Submit only the explicitly requested DRAFT inbox file and freeze local handoffs."""
from datetime import datetime, timezone
from pathlib import Path
import argparse
import hashlib
import json

root = Path(__file__).resolve().parent
parser = argparse.ArgumentParser()
parser.add_argument("--patch-check-exit-code", type=int, required=True)
args = parser.parse_args()
assert args.patch_check_exit_code == 0, "Do not finalize a failed patch check"
receipt = json.loads((root/"VALIDATION_RECEIPT.json").read_text(encoding="utf-8"))
assert receipt["preflight"] == "PASS" and receipt["unreviewed_theorem_entries"] == 0
raw = (root/"drafts/bundle_001.json").read_bytes()
bundle = json.loads(raw)
assert all(e["kind"] == "concept" and e["proof_text"] is None for e in bundle["entries"])

# This exact inbox directory is named in the worker's brief. No live store or
# integrator is opened. All other writes below stay in the worker folder.
inbox = Path("~/math-brain-inbox/w463")
assert inbox.parent.is_dir()
inbox.mkdir(exist_ok=True)
for number in range(1, 100):
    candidate = inbox/f"bundle_{number:03d}.json"
    assert candidate.parent.resolve() == inbox.resolve()
    if not candidate.exists() or candidate.read_bytes() == raw:
        destination = candidate
        break
else:
    raise RuntimeError("No unused draft name; existing drafts preserved")
if not destination.exists():
    part = destination.with_suffix(".json.part")
    assert part.parent.resolve() == inbox.resolve()
    part.write_bytes(raw)
    part.replace(destination)
assert destination.read_bytes() == raw
stamp = datetime.now(timezone.utc).isoformat()


def write_json(name, obj):
    (root/name).write_text(json.dumps(obj, indent=2)+"\n", encoding="utf-8")


write_json("DRAFT_LIFECYCLE.json", {"prepared": True, "submitted": {"value": True, "path": str(destination), "at_utc": stamp, "byte_identity_verified_against_local_draft": True}, "reviewed": {"value": False, "pending_referee": "w464"}, "ingested": "not observed", "retrievable": "not verified", "integrator_invoked_by_worker": False, "live_store_written_by_worker": False, "promotion": "All entries remain explicit review-pending concepts; proof/model/account gates remain pending."})
with (root/"REPORT.md").open("a", encoding="utf-8") as stream:
    stream.write(f"\nSubmitted the four-card concept DRAFT at {destination}; the complete .part file was renamed atomically and its bytes were checked against the local draft. Local preflight passed six claim rows, four concept entries, three exact-end relation records, and three scoped peer KEEP rows. The optional unified diff passed git apply --check in the local patch_check folder. Review, ingestion and recall retrieval have not been verified.\n\nTeam notifications failed twice because this worker has no registered team and the suggested integration team name was unavailable. Concrete handoffs are in review/HANDOFF_w464.md and review/HANDOFF_integration.md; no reply is awaited.\n\nNEXT: w464 verify the full-simplex barrier, perturbation bound, normalized allowance and critical-point qualifier; the validating coordinator may integrate only the permitted draft state.\n")

(root/"review/HANDOFF_w464.md").write_text(f"""w463 C0048 review packet is ready at {root}/REVIEW_PACKET.json.

Check Claims A/B/C in ATTEMPT.md independently: classify the interior stationary points and exclude boundary minima; establish the full-simplex x1=1/2 minimax lower bound; check the |J-J0|/3 perturbation estimate; verify n=2,kappa=2/3 and I_d>=1/(2d) against Biskup-Chayes. The resulting d=3 allowance is >=272.80465 Delta. The integer cutoff 819 is necessary for this coarse criterion, not sufficient and not a phase threshold.

Source Claim S1 is restricted to Theorem 2.1 and its following paragraph: identify J_t=J_c before inferring first-critical-point ordering. Own finite controls in Claim D preserve the distinction between ordinary paths and wired connectivity. Author proof and novelty remain unreviewed. The peer audit covers only w462 L1/L2/L3 in the frozen review/w462_ATTEMPT_reviewed.md snapshot.

Actual served-model/account evidence is unavailable; requested settings are not evidence. Return an exact scoped verdict and gaps on disk. No parent C0048 solution or theorem promotion is asserted.

NEXT: Verify the full-simplex minimax lower bound first, then the source normalization.
""", encoding="utf-8")
(root/"review/HANDOFF_integration.md").write_text(f"""For codex-01a12190: review-ready C0048 packet {root}/REVIEW_PACKET.json, report {root}/REPORT.md. Submitted DRAFT: {destination}. It contains four explicitly review-pending concept cards and three relations with exact supporting ends in RELATIONS_EVIDENCE.jsonl. w464 is the independent referee for author Claims A/B/C/D; the peer L1/L2/L3 audit has scoped mathematical KEEP only. No response-side served-model/account receipt is available. No full-target solved claim, live integration or recall-performance gain is claimed.

Publish the local PROGRESS_EVENT.json and hook proposal only through an authorized coordinator path; they stayed local under the worker-folder restriction. Team notices failed twice and the delivery fallback is this concrete on-disk handoff. Proof/model/account gates remain pending and ingestion/retrieval have not been observed.

NEXT: Route the frozen author proof to w464 and keep all bundle entries in concept/draft state until the corresponding gates pass.
""", encoding="utf-8")

# These are review artifact fingerprints, not bundle digests, source manifests,
# store seals or cryptographic ingestion ceremony.
files = ["ATTEMPT.md", "CLAIMS.jsonl", "SOURCE_STATUS.json", "REPORT.md", "PEER_AUDIT.md", "PEER_AUDIT.jsonl", "review/w462_ATTEMPT_reviewed.md", "MEASUREMENTS.json", "PEER_AUDIT_MEASUREMENTS.json", "VALIDATION_RECEIPT.json", "COMPUTE_GATE.json", "DRAFT_LIFECYCLE.json", "RELATIONS_EVIDENCE.jsonl", "patches/01_C0048_minimax_note.diff", "PATCH_PRECONDITION.md", "check_barrier.py", "check_peer_bound.py", "review/HANDOFF_w464.md", "review/HANDOFF_integration.md"]
artifacts = [{"path": str(root/name), "bytes": (root/name).stat().st_size, "review_sha256": hashlib.sha256((root/name).read_bytes()).hexdigest()} for name in files]
write_json("REVIEW_PACKET.json", {"candidate": "C0048", "author": "w463", "independent_referee": "w464", "prepared_at_utc": stamp, "scope": "exact three-state mean-field minimax special case, approximation-only bridge obstruction, normalized primary-source allowance and scoped peer-proof audit", "claims": ["w463-C0048-A", "w463-C0048-B", "w463-C0048-C", "w463-C0048-D", "w463-C0048-S0", "w463-C0048-S1"], "parent_problem_solved": False, "current_openness": "UNKNOWN", "novelty": "UNVERIFIED", "hardest_open_gap": "theta^wired(pc,3)>0 on actual nearest-neighbor Z^3", "own_proof_review_status": "pending w464", "peer_math_verdict": "KEEP L1/L2/L3 with the stated assumptions; not a parent-problem proof", "formal_check": {"performed": False, "trusted_axiom_receipt": None, "admitted_placeholder_used": False}, "served_identity": {"response_side_served_model_evidence": None, "account_evidence": None, "requested_model": "gpt-6.1-sol", "requested_reasoning": "max", "requested_service_tier": "Fast", "requested_settings_are_not_served_evidence": True, "different_model_review_gate": "pending"}, "checks": {"analytic_proof": str(root/"ATTEMPT.md"), "arithmetic_command": "python -X utf8 check_barrier.py", "exact_finite_controls_command": "python -X utf8 check_peer_bound.py", "preflight_command": "python -X utf8 validate_packet.py", "patch_command": "git apply --check ~/brain_workers/w463/patches/01_C0048_minimax_note.diff", "patch_check_exit_code": args.patch_check_exit_code, "live_store_mutations": 0}, "draft_submission": str(destination), "lifecycle": str(root/"DRAFT_LIFECYCLE.json"), "communication": "team notification unavailable; concrete on-disk handoffs saved", "artifact_fingerprints": artifacts})

old = (root/"STATUS.md").read_text(encoding="utf-8")
lines = old.splitlines()
lines[0] = "STATE: NEEDS_REVIEW"
for i, line in enumerate(lines):
    if line.startswith("NEXT:"):
        lines[i] = "NEXT: w464 verify the full-simplex minimax proof and normalized source allowance in REVIEW_PACKET.json; retain the Z^3 critical-ordering gap."
        break
lines.append(f"{stamp}: Complete and measured: six claim rows, three scoped peer KEEP rows, four concept DRAFT cards and three supported relations. Local preflight and patch check passed. Named inbox draft submitted; review/ingestion/retrieval unverified. REVIEW_PACKET.json freezes the evidence. Team-notice fallback is on disk.")
(root/"STATUS.md").write_text("\n".join(lines)+"\n", encoding="utf-8")
print(json.dumps({"state": "NEEDS_REVIEW", "review_packet": str(root/"REVIEW_PACKET.json"), "draft_submitted": str(destination), "entries": len(bundle["entries"]), "relations": len(bundle["relations"]), "parent_problem_solved": False}, indent=2))
