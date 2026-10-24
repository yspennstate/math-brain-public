import json
import sqlite3
from pathlib import Path

root = Path(__file__).parent
db = 'file:~/math-brain-build/local/population/brain.sqlite3?mode=ro'
conn = sqlite3.connect(db, uri=True)
for name in ('bundle_001.json', 'bundle_002.json'):
    obj = json.loads((root / name).read_text(encoding='utf-8'))
    print(name, 'entries', len(obj['entries']), 'relations', len(obj['relations']))
    for entry in obj['entries']:
        logical = f'math:{entry["namespace"]}:{entry["logical_name"]}'
        rows = conn.execute('SELECT id FROM nodes WHERE metadata_json LIKE ?', (f'%{logical}%',)).fetchall()
        print(logical, 'live_nodes', len(rows))
