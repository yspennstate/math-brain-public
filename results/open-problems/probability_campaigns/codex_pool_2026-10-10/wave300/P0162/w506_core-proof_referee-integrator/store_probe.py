"""Read only the cited FEI store card and its namespace metadata."""
import json
import sqlite3

db = "file:~/math-brain-build/local/population/brain.sqlite3?mode=ro"
con = sqlite3.connect(db, uri=True)
ids = [
    "claim_d7e82bff88909352dff2f23bfcaf7a76446d6bfd14af38c5bda1d5efeb9d9c06",
    "claim_d15d0160e58b4c9183707be9f49462d2",
    "claim_06b0c09db7e28efc6febd3962e234332a00c2ba45a17792cc4d83fdbc6752fba",
]
for card_id in ids:
    row = con.execute("SELECT id,title,body,metadata_json FROM nodes WHERE id=?", (card_id,)).fetchone()
    if row is None:
        print(card_id, "MISSING")
        continue
    meta = json.loads(row[3]) if row[3] else {}
    print(json.dumps({"id": row[0], "title": row[1], "body": row[2][:1500],
                      "metadata": {k:v for k,v in meta.items() if k in
                                   ("namespace", "logical_name", "source", "source_id", "status")}},
                     ensure_ascii=False))
for row in con.execute("SELECT id,title FROM nodes WHERE id LIKE 'math:%' AND (title LIKE '%Fourier%' OR title LIKE '%Boolean%') LIMIT 12"):
    print("math_card", row[0], row[1][:120])
for prefix in ("math:combinatorics.boolean_analysis:%", "math:analysis.boolean_functions:%",
               "math:probability.boolean_functions:%"):
    count = con.execute("SELECT count(*) FROM nodes WHERE id LIKE ?", (prefix,)).fetchone()[0]
    print("namespace_count", prefix, count)
con.close()
