"""Read only the named source metadata and the population-store schema."""
from pathlib import Path
import json
import sqlite3

root = Path(__file__).resolve().parent
store_path = Path('~/math-brain-build/local/population/brain.sqlite3')
conn = sqlite3.connect(store_path.as_uri() + '?mode=ro', uri=True, timeout=10)
conn.execute('PRAGMA query_only=ON')
table_names = [r[0] for r in conn.execute("SELECT name FROM sqlite_master WHERE type='table' AND name IN ('nodes','claims','cards','sources')")]
result = {name: [dict(zip(('cid','name','type','notnull','default','pk'), row)) for row in conn.execute('PRAGMA table_info(' + name + ')')] for name in table_names}
conn.close()
(root / 'store_schema.json').write_text(json.dumps(result, indent=2), encoding='utf-8')
print(json.dumps(result, indent=2))
