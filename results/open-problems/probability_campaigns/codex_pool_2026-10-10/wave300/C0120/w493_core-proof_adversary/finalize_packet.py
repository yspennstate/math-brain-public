import datetime
import hashlib
import json
from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parent
now = datetime.datetime.now(datetime.timezone.utc).isoformat()
review_path = Path("~/brain_workers/w494/REVIEW_PACKET.md")
review_bytes = review_path.read_bytes()
review_text = review_bytes.decode("utf-8")
review_sha = hashlib.sha256(review_bytes).hexdigest()
for claim_suffix in ("002", "003", "004", "005"):
    if f"w493-C0120-{claim_suffix} KEEP" not in review_text:
        raise RuntimeError(f"Missing explicit referee KEEP for claim {claim_suffix}")
if "w493-C0120-001" not in review_text or "KEEP as abstract special case" not in review_text:
    raise RuntimeError("Missing dependency-counterexample referee receipt")

referee = {"referee": "w494", "received_at_utc": now, "verdict_path": str(review_path),
    "verdict_sha256_as_read": review_sha, "scoped_keep_claims": [f"w493-C0120-{i:03d}" for i in range(1, 6)],
    "mathematical_special_cases_checked": ["001", "003", "004", "005"],
    "source_correction": "002 KEEP; Claude statement gate remains pending",
    "parent_problem_solved": False, "missing_input": "Lattice-specific polynomial spectral/overlap rate",
    "formal_check": False, "served_model_evidence": "UNVERIFIED",
    "different_model_promotion_gate": "not established",
    "policy": "Recorded the referee's verdict; did not re-audit the referee's review or originate a review of its own new result."}
(ROOT / "REFEREE_RECEIPT.json").write_text(json.dumps(referee, indent=2)+"\n", encoding="utf-8")
claims = [json.loads(x) for x in (ROOT / "CLAIMS.jsonl").read_text(encoding="utf-8").splitlines() if x.strip()]
for claim in claims:
    claim["independent_reviewer"] = "w494"
    claim["review_state"] = "scoped KEEP by w494"
    claim["review_evidence"] = {"path": str(review_path), "sha256_as_read": review_sha,
                               "receipt": "~/brain_workers/w493/REFEREE_RECEIPT.json"}
    claim["store_promotion_gate"] = "not established; concept/DRAFT only"
    if claim["claim_id"].endswith("002"):
        claim["status"] = "sketch"
        claim["remaining_gap"] = "Claude/source-statement review and integration pending; present openness UNKNOWN. This is not a mathematical-proof claim."
    else:
        claim["status"] = "independently checked proof"
        if claim["claim_id"].endswith("005"):
            claim["remaining_gap"] = "Polynomial-time polynomial-overlap hypothesis remains UNPROVED; independently checked reduction does not prove it. Served-model promotion gate not established."
        else:
            claim["remaining_gap"] = "Only the stated abstract/finite special case is checked. Parent polynomial variance target remains unproved; served-model promotion gate not established."
(ROOT / "CLAIMS.jsonl").write_text("".join(json.dumps(c)+"\n" for c in claims), encoding="utf-8")

source = json.loads((ROOT / "SOURCE_STATUS.json").read_text(encoding="utf-8"))
source["review_state"] = "w494 scoped KEEP for claims 001-005; source correction still requires Claude gate"
source["referee_receipt"] = "~/brain_workers/w493/REFEREE_RECEIPT.json"
(ROOT / "SOURCE_STATUS.json").write_text(json.dumps(source, indent=2)+"\n", encoding="utf-8")
submission = json.loads((ROOT / "SUBMISSION_RECEIPT.json").read_text(encoding="utf-8"))
submission.update({"reviewed": True, "review_state": "scoped mathematical KEEP by w494; served-model/source gates pending",
                   "reviewed_at_utc": now, "referee_receipt": "REFEREE_RECEIPT.json",
                   "frozen_submission_label": "The inbox file retains its UNREVIEWED-at-authoring label; current review state is recorded separately, without changing the submitted file."})
(ROOT / "SUBMISSION_RECEIPT.json").write_text(json.dumps(submission, indent=2)+"\n", encoding="utf-8")
(ROOT / "REVIEW_ADDENDUM.md").write_text(
    "2026-10-10: w494 independently checked and kept w493 claims 001, 003, 004 and 005 in their exact finite/abstract/conditional scopes. Source correction 002 also received scoped KEEP but still needs the Claude statement gate.\n\n"
    "ATTEMPT.md and the submitted bundle are frozen pre-review artifacts; their pending/UNREVIEWED labels describe that earlier state. Current states and the exact referee artifact hash are in REFEREE_RECEIPT.json and SUBMISSION_RECEIPT.json. G1 remains unproved, present openness is UNKNOWN, served-model evidence is unavailable, and no theorem or parent-solution promotion is asserted.\n\n"
    "NEXT: Integration reviews the source correction gate and keeps the two floor/witness nodes as concept/DRAFT; the full-target proof needs the explicit polynomial spectral/overlap bound.\n", encoding="utf-8")

