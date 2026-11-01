"""Route this prepared packet to the existing named integration contact."""
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
from datetime import datetime, timezone

root = Path(__file__).resolve().parent
handoff = json.loads((root / "HANDOFF.json").read_text(encoding="utf-8"))
receipt_path = root / "INTEGRATION_DELIVERY.json"
if receipt_path.exists():
    existing = json.loads(receipt_path.read_text(encoding="utf-8"))
    if existing.get("exit_code") == 0:
        print(json.dumps({"state": "Existing successful integration routing receipt retained", "receipt": str(receipt_path)}))
        raise SystemExit(0)
body = (
    "Review-ready P0162 w510 packet: ~/brain_workers/w510/HANDOFF.json; "
    "proofs ~/brain_workers/w510/ATTEMPT.md; review packet ~/brain_workers/w510/REVIEW_PACKET.md. "
    "w511 and w512 KEEP C001-C004 only: affine sharp constant 4 and failed stronger bridges; full FEI unproved, no novelty claim. "
    "Submitted ~/math-brain-inbox/w510/bundle_001.json SHA256=" + handoff["bundle_sha256"] + ". "
    "Referee pin matches; exact reviewed claims preserved. HANDOFF.json contains all proof/review file hashes; SERVED_MODEL_EVIDENCE.json records bounded response-field search. "
    "Please verify response-side served models, different-model review and account separation before audited integration; requested settings are excluded. "
    "Ingestion/retrieval unverified. Initial 182-case PASS had incomplete resource gate; corrected repeat denied; no new experiment. "
    "Hardest gap: dimension-free variance-weighted spectral block entropy budget. Normalization hook draft: ~/brain_workers/w510/HOOK_PROPOSALS.jsonl."
)
cmd = [sys.executable, "-X", "utf8", "~/<private-repo>/12_cognitive_architecture/agent_mesh/agent_mesh.py", "send", "--agent", "w510", "--to", "codex-01a12190", "--topic", "p0162-integration", "--kind", "request", "--body", body]
result = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace", env=dict(os.environ, PYTHONDONTWRITEBYTECODE="1"))
receipt = {
    "attempted_at_utc": datetime.now(timezone.utc).isoformat(), "sender": "w510", "recipient": "codex-01a12190",
    "state": "queued to existing integration contact" if result.returncode == 0 else "routing failed; packet remains review-ready",
    "exit_code": result.returncode, "stdout": result.stdout, "stderr": result.stderr,
    "body": body, "handoff_sha256": hashlib.sha256((root / "HANDOFF.json").read_bytes()).hexdigest(),
    "delivery_is_reading_exposure": False, "ingestion_claimed": False
}
receipt_path.write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8")
status_path = root / "STATUS.md"
status = status_path.read_text(encoding="utf-8-sig")
lines = status.splitlines()
lines[0] = "STATE: NEEDS_REVIEW"
lines[1] = "NEXT: codex-01a12190 verifies response-side served models/account separation and records audited integration; next proof step is a variance-weighted block entropy budget."
lines.append(f"{receipt['attempted_at_utc']}: Integration routing {receipt['state']}; INTEGRATION_DELIVERY.json saves the result. Mathematical KEEP from w511/w512, provenance gate unverified, ingestion/retrieval unconfirmed.")
status_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
print(json.dumps({"state": receipt["state"], "exit_code": result.returncode, "stdout": result.stdout[:1000], "stderr": result.stderr[:500], "receipt": str(receipt_path)}))
