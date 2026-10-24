"""Read only the named P0321 card and its attempt from the approved store."""
import json
import sqlite3
import sys
from pathlib import Path

store = Path(sys.argv[1] if len(sys.argv)>1 else '~/math-brain-build/local/population/brain.sqlite3')
db = sqlite3.connect(store.as_uri() + '?mode=ro', uri=True, timeout=2)
db.execute('PRAGMA query_only=ON')
schemas = db.execute('SELECT name, sql FROM sqlite_master WHERE type=?', ('table',)).fetchall()
selected = [(name, sql) for name, sql in schemas if name in ('nodes', 'cards', 'sources', 'claims')]
print(json.dumps(selected, indent=2))
for name, _ in selected:
    columns = [row[1] for row in db.execute('PRAGMA table_info(' + name + ')')]
    if name != 'nodes':
        continue
    if 'logical_name' in columns:
        rows = db.execute('SELECT * FROM nodes WHERE logical_name LIKE ? LIMIT 4', ('%p0321%',)).fetchall()
    elif 'metadata_json' in columns:
        rows = db.execute('SELECT * FROM nodes WHERE metadata_json LIKE ? LIMIT 4', ('%p0321%',)).fetchall()
    else:
        continue
    found=[dict(zip(columns,row)) for row in rows]
    out={'store':str(store),'read_only':True,'matched_nodes':found}
    Path('population_store_p0321.json').write_text(json.dumps(out,indent=2,ensure_ascii=False,default=str),encoding='utf-8')
    print(json.dumps({'store':str(store),'matched_node_count':len(found),'titles':[r.get('title') for r in found]},indent=2))
db.close()
