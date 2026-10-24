"""Collect only named problems and their cited attempt rows; store reads are read-only."""
import json
import re
import sqlite3
from pathlib import Path

ROOT = Path(__file__).resolve().parent
BASE = Path('~/<private-repo>/06_math_research')
IDS = ['P0276','C0033','C0135','P0109','P0441','C0045','C0081','C0123','P0012','P0038']
pattern = re.compile(r'(?<![A-Za-z0-9])('+'|'.join(IDS)+r')(?![A-Za-z0-9])', re.I)
report = {p: {'ledger_rows': [], 'store_nodes': []} for p in IDS}
for directory in sorted(BASE.glob('probability_1000_intake_*')):
    for path in sorted(directory.glob('*.jsonl')):
        # Flat intake ledgers, never a bank/keys directory or a store export.
        with path.open(encoding='utf-8-sig', errors='replace') as source:
            for lineno,line in enumerate(source,1):
                matches = set(m.upper() for m in pattern.findall(line))
                if not matches:
                    continue
                try:
                    payload = json.loads(line)
                except json.JSONDecodeError:
                    payload = {'unparsed_line': line.rstrip()}
                owned = str(payload.get('problem_id', payload.get('id', ''))).upper()
                if owned and owned not in IDS:
                    continue
                for problem in matches:
                    report[problem]['ledger_rows'].append({'path': str(path), 'line': lineno, 'payload': payload})

terms = {'P0276': 'Product condition', 'C0033': 'entropy of determinantal', 'C0135': 'Running-maximum', 'P0109':'finite FPP geodesics', 'P0441': 'DelayedOff', 'C0045': 'positive velocity', 'C0081': 'Lace-expansion-free', 'C0123': 'NK fitness', 'P0012':'Gaussian tensor', 'P0038': 'Transience preserved'}
with sqlite3.connect('file:~/math-brain-build/local/population/brain.sqlite3?mode=ro',uri=True,timeout=5) as conn:
    for problem in IDS:
        rows = conn.execute('SELECT id,kind,title,body,metadata_json FROM nodes WHERE title LIKE ? LIMIT 8',('%'+terms[problem]+'%',)).fetchall()
        report[problem]['store_nodes'] = [dict(zip(['id','kind','title','body','metadata_json'], row)) for row in rows]
(ROOT/'SOURCE_REPORT.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
for problem in IDS:
    info=report[problem]
    print('\n'+problem, 'ledger_rows='+str(len(info['ledger_rows'])), 'existing_nodes='+str(len(info['store_nodes'])))
    for item in info['ledger_rows']:
        p=item['payload']
        fields={k:p[k] for k in ['id','problem_id','title','statement','source_id','source_url','source','status','attempt_id','result','obstruction','superseded_by','correction_note','reason','paper_id'] if k in p}
        print(json.dumps({'path':item['path'],'line':item['line'], **fields}, ensure_ascii=False))
    for item in info['store_nodes'][:2]:
        print(json.dumps(item,ensure_ascii=False))
