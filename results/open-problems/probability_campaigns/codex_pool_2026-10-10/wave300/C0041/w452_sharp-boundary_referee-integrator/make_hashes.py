"""Record final local artifact hashes for handoff; hashes are not proof receipts."""

import hashlib
import json
from pathlib import Path


root = Path(__file__).parent
names = [
    "SOURCE_STATUS.json",
    "CLAIMS.jsonl",
    "ATTEMPT.md",
    "bundle_001.json",
    "RELATIONS_EVIDENCE.md",
    "REVIEW_PACKET.md",
    "REPORT.md",
    "hook_proposal.jsonl",
    "patches/01_bundle.diff",
    "patches/02_hook.diff",
]
hashes = {name: hashlib.sha256((root / name).read_bytes()).hexdigest() for name in names}
(root / "HASHES.json").write_text(json.dumps({"algorithm": "sha256", "files": hashes}, indent=2) + "\n", encoding="utf-8")
print(f"PASS: hashed {len(hashes)} final artifacts")
