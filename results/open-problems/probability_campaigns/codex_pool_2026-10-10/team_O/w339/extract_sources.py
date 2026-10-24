import json
import sqlite3
from pathlib import Path

ROOT = Path(__file__).resolve().parent
IDS = {'P0267','C0031','C0134','P0092','P0439','C0040','C0079','C0122','P0011','P0037'}
paths = [
    Path('~/Downloads/Probability_1000_20h_20260906'),
    Path('~/<private-repo>/06_math_research/probability_1000_intake_claude_20260907'),
]
out = []
for parent in paths:
    for name in ('problems.jsonl','attempts.jsonl','sources.jsonl'):
        path = parent / name
        if not path.exists():
            print('ABSENT', path)
            continue
        with path.open(encoding='utf-8') as f:
            for line_no, line in enumerate(f, 1):
                if any(pid in line for pid in IDS):
                    row = json.loads(line)
                    if row.get('problem_id') in IDS:
                        out.append({'file':str(path),'line':line_no,'row':row})
dbpath = Path('~/math-brain-build/local/population/brain.sqlite3')
cards = []
with sqlite3.connect(dbpath.as_uri()+'?mode=ro', uri=True, timeout=3) as db:
    for phrase in ('Endpoint energy-space', 'Randomized tree automata', 'Server provisioning', 'Brownian SIR', 'BK disjoint', 'Intrinsic-distance two-point', 'Chaos implies multiple', 'Almost-sure convergence in the heavy-tailed', 'Ballisticity criterion under', 'Absolutely continuous invariant measure for the environment'):
        rows = db.execute('SELECT id,kind,title,body,metadata_json FROM nodes WHERE title LIKE ? LIMIT 3', ('%'+phrase+'%',)).fetchall()
        for rid,kind,title,body,meta in rows:
            cards.append({'id':rid,'kind':kind,'title':title,'body':body,'metadata':json.loads(meta)})
ROOT.joinpath('source_rows.json').write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding='utf-8')
ROOT.joinpath('store_cards.json').write_text(json.dumps(cards,ensure_ascii=False,indent=2),encoding='utf-8')
for item in out:
    print(json.dumps(item,ensure_ascii=False))
print('STORE_MATCHES',len(cards))
for card in cards:
    print(json.dumps(card,ensure_ascii=False)[:2500])
