"""Save the completed scoped review and pin a review-ready integration packet."""
import hashlib
import json
from pathlib import Path
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parent
PEER = ROOT.parent / "w512"
INBOX = Path("~/math-brain-inbox/w510/bundle_001.json")
now = datetime.now(timezone.utc).isoformat()

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def write_json(name, obj):
    (ROOT / name).write_text(json.dumps(obj, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

verdicts = [json.loads(line) for line in (PEER / "VERDICTS.jsonl").read_text(encoding="utf-8-sig").splitlines() if line.strip()]
claim_ids = [f"P0162-w510-C{i:03d}" for i in range(1, 5)]
keeps = {row["target"]: row for row in verdicts if row.get("target") in claim_ids and row.get("verdict") == "KEEP" and row.get("reviewer") == "w512"}
if set(keeps) != set(claim_ids):
    raise SystemExit("Missing scoped w512 KEEP: preserve files; do not advance review state.")

peer_handoff = json.loads((PEER / "HANDOFF.json").read_text(encoding="utf-8-sig"))
bundle_expected = next(value for key, value in peer_handoff["sha256"].items() if Path(key).name == "bundle_001.json" and "w510" in key)
bundle_hash = digest(INBOX)
if bundle_hash != bundle_expected:
    raise SystemExit("Submitted bundle differs from the pinned referee artifact: do not promote.")
if digest(ROOT / "DRAFT_BUNDLE.json") != bundle_hash:
    raise SystemExit("Local/submitted bundle bytes differ: preserve state and inspect.")

claim_path = ROOT / "CLAIMS.jsonl"
old_claim_bytes = claim_path.read_bytes()
old_claim_hash = hashlib.sha256(old_claim_bytes).hexdigest()
snapshot = ROOT / "REVIEWED_CLAIMS_SNAPSHOT.jsonl"
if not snapshot.exists():
    snapshot.write_bytes(old_claim_bytes)
reviewed_claim_expected = next(value for key, value in peer_handoff["sha256"].items() if Path(key).name == "CLAIMS.jsonl" and "w510" in key)
if digest(snapshot) != reviewed_claim_expected:
    raise SystemExit("Reviewed claim snapshot does not match the referee pin.")

claims = [json.loads(line) for line in old_claim_bytes.decode("utf-8-sig").splitlines() if line.strip()]
for claim in claims:
    if claim.get("claim_id") not in keeps:
        continue
    claim["primary_referee"] = {
        "agent": "w512", "state": "KEEP", "evidence": str(PEER / "VERDICTS.jsonl"),
        "scope_evidence": str(PEER / "REVIEW_PACKET.md"), "receipt_read_at_utc": now,
        "response_side_model_evidence": "not verified", "different_model_review": "not certified",
        "account_separation": "not certified"
    }
    claim["remaining_gap"] = claim["remaining_gap"].replace("primary referee review pending; ", "")
    claim["promotion_state"] = "Scoped mathematical KEEP from w511 and w512; identity/account gates pending."
claim_path.write_text("".join(json.dumps(row, ensure_ascii=False) + "\n" for row in claims), encoding="utf-8")

states = json.loads((ROOT / "BUNDLE_STATES.json").read_text(encoding="utf-8-sig"))
states["reviewed"] = {
    "state": "Scoped mathematical KEEP from w511 and w512; promotion provenance pending",
    "primary_referee": "w512", "primary_referee_state": "KEEP C001-C004",
    "primary_referee_evidence": str(PEER / "VERDICTS.jsonl"),
    "primary_referee_scope_evidence": str(PEER / "REVIEW_PACKET.md"),
    "adversary": "w511", "adversary_verdict": "KEEP C001-C004",
    "adversary_evidence": "~/brain_workers/w511/AUDIT_W510.md",
    "two_account_keeps": "not certified", "different_model_review": "not certified",
    "served_models": "response-side evidence not verified"
}
states["ingested"] = {"state": "unverified; no integration run by w510"}
states["retrievable"] = {"state": "not tested"}
states["integration_contact"] = "codex-01a12190"
states["submitted_file_sha256"] = bundle_hash
write_json("BUNDLE_STATES.json", states)

verification = json.loads((ROOT / "FINAL_VERIFICATION_STATE.json").read_text(encoding="utf-8-sig"))
verification["review_receipt_update"] = {
    "checked_at_utc": now, "w511": "KEEP C001-C004", "w512": "KEEP C001-C004",
    "promotion_provenance": "unverified", "corrected_gate_rerun": "pending; no new experiment run during resumption"
}
write_json("FINAL_VERIFICATION_STATE.json", verification)

row_id = "P0162-w510-referee-receipt-001"
source_rows = ROOT / "SOURCE_ROWS.jsonl"
if row_id not in source_rows.read_text(encoding="utf-8-sig"):
    row = {
        "row_id": row_id, "kind": "audit verdict receipt", "date_utc": now,
        "claim_ids": claim_ids, "verdict": "KEEP", "reviewer": "w512",
        "source": str(PEER / "REVIEW_PACKET.md"),
        "source_quote": "KEEP w510 C001-C004 and w511 C001-C004 at their stated narrow scopes.",
        "proof_evidence": str(PEER / "VERDICTS.jsonl"), "receipt_read": True,
        "remaining_gap": "General FEI unproved; account separation and response-side model evidence unverified.",
        "status": "scoped mathematical review received; not an ingestion receipt"
    }
    with source_rows.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(row, ensure_ascii=False) + "\n")

report = """The sharp constant 4 for affine-subspace indicators and two Boolean counterexamples to stronger entropy bridges are independently kept by w511 and w512 (C001-C004). General Fourier entropy versus influence is unproved; novelty and current openness are not certified. ATTEMPT.md gives the exact target, prior attempt digest, assumptions and proofs.

Command: python -X utf8 ~/brain_workers/w510/verify_affine.py

The initial run checked 182 exact truth-table spectra in 0.438023 seconds with zero formula mismatches. At codimension 128, the marginal-entropy bound 9.662954395197108e-35 becomes the exact entropy 3.0027144497938533e-36: a 32.18073-fold tighter bound on this family, with H/I=3.99129211. This comparison is not a live recall improvement.

The initial resource gate omitted commit telemetry. The corrected gate denied the repeat at 92.1999% commit and 2.082 GB physical memory available. MEASUREMENTS.json preserves the initial passing run; COMPUTE_GATE.json preserves the denial. No new experiment ran during resumption. These numeric checks are not formal proof certificates; the referee verdicts rest on algebra.

w512/VERDICTS.jsonl and w511/AUDIT_W510.jsonl are the scoped mathematical receipts. The author's receipt was read on resumption. Account separation, response-side served models and the different-model review gate remain unverified. Requested settings and delivery receipts establish neither model identity nor reading exposure. REVIEWED_CLAIMS_SNAPSHOT.jsonl preserves the exact claim bytes pinned by w512; the current CLAIMS.jsonl only updates review metadata.

Apply: codex-01a12190 verifies the review provenance, then uses the normal audited draft pipeline for ~/math-brain-inbox/w510/bundle_001.json. It has six entries and five relations with owner-own-work source tags. HANDOFF.json pins the files with SHA-256 for integrity, not as proof or an integration seal. BUNDLE_STATES.json separates submission, mathematical review, ingestion and retrieval; ingestion and retrieval are unconfirmed. The worker did not run an integrator or write to a live store.

The mathematical risk is extrapolation beyond flat affine spectra. The hardest remaining gap is a dimension-free budget for mass-weighted nonempty entropy of arbitrary Boolean spectra. HOOK_PROPOSALS.jsonl contains the local normalization hook for authorized integration.

NEXT: codex-01a12190 verifies account and response-side model provenance for the reviewed bundle; the next mathematical step is a variance-weighted block exposure budget.
"""
(ROOT / "REPORT.md").write_text(report, encoding="utf-8")

packet_path = ROOT / "REVIEW_PACKET.md"
marker = "Review receipt on resumption (2026-10-10)"
packet = packet_path.read_text(encoding="utf-8-sig")
if marker not in packet:
    with packet_path.open("a", encoding="utf-8") as handle:
        handle.write("\n\n" + marker + ": w512 independently KEEP C001-C004; VERDICTS.jsonl and REVIEW_PACKET.md were read by w510. w511 also KEEP C001-C004. Earlier pending-review entries are historical. Mathematical scope remains affine special cases and failed stronger bridges, not universal FEI or a novelty claim. Account separation and response-side served-model/different-model evidence remain unverified. Route to codex-01a12190; do not promote solely on these receipts. No experiment ran on resumption; corrected-gate rerun remains pending. See REFEREE_RECEIPT.json, REVIEWED_CLAIMS_SNAPSHOT.jsonl and HANDOFF.json.\n")

files = ["STATEMENT.md", "ATTEMPT.md", "CLAIMS.jsonl", "REVIEWED_CLAIMS_SNAPSHOT.jsonl", "SOURCE_STATUS.json", "SOURCE_ROWS.jsonl", "REPORT.md", "REVIEW_PACKET.md", "REFEREE_RECEIPT.json", "DRAFT_BUNDLE.json", "BUNDLE_STATES.json", "MEASUREMENTS.json", "COMPUTE_GATE.json", "FINAL_VERIFICATION_STATE.json", "HOOK_PROPOSALS.jsonl"]
pins = {str(ROOT / name): digest(ROOT / name) for name in files}
for path in [INBOX, PEER / "VERDICTS.jsonl", PEER / "REVIEW_PACKET.md", PEER / "HANDOFF.json", ROOT.parent / "w511" / "AUDIT_W510.jsonl"]:
    pins[str(path)] = digest(path)

handoff = {
    "target": "P0162", "author": "w510", "integration_contact": "codex-01a12190", "prepared_at_utc": now,
    "bundle": str(INBOX), "bundle_sha256": bundle_hash, "referee_pinned_bundle_match": True,
    "local_submitted_bundle_match": True, "reviewed_claim_snapshot_matches_referee_pin": True,
    "claim_changes_since_review": "Review metadata only; statements, assumptions, sources and proof fields unchanged.",
    "scoped_keeps": {"w511": claim_ids, "w512": claim_ids},
    "referee_receipt_read": True, "review_scope": "Affine sharp constant 4 and stronger-bridge counterexamples only",
    "general_fei_proved": False, "novelty_claimed": False, "current_openness": "UNKNOWN",
    "served_model_evidence": {"author": "not verified", "w511": "not verified", "w512": "not verified"},
    "account_separation_evidence": "not certified", "different_model_review": "not certified",
    "proof_gate_state": "Scoped mathematics kept; final promotion provenance unresolved",
    "ingested": "unverified", "retrievable": "not tested",
    "compute": "Initial 182-case PASS with incomplete gate; corrected gate DENIED repeat; no new experiment on resumption",
    "sha256_purpose": "File integrity and reviewed-byte identity only; not mathematical proof or bundle signing",
    "sha256": pins,
    "next": "Verify response-side served-model/account provenance, then audited integration; next research step mass-weighted block entropy budget."
}
write_json("HANDOFF.json", handoff)

status = (ROOT / "STATUS.md").read_text(encoding="utf-8-sig")
log = f"\n{now}: Resumed STOPPED_stage1.json; consumed w512 KEEP C001-C004. Saved referee receipt, exact reviewed claim snapshot, reviewed bundle hash match and integration handoff. Promotion model/account gates remain unverified; no new experiment.\n"
if "consumed w512 KEEP C001-C004" not in status:
    (ROOT / "STATUS.md").write_text(status + log, encoding="utf-8")
print(json.dumps({"state": "handoff prepared", "claims_kept": len(keeps), "bundle_sha256": bundle_hash, "reviewed_bundle_matches": True, "reviewed_claim_snapshot_matches": True, "model_account_gates": "unverified"}))
