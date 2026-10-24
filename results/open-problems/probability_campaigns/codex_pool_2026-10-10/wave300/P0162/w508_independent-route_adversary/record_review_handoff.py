"""Record scoped referee receipts and prepare an integration packet, without ingestion."""
import datetime as dt
import hashlib
import json
import pathlib
import subprocess

ROOT = pathlib.Path(__file__).resolve().parent
REFEREE = pathlib.Path("~/brain_workers/w509")
BUNDLE = pathlib.Path("~/math-brain-inbox/w508/bundle_001.json")
NOW = dt.datetime.now(dt.timezone.utc).isoformat()

def load(name):
    return json.loads((ROOT / name).read_text(encoding="utf-8-sig"))

def save(name, value):
    (ROOT / name).write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

def digest(path):
    hasher = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(65536), b""):
            hasher.update(chunk)
    return hasher.hexdigest()

verdict_path = REFEREE / "REVIEW_VERDICTS.jsonl"
result = subprocess.run(
    ["rg", "-n", "-F", "w508-MATH-", str(verdict_path)],
    capture_output=True, text=True, encoding="utf-8", timeout=25, check=False,
)
assert result.returncode == 0, "Missing scoped referee verdicts"
verdict_hash = digest(verdict_path)
receipts = []
for numbered in result.stdout.splitlines():
    line, raw = numbered.split(":", 1)
    row = json.loads(raw)
    if row["claim"] not in {"w508-MATH-001", "w508-MATH-002", "w508-MATH-003"}:
        continue
    assert row["verdict"] == "KEEP"
    receipts.append({
        "claim_id": row["claim"], "referee": "w509", "verdict": "KEEP",
        "received_utc": NOW, "source_path": str(verdict_path), "source_line": int(line),
        "source_file_sha256_at_capture": verdict_hash,
        "source_row_sha256": hashlib.sha256(raw.encode("utf-8")).hexdigest(),
        "source_quote": raw, "scope": row["scope"],
        "reproduction": row["reproduction"], "remaining_gap": row["remaining_gap"],
        "basis": "Independent analytic derivation described by the referee",
        "referee_finite_run": "Auxiliary; referee reports no central fresh-gate receipt",
        "served_model_gate": "not_verified",
    })
assert len(receipts) == 3 and len({r["claim_id"] for r in receipts}) == 3
receipts.sort(key=lambda r: r["claim_id"])
(ROOT / "REVIEW_RECEIPTS.jsonl").write_text(
    "".join(json.dumps(row, ensure_ascii=False) + "\n" for row in receipts), encoding="utf-8"
)

claims = [json.loads(line) for line in (ROOT / "CLAIMS.jsonl").read_text(encoding="utf-8-sig").splitlines() if line.strip()]
by_id = {r["claim_id"]: r for r in receipts}
for claim in claims:
    if claim["claim_id"] in by_id:
        claim["independent_reviewer"] = "w509"
        claim["status"] = "independently checked proof"
        claim["review_state"] = "scoped_analytic_KEEP"
        claim["review_receipt"] = {
            "path": str(ROOT / "REVIEW_RECEIPTS.jsonl"),
            "claim_id": claim["claim_id"], "verdict": "KEEP",
            "scope": by_id[claim["claim_id"]]["scope"],
            "different_model_gate": "not_verified",
        }
        claim["remaining_gap"] = (
            by_id[claim["claim_id"]]["remaining_gap"]
            + "; served-model/different-model gate unverified; no author numerical run; no global FEI proof."
        )
        claim["promotion_state"] = "Original inbox entry remains concept/draft; integration gates pending"
    elif claim["claim_id"] == "w508-SRC-001":
        claim["remaining_gap"] = "Exact FEI definition and primary author sources recovered in SOURCE_STATUS.json; current openness UNKNOWN. This historical row has no independent source-row verdict."
(ROOT / "CLAIMS.jsonl").write_text(
    "".join(json.dumps(row, ensure_ascii=False) + "\n" for row in claims), encoding="utf-8"
)

model = load("MODEL_EVIDENCE.json")
gate = load("COMPUTE_GATE.json")
assert not gate["bounded_cpu_check_allowed"]
assert not (ROOT / "MEASUREMENTS.json").exists(), "Reconcile actual measurements before finalizing"
source = load("SOURCE_STATUS.json")
source["review_state"] = "scoped_analytic_KEEP_for_w508_MATH_001_002_003"
source["review_receipts"] = str(ROOT / "REVIEW_RECEIPTS.jsonl")
source["different_model_gate"] = "not_verified"
source["model_evidence"] = str(ROOT / "MODEL_EVIDENCE.json")
save("SOURCE_STATUS.json", source)

