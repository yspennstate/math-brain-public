from pathlib import Path
import hashlib
import json

root = Path(__file__).resolve().parent
receipts = []
for source_name, output_name in [("PROVED_LEMMAS.md", "PEER_PROOF_SNAPSHOT.md"),
                                 ("STATEMENT_FOR_ADVERSARY.md", "PEER_STATEMENT_SNAPSHOT.md")]:
    source = Path("~/brain_workers/w375") / source_name
    raw = source.read_bytes()
    output = root / output_name
    output.write_bytes(raw)
    receipts.append({"source": str(source), "snapshot": output_name,
                     "sha256": hashlib.sha256(raw).hexdigest(),
                     "reviewed_scope": "L1-L4 only" if source_name == "PROVED_LEMMAS.md" else "Target statement, no proof claim",
                     "scope": "Byte binding of original artifact; not mathematical verification or a bundle manifest."})
(root / "PEER_PROOF_RECEIPTS.json").write_text(json.dumps(receipts, indent=2) + "\n", encoding="utf-8")
print(json.dumps(receipts, indent=2))
