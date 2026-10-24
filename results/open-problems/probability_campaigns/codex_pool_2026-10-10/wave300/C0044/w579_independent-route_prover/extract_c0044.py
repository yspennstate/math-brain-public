"""Read only exact C0044 intake rows and the two named store cards."""
import json
import sqlite3
from pathlib import Path

root = Path('~/<private-repo>/06_math_research/probability_1000_intake_claude_20260907')
out = {'intake': [], 'store': []}
for name in ['problems.jsonl', 'attempts.jsonl']:
    with (root / name).open(encoding='utf-8') as f:
        for number, line in enumerate(f, 1):
            if 'C0044' not in line:
                continue
            row = json.loads(line)
            if row.get('problem_id', row.get('id')) != 'C0044':
                continue
            out['intake'].append({'file': str(root / name), 'line': number, 'row': row})
uri = 'file:~/math-brain-build/local/population/brain.sqlite3?mode=ro'
con = sqlite3.connect(uri, uri=True)
for ident in ['claim_77b8c8b3e552560382a17be2fac6b00021e3a08ff74f780812e6f39787d2abb8', 'claim_4b1317a4c7b663b925ef6da8c356e0c7f99b89503f70b7d0d4a8e76475ed3df5']:
    row = con.execute('SELECT id,title,body,metadata_json,digest FROM nodes WHERE id=?', (ident,)).fetchone()
    if row:
        out['store'].append(dict(zip(['id', 'title', 'body', 'metadata_json', 'digest'], row)))
con.close()
dest = Path(__file__).resolve().parent / 'C0044_PRIOR_EXTRACT.json'
dest.write_text(json.dumps(out, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
for record in out['intake']:
    print(record['file'], record['line'])
    print(json.dumps(record['row'], ensure_ascii=False))
for row in out['store']:
    print('STORE', row['id'], row['digest'], row['title'])
    print(row['body'])