delivery = load("DELIVERY_STATE.json")
delivery["updated_utc"] = NOW
delivery["submitted"]["sha256"] = digest(BUNDLE)
delivery["submitted"]["immutable_original_preserved"] = True
delivery["reviewed"] = {
    "state": True, "scope": "Three narrow mathematical claims; analytic KEEP only",
    "referee": "w509", "claim_ids": sorted(by_id),
    "receipt_path": str(ROOT / "REVIEW_RECEIPTS.jsonl"),
    "served_model_gate": "not_verified", "global_FEI_reviewed_or_proved": False,
}
delivery["different_model_gate"] = {
    "state": "not_verified", "author_served_model": model["author_served_model_state"],
    "referee_served_model": model["referee_served_model_state"],
    "evidence_path": str(ROOT / "MODEL_EVIDENCE.json"),
}
delivery["experiment"] = {
    "state": "not_run_gate_denied", "count": 0, "passes": 0,
    "last_gate_utc": gate["checked_utc"],
    "last_governor_status": gate["local_metrics"]["status"],
    "referee_auxiliary_run_is_author_run": False,
}
delivery["integration_contact"] = "codex-01a12190"
delivery["integration_handoff"] = {"state": "prepared", "path": str(ROOT / "INTEGRATION_HANDOFF.json")}
save("DELIVERY_STATE.json", delivery)

report = """P0162 is not solved. w509 independently derived and kept all three scoped mathematical claims: the one-point Boolean obstruction, the sparse-flip extension for every bent function and every allowed flip set, and the coordinate logarithmic bound with sharp additive coefficient 3/ln 2. The exact KEEP rows are in REVIEW_RECEIPTS.jsonl. The claims are independently checked analytically; the submitted inbox entries remain concepts/drafts pending integration gates. No novelty claim is made.

The result identifies a false proof step: charging every coordinate entropy split by a constant times its influence. The sparse-flip bound quantifies that obstruction. Global FEI still needs a universal good-coordinate or aggregate argument. Related logarithmic restriction bounds and arbitrary-coordinate obstructions already occur in the owner's canonical store.

Measurements: three scoped analytic KEEP verdicts are recorded. The resumed command python -X utf8 fresh_compute_gate.py saw 26.68-second-old telemetry with status warn, CPU 83.9%, physical availability 6169 MB and effective commit availability 68221 MB, and denied the run. Author experiments executed = 0; numerical passes = 0. MEASUREMENTS.json does not exist. The referee's auxiliary finite run lacks a central fresh-gate receipt and is not counted as an author run. No before/after brain-performance improvement or formal proof-assistant check is claimed.

The command python -X utf8 inspect_model_evidence.py inspected 10 model-bearing records in the author's exact native transcript. None contained response-side served-model metadata. Author and referee served identities, and the different-model gate, remain UNKNOWN/unverified. Requested models and turn_context are excluded as evidence.

Apply: codex-01a12190 can validate and deduplicate ~/math-brain-inbox/w508/bundle_001.json using INTEGRATION_HANDOFF.json and BUNDLE_SPEC.md. Preserve concept/draft status until the applicable model and proof gates pass. Separately apply patches/01_fei_hook_proposal.diff only if the hook is kept. This worker did not mutate a live store or run an integrator. Submission, analytic review, model gate, ingestion and retrieval have separate states.

Risks: confusing an every-coordinate obstruction with an existential good-coordinate claim, promoting a local constant to the global FEI constant, duplicate restriction-ledger concepts, or treating packaging or an ungated finite run as proof. Current global openness remains UNKNOWN.

NEXT: codex-01a12190 resolves served-model evidence and deduplication, then validates integration and retrieval for the scoped draft bundle.
"""
(ROOT / "REPORT.md").write_text(report, encoding="utf-8")

packet = """# w508 P0162 review and integration packet

w509 has returned scoped analytic KEEP for w508-MATH-001, w508-MATH-002 and w508-MATH-003. REVIEW_RECEIPTS.jsonl quotes the original rows with source paths, line numbers and hashes. The receipt capture records acceptance; it does not review the referee's review. New results originated by w509 require its assigned independent referee w512.

INDEPENDENT_DERIVATION.md supplies the one-point and arbitrary sparse-flip proofs. SHARP_COORDINATE_BOUND.md supplies the universal logarithmic coordinate bound and sharpness of its additive 3/ln 2 coefficient. Use the exact statements and assumptions in CLAIMS.jsonl. CORE_PROOF_AUDIT.md records the earlier adversarial KEEP of w507's narrow L1-L3 claims.

The independent approach was saved before reading w507. Both agents used the same one-point bent family; w508 used a different second-difference method, then extended it to arbitrary allowed sparse flip sets. No novelty is claimed, and related owner-store bounds are cited in SOURCE_STATUS.json.

Neither agent has proved global FEI. The strongest obstruction is to an every-coordinate constant charge. The remaining global step is a universal good-coordinate selection or aggregate-charge argument. Current openness remains UNKNOWN.

The author verifier has not run: the fresh resource gate reported warn and denied execution. Author experiments = 0 and passes = 0. verify_spectra.py is optional supplemental verification, capped at 2048 atoms and 45 seconds. Run fresh_compute_gate.py before verify_spectra.py --gate COMPUTE_GATE.json; never override a denied or stale gate. The referee reports auxiliary finite calculations without a central fresh-gate receipt; its KEEP verdicts are based on independent analytic algebra. No formal theorem receipt exists.

MODEL_EVIDENCE.json records a bounded inspection of the exact author native transcript. Its model-bearing records provide no response-side served identity. Both author and referee served-model states are UNKNOWN, and the different-model gate is unverified. A narrow receipt request was sent to w509; no proof re-review was requested.

Route integration to codex-01a12190. INTEGRATION_HANDOFF.json records exact paths and hashes, scoped KEEP, gaps and duplicate-definition cautions. The original bundle_001.json is unchanged: three entries and three relations, with own results still concept/draft and owner-own-work sources. Dedupe the restriction-ledger definition with w507 before integration. Submission, analytic review, model gate, ingestion and retrievability are distinct; the last two remain unverified.

NEXT: validating coordinator resolves the evidence gate and deduplication, then validates ingestion and retrieval without claiming a global FEI solution.
"""
(ROOT / "REVIEW_PACKET.md").write_text(packet, encoding="utf-8")
attempt = (ROOT / "ATTEMPT.md").read_text(encoding="utf-8-sig")
attempt = "\n".join(
    "NEXT: Integration contact codex-01a12190 resolves served-model evidence and deduplication for the three scoped analytic KEEP claims; global coordinate-selection remains unproved."
    if line.startswith("NEXT:") else line for line in attempt.splitlines()
) + "\n"
(ROOT / "ATTEMPT.md").write_text(attempt, encoding="utf-8")

