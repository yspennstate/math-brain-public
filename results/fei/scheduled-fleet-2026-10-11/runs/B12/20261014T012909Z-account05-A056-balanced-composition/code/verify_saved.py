from pathlib import Path
import json,hashlib
R=Path(__file__).resolve().parents[1]
protocol=Path('~/mop_fei100/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json')
rules=json.loads(protocol.read_text(encoding='utf-8-sig'))['required_per_run']
expected={s.split(' (')[0] for s in rules['progress_fields']}
progress=json.loads((R/'PROGRESS.json').read_text(encoding='utf-8'))
assert set(progress)==expected
assert (R/'PROGRESS.json').read_bytes()==(R/'PACKET_DELTA.json').read_bytes()
for c in json.loads((R/'CLAIMS.json').read_text(encoding='utf-8')):
 assert set(c)==set(rules['claim_fields'])
 serial=json.dumps({'statement':c['exact_statement'],'hypotheses':c['hypotheses']},sort_keys=True,separators=(',',':')).encode()
 assert hashlib.sha256(serial).hexdigest()==c['statement_sha256']
report=(R/'REPORT.md').read_text(encoding='utf-8')
assert all('# '+field in report for field in rules['report_fields'])
assert report.split('\n# ')[-1].startswith('Universal bridge\n')
status=(R.parents[1]/'STATUS.md').read_text(encoding='utf-8').splitlines()
assert len(status)==2 and status[0].startswith('STATE: ') and status[1].startswith('NEXT: ')
result={'schema':'ALL PASS','claim_hash':'canonical statement+hypotheses VERIFIED','packet_copy':'BYTE IDENTICAL','rolling_status':'TWO LINES','universal_bridge':'FINAL PARAGRAPH'}
(R/'out/SCHEMA_CHECK.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
checks=json.loads((R/'out/checks.json').read_text(encoding='utf-8'))
files=[]
for p in sorted(R.rglob('*')):
 if p.is_file() and p.name!='PERSISTENCE.json':
  raw=p.read_bytes();assert len(raw)<20_000_000
  files.append({'path':str(p.relative_to(R)),'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest()})
(R/'out/PERSISTENCE.json').write_text(json.dumps({'scope':'local only; mirror and downstream adoption unobserved','files':files,'checks':checks,'schema_check':result},indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
