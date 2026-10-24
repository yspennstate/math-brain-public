"""Read exactly the returned cards and a bounded list of named bridge titles."""
import json
from pathlib import Path
import sqlite3
import time

root = Path(__file__).resolve().parent
database = "~/math-brain-build/local/population/brain.sqlite3"
raw = (root / "math_recall.txt").read_bytes()
encoding = "utf-16" if raw.startswith((b"\xff\xfe", b"\xfe\xff")) else "utf-8-sig"
recall = json.loads(raw.decode(encoding))
started = time.perf_counter()
cards = []
with sqlite3.connect("file:" + database + "?mode=ro", uri=True, timeout=5) as connection:
    connection.row_factory = sqlite3.Row
    connection.execute("PRAGMA query_only=ON")
    for hit in recall["hits"]:
        row = connection.execute(
            "SELECT id,kind,title,body,metadata_json,digest FROM nodes WHERE id=?", (hit["id"],)
        ).fetchone()
        if row is None:
            raise RuntimeError("Returned card disappeared: " + hit["id"])
        card = dict(row)
        card["metadata"] = json.loads(card.pop("metadata_json"))
        claim = connection.execute("SELECT payload_json FROM claims WHERE id=?", (hit["id"],)).fetchone()
        if claim is not None:
            card["claim_payload"] = json.loads(claim[0])
        cards.append(card)
    bridge_titles = [dict(row) for row in connection.execute(
        "SELECT id,kind,title FROM nodes WHERE title LIKE ? OR title LIKE ? OR title LIKE ? LIMIT 12",
        ("%1502.03051%", "%Liggett%", "%Domination by product%"),
    )]
result = {"database": database, "read_only": True, "query": recall,
          "input_encoding": encoding,
          "cards": cards, "bounded_bridge_title_matches": bridge_titles,
          "elapsed_seconds": round(time.perf_counter() - started, 6)}
(root / "MATH_BRAIN_CARDS.json").write_text(json.dumps(result, indent=2, ensure_ascii=False), encoding="utf-8")
for card in cards:
    print(json.dumps(card, ensure_ascii=False))
print(json.dumps({"bounded_bridge_title_matches": bridge_titles, "elapsed_seconds": result["elapsed_seconds"], "input_encoding": encoding}))
