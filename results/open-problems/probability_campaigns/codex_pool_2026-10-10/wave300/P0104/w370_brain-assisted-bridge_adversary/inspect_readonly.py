import json
from pathlib import Path
import sqlite3

ROOT = Path(__file__).resolve().parent
research = Path('~/<private-repo>/06_math_research')
for folder in sorted(research.glob('probability_1000_intake_*')):
    print(folder.name, [p.name for p in folder.iterdir() if p.is_file() and p.suffix not in {'.pdf', '.png'}][:30])
for label, path in [('population', '~/math-brain-build/local/population/brain.sqlite3'), ('mesh', '~/.agents/coordination/agent_mesh.sqlite3')]:
    con = sqlite3.connect('file:' + path + '?mode=ro', uri=True, timeout=5)
    rows = con.execute("SELECT name,sql FROM sqlite_master WHERE type='table' AND (name LIKE '%node%' OR name LIKE '%message%' OR name LIKE '%agent%' OR name LIKE '%claim%')").fetchall()
    (ROOT / (label + '_schema.json')).write_text(json.dumps(rows, indent=2), encoding='utf-8')
    print(label, [(r[0], r[1][:260]) for r in rows])
    if label == 'population':
        print('TABLES', [r[0] for r in con.execute("SELECT name FROM sqlite_master WHERE type='table'")])
    con.close()
