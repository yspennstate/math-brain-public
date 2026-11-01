from pathlib import Path
import json,hashlib,datetime
R=Path(__file__).resolve().parents[1];A=R.parents[1]
P=json.loads(Path('~/mop_fei100/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json').read_text(encoding='utf-8'))
c=json.loads((R/'CLAIMS.json').read_text(encoding='utf-8'))[0];p=json.loads((R/'PROGRESS.json').read_text(encoding='utf-8'));r=(R/'REPORT.md').read_text(encoding='utf-8');d=(R/'DERIVATION.md').read_text(encoding='utf-8')
assert set(c)==set(P['required_per_run']['claim_fields'])
assert set(p)=={x if not x.startswith('packet_ids ') else 'packet_ids' for x in P['required_per_run']['progress_fields']}
assert c['statement_sha256']==hashlib.sha256(c['exact_statement'].encode()).hexdigest()
assert (R/'PROGRESS.json').read_bytes()==(R/'PACKET_DELTA.json').read_bytes()
assert p['packet_ids']==['A011']
for h in P['required_per_run']['report_fields']:assert '## '+h in r
assert '## Universal bridge\n' in r and not r.rstrip().split('## Universal bridge\n')[-1].strip().count('\n')
assert '41/4' in d and '37/4' not in d
assert '[(3/2)C0+1]' in d and '+2] I_g' not in d
assert len((A/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
tot=json.loads((R/'out/VALIDATION_TOTALS.json').read_text(encoding='utf-8'));assert tot['exact_assertions']==230455
assert json.loads((R/'out/FORMAL_RESULT.json').read_text(encoding='utf-8'))['formal_target_verified'] is False
sources=json.loads((R/'out/SOURCE_RECEIPTS.json').read_text(encoding='utf-8'));encodings={}
for s in sources:encodings[s.get('encoding','MISSING')]=encodings.get(s.get('encoding','MISSING'),0)+1
receipt=[]
for f in R.rglob('*'):
 if f.is_file() and f.name!='PERSISTENCE_RECEIPTS.json':
  raw=f.read_bytes();assert len(raw)<20*1024*1024
  receipt.append({'path':str(f.relative_to(R)),'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest()})
(R/'out/PERSISTENCE_RECEIPTS.json').write_text(json.dumps({'saved_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'files':receipt,'external_mirror_verified':False,'independent_review_accepted':False,'schema_checks':'PASS'},indent=2),encoding='utf-8')
print(json.dumps({'status':'FINAL_AUDIT_PASS','exact_assertions':230455,'files':len(receipt),'source_encodings':encodings,'proof_rung':'analytic proof; new independent review pending; not Lean-checked'}))
