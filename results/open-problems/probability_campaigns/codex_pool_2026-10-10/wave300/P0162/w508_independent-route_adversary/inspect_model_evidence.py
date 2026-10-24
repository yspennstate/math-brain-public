"""Inspect only model-bearing metadata in this native transcript; never copy text."""
import collections
import datetime as dt
import hashlib
import json
import pathlib
import subprocess

ROOT = pathlib.Path(__file__).resolve().parent
locator = json.loads((ROOT / "MODEL_RECEIPT_LOCATOR.json").read_text(encoding="utf-8-sig"))
records = []
for filename in locator.get("author_transcript_candidates", [])[:1]:
    path = pathlib.Path(filename)
    result = subprocess.run(
        ["rg", "-n", "--max-count", "120", r'"model"\s*:', str(path)],
        capture_output=True, text=True, encoding="utf-8", timeout=25, check=False,
    )
    if result.returncode not in (0, 1):
        raise RuntimeError("Targeted metadata search failed")
    matched = result.stdout.splitlines()
    counts = collections.Counter()
    response_models = []
    for numbered in matched:
        line_number, raw = numbered.split(":", 1)
        obj = json.loads(raw)
        kind = obj.get("type", "unknown")
        counts[kind] += 1
        payload = obj.get("payload", {})
        if not isinstance(payload, dict):
            continue
        is_response = kind == "response_item" and payload.get("role") == "assistant"
        is_assistant = kind == "assistant" and isinstance(obj.get("message"), dict)
        if not (is_response or is_assistant):
            continue
        candidates = [("payload.model", payload.get("model"))]
        if is_assistant:
            candidates.append(("message.model", obj["message"].get("model")))
        for key, model in candidates:
            if isinstance(model, str) and model and model != "<synthetic>":
                response_models.append({
                    "line": int(line_number), "record_type": kind,
                    "field": key, "model": model,
                    "metadata_line_sha256": hashlib.sha256(raw.encode("utf-8")).hexdigest(),
                })
    records.append({
        "path": str(path), "matched_metadata_lines": len(matched),
        "record_type_counts": dict(counts), "search_capped": len(matched) >= 120,
        "response_model_evidence": response_models,
    })

evidence = [item for record in records for item in record["response_model_evidence"]]
out = {
    "checked_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
    "author_agent": "w508", "author_native_thread_id": locator["author_thread_id"],
    "author_served_model_state": "verified_response_metadata" if evidence else "UNKNOWN",
    "author_transcript_checks": records,
    "referee_agent": "w509", "referee_served_model_state": "UNKNOWN",
    "referee_receipt_request": "msg-fa4f0c217b",
    "different_model_gate": "not_verified",
    "policy": "Requested models, registration/runtime and turn_context are excluded from served-model evidence. No transcript message text copied.",
}
(ROOT / "MODEL_EVIDENCE.json").write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
print(json.dumps(out))
