"""Check captured artifact hashes; this is packaging verification, not a proof."""
import datetime as dt
import hashlib
import json
from pathlib import Path

root = Path(__file__).resolve().parent
manifest_path = root / "INTEGRATION_HANDOFF.json"
manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
checked = []
for artifact in manifest["artifacts"]:
    path = Path(artifact["path"])
    actual = hashlib.sha256(path.read_bytes()).hexdigest()
    assert actual == artifact["sha256_at_capture"], f"Changed artifact: {path}"
    checked.append(str(path))
bundle = Path(manifest["bundle"]["path"])
assert hashlib.sha256(bundle.read_bytes()).hexdigest() == manifest["bundle"]["sha256"]
assert len(manifest["scoped_KEEP"]) == 3
assert manifest["model_evidence"]["different_model_gate"] == "not_verified"
out = {
    "checked_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
    "command": "python -X utf8 ~/brain_workers/w508/validate_handoff.py",
    "state": "passed", "artifact_hashes_checked": len(checked), "scoped_KEEP_rows": 3,
    "manifest_sha256": hashlib.sha256(manifest_path.read_bytes()).hexdigest(),
    "mathematical_proof": False, "formal_receipt": None,
    "served_model_gate_verified": False, "ingestion_or_retrieval_verified": False,
}
(root / "HANDOFF_VALIDATION.json").write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
print(json.dumps(out))
