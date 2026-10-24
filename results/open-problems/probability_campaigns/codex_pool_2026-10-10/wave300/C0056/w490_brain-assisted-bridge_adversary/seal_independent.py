import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

root = Path(__file__).resolve().parent
path = root / "INDEPENDENT.md"
receipt = {
    "worker": "w490", "target": "C0056",
    "utc": datetime.now(timezone.utc).isoformat(),
    "file": str(path), "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
    "paired_proof_read": False,
    "meaning": "Order/provenance checkpoint, not a mathematical verification.",
}
out = root / "independence_receipt.json"
if out.exists():
    raise SystemExit("Existing independence receipt is preserved; do not overwrite it.")
out.write_text(json.dumps(receipt, indent=2), encoding="utf-8")
print(json.dumps(receipt))
