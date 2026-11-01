"""Consume scoped verdicts; preserve draft, ingestion and proof-gap boundaries."""
import datetime
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent
REFEREE = pathlib.Path("~/brain_workers/w374/REVIEW_PACKET.md")
IDS = ["S1.w372.L1", "S1.w372.L1-short", "S1.w372.L2", "S1.w372.L3",
       "S1.w372.CEX", "S1.w372.L4", "S1.w372.CEX-global"]
primary_rows = [line.strip() for line in REFEREE.read_text(encoding="utf-8").splitlines()
                if line.startswith("| w372")]
verdicts = {}
for claim_id in IDS:
    matches = [line for line in primary_rows if "`" + claim_id + "`" in line]
    assert len(matches) == 1, (claim_id, matches)
    verdict = matches[0].split("|")[2].strip()
    assert verdict in {"KEEP", "KEEP conditional"}, (claim_id, verdict)
    verdicts[claim_id] = verdict

receipt = {
    "at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
    "reviewer": "w374", "primary_verdict_file": str(REFEREE),
    "verdicts": verdicts, "verdict_rows": primary_rows,
    "adversary": {"reviewer": "w373", "verdict": "KEEP AS PARTIAL REDUCTIONS",
                  "artifact": "~/brain_workers/w373/PAIRED_AUDIT.md",
                  "scope": "Frozen L2/L4 reductions; H_MEAN and H_GLOBAL remain open"},
    "statement_correction": "Question 22: printed page 88, PDF page 89",
    "parent_problem_solved": False, "formal_check_receipt": None,
    "reviewer_served_model": "UNKNOWN", "different_model_gate": "UNVERIFIED",
    "independent_account_gate": "UNVERIFIED",
    "ingestion_receipt": None, "retrieval_receipt": None,
}
(ROOT / "PEER_AUDIT_RECEIPT.json").write_text(json.dumps(receipt, indent=2)+"\n", encoding="utf-8")

claims = [json.loads(line) for line in (ROOT / "CLAIMS.jsonl").read_text(encoding="utf-8").splitlines() if line]
for claim in claims:
    if claim["claim_id"] in verdicts:
        claim["status"] = "independently checked proof"
        claim["independent_reviewer"] = {
            "assigned": "w374", "verdict": verdicts[claim["claim_id"]],
            "receipt": str(ROOT / "PEER_AUDIT_RECEIPT.json"),
            "scope": "Exact stated assumptions only; no parent-problem solution or store-promotion gate"
        }
(ROOT / "CLAIMS.jsonl").write_text("".join(json.dumps(row, ensure_ascii=False)+"\n" for row in claims), encoding="utf-8")

for name in ("STATEMENT.md", "SOURCE_STATUS.json", "ATTEMPT.md", "REPORT.md", "REVIEW_PACKET.md"):
    path = ROOT / name
    text = path.read_text(encoding="utf-8")
    text = text.replace("printed p. 89", "printed p. 88 (PDF p. 89)")
    text = text.replace("printed page 89;", "printed page 88 (PDF page 89);")
    path.write_text(text, encoding="utf-8")
source = json.loads((ROOT / "SOURCE_STATUS.json").read_text(encoding="utf-8"))
source["independent_reviewer"] = "w374; seven scoped mathematical KEEP verdicts, parent gap unproved"
source["review_receipt"] = str(ROOT / "PEER_AUDIT_RECEIPT.json")
(ROOT / "SOURCE_STATUS.json").write_text(json.dumps(source, indent=2)+"\n", encoding="utf-8")

state = json.loads((ROOT / "BUNDLE_STATE.json").read_text(encoding="utf-8"))
state["reviewed"] = {
    "status": "scoped-KEEP", "reviewer": "w374", "claim_ids": IDS,
    "receipt": str(ROOT / "PEER_AUDIT_RECEIPT.json"),
    "scope": "Seven exact claims; conditional premises remain open. Submitted DRAFT files retain their initial pending labels.",
    "promotion_gate": "UNVERIFIED; served-model and independent-account evidence not supplied",
}
(ROOT / "BUNDLE_STATE.json").write_text(json.dumps(state, indent=2)+"\n", encoding="utf-8")
model = {
    "requested": {"model": "gpt-6.1-sol", "reasoning": "max", "service_tier": "Fast"},
    "author_response_side_served_model": "UNKNOWN",
    "referee_response_side_served_model": "UNKNOWN",
    "evidence": "No response-side served-model metadata was available; requested settings and turn context do not prove served identity.",
    "different_model_gate": "UNVERIFIED"
}
(ROOT / "MODEL_EVIDENCE.json").write_text(json.dumps(model, indent=2)+"\n", encoding="utf-8")

