"""Read only the two named P0110 store rows; save receipts in this folder."""
from __future__ import annotations

import hashlib
import json
import sqlite3
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DB = Path("~/math-brain-build/local/population/brain.sqlite3")


def main() -> None:
    peer = Path("~/brain_workers/w375/APPROACH_PRECOMMIT.md")
    content = peer.read_bytes()
    (ROOT / "PEER_SNAPSHOT.md").write_bytes(content)
    peer_receipt = {"source": str(peer), "snapshot": "PEER_SNAPSHOT.md",
                    "sha256": hashlib.sha256(content).hexdigest(),
                    "scope": "Original mathematical argument snapshot; no bundle manifest or proof attestation."}
    (ROOT / "PEER_SNAPSHOT_RECEIPT.json").write_text(json.dumps(peer_receipt, indent=2) + "\n", encoding="utf-8")

    conn = sqlite3.connect(DB.as_uri() + "?mode=ro", uri=True, timeout=3)
    try:
        schema = conn.execute("SELECT name,sql FROM sqlite_master WHERE type='table' AND name IN ('nodes','claims')").fetchall()
        result = {"db": str(DB), "mode": "ro", "schema": schema, "matched_rows": []}
        for table, _ in schema:
            columns = [r[1] for r in conn.execute(f'PRAGMA table_info("{table}")')]
            available = [x for x in ("id", "node_id", "claim_id", "logical_name", "namespace", "kind", "title", "statement", "body", "metadata_json", "body_json", "payload_json", "data_json") if x in columns]
            filters = [x for x in ("logical_name", "title", "body", "metadata_json", "body_json", "payload_json", "data_json") if x in columns]
            if not available or not filters:
                continue
            select = ",".join('"' + x + '"' for x in available)
            where = " OR ".join('lower("' + x + '") LIKE ?' for x in filters)
            rows = conn.execute(f'SELECT {select} FROM "{table}" WHERE {where} LIMIT 6', ["%p0110%"] * len(filters)).fetchall()
            result["matched_rows"].extend({"table": table, **dict(zip(available, row))} for row in rows)
        (ROOT / "STORE_SOURCE_RECEIPT.json").write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        print(json.dumps(result, indent=2, ensure_ascii=False))
        print(json.dumps(peer_receipt))
    finally:
        conn.close()


if __name__ == "__main__":
    main()
