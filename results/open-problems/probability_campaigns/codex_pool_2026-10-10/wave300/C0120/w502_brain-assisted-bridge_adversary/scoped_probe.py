"""Read only named C0120 records and a few matching brain cards. No store writes."""
from pathlib import Path
import hashlib
import json
import re
import sqlite3
import sys
import time

ROOT = Path(__file__).resolve().parent
CODE = Path('~/<private-repo>')
INTAKE = CODE / '06_math_research/probability_1000_intake_claude_20260907'

def emit(path, data):
    (ROOT / path).write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

def records():
    out = {}
    for name, key, val in [('problems.jsonl','problem_id','C0120'),('attempts.jsonl','problem_id','C0120'),('sources.jsonl','source_id','chatterjee_chaos_2008')]:
        with (INTAKE / name).open(encoding='utf-8') as fh:
            out[name] = [json.loads(line) for line in fh if val in line and json.loads(line).get(key) == val]
    emit('intake_records.json', out)
    print(json.dumps(out, ensure_ascii=False))

def cards():
    path = Path('~/math-brain-build/export/population/nodes.jsonl')
    hits = []
    start = time.monotonic()
    # Targeted title match; keep full exact ends on disk, output summaries only.
    title_re = re.compile(r'"title": "[^"\n]*(?:superconcentration|chaos|directed polymer|fluctuation exponent)', re.I)
    with path.open(encoding='utf-8') as fh:
        for line_no, line in enumerate(fh, 1):
            if not title_re.search(line):
                continue
            row = json.loads(line)
            meta = json.loads(row.get('metadata_json','{}'))
            if 'polymer' in row.get('title','').lower() or 'superconcentration' in row.get('title','').lower():
                hits.append({'line':line_no,'id':row['id'],'title':row.get('title'),'body':row.get('body'), 'metadata':meta})
            if len(hits) >= 12:
                break
    out = {'path':str(path),'query':'title: directed polymer OR superconcentration','limit':12,'elapsed_seconds':time.monotonic()-start,'hits':hits}
    emit('brain_cards.json',out)
    print(json.dumps({'elapsed_seconds':out['elapsed_seconds'],'hits':[{'id':x['id'],'title':x['title'],'logical_id':x['metadata'].get('logical_id'),'body':(x.get('body') or '')[:2300]} for x in hits]},ensure_ascii=False))

def schema():
    path=Path('~/math-brain-build/local/population/brain.sqlite3')
    with sqlite3.connect(path.as_uri()+'?mode=ro',uri=True,timeout=2) as con:
        con.execute('PRAGMA query_only=ON')
        rows=con.execute("SELECT name,sql FROM sqlite_master WHERE type='table' AND (name LIKE '%node%' OR name LIKE '%fts%')").fetchall()
    emit('store_schema.json',{'path':str(path),'tables':rows})
    print(json.dumps(rows))

if __name__=='__main__':
    {'records':records,'cards':cards,'schema':schema}[sys.argv[1]]()
