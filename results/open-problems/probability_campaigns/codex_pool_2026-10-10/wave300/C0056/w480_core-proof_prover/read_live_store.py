"""Read only the two named C0056 card IDs in the explicitly assigned population DB."""
import json
import sqlite3
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent
db_path = Path('~/math-brain-build/local/population/brain.sqlite3')
cards = json.loads((ROOT / 'sources' / 'store_c0056_cards.json').read_text(encoding='utf-8'))
ids = [r['id'] for r in cards]
receipt = {'db_path':str(db_path), 'open_mode':'read-only URI mode=ro', 'query_scope':'exact two C0056 IDs previously recovered from the assigned export', 'canonical_designation':'Assigned active population database checked; a separate canonical path under math-research-brain/local was not located in the targeted pilot directories.', 'results':[]}
start = time.monotonic()
try:
    con = sqlite3.connect('file:'+db_path.as_posix()+'?mode=ro',uri=True,timeout=3)
    con.row_factory = sqlite3.Row
    con.set_progress_handler(lambda: int(time.monotonic()-start > 8),10000)
    tables = {r['name'] for r in con.execute("SELECT name FROM sqlite_master WHERE type='table'")}
    for table in ['nodes','claims']:
        if table not in tables:
            continue
        columns = {r['name'] for r in con.execute(f'PRAGMA table_info("{table}")')}
        if 'id' not in columns:
            continue
        selected = [c for c in ['id','title','kind','body','statement','metadata_json','truth_status','status'] if c in columns]
        fields = ','.join('"'+c+'"' for c in selected)
        sql = f'SELECT {fields} FROM "{table}" WHERE id IN ({",".join("?" for _ in ids)}) LIMIT 6'
        for r in con.execute(sql,ids):
            item = dict(r)
            if 'metadata_json' in item:
                meta = json.loads(item.pop('metadata_json') or '{}')
                item['logical_id'] = meta.get('logical_id')
                item['truth_status'] = meta.get('truth_status')
                item['claim_kind'] = meta.get('claim_kind')
                item['source_id'] = meta.get('source_id')
            item['table'] = table
            receipt['results'].append(item)
    con.close()
    receipt['status'] = 'read-only exact-ID query complete'
except Exception as error:
    receipt['status'] = 'unavailable; no status certification'
    receipt['error'] = str(error)
receipt['elapsed_seconds'] = time.monotonic()-start
(ROOT / 'sources' / 'canonical_store_c0056.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'status':receipt['status'],'matches':len(receipt['results']),'db_path':str(db_path),'store_written':False}))
