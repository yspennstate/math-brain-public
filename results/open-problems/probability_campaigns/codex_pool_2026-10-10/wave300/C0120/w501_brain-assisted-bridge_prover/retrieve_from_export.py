"""Fallback: rg one named export with limits, then inspect only matching cards."""
import json
from pathlib import Path
import subprocess
import time

ROOT = Path(__file__).resolve().parent
EXPORT = "~/math-brain-build/export/population/nodes.jsonl"
PATTERN = "hypercontract|superconcentr|Gaussian covariance|Ornstein.Uhlenbeck|C0120"
started = time.monotonic()
receipt = {"source": EXPORT, "command": ["rg", "-i", "-m", "20", PATTERN, EXPORT],
           "deadline_seconds": 20, "limit": 20, "method": "targeted_rg_export_fallback"}
try:
    result = subprocess.run(receipt["command"], capture_output=True, text=True,
                            encoding="utf-8", errors="replace", timeout=20)
    rows = [json.loads(line) for line in result.stdout.splitlines() if line.strip()]
    receipt.update(exit_code=result.returncode, timed_out=False, returned=len(rows), stderr=result.stderr)
    (ROOT / "retrieved_cards.json").write_text(json.dumps(rows, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
    print(json.dumps([{"id": r.get("id"), "title": r.get("title"), "kind": r.get("kind")} for r in rows]))
except subprocess.TimeoutExpired:
    receipt.update(exit_code=None, timed_out=True, returned=0)
receipt["elapsed_seconds"] = time.monotonic()-started
(ROOT / "retrieval_fallback_receipt.json").write_text(json.dumps(receipt, indent=2)+"\n", encoding="utf-8")
print(json.dumps(receipt))
