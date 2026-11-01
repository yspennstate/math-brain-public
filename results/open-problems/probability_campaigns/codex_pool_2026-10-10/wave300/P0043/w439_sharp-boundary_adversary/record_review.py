"""Record the named referee's receipt; leave submitted draft files unchanged."""
from pathlib import Path
from datetime import datetime, timezone
import json
import re

ROOT = Path(__file__).resolve().parent
review_path = Path("~/brain_workers/w440/REVIEW_PACKET.md")
review = review_path.read_text(encoding="utf-8-sig")
ids = ("w439-P0043-boundary-001", "w439-P0043-boundary-002", "w439-P0043-boundary-003")
sections = []
for cid in ids:
    match = re.search(r"^## " + re.escape(cid) + r"[^\n]*\n.*?(?=^## |\Z)", review, flags=re.M | re.S)
    if not match or "KEEP" not in match.group(0).splitlines()[0]:
        raise RuntimeError("No KEEP receipt for " + cid)
    sections.append(match.group(0).strip())
receipt = "# w440 independent review receipt for w439\n\nSource: " + review_path.as_posix() + ". Recorded " + datetime.now(timezone.utc).isoformat() + ". These sections record the referee's verdict; this is not a review of that review. Source correction 004 is not included in this receipt.\n\n" + "\n\n".join(sections) + "\n\nNo full P0043 solution, novelty certification, served-account certification, or formal proof receipt is claimed.\n"
(ROOT / "REVIEW_RECEIPT_w440.md").write_text(receipt, encoding="utf-8")

claims = [json.loads(x) for x in (ROOT / "CLAIMS.jsonl").read_text(encoding="utf-8").splitlines() if x.strip()]
for c in claims:
    if c["claim_id"] in ids:
        c["status"] = "independently checked proof"
        c["independent_reviewer"] = "w440"
        c["review_status"] = "KEEP"
        c["review_receipt"] = "REVIEW_RECEIPT_w440.md"
        c["remaining_gap"] = "No gap found by w440 in this boundary result; the full P0043 target is not proved."
        c["brain_states"]["reviewed"] = True
        if c["claim_id"].endswith("001"):
            c["source"]["basis"] = "Independent elementary derivation; Hutchcroft's primary statement verifies that the intended target already assumes p_c<1."
    if c["claim_id"] == "w439-audit-w438-A":
        c["separate_referee_receipt"] = "w440 REVIEW_PACKET.md, w438-C02 KEEP; original independent audit by w439 is AUDIT_W438.md."
(ROOT / "CLAIMS.jsonl").write_text("".join(json.dumps(c, ensure_ascii=False) + "\n" for c in claims), encoding="utf-8")

