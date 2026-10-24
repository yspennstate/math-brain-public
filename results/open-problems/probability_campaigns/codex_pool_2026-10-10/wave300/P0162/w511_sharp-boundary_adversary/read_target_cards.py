"""Read only the two identified P0162 cards with the required SQLite read-only URI."""
import json
import sqlite3
from pathlib import Path

base = Path(__file__).resolve().parent
store = "~/math-brain-build/local/population/brain.sqlite3"
identifiers = ["claim_d7e82bff88909352dff2f23bfcaf7a76446d6bfd14af38c5bda1d5efeb9d9c06",
               "claim_06b0c09db7e28efc6febd3962e234332a00c2ba45a17792cc4d83fdbc6752fba"]
titles = ["Open problem: Fourier entropy versus total influence", "Attempt on Fourier entropy versus total influence"]
conn = sqlite3.connect(f"file:{store}?mode=ro",uri=True,timeout=4)
conn.row_factory = sqlite3.Row
try:
    nodes = [dict(row) for row in conn.execute(
        "SELECT id,kind,title,body,metadata_json FROM nodes WHERE id IN (?,?) OR title IN (?,?) LIMIT 6",identifiers+titles)]
    claims = [dict(row) for row in conn.execute("SELECT id,payload_json FROM claims WHERE id IN (?,?)",identifiers)]
    result = {"mode":"ro","nodes":nodes,"claims":claims,"target_titles":titles}
    (base/"TARGET_CARDS.json").write_text(json.dumps(result,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
    for row in nodes:
        print(json.dumps({"id":row["id"],"kind":row["kind"],"title":row["title"],"body":row["body"]},ensure_ascii=False))
    print(json.dumps({"matched_nodes":len(nodes),"matched_claims":len(claims)}))
finally:
    conn.close()
