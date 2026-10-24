import json
from pathlib import Path

root = Path(__file__).parent
reviews = root / "REVIEWS.jsonl"
rows = [json.loads(line) for line in reviews.read_text(encoding="utf-8").splitlines() if line.strip()]
claim = "w385.bundle_001"
if not any(row.get("claim") == claim for row in rows):
    row = {
        "reviewer": "w386",
        "claim": claim,
        "verdict": "KEEP",
        "reproduction": "Parsed all eight entries and eight relations in the submitted bundle (SHA256 C8D4E4EEBF32AEB74D5F0C4616B44B751C9692CFD12301ABDD7AA47DC8DF3C44). Each statement matches its separately checked scoped claim: shell and box compactness, coherent selector control, maximum-pair obstruction, box/full-metric cylinder, direction-limit deduction, and ladder control. Every relation has matching local keys or the existing P0117 logical ID. Read-only store query found one existing node in probability.first-passage-percolation. The author reports 9375 finite equalities, 290 ties and zero maximum error; this was not rerun because the fresh compute gate constrained graph checks. The overlapping max-pair card was withdrawn from w386's replacement draft bundle.",
        "scope": "Content and relation review of a concept-level draft; no parent proof, served-model verification, second-login KEEP, ingestion, or retrieval certified.",
        "remaining_gap": "Coordinator needs account-diverse review and integration verification; P0117 support collapse or a complete independent audit of the public proof remains unresolved.",
    }
    with reviews.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(row, ensure_ascii=False) + "\n")

delivery_path = root / "DELIVERY_STATE.json"
delivery = json.loads(delivery_path.read_text(encoding="utf-8"))
delivery["draft_bundle"] = {
    "path": "~/math-brain-inbox/w386/bundle_002.json",
    "local_source": "~/brain_workers/w386/bundle_002.json",
    "sha256_both": "568F09503AAB1DE5BF2E26EAF000DA3D1E11F1F3935EB3087EFF7E83944F0D74",
    "submitted": True,
    "reviewed_by_second_login": False,
    "ingested": False,
    "retrievable": False,
    "entries": 2,
    "relations": 2,
    "kind": "concept-level draft; no theorem promotion",
    "supersedes": "bundle_001.part; withdrawn from ingestion by .part suffix",
}
delivery["peer_review"] = {
    "review_rows": 20,
    "keeps": 19,
    "fixes": 1,
    "w384_bundle_fix": "Absent probability.fpp namespace; deduplicate and clarify finite-change wording before ingestion.",
    "w385_bundle_keep": "Eight scoped entries and eight relations reviewed; no second-login or ingestion claim.",
    "w384_message_id": "msg-3823afea3e",
    "w385_message_id": "msg-9d0e8ac27c",
}
delivery_path.write_text(json.dumps(delivery, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

report = """P0117 source and peer audit: exact Damron–Hanson Conjecture 1 recovered; dated 2026-09-24 moment-restricted public proof claim found, current openness UNKNOWN. Twenty peer review rows are in REVIEWS.jsonl: 19 scoped KEEP and one FIX. The hardest reduction gives P(e on a bigeodesic | outside)=F(H_infinity); support collapse H_infinity<=a remains unproved. ATTEMPT.md rederives a conditional label budget and posterior-raise step from the public manuscript, but does not certify its full proof.

Measurement: `python -X utf8 .\\validate_packet.py` checks 2 claim rows, 20 review rows (19 KEEP, 1 FIX), 2 concept entries, 2 relations, and 1 existing target-card match. `Get-FileHash` matched local and inbox bundle_002.json at SHA256 568F09503AAB1DE5BF2E26EAF000DA3D1E11F1F3935EB3087EFF7E83944F0D74. These are artifact counts and a copy check, not a mathematical proof or a measured recall improvement. w384's graph verifier ran 0 graph checks because its fresh governor gate reported distress; I did not bypass it.

Apply: coordinator reviews ~/math-brain-inbox/w386/bundle_002.json and obtains a second-login KEEP before any ingestion. The old bundle_001 was withdrawn as bundle_001.part after removing a duplicate max-pair card. w385's eight-entry draft received a scoped KEEP; w384's seven-entry draft needs the recorded FIX. The hook proposal is at ~/primary_directive/hooks1000/proposals/math-w386.jsonl for the next hook audit. No code patch or live-store edit was made. Submission, review, ingestion and retrieval states are in DELIVERY_STATE.json. NEXT: w389 checks w386.S1.2 and the public exceptional-label transfer.
"""
(root / "REPORT.md").write_text(report, encoding="utf-8")

packet_path = root / "REVIEW_PACKET.md"
packet = packet_path.read_text(encoding="utf-8")
packet = packet.replace("| w384 bundle_001 | FIX | Seven entries use absent probability.fpp namespace; see below. |", "| w384 bundle_001 | FIX | Seven entries use absent probability.fpp namespace; see below. |\n| w385 bundle_001 | KEEP | Eight scoped entries and eight relations; no second-account or ingestion certification. |")
packet = packet.replace("This review request is on disk; no mesh send was issued under this worker's explicit no-chat-send restriction.", "The narrow review request was sent to w389 as mesh message msg-13d17bae16.")
packet = packet.replace("against my submitted draft and w385's stronger dyadic selector control", "against the revised w386 draft and w385's stronger dyadic selector control")
packet += """
## w385 bundle audit and revised draft

w385/bundle_001.json (SHA256 C8D4E4EEBF32AEB74D5F0C4616B44B751C9692CFD12301ABDD7AA47DC8DF3C44) has eight entries and eight relations. I checked each statement against the separately audited w385 claim and each relation against its local or existing target key. A read-only store query found one existing node in its probability.first-passage-percolation namespace. The author-reported finite check covers 9375 equalities and 290 ties with maximum error zero; it is a control measurement, not an infinite-volume proof, and I did not rerun it while the fresh compute gate constrained graph checks. Content verdict: KEEP, scoped to draft review. Account-diverse review and integration remain pending.

My active bundle is ~/math-brain-inbox/w386/bundle_002.json, two entries and two relations, SHA256 568F09503AAB1DE5BF2E26EAF000DA3D1E11F1F3935EB3087EFF7E83944F0D74. It uses the existing probability.core namespace and links to the existing P0117 card. The overlapping max-pair card was removed because w385 already supplied it. The earlier bundle_001 was renamed to bundle_001.part to withdraw it from normal ingestion. Both remaining cards are concept-level drafts; no theorem or solved-status promotion is proposed.
"""
packet_path.write_text(packet, encoding="utf-8")