handoff = json.loads((ROOT / "BRAIN_HANDOFF.json").read_text(encoding="utf-8"))
handoff["review_states"] = {"boundary_claims_001_003": "w440 KEEP", "boundary_bundle": "mathematical contents independently kept by w440; initial DRAFT annotations preserved", "source_correction_004": "pending w440", "all_packet_review_complete": False, "receipt": "REVIEW_RECEIPT_w440.md"}
handoff["reviewed"] = False  # Whole packet still includes the unreviewed correction.
handoff["ingested"] = "not observed; integrator not run"
handoff["retrievable"] = "not checked"
(ROOT / "BRAIN_HANDOFF.json").write_text(json.dumps(handoff, indent=2) + "\n", encoding="utf-8")
source = json.loads((ROOT / "SOURCE_STATUS.json").read_text(encoding="utf-8"))
source["independent_review"] = {"reviewer": "w440", "verdict": "KEEP on boundary claims 001-003", "receipt": "REVIEW_RECEIPT_w440.md", "source_correction_004": "pending"}
(ROOT / "SOURCE_STATUS.json").write_text(json.dumps(source, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

for filename in ("ATTEMPT.md", "REVIEW_PACKET.md"):
    path = ROOT / filename
    text = path.read_text(encoding="utf-8")
    note = "\n## Review receipt update\n\nw440 independently returned KEEP on w439 boundary claims 001-003, including the subdivision formula, graph-uniformity obstruction, exact 6L asymptotic and susceptibility divergence. See REVIEW_RECEIPT_w440.md. Source correction 004 remains pending. Submitted concept drafts keep their original preparation-time annotations; the receipt and BRAIN_HANDOFF.json record the subsequent review state. Ingestion and retrieval have not been checked.\n\nNEXT: w440 reviews source correction 004; coordinator integrates accepted concept drafts using the receipt and audits the local hook.\n"
    if "## Review receipt update" not in text:
        path.write_text(text + note, encoding="utf-8")

report_path = ROOT / "REPORT.md"
report = report_path.read_text(encoding="utf-8")
report = report.replace("This is a special case and a bridge counterexample, not a solution of P0043.", "w440 independently returned KEEP on the boundary proofs (claims 001-003); see REVIEW_RECEIPT_w440.md. This is a special case and a bridge counterexample, not a solution of P0043.")
report = report.replace("Reviewed/ingested/retrievable remain unobserved or pending in BRAIN_HANDOFF.json.", "BRAIN_HANDOFF.json records boundary proofs reviewed/KEEP, source correction pending, and ingestion/retrieval unobserved.")
report = report.replace("No live before/after recall effect was measured or claimed.", "No live before/after recall effect was measured or claimed. The staged hook passed two textual fire controls and two silence controls in HOOK_CONTROLS.json; deployed precision was not measured.")
report = report.replace("NEXT: w440 independently checks the subdivision and source-correction claims, then coordinator ingests the accepted concepts and checks retrieval of the resulting logical IDs.", "NEXT: w440 checks source correction 004; coordinator ingests accepted concept drafts with the independent KEEP receipt and checks retrieval of the resulting logical IDs.")
report_path.write_text(report, encoding="utf-8")

for field, local in (("submitted_path", "BRAIN_BUNDLE.json"), ("correction_submitted_path", "BRAIN_BUNDLE_CORRECTION.json")):
    assert Path(handoff[field]).read_text(encoding="utf-8") == (ROOT / local).read_text(encoding="utf-8")
assert json.loads((ROOT / "HOOK_CONTROLS.json").read_text(encoding="utf-8"))["passed"] == 4
status = "STATE: NEEDS_REVIEW\nNEXT: w440 reviews source correction 004; coordinator integrates accepted boundary concepts with the KEEP receipt and audits the staged hook.\n\n2026-10-10: Read PRIMARY_DIRECTIVE.md; saved the first boundary row before turn 20 and saved independent derivation before reading w438. Recall stopped at the authorized 60-second timeout; used the named proof-gap scar.\n2026-10-10: Exact target verified in Hutchcroft's primary paper; original P0043 book locator recovered, exact PDF not fetched. Full present openness UNKNOWN; no solution or novelty claim.\n2026-10-10: Independent tree obstruction shows critical one-arm supremum 1 over degree-3 quasi-transitive graphs at every fixed radius, with p_c<1 and extinction on each graph. Derived sharp 6L asymptotic and infinite critical susceptibility.\n2026-10-10: Audited w438's stated reciprocal identity, critical threshold and local-limit proof. Thirty finite checks passed (584 exact configurations, 0.015625 CPU seconds); two fire and two silent hook controls passed.\n2026-10-10: Submitted five concept DRAFT entries and three relations in two authorized w439 inbox bundles; mathematical store and memories were not edited. Five claim rows, unified diffs, REPORT.md and REVIEW_PACKET.md saved.\n2026-10-10: w440 independently kept claims 001-003; receipt saved. Source correction 004, global-hook audit, coordinator ingestion and retrieval remain pending. Prepared source correction repairs the old C0084 account of susceptibility at the endpoint; it does not discard the entire old attempt.\n"
(ROOT / "STATUS.md").write_text(status, encoding="utf-8")
print(json.dumps({"state": "NEEDS_REVIEW", "boundary_review": "w440 KEEP 001-003", "source_correction": "pending", "submitted_entries": 5, "submitted_relations": 3, "finite_checks_passed": 30, "hook_controls_passed": 4, "openness": "UNKNOWN"}))
