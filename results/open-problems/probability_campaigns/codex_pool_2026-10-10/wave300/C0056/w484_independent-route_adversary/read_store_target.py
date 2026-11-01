"""Read-only targeted lookup of C0056-related cards; never print a store export."""
from pathlib import Path
import json
import sqlite3

root = Path(__file__).resolve().parent
terms = ('c0056', 'anderson model', 'anderson delocal', 'extended states')
export = Path('~/math-brain-build/export/population/nodes.jsonl')
matches = []
with export.open(encoding='utf-8-sig') as handle:
    for number, line in enumerate(handle, 1):
        if not any(term in line.lower() for term in terms):
            continue
        row = json.loads(line)
        metadata = json.loads(row.get('metadata_json') or '{}')
        text = (row.get('title','')+' '+row.get('body','')).lower()
        logical = str(metadata.get('logical_id','')).lower()
        if '-c0056-' not in logical and row.get('title') != 'Anderson model (random Schrodinger operators)':
            continue
        matches.append(dict(line=number, row=row))
        if len(matches) >= 12:
            break
(root/'STORE_TARGET_ROWS.json').write_text(json.dumps(matches, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
for match in matches:
    row = match['row']
    print(json.dumps({'line':match['line'], 'fields':list(row), 'row_excerpt':json.dumps(row,ensure_ascii=False)[:1800]}, ensure_ascii=False))

for candidate in (
    '~/math-research-brain/local/population/brain.sqlite3',
    '~/math-research-brain/local/brain.sqlite3',
    '~/math-research-brain/local/math_brain.sqlite3',
    '~/math-brain-build/local/population/brain.sqlite3',
):
    path = Path(candidate)
    if not path.is_file():
        print('STORE_PATH_ABSENT', candidate)
        continue
    with sqlite3.connect(path.as_uri()+'?mode=ro', uri=True, timeout=2) as connection:
        connection.execute('PRAGMA query_only=ON')
        tables = [r[0] for r in connection.execute("SELECT name FROM sqlite_master WHERE type='table' AND name IN ('nodes','claims','sources')")]
        print('READ_ONLY_STORE', candidate, 'TABLES', tables)
        for table in tables:
            columns = [r[1] for r in connection.execute('PRAGMA table_info('+table+')')]
            print('SCHEMA', table, columns)
        if 'nodes' in tables:
            ids = [match['row']['id'] for match in matches]
            for identifier in ids:
                found = connection.execute('SELECT id,title,body,metadata_json FROM nodes WHERE id=?',(identifier,)).fetchone()
                if found:
                    print('TARGET_CARD', json.dumps({'id':found[0],'title':found[1],'body':found[2]},ensure_ascii=False))

canonical_root=Path('~/math-research-brain')
for directory in (canonical_root, canonical_root/'local'):
    for extension in ('*.sqlite3','*.sqlite','*.db'):
        paths=[p for p in directory.glob(extension) if not any(t in p.name.lower() for t in ('test','blind','answer','eval'))]
        for path in paths[:3]:
            print('CANONICAL_STORE_CANDIDATE', str(path))
