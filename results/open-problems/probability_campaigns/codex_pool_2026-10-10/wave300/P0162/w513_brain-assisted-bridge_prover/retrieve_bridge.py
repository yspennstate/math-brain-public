"""Bounded lexical retrieval, read-only SQLite; no model or store mutation."""
import json
import pathlib
import sqlite3
import time

root = pathlib.Path(__file__).resolve().parent
conn = sqlite3.connect('file:~/math-brain-build/local/population/brain.sqlite3?mode=ro', uri=True, timeout=5)
conn.execute('PRAGMA query_only=ON')
conn.row_factory = sqlite3.Row
queries = [
    ('target', "(lower(title) LIKE '%fourier%' AND lower(title) LIKE '%entrop%') OR lower(title) LIKE '%entropy%influence%'"),
    ('chain-rule', "lower(title) LIKE '%entropy%chain%' OR lower(title) LIKE '%chain%entropy%'"),
    ('divergence', "lower(title) LIKE '%jensen%shannon%' OR lower(title) LIKE '%hellinger%'"),
    ('entropy', "lower(title) LIKE '%shannon%' OR lower(title) LIKE '%subadditiv%entrop%'"),
]
receipt=[]
for key, where in queries:
    start=time.perf_counter()
    rows=[dict(r) for r in conn.execute('SELECT id,kind,title,body,metadata_json FROM nodes WHERE '+where+' LIMIT 6')]
    receipt.append(dict(query=key,predicate=where,limit=6,elapsed_s=time.perf_counter()-start,rows=rows))
conn.close()
(root/'brain_retrieval.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2),encoding='utf-8')
for result in receipt:
    print(json.dumps(result,ensure_ascii=False))
