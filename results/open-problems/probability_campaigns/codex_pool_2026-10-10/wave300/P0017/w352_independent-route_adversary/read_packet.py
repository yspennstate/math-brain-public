"""Read only named source tables, target rows, and worker metadata."""
import json
from pathlib import Path
import re
import sqlite3

ROOT = Path(__file__).resolve().parent
research = Path('~/<private-repo>/06_math_research')
match = re.compile(r'P0*17\b|dimension.free.{0,40}(?:log.concav|Poincar)|Kannan.Lov|\bKLS\b', re.I)
found = []
for directory in sorted(research.glob('probability_1000_intake_*')):
    for name in ('problems.jsonl', 'attempts.jsonl'):
        path = directory / name
        if not path.is_file():
            continue
        hits = 0
        with path.open(encoding='utf-8-sig', errors='replace') as stream:
            for line_number, line in enumerate(stream, 1):
                if match.search(line):
                    row = {'path': str(path), 'line': line_number, 'text': line.strip()}
                    found.append(row)
                    print(json.dumps(row, ensure_ascii=False))
                    hits += 1
                    if hits >= 3:
                        break
for path in (research/'Open problem project'/'solved_register.md', research/'Open problem project'/'solved_so_far.md'):
    if path.is_file():
        hits = []
        with path.open(encoding='utf-8-sig', errors='replace') as stream:
            for line_number, line in enumerate(stream, 1):
                if match.search(line):
                    hits.append({'line': line_number, 'text': line.strip()})
        item={'path': str(path), 'target_matches': hits}
        found.append(item)
        print(json.dumps(item, ensure_ascii=False))
(ROOT/'LOCAL_SOURCE_REPORT.json').write_text(json.dumps(found, indent=2, ensure_ascii=False), encoding='utf-8')

db = Path('~/.agents/coordination/agent_mesh.sqlite3')
if db.is_file():
    with sqlite3.connect(db.as_uri()+'?mode=ro', uri=True, timeout=3) as con:
        columns = {r[1] for r in con.execute('PRAGMA table_info(messages)')}
        print('MESH_MESSAGE_COLUMNS', sorted(columns))
        if {'sender_agent','recipient_agent','created_at','topic','body'} <= columns:
            rows=con.execute('SELECT sender_agent,recipient_agent,created_at,topic,body FROM messages WHERE recipient_agent=? ORDER BY created_at DESC LIMIT 8', ('w352',)).fetchall()
            print('MESH_READONLY', json.dumps(rows, ensure_ascii=False))

for path in (Path('~/math-brain-inbox/BUNDLE_SPEC.md'),):
    if path.is_file():
        print('BUNDLE_SPEC', path.read_text(encoding='utf-8-sig'))
for base in (Path('~/primary_directive'), Path('~/brain_workers'), Path('~/.claude/dreaming')):
    print('COMPUTE_FILE_NAMES', str(base), [p.name for p in base.iterdir() if p.is_file() and re.search('compute|govern|resource', p.name, re.I)])
