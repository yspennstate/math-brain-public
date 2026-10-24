"""Hash only the named P0162 handoff artifacts; no live mutation."""

import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path


paths = [
    Path("~/brain_workers/w510/CLAIMS.jsonl"),
    Path("~/math-brain-inbox/w510/bundle_001.json"),
    Path("~/brain_workers/w511/CLAIMS.jsonl"),
    Path("~/math-brain-inbox/w511/bundle_002.json"),
    Path("~/brain_workers/w512/VERDICTS.jsonl"),
    Path("~/brain_workers/w512/REVIEW_PACKET.md"),
    Path("~/brain_workers/w512/DRAFT_BUNDLE.json"),
]
receipt = {
    "target": "P0162",
    "integration_contact": "codex-01a12190",
    "checked_utc": datetime.now(timezone.utc).isoformat(),
    "scoped_verdicts": "KEEP w510 C001-C004 and w511 C001-C004; no universal FEI proof or novelty claim",
    "hardest_gap": "Dimension-free mass-weighted spectral entropy budget or suitable-coordinate selection for arbitrary Boolean functions",
    "served_model_evidence": "Unavailable to w512; requested model/tier is not a served-model receipt; coordinator must verify response-side evidence",
    "account_separation_evidence": "Unavailable to w512; coordinator must verify accounts before using two-Codex quorum",
    "sha256": {str(path): hashlib.sha256(path.read_bytes()).hexdigest() for path in paths},
}
out = Path(__file__).resolve().parent / "HANDOFF.json"
out.write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8")
for path in paths:
    print(f"{path.name}: {receipt['sha256'][str(path)][:16]}...")