packet = ROOT / "REVIEW_PACKET.md"
text = packet.read_text(encoding="utf-8")
text = text.replace("Review status: pending.", "Review status: seven scoped mathematical KEEP verdicts from w374; promotion gates unverified.")
text = text.replace("No claim has yet been marked independently checked.", "Seven exact claims now carry independently checked proof status, with their original assumptions and remaining gaps.")
text += "\nReview receipt: PEER_AUDIT_RECEIPT.json records the referee's own verdict rows, including the conditional L3/L4 and abstract CEX-global scopes. Question 22's locator is corrected to printed page 88 (PDF page 89). Submitted DRAFT metadata remains frozen at its initial pending status; the integration contact must use this receipt and MODEL_EVIDENCE.json. No parent solution, ingestion, retrieval, or different-model gate is certified.\n"
packet.write_text(text, encoding="utf-8")
report = ROOT / "REPORT.md"
text = report.read_text(encoding="utf-8")
text = text.replace("NEXT: Verify the L2 and mean-gap reductions independently, then seek a positive quadratic mean-gap bound for an actual iid law; retain H_GLOBAL as the parent gap.", "NEXT: The integration contact checks the scoped verdicts and promotion evidence; the next mathematical step is a positive quadratic H_MEAN bound for Uniform[1,2], while H_GLOBAL remains unproved.")
text += "\nIndependent mathematical review: w374 kept L1, L1-short, L2, L3 (conditional), CEX, L4 (conditional), and CEX-global (abstract). The source locator was corrected to printed page 88, PDF page 89. The exact verdicts are saved in PEER_AUDIT_RECEIPT.json. Served-model and account evidence remain unverified, so no store-promotion gate is claimed.\n"
report.write_text(text, encoding="utf-8")
status = ROOT / "STATUS.md"
lines = status.read_text(encoding="utf-8").splitlines()
assert lines[0] == "STATE: NEEDS_REVIEW"
lines[1] = "NEXT: Integration checks scoped KEEP receipts and promotion evidence; the next proof step is a positive H_MEAN bound for Uniform[1,2], with H_GLOBAL still unproved."
lines.append("2026-10-10: Consumed w374's seven scoped mathematical KEEP verdicts and w373's frozen partial audit. Corrected Question 22 to printed p.88 (PDF p.89). Saved exact receipts and UNKNOWN served-model evidence. Coupling claim clm-a29fa94dd7 released; no live math-store change. Integration handoff is review-ready.")
status.write_text("\n".join(lines)+"\n", encoding="utf-8")

sys.path.insert(0, "~/<private-repo>/12_cognitive_architecture/agent_mesh")
import team_comm as tc
body = ("P0110 w372 review-ready partial packet: ~/brain_workers/w372/REVIEW_PACKET.md; "
        "CLAIMS.jsonl; PEER_AUDIT_RECEIPT.json; MODEL_EVIDENCE.json; measurements.json. "
        "w374's own verdict rows KEEP all seven exact proved claims, L3/L4 conditional; w373 keeps frozen L2/L4. "
        "9216 finite environments checked; two corrected cases pass and both naive independence identities fail. "
        "DRAFT files: ~/math-brain-inbox/w372/bundle_001.json and bundle_002.json, 9 entries/7 relations. "
        "Question 22 locator corrected to printed p.88/PDF p.89 in the packet. "
        "H_MEAN and H_GLOBAL remain unproved, current openness UNKNOWN. "
        "Author/referee response-side served-model and different-account evidence UNKNOWN; no different-model or promotion gate claimed. "
        "Bundle hashes not computed under BUNDLE_SPEC; ingestion UNKNOWN and retrieval UNVERIFIED. Please route only scoped accepted material after gate checks.")
try:
    mesh = tc.mesh()
    sent = mesh.send("w372", "codex-01a12190", "P0110-w372-integration-handoff", body, kind="message")
    tc.ring("codex-01a12190")
    delivery = {"to": "codex-01a12190", "topic": "P0110-w372-integration-handoff", "receipt": sent}
except Exception as exc:
    delivery = {"to": "codex-01a12190", "status": "STUCK: handoff not delivered", "error": str(exc)}
with (ROOT / "COMMUNICATION_RECEIPTS.jsonl").open("a", encoding="utf-8") as handle:
    handle.write(json.dumps(delivery, default=str)+"\n")
print(json.dumps({"scoped_keep_claims": len(IDS), "parent_problem_solved": False, "handoff": delivery}, default=str))
