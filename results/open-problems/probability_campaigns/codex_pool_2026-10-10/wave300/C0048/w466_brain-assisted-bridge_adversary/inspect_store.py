"""Read-only schema/target lookup. Never opens or writes evaluation material."""
from pathlib import Path
import json
import sqlite3
import time

OUT = Path(__file__).resolve().parent
STORE = Path('~/math-brain-build/local/population/brain.sqlite3')
t0 = time.perf_counter()
con = sqlite3.connect(STORE.as_uri() + '?mode=ro', uri=True, timeout=3)
con.execute('PRAGMA query_only=ON')
tables = [r[0] for r in con.execute("SELECT name FROM sqlite_master WHERE type='table'")]
schema = {name: [list(r) for r in con.execute('PRAGMA table_info(' + name + ')')]
          for name in ('nodes', 'claims', 'edges') if name in tables}
data = {'store': str(STORE), 'read_only': True, 'tables': tables, 'schema': schema,
        'elapsed_seconds': time.perf_counter() - t0}
(OUT / 'store_schema.json').write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding='utf-8')
print(json.dumps(data, ensure_ascii=False))
con.row_factory = sqlite3.Row
started = time.perf_counter()
con.set_progress_handler(lambda: int(time.perf_counter() - started > 8), 10000)
rows = [dict(r) for r in con.execute("SELECT id,kind,title,body,metadata_json FROM nodes WHERE title LIKE '%Potts%' OR body LIKE '%C0048%' OR title LIKE '%Biskup%' LIMIT 30")]
(OUT / 'brain_target_nodes.json').write_text(json.dumps(rows, ensure_ascii=False, indent=2), encoding='utf-8')
print('TARGET_ROWS',len(rows))
for row in rows:
    print(json.dumps({'id':row['id'],'kind':row['kind'],'title':row['title'],'body':row['body'][:1800],'metadata_json':row['metadata_json'][:500]},ensure_ascii=False))
con.close()