report = (ROOT / "REPORT.md").read_text(encoding="utf-8")
report = report.replace("w494's independent check and response-side served-model evidence are pending; no theorem or solved-parent promotion is authorized by this packet.",
    "w494 independently checked and kept all four mathematical claims in their stated scopes. Response-side served-model evidence and the Claude source-statement gate remain pending; no theorem or solved-parent promotion is authorized by this packet.")
report = report.replace("NEXT: w494 independently checks claims 003-005 and the exact n=2 witness; the next full-target proof step is a uniform lattice-specific polynomial spectral-escape estimate, not another open-status search.",
    "NEXT: Integration reviews the source-correction gate and the two frozen concept/DRAFT nodes; the next full-target proof step is a uniform lattice-specific polynomial spectral-escape estimate.")
(ROOT / "REPORT.md").write_text(report, encoding="utf-8")

check = subprocess.run(["python", "-X", "utf8", str(ROOT / "verify_packet.py")], capture_output=True,
                       text=True, encoding="utf-8", timeout=60)
print(check.stdout.strip())
if check.returncode:
    print(check.stderr)
    raise RuntimeError("Final metadata check failed")
files = ["ATTEMPT.md", "CLAIMS.jsonl", "AUDIT_VERDICTS.jsonl", "SOURCE_STATUS.json", "REPORT.md",
         "MEASUREMENTS.json", "COMPUTE_GATE.json", "CHECK_RECEIPT.json", "REFEREE_RECEIPT.json",
         "REVIEW_ADDENDUM.md", "SUBMISSION_RECEIPT.json", "LEASE_RECEIPT.json", "bundle_001.json",
         "RELATION_EVIDENCE.jsonl", "HOOK_PROPOSAL.jsonl", "HOOK_CONTROLS.json",
         "patches/01_polymer_overlap_floor_hook.diff", "verify_obstructions.py", "verify_packet.py"]
packet = {"worker": "w493", "candidate": "C0120", "status": "NEEDS_REVIEW",
    "native_thread_identity": "w493", "prepared_at_utc": now,
    "independent_derivation_saved_before_peer_proof": True,
    "independent_derivation_sha256": source["independent_save_sha256_before_peer_read"],
    "parent_problem_solved": False, "current_openness": "UNKNOWN", "novelty_claim": False,
    "hardest_missing_input": "w492-G1: uniform lattice-specific polynomial low-degree Hermite gradient spectral escape, equivalently a polynomial-time polynomial-overlap gain with exponent loss.",
    "own_claims": [c["claim_id"] for c in claims], "own_review": referee,
    "paired_proof_audit": "w492 L1-L4 KEEP in finite/conditional/parallel-corridor scopes; G1 UNPROVED",
    "source_correction": {"patch": "~/brain_workers/w492/patches/01_c0120_source_scope.diff",
        "store_targets": "~/brain_workers/w492/STORE_CORRECTIONS.json", "claude_statement_gate": "pending"},
    "brain_states": submission, "served_identity": source["served_identity"],
    "formal_receipt": None, "admitted_placeholders_counted": False,
    "measurements": {"exact_finite_checks": 116, "unsafe_shortcuts_rejected": 2,
        "finite_check_wall_seconds": 0.18882360006682575, "final_packaging_checks": json.loads((ROOT / "CHECK_RECEIPT.json").read_text())["packaging_checks_passed"]},
    "next": "Integration applies the source review gate; prove a lattice-specific polynomial spectral/overlap estimate before a full-target claim.",
    "files": {name: {"path": str(ROOT / name), "sha256": hashlib.sha256((ROOT / name).read_bytes()).hexdigest(),
                     "bytes": (ROOT / name).stat().st_size} for name in files}}
(ROOT / "REVIEW_PACKET.json").write_text(json.dumps(packet, indent=2)+"\n", encoding="utf-8")
print(json.dumps({"review_packet": str(ROOT / "REVIEW_PACKET.json"),
    "packet_sha256": hashlib.sha256((ROOT / "REVIEW_PACKET.json").read_bytes()).hexdigest(),
    "claims": len(claims), "reviewed_mathematical_claims": 4, "source_gate": "pending", "parent_solved": False}))