paths = [ROOT / name for name in (
    "CLAIMS.jsonl", "INDEPENDENT_DERIVATION.md", "SHARP_COORDINATE_BOUND.md",
    "CORE_PROOF_AUDIT.md", "SOURCE_STATUS.json", "REVIEW_RECEIPTS.jsonl",
    "MODEL_EVIDENCE.json", "REPORT.md", "REVIEW_PACKET.md",
)] + [BUNDLE, verdict_path, REFEREE / "REVIEW_PACKET.md"]
handoff = {
    "target": "P0162", "author": "w508", "referee": "w509",
    "integration_contact": "codex-01a12190", "created_utc": NOW,
    "bundle": {"path": str(BUNDLE), "sha256": digest(BUNDLE), "entries": 3,
               "relations": 3, "state": "submitted draft; original unchanged"},
    "scoped_KEEP": [{"claim_id": r["claim_id"], "scope": r["scope"],
                     "receipt_path": str(ROOT / "REVIEW_RECEIPTS.jsonl")} for r in receipts],
    "artifacts": [{"path": str(path), "sha256_at_capture": digest(path)} for path in paths],
    "model_evidence": {
        "path": str(ROOT / "MODEL_EVIDENCE.json"),
        "author_native_thread_id": model["author_native_thread_id"],
        "author_served_model": model["author_served_model_state"],
        "referee_served_model": model["referee_served_model_state"],
        "different_model_gate": "not_verified",
        "referee_receipt_request": model["referee_receipt_request"],
    },
    "proof_assistant_receipt": None,
    "author_experiments": {"executed": 0, "passed": 0, "fresh_gate": "denied"},
    "remaining_gaps": [
        "Global FEI and universal coordinate-selection/aggregate argument are unproved",
        "Current openness UNKNOWN; novelty unverified and not claimed",
        "Response-side served-model identity and different-model gate unverified",
        "Author numerical verification not executed because fresh gate denied it",
        "Deduplicate restriction-ledger definition against w507; preserve sparse/sharp claim scope",
        "Ingestion and retrievability not verified",
    ],
    "promotion": "No theorem promotion or parent-problem solved claim authorized by these receipts",
    "NEXT": "Coordinator resolves model gate and deduplication, validates integration, then checks retrieval",
}
save("INTEGRATION_HANDOFF.json", handoff)
with (ROOT / "RESUME_RESULTS.jsonl").open("a", encoding="utf-8") as stream:
    stream.write(json.dumps({"row_id": "w508-RESUME-004", "saved_utc": NOW,
        "result": "Three scoped analytic KEEP receipts recorded; immutable integration handoff prepared",
        "evidence": str(ROOT / "INTEGRATION_HANDOFF.json"),
        "global_FEI_proved": False, "different_model_gate": "not_verified"}) + "\n")
(ROOT / "STATUS.md").write_text(
    "STATE: WORKING\nNEXT: Send the hashed scoped KEEP packet to codex-01a12190, record the delivery receipt and set NEEDS_REVIEW.\n\n"
    + NOW + " Recorded w509's three exact scoped KEEP receipts, updated claim/review states, preserved the original inbox bundle, and prepared INTEGRATION_HANDOFF.json. Native transcript lacks response-side model evidence; fresh numerical gate denied execution. Global FEI unproved; ingestion/retrieval unverified.\n",
    encoding="utf-8",
)
print(json.dumps({"scoped_KEEP": len(receipts), "claims": len(claims),
                  "bundle_sha256": digest(BUNDLE), "handoff": str(ROOT / "INTEGRATION_HANDOFF.json")}))
