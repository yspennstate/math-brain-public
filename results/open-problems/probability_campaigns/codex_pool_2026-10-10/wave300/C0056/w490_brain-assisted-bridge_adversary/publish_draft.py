"""Validate and submit only this worker's explicitly authorised DRAFT slot."""
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path

root = Path(__file__).resolve().parent
bundle_path = root / "bundle_001.json"
raw = bundle_path.read_bytes()
bundle = json.loads(raw)
assert bundle["spec"] == "mathbrain-draft-v1" and bundle["author_agent"] == "w490"
required = {"key", "namespace", "logical_name", "kind", "title", "statement", "proof_text", "assumptions", "domain", "source"}
keys = {entry["key"] for entry in bundle["entries"]}
assert len(keys) == len(bundle["entries"]) <= 200
for entry in bundle["entries"]:
    assert required <= entry.keys()
    assert entry["kind"] == "concept" and entry["proof_text"] is None
    assert entry["statement"].startswith("DRAFT, independent review pending.")
    assert entry["source"]["license"].startswith("owner-own-work")
for relation in bundle["relations"]:
    assert relation["from_key"] in keys
    if "to_key" in relation:
        assert relation["to_key"] in keys
    else:
        assert relation["to_existing_logical"].startswith("math:")

status_path = root / "SOURCE_STATUS.json"
status = json.loads(status_path.read_text(encoding="utf-8"))
for source in status["sources"]:
    if source.get("checked"):
        data = Path(source["path"]).read_bytes()
        assert hashlib.sha256(data).hexdigest() == source["sha256"]
        if source["path"].endswith(".pdf"):
            assert data.startswith(b"%PDF-")
        else:
            assert b"\\begin{theorem}" in data and b"\\label{thm:main}" in data

directory = Path("~/math-brain-inbox/w490").resolve()
assert directory.name == "w490" and directory.parent.name == "math-brain-inbox"
directory.mkdir(parents=True, exist_ok=True)
destination = directory / "bundle_001.json"
temporary = directory / "bundle_001.part"
if destination.exists():
    assert destination.read_bytes() == raw, "Existing draft is preserved; different content must use another slot."
else:
    if temporary.exists():
        assert temporary.read_bytes() == raw, "Preserve unmatched partial draft."
    else:
        with temporary.open("xb") as handle:
            handle.write(raw)
    temporary.rename(destination)
assert destination.read_bytes() == raw
receipt = {
    "utc": datetime.now(timezone.utc).isoformat(), "worker": "w490", "target": "C0056",
    "path": str(destination), "artifact_sha256": hashlib.sha256(raw).hexdigest(),
    "submitted": True, "reviewed": False, "ingested": False, "retrievable": False,
    "entries": len(bundle["entries"]), "relations": len(bundle["relations"]),
    "source_byte_hash_checks": "PASS", "schema_checks": "PASS", "proof_check": "NONE",
    "note": "Artifact hash is a handoff receipt, not an integrator seal or mathematical proof. No integration command was run.",
}
(root / "SUBMISSION_RECEIPT.json").write_text(json.dumps(receipt, indent=2), encoding="utf-8")
status.update(submitted=True, reviewed=False, ingested=False, retrievable=False, draft_submission=receipt)
status["owner_retirement_check"]["scope"] = status["owner_retirement_check"]["scope"].replace("canonical-store", "provided population-store")
status_path.write_text(json.dumps(status, indent=2), encoding="utf-8")
with (root / "REVIEW_PACKET.md").open("a", encoding="utf-8") as handle:
    handle.write(f"\nDRAFT submitted: {destination}\nArtifact SHA256: {receipt['artifact_sha256']}\nStates: submitted=true; reviewed=false; ingested=false; retrievable=false.\n")
with (root / "ATTEMPT.md").open("a", encoding="utf-8") as handle:
    handle.write("\n2026-10-10: Frozen independent derivation preceded the paired-proof read. w489 L3--L5 receive scoped conditional KEEP, with the fixed-disorder cavity moment, nonzero mass and GOE gaps retained. UI_SEPARATION.md shows why the higher-moment route is stronger than necessary. Scoped fallback recovered six cards; their full density assumptions were compared with the missing proof step. Primary source bytes and draft schema were checked; these are not theorem proofs. Draft submission is recorded separately from review/ingestion/retrieval.\n\nNEXT: w491 checks event-weighted L1 identification and the countable exhaustion in the joint-UI proof; then checks the ac/no-Lp example.\n")
print(json.dumps(receipt))
