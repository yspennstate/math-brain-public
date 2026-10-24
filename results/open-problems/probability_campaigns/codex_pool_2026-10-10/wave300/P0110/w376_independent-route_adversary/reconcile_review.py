"""Bind the requested referee verdict, reconcile local rows, and check the named drafts read-only."""
from __future__ import annotations

import hashlib
import json
import sqlite3
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent
REFEREE = Path("~/brain_workers/w377")
INBOX = Path("~/math-brain-inbox/w376/bundle_001.json")
DB = Path("~/math-brain-build/local/population/brain.sqlite3")


def save_json(name: str, data: object) -> None:
    (ROOT / name).write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def main() -> None:
    timestamp = datetime.now(timezone.utc).isoformat()
    artifacts = []
    for source_name, snapshot_name in (("REVIEW_PACKET.md", "REFEREE_VERDICT_SNAPSHOT.md"),
                                       ("CLAIMS.jsonl", "REFEREE_VERDICT_ROWS.jsonl")):
        content = (REFEREE / source_name).read_bytes()
        (ROOT / snapshot_name).write_bytes(content)
        artifacts.append({"source": str(REFEREE / source_name), "snapshot": str(ROOT / snapshot_name),
                          "sha256": hashlib.sha256(content).hexdigest(), "bytes": len(content)})
    referee_rows = {r["id"]: r for line in (ROOT / "REFEREE_VERDICT_ROWS.jsonl").read_text(encoding="utf-8").splitlines()
                    if line.strip() for r in [json.loads(line)]}
    mapping = {"w376-C001": ["w376-P0110-C001-review"],
               "w376-C002": ["w376-P0110-C002-review"],
               "w376-C003": ["w376-P0110-C003-review"],
               "w376-C004": ["w375-P0110-L1-review"],
               "w376-C005": ["P0110-source-quantifier-review"],
               "w376-C007": ["w375-P0110-L2-review", "w375-P0110-L3-review", "w375-P0110-L4-review"],
               "w376-C008": ["w376-P0110-C008-review"]}
    claims = [json.loads(line) for line in (ROOT / "CLAIMS.jsonl").read_text(encoding="utf-8").splitlines() if line.strip()]
    for claim in claims:
        ids = mapping.get(claim["claim_id"])
        if ids is None:
            continue
        rows = [referee_rows[rid] for rid in ids]
        assert all(row["verdict"].startswith("KEEP") for row in rows)
        claim["independent_reviewer"] = "w377; served-model provenance UNKNOWN"
        claim["referee_receipt"] = {"artifact": str(ROOT / "REFEREE_VERDICT_ROWS.jsonl"), "row_ids": ids,
                                    "verdicts": [row["verdict"] for row in rows]}
        claim["review_state"] = "w377 scoped KEEP; different-model gate pending; concept promotion not authorized"
        if claim["claim_id"] == "w376-C005":
            claim["review_state"] += "; referee explicitly retains an independent promotion gate"
        elif claim["claim_id"] in ("w376-C001", "w376-C002", "w376-C008"):
            claim["status"] = "independently checked proof"
        if claim["claim_id"] == "w376-C008":
            claim["remaining_gap"] = "No conclusion about centered fluctuation exponents, universality, novelty, or P0110; different-model promotion gate remains pending."
    (ROOT / "CLAIMS.jsonl").write_text("".join(json.dumps(row, ensure_ascii=False) + "\n" for row in claims), encoding="utf-8")

    local_bytes = (ROOT / "bundle_001.json").read_bytes()
    inbox_bytes = INBOX.read_bytes()
    assert inbox_bytes == local_bytes, "Inbox differs from the reviewed local draft: do not overwrite it."
    bundle = json.loads(local_bytes)
    assert len(bundle["entries"]) == 4 and len(bundle["relations"]) == 3
    assert all(e["kind"] == "concept" and e["proof_text"] is None for e in bundle["entries"])
    names = [e["logical_name"] for e in bundle["entries"]]
    candidates = names + [f"math:probability.fpp:{name}" for name in names]
    store_check = {"db": str(DB), "mode": "ro", "exact_logical_names": names,
                   "matched_nodes": [], "queries": [], "coverage": "This population DB only; no global ingestion or recall conclusion."}
    connection = sqlite3.connect(DB.as_uri() + "?mode=ro", uri=True, timeout=3)
    try:
        connection.execute("PRAGMA query_only=ON")
        for table in ("nodes", "claims"):
            columns = {row[1] for row in connection.execute(f'PRAGMA table_info("{table}")')}
            if not columns:
                continue
            expressions = []
            if "logical_name" in columns:
                expressions.append('"logical_name"')
            if "metadata_json" in columns:
                expressions.append('json_extract("metadata_json",\'$.logical_name\')')
            for expression in expressions:
                placeholders = ",".join("?" for _ in candidates)
                sql = f'SELECT {expression} FROM "{table}" WHERE {expression} IN ({placeholders}) LIMIT 8'
                matches = connection.execute(sql, candidates).fetchall()
                store_check["queries"].append({"table": table, "expression": expression, "matched": len(matches)})
                store_check["matched_nodes"].extend({"table": table, "logical_name": row[0]} for row in matches)
    except sqlite3.Error as error:
        store_check["error"] = str(error)
        store_check["coverage"] = "Bounded read-only lookup incomplete; ingestion remains unverified."
    finally:
        connection.close()
    save_json("RESUME_STORE_CHECK.json", store_check)
    receipt = {"timestamp_utc": timestamp, "command": "python -X utf8 ~/brain_workers/w376/reconcile_review.py",
               "referee_artifacts": artifacts, "kept_local_claim_ids": list(mapping),
               "bundle_path": str(INBOX), "bundle_sha256": hashlib.sha256(inbox_bytes).hexdigest(),
               "local_inbox_bytes_equal": True, "concept_entries": 4, "relations": 3,
               "independent_mathematical_review": "w377 scoped KEEP of the named rows",
               "reviewer_model": "UNKNOWN: no served-model provenance in the named referee artifacts",
               "different_model_keep_gate": "PENDING per the manager update delivered on resume",
               "C005_promotion_gate": "Referee explicitly retains a pending independent promotion gate",
               "bundle_review_complete": False, "integration_verified": False, "retrievability_verified": False,
               "target_verdict": "GAP", "current_openness": "UNKNOWN", "live_store_writes": 0,
               "byte_hash_scope": "Hashes bind artifacts; they do not prove mathematics or certify reviewer identity."}
    save_json("REFEREE_RECONCILIATION_RECEIPT.json", receipt)
    state = json.loads((ROOT / "SUBMISSION_STATE.json").read_text(encoding="utf-8"))
    state.update({"submitted": True, "reviewed": False, "independent_claim_review": "w377 scoped KEEP received",
                  "reviewed_claim_ids": list(mapping), "different_model_keep_gate": "PENDING",
                  "reviewer_model": "UNKNOWN", "review_receipt": str(ROOT / "REFEREE_RECONCILIATION_RECEIPT.json"),
                  "ingestion_check": str(ROOT / "RESUME_STORE_CHECK.json"),
                  "ingested": False, "retrievable": False,
                  "retrievability_check": "Not verified; bounded population lookup does not certify global ingestion or recall.",
                  "resume_command": receipt["command"]})
    save_json("SUBMISSION_STATE.json", state)
    print(json.dumps({"kept_claims": list(mapping), "concepts": 4, "relations": 3,
                      "bundle_sha256": receipt["bundle_sha256"], "model_gate": "PENDING",
                      "population_matches": len(store_check["matched_nodes"]),
                      "store_lookup_error": store_check.get("error"), "live_store_writes": 0}))


if __name__ == "__main__":
    main()
