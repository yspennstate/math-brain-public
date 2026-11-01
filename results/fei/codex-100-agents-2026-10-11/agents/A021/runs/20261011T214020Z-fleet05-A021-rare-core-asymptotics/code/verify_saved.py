"""Check persisted schemas, proof section fields, validation output and receipts."""
import json, hashlib
from pathlib import Path
from datetime import datetime,timezone
run=Path(__file__).resolve().parents[1]
protocol=json.loads(Path(r'~\mop_fei100\reports\fei-2026-10-11\EXECUTION_PROTOCOL.json').read_text())
req=protocol['required_per_run']
progress=json.loads((run/'PROGRESS.json').read_text())
assert set(progress)=={f.split(' (',1)[0] for f in req['progress_fields']}
assert progress==json.loads((run/'PACKET_DELTA.json').read_text())
assert progress['packet_ids']==['A021']
for claim in json.loads((run/'CLAIMS.json').read_text()):
    assert set(claim)==set(req['claim_fields'])
    data=json.dumps({'statement':claim['exact_statement'],'hypotheses':claim['hypotheses']},sort_keys=True,separators=(',',':')).encode()
    assert claim['statement_sha256']==hashlib.sha256(data).hexdigest()
report=(run/'REPORT.md').read_text(encoding='utf-8')
for field in req['report_fields']: assert '## '+field in report
validation=json.loads((run/'out'/'validation.json').read_text())
assert validation['cases']==420 and validation['assertions_passed']==3220
artifacts=[]
for p in sorted(run.rglob('*')):
    if p.is_file() and p.name!='artifact_receipt.json':
        b=p.read_bytes(); assert len(b)<20_000_000
        artifacts.append({'path':str(p.relative_to(run)),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()})
receipt={'saved_at_utc':datetime.now(timezone.utc).isoformat(),'scope':'local files only; no independent acceptance, mirror or downstream use claimed','schemas_checked':True,'artifacts':artifacts}
(run/'out'/'artifact_receipt.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'local_artifacts':len(artifacts),'schemas_checked':True,'all_report_fields_present':True,'claims_hashes_checked':True,'validation':'420 cases, 3220 exact assertions','files_under_20_MB':True},indent=2))
