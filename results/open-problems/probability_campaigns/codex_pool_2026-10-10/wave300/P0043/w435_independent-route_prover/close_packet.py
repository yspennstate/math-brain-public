"""Check the published DRAFT and save final handoff/source receipts locally."""
from datetime import datetime, timezone
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parent
now = datetime.now(timezone.utc).isoformat()
submission = json.loads((ROOT / "SUBMISSION.json").read_text(encoding="utf-8"))
assert submission["submitted"]["state"] is True
published = Path(submission["submitted"]["path"])
assert published.read_bytes() == (ROOT / "draft_bundle_001.json").read_bytes()
bundle = json.loads(published.read_text(encoding="utf-8"))
assert len(bundle["entries"]) == 8 and len(bundle["relations"]) == 7
assert all(e["kind"] in {"concept", "definition"} and e["proof_text"] is None for e in bundle["entries"])
delivery = json.loads((ROOT / "DELIVERY_w437.json").read_text(encoding="utf-8"))
assert delivery["inserted"] == 1 and delivery["to"] == "w437"

source_file = ROOT / "SOURCE_STATUS.json"
source = json.loads(source_file.read_text(encoding="utf-8"))
source["canonical_store_limit"] = {
    "repository": "~/math-research-brain",
    "population_default": "~/math-research-brain/local/population/brain.sqlite3",
    "population_default_present": False,
    "stuck": "STUCK: repository-relative population default is absent. A targeted local SQLite filename search found only two audit snapshots; these were not opened. Use the explicitly provided read-only active population store for historical cards, and do not certify current canonical status.",
    "provided_population_read": "~/math-brain-build/local/population/brain.sqlite3",
    "provided_population_rows_read": 4, "receipt": "STORE_SOURCE_ROWS.json",
    "current_canonical_resolution_verified": False
}
source["assigned_referee_delivery"] = {"to": "w437", "message_id": delivery["message_id"],
    "inserted": 1, "final_packet": "REVIEW_PACKET.md", "mathematical_review_complete": False}
source_file.write_text(json.dumps(source, indent=2)+"\n", encoding="utf-8")

validation_file = ROOT / "VALIDATION.json"
validation = json.loads(validation_file.read_text(encoding="utf-8"))
validation.update({"published_draft_matches_local": True, "publication_checked_at": now,
                   "designated_referee_delivery": delivery["message_id"]})
validation_file.write_text(json.dumps(validation, indent=2)+"\n", encoding="utf-8")

comm_file = ROOT / "COMMUNICATION.md"
comm = comm_file.read_text(encoding="utf-8")
comm = comm.replace("Inbox submission receipt: pending.",
    "Inbox submitted at "+submission["submitted"]["at"]+": "+str(published)+"; eight definition/concept entries, seven relations. Full designated review, ingestion and retrieval are not confirmed. Final referee update: "+delivery["message_id"]+", inserted=1.")
comm_file.write_text(comm, encoding="utf-8")

for name in ("REPORT.md", "REVIEW_PACKET.md"):
    p = ROOT / name
    text = p.read_text(encoding="utf-8")
    if "Publication receipt:" not in text:
        text += "\nPublication receipt: "+str(published)+", submitted "+submission["submitted"]["at"]+". Published bytes match the validated local DRAFT. Final referee update "+delivery["message_id"]+" delivered to w437. Review, ingestion and retrieval are recorded separately and remain unconfirmed. Canonical-source limit: the repository's population default is absent; only audit snapshots were located and not opened. Four directly relevant cards were read from the explicitly provided population store. Current openness stays UNKNOWN.\n"
    p.write_text(text, encoding="utf-8")

summary = {"checked_at": now, "claim_rows": 8, "draft_entries": 8, "relations": 7,
    "finite_checks_passed": 48, "enumerated_configurations": 9312,
    "auxiliary_keep_count_w436": 4, "G1": "unproved completion premise",
    "submitted": True, "designated_review_complete": False,
    "ingestion_receipt_obtained": False, "retrieval_receipt_obtained": False,
    "full_target_proved": False, "current_openness": "UNKNOWN",
    "referee_message": delivery["message_id"]}
(ROOT / "FINAL_CHECK.json").write_text(json.dumps(summary, indent=2)+"\n", encoding="utf-8")
print(json.dumps(summary))
