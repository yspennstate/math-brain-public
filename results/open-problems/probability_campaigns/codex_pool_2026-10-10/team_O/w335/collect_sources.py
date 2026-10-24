import json
import pathlib
import sqlite3
import subprocess

root = pathlib.Path(__file__).resolve().parent
base = pathlib.Path('~/<private-repo>/06_math_research')
ids = ['P0205', 'P0429', 'C0127', 'P0050', 'P0255', 'C0014', 'C0073', 'C0109', 'P0004', 'P0027']
folders = [base / name for name in ['probability_1000_intake_claude_20260907', 'probability_1000_intake_D_20260908', 'probability_1000_intake_E_20260908', 'probability_1000_intake_F_20260908', 'probability_1000_intake_G_20260910', 'probability_1000_intake_H_20260914', 'probability_1000_intake_I_20260914']]
records = []
for folder in folders:
    for name in ('problems.jsonl', 'attempts.jsonl'):
        path = folder / name
        if not path.is_file():
            continue
        match = subprocess.run(['rg', '-n', '-i', '|'.join(ids), str(path)], capture_output=True, text=True, encoding='utf-8', timeout=30)
        for line in match.stdout.splitlines():
            number, value = line.split(':', 1)
            row = json.loads(value)
            records.append({'file': str(path), 'line': int(number), 'record': row})
source_ids = {x['record'].get('source_id') for x in records if x['record'].get('source_id')}
for folder in folders:
    path = folder / 'sources.jsonl'
    if path.is_file() and source_ids:
        match = subprocess.run(['rg', '-n', '|'.join(sorted(source_ids)), str(path)], capture_output=True, text=True, encoding='utf-8', timeout=30)
        for line in match.stdout.splitlines():
            number, value = line.split(':', 1)
            records.append({'file': str(path), 'line': int(number), 'record': json.loads(value)})
(root / 'source_records.json').write_text(json.dumps(records, ensure_ascii=False, indent=2), encoding='utf-8')
for item in records:
    print(json.dumps(item, ensure_ascii=False))

topics = ['geometric-time Cayley', 'fork-join batch', 'multiple-peaks condition', 'free and wired forest', 'nearest-unvisited', 'log-effective resistance', 'diffusion constant', 'circular law', 'quenched connective', 'shy reflected']
connection = sqlite3.connect('file:~/math-brain-build/local/population/brain.sqlite3?mode=ro', uri=True, timeout=15)
cards = []
for topic in topics:
    for row in connection.execute("SELECT id,kind,title,substr(body,1,3500),metadata_json FROM nodes WHERE title LIKE ? AND kind NOT LIKE '%test%' AND title NOT LIKE '%test%' LIMIT 3", ('%' + topic + '%',)):
        card = dict(zip(('id','kind','title','body','metadata_json'),row))
        card['query'] = topic
        cards.append(card)
connection.close()
(root / 'baseline_cards.json').write_text(json.dumps(cards, ensure_ascii=False, indent=2), encoding='utf-8')
print('BASELINE_CARDS')
for card in cards:
    print(json.dumps(card, ensure_ascii=False))
