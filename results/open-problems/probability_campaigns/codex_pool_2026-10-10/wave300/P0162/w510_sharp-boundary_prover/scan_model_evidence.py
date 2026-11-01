"""Inspect only grep-selected model fields in the two cited worker streams."""
import hashlib
import json
from pathlib import Path
import re
import subprocess
from datetime import datetime, timezone

root = Path(__file__).resolve().parent
records = {}
for agent in ("w510", "w512"):
    path = root.parent / "runs" / f"{agent}_k01.jsonl"
    record = {"stream": str(path), "scope": "First three grep-selected model-bearing rows only; not a complete provenance audit", "verified_response_models": [], "candidates": []}
    if not path.is_file():
        record["state"] = "Named stream unavailable"
        records[agent] = record
        continue
    result = subprocess.run(["rg", "-n", "-m", "3", "-o", r'"model"\s*:\s*"[^"]+"', str(path)], capture_output=True, text=True, encoding="utf-8", errors="replace")
    record["grep_exit_code"] = result.returncode
    if result.returncode not in (0, 1):
        record["state"] = "Targeted grep failed; no identity certification"
        record["error"] = result.stderr[:400]
        records[agent] = record
        continue
    numbers = {int(match.group(1)) for line in result.stdout.splitlines() if (match := re.match(r"^(\d+):", line))}
    if numbers:
        with path.open(encoding="utf-8", errors="replace") as handle:
            for number, line in enumerate(handle, 1):
                if number > max(numbers):
                    break
                if number not in numbers:
                    continue
                if len(line) > 4_000_000:
                    record["candidates"].append({"line": number, "state": "Oversized row skipped"})
                    continue
                try:
                    row = json.loads(line)
                except (ValueError, TypeError):
                    record["candidates"].append({"line": number, "state": "Not a JSON response record"})
                    continue
                outer_type = row.get("type", row.get("event", "unknown")) if isinstance(row, dict) else "unknown"
                candidate = {"line": number, "outer_type": outer_type, "row_sha256": hashlib.sha256(line.encode("utf-8")).hexdigest(), "eligible_message_models": []}
                for keys in (("message",), ("payload", "message"), ("data", "message")):
                    message = row
                    for key in keys:
                        message = message.get(key) if isinstance(message, dict) else None
                    if isinstance(message, dict) and message.get("role") == "assistant" and isinstance(message.get("model"), str) and outer_type in ("assistant", "message_start", "response", "response_item", "response.completed"):
                        evidence = {"model": message["model"], "field": ".".join(keys) + ".model", "line": number, "stream": str(path), "row_sha256": candidate["row_sha256"]}
                        candidate["eligible_message_models"].append(evidence)
                        record["verified_response_models"].append(evidence)
                candidate["state"] = "Response message model found" if candidate["eligible_message_models"] else "No response-side assistant message.model; requested/context models excluded"
                record["candidates"].append(candidate)
    record["state"] = "Response-side evidence found; coordinator verifies account/different-model gate" if record["verified_response_models"] else "Response-side served identity not verified by this bounded search"
    records[agent] = record

receipt = {"checked_at_utc": datetime.now(timezone.utc).isoformat(), "agents": records, "requested_models_are_evidence": False, "account_separation": "not certified", "different_model_review": "not certified"}
(root / "SERVED_MODEL_EVIDENCE.json").write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8")
handoff_path = root / "HANDOFF.json"
handoff = json.loads(handoff_path.read_text(encoding="utf-8"))
handoff["response_side_evidence_search"] = str(root / "SERVED_MODEL_EVIDENCE.json")
handoff["sha256"][str(root / "SERVED_MODEL_EVIDENCE.json")] = hashlib.sha256((root / "SERVED_MODEL_EVIDENCE.json").read_bytes()).hexdigest()
for agent in records:
    if records[agent]["verified_response_models"]:
        handoff["served_model_evidence"]["author" if agent == "w510" else agent] = records[agent]["verified_response_models"]
handoff_path.write_text(json.dumps(handoff, indent=2) + "\n", encoding="utf-8")
print(json.dumps({agent: {"state": record["state"], "candidate_rows": len(record["candidates"]), "eligible_response_models": len(record["verified_response_models"])} for agent, record in records.items()}))
