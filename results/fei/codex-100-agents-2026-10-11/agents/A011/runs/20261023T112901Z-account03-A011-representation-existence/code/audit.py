from pathlib import Path
import json,hashlib
R=Path(__file__).resolve().parents[1];A=R.parents[1]
def rd(p):return json.loads(p.read_text(encoding='utf-8'))
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
protocol=rd(Path('math-open-problems/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json'))
claims=rd(R/'CLAIMS.json');assert len(claims)==1
c=claims[0];assert set(c)==set(protocol['required_per_run']['claim_fields'])
assert sha(R/'PROGRESS.json')==sha(R/'PACKET_DELTA.json')
p=rd(R/'PROGRESS.json');assert p['packet_ids']==['A011']
assert set(p)=={x.split(' (')[0] for x in protocol['required_per_run']['progress_fields']}
assert hashlib.sha256(c['exact_statement'].encode('utf-8')).hexdigest()==c['statement_sha256']
assert c['version']==4 and not c['review_records']
report=(R/'REPORT.md').read_text(encoding='utf-8')
for field in protocol['required_per_run']['report_fields']:assert '## '+field in report
assert report.strip().split('\n\n')[-1].startswith('Universal bridge:')
assert len((A/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
v=rd(R/'out/VALIDATION_SUMMARY.json');assert v['all_validation_assertions']==4279503
assert v['main']['frontiers']==5112 and v['main']['positive_resets']==921 and v['main']['negative_resets']==4191
receipt=rd(R/'out/ARTIFACT_RECEIPTS.json')
for item in receipt['files']:
 q=Path(item['path']);q=q if q.is_absolute() else R/q
 assert q.stat().st_size==item['bytes'] and sha(q)==item['sha256'],str(q)
for q in R.rglob('*'):
 if q.is_file():assert q.stat().st_size<20_000_000,str(q)
# Additional audit source/result do not change any already verified artifact.
out={'status':'PASS','schema_claim_fields':True,'schema_progress_fields':True,'progress_delta_byte_identity':True,'statement_hash':c['statement_sha256'],'verified_prior_receipts':len(receipt['files']),'validation_assertions':v['all_validation_assertions'],'independent_review':'Still pending; no acceptance created by this audit','remote_mirror':'Not verified; supervisor handoff only','background_mathematical_jobs':'None; all finite checks completed'}
dest=R/'out/FINAL_AUDIT.json';dest.write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8',newline='')
for q in [Path(__file__).resolve(),dest]:
 receipt['files'].append({'path':str(q.relative_to(R)),'bytes':q.stat().st_size,'sha256':sha(q)})
(R/'out/ARTIFACT_RECEIPTS.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8',newline='')
print(json.dumps(out))
