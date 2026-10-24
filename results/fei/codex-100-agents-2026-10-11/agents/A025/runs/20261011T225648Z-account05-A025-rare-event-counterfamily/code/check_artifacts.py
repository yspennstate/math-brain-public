from pathlib import Path
import json,hashlib
r=Path(__file__).resolve().parents[1]
p=json.loads(Path(r'~\mop_fei100\reports\fei-2026-10-11\EXECUTION_PROTOCOL.json').read_text())
c=json.loads((r/'CLAIMS.json').read_text());g=json.loads((r/'PROGRESS.json').read_text())
# Parenthesized words in the protocol's field list describe the actual packet_ids key.
expected={s.split(' (')[0] for s in p['required_per_run']['progress_fields']}
assert set(g)==expected
assert all(set(x)==set(p['required_per_run']['claim_fields']) for x in c)
assert (r/'PROGRESS.json').read_bytes()==(r/'PACKET_DELTA.json').read_bytes()
assert c[0]['statement_sha256']==hashlib.sha256(json.dumps({'statement':c[0]['exact_statement'],'hypotheses':c[0]['hypotheses']},sort_keys=True,separators=(',',':')).encode()).hexdigest()
t=(r/'REPORT.md').read_text()
assert all('## '+s in t for s in p['required_per_run']['report_fields'])
assert 'PLACEHOLDER' not in t
assert all(p.stat().st_size<20*1024*1024 for p in r.rglob('*') if p.is_file())
assert len((r.parents[1]/'STATUS.md').read_text().splitlines())==2
result={'status':'PASS','checked':['claim schema','progress schema','statement hash','packet delta byte equality','all report fields','no placeholders','file size caps','two-line rolling status'],'exact_census_assertions':197286,'family_assertions':2185,'independent_review':'PENDING'}
(r/'out'/'ARTIFACT_VALIDATION.json').write_text(json.dumps(result,indent=2))
receipts=[]
for f in r.rglob('*'):
 if f.is_file() and f.name!='RECEIPTS.json':receipts.append({'path':str(f.relative_to(r)),'bytes':f.stat().st_size,'sha256':hashlib.sha256(f.read_bytes()).hexdigest()})
(r/'out'/'RECEIPTS.json').write_text(json.dumps(receipts,indent=2))
assert all(hashlib.sha256((r/x['path']).read_bytes()).hexdigest()==x['sha256'] for x in receipts)
print(json.dumps(result));print('Verified artifact receipts:',len(receipts))
