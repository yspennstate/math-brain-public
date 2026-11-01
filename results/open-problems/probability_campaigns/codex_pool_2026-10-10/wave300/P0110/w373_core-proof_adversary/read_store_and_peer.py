"""Read only the P0110 card and the named paired proof; save worker receipts."""
from pathlib import Path
import hashlib
import json
import sqlite3

root = Path(__file__).resolve().parent
store_path = Path("~/math-brain-build/local/population/brain.sqlite3")
receipt = {"database_mode":"ro", "path":str(store_path), "target":"P0110", "rows":[]}
if store_path.is_file():
    with sqlite3.connect(store_path.as_uri()+"?mode=ro",uri=True,timeout=3) as conn:
        conn.execute("PRAGMA query_only=ON")
        conn.row_factory = sqlite3.Row
        receipt["rows"] = [dict(row) for row in conn.execute(
            "SELECT id,kind,title,body,metadata_json FROM nodes WHERE title=? OR title=? LIMIT 6",
            ("Open problem: An iid FPP law with proved KPZ exponent relation", "An iid FPP law with proved KPZ exponent relation"))]
else:
    receipt["status"] = "named population store missing"
(root / "store_target_receipt.json").write_text(json.dumps(receipt,ensure_ascii=False,indent=2),encoding="utf-8")
print(json.dumps(receipt,ensure_ascii=False,indent=2))

proof = Path("~/brain_workers/w372/ATTEMPT.md")
if proof.is_file():
    data = proof.read_bytes()
    (root / "paired_ATTEMPT_snapshot.md").write_bytes(data)
    snap = {"path":str(proof), "snapshot":"paired_ATTEMPT_snapshot.md", "sha256":hashlib.sha256(data).hexdigest(),
            "bytes":len(data), "independent_checkpoint":"INDEPENDENT.md saved before paired proof was read", "hash_is_proof":False}
    (root / "paired_snapshot_receipt.json").write_text(json.dumps(snap,indent=2),encoding="utf-8")
    print(json.dumps(snap,indent=2))
    for i,line in enumerate(data.decode("utf-8-sig").splitlines(),1):
        print(f"{i}: {line}")
else:
    print("Paired ATTEMPT.md not present; independent packet remains available.")
