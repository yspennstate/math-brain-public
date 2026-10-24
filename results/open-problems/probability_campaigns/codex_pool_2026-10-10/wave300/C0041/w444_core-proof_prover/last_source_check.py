import json
import sqlite3
from pathlib import Path

ROOT = Path(__file__).resolve().parent
path = Path('~/math-brain-build/local/population/brain.sqlite3')
record = {'database': str(path), 'mode': 'ro', 'candidate': 'C0041', 'matched_nodes': []}
with sqlite3.connect(path.as_uri() + '?mode=ro', uri=True, timeout=3) as conn:
    query = "SELECT id,kind,title,substr(body,1,5000),substr(metadata_json,1,1800) FROM nodes WHERE lower(title) LIKE '%transien%ballistic%' OR lower(title) LIKE '%c0041%' LIMIT 6"
    for row in conn.execute(query):
        record['matched_nodes'].append(dict(zip(['id', 'kind', 'title', 'body_excerpt', 'metadata_excerpt'], row)))
record['limit'] = 6
record['conclusion'] = 'A bounded title lookup cannot certify absence of another solved or retired owner record.'
(ROOT / 'REPORT_STORE_CHECK.json').write_text(json.dumps(record, ensure_ascii=False, indent=2), encoding='utf-8')
print(json.dumps(record, ensure_ascii=False, indent=2)[:16000])
