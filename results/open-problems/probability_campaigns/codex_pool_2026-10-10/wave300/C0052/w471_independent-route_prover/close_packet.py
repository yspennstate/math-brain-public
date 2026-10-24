"""Record final review-ready state after confirmed named-peer deliveries."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json

HERE = Path(__file__).resolve().parent
delivery = json.loads((HERE / "HANDOFF_RECEIPT.json").read_text(encoding="utf-8"))
assert delivery["statement_sent"] and delivery["proof_sent"]
messages = {attempt["peer"]: json.loads(attempt["stdout"])["message_id"]
            for attempt in delivery["attempts"] if attempt["returncode"] == 0}
source_path = HERE / "SOURCE_STATUS.json"
source = json.loads(source_path.read_text(encoding="utf-8"))
source["local_evidence"]["scope_boundaries"] = "SCOPE_BOUNDARIES.md; only four STATUS lines read from nearby lanes; no proposed core proof or referee verdict read"
source["review"]["handoff"] = {"statement_to_w472": messages["w472"], "complete_packet_to_w473": messages["w473"], "receipt": "HANDOFF_RECEIPT.json"}
source_path.write_text(json.dumps(source, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

claims_path = HERE / "CLAIMS.jsonl"
claims = [json.loads(line) for line in claims_path.read_text(encoding="utf-8").splitlines() if line.strip()]
if "w471-C0052-source" not in {row["id"] for row in claims}:
    row = {"id": "w471-C0052-source", "status": "conjecture",
           "statement": "C0052's primary target is that g_+(beta)=-sum_{x2,x3,x4} U4(0,x2,x3,x4)/(chi(beta)^2 xi(beta)^3) does not tend to zero as beta increases to beta_c from below in the nearest-neighbor zero-field ferromagnetic Ising free state on Z^3. Here U4 is the four-spin moment minus its three two-point pairings, chi=sum_x <sigma_0 sigma_x>, and xi=(lim_n[-log <sigma_0 sigma_ne1>/n])^(-1). The primary source uses the opposite signed coupling; vanishing is unchanged. An eventual positive lower bound is stronger than this target. Source statement verified; current openness UNKNOWN; this attempt does not prove the target.",
           "assumptions": ["Nearest-neighbor ferromagnetic Ising model on Z^3", "Symmetric free infinite-volume state at zero field", "beta approaches beta_c from below", "Exponential, not second-moment, correlation length"],
           "source": "Duminil-Copin 2017, Conjecture 6 and equations (7.1)-(7.2), p.94; Exercise 34, p.42; https://www.ihes.fr/~duminil/publi/2017PIMS.pdf",
           "source_quote_location": "SOURCE_STATUS.json: primary_source.short_quote",
           "proof_or_counterexample": "Primary source and exact normalization verified; no mathematical proof of this conjecture. Historical unreviewed source/store records and 4D theorem do not certify current 3D status.",
           "independent_reviewer": "w473; packet delivered, independent disposition pending",
           "remaining_gap": "The full target is unproved in this attempt; the proposed sufficient normalized-zero condition is recorded in w471-C0052-gap.",
           "parent_problem_solved": False, "supersedes_scope_checkpoint": "w471-C0052-scope-001"}
    with claims_path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(row, ensure_ascii=False) + "\n")

report_path = HERE / "REPORT.md"
report = report_path.read_text(encoding="utf-8").replace("selected correlation-scale Gibbs blocks", "selected susceptibility-quantile Gibbs blocks")
report = report.replace("Peer delivery receipts and the separate submitted/reviewed/ingested/retrievable states are recorded on disk.",
                        "Named-peer delivery succeeded: statement-only packet to w472, then full packet to w473. HANDOFF_RECEIPT.json records both message IDs and the earlier failed team routes. Submitted, reviewed, ingested, and retrievable states remain separate in BUNDLE_STATE.json.")
report_path.write_text(report, encoding="utf-8")

hash_path = HERE / "REVIEW_HASHES.json"
frozen = json.loads(hash_path.read_text(encoding="utf-8"))
frozen["timestamp"] = datetime.now(timezone.utc).isoformat()
frozen["sha256"] = {name: hashlib.sha256((HERE / name).read_bytes()).hexdigest()
                    for name in frozen["sha256"]}
assert frozen["sha256"]["ATTEMPT.md"] == "7be0737e6fcd5803a673f0cb426d3343984a8f481d5c7ed8ca5e88d3ab2d2b2d"
hash_path.write_text(json.dumps(frozen, indent=2) + "\n", encoding="utf-8")

packet_state = json.loads((HERE / "BUNDLE_STATE.json").read_text(encoding="utf-8"))
measurements = json.loads((HERE / "MEASUREMENTS.json").read_text(encoding="utf-8"))
assert packet_state["local_schema_check"].startswith("PASS")
assert measurements["status"] == "PASS" and measurements["failed_assertions"] == 0
for filename in ("SOURCE_STATUS.json", "ATTEMPT.md", "CLAIMS.jsonl", "REVIEW_PACKET.md", "REPORT.md"):
    assert (HERE / filename).is_file() and (HERE / filename).stat().st_size > 0

(HERE / "STATUS.md").write_text(
    "STATE: NEEDS_REVIEW\n"
    "NEXT: w473 audits L1/L2 and the source row; the next proof step is a bounded normalized first-zero subsequence for the exact susceptibility-quantile Gibbs blocks.\n\n"
    "2026-10-10: Recovered the exact C0052 primary statement and sign/length definitions. Current openness UNKNOWN; parent target unproved; no novelty claim.\n"
    "2026-10-10: Recorded the Lee–Yang route before peer proof access; digested the older random-current attempt. Read only nearby STATUS metadata for scope boundaries; no proposed core proof or referee verdict read.\n"
    "2026-10-10: Saved two author-derived conditional lemmas, including g_+>=3/r^4, their exact hypotheses and proofs, the single hardest normalized-zero gap, and independent-spin controls.\n"
    "2026-10-10: Fresh CPU-only diagnostics passed 23 analytical/finite cases, 1,620 enumerated configurations, and eight geometry controls; zero failures. Maximum relative cumulant discrepancy 4.17e-15.\n"
    "2026-10-10: Submitted four concept-only DRAFT entries and four supported relations to math-brain-inbox/w471/bundle_001.json; local schema checks passed. Review, ingestion, and retrieval are unconfirmed and tracked separately.\n"
    "2026-10-10: Early team transports failed (lock/stale team). Resolved via task-authorized direct named-peer mesh; statement to w472 preceded full packet to w473. Delivery IDs recorded in HANDOFF_RECEIPT.json.\n"
    "2026-10-10: Review packet frozen in REVIEW_HASHES.json; author served-model response receipt unavailable; independent review pending. Hook and owner progress event staged locally under the folder-only rule.\n",
    encoding="utf-8")
print(json.dumps({"state": "NEEDS_REVIEW", "messages": messages,
                  "claim_rows": sum(1 for line in claims_path.read_text(encoding="utf-8").splitlines() if line.strip()),
                  "draft_entries": packet_state["entries"], "independent_review": "pending",
                  "parent_solved": False}))
