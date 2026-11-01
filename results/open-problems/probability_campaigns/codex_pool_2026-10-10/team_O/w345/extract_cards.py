"""Grep first, parse only assigned store rows, save a small local evidence set."""
import json
from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parent
IDS = ['P0342','C0057','P0024','P0218','C0005','C0065','C0090','C0143','P0019','P0048']
pattern = '(open-problem|attempt)-(' + '|'.join(i.lower() for i in IDS) + ')-'
store = '~/math-brain-build/export/population/nodes.jsonl'
r = subprocess.run(['rg','-n',pattern,store],capture_output=True,text=True,encoding='utf-8',check=False)
if r.returncode not in (0,1):
    raise RuntimeError(r.stderr)
cards=[]
for line in r.stdout.splitlines():
    number, body = line.split(':',1)
    node=json.loads(body)
    meta=json.loads(node.get('metadata_json') or '{}')
    logical=meta.get('logical_id','')
    for pid in IDS:
        if f':open-problem-{pid.lower()}-' in logical or f':attempt-{pid.lower()}-' in logical:
            cards.append({'problem_id':pid,'logical_id':logical,'kind':'attempt' if ':attempt-' in logical else 'problem','title':node['title'],'statement':node['body'],'source_id':meta.get('source_id'),'source_revision':meta.get('source_revision'),'evidence_path':store,'evidence_line':int(number)})
            break
cards.sort(key=lambda c:(IDS.index(c['problem_id']),c['kind']))
(ROOT/'cards.json').write_text(json.dumps(cards,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
for c in cards:
    print(f"{c['problem_id']} {c['kind']} {c['logical_id']}\n{c['statement']}\n")
print('ASSIGNED_CARDS',len(cards))
